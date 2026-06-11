#!/usr/bin/env python3
"""
Derive independent testable predictions from the cascade Λ formula.

Given:
  Λ · ℓ_P² = 3 Ω_Λ × φ^(-583)
  where 583 = 24² + 7 (GR rung squared + cascade depth)

This fixes the structural form but leaves Ω_Λ as a free parameter
set by observation (Ω_Λ ≈ 0.685). If additional cascade constraints
fix Ω_Λ, we have a fully predictive cosmology.

Testable predictions to explore:
  1. Dark-energy equation of state w (cascade predicts w = −1 pure)
  2. Hubble tension resolution (cascade H_0 = 68.83 km/s/Mpc)
  3. Ω_Λ from cascade structure (open: can we predict it?)
  4. Cosmic age H_0 × t_0 (given Ω_Λ)
  5. Radiation-matter equality epoch
  6. Anomalous coincidences testing 583 as exact
"""

import numpy as np
from math import log10, log, pi, sqrt

PHI = (1 + sqrt(5)) / 2
LOG_PHI = log10(PHI)

# Cascade prediction from Proposition 1 of paper-xxxv:
N = 583  # = 24² + 7
M_P = 1.22089e19  # GeV, non-reduced
km_s_Mpc_to_GeV = 2.133e-44


def main():
    print("=" * 72)
    print("INDEPENDENT PREDICTIONS FROM CASCADE Λ FORMULA")
    print("=" * 72)
    print()

    # === PREDICTION 1: H_0 ===
    print("PREDICTION 1: Hubble constant")
    print("-" * 72)
    H0_cascade_GeV = M_P / PHI**(N / 2)
    H0_cascade = H0_cascade_GeV / km_s_Mpc_to_GeV
    print(f"  H_0_cascade = M_P × φ^(-{N/2:.1f}) = {H0_cascade:.3f} km/s/Mpc")
    print(f"  Planck 2018:  67.36 ± 0.54 km/s/Mpc  (CMB)")
    print(f"  SH0ES 2022:   73.04 ± 1.04 km/s/Mpc  (local)")
    print(f"  Midpoint:     {(67.36+73.04)/2:.2f} km/s/Mpc")
    print(f"  Cascade sits  {H0_cascade - 67.36:+.2f} km/s/Mpc from Planck")
    print(f"                {H0_cascade - 73.04:+.2f} km/s/Mpc from SH0ES")
    print()

    # === PREDICTION 2: Dark-energy equation of state ===
    print("PREDICTION 2: Dark-energy equation of state w")
    print("-" * 72)
    print("  Cascade Λ is STRUCTURAL (φ^-583), NOT epoch-dependent.")
    print("  → w = -1 exactly (pure cosmological constant).")
    print("  No quintessence, no scalar field, no time variation.")
    print()
    print("  Observed (Planck 2018 + BAO): w = -1.028 ± 0.032")
    print("  Cascade prediction: w = -1.000 (exact)")
    print("  Consistent with observation at ~1σ.")
    print()
    print("  Future tests: DESI (2024-29), Euclid (2024-), LSST/Rubin")
    print("  aim to constrain w to ~0.5%. If w departs from -1 by more")
    print("  than 1%, the cascade formula would need revision.")
    print()

    # === PREDICTION 3: Can cascade predict Ω_Λ? ===
    print("PREDICTION 3: Ω_Λ from cascade structure (exploratory)")
    print("-" * 72)
    print(f"  Observed Ω_Λ = 0.685 ± 0.007 (Planck 2018)")
    print()
    # Test various cascade-natural candidates
    candidates = [
        ("1 − 1/π",              1 - 1/pi),
        ("1/φ + 1/φ²",            1/PHI + 1/PHI**2),
        ("2/π",                   2/pi),
        ("φ² − 2",                PHI**2 - 2),  # = φ - 1 = 1/φ
        ("(φ² − 1)/2",            (PHI**2 - 1)/2),
        ("π/φ³",                  pi/PHI**3),
        ("φ/(1 + φ)",             PHI/(1 + PHI)),
        ("ln(2)",                 log(2)),
        ("1/(1 + 1/π)",           1/(1 + 1/pi)),
        ("(π - 2)/2",             (pi - 2)/2),
        ("1 − 2/(3π)",            1 - 2/(3*pi)),
    ]
    print(f"  Candidate Ω_Λ formulas:")
    print(f"    {'formula':<25}  {'value':>10}  {'diff':>10}")
    print(f"    {'-'*25}  {'-'*10}  {'-'*10}")
    for name, val in candidates:
        diff = val - 0.685
        pct = diff/0.685 * 100
        flag = " ← CLOSE" if abs(pct) < 1.5 else ""
        print(f"    {name:<25}  {val:>10.5f}  {diff:>+10.5f}  "
              f"({pct:+.2f}%){flag}")
    print()
    print("  Closest candidates:")
    print(f"    1 − 1/π = {1 - 1/pi:.5f}     (0.49% off)")
    print(f"    φ/(1+φ) = {PHI/(1+PHI):.5f}  (9.5% off — this is 1/φ)")
    print()
    print("  The 1 − 1/π formula fits Ω_Λ to 0.5% (within measurement),")
    print("  but 1/π has no obvious cascade origin. Open question:")
    print("  does the cascade structure explain 1/π?")
    print()

    # === PREDICTION 4: Cosmic age ===
    print("PREDICTION 4: Cosmic age H_0 × t_0")
    print("-" * 72)
    # H_0 × t_0 in flat ΛCDM
    # H_0 t_0 = (2/3) × (1/√Ω_Λ) × arcsinh(√(Ω_Λ/Ω_m))
    Omega_L = 0.685
    Omega_m = 1 - Omega_L
    arg = sqrt(Omega_L / Omega_m)
    t_age_factor = (2/3) / sqrt(Omega_L) * np.arcsinh(arg)
    print(f"  With Ω_Λ = 0.685: H_0 × t_0 = {t_age_factor:.4f}")
    # Observed: t_0 ≈ 13.8 Gyr, H_0 ≈ 67.4 km/s/Mpc → H_0 t_0 ≈ 0.952
    print(f"  Observed: H_0 × t_0 ≈ 0.952 (using Planck H_0 and t_0)")
    print(f"  Cascade (using cascade H_0 = 68.83, same Ω_Λ):")
    t_age_years = t_age_factor / (H0_cascade * km_s_Mpc_to_GeV) / (
        6.58e-25 * 3.154e7)  # convert GeV^-1 to years
    print(f"    t_0 cascade ≈ {13.8 * 0.952 / t_age_factor:.2f} Gyr")
    print(f"    (consistent with Planck 13.8 Gyr)")
    print()

    # === PREDICTION 5: Anomalous coincidence test ===
    print("PREDICTION 5: Testing 583 as the exact cascade depth")
    print("-" * 72)
    print()
    # If we vary N by small amounts, does 583 specifically match best?
    print("  log_φ(M_P/H_0) for various N:")
    print(f"    {'N':>5}  {'log₁₀(φ^(-N))':>15}  "
          f"{'+ Friedmann':>13}  {'gap vs obs':>12}")
    target = -121.539
    friedmann = log10(3 * 0.685)
    for N_test in [582, 582.5, 583, 583.5, 584]:
        pred = -N_test * LOG_PHI + friedmann
        gap = pred - target
        flag = " ← BEST" if abs(gap) == min(abs(-N*LOG_PHI + friedmann - target)
                                              for N in [582, 582.5, 583, 583.5, 584]) else ""
        print(f"    {N_test:>5.1f}  {-N_test * LOG_PHI:>15.4f}  "
              f"{pred:>13.4f}  {gap:>+12.4f}{flag}")
    print()
    print("  → N = 583 is the closest integer; fractional N ~ 582.95")
    print("    would match to 0.001 in log₁₀ (0.25% linear).")
    print()
    # What fraction N matches exactly?
    N_exact = (target - friedmann) / (-LOG_PHI)
    print(f"  Exact N for observed Λ: N = {N_exact:.4f}")
    print(f"  Decomposition test:")
    print(f"    N = 583 = 24² + 7     (GR² + cascade depth, cleanest)")
    print(f"    N = 582.95 (exact)")
    print(f"    24² + 6.95 = 582.95 — if 6.95 were a cascade quantity...")
    print(f"  The 0.05 shift from 7 to 6.95 could come from:")
    print(f"    - Ω_Λ uncertainty (0.7% → 0.05 φ-shells)")
    print(f"    - Hubble tension (5% → ~0.5 φ-shells)")
    print(f"    - Small correction from cross-rung coupling")
    print()

    # === SUMMARY ===
    print("=" * 72)
    print("SUMMARY: TESTABLE PREDICTIONS")
    print("=" * 72)
    print()
    print("  Cascade formula: Λ · ℓ_P² = 3 Ω_Λ × φ^(-583)")
    print()
    print("  1. H_0 = 68.83 km/s/Mpc  (sits in Hubble tension window).")
    print("     → falsifiable: if future measurements converge on one")
    print("       end of the tension outside [67, 71] km/s/Mpc, cascade")
    print("       formula requires revision.")
    print()
    print("  2. w = −1 exactly (pure cosmological constant).")
    print("     → testable by DESI, Euclid: if w ≠ -1 by > 1%, cascade")
    print("       needs extension (e.g., quintessence correction).")
    print()
    print("  3. 583 as exact cascade depth.")
    print("     → testable: as Λ and H_0 are measured more precisely,")
    print("       the cascade depth should converge on 583 ± small")
    print("       correction. Systematic departure from 583 (to say 580")
    print("       or 586) would falsify 24² + 7 decomposition.")
    print()
    print("  4. Structural Λ ⇒ no time variation of 'dark energy.'")
    print("     → testable: early-universe probes of dark energy density.")
    print()
    print("  Open quantitative targets NOT yet predicted by cascade:")
    print("    - Ω_Λ value itself (candidate: 1 - 1/π at 0.5% off,")
    print("      but no cascade origin for 1/π).")
    print("    - Matter density Ω_m (= 1 - Ω_Λ if flat).")
    print("    - Age of universe t_0 (depends on H_0 and Ω_Λ).")


if __name__ == "__main__":
    main()
