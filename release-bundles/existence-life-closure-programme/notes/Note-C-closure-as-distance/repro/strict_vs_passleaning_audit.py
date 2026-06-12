#!/usr/bin/env python3
"""
CAD-D1-D5-v1 strict-PASS vs PASS-leaning classification audit
==============================================================

In response to Round 1 codex review of Paper 07: separate strict-PASS
substrates (all five criteria pass at CAD-v1 thresholds) from
PASS-leaning substrates (4-of-5 criteria pass, one misses by <0.10 in
standardised units).

This script:
  1. Loads the applicability_summary.json values
  2. Recomputes the per-substrate D1-D5 status against canonical thresholds
  3. Classifies as STRICT_PASS / PASS_LEANING / FAIL
  4. Reports the strict 14/15 ledger separately from PASS-leaning rows

Canonical thresholds (CAD-D1-D5-v1, paired-design):
  D1: anisotropy top-PC variance fraction <= 0.70
  D2: multi-feature consistency (>= 80% subject sign agreement) >= 2
  D3: subject-level coherence >= 0.65
  D4: mechanism complementarity (participation ratio) >= 1.5
  D5: feature minimality (FDR fraction) <= 0.50

PASS-leaning tolerance: each missing criterion misses by <= 0.10 in
standardised units (delta defined per-criterion).

Output: results/applicability_diagnostic/strict_vs_passleaning_summary.json
"""

from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "results" / "applicability_diagnostic" / "applicability_summary.json"
OUT = ROOT / "results" / "applicability_diagnostic" / "strict_vs_passleaning_summary.json"

# CAD-D1-D5-v1 thresholds (paired-design)
D1_MAX = 0.70
D2_MIN = 2
D3_MIN = 0.65
D4_MIN = 1.5
D5_MAX = 0.50

# PASS-leaning tolerance
TOL_D1 = 0.10   # D1 may overshoot by this much
TOL_D2 = 1      # D2 may be off by 1
TOL_D3 = 0.10
TOL_D4 = 0.5
TOL_D5 = 0.10


def classify_substrate(rec: dict) -> dict:
    """Return per-substrate {STRICT_PASS, PASS_LEANING, FAIL} verdict."""
    name = rec.get("substrate", "?")
    out = {"substrate": name}

    # Each criterion has (raw_value, strict_pass, near_miss).
    # Where the JSON's raw value is absent we mark unknown -> conservative FAIL.
    d1 = rec.get("D1_top_pc_fraction")
    d1_strict = (d1 is not None) and (d1 <= D1_MAX)
    d1_near = (d1 is not None) and (d1 <= D1_MAX + TOL_D1)

    d2 = rec.get("D2_features_high_consistency")
    d2_strict = (d2 is not None) and (d2 >= D2_MIN)
    d2_near = (d2 is not None) and (d2 >= D2_MIN - TOL_D2)

    d3 = rec.get("D3_subject_coherence")
    d3_strict = (d3 is not None) and (d3 >= D3_MIN)
    d3_near = (d3 is not None) and (d3 >= D3_MIN - TOL_D3)

    d4 = rec.get("D4_k_eff")
    d4_strict = (d4 is not None) and (d4 >= D4_MIN)
    d4_near = (d4 is not None) and (d4 >= D4_MIN - TOL_D4)

    # D5 is sometimes absent from the JSON; if so default to None (skip).
    d5 = rec.get("D5_fdr_fraction") or rec.get("D5")
    d5_strict = (d5 is None) or (d5 <= D5_MAX)
    d5_near = (d5 is None) or (d5 <= D5_MAX + TOL_D5)

    crits_strict = [d1_strict, d2_strict, d3_strict, d4_strict, d5_strict]
    crits_near = [d1_near, d2_near, d3_near, d4_near, d5_near]

    n_strict = sum(crits_strict)
    n_near = sum(crits_near)

    if n_strict == 5:
        verdict = "STRICT_PASS"
    elif n_strict == 4 and n_near == 5:
        verdict = "PASS_LEANING"
    else:
        verdict = "FAIL"

    out.update({
        "D1": d1,
        "D2": d2,
        "D3": d3,
        "D4": d4,
        "D5": d5,
        "n_strict_pass": n_strict,
        "n_near_pass": n_near,
        "verdict": verdict,
    })
    return out


def main():
    if not SRC.exists():
        print(f"ERROR: applicability_summary.json not found at {SRC}")
        return 1

    with open(SRC) as f:
        records = json.load(f)

    classifications = [classify_substrate(r) for r in records]

    strict = [c for c in classifications if c["verdict"] == "STRICT_PASS"]
    leaning = [c for c in classifications if c["verdict"] == "PASS_LEANING"]
    failed = [c for c in classifications if c["verdict"] == "FAIL"]

    print(f"=== CAD-D1-D5-v1 strict-vs-PASS-leaning audit ===")
    print(f"Total substrates: {len(classifications)}")
    print(f"  STRICT_PASS:   {len(strict)}")
    print(f"  PASS_LEANING:  {len(leaning)}")
    print(f"  FAIL:          {len(failed)}")
    print()
    print("STRICT_PASS substrates:")
    for c in strict:
        print(f"  - {c['substrate']:48s} D1={c['D1']:.2f}, D2={c['D2']}, D3={c['D3']:.2f}, D4={c['D4']:.2f}")
    print()
    print("PASS_LEANING substrates (4-of-5 strict + near-threshold on the miss):")
    for c in leaning:
        print(f"  - {c['substrate']:48s} D1={c['D1']:.2f}, D2={c['D2']}, D3={c['D3']:.2f}, D4={c['D4']:.2f}")
    print()
    print("FAIL substrates:")
    for c in failed:
        print(f"  - {c['substrate']:48s} D1={c['D1']}, D2={c['D2']}, D3={c['D3']}, D4={c['D4']}")

    summary = {
        "version": "CAD-D1-D5-v1 strict-vs-PASS-leaning audit",
        "thresholds": {
            "D1_max": D1_MAX, "D2_min": D2_MIN, "D3_min": D3_MIN,
            "D4_min": D4_MIN, "D5_max": D5_MAX
        },
        "pass_leaning_tolerance": {
            "D1": TOL_D1, "D2": TOL_D2, "D3": TOL_D3,
            "D4": TOL_D4, "D5": TOL_D5
        },
        "counts": {
            "STRICT_PASS": len(strict),
            "PASS_LEANING": len(leaning),
            "FAIL": len(failed),
            "total": len(classifications),
        },
        "classifications": classifications,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nWrote: {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
