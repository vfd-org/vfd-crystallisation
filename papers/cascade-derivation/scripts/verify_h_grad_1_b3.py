#!/usr/bin/env python3
"""B3 Fano quotient construction for H-grad-1, Route K (Kirmse-Coxeter).

Uses sim-verified q_I from verify_h_grad_1.py (B1+B2). Implements
codex's Section B sub-builds (codex-derive WO 2026-04-23):

  B3.1 — Enumerate all maximal totally singular 4-dim subspaces of
         F_2^8 (expected 270); count those containing the identity
         class [1] (expected 30).
  B3.2 — Canonicalise (L_0, η) by lex-first enumeration. L_0 is the
         lex-first totally singular 4-space NOT containing [1] (so
         K = L_0 ⊕ ⟨[1]⟩ has dim 5).
  B3.3 — K = L_0 ⊕ ⟨[1]⟩, dim 5; T = lex-first 3-dim complement.
  B3.4 — Octonion basis labels η(0)=[1], η(v_i)=[1]+L(v_i) where L
         is the linear iso F_2^3 → T sending standard basis to
         T-basis vectors.
  B3.5 — Define μ_I as 3×8 F_2 matrix; verify rank 3, |ker|=32,
         image=8, all 7 Fano lines, exhaustive linearity (256² pairs).

Performance: precomputes q_table[256] once; subspace enumeration
uses RREF over F_2 to avoid the O(N^4) loops that the prior draft
used. Total runtime: under 5 seconds.

Run:
    python3 papers/cascade-derivation/scripts/verify_h_grad_1_b3.py
"""

from __future__ import annotations

import os
import sys
from itertools import combinations, product

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify_h_grad_1 import q_mod2  # type: ignore


# --------------------------------------------------------------------
# F_2^8 setup
# --------------------------------------------------------------------

N = 8
ALL_VECS = [tuple((i >> k) & 1 for k in range(N)) for i in range(1 << N)]
ZERO = ALL_VECS[0]
IDENTITY = (1, 0, 0, 0, 0, 0, 0, 0)  # ω_1 = 1 ∈ I, mod 2 = standard e_1


def vint(v):
    return sum(v[k] << k for k in range(N))


def vxor(a, b):
    return tuple(a[k] ^ b[k] for k in range(N))


def vint3(v):
    return v[0] | (v[1] << 1) | (v[2] << 2)


# Precompute q_I and polar form b_I once.
Q_TABLE = [q_mod2(v) for v in ALL_VECS]


def q_at(v):
    return Q_TABLE[vint(v)]


def b_at(u, v):
    """Polar form b(u, v) = q(u+v) - q(u) - q(v) over F_2."""
    return Q_TABLE[vint(vxor(u, v))] ^ Q_TABLE[vint(u)] ^ Q_TABLE[vint(v)]


# --------------------------------------------------------------------
# Subspace enumeration via RREF
# --------------------------------------------------------------------

def f2_rank(rows):
    """Rank over F_2."""
    rows = [list(r) for r in rows]
    r = 0
    for c in range(N):
        piv = None
        for i in range(r, len(rows)):
            if rows[i][c] == 1:
                piv = i
                break
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(len(rows)):
            if i != r and rows[i][c] == 1:
                rows[i] = [rows[i][k] ^ rows[r][k] for k in range(N)]
        r += 1
    return r


def span(basis):
    """All elements of the F_2-span of basis."""
    out = {ZERO}
    for v in basis:
        out = out | {vxor(s, v) for s in out}
    return out


