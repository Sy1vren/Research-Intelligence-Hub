"""Generate explicitly synthetic vibration data for pipeline smoke tests."""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("data/raw/demo_synthetic.csv"))
    parser.add_argument("--duration", type=float, default=60.0)
    parser.add_argument("--sampling-frequency", type=float, default=100.0)
    args = parser.parse_args()

    if args.duration <= 0 or args.sampling_frequency <= 0:
        raise ValueError("Duration and sampling frequency must be positive.")
    count = int(args.duration * args.sampling_frequency)
    if count < 16:
        raise ValueError("Demo must contain at least 16 samples.")

    rng = np.random.default_rng(20261115)
    time = np.arange(count, dtype=float) / args.sampling_frequency
    # Synthetic components at 1.8 Hz and 6.2 Hz plus small white noise.
    signal_value = (
        0.8 * np.sin(2 * np.pi * 1.8 * time)
        + 0.25 * np.sin(2 * np.pi * 6.2 * time)
        + 0.08 * rng.standard_normal(count)
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame({
        "time_s": time,
        "acceleration_m_s2": signal_value,
    }).to_csv(args.output, index=False)
    print(f"Synthetic demo written to: {args.output}")
    print("Reminder: these are generated values, not measured bridge data.")


if __name__ == "__main__":
    main()
