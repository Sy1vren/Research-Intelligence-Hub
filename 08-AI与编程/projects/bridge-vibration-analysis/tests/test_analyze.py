from pathlib import Path
import tempfile
import unittest

import numpy as np
import pandas as pd

from src.analyze import analyze, load_signal


class TestVibrationAnalysis(unittest.TestCase):
    def test_load_signal_infers_sampling_frequency(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "signal.csv"
            time = np.arange(100) / 50.0
            pd.DataFrame({"time_s": time, "acceleration_m_s2": np.sin(2*np.pi*2*time)}).to_csv(path, index=False)
            _, _, fs = load_signal(path, "time_s", "acceleration_m_s2")
            self.assertAlmostEqual(fs, 50.0, places=8)

    def test_load_signal_rejects_irregular_sampling(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "irregular.csv"
            time = np.arange(100, dtype=float) / 50.0
            time[50:] += 0.002
            pd.DataFrame({"time_s": time, "acceleration_m_s2": np.ones(100)}).to_csv(path, index=False)
            with self.assertRaises(ValueError):
                load_signal(path, "time_s", "acceleration_m_s2")

    def test_bandpass_filter_rejects_record_that_is_too_short(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            time = np.arange(16) / 100.0
            values = np.sin(2*np.pi*5*time)
            source = root / "short.csv"
            pd.DataFrame({"time_s": time, "acceleration_m_s2": values}).to_csv(source, index=False)
            with self.assertRaisesRegex(ValueError, "requires more than"):
                analyze(source, root / "results", lowcut=1.0, highcut=20.0)

    def test_pipeline_detects_synthetic_dominant_frequency(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fs = 100.0
            time = np.arange(6000) / fs
            values = np.sin(2*np.pi*2.0*time) + 0.1*np.sin(2*np.pi*8.0*time)
            source = root / "input.csv"
            pd.DataFrame({"time_s": time, "acceleration_m_s2": values}).to_csv(source, index=False)
            summary = analyze(source, root / "results")
            self.assertAlmostEqual(summary["features"]["dominant_frequency_hz"], 2.0, delta=0.3)
            self.assertTrue((root / "results" / "summary.json").exists())
            self.assertTrue((root / "results" / "time_history.png").exists())


if __name__ == "__main__":
    unittest.main()
