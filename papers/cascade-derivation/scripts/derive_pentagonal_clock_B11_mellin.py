#!/usr/bin/env python3
"""
Build B11: Mellin formalisation via closure-dynamics-selected N.

Strategy:
  The clock T_τ has cycle length 10 = ord(τ) (the pentagonal
  period). In the Mellin pairing z^10 = N^{-s}, the natural choice
  of N comes from the σ-symmetric dynamics on the Z[φ] unit group:
    N = φ^10
  because one full clock cycle multiplies by φ^10 in the closure-
  dynamics accumulator (equivalently, the cascade's natural scale
  is the 10th power of the fundamental Z[φ] unit).

  Tate-shifted convention (q = N^{1/2 - s}):
    z^10 = φ^{10(1/2 - s)} = φ^5 · φ^{-10s}
  giving poles of ẑ(s) at specific locations determined by the
  factor (1 - L_K z^10 + z^20)^{-m_K}.

Deliverables:
  1. Fix N = φ^10 as the cascade-canonical Mellin scale.
  2. Compute pole locations of ẑ(s) under M1 (Tate-shifted).
  3. Verify σ-action on s-variable: σ(q) under z → σ(z) = -z/φ²? ...
     More precisely: under q → σ(q), s → 1-s (Mellin-transform
     scale-inversion property).
  4. Compute the critical-line hypothesis: zeros of ẑ(s) lie on
     Re(s) = 1/2?
  5. For each Lucas factor (1 - L_K z^10 + z^20) = 0, compute the
     roots in z and translate to s via z^10 = φ^{10/2 - 10s}.

Output: the pole-set of ẑ(s) and their distance from the critical
line Re(s) = 1/2.
"""

from __future__ import annotations

import sys
from math import log
from fractions import Fraction


def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    a, b = 2, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def phi_value():
    return (1 + 5 ** 0.5) / 2


