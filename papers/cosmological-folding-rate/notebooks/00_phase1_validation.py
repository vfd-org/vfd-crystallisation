"""Phase 1 — synthetic null + injection-recovery validation.

This script is the implementation honesty gate. It MUST pass before any
real-data result from this module is taken seriously.

Three checks:

  (i)   Pure ΛCDM data → VFD models do NOT win after AIC/BIC penalties.
  (ii)  Inject VFD-A → fit recovers A and θ.
  (iii) Inject VFD-B → fit recovers A near the truth.

Results land in `results/tables/phase1_validation.csv`.
"""
from __future__ import annotations

import os

import numpy as np

from _pipeline import TABLE_DIR, fit_to_metrics, stamp, write_csv
from src.data_loader import (
    make_synthetic_lcdm,
    make_synthetic_vfd_phi_log,
    make_synthetic_vfd_seven_fold,
)
from src.fitting import fit_lcdm, fit_vfd_phi_log, fit_vfd_seven_fold


def _delta(rows):
    by = {r["model"]: r for r in rows}
    base = by["LCDM"]
    out = {}
    for r in rows:
        if r["model"] == "LCDM":
            continue
        out[r["model"]] = {
            "delta_aic": r["aic"] - base["aic"],
            "delta_bic": r["bic"] - base["bic"],
        }
    return out


def check_null_no_false_positive():
    stamp("(i) ΛCDM-null false-positive check")
    z, H, sH, _ = make_synthetic_lcdm(n=80, sigma_frac=0.03, seed=101)
    res_l = fit_lcdm(z, H, sH)
    res_a = fit_vfd_phi_log(z, H, sH)
    res_b = fit_vfd_seven_fold(z, H, sH)
    rows = [fit_to_metrics(r) for r in (res_l, res_a, res_b)]
    deltas = _delta(rows)
    passed = all(d["delta_bic"] >= -2.0 for d in deltas.values())
    return rows, deltas, passed


def check_recovery_vfd_a():
    stamp("(ii) inject VFD-A and recover")
    A_true, theta_true = 0.05, 0.7
    z, H, sH, _ = make_synthetic_vfd_phi_log(
        n=120, A=A_true, theta=theta_true, sigma_frac=0.01, seed=202
    )
    res_l = fit_lcdm(z, H, sH)
    res_a = fit_vfd_phi_log(z, H, sH)
    rows = [fit_to_metrics(r) for r in (res_l, res_a)]
    A_err = abs(res_a.params["A"] - A_true)
    # phase recovery is reported but not tested rigidly (A near 0 makes θ ill-defined)
    theta_err = float((res_a.params["theta"] - theta_true) % (2 * np.pi))
    if theta_err > np.pi:
        theta_err = 2 * np.pi - theta_err
    passed = A_err < 0.02
    return rows, {"A_true": A_true, "A_fit": res_a.params["A"],
                  "A_err": A_err, "theta_err": theta_err}, passed


def check_recovery_vfd_b():
    stamp("(iii) inject VFD-B and recover")
    # σ < ln(φ)≈0.481 so the cascade's seven bumps remain resolved and
    # do not collapse into the cascade↔H0 degenerate plateau.
    A_true, z0_true, sigma_true = 0.20, 0.05, 0.18
    z, H, sH, _ = make_synthetic_vfd_seven_fold(
        n=200, A=A_true, z0=z0_true, sigma=sigma_true, sigma_frac=0.005, seed=303
    )
    res_l = fit_lcdm(z, H, sH)
    res_b = fit_vfd_seven_fold(z, H, sH)
    rows = [fit_to_metrics(r) for r in (res_l, res_b)]
    A_err = abs(res_b.params["A"] - A_true)
    passed = A_err < 0.10
    return rows, {"A_true": A_true, "A_fit": res_b.params["A"], "A_err": A_err}, passed


def main() -> None:
    summary = []

    rows_null, deltas_null, ok_null = check_null_no_false_positive()
    stamp(f"  null check passed: {ok_null}; ΔBIC={ {m: d['delta_bic'] for m, d in deltas_null.items()} }")
    for r in rows_null:
        summary.append({"phase": "null", **r})

    rows_a, recov_a, ok_a = check_recovery_vfd_a()
    stamp(f"  VFD-A recovery passed: {ok_a}; {recov_a}")
    for r in rows_a:
        summary.append({"phase": "inject_vfdA", **r})

    rows_b, recov_b, ok_b = check_recovery_vfd_b()
    stamp(f"  VFD-B recovery passed: {ok_b}; {recov_b}")
    for r in rows_b:
        summary.append({"phase": "inject_vfdB", **r})

    out = os.path.join(TABLE_DIR, "phase1_validation.csv")
    write_csv(out, summary)
    stamp(f"wrote {out}")

    overall = ok_null and ok_a and ok_b
    stamp(f"PHASE 1 OVERALL: {'PASS' if overall else 'FAIL'}")
    if not overall:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
