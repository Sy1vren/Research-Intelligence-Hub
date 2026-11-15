"""Single-channel vibration time-history analysis starter.

This is a research/teaching template, not a certified structural monitoring tool.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import signal


def load_signal(path: Path, time_column: str, signal_column: str) -> tuple[np.ndarray, np.ndarray, float]:
    """Load a CSV and validate a nearly uniform, increasing time axis."""
    frame = pd.read_csv(path)
    missing = [name for name in (time_column, signal_column) if name not in frame.columns]
    if missing:
        raise ValueError(f"Missing required CSV columns: {missing}")

    time = pd.to_numeric(frame[time_column], errors="coerce").to_numpy(dtype=float)
    values = pd.to_numeric(frame[signal_column], errors="coerce").to_numpy(dtype=float)
    if time.size < 16:
        raise ValueError("At least 16 samples are required for this starter workflow.")
    if not np.isfinite(time).all() or not np.isfinite(values).all():
        raise ValueError("Time and signal columns must contain finite numeric values; handle missing data explicitly.")
    dt = np.diff(time)
    if np.any(dt <= 0):
        raise ValueError("Time values must be strictly increasing.")
    median_dt = float(np.median(dt))
    relative_jitter = float(np.max(np.abs(dt - median_dt)) / median_dt)
    if relative_jitter > 0.01:
        raise ValueError(
            f"Sampling interval varies by more than 1% (max relative deviation={relative_jitter:.4g}). "
            "Do not silently treat irregular samples as uniform; inspect or resample with a justified method."
        )
    fs = 1.0 / median_dt
    return time, values, fs


def calculate_features(values: np.ndarray, fs: float, frequencies: np.ndarray, psd: np.ndarray) -> dict:
    """Calculate transparent basic time- and frequency-domain descriptors."""
    rms = float(np.sqrt(np.mean(np.square(values))))
    peak = float(np.max(np.abs(values)))
    dominant_index = int(np.argmax(psd[1:]) + 1) if psd.size > 1 else 0
    return {
        "sample_count": int(values.size),
        "sampling_frequency_hz": float(fs),
        "duration_s": float((values.size - 1) / fs),
        "mean": float(np.mean(values)),
        "standard_deviation": float(np.std(values, ddof=1)),
        "rms": rms,
        "absolute_peak": peak,
        "peak_to_peak": float(np.ptp(values)),
        "crest_factor": float(peak / rms) if rms > 0 else None,
        "dominant_frequency_hz": float(frequencies[dominant_index]),
        "dominant_psd_value": float(psd[dominant_index]),
    }


def analyze(
    input_path: Path,
    output_dir: Path,
    time_column: str = "time_s",
    signal_column: str = "acceleration_m_s2",
    lowcut: float | None = None,
    highcut: float | None = None,
    filter_order: int = 4,
) -> dict:
    time, raw, fs = load_signal(input_path, time_column, signal_column)
    detrended = signal.detrend(raw, type="linear")
    processed = detrended.copy()
    filter_applied = False

    if (lowcut is None) != (highcut is None):
        raise ValueError("Specify both --lowcut and --highcut, or neither.")
    if lowcut is not None and highcut is not None:
        nyquist = fs / 2.0
        if not (0 < lowcut < highcut < nyquist):
            raise ValueError(f"Require 0 < lowcut < highcut < Nyquist ({nyquist:.6g} Hz).")
        if filter_order < 1:
            raise ValueError("Filter order must be a positive integer.")
        sos = signal.butter(
            filter_order, [lowcut, highcut], btype="bandpass", fs=fs, output="sos"
        )
        # Match SciPy's default SOS forward-backward padding requirement so
        # short records fail with an actionable message rather than a low-level error.
        padlen = 3 * (
            2 * len(sos) + 1
            - min(int(np.sum(sos[:, 2] == 0)), int(np.sum(sos[:, 5] == 0)))
        )
        if detrended.size <= padlen:
            raise ValueError(
                f"Signal has {detrended.size} samples, but this filter requires "
                f"more than {padlen} samples. Use a longer record or reconsider "
                "the filter order and analysis method."
            )
        processed = signal.sosfiltfilt(sos, detrended)
        filter_applied = True

    nperseg = min(processed.size, max(16, int(round(fs * 4.0))))
    frequencies, psd = signal.welch(
        processed, fs=fs, window="hann", nperseg=nperseg,
        noverlap=nperseg // 2, detrend="constant", scaling="density"
    )
    features = calculate_features(processed, fs, frequencies, psd)
    summary = {
        "input_file": str(input_path),
        "time_column": time_column,
        "signal_column": signal_column,
        "signal_unit": "user_defined; document the physical unit with the source data",
        "preprocessing": {
            "linear_detrend": True,
            "bandpass_filter_applied": filter_applied,
            "lowcut_hz": lowcut,
            "highcut_hz": highcut,
            "filter_order": filter_order if filter_applied else None,
            "filter_method": "Butterworth SOS + forward-backward filtering" if filter_applied else None,
        },
        "welch": {
            "window": "hann",
            "nperseg": int(nperseg),
            "noverlap": int(nperseg // 2),
            "frequency_resolution_approx_hz": float(fs / nperseg),
            "psd_units": "signal_unit^2/Hz",
        },
        "features": features,
        "limitations": [
            "Dominant spectral peak is not automatically a structural natural frequency.",
            "Filtering and Welch parameters affect results and must be justified for the research question.",
            "This single-channel workflow does not perform modal identification or engineering safety assessment.",
        ],
    }

    output_dir.mkdir(parents=True, exist_ok=True)
    output = pd.DataFrame({
        "time_s": time,
        "raw_signal": raw,
        "detrended_signal": detrended,
        "processed_signal": processed,
    })
    output.to_csv(output_dir / "processed_signal.csv", index=False)
    pd.DataFrame({"frequency_hz": frequencies, "psd": psd}).to_csv(
        output_dir / "power_spectral_density.csv", index=False
    )
    (output_dir / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    fig, ax = plt.subplots(figsize=(11, 4))
    ax.plot(time, raw, linewidth=0.8, alpha=0.55, label="Raw")
    ax.plot(time, processed, linewidth=0.9, label="Processed")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel(signal_column)
    ax.set_title("Vibration time history")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_dir / "time_history.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(11, 4))
    ax.semilogy(frequencies[1:], psd[1:])
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Power spectral density (signal unit²/Hz)")
    ax.set_title("Welch power spectral density")
    ax.grid(True, which="both", alpha=0.3)
    fig.tight_layout()
    fig.savefig(output_dir / "power_spectral_density.png", dpi=180)
    plt.close(fig)
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze a single-channel vibration CSV.")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output-dir", default=Path("results"), type=Path)
    parser.add_argument("--time-column", default="time_s")
    parser.add_argument("--signal-column", default="acceleration_m_s2")
    parser.add_argument("--lowcut", type=float, default=None)
    parser.add_argument("--highcut", type=float, default=None)
    parser.add_argument("--filter-order", type=int, default=4)
    args = parser.parse_args()
    summary = analyze(
        args.input, args.output_dir, args.time_column, args.signal_column,
        args.lowcut, args.highcut, args.filter_order
    )
    print(json.dumps(summary["features"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
