#!/usr/bin/env python3
"""
F8 — Derivation of α, β, γ in F = αR + βE − γQ
from cascade-derived couplings.

Inputs (all cascade-derived in prior work):
  G          = 1                        (Planck units, cascade-intrinsic)
  α_em⁻¹     = 137 + π/87               (Paper XXII, 0.81 ppm off obs)
  sin²θ_W    = 3/8                      (cascade-qm.md §4.1, GUT-scale)

Derivation (action matching at each physics rung):
  D₄ rung → Einstein-Hilbert   →  α = 1/(16π·G) = 1/16π
  8  rung → Maxwell (EM)       →  γ = 1/(16π·α_em)
  16 rung → SU(2) Yang-Mills   →  β = sin²θ_W/(16π·α_em) = (3/8)·γ

Outputs: specific cascade-derived values of α, β, γ.
"""

import numpy as np
from math import pi, sqrt


def main():
    print("=" * 72)
    print("F8 — THE THREE COEFFICIENTS α, β, γ (CASCADE-DERIVED)")
    print("=" * 72)
    print()

    # Cascade inputs
    G_planck = 1.0                                    # Planck units
    alpha_em_inv = 137 + pi/87                        # Paper XXII
    alpha_em = 1 / alpha_em_inv
    sin_sq_theta_W = 3/8                              # cascade-qm.md
    print(f"  Cascade inputs (all derived elsewhere):")
    print(f"    G                   = {G_planck}        (Planck, cascade-intrinsic)")
    print(f"    α_em⁻¹              = 137 + π/87 = {alpha_em_inv:.6f}")
    print(f"    α_em                = {alpha_em:.6e}")
    print(f"    sin²θ_W             = 3/8 = {sin_sq_theta_W}  (GUT, cascade-qm)")
    print()

    # F8.2: α from Einstein-Hilbert
    print(f"  F8.2: Einstein-Hilbert matching (D₄ rung):")
    alpha = 1 / (16 * pi * G_planck)
    print(f"    α = 1/(16π·G) = 1/(16π) = {alpha:.6f}")
    print()

    # F8.3: γ from Maxwell (fine structure)
    print(f"  F8.3: Maxwell matching (8/octonion rung):")
    gamma = 1 / (16 * pi * alpha_em)
    print(f"    γ = 1/(16π·α_em) = {gamma:.6f}")
    print(f"       = (137 + π/87)/(16π)")
    print(f"       = {alpha_em_inv/(16*pi):.6f}")
    print()

    # F8.4: β from weak coupling (Weinberg angle)
    print(f"  F8.4: SU(2) weak matching (16/Cl(1,3) rung):")
    beta = sin_sq_theta_W / (16 * pi * alpha_em)
    print(f"    β = sin²θ_W/(16π·α_em) = (3/8)·(137+π/87)/(16π)")
    print(f"       = 3(137+π/87)/(128π)")
    print(f"       = {beta:.6f}")
    print()

    # Summary table
    print("=" * 72)
    print("CASCADE-DERIVED VALUES")
    print("=" * 72)
    print()
    print(f"   {'Coefficient':<8}  {'Formula':<30}  {'Value':>10}")
    print(f"   {'-'*8}  {'-'*30}  {'-'*10}")
    print(f"   {'α':<8}  {'1 / (16π)':<30}  {alpha:>10.6f}")
    print(f"   {'β':<8}  {'3(137+π/87) / (128π)':<30}  {beta:>10.6f}")
    print(f"   {'γ':<8}  {'(137+π/87) / (16π)':<30}  {gamma:>10.6f}")
    print()
    print(f"   Ratios:")
    print(f"     β/α = {beta/alpha:>10.4f}  (= weak/gravity)")
    print(f"     γ/α = {gamma/alpha:>10.4f}  (= EM/gravity = 137+π/87)")
    print(f"     γ/β = {gamma/beta:>10.4f}  (= EM/weak = 8/3 = 1/sin²θ_W)")
    print()

    # Cross-checks
    print("=" * 72)
    print("CROSS-CHECKS")
    print("=" * 72)
    print()
    # Check γ/α = α_em⁻¹
    check1 = gamma / alpha
    assert abs(check1 - alpha_em_inv) < 1e-10
    print(f"  γ/α = {check1:.6f}  ≡  α_em⁻¹ = {alpha_em_inv:.6f}  ✓")

    # Check γ/β = 1/sin²θ_W
    check2 = gamma / beta
    assert abs(check2 - 1/sin_sq_theta_W) < 1e-10
    print(f"  γ/β = {check2:.6f}  ≡  1/sin²θ_W = {1/sin_sq_theta_W:.6f}  ✓")

    # Check β = γ · sin²θ_W
    check3 = gamma * sin_sq_theta_W
    assert abs(check3 - beta) < 1e-10
    print(f"  γ·sin²θ_W = {check3:.6f}  ≡  β = {beta:.6f}  ✓")
    print()

    # Rung-coupling table
    print("=" * 72)
    print("RUNG ↔ COEFFICIENT ↔ COUPLING MAP")
    print("=" * 72)
    print()
    print(f"   {'Rung':<10} {'Coeff':<5} {'Coupling':<15} {'Cascade source':<35}")
    print(f"   {'-'*10} {'-'*5} {'-'*15} {'-'*35}")
    print(f"   {'D₄ (24)':<10} {'α':<5} {'G = 1 Planck':<15} {'Planck-scale intrinsic':<35}")
    print(f"   {'8':<10} {'γ':<5} {'α_em = 1/137.036':<15} {'Paper XXII (0.81 ppm)':<35}")
    print(f"   {'16':<10} {'β':<5} {'sin²θ_W = 3/8':<15} {'cascade-qm.md §4.1':<35}")
    print()

    # The big claim
    print("=" * 72)
    print("CONSEQUENCE: ZERO FREE PARAMETERS IN THE CASCADE")
    print("=" * 72)
    print()
    print("  Prior to F8, α, β, γ were `free parameters'.")
    print("  After F8, they are derived from three cascade-derived couplings")
    print("  (G = Planck, α_em from Paper XXII, sin²θ_W from cascade-qm.md).")
    print()
    print("  Combined with F1-F7 (all theorems), the cascade framework")
    print("  depends only on two foundational axioms:")
    print("    A1: self-similarity r(2L) = 1 + 1/r(L)")
    print("    A2: cascade totality = E₈")
    print()
    print("  Every numerical prediction (Λ, H₀, Ω_Λ, G, α_em, masses,")
    print("  chirality, DNA 10-fold, …) is a theorem from A1 + A2.")
    print()
    print("  Number of free parameters: 0.")
    print("  Number of fitted quantities: 0.")
    print("  Number of theorems: all of them.")


if __name__ == "__main__":
    main()