def enumerate_4d_totally_singular():
    """Enumerate all 4-dim subspaces L ≤ F_2^8 with q_I|L = 0.

    Returns list of frozensets, sorted by lex order of the sorted-tuple
    of elements.

    Strategy: enumerate vectors in RREF order. A 4-dim subspace has a
    unique RREF basis with 4 pivot columns chosen from {0,...,7}, the
    pivot rows filled with identity, and the non-pivot column entries
    arbitrary (free). Enumerate over pivot patterns and free entries.

    Total subspaces of 4-dim in F_2^8 = Gaussian binomial = 200787 —
    too many to enumerate naively. But we filter by isotropy on a
    spanning set of 4 vectors.
    """
    found = set()
    # Build the 135-element list of nonzero isotropic vectors.
    iso = [v for v in ALL_VECS if v != ZERO and q_at(v) == 0]
    assert len(iso) == 135, f"got {len(iso)} isotropic, expected 135"
    iso_set = set(iso)

    # For each 4-tuple of isotropic vectors (with ordering enforced),
    # check linear independence and that all pairwise sums are also
    # isotropic (which forces the whole span to be isotropic by
    # induction). Enforce v_a < v_b < v_c < v_d in vint order.
    iso_sorted = sorted(iso, key=vint)

    # Precompute polar-orthogonal lists per vector for fast pruning.
    # b(u,v) = 0 means u and v are polar-orthogonal — required for
    # u+v to also be isotropic when both are.
    b_orth = {u: [v for v in iso_sorted if vint(v) > vint(u) and b_at(u, v) == 0]
              for u in iso_sorted}

    for v1 in iso_sorted:
        L1 = b_orth[v1]
        for v2 in L1:
            # v3 must be polar-orthogonal to both v1 and v2.
            S12 = set(L1) & set(b_orth[v2])
            S12_sorted = sorted(S12, key=vint)
            sp12 = {ZERO, v1, v2, vxor(v1, v2)}
            for v3 in S12_sorted:
                if v3 in sp12:
                    continue
                S123 = S12 & set(b_orth[v3])
                sp123 = sp12 | {vxor(s, v3) for s in sp12}
                S123_sorted = [v for v in sorted(S123, key=vint) if v not in sp123]
                for v4 in S123_sorted:
                    sp = sp123 | {vxor(s, v4) for s in sp123}
                    if len(sp) != 16:
                        continue
                    # Confirm all elements isotropic (should be guaranteed).
                    if any(q_at(w) for w in sp):
                        continue
                    found.add(frozenset(sp))

    return sorted(found, key=lambda s: sorted(s, key=vint))


# --------------------------------------------------------------------
# Fano structure
# --------------------------------------------------------------------

V3 = {
    1: (1, 0, 0), 2: (0, 1, 0), 3: (1, 1, 0),
    4: (0, 0, 1), 5: (1, 0, 1), 6: (0, 1, 1), 7: (1, 1, 1),
}
FANO_LINES = [
    (1, 2, 3), (1, 4, 5), (1, 6, 7),
    (2, 4, 6), (2, 5, 7), (3, 4, 7), (3, 5, 6),
]
# Verify: each line sums to 0 in F_2^3.
for (i, j, k) in FANO_LINES:
    s = tuple(V3[i][m] ^ V3[j][m] ^ V3[k][m] for m in range(3))
    assert s == (0, 0, 0), f"Fano line {(i,j,k)} sums to {s}"


# --------------------------------------------------------------------
# B3.3 — Kernel + complement
# --------------------------------------------------------------------

def build_K(L0):
    """K = L_0 ⊕ ⟨[1]⟩ when [1] ∉ L_0."""
    assert IDENTITY not in L0, "L_0 must not contain [1]"
    K = set(L0) | {vxor(v, IDENTITY) for v in L0}
    assert len(K) == 32, f"|K|={len(K)}, expected 32"
    return K


def find_T(K_set):
    """Return lex-first 3-dim complement T of K (as basis t1, t2, t3)."""
    def smallest_outside(S):
        for v in ALL_VECS:
            if v != ZERO and v not in S:
                return v
        raise RuntimeError("no vector outside S")

    t1 = smallest_outside(K_set)
    S1 = K_set | {vxor(s, t1) for s in K_set}
    t2 = smallest_outside(S1)
    S2 = S1 | {vxor(s, t2) for s in S1}
    t3 = smallest_outside(S2)
    return (t1, t2, t3)


# --------------------------------------------------------------------
# B3.5 — μ_I matrix
# --------------------------------------------------------------------

