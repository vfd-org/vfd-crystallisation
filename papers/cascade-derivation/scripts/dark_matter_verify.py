#!/usr/bin/env python3
"""
E1 — Dark matter as σ-conjugate sector (verification).

Structural prediction: Ω_DM / Ω_baryon = |H₄'| / (|16| + |8|)
                                       = 120 / 24 = 5.
Observed: 5.33.
"""

import numpy as np
from math import sqrt

PHI = (1 + sqrt(5)) / 2


def main():
    print("=" * 72)
    print("E1 — DARK MATTER = σ-CONJUGATE H₄' SECTOR")
    print("=" * 72)
    print()

    # Root-count structural prediction
    cl13_fermions = 16   # 16/Cl(1,3) spinors = SM fermions
    octonion_gauge = 8   # 8/octonion gauge bosons (EM + weak + strong carriers)
    d4_metric = 24       # D₄ = gravity (not matter, shared between sectors)
    h4_visible = cl13_fermions + octonion_gauge  # matter-carrying rungs
    h4p_hidden = 120     # full H₄' σ-conjugate sector

    print(f"  Visible-sector matter content (our H₄):")
    print(f"    16/Cl(1,3) spinors (fermions):  {cl13_fermions}")
    print(f"    8/octonion (gauge bosons):       {octonion_gauge}")
    print(f"    D₄/metric (gravity, not matter):  {d4_metric}  [shared]")
    print(f"    Total visible matter roots:       {h4_visible}")
    print()
    print(f"  Hidden-sector (σ-conjugate H₄'):")
    print(f"    Full H₄' (all σ-images):          {h4p_hidden}")
    print()

    ratio_cascade = h4p_hidden / h4_visible
    ratio_observed = 5.33

    print(f"  Cascade prediction: Ω_DM/Ω_baryon = {h4p_hidden}/{h4_visible} = {ratio_cascade}")
    print(f"  Observed (Planck 2018):            = {ratio_observed}")
    print(f"  Gap:                                {(ratio_cascade - ratio_observed)/ratio_observed*100:+.2f}%")
    print()

    # Ω values
    Omega_L_cascade = 2/3
    Omega_matter = 1 - Omega_L_cascade
    print(f"  Cascade Ω_Λ = 2/3 = {Omega_L_cascade:.4f}")
    print(f"  Cascade Ω_m = 1/3 = {Omega_matter:.4f}")
    print()
    # Baryon fraction of matter in cascade (from ratio)
    f_baryon = 1 / (1 + ratio_cascade)
    f_DM = ratio_cascade / (1 + ratio_cascade)
    Omega_b_cascade = Omega_matter * f_baryon
    Omega_DM_cascade = Omega_matter * f_DM
    print(f"  Cascade Ω_baryon = Ω_m × 1/(1+5)  = {Omega_b_cascade:.4f}")
    print(f"  Cascade Ω_DM     = Ω_m × 5/(1+5)  = {Omega_DM_cascade:.4f}")
    print()
    print(f"  Observed Ω_baryon (Planck):        0.0486")
    print(f"  Observed Ω_DM     (Planck):        0.2589")
    print(f"  Cascade Ω_b gap: {(Omega_b_cascade - 0.0486)/0.0486*100:+.1f}%")
    print(f"  Cascade Ω_DM gap: {(Omega_DM_cascade - 0.2589)/0.2589*100:+.1f}%")
    print()

    # Other structural candidates
    print("-" * 72)
    print("  ALTERNATIVE VISIBLE-COUNT READINGS (rule out)")
    print("-" * 72)
    candidates = [
        ("16 + 8 = 24 (fermions + gauge) ⭐",  24, 120),
        ("16 (fermions only)",                 16, 120),
        ("8  (gauge only)",                     8, 120),
        ("120 (whole H₄)",                    120, 120),
        ("24+120=144 (visible+hidden total)", 144, 240),
        ("24 (= rank of D₄²)",                 24, 240),
    ]
    print(f"    {'Visible roots':<35}  {'Hidden':>6}  {'Ratio':>8}  {'vs 5.33':>8}")
    print(f"    {'-'*35}  {'-'*6}  {'-'*8}  {'-'*8}")
    for name, v, h in candidates:
        r = h / v
        gap = (r - 5.33) / 5.33 * 100
        flag = "  ⭐" if "⭐" in name else ""
        print(f"    {name:<35}  {h:>6}  {r:>8.2f}  {gap:>+7.1f}%{flag}")
    print()
    print("  Only 24:120 = 1:5 matches observed 1:5.33 within ~7%.")
    print("  All other readings fail by ≥40%.")
    print()

    # σ-mirror particle spectrum
    print("-" * 72)
    print("  σ-MIRROR PARTICLE MASS PREDICTIONS")
    print("-" * 72)
    print()
    fermions = [
        ("electron",    5.11e-4),
        ("muon",        0.1057),
        ("tau",         1.777),
        ("up quark",    2.16e-3),
        ("charm quark", 1.273),
        ("top quark",   172.76),
        ("down quark",  4.67e-3),
        ("strange",     93.4e-3),
        ("bottom",      4.18),
    ]
    print(f"    {'SM fermion':<12}  {'m [GeV]':>8}  {'σ-mirror mass':>15}")
    print(f"    {'-'*12}  {'-'*8}  {'-'*15}")
    for name, m in fermions:
        print(f"    {name:<12}  {m:>8.4g}  {m:>15.4g} (same)")
    print()
    print("  Prediction: every SM fermion has a σ-mirror with identical mass.")
    print("  Falsifiable by direct detection.")
    print()

    # Summary
    print("=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print()
    print(f"  Dark matter = σ-conjugate H₄' sector in E₈ = H₄ ⊕ H₄'.")
    print(f"  Structural ratio 24:120 = 1:5, observed 1:5.33 (+7% cosmological).")
    print(f"  DM is EM-dark, gravitationally coupled, σ-mirror of SM.")
    print(f"  Self-interacts via σ-photon with α_em' = α_em.")
    print(f"  No kinetic mixing with visible photon (falsifiable).")


if __name__ == "__main__":
    main()
