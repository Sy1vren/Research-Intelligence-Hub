#!/usr/bin/env python3
"""Overlay handwriting-style text onto selected regions of an existing PDF.

Coordinates in config are PDF points from the top-left of each page.
The source PDF is never overwritten. Personal glyph images remain local.
"""
from __future__ import annotations

import argparse
import json
import math
import random
import sys
from pathlib import Path

import fitz
from PIL import Image, ImageDraw, ImageFont


def load_font(path: str | None, size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    if not path:
        raise ValueError("请在配置中填写可用的中文 TTF/OTF 字体路径。")
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(f"找不到字体文件：{p}")
    return ImageFont.truetype(str(p), size=size)


def glyph_candidates(glyph_dir: Path, char: str) -> list[Path]:
    stem = f"{ord(char):04X}"
    candidates = list(glyph_dir.glob(f"{stem}*.png"))
    return sorted(candidates)


def make_char_tile(
    char: str,
    font: ImageFont.FreeTypeFont,
    scale: float,
    rng: random.Random,
    angle_jitter: float,
    position_jitter: float,
    size_jitter: float,
    opacity: float,
    glyph_dir: Path | None,
    mode: str,
    missing_glyph: str,
) -> Image.Image:
    source = None
    if mode == "personal":
        if glyph_dir is None:
            raise ValueError("personal 模式必须设置 glyph_dir。")
        candidates = glyph_candidates(glyph_dir, char)
        if candidates:
            source = Image.open(rng.choice(candidates)).convert("RGBA")
        elif missing_glyph == "error":
            raise ValueError(f"个人字形库缺少字符“{char}”（文件名应以 {ord(char):04X} 开头）。")
        elif missing_glyph != "generic":
            raise ValueError("missing_glyph 只能是 error 或 generic。")

    if source is not None:
        bbox = source.getbbox()
        if bbox:
            source = source.crop(bbox)
        target_h = max(1, int(font.size * rng.uniform(1-size_jitter, 1+size_jitter)))
        ratio = target_h / max(1, source.height)
        target_w = max(1, int(source.width * ratio))
        tile = source.resize((target_w, target_h), Image.Resampling.LANCZOS)
    else:
        bbox = font.getbbox(char)
        w = max(2, bbox[2] - bbox[0] + 8)
        h = max(2, font.size + 10)
        tile = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        d = ImageDraw.Draw(tile)
        d.text((4 - bbox[0], 3 - bbox[1]), char, font=font, fill=(25, 22, 20, int(255 * opacity)))

    alpha = tile.getchannel("A").point(lambda a: int(a * max(0.0, min(1.0, opacity))))
    tile.putalpha(alpha)
    angle = rng.uniform(-angle_jitter, angle_jitter)
    tile = tile.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True)
    return tile


def render_box(page: fitz.Page, box: dict, cfg: dict, rng: random.Random) -> None:
    dpi = int(cfg.get("dpi", 144))
    scale = dpi / 72.0
    page_w = float(page.rect.width)
    page_h = float(page.rect.height)
    canvas = Image.new("RGBA", (math.ceil(page_w * scale), math.ceil(page_h * scale)), (0, 0, 0, 0))

    x = float(box["x"])
    y = float(box["y"])
    width = float(box["width"])
    height = float(box["height"])
    if min(x, y, width, height) < 0 or width <= 0 or height <= 0:
        raise ValueError(f"文字框坐标无效：{box}")
    if x + width > page_w or y + height > page_h:
        raise ValueError(f"文字框超出页面边界：{box}")

    mode = box.get("mode", cfg.get("default_mode", "generic"))
    if mode not in {"generic", "personal"}:
        raise ValueError(f"不支持的模式：{mode}")
    font_size_pt = float(box.get("font_size", 13))
    font = load_font(cfg.get("font_path"), max(6, round(font_size_pt * scale)))
    glyph_dir = Path(cfg.get("glyph_dir", "private_data/glyphs"))
    if not glyph_dir.is_absolute():
        glyph_dir = Path.cwd() / glyph_dir

    line_spacing = float(box.get("line_spacing", 1.5))
    char_spacing = float(box.get("char_spacing", 1.0)) * scale
    angle_jitter = float(box.get("angle_jitter", 1.0))
    position_jitter = float(box.get("position_jitter", 0.5)) * scale
    size_jitter = float(box.get("size_jitter", 0.02))
    opacity = float(box.get("ink_opacity", 0.92))
    missing = cfg.get("missing_glyph", "error")

    left, top = x * scale, y * scale
    right, bottom = (x + width) * scale, (y + height) * scale
    cursor_x, cursor_y = left, top
    line_height = font.size * line_spacing
    draw = ImageDraw.Draw(canvas)

    for char in str(box.get("text", "")):
        if char == "\n":
            cursor_x = left
            cursor_y += line_height
            continue
        tile = make_char_tile(
            char, font, scale, rng, angle_jitter, position_jitter,
            size_jitter, opacity, glyph_dir, mode, missing
        )
        if cursor_x + tile.width > right:
            cursor_x = left
            cursor_y += line_height
        if cursor_y + tile.height > bottom:
            raise ValueError(f"文字内容超出文字框；请缩小字号或扩大区域。文本框：{box}")
        dx = rng.uniform(-position_jitter, position_jitter)
        dy = rng.uniform(-position_jitter, position_jitter)
        canvas.alpha_composite(tile, (round(cursor_x + dx), round(cursor_y + dy)))
        cursor_x += tile.width + char_spacing

    png = canvas
    page.insert_image(page.rect, stream=_image_bytes(png), overlay=True)


def _image_bytes(image: Image.Image) -> bytes:
    from io import BytesIO
    buf = BytesIO()
    image.save(buf, format="PNG")
    return buf.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description="将通用或个人字形手写图层叠加到原 PDF 副本。")
    parser.add_argument("--config", required=True, help="JSON 配置文件路径")
    args = parser.parse_args()

    config_path = Path(args.config).resolve()
    cfg = json.loads(config_path.read_text(encoding="utf-8"))
    base = config_path.parent.parent
    for key in ("font_path", "glyph_dir"):
        value = cfg.get(key)
        if value and not Path(value).is_absolute():
            cfg[key] = str((base / value).resolve())
    input_pdf = Path(cfg["input_pdf"])
    output_pdf = Path(cfg["output_pdf"])
    if not input_pdf.is_absolute():
        input_pdf = base / input_pdf
    if not output_pdf.is_absolute():
        output_pdf = base / output_pdf
    if input_pdf.resolve() == output_pdf.resolve():
        raise ValueError("禁止覆盖原 PDF；请设置不同的 output_pdf。")
    if not input_pdf.is_file():
        raise FileNotFoundError(f"找不到输入 PDF：{input_pdf}")
    output_pdf.parent.mkdir(parents=True, exist_ok=True)

    rng = random.Random(cfg.get("seed"))
    doc = fitz.open(input_pdf)
    try:
        for index, box in enumerate(cfg.get("boxes", []), start=1):
            page_no = int(box["page"])
            if page_no < 0 or page_no >= len(doc):
                raise IndexError(f"第 {index} 个文字框指定了不存在的页面：{page_no}")
            render_box(doc[page_no], box, cfg, rng)
        doc.save(output_pdf, garbage=4, deflate=True)
    finally:
        doc.close()

    print(f"已生成：{output_pdf}")
    print("提醒：请逐页检查文字框位置、缺字、越界及原 PDF 内容是否完整。")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"错误：{exc}", file=sys.stderr)
        raise SystemExit(1)
