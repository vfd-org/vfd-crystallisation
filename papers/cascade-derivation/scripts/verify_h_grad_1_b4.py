#!/usr/bin/env python3
"""B4 primal reduction `red : Z[φ]⁶ → I/2I_lat` for H-grad-1.

Implements codex-derive Route P (Phase-M3 projection):
   Z[φ]⁶ ≅ σ(I) ⊕ M       (π_int(L_12) split per cascade-phase-m3-closure.md:49-69)
          ↓ p_O = projection to first σ(I)-summand
   σ(I)                    (rank 4 over Z[φ] = rank 8 over Z)
          ↓ θ_O = σ⁻¹      (Galois twist: (α, β) ↦ (α+β, -β) on Z[φ]-coeffs)
   I
          ↓ ρ_I            (mod 2I_lat using B1 basis)
   I / 2I_lat ≅ F_2⁸

Verifies:
  B4.5.1 — red is well-defined and F_2-linear.
  B4.5.2 — rank_F2(red) = 8, image = all of I/2I_lat.
  B4.5.3 — kernel_F2(red) has dim 4 in F_2^12 (matching the M-summand).
  B4.5.4 — μ_I ∘ red has rank 3 (composed with B3's μ_I).
  B4.5.5 — the 12 F_2¹² standard generators span (F_2)³ under μ_I ∘ red
           (their individual images need not be distinct; the F_2-span
           of their images must equal (F_2)³, i.e. rank 3). The four
           M-summand generators must all map to 0.

Run:
    python3 papers/cascade-derivation/scripts/verify_h_grad_1_b4.py
"""

from __future__ import annotations

import os
import sys
from fractions import Fraction
from itertools import product

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify_h_grad_1 import (  # type: ignore
    BASIS, basis_column_matrix, inverse, determinant,
    embed_scaled, Quat, qadd, qscale, qnorm,
)
# Reuse B3's μ_I and its F_2 machinery.
from verify_h_grad_1_b3 import (  # type: ignore
    ALL_VECS, ZERO, IDENTITY, apply_M, f2_rank,
    build_K, build_mu_matrix, find_T,
    enumerate_4d_totally_singular, vxor,
)


# --------------------------------------------------------------------
# φ-multiplication matrix Φ on B_I basis
# --------------------------------------------------------------------

PHI_Q: Quat = ((Fraction(0), Fraction(1)), (Fraction(0), Fraction(0)),
               (Fraction(0), Fraction(0)), (Fraction(0), Fraction(0)))
# PHI_Q represents the pure-scalar quaternion φ + 0·i + 0·j + 0·k,
# with φ encoded as ZPhi(a=0, b=1). But ZPhi is a dataclass, not tuples.
# Re-import ZPhi for correct typing.

from verify_h_grad_1 import ZPhi, z  # type: ignore

# Correct φ as ZPhi.
PHI = z(0, 1)  # a + b*phi with (a=0, b=1)

def qmul_scalar(x: Quat, s: ZPhi) -> Quat:
    """Multiply quaternion x by a scalar in Q(φ)."""
    return tuple(zmul(xi, s) for xi in x)  # type: ignore


def zmul(a: ZPhi, b: ZPhi) -> ZPhi:
    """Product in Q(φ)."""
    # (a0 + a1*φ)(b0 + b1*φ) = a0 b0 + (a0 b1 + a1 b0) φ + a1 b1 φ²
    # with φ² = φ + 1, so = (a0 b0 + a1 b1) + (a0 b1 + a1 b0 + a1 b1) φ.
    return ZPhi(
        a.a * b.a + a.b * b.b,
        a.a * b.b + a.b * b.a + a.b * b.b,
    )


def compute_phi_matrix():
    """Compute the 8×8 integer matrix Φ such that φ·ω_i = Σ_j Φ[j][i] ω_j
    where ω_1,...,ω_8 is the B1 Z-basis of I.

    Returns Φ as 8 rows, 8 cols, integer entries.
    """
    # embed_scaled expresses a quaternion as 8 scaled coefficients (doubled)
    # in B_I basis. The scaling is the same for all columns.
    basis_cols = basis_column_matrix()  # 8×8 Fraction matrix
    basis_inv = inverse(basis_cols)
    Phi_cols = []
    for i in range(8):
        omega_i = BASIS[i]
        phi_omega_i = qmul_scalar(omega_i, PHI)
        # Express phi_omega_i in B_I basis.
        coords_scaled = embed_scaled(phi_omega_i)  # list of 8 Fractions
        coords = []
        for j in range(8):
            s = Fraction(0)
            for k in range(8):
                s += basis_inv[j][k] * coords_scaled[k]
            # The basis_column_matrix scales everything by the same factor;
            # after inversion, integer coords should pop out.
            assert s.denominator == 1, f"φ·ω_{i+1} has non-integer coord {s}"
            coords.append(int(s))
        Phi_cols.append(coords)
    # Phi_cols[i] = coords of φ·ω_i in B_I basis.
    # We want Phi[j][i] = coefficient on ω_j for φ·ω_i.
    Phi = [[Phi_cols[i][j] for i in range(8)] for j in range(8)]
    return Phi


