"""Notebook 06 — full pipeline against a user-supplied H(z) compilation.

Usage:
    PYTHONPATH=. python3 notebooks/06_real_data_run.py path/to/file.csv

The CSV must have columns z,H,sigma_H,source. The script fits ΛCDM,
VFD-A, and VFD-B; produces all figures + tables; and writes a verdict
into results/summary_report.md.
"""
from __future__ import annotations

import os
import sys

import numpy as np

from _pipeline import FIG_DIR, RESULTS_DIR, TABLE_DIR, fit_to_metrics, stamp, write_csv
from src.bootstrap import bootstrap_fit, summarise
from src.data_loader import load_hz
from src.fitting import fit_lcdm, fit_vfd_phi_log, fit_vfd_seven_fold
from src.lcdm import H_lcdm
from src.plotting import (
    plot_hz_with_fit,
    plot_information_criteria,
    plot_log_phi_residuals,
    plot_residuals,
)
from src.vfd_folding import H_vfd_phi_log, H_vfd_seven_fold


def classify_verdict(rows, bootstrap_summary):
    by = {r["model"]: r for r in rows}
    base = by["LCDM"]
    candidates = [r for r in rows if r["model"] != "LCDM"]
    deltas = [(c["model"], c["aic"] - base["aic"], c["bic"] - base["bic"]) for c in candidates]
    best_aic = min(d[1] for d in deltas)
    best_bic = min(d[2] for d in deltas)

    a_summ = bootstrap_summary.get("VFD-A:A")
    a_excludes_zero = a_summ is not None and (a_summ["p16"] > 0 or a_summ["p84"] < 0)

    if best_bic < -10 and a_excludes_zero:
        return "SUPPORTED"
    if best_bic < -2 and best_aic < -2:
        return "WEAKLY SUGGESTIVE"
    if best_aic < 0 < best_bic:
        return "WEAKLY SUGGESTIVE"
    if abs(best_aic) < 2 and abs(best_bic) < 2:
        return "INCONCLUSIVE"
    return "NOT SUPPORTED"


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("usage: 06_real_data_run.py <data.csv>")
    path = sys.argv[1]
    z, H, sH, src = load_hz(path)
    stamp(f"loaded {path} (n={len(z)}, z∈[{z.min():.3f},{z.max():.3f}])")

    res_lcdm = fit_lcdm(z, H, sH)
    res_a = fit_vfd_phi_log(z, H, sH)
    res_b = fit_vfd_seven_fold(z, H, sH)
    rows = [fit_to_metrics(r) for r in (res_lcdm, res_a, res_b)]

    H_pred_lcdm = H_lcdm(z, H0=res_lcdm.params["H0"], omega_m=res_lcdm.params["omega_m"])
    H_pred_a = H_vfd_phi_log(z, **res_a.params)
    H_pred_b = H_vfd_seven_fold(z, **res_b.params)

    plot_hz_with_fit(z, H, sH, res_lcdm.params, "LCDM",
                     os.path.join(FIG_DIR, "06_real_lcdm_fit.png"))
    plot_hz_with_fit(z, H, sH, res_a.params, "VFD-A",
                     os.path.join(FIG_DIR, "06_real_vfdA_fit.png"))
    plot_hz_with_fit(z, H, sH, res_b.params, "VFD-B",
                     os.path.join(FIG_DIR, "06_real_vfdB_fit.png"))
    plot_residuals(z, H, sH, H_pred_lcdm,
                   os.path.join(FIG_DIR, "06_real_lcdm_residuals.png"))
    plot_log_phi_residuals(z, H, sH, H_pred_lcdm,
                           os.path.join(FIG_DIR, "06_real_lcdm_residuals_phi_axis.png"))
    plot_information_criteria(rows,
                              os.path.join(FIG_DIR, "06_real_information_criteria.png"))

    write_csv(os.path.join(TABLE_DIR, "real_data_results.csv"), rows)

    stamp("running 500-sample bootstrap on VFD-A and VFD-B")
    boot_a = bootstrap_fit(fit_vfd_phi_log, z, H, sH, n_boot=500, seed=11, track=("A", "theta"))
    boot_b = bootstrap_fit(fit_vfd_seven_fold, z, H, sH, n_boot=500, seed=12, track=("A", "z0", "sigma"))
    boot_rows = []
    summary_map = {}
    for model, boot in (("VFD-A", boot_a), ("VFD-B", boot_b)):
        for param, samples in boot.items():
            if param == "failures":
                continue
            s = summarise(samples)
            summary_map[f"{model}:{param}"] = s
            boot_rows.append({"model": model, "param": param, **s})
    write_csv(os.path.join(TABLE_DIR, "real_data_bootstrap.csv"), boot_rows)

    verdict = classify_verdict(rows, summary_map)
    stamp(f"verdict: {verdict}")

    report = os.path.join(RESULTS_DIR, "summary_report.md")
    with open(report, "w") as fh:
        fh.write("# Cosmological Folding Rate — Real-Data Run\n\n")
        fh.write(f"Dataset: `{path}`  (n={len(z)})\n\n")
        fh.write("## Fits\n\n")
        fh.write("| model | params | χ² | χ²_red | AIC | BIC | ΔAIC | ΔBIC |\n")
        fh.write("|---|---:|---:|---:|---:|---:|---:|---:|\n")
        base = rows[0]
        for r in rows:
            fh.write(
                f"| {r['model']} | {r['n_params']} | {r['chi2']:.2f} | {r['chi2_red']:.3f} | "
                f"{r['aic']:.2f} | {r['bic']:.2f} | {r['aic']-base['aic']:+.2f} | "
                f"{r['bic']-base['bic']:+.2f} |\n"
            )
        fh.write("\n## Bootstrap (500 resamples)\n\n")
        fh.write("| model | param | p16 | p50 | p84 |\n|---|---|---:|---:|---:|\n")
        for br in boot_rows:
            if br["param"] == "chi2":
                continue
            fh.write(
                f"| {br['model']} | {br['param']} | {br['p16']:.4f} | "
                f"{br['p50']:.4f} | {br['p84']:.4f} |\n"
            )
        fh.write(f"\n## Verdict\n\n**{verdict}**\n\n")
        fh.write("## Notes\n\n")
        fh.write("- ΛCDM is the baseline; ΔAIC/ΔBIC are computed against it.\n")
        fh.write("- BIC penalty per parameter ≈ ln(N), heavier than AIC's 2.\n")
        fh.write("- VFD-B amplitude has a partial degeneracy with H0 when σ ≳ ln(φ).\n")
        fh.write("- A φ-supported claim requires ΔBIC < -10 *and* bootstrap A interval excluding zero.\n")
    stamp(f"wrote {report}")


if __name__ == "__main__":
    main()
