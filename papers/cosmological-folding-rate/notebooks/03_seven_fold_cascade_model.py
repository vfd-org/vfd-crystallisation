"""Notebook 03 — fit VFD-B seven-fold cascade.

Loads the synthetic dataset produced by notebook 01, fits VFD-B with
multistart, plots the fit + residuals, and writes the comparison metrics.
"""
from __future__ import annotations

import os

from _pipeline import DATA_PROC_DIR, FIG_DIR, TABLE_DIR, fit_to_metrics, stamp, write_csv
from src.data_loader import load_hz
from src.fitting import fit_lcdm, fit_vfd_seven_fold
from src.plotting import plot_hz_with_fit, plot_residuals
from src.vfd_folding import H_vfd_seven_fold


def main() -> None:
    csv_path = os.path.join(DATA_PROC_DIR, "synthetic_lcdm.csv")
    if not os.path.exists(csv_path):
        raise SystemExit("Run 01_lcdm_baseline.py first")
    z, H, sH, _src = load_hz(csv_path)

    stamp("fitting ΛCDM and VFD-B")
    res_lcdm = fit_lcdm(z, H, sH)
    res_b = fit_vfd_seven_fold(z, H, sH)

    H_pred_b = H_vfd_seven_fold(z, **res_b.params)

    stamp("plotting")
    plot_hz_with_fit(
        z,
        H,
        sH,
        res_b.params,
        "VFD-B",
        os.path.join(FIG_DIR, "03_vfdB_fit.png"),
        title="VFD-B fit (seven-fold cascade)",
    )
    plot_residuals(
        z,
        H,
        sH,
        H_pred_b,
        os.path.join(FIG_DIR, "03_vfdB_residuals.png"),
        title="VFD-B residuals",
    )

    rows = [fit_to_metrics(res_lcdm), fit_to_metrics(res_b)]
    write_csv(os.path.join(TABLE_DIR, "vfd_seven_fold_results.csv"), rows)
    stamp("done. metrics:")
    for r in rows:
        print(" ", r)


if __name__ == "__main__":
    main()
