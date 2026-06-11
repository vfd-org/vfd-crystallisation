"""Notebook 01 — ΛCDM baseline.

Generates a synthetic flat-ΛCDM H(z) dataset, fits ΛCDM, plots the fit
and the residuals, and writes baseline metrics. This script also
saves the synthetic dataset for the downstream notebooks.
"""
from __future__ import annotations

import os

import numpy as np

from _pipeline import DATA_PROC_DIR, FIG_DIR, TABLE_DIR, fit_to_metrics, stamp, write_csv
from src.data_loader import make_synthetic_lcdm, write_hz
from src.fitting import fit_lcdm
from src.lcdm import H_lcdm
from src.plotting import plot_hz_with_fit, plot_residuals


def main() -> None:
    stamp("generating synthetic ΛCDM dataset")
    z, H, sH, src = make_synthetic_lcdm(n=40, sigma_frac=0.05, seed=42)
    csv_path = os.path.join(DATA_PROC_DIR, "synthetic_lcdm.csv")
    write_hz(csv_path, z, H, sH, src)
    stamp(f"wrote {csv_path}")

    stamp("fitting ΛCDM")
    res = fit_lcdm(z, H, sH)
    H_pred = H_lcdm(z, H0=res.params["H0"], omega_m=res.params["omega_m"])

    stamp("plotting")
    plot_hz_with_fit(
        z,
        H,
        sH,
        res.params,
        "LCDM",
        os.path.join(FIG_DIR, "01_lcdm_fit.png"),
        title="Synthetic data + ΛCDM fit",
    )
    plot_residuals(
        z,
        H,
        sH,
        H_pred,
        os.path.join(FIG_DIR, "01_lcdm_residuals.png"),
        title="ΛCDM residuals (synthetic)",
    )

    rows = [fit_to_metrics(res)]
    write_csv(os.path.join(TABLE_DIR, "lcdm_baseline.csv"), rows)
    stamp("done. metrics:")
    for k, v in rows[0].items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
