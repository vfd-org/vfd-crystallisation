"""Notebook 04 — combined model comparison + verdict.

Re-runs all three fits on the same dataset, produces the AIC/BIC bar
chart, and writes a single combined metrics table plus a verdict
classification per WO §11.
"""
from __future__ import annotations

import csv
import os
from typing import Dict, List

from _pipeline import DATA_PROC_DIR, FIG_DIR, TABLE_DIR, fit_to_metrics, stamp, write_csv
from src.data_loader import load_hz
from src.fitting import fit_lcdm, fit_vfd_phi_log, fit_vfd_seven_fold
from src.plotting import plot_information_criteria


def classify_verdict(rows: List[Dict[str, float]]) -> str:
    by = {r["model"]: r for r in rows}
    base = by["LCDM"]
    candidates = [r for r in rows if r["model"] != "LCDM"]
    if not candidates:
        return "INCONCLUSIVE"
    deltas = []
    for c in candidates:
        d_aic = c["aic"] - base["aic"]
        d_bic = c["bic"] - base["bic"]
        deltas.append((c["model"], d_aic, d_bic))
    best_aic = min(d[1] for d in deltas)
    best_bic = min(d[2] for d in deltas)
    if best_bic < -10:
        return "SUPPORTED"
    if best_bic < -2 and best_aic < -2:
        return "WEAKLY SUGGESTIVE"
    if best_aic < 0 < best_bic:
        return "WEAKLY SUGGESTIVE"
    if abs(best_aic) < 2 and abs(best_bic) < 2:
        return "INCONCLUSIVE"
    return "NOT SUPPORTED"


def main() -> None:
    csv_path = os.path.join(DATA_PROC_DIR, "synthetic_lcdm.csv")
    if not os.path.exists(csv_path):
        raise SystemExit("Run 01_lcdm_baseline.py first")
    z, H, sH, _src = load_hz(csv_path)

    stamp("fitting all three models")
    res_lcdm = fit_lcdm(z, H, sH)
    res_a = fit_vfd_phi_log(z, H, sH)
    res_b = fit_vfd_seven_fold(z, H, sH)

    rows = [fit_to_metrics(res_lcdm), fit_to_metrics(res_a), fit_to_metrics(res_b)]
    write_csv(os.path.join(TABLE_DIR, "model_comparison.csv"), rows)

    stamp("plotting AIC/BIC comparison")
    plot_information_criteria(
        rows,
        os.path.join(FIG_DIR, "04_information_criteria.png"),
        title="ΔAIC / ΔBIC (lower is better)",
    )

    verdict = classify_verdict(rows)
    stamp(f"verdict: {verdict}")
    for r in rows:
        print(" ", r)


if __name__ == "__main__":
    main()
