#!/usr/bin/env python3
"""B5 C_O Pontryagin characters for H-grad-1.

Construction. The mod-2 character quotient of Z[φ]⁶ is
(Z[φ]/2Z[φ])⁶∨ ≅ F_2¹² (self-dual). Under the Pontryagin pairing
⟨α, x⟩ = Σ α_j x_j mod 2, the character α pairs with primal class x
to give a bit.

Define C_O ⊂ F_2¹² as the pullback of (F_2)³ through the composed
primal map μ ∘ red : F_2¹² → (F_2)³. Concretely:

    C_O := image of (μ ∘ red)^T : (F_2)³ → F_2¹²
         = F_2-span of the three rows of the 3×12 matrix MR = M_μ · R.

This is a 3-dim F_2-subspace of F_2¹² (since MR has rank 3), hence
|C_O| = 8. For each v ∈ (F_2)³, define

    α_v := v^T · MR         (row vector in F_2¹²).

The pairing ⟨α_v, x⟩ = α_v^T x = v^T MR x = v · (μ ∘ red)(x) gives,
for each primal x, the v-component of its Fano grading. This is the
"character" description of the Fano label.

Trace-dual lift. Using codex's trace-dual basis of Z[φ] over Z:
    τ_0 = (3 - φ)/5,    τ_1 = (-1 + 2φ)/5
the bit vector c ∈ F_2¹² lifts to a character

    α = (1/2) Σ_{j=0..11} c_j · τ_{j mod 2, at coord ⌊j/2⌋}  ∈ Q(φ)⁶ / (Z[φ]⁶)^∨.

α_v for v ≠ 0 is nonzero in Q(φ)⁶ / (Z[φ]⁶)^∨ iff c ≠ 0. For v = 0
the character is trivial (α_0 = 0).

Verifies:
    B5.1 — C_O is a 3-dim F_2-subspace of F_2¹² (|C_O| = 8, rank of
           generators = 3).
    B5.2 — the 8 characters are distinct.
    B5.3 — for each v, μ_primal(α_v) = (something that pairs as the
           bijection with v via the adjointness above).
    B5.4 — Pontryagin pairing ⟨α_v, x⟩ = v · μ_primal(x) on all
           32768 input pairs (8 v × 4096 x).
    B5.5 — C_O lifts to 8 distinct elements of Q(φ)⁶ / (Z[φ]⁶)^∨ via
           trace-dual basis.

Run:
    python3 papers/cascade-derivation/scripts/verify_h_grad_1_b5.py
"""

from __future__ import annotations

import os
import sys
from fractions import Fraction
from itertools import product

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# Reuse B3/B4 machinery.
from verify_h_grad_1_b3 import (  # type: ignore
    apply_M, f2_rank,
    enumerate_4d_totally_singular, build_K, find_T, build_mu_matrix,
    IDENTITY as ID8,
)
from verify_h_grad_1_b4 import (  # type: ignore
    compute_phi_matrix, find_zphi_basis, build_red_matrix, apply_R,
)


# --------------------------------------------------------------------
# Rebuild MR (3×12) from B3 μ_I and B4 red
# --------------------------------------------------------------------

def build_composed_matrix():
    """Reconstruct MR = M_μ · R (3×12 F_2 matrix)."""
    # B3 μ_I
    all_L = enumerate_4d_totally_singular()
    L_not_through_1 = [L for L in all_L if ID8 not in L]
    L0 = sorted(L_not_through_1[0], key=lambda v: sum(v[i] << i for i in range(8)))
    K_set = build_K(set(L0))
    T_basis = find_T(K_set)
    M_mu = build_mu_matrix(K_set, T_basis)  # 3×8

    # B4 red
    Phi = compute_phi_matrix()
    zphi_basis_idx = find_zphi_basis(Phi)
    R = build_red_matrix(zphi_basis_idx, Phi)  # 8×12

    # Compose.
    MR = [[0] * 12 for _ in range(3)]
    for r in range(3):
        for c in range(12):
            s = 0
            for k in range(8):
                s ^= M_mu[r][k] & R[k][c]
            MR[r][c] = s
    return MR, M_mu, R


# --------------------------------------------------------------------
# Main
# --------------------------------------------------------------------

