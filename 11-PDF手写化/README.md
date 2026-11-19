# 11 PDF 手写化：本地部署说明

本模块目标：Windows 电脑负责 PDF 处理和个人字形存储；手机通过浏览器调用电脑上的服务。当前先部署 CLI MVP，再逐步增加图形界面和手机 Web 入口。

## 一、环境准备（Windows）

建议安装：
- Windows 10/11 64 位
- Python 3.11 或 3.12（安装时勾选 Add Python to PATH）
- Git（可选，用于更新代码）
- 一款已获许可且支持中文的 TTF/OTF 手写字体

先从 GitHub 下载仓库 ZIP 并解压，进入 `11-PDF手写化` 文件夹。也可以双击 `install_windows.bat` 自动创建虚拟环境并安装依赖。\n\n手动安装时，在该文件夹打开 PowerShell：

```powershell
cd 11-PDF手写化
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

如果 PowerShell 阻止激活脚本，可在当前窗口执行：
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

安装完成后，双击 `run_windows.bat` 可运行默认配置；也可以把自定义配置路径作为参数传入。首次运行前必须先编辑配置文件。\n\n## 二、准备目录

在本模块目录下创建本地私有目录（不要上传 GitHub）：

```text
private_data/
  fonts/
  glyphs/
input/
output/
```

把自己有权使用的中文手写 TTF/OTF 放入 `private_data/fonts/`。个人字形模式使用 `private_data/glyphs/`，按字符 Unicode 十六进制命名 PNG，例如“中”是 `4E2D.png`；同一字符可增加 `4E2D_2.png`、`4E2D_3.png` 等版本。PNG 最好是透明背景、深色笔迹、四周留少量空白。

## 三、运行通用手写模式

1. 将原 PDF 复制到 `input/`。
2. 复制 `config/example.json`，另存为自己的配置文件。
3. 修改 PDF 路径、输出路径、字体路径、填写文字和文字框坐标。
4. 运行：

```powershell
python scripts/pdf_handwrite.py --config config/example.json
```

坐标单位是 PDF point（1 point = 1/72 inch），原 PDF 页面左上角为 (0, 0)。每个 box 的 x、y、width、height 都以对应页面为准。先用一页测试并检查坐标，再处理整份 PDF。

## 四、运行个人笔迹模式

在配置中将某个文本框的 `mode` 设置为 `personal`，并把 `glyph_dir` 指向本地字形目录。程序优先查找该字符的 PNG；若没有字形，按 `missing_glyph` 设置停止或回退到通用字体。个人模式初期是“真实字形库拼接”，并非完整的 AI 风格迁移模型。

## 五、手机调用规划

当前版本先完成电脑本地 CLI。手机端 Web 界面尚未交付，后续按以下方式建设：

1. Windows 上运行本地 Web 服务，文件只在电脑处理。
2. 手机和电脑连接同一可信 Wi-Fi，在手机浏览器打开电脑局域网地址。
3. Web 服务必须有访问口令、限制上传大小、只允许访问指定 input/output 目录，并在任务结束后清理临时文件。
4. 不要在路由器上直接开放端口，也不要把无认证的服务暴露到公网。
5. 需要异地访问时，优先使用 VPN/私有组网方案。

## 六、隐私与备份

- 不把个人笔迹、字形库、真实实验报告、学号、签名或扫描件提交到 GitHub。
- 原 PDF 保持只读；程序输出新文件。
- 个人字形库建议单独加密备份。
- 不使用他人笔迹或伪造签名、授权、考勤、证件和票据。

## 七、当前状态

- [x] Skill 与目录结构
- [x] PDF 叠加 CLI 初版
- [ ] Windows 安装实测
- [ ] 个人字形采集工具
- [ ] 浏览器框选 GUI
- [ ] 手机端 Web 服务
