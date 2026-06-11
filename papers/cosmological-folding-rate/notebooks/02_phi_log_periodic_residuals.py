"""Notebook 02 — fit VFD-A φ-log-periodic residuals.

Loads the synthetic dataset produced by notebook 01, fits ΛCDM and VFD-A,
plots the residuals on a φ-log axis, and writes the comparison metrics.
"""
from __future__ import annotations

import os

import numpy as np

from _pipeline import DATA_PROC_DIR, FIG_DIR, TABLE_DIR, fit_to_metrics, stamp, write_csv
from src.data_loader import load_hz
from src.fitting import fit_lcdm, fit_vfd_phi_log
from src.lcdm import H_lcdm
from src.plotting import plot_hz_with_fit, plot_log_phi_residuals, plot_residuals
from src.vfd_folding import H_vfd_phi_log


def main() -> None:
    csv_path = os.path.join(DATA_PROC_DIR, "synthetic_lcdm.csv")
    if not os.path.exists(csv_path):
        raise SystemExit("Run 01_lcdm_baseline.py first to produce synthetic_lcdm.csv")
    z, H, sH, _src = load_hz(csv_path)

    stamp("fitting ΛCDM and VFD-A")
    res_lcdm = fit_lcdm(z, H, sH)
    res_a = fit_vfd_phi_log(z, H, sH)

    H_pred_lcdm = H_lcdm(z, H0=res_lcdm.params["H0"], omega_m=res_lcdm.params["omega_m"])
    H_pred_a = H_vfd_phi_log(z, **res_a.params)

    stamp("plotting")
    plot_hz_with_fit(
        z,
        H,
        sH,
        res_a.params,
        "VFD-A",
        os.path.join(FIG_DIR, "02_vfdA_fit.png"),
        title="VFD-A fit",
    )
    plot_residuals(
        z,
        H,
        sH,
        H_pred_a,
        os.path.join(FIG_DIR, "02_vfdA_residuals.png"),
        title="VFD-A residuals",
    )
    plot_log_phi_residuals(
        z,
        H,
        sH,
        H_pred_lcdm,
        os.path.join(FIG_DIR, "02_lcdm_residuals_phi_axis.png"),
        title="ΛCDM residuals on ln(1+z)/ln φ axis",
    )

    rows = [fit_to_metrics(res_lcdm), fit_to_metrics(res_a)]
    write_csv(os.path.join(TABLE_DIR, "vfd_phi_log_results.csv"), rows)

    stamp("done. metrics:")
    for r in rows:
        print(" ", r)


if __name__ == "__main__":
    main()