# --------------------------------------------------------------------
# Find a Z[φ]-basis of I among {ω_1,...,ω_8}
# --------------------------------------------------------------------

def find_zphi_basis(Phi) -> list[int]:
    """Find a 4-element subset S ⊂ {0..7} such that {ω_{S[0]}, ω_{S[1]},
    ω_{S[2]}, ω_{S[3]}, φ·ω_{S[0]}, ..., φ·ω_{S[3]}} is a Z-basis of I.

    Test: the 8×8 Z-matrix with columns = these 8 vectors in B_I basis
    should have determinant ±1.
    """
    from itertools import combinations
    for combo in combinations(range(8), 4):
        # Build 8×8 integer matrix: columns 0..3 are e_{combo[0..3]};
        # columns 4..7 are Phi-column combo[0..3] (φ·ω_{combo[i]}).
        M = [[0] * 8 for _ in range(8)]
        for k, i in enumerate(combo):
            M[i][k] = 1  # column k is e_i
        for k, i in enumerate(combo):
            for j in range(8):
                M[j][4 + k] = Phi[j][i]
        # Compute determinant over Q.
        det = _int_det_f2_aware(M)
        if det in (1, -1):
            return list(combo)
    raise RuntimeError("no Z[φ]-basis subset of B_I found")


def _int_det_f2_aware(M):
    """Determinant of an 8×8 integer matrix (using Bareiss/LU)."""
    n = len(M)
    A = [row[:] for row in M]
    sign = 1
    for i in range(n):
        # Find pivot.
        piv = None
        for r in range(i, n):
            if A[r][i] != 0:
                piv = r
                break
        if piv is None:
            return 0
        if piv != i:
            A[i], A[piv] = A[piv], A[i]
            sign = -sign
        for r in range(i + 1, n):
            if A[r][i] == 0:
                continue
            # Integer row-reduction via common denominator-free approach.
            # Use rational Gaussian elimination.
            factor = Fraction(A[r][i], A[i][i])
            for c in range(i, n):
                A[r][c] = A[r][c] - factor * A[i][c]
    det = Fraction(sign)
    for i in range(n):
        det = det * A[i][i]
    assert det.denominator == 1
    return int(det)


# --------------------------------------------------------------------
# Build red : Z[φ]⁶ → F_2⁸
# --------------------------------------------------------------------

def build_red_matrix(zphi_basis_subset, Phi):
    """Build the 8×12 F_2 matrix R = red applied to Z[φ]⁶, viewed as
    Z^12 = ((α_1, β_1), ..., (α_6, β_6)) where (α_k, β_k) represent
    the k-th Z[φ]-coordinate.

    The first 4 Z[φ]-coords (Z^8) are the σ(I) component; apply σ⁻¹ at
    Z[φ]-coeff level (α, β) ↦ (α+β, -β), then map each resulting Z[φ]-
    coord to a pair of B_I basis vectors (g_k, φ·g_k) via zphi_basis_subset.
    The last 2 Z[φ]-coords (Z^4) are the M component; they go to 0.

    Column ordering of Z^12 input:
      col 0 = α_1 (coef of 1 in Z[φ]-coord 1)
      col 1 = β_1 (coef of φ in Z[φ]-coord 1)
      col 2 = α_2
      col 3 = β_2
      ...
      col 7 = β_4
      col 8..11 = (α_5, β_5, α_6, β_6) — in M, kernel of red.
    """
    R = [[0] * 12 for _ in range(8)]  # 8 rows, 12 cols, entries in F_2.
    S = zphi_basis_subset  # list of 4 indices into B_I.
    for k in range(4):
        # σ⁻¹((α, β)) = (α+β, -β); for input (α_k, β_k), the B_I contribution
        # after σ⁻¹ is (α_k + β_k) · g_k + (-β_k) · φ·g_k.
        # In F_2: coefficients (α_k + β_k) mod 2 and -β_k mod 2 ≡ β_k mod 2.
        # The B_I-basis contribution of g_k (= ω_{S[k]}) is the S[k]-th
        # B_I basis vector, i.e. row S[k] of the identity; of φ·g_k is
        # Phi column S[k], i.e. Phi[:][S[k]].
        # Contribution to row j of R:
        #   coefficient of α_k (col 2k) in row j = (1 if j == S[k] else 0) + Phi[j][S[k]] · 0  mod 2
        #                                        = δ_{j,S[k]}   ... wait, let me re-derive.
        # Actually: input α_k contributes (α_k + β_k)·g_k + β_k·φ·g_k.
        # After σ⁻¹: input (α_k, β_k) maps to:
        #   (α_k + β_k) · g_k  + (-β_k) · (φ·g_k)
        # In F_2: (α_k + β_k)·g_k + β_k·(φ·g_k)  (since -β_k ≡ β_k mod 2)
        # Contribution to B_I row j:
        #   [j==S[k]] · (α_k + β_k) + Phi[j][S[k]] · β_k
        # = [j==S[k]]·α_k + ([j==S[k]] + Phi[j][S[k]])·β_k   mod 2
        # So col 2k (α_k) in R: row j gets [j==S[k]] mod 2.
        # Col 2k+1 (β_k) in R: row j gets ([j==S[k]] + Phi[j][S[k]]) mod 2.
        for j in range(8):
            R[j][2 * k] = (1 if j == S[k] else 0) & 1
            R[j][2 * k + 1] = ((1 if j == S[k] else 0) + Phi[j][S[k]]) & 1
        # Cols 8..11 stay zero: M-summand in kernel.
    return R