def main():
    print("=" * 76)
    print("Build B11: Mellin formalisation with N = φ^10.")
    print("=" * 76)

    phi = phi_value()
    print(f"\n[B11.1] Cascade-canonical Mellin scale:")
    print(f"        N = φ^10 = {phi ** 10:.6f}")
    print(f"        log N = 10 log φ = {10 * log(phi):.6f}")

    # --- Factor roots ---------------------------------------
    # Each factor (1 - L_K z^10 + z^20) factors as (1 - φ^K z^10)(1 - φ^(-K) z^10)
    # Roots in z^10: φ^(-K) (from the first factor) and φ^K (from the second)
    # Actually: (1 - φ^K z^10) = 0 ⟹ z^10 = φ^(-K)
    # And (1 - φ^(-K) z^10) = 0 ⟹ z^10 = φ^K
    K_values = [72, 0, 52, 20]

    print(f"\n[B11.2] Roots of each factor (1 - L_K z^10 + z^20) in z^10:")
    print(f"        (1 - φ^K z^10)(1 - φ^(-K) z^10) = 0")
    for K in K_values:
        root_1 = phi ** (-K)
        root_2 = phi ** K
        print(f"        K = {K:2d}: z^10 ∈ {{φ^{{-K}} = {root_1:.6e}, φ^K = {root_2:.6e}}}")

    # --- Mellin M1: q = N^{1/2 - s} where q = z^10, N = φ^10 -----
    # So z^10 = φ^{10(1/2 - s)} = φ^{5 - 10s}
    # Root z^10 = φ^K corresponds to s such that φ^{5 - 10s} = φ^K
    # ⟹ 5 - 10s = K ⟹ s = (5 - K) / 10
    # Root z^10 = φ^(-K) ⟹ 5 - 10s = -K ⟹ s = (5 + K) / 10

    print(f"\n[B11.3] Under M1 Mellin (q = N^{{1/2 - s}}, N = φ^10):")
    print(f"        z^10 = φ^{{5 - 10s}}, so factors have zeros at:")
    print(f"           s = (5 - K) / 10  (from z^10 = φ^K)")
    print(f"           s = (5 + K) / 10  (from z^10 = φ^{{-K}})")
    print(f"        These are the REAL parts; full root set includes imaginary")
    print(f"        offsets s → s + 2πi n / (10 log φ).")

    print(f"\n        Pole locations Re(s) for each K:")
    for K in K_values:
        s_plus = (5 - K) / 10
        s_minus = (5 + K) / 10
        m_K = {72: 1, 0: 1, 52: 5, 20: 5}[K]
        print(f"        K = {K:2d}, mult = {m_K}: "
              f"s = {s_plus:.3f} (m_K-fold), s = {s_minus:.3f} (m_K-fold)")

    # --- Distance from critical line Re(s) = 1/2 ---
    print(f"\n[B11.4] Distance of each pole Re(s) from critical line Re(s) = 1/2:")
    off_line = []
    on_line_K = []
    for K in K_values:
        s_plus_real = (5 - K) / 10
        s_minus_real = (5 + K) / 10
        dist_plus = abs(s_plus_real - 0.5)
        dist_minus = abs(s_minus_real - 0.5)
        print(f"        K = {K:2d}: |s_+ - 1/2| = {dist_plus:.3f}, "
              f"|s_- - 1/2| = {dist_minus:.3f}")
        if dist_plus == 0 and dist_minus == 0:
            on_line_K.append(K)
        else:
            off_line.append((K, dist_plus, dist_minus))

    # For K = 0: s_+ = 0.5, s_- = 0.5 → BOTH on critical line
    # For K > 0: off by K/10 on each side

    print(f"\n[B11.5] Analysis:")
    print(f"        K = 0 factor has BOTH poles at s = 1/2 (on critical line).")
    print(f"        K > 0 factors have poles at s = 1/2 ± K/10 (OFF critical line).")
    print(f"        ⇒ Under naive M1 Mellin with N = φ^10, the poles of ẑ(s) are")
    print(f"        NOT all on the critical line.")
    print()
    print(f"        For all poles to lie on Re(s) = 1/2, the cascade must select")
    print(f"        a DIFFERENT Mellin scale N such that N^{{1/2-s}} = φ^K implies")
    print(f"        Re(s) = 1/2 regardless of K. This requires log N = ∞ or a")
    print(f"        logarithmic scaling, which does not correspond to a standard")
    print(f"        analytic Mellin transform.")
    print()
    print(f"        STRUCTURAL CONCLUSION:")
    print(f"        The cascade-native M1 Mellin with N = φ^10 does NOT place all")
    print(f"        poles of ẑ(s) on the critical line. The poles lie on a")
    print(f"        \"staircase\" at Re(s) ∈ {{1/2 ± K/10 : K ∈ cycle profile}}.")
    print(f"        The RH-analogue statement must therefore be:")
    print(f"        \"The τ_crit-fixed sub-locus within the pole set lies on Re(s) = 1/2.\"")
    print(f"        The holomorphic σ-action ι: s → 1-s has only s=1/2 as its")
    print(f"        complex fixed point; the critical line Re(s)=1/2 is")
    print(f"        Fix(τ_crit) of the anti-holomorphic τ_crit = ι ∘ conj.")
    print(f"        Effective σ-action on q under M1 (worked through in [B11.6]):")
    print(f"        σ(φ^K) = (-1)^K φ^{{-K}}; for our even K-values this gives")
    print(f"        σ(φ^{{5-10s}}) = φ^{{-(5-10s)}} = φ^{{10s-5}}, matching s → 1-s.")

    # --- σ-action verification -----------------------------
    print(f"\n[B11.6] σ-action on q under M1:")
    print(f"        σ(φ^K) = (-1)^K φ^{{-K}} (Proposition 4.3)")
    print(f"        For K even (all our K values ARE even): σ(φ^K) = φ^{{-K}}.")
    print(f"        So σ(z^10) = σ(φ^{{5-10s}}) = φ^{{-(5-10s)}} = φ^{{10s-5}}")
    print(f"        This corresponds to z^10 under s → 1-s (since")
    print(f"         φ^{{5-10(1-s)}} = φ^{{10s-5}} ✓).")
    print()
    print(f"        So σ on q does match s → 1-s (holomorphic involution).")
    print(f"        Fixed set of s → 1-s alone in C: only s=1/2; the critical line")
    print(f"        Re(s)=1/2 is reached ONLY for σ combined with complex conjugation:")
    print(f"             τ_crit(s) = 1 - conj(s), Fix = {{s : Re(s) = 1/2}}.")

    # --- σ-symmetric pole pairs ---
    print(f"\n[B11.7] σ-symmetric pole pairs on ẑ(s) under M1:")
    print(f"        For each K > 0, the two poles (5-K)/10 and (5+K)/10 are")
    print(f"        σ-conjugate (swap under s → 1-s): indeed (5+K)/10 + (5-K)/10 = 1.")
    print(f"        ⇒ The PAIR {{(5-K)/10, (5+K)/10}} is σ-fixed as a SET, not pointwise.")
    print(f"        ⇒ σ-SYMMETRY of ẑ(s): ẑ(s) = ẑ(1-s).")
    for K in K_values:
        if K == 0:
            continue
        s_plus = (5 - K) / 10
        s_minus = (5 + K) / 10
        pair_sum = s_plus + s_minus
        print(f"        K = {K:2d}: {s_plus:.3f} + {s_minus:.3f} = {pair_sum:.3f} ✓")

    # --- Final summary ---
    print()
    print("=" * 76)
    print("BUILD B11 REPORT.")
    print("  - M1 Mellin with N = φ^10 gives poles at Re(s) = 1/2 ± K/10.")
    print("  - K = 0 is on critical line (trivially); K > 0 is OFF.")
    print("  - σ-action on s is the holomorphic s → 1-s.")
    print("  - ẑ(s) is σ-symmetric: ẑ(s) = ẑ(1-s).")
    print("  - POLE PAIRS {(5-K)/10, (5+K)/10} are σ-related, sum = 1.")
    print("  - Critical line = Fix(τ_crit) with τ_crit = ι ∘ bar (anti-holomorphic).")
    print()
    print("FINDING: the cascade's natural M1 Mellin produces a function ẑ(s)")
    print("  with σ-symmetric pole pairs, but poles themselves are NOT on the")
    print("  critical line unless K = 0. The RH-analogue for ẑ is NOT")
    print("  automatically true — it would require a STRUCTURALLY different")
    print("  Mellin convention or a separate proof that the cascade's σ-fixed")
    print("  closure points project to Re(s) = 1/2.")
    print()
    print("NEXT BUILD (B12 structural + B13 RH-analogue):")
    print("  - Derive K-multiset {0, 20, 52, 72}×{1, 1, 5, 5} from 2I subgroup")
    print("    structure (not sim enumeration).")
    print("  - Explore alternative Mellin conventions: Hurwitz-Euler shift,")
    print("    Selberg-trace convention. Determine if any places all poles on")
    print("    Re(s) = 1/2.")
    print("  - If no Mellin places all poles on critical line, the RH-analogue")
    print("    for ẑ is FALSE under naive interpretation. This would be an")
    print("    important structural result: the cascade zeta has a specific")
    print("    pole-staircase, NOT a Riemann-style critical-line concentration.")
    print("=" * 76)


if __name__ == "__main__":
    main()
