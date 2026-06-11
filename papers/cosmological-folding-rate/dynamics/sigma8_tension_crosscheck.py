"""σ₈ / S₈ tension cross-check using the same 1/12 substrate correction.

If 1/12 is a real cascade-derived correction (12 = pentagonal clock cycles
= L_12 dim), the same factor should predict the σ₈ / S₈ tension between
Planck CMB and weak-lensing surveys (KiDS-1000, DES, HSC).

Direction: structure clustering should be SUPPRESSED at late times if
boundary projection scrambles coherence — the opposite sign of H0 (which
gets ENHANCED at late times). So the prediction is:

    σ₈_late = σ₈_early · (1 − 1/12)        (suppressed)
    H0_late = H0_early · (1 + 1/12)        (enhanced)

These are *signed* predictions from the same 1/12 magnitude. Each is
independently falsifiable.

Published values:
  Planck 2018       σ₈ = 0.8111 ± 0.0060,   S₈ = 0.832 ± 0.013
  KiDS-1000         σ₈ = 0.760 ± 0.021,     S₈ = 0.759 ± 0.024
  DES Y3            σ₈ ≈ 0.776 ± 0.017,     S₈ = 0.776 ± 0.017
  HSC Y3            S₈ = 0.776 ± 0.033

Sources:
  Planck Collaboration 2020 A&A 641, A6 (arXiv:1807.06209)
  Heymans+ 2021 KiDS-1000 (arXiv:2007.15632)
  Abbott+ 2022 DES Y3 (arXiv:2105.13549)
  Sugiyama+ 2023 HSC Y3 (arXiv:2304.00705)
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import List

# Substrate constant (same as h0 script)
DIM_L12 = 12
N_CYCLES = 12
PHI = (1 + math.sqrt(5)) / 2

CORRECTION = 1.0 / DIM_L12  # = 1/12, the candidate that won the H0 screen


@dataclass(frozen=True)
class Measurement:
    name: str
    value: float
    sigma: float
    note: str


# --- σ₈ ----------------------------------------------------------------
PLANCK_S8_AMP = Measurement("Planck18 σ₈ (CMB-inferred)",  0.8111, 0.0060,
                            "early-universe-anchored")
KIDS_S8_AMP   = Measurement("KiDS-1000 σ₈ (cosmic shear)", 0.760,  0.021,
                            "weak-lensing late-time")
DES_S8_AMP    = Measurement("DES Y3 σ₈",                   0.776,  0.017,
                            "weak-lensing late-time")

# --- S₈ = σ₈ · √(Ω_m/0.3) ---------------------------------------------
PLANCK_S8 = Measurement("Planck18 S₈",  0.832, 0.013, "CMB-anchored")
KIDS_S8   = Measurement("KiDS-1000 S₈", 0.759, 0.024, "cosmic shear")
DES_S8    = Measurement("DES Y3 S₈",    0.776, 0.017, "cosmic shear")
HSC_S8    = Measurement("HSC Y3 S₈",    0.776, 0.033, "cosmic shear")


def predict_late(early: Measurement, sign: int = -1) -> float:
    """Apply (1 + sign · 1/12) to the early-anchored value."""
    return early.value * (1.0 + sign * CORRECTION)


def score(predicted: float, predicted_sigma: float, target: Measurement) -> dict:
    delta = predicted - target.value
    sigma_total = math.hypot(predicted_sigma, target.sigma)
    z = delta / sigma_total
    return {
        "target": target.name,
        "target_value": target.value,
        "target_sigma": target.sigma,
        "predicted": predicted,
        "delta": delta,
        "abs_z": abs(z),
    }


def report(label: str, early: Measurement, late_list: List[Measurement]) -> None:
    print(f"\n--- {label} ---")
    print(f"early anchor: {early.name}  =  {early.value:.4f} ± {early.sigma:.4f}")
    pred = predict_late(early, sign=-1)
    pred_sigma = early.sigma * (1.0 - CORRECTION)
    print(f"predicted late = early · (1 − 1/12)  =  {pred:.4f}  (σ_pred = {pred_sigma:.4f})")
    print()
    print(f"  {'survey':<35} {'observed':>10} {'pred-obs':>10} {'|z|':>6}")
    for m in late_list:
        r = score(pred, pred_sigma, m)
        print(f"  {m.name:<35} {r['target_value']:>10.4f} "
              f"{r['delta']:>+10.4f} {r['abs_z']:>6.2f}")
    # Null comparison
    pred_null = early.value
    print(f"\n  ΛCDM null (no correction, late=early):")
    for m in late_list:
        r = score(pred_null, early.sigma, m)
        print(f"  {m.name:<35} {r['target_value']:>10.4f} "
              f"{r['delta']:>+10.4f} {r['abs_z']:>6.2f}")


def main() -> None:
    print("=" * 70)
    print("σ₈ / S₈ tension cross-check  —  same 1/12 correction as H0")
    print("=" * 70)

    report("σ₈ amplitude", PLANCK_S8_AMP, [KIDS_S8_AMP, DES_S8_AMP])
    report("S₈ = σ₈ · √(Ω_m/0.3)", PLANCK_S8, [KIDS_S8, DES_S8, HSC_S8])

    # Positive direction (late ENHANCED) — sanity check, expected to fail
    print("\n--- sanity: late = early · (1 + 1/12)  [wrong sign for clustering] ---")
    pred_pos = predict_late(PLANCK_S8, sign=+1)
    for m in [KIDS_S8, DES_S8, HSC_S8]:
        r = score(pred_pos, PLANCK_S8.sigma * (1 + CORRECTION), m)
        print(f"  {m.name:<35} {r['target_value']:>10.4f} "
              f"{r['delta']:>+10.4f} {r['abs_z']:>6.2f}")


if __name__ == "__main__":
    main()