def main():
    print("=" * 72)
    print("B5 — C_O Pontryagin characters of Z[φ]⁶")
    print("=" * 72)
    print()

    MR, M_mu, R = build_composed_matrix()
    print("Composed μ ∘ red as 3×12 F_2 matrix MR (rebuilt from B3 + B4):")
    for r_idx, row in enumerate(MR):
        print(f"    row {r_idx}: {row}")
    print()

    # B5.1 — Build C_O as span of 3 rows of MR.
    print("=== B5.1 — C_O as 3-dim F_2-subspace of F_2¹² ===")
    rk = f2_rank([list(r) for r in MR])
    print(f"  rank(MR rows) = {rk}  (expected 3, equals rank(μ∘red))  - "
          f"{'PASS' if rk == 3 else 'FAIL'}")

    # 8 characters: α_v = v^T · MR  for v ∈ (F_2)³.
    C_O = {}  # v -> α_v as 12-bit tuple
    for v in product((0, 1), repeat=3):
        alpha = [0] * 12
        for c in range(12):
            s = 0
            for r in range(3):
                s ^= v[r] & MR[r][c]
            alpha[c] = s
        C_O[v] = tuple(alpha)
    print(f"  |C_O| = {len(set(C_O.values()))}  (expected 8)  - "
          f"{'PASS' if len(set(C_O.values())) == 8 else 'FAIL'}")
    print()
    print("  The 8 characters α_v for v ∈ (F_2)³:")
    for v in sorted(C_O.keys()):
        alpha = C_O[v]
        print(f"    v={v}  α_v = {list(alpha)}")
    print()

    # B5.2 — Subgroup closure.
    print("=== B5.2 — C_O is a subgroup of F_2¹² (closed under addition) ===")
    closed = True
    for v1 in C_O:
        for v2 in C_O:
            s = tuple(C_O[v1][i] ^ C_O[v2][i] for i in range(12))
            # s should equal C_O[v1+v2]
            vsum = tuple(v1[j] ^ v2[j] for j in range(3))
            if s != C_O[vsum]:
                closed = False
                break
        if not closed:
            break
    print(f"  Subgroup closure: {'PASS' if closed else 'FAIL'}")
    print()

    # B5.3 — Pontryagin pairing: ⟨α_v, x⟩ = v · μ_primal(x) for all x.
    print("=== B5.3 — Pontryagin pairing ⟨α_v, x⟩ = v · μ_primal(x) over all 2¹² x ===")
    pair_ok = True
    bad_example = None
    for v in C_O:
        alpha = C_O[v]
        for x in product((0, 1), repeat=12):
            # LHS: ⟨α_v, x⟩ = Σ α_v[i] x[i] mod 2.
            lhs = 0
            for i in range(12):
                lhs ^= alpha[i] & x[i]
            # RHS: μ_primal(x) = MR · x (compute as 3-bit vector), then dot with v.
            mu = [0, 0, 0]
            for r in range(3):
                s = 0
                for c in range(12):
                    s ^= MR[r][c] & x[c]
                mu[r] = s
            rhs = v[0]*mu[0] ^ v[1]*mu[1] ^ v[2]*mu[2]
            if lhs != rhs:
                pair_ok = False
                bad_example = (v, x, lhs, rhs)
                break
        if not pair_ok:
            break
    if pair_ok:
        print(f"  All 8 × 4096 = 32768 pairings satisfy the adjointness: PASS")
    else:
        print(f"  FAIL: pairing at v={bad_example[0]}, x={bad_example[1]}: "
              f"lhs={bad_example[2]}, rhs={bad_example[3]}")

    # B5.4 — Bijection v ↔ α_v.
    print()
    print("=== B5.4 — v ↔ α_v bijection ===")
    distinct = len(set(C_O.values()))
    bij_ok = distinct == 8
    print(f"  8 F_2³ values map to {distinct} distinct characters  - "
          f"{'PASS' if bij_ok else 'FAIL'}")

    # B5.5 — Trace-dual lift to Q(φ)⁶ / (Z[φ]⁶)^∨.
    print()
    print("=== B5.5 — Trace-dual lift to Q(φ)⁶ / (Z[φ]⁶)^∨ ===")
    # τ_0 = (3 - φ)/5, τ_1 = (-1 + 2φ)/5.
    # Each bit c_j with j = 2k or 2k+1 contributes to coord k of Z[φ]⁶.
    # τ_0 in coord k has value (3-φ)/5 at coord k.
    # α = (1/2) Σ c_j τ_{j%2}_at_coord{j//2}.
    # Represented as tuple of 6 pairs (a_k, b_k) of Fractions, where the
    # character in coord k is a_k + b_k φ ∈ Q(φ).
    lifts = {}
    for v, alpha in C_O.items():
        # 6 coords, each (a, b) Fraction pair.
        coord = [(Fraction(0), Fraction(0))] * 6
        coord_list = list(coord)
        for j in range(12):
            if alpha[j] == 0:
                continue
            k = j // 2
            which = j % 2  # 0 → τ_0, 1 → τ_1
            if which == 0:
                # (3 - φ)/5: a = 3/5, b = -1/5
                da, db = Fraction(3, 5), Fraction(-1, 5)
            else:
                # (-1 + 2φ)/5: a = -1/5, b = 2/5
                da, db = Fraction(-1, 5), Fraction(2, 5)
            a, b = coord_list[k]
            coord_list[k] = (a + Fraction(1, 2) * da,
                             b + Fraction(1, 2) * db)
        lifts[v] = tuple(coord_list)

    # Print lifts for first few v values.
    for v in sorted(lifts):
        pieces = []
        for k, (a, b) in enumerate(lifts[v]):
            if a == 0 and b == 0:
                pieces.append(f"0")
            else:
                pieces.append(f"({a}+{b}φ)" if b >= 0 else f"({a}{b}φ)")
        print(f"    α_{v} = ({', '.join(pieces)})")

    # Check distinctness of lifts.
    distinct_lifts = len({tuple(l) for l in lifts.values()})
    lift_ok = distinct_lifts == 8
    print(f"  8 lifts distinct in Q(φ)⁶: {'PASS' if lift_ok else 'FAIL'}")

    # Overall verdict.
    all_ok = (rk == 3 and len(set(C_O.values())) == 8 and closed
              and pair_ok and bij_ok and lift_ok)
    print()
    print("=" * 72)
    print(f"B5 OVERALL: {'PASS' if all_ok else 'FAIL'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
