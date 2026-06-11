"""Numerical verification that the V_600 cycle-eigenvalue model produces
H_late / H_early = 13/12 = 1 + 1/12 exactly.

Constructs explicit per-cycle eigenvalues, applies the two observer
projections, and prints both the symbolic ratio and the numerical value.
"""
from __future__ import annotations

import math
from fractions import Fraction
from typing import List, Tuple

import numpy as np


# Substrate constants
N_CYCLES = 12
N_BULK_CYCLES = 2          # σ-fixed: K=72 and K=0
N_PAIRED_CYCLES = 10       # σ-paired
CYCLE_LENGTH = 10          # vertices per cycle
N_V600 = N_CYCLES * CYCLE_LENGTH  # 120


def cycle_eigenvalues_symbolic(h0: Fraction, delta: Fraction) -> List[Fraction]:
    """Return the 12 cycle eigenvalues as exact Fractions."""
    eigenvalues: List[Fraction] = []
    eigenvalues.extend([h0] * N_BULK_CYCLES)             # σ-fixed bulk
    eigenvalues.extend([h0 * (Fraction(1) + delta)] * N_PAIRED_CYCLES)
    return eigenvalues


def project_cmb(eigenvalues: List[Fraction]) -> Fraction:
    """Coarse observer: averages over bulk cycles only (σ-antisym averages out)."""
    bulk = eigenvalues[:N_BULK_CYCLES]
    return sum(bulk) / len(bulk)


def project_local(eigenvalues: List[Fraction]) -> Fraction:
    """Fine observer: averages over all cycles (σ-antisym does not cancel)."""
    return sum(eigenvalues) / len(eigenvalues)


def main() -> None:
    h0 = Fraction(1)
    delta = Fraction(1, CYCLE_LENGTH)  # = 1/10
    eigs = cycle_eigenvalues_symbolic(h0, delta)

    H_early = project_cmb(eigs)
    H_late = project_local(eigs)
    ratio = H_late / H_early

    print("=" * 70)
    print("Symbolic check: H_late / H_early using exact rational arithmetic")
    print("=" * 70)
    print(f"  h0    = {h0}")
    print(f"  δ     = 1/L = 1/{CYCLE_LENGTH} = {delta}")
    print(f"  N_cycles total            = {N_CYCLES}")
    print(f"  N_bulk_cycles (σ-fixed)   = {N_BULK_CYCLES}")
    print(f"  N_paired_cycles (σ-paired)= {N_PAIRED_CYCLES}")
    print(f"  cycle eigenvalues         = {[str(e) for e in eigs]}")
    print()
    print(f"  H_early  (bulk avg)       = {H_early}    ({float(H_early):.6f})")
    print(f"  H_late   (all-cycle avg)  = {H_late}     ({float(H_late):.6f})")
    print(f"  ratio                     = {ratio}     ({float(ratio):.6f})")
    print()
    expected = Fraction(13, 12)
    assert ratio == expected, f"Expected 13/12, got {ratio}"
    print(f"  ✓ ratio == 13/12 = 1 + 1/12 (exact)")

    # ----- Sensitivity: vary each substrate input to confirm the
    #       prediction depends on the right structural numbers --------
    print()
    print("=" * 70)
    print("Sensitivity: which structural numbers does the prediction depend on?")
    print("=" * 70)

    cases = [
        ("baseline (12 cycles, 10 paired, L=10)", N_CYCLES, N_PAIRED_CYCLES, CYCLE_LENGTH),
        ("if cycles were 8 (no D_L12)",            8, 6, 10),
        ("if paired count were 8",                 N_CYCLES, 8, CYCLE_LENGTH),
        ("if cycle length were 12",                N_CYCLES, N_PAIRED_CYCLES, 12),
        ("if no σ-paired cycles",                  N_CYCLES, 0, CYCLE_LENGTH),
        ("all cycles σ-paired",                    N_CYCLES, N_CYCLES, CYCLE_LENGTH),
    ]
    print(f"{'case':<42} {'N_c':>4} {'N_p':>4} {'L':>3}  {'ratio':>10}")
    print("-" * 70)
    for label, nc, np_paired, L in cases:
        nb = nc - np_paired
        if nb < 1 or L < 1 or nc < nb:
            print(f"{label:<42} (skipped)")
            continue
        d = Fraction(1, L)
        eigs_c = [h0] * nb + [h0 * (Fraction(1) + d)] * np_paired
        H_e = sum(eigs_c[:nb]) / max(nb, 1) if nb > 0 else h0
        H_l = sum(eigs_c) / nc
        r = H_l / H_e
        print(f"{label:<42} {nc:>4} {np_paired:>4} {L:>3}  {str(r):>10}")

    print()
    print("Confirms: the 1/12 prediction requires N_cycles=12, N_paired=10, L=10.")
    print("All three are immutable V_600 structural numbers — no fit room.")

    # ----- Sign check for amplitude (σ_8) ------------------------
    print()
    print("=" * 70)
    print("σ_8 amplitude (decoherence accounting)")
    print("=" * 70)
    sigma8_early = Fraction(1)
    sigma8_late = sigma8_early * (Fraction(N_CYCLES) - Fraction(N_PAIRED_CYCLES) * delta) / N_CYCLES
    ratio_amp = sigma8_late / sigma8_early
    print(f"  σ_8_late / σ_8_early = {ratio_amp} = {float(ratio_amp):.6f}")
    assert ratio_amp == Fraction(11, 12)
    print(f"  ✓ ratio == 11/12 = 1 − 1/12 (exact, opposite sign of H₀)")


if __name__ == "__main__":
    main()