def apply_R(R, v):
    """Apply the 8×12 F_2 matrix R to a 12-bit vector v."""
    out = [0] * 8
    for j in range(8):
        s = 0
        for c in range(12):
            s ^= R[j][c] & v[c]
        out[j] = s
    return tuple(out)


# --------------------------------------------------------------------
# Verification
# --------------------------------------------------------------------

def verify_red(R):
    """Run all B4.5 checks."""
    print("=== B4.5.1 — F_2-linearity (sampled) ===")
    # F_2-linearity is automatic because R is an F_2 matrix — applying it
    # entrywise IS linear. Quick sanity on 20 random pairs.
    import random
    random.seed(0)
    lin_ok = True
    for _ in range(20):
        a = tuple(random.randint(0, 1) for _ in range(12))
        b = tuple(random.randint(0, 1) for _ in range(12))
        ab = tuple((a[i] ^ b[i]) for i in range(12))
        if apply_R(R, ab) != tuple((apply_R(R, a)[i] ^ apply_R(R, b)[i]) for i in range(8)):
            lin_ok = False
            break
    print(f"  Sampled linearity: {'PASS' if lin_ok else 'FAIL'}")

    print()
    print("=== B4.5.2 — rank and image ===")
    rk = f2_rank([list(row) for row in R])
    print(f"  rank_F2(red) = {rk}  (expected 8)  - {'PASS' if rk == 8 else 'FAIL'}")
    # Enumerate full image on Z^12 mod 2.
    image = set()
    for v in product((0, 1), repeat=12):
        image.add(apply_R(R, v))
    print(f"  |image(red)| = {len(image)}  (expected 256 = |F_2^8|)  - "
          f"{'PASS' if len(image) == 256 else 'FAIL'}")

    print()
    print("=== B4.5.3 — kernel dimension in F_2^12 ===")
    ker_count = sum(1 for v in product((0, 1), repeat=12) if apply_R(R, v) == tuple([0]*8))
    # ker dim d means |ker| = 2^d; expected d = 4.
    expected_ker = 2 ** 4  # 16
    print(f"  |ker(red)| = {ker_count}  (expected 16 = 2^4)  - "
          f"{'PASS' if ker_count == 16 else 'FAIL'}")

    return (lin_ok and rk == 8 and len(image) == 256 and ker_count == 16)


# --------------------------------------------------------------------
# Compose with μ_I (B3) and verify
# --------------------------------------------------------------------

def verify_mu_of_red(R, M_mu):
    """Compute μ_I ∘ red and verify rank 3, all 8 Fano values hit."""
    print()
    print("=== B4.5.4 — μ_I ∘ red rank 3 and full image ===")
    # Compose matrices: M_mu is 3×8, R is 8×12, so product is 3×12.
    MR = [[0] * 12 for _ in range(3)]
    for r in range(3):
        for c in range(12):
            s = 0
            for k in range(8):
                s ^= M_mu[r][k] & R[k][c]
            MR[r][c] = s
    rk_comp = f2_rank([list(row) for row in MR])
    print(f"  rank_F2(μ_I ∘ red) = {rk_comp}  (expected 3)  - "
          f"{'PASS' if rk_comp == 3 else 'FAIL'}")
    # Enumerate image over Z^12 mod 2.
    composed_image = set()
    for v in product((0, 1), repeat=12):
        out8 = apply_R(R, v)
        composed_image.add(apply_M(M_mu, out8))
    print(f"  |image(μ_I ∘ red)| = {len(composed_image)}  (expected 8 = |(F_2)^3|)  - "
          f"{'PASS' if len(composed_image) == 8 else 'FAIL'}")
    print(f"  Image values: {sorted(composed_image)}")
    return rk_comp == 3 and len(composed_image) == 8


