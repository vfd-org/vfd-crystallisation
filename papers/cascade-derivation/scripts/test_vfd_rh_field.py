#!/usr/bin/env python3
"""
Test the VFD-RH field Ψ(s) from `VFD Math/RH Solution/New Proofs/`.

The VFD-RH framework defines:
    Ψ(s) = ∑_{n=2}^∞ φ^(-n) A_n sin(ω_n t + φ_n(s))
with A_n = 1/√n (Weil-explicit-formula weighting), ω_n = log(n),
φ_n(s) = arg(1 - n^(-s)).

(Note: original validation scripts start at n=1, but log(1)=0 causes
A_n = 1/log(1) division-by-zero. We start at n=2 which is the
mathematically natural lower bound. We use 1/√n weighting consistent
with the cascade work this session — it matches the cascade Hecke-
operator weight used in T_E(s) for BSD.)

Theorem A (Energy Minimization, claimed in rh-energy-proof.md):
    E(σ) = ∫|Ψ(σ+it)|² dt globally minimized at σ=1/2.
Theorem B (Phase Coherence, claimed in rh-phase-proof.md):
    Phase bounded ≤ K log t at σ=1/2; exponentially decoheres elsewhere.
Theorem C (Zero Correspondence, claimed in rh-zero-proof.md):
    Ψ(s) = 0 ⟺ ζ(s) = 0 in the critical strip.

This script tests the empirical claims:
1. Is |Ψ(0.5 + iγ_n)| << |Ψ(σ + iγ_n)| for σ ≠ 0.5 at known γ_n?
2. Is the energy ∑|Ψ(σ + it_k)|² minimized at σ = 0.5?
3. Is phase evolution bounded at σ = 0.5?

If the empirical answers are YES for all three, the VFD-RH framework
has empirical support; the proofs in the .md files become candidates
for formal verification.

Uses mpmath at moderate precision for performance.
"""

from __future__ import annotations

import sys
from mpmath import mp, mpf, mpc, sqrt, log, sin, arg, power, im


def vfd_field(s, max_terms=200, A_form='inv_sqrt'):
    """Compute Ψ(s) = Σ_{n=2}^max_terms φ^(-n) A_n sin(ω_n t + φ_n(s))."""
    phi = (1 + sqrt(5)) / 2
    field = mpc(0)
    scale = mp.mpf(1)
    t = im(s)
    for n in range(2, max_terms + 1):
        scale = power(phi, -n)
        if A_form == 'inv_sqrt':
            A_n = 1 / sqrt(n)
        elif A_form == 'inv_log':
            A_n = 1 / log(n)
        else:
            A_n = mpf(1)
        omega_n = log(n)
        # phase φ_n(s) = arg(1 - n^(-s))
        n_to_minus_s = power(n, -s)
        one_minus = 1 - n_to_minus_s
        phase = arg(one_minus)
        term = scale * A_n * sin(omega_n * t + phase)
        field += term
        if abs(term) < mp.mpf('1e-50'):
            break
    return field