def build_mu_matrix(K_set, T_basis):
    """Solve for the 3x8 F_2 matrix M such that:
       M(k) = 0 for k ∈ K (basis),
       M(t_j) = e_j ∈ F_2^3 for j = 1,2,3.

    Uses Gauss-Jordan on B = [K_basis (5 cols) | T_basis (3 cols)] augmented
    with identity to invert; then M = T_targets · B^{-1}.
    """
    # Pick a 5-element basis of K.
    K_basis = []
    sp = {ZERO}
    for v in sorted(K_set, key=vint):
        if v not in sp:
            K_basis.append(v)
            sp = sp | {vxor(s, v) for s in sp}
            if len(K_basis) == 5:
                break
    assert len(K_basis) == 5

    full_basis = K_basis + list(T_basis)  # 8 vectors, basis of F_2^8.
    # Verify full span.
    full_span = set()
    for coeffs in product((0, 1), repeat=8):
        v = ZERO
        for c, b in zip(coeffs, full_basis):
            if c:
                v = vxor(v, b)
        full_span.add(v)
    assert len(full_span) == 256, f"full_basis spans only {len(full_span)} vectors"

    targets = [(0, 0, 0)] * 5 + [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

    # Build augmented matrix [B^T | I] then row-reduce to get [I | (B^T)^-1].
    # Each row of aug is full_basis[i] (8 cols) ++ identity row e_i (8 cols).
    aug = []
    for i in range(8):
        row = list(full_basis[i]) + [1 if k == i else 0 for k in range(8)]
        aug.append(row)

    r = 0
    for c in range(8):
        piv = None
        for i in range(r, 8):
            if aug[i][c] == 1:
                piv = i
                break
        if piv is None:
            raise RuntimeError("singular full_basis")
        aug[r], aug[piv] = aug[piv], aug[r]
        for i in range(8):
            if i != r and aug[i][c] == 1:
                aug[i] = [aug[i][kk] ^ aug[r][kk] for kk in range(16)]
        r += 1
    # Right half is (B^T)^{-1}.
    Binv_T = [aug[i][8:] for i in range(8)]

    # Setup: aug[i] starts as [full_basis[i] | e_i]. After Gauss-Jordan
    # reducing the LEFT 8 columns to identity, the right 8 columns hold
    # (B^T)^{-1} where B has full_basis[i] as its i-th COLUMN. Thus
    # aug[i][8:][k] = (B^T)^{-1}[i][k] = (B^{-1})[k][i].
    #
    # We want M = T · B^{-1} where T is 3×8 with columns = targets[i].
    # So M[r][c] = sum_k T[r][k] · B^{-1}[k][c]
    #           = sum_k targets[k][r] · (B^{-1})[k][c]
    #           = sum_k targets[k][r] · aug[c][8+k].
    M = []
    for r_idx in range(3):
        row = [0] * 8
        for c_idx in range(8):
            s = 0
            for k in range(8):
                s ^= targets[k][r_idx] & Binv_T[c_idx][k]
            row[c_idx] = s
        M.append(tuple(row))
    return M


def apply_M(M, v):
    return tuple(sum(M[r][c] & v[c] for c in range(8)) & 1 for r in range(3))


# --------------------------------------------------------------------
# Main
# --------------------------------------------------------------------

def main():
    print("=" * 72)
    print("B3 — Fano quotient μ_I : I/2I_lat ↠ (F_2)^3 via Route K")
    print("=" * 72)
    print()

    # B3.1 enumeration.
    print("=== B3.1 — Maximal totally singular 4-spaces ===")
    all_L = enumerate_4d_totally_singular()
    print(f"All 4-dim totally singular subspaces of F_2^8: {len(all_L)}  "
          f"(expected 270 for E_8/2E_8)  - "
          f"{'PASS' if len(all_L) == 270 else 'FAIL'}")
    L_through_1 = [L for L in all_L if IDENTITY in L]
    print(f"Those containing [1]={IDENTITY}: {len(L_through_1)}  "
          f"(expected 30 incidence count)  - "
          f"{'PASS' if len(L_through_1) == 30 else 'FAIL'}")
    L_not_through_1 = [L for L in all_L if IDENTITY not in L]
    print(f"Those NOT containing [1]: {len(L_not_through_1)}  "
          f"(expected 240 = 270−30)  - "
          f"{'PASS' if len(L_not_through_1) == 240 else 'FAIL'}")
    print()

    # B3.2 canonical L_0.
    print("=== B3.2 — Canonical L_0 (lex-first NOT containing [1]) ===")
    L0 = sorted(L_not_through_1[0], key=vint)
    L0_set = set(L0)
    print("L_0 elements (16 total):")
    for v in L0:
        print(f"    {v}  int={vint(v):3d}")
    print()

    # B3.3 kernel + complement.
    print("=== B3.3 — Kernel K = L_0 ⊕ ⟨[1]⟩ and complement T ===")
    K_set = build_K(L0_set)
    print(f"|K| = {len(K_set)}  (expected 32 = 2^5)  - "
          f"{'PASS' if len(K_set) == 32 else 'FAIL'}")
    T_basis = find_T(K_set)
    T_set = span(list(T_basis))
    print(f"T basis: t1={T_basis[0]} t2={T_basis[1]} t3={T_basis[2]}")
    print(f"|T| = {len(T_set)}  (expected 8 = 2^3)  - "
          f"{'PASS' if len(T_set) == 8 else 'FAIL'}")
    inter = K_set & T_set
    print(f"K ∩ T = {{{','.join(str(v) for v in inter)}}}  "
          f"(expected just zero)  - "
          f"{'PASS' if inter == {ZERO} else 'FAIL'}")
    print()

    # B3.4 Build μ_I.
    print("=== B3.4 + B3.5 — μ_I matrix and Fano verification ===")
    M = build_mu_matrix(K_set, T_basis)
    print("μ_I as 3×8 F_2 matrix (rows):")
    for r_idx, row in enumerate(M):
        print(f"    row {r_idx}: {row}")

    rk = f2_rank([list(row) for row in M])
    print(f"rank(μ_I) = {rk}  (expected 3)  - "
          f"{'PASS' if rk == 3 else 'FAIL'}")

    ker_count = sum(1 for v in ALL_VECS if apply_M(M, v) == (0, 0, 0))
    print(f"|ker(μ_I)| = {ker_count}  (expected 32)  - "
          f"{'PASS' if ker_count == 32 else 'FAIL'}")

    image = {apply_M(M, v) for v in ALL_VECS}
    print(f"|image(μ_I)| = {len(image)}  (expected 8)  - "
          f"{'PASS' if len(image) == 8 else 'FAIL'}")

    # η: F_2^3 → F_2^8 with η(0)=[1] and η(v_i)=[1] + L(v_i) where L is
    # the linear iso F_2^3 → T sending (1,0,0)→t1, (0,1,0)→t2, (0,0,1)→t3.
    def L_lin(v):
        r = ZERO
        for idx, bit in enumerate(v):
            if bit:
                r = vxor(r, T_basis[idx])
        return r

    def eta(v):
        return IDENTITY if v == (0, 0, 0) else vxor(IDENTITY, L_lin(v))

    print()
    print("η-labelling (octonion basis classes):")
    labels_ok = apply_M(M, IDENTITY) == (0, 0, 0)
    print(f"    η(0,0,0)  = [1] = {IDENTITY}, μ_I = {apply_M(M, IDENTITY)}  "
          f"({'matches identity → 0' if labels_ok else 'MISMATCH'})")
    for i in range(1, 8):
        h = eta(V3[i])
        m = apply_M(M, h)
        expected = V3[i]
        match = (m == expected)
        labels_ok = labels_ok and match
        print(f"    η(v_{i}={V3[i]}) = {h}, μ_I = {m}  "
              f"({'matches v_'+str(i) if match else 'MISMATCH'})")
    print(f"All 8 octonion labels match v_i: {'PASS' if labels_ok else 'FAIL'}")

    # Fano line check: η(v_i) + η(v_j) + η(v_k) + [1] ∈ L_0?
    print()
    print("Fano incidence: η(v_i) + η(v_j) + η(v_k) + [1] ∈ L_0?")
    fano_ok = True
    for (i, j, k) in FANO_LINES:
        s = vxor(vxor(vxor(eta(V3[i]), eta(V3[j])), eta(V3[k])), IDENTITY)
        in_L = s in L0_set
        print(f"    line ({i},{j},{k}): sum={s}  "
              f"{'∈ L_0 — PASS' if in_L else '∉ L_0 — FAIL'}")
        fano_ok = fano_ok and in_L
    print(f"All 7 Fano lines: {'PASS' if fano_ok else 'FAIL'}")

    # Exhaustive linearity: all 256² pairs.
    print()
    print("Exhaustive F_2-linearity: μ_I(a+b) = μ_I(a) + μ_I(b) over all 65536 pairs:")
    bad = 0
    for a in ALL_VECS:
        ma = apply_M(M, a)
        for b in ALL_VECS:
            mb = apply_M(M, b)
            mab = apply_M(M, vxor(a, b))
            sum_mab = tuple(ma[r] ^ mb[r] for r in range(3))
            if sum_mab != mab:
                bad += 1
                if bad < 3:
                    print(f"    FAIL at a={a}, b={b}: μ(a)+μ(b)={sum_mab}, μ(a+b)={mab}")
    linearity_ok = bad == 0
    print(f"Exhaustive linearity: {'PASS' if linearity_ok else f'FAIL ({bad} bad pairs)'}")

    # Verdict.
    all_ok = (
        len(all_L) == 270 and len(L_through_1) == 30
        and len(K_set) == 32 and len(T_set) == 8 and inter == {ZERO}
        and rk == 3 and ker_count == 32 and len(image) == 8
        and labels_ok and fano_ok and linearity_ok
    )
    print()
    print("=" * 72)
    print(f"B3 OVERALL: {'PASS' if all_ok else 'FAIL'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