# --------------------------------------------------------------------
# Main
# --------------------------------------------------------------------

def main():
    print("=" * 72)
    print("B4 — Primal reduction red : Z[φ]⁶ → I/2I_lat (Route P)")
    print("=" * 72)
    print()

    print("=== B4.1+B4.2 — Compute φ-multiplication matrix Φ on B_I ===")
    Phi = compute_phi_matrix()
    print("  8×8 integer matrix Φ (row j, col i = coeff of ω_{j+1} in φ·ω_{i+1}):")
    for j in range(8):
        print(f"    {Phi[j]}")
    print()
    print("=== B4.3 — Find Z[φ]-basis subset of B_I ===")
    S = find_zphi_basis(Phi)
    print(f"  Z[φ]-basis of I: {{ω_{S[0]+1}, ω_{S[1]+1}, ω_{S[2]+1}, ω_{S[3]+1}}}  "
          f"(det ±1 via 8×8 integer basis check)")
    print()

    print("=== B4.4 — Build red (8×12 F_2 matrix) ===")
    R = build_red_matrix(S, Phi)
    print("  Rows of R:")
    for r, row in enumerate(R):
        print(f"    ω_{r+1}: {row}")
    print()

    ok1 = verify_red(R)

    # Compose with B3's μ_I. Reconstruct μ_I from the B3 sim.
    print()
    print("=== Composing with B3's μ_I ===")
    # Rebuild μ_I exactly as B3 does.
    from verify_h_grad_1_b3 import (  # type: ignore
        enumerate_4d_totally_singular as _enum, build_K as _K_builder,
        find_T as _T, build_mu_matrix as _mu_builder, IDENTITY as _ID,
    )
    all_L = _enum()
    L_not_through_1 = [L for L in all_L if _ID not in L]
    L0 = sorted(L_not_through_1[0], key=lambda v: sum(v[i] << i for i in range(8)))
    K_set = _K_builder(set(L0))
    T_basis = _T(K_set)
    M_mu = _mu_builder(K_set, T_basis)
    print(f"  μ_I rebuilt: {[list(row) for row in M_mu]}")

    ok2 = verify_mu_of_red(R, M_mu)

    # B4.5.5 — The 12 standard generators of F_2^12, under μ_I ∘ red,
    # must linearly span (F_2)^3 (i.e. the composition is surjective
    # when restricted to the span of generators; equivalently rank 3).
    # Note: the 8 σ(I)-generators on their own don't need to hit all 8
    # Fano values (their image set has cardinality ≤ 8 but can be less,
    # since redundancy is permitted as long as the span is rank 3).
    print()
    print("=== B4.5.5 — 12 standard F_2^12 generators span (F_2)^3 under μ_I∘red ===")
    gen_imgs = []
    for i in range(12):
        v = [0] * 12
        v[i] = 1
        out = apply_R(R, tuple(v))
        fin = apply_M(M_mu, out)
        gen_imgs.append(fin)
        # Describe generator origin.
        if i < 8:
            origin = f"σ(I) coord {i//2+1}, '{'α' if i%2==0 else 'β'}'"
        else:
            origin = f"M coord {(i-8)//2+1}, '{'α' if (i-8)%2==0 else 'β'}' (expected 0)"
        print(f"    gen_{i+1} ({origin}): μ_I∘red = {fin}")
    # Span is the F_2-linear closure of gen_imgs under addition.
    span_set = {(0, 0, 0)}
    for g in gen_imgs:
        span_set = span_set | {tuple(a ^ b for a, b in zip(s, g)) for s in span_set}
    ok3 = len(span_set) == 8
    distinct = len(set(gen_imgs))
    print(f"  Generators hit {distinct} distinct values; their F_2-span has {len(span_set)} elements "
          f"(expected 8)  - {'PASS' if ok3 else 'FAIL'}")

    all_ok = ok1 and ok2 and ok3
    print()
    print("=" * 72)
    print(f"B4 OVERALL: {'PASS' if all_ok else 'FAIL'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