def main():
    mp.dps = 50  # 50 digit precision for speed
    phi_val = float((1 + mp.sqrt(5)) / 2)

    print("=" * 76)
    print("VFD-RH field Ψ(s) empirical validation test")
    print("Tests Theorems A, B, C from VFD Math/RH Solution/New Proofs/")
    print("Precision: 50 decimal digits, max_terms=200, n starting at 2")
    print(f"φ = {phi_val:.15f}")
    print("=" * 76)

    # First 6 known Riemann ζ-zero imaginary parts
    known_zeros = [
        14.134725141734693,
        21.022039638771554,
        25.010857580145688,
        30.424876125859513,
        37.586178158825671,
        49.773832477672302,
    ]

    # Test Theorem C / critical-line concentration
    print(f"\n[Test 1] |Ψ(σ + iγ_n)| at known ζ-zeros for σ ∈ {{0.4, 0.5, 0.6}}:")
    print(f"  If the VFD field captures ζ-zeros, we expect |Ψ(0.5+iγ_n)| << |Ψ(0.4+iγ_n)|.")
    print(f"\n  γ_n        |Ψ(0.4+iγ)|     |Ψ(0.5+iγ)|     |Ψ(0.6+iγ)|     ratio")
    for gamma in known_zeros:
        s_lo = mpc(mpf("0.4"), mpf(gamma))
        s_cr = mpc(mpf("0.5"), mpf(gamma))
        s_hi = mpc(mpf("0.6"), mpf(gamma))
        psi_lo = abs(vfd_field(s_lo))
        psi_cr = abs(vfd_field(s_cr))
        psi_hi = abs(vfd_field(s_hi))
        ratio = float(psi_cr / max(psi_lo, psi_hi)) if max(psi_lo, psi_hi) > 0 else float('inf')
        print(f"  {gamma:8.4f}   {float(psi_lo):.6e}   {float(psi_cr):.6e}   "
              f"{float(psi_hi):.6e}   {ratio:.4f}")

    # Test Theorem A / energy minimization at σ = 1/2
    print(f"\n[Test 2] Energy E(σ) = Σ |Ψ(σ + it_k)|² for σ ∈ [0.3, 0.7]:")
    print(f"  Sampling at t = γ_1, γ_2, γ_3, γ_4, γ_5, γ_6 (the 6 zeros above).")
    sigmas = [0.3, 0.4, 0.45, 0.5, 0.55, 0.6, 0.7]
    print(f"\n  σ        E(σ)")
    for sigma in sigmas:
        energy = mpf(0)
        for gamma in known_zeros:
            s = mpc(mpf(sigma), mpf(gamma))
            field = vfd_field(s)
            energy += abs(field) ** 2
        print(f"  {sigma:.2f}    {float(energy):.6e}")

    # Test Theorem B / phase coherence at σ = 0.5
    print(f"\n[Test 3] Phase difference Δθ = |arg(Ψ(0.5+i(t+0.1))) - arg(Ψ(0.5+it))|:")
    print(f"  If phase coherent at σ=0.5, expect bounded Δθ over t ∈ [10, 50].")
    t_values = [10.0, 14.13, 20.0, 25.01, 30.0, 37.59, 40.0, 49.77, 50.0]
    print(f"\n  t        |Δθ at σ=0.5|     |Δθ at σ=0.4| (off-line)")
    for t in t_values:
        s1_cr = mpc(mpf("0.5"), mpf(t))
        s2_cr = mpc(mpf("0.5"), mpf(t + 0.1))
        s1_off = mpc(mpf("0.4"), mpf(t))
        s2_off = mpc(mpf("0.4"), mpf(t + 0.1))
        d_cr = abs(arg(vfd_field(s2_cr)) - arg(vfd_field(s1_cr)))
        d_off = abs(arg(vfd_field(s2_off)) - arg(vfd_field(s1_off)))
        print(f"  {t:6.2f}    {float(d_cr):.6e}      {float(d_off):.6e}")

    print()
    print("=" * 76)
    print("Verification summary:")
    print("  Test 1: does |Ψ(0.5+iγ_n)| concentrate near zero relative to off-line?")
    print("  Test 2: is E(σ) minimized at σ = 0.5?")
    print("  Test 3: is phase Δθ bounded at σ = 0.5 vs growing off-line?")
    print()
    print("  If YES on all three: empirical evidence supports Theorems A, B, C")
    print("  (ie the VFD field has its zeros aligned with classical ζ-zeros on")
    print("  the critical line).")
    print()
    print("  If NO: the VFD field as currently defined doesn't match ζ-zeros,")
    print("  and the proofs in rh-{energy,phase,zero}-proof.md have wrong")
    print("  starting hypotheses (or the formula needs adjustment).")
    print("=" * 76)


if __name__ == "__main__":
    main()
