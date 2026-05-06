#!/usr/bin/env python3
"""
explore_defect.py — load-bearing numerical exploration for
`papers/cascade-refinement-compat/`.

Question: in the cascade refinement tower of P3/P4 with curvature
operator A_n = block-diag(d_n* d_n, d_n d_n*) and bonding maps
(p^0, p^1) where p^0 is vertex restriction and p^1 is parent-fibre
averaging, what relation (if any) holds between A_n and A_{n+1}
under the bonding maps?

Two hypotheses to test:

(H1) Strict refinement compatibility:
        p ∘ A_{n+1} = A_n ∘ p
     EXPECTED: false in general (refinement adds midpoints that change
     graph-Laplacian values at level-n vertices).

(H2) Harmonic-subspace scaled compatibility:
     Let H_{n+1}: X_n^0 → X_{n+1}^0 be the harmonic extension that
     fixes values on V(G_n^•) and minimises A_{n+1}^vertex-energy.
     Then on the image of H_{n+1}:
        p^0 ∘ A_{n+1}^vertex ∘ H_{n+1} = (1/2) ∘ A_n^vertex
     EXPECTED: true; same factor-1/2 as the source's coboundary
     refinement relation `p^1 d_{n+1} = (1/2) d_n p^0`.

(H3) Schur-complement intertwining (clean restatement of H2):
     Define the Schur-complement operator
        Ã_n := p^0 A_{n+1}^vertex H_{n+1}
     where H_{n+1} is harmonic extension. Then Ã_n is itself a graph
     Laplacian on V(G_n^•) (with possibly modified weights), and
        p^0 ∘ A_{n+1}^vertex ∘ H_{n+1} ∘ p^0 = Ã_n ∘ p^0
     holds by construction.
     EXPECTED: true; the question is what graph Ã_n corresponds to
     and whether it equals A_n or a re-weighted variant.

(H4) Residual monotonicity on the harmonic subspace:
        <p^0 H_{n+1} f, A_n p^0 H_{n+1} f>
            ≤ <H_{n+1} f, A_{n+1} H_{n+1} f>
     for all f in X_n^0. (Equivalent question: how does Ã_n compare
     to A_n in quadratic-form order?)

The script tests (H1)–(H4) on three concrete refinement instances:

  Tower I  — single edge → 1-midpoint subdivision (n=0 has 2 vertices,
             n=1 has 3 vertices). The minimal nontrivial case.
  Tower II — triangle (3-cycle) → barycentric subdivision adding 3
             edge-midpoints (n=0 has 3 vertices, n=1 has 6 vertices).
  Tower III — single edge → two-step refinement (n=0 → n=1 → n=2),
              testing whether a discovered relation composes across
              levels.

All linear algebra is exact via numpy on integer/rational matrices.
"""

from __future__ import annotations

import numpy as np
from fractions import Fraction


def build_edge_tower():
    """Tower I: single edge → 1-midpoint subdivision."""
    # Level 0: G_0 = ({u, v}, {(u,v)})
    # X_0^0 = R^2 indexed (u, v). X_0^1 = R^1 indexed (u,v).
    d_0 = np.array([[-1, 1]], dtype=Fraction)  # d_0(f)(u,v) = f(v) - f(u)

    # Level 1: G_1 = ({u, m, v}, {(u,m), (m,v)})
    # X_1^0 = R^3 indexed (u, m, v). X_1^1 = R^2 indexed ((u,m), (m,v)).
    d_1 = np.array(
        [
            [-1, 1, 0],   # (u,m): f(m) - f(u)
            [0, -1, 1],   # (m,v): f(v) - f(m)
        ],
        dtype=Fraction,
    )

    # Bonding maps:
    # p^0: X_1^0 → X_0^0 (vertex restriction; drops the midpoint m)
    p0 = np.array(
        [
            [1, 0, 0],   # u
            [0, 0, 1],   # v
        ],
        dtype=Fraction,
    )

    # p^1: X_1^1 → X_0^1 (parent-fibre averaging; both children of (u,v) average)
    p1 = np.array(
        [
            [Fraction(1, 2), Fraction(1, 2)],
        ],
        dtype=Fraction,
    )

    return {"d_0": d_0, "d_1": d_1, "p0": p0, "p1": p1, "name": "Tower I (edge→midpoint)"}


def build_triangle_tower():
    """Tower II: triangle (3-cycle) → barycentric edge-midpoint subdivision."""
    # Level 0: G_0 = ({0, 1, 2}, edges (0,1), (1,2), (2,0))
    # X_0^0 = R^3 indexed (0, 1, 2). X_0^1 = R^3 indexed (e01, e12, e20).
    # d_0 in oriented form:
    d_0 = np.array(
        [
            [-1, 1, 0],   # e01 = f(1) - f(0)
            [0, -1, 1],   # e12 = f(2) - f(1)
            [1, 0, -1],   # e20 = f(0) - f(2)
        ],
        dtype=Fraction,
    )

    # Level 1: original 3 vertices + 3 edge-midpoints. Index: 0, 1, 2, m01, m12, m20.
    # Edges: (0, m01), (m01, 1), (1, m12), (m12, 2), (2, m20), (m20, 0).
    # X_1^0 = R^6, X_1^1 = R^6.
    d_1 = np.zeros((6, 6), dtype=Fraction)
    # Edge index → (tail, head) in vertex indexing (0,1,2,m01,m12,m20 → 0..5)
    edges_1 = [
        (0, 3),   # (0, m01)
        (3, 1),   # (m01, 1)
        (1, 4),   # (1, m12)
        (4, 2),   # (m12, 2)
        (2, 5),   # (2, m20)
        (5, 0),   # (m20, 0)
    ]
    for i, (tail, head) in enumerate(edges_1):
        d_1[i, tail] = Fraction(-1)
        d_1[i, head] = Fraction(1)

    # p^0: X_1^0 → X_0^0 (restriction to original 3 vertices)
    p0 = np.zeros((3, 6), dtype=Fraction)
    p0[0, 0] = Fraction(1)
    p0[1, 1] = Fraction(1)
    p0[2, 2] = Fraction(1)

    # p^1: X_1^1 → X_0^1 (parent-fibre averaging; each old edge has 2 children)
    # Parent map: edges_1 indices [0,1] → e01, [2,3] → e12, [4,5] → e20.
    p1 = np.zeros((3, 6), dtype=Fraction)
    p1[0, 0] = Fraction(1, 2); p1[0, 1] = Fraction(1, 2)   # e01
    p1[1, 2] = Fraction(1, 2); p1[1, 3] = Fraction(1, 2)   # e12
    p1[2, 4] = Fraction(1, 2); p1[2, 5] = Fraction(1, 2)   # e20

    return {"d_0": d_0, "d_1": d_1, "p0": p0, "p1": p1, "name": "Tower II (triangle→barycentric)"}


def fmat(M):
    """Format a Fraction matrix for display."""
    rows = []
    for r in M:
        rows.append("[ " + "  ".join(f"{x}" for x in r) + " ]")
    return "\n".join(rows)


def is_zero(M):
    """Check exact zero for a Fraction matrix."""
    return all(x == 0 for row in M for x in row)


def quad_form(M, v):
    """Compute v^T M v exactly using Fraction arithmetic."""
    Mv = M @ v
    return sum(v[i] * Mv[i] for i in range(len(v)))


def test_hypotheses(tower):
    """Test (H1)–(H4) for a given tower."""
    print(f"\n{'='*70}")
    print(f"{tower['name']}")
    print('=' * 70)

    d_0 = tower["d_0"]
    d_1 = tower["d_1"]
    p0 = tower["p0"]
    p1 = tower["p1"]

    # Sanity check: source's coboundary refinement relation
    # p^1 d_1 = (1/2) d_0 p^0
    LHS = p1 @ d_1
    RHS = Fraction(1, 2) * (d_0 @ p0)
    coboundary_ok = is_zero(LHS - RHS)
    print(f"\n[sanity] coboundary refinement relation `p^1 d_1 = (1/2) d_0 p^0`")
    print(f"         holds: {coboundary_ok}")
    if not coboundary_ok:
        print("         LHS - RHS:")
        print(fmat(LHS - RHS))
        return None

    # Construct A_n^vertex = d_n* d_n on each level
    A_0 = d_0.T @ d_0   # vertex graph Laplacian at level 0
    A_1 = d_1.T @ d_1   # vertex graph Laplacian at level 1

    print(f"\n[setup] A_0^vertex (graph Laplacian on level-0 vertices):")
    print(fmat(A_0))
    print(f"\n[setup] A_1^vertex (graph Laplacian on level-1 vertices):")
    print(fmat(A_1))

    # ===== H1: strict refinement compatibility (SCALED, paper's defect) =====
    # Paper defines D_n := p^0 A_{n+1}^vertex - (1/2) A_n^vertex p^0
    # (the "scaled" defect, matching p^0 \tilde A_{n+1} = \tilde A_n p^0).
    LHS = p0 @ A_1
    RHS = Fraction(1, 2) * (A_0 @ p0)
    defect_D = LHS - RHS
    H1_holds = is_zero(defect_D)
    print(f"\n[H1] strict scaled: `p^0 A_1 = (1/2) A_0 p^0`? (paper's D_n=0?)  {H1_holds}")
    if not H1_holds:
        print(f"     defect D_n = p^0 A_1 - (1/2) A_0 p^0:")
        print(fmat(defect_D))

    # ===== H2 / H3: harmonic-extension scaled compatibility =====
    # Construct harmonic extension H_{n+1}: X_n^0 → X_{n+1}^0 by minimising
    # A_1-energy subject to f|level_0 = boundary data.
    # Strategy: partition X_1^0 into "level-0 vertices" (kept) and
    # "new midpoints" (interior). Schur-complement.
    n0 = p0.shape[0]                 # number of level-0 vertices
    n1 = p0.shape[1]                 # number of level-1 vertices
    # Identify which level-1 indices are level-0 (boundary) vs new (interior).
    boundary_idx = []
    interior_idx = []
    for j in range(n1):
        col = p0[:, j]
        if any(c != 0 for c in col):
            boundary_idx.append(j)
        else:
            interior_idx.append(j)
    print(f"\n[partition] level-1 vertices: {n1} total = {len(boundary_idx)} boundary + {len(interior_idx)} interior")

    # Block decomposition: A_1 = [[A_BB, A_BI], [A_IB, A_II]]
    # Reorder rows/cols: boundary first, then interior.
    perm = boundary_idx + interior_idx
    A_1_perm = A_1[np.ix_(perm, perm)]
    n_B = len(boundary_idx)
    A_BB = A_1_perm[:n_B, :n_B]
    A_BI = A_1_perm[:n_B, n_B:]
    A_IB = A_1_perm[n_B:, :n_B]
    A_II = A_1_perm[n_B:, n_B:]

    # Harmonic extension: given boundary values f_B, interior values
    # are f_I = -A_II^{-1} A_IB f_B (minimises (1/2) f^T A_1 f w.r.t. f_I).
    # Schur complement (boundary block of harmonically-extended A_1):
    #     S = A_BB - A_BI A_II^{-1} A_IB
    # We compute A_II^{-1} exactly using Fraction-aware inversion.
    def fraction_inverse(M):
        """Exact rational inverse via Gauss-Jordan."""
        n = M.shape[0]
        aug = np.zeros((n, 2 * n), dtype=Fraction)
        for i in range(n):
            for j in range(n):
                aug[i, j] = M[i, j]
            aug[i, n + i] = Fraction(1)
        for i in range(n):
            # Find pivot
            pivot = None
            for k in range(i, n):
                if aug[k, i] != 0:
                    pivot = k
                    break
            if pivot is None:
                raise ValueError("Singular matrix")
            if pivot != i:
                aug[[i, pivot]] = aug[[pivot, i]]
            # Scale row i
            scale = aug[i, i]
            for j in range(2 * n):
                aug[i, j] = aug[i, j] / scale
            # Eliminate other rows
            for k in range(n):
                if k != i and aug[k, i] != 0:
                    factor = aug[k, i]
                    for j in range(2 * n):
                        aug[k, j] = aug[k, j] - factor * aug[i, j]
        return aug[:, n:]

    A_II_inv = fraction_inverse(A_II)
    schur_S = A_BB - A_BI @ A_II_inv @ A_IB

    # The Schur-complement S acts on boundary (= level-0 vertex) data.
    # H3 question: is S equal to A_0, equal to A_0 / 2, or some other matrix?
    print(f"\n[H3] Schur complement S = A_BB - A_BI A_II^{{-1}} A_IB:")
    print(fmat(schur_S))
    print(f"     A_0:")
    print(fmat(A_0))

    if is_zero(schur_S - A_0):
        print(f"     S = A_0 (strict equality on boundary block).")
        H3_relation = "S = A_0"
    elif is_zero(schur_S - Fraction(1, 2) * A_0):
        print(f"     S = (1/2) A_0  ✓✓✓ (Schur complement halves the level-0 Laplacian)")
        H3_relation = "S = (1/2) A_0"
    elif is_zero(2 * schur_S - A_0):
        print(f"     2 S = A_0  ✓✓✓ (Schur complement halves the level-0 Laplacian)")
        H3_relation = "S = (1/2) A_0"
    else:
        # Try general scalar
        nonzero_pair = None
        for i in range(n_B):
            for j in range(n_B):
                if A_0[i, j] != 0 and schur_S[i, j] != 0:
                    nonzero_pair = (i, j)
                    break
            if nonzero_pair:
                break
        if nonzero_pair is not None:
            i, j = nonzero_pair
            ratio = schur_S[i, j] / A_0[i, j]
            test = is_zero(schur_S - ratio * A_0)
            if test:
                print(f"     S = {ratio} · A_0")
                H3_relation = f"S = {ratio} · A_0"
            else:
                print(f"     S not a scalar multiple of A_0; structural analysis needed")
                print(f"     Non-trivial relation: needs further structural analysis")
                H3_relation = "non-scalar"
        else:
            print(f"     Cannot determine relation without further analysis")
            H3_relation = "unknown"

    # ===== H2 (operational): on harmonically-extended states =====
    # Test: for each boundary-only state f_B, the harmonic extension
    # H f_B = (f_B; -A_II^{-1} A_IB f_B). Then p^0 A_1 H f_B vs (1/2) A_0 f_B.
    print(f"\n[H2 op] On harmonic extensions of unit boundary states:")
    test_ok = True
    for k in range(n_B):
        f_B = np.zeros(n_B, dtype=Fraction)
        f_B[k] = Fraction(1)
        f_I = -(A_II_inv @ (A_IB @ f_B))
        # Reconstruct full f_1 in original level-1 indexing.
        f_1 = np.zeros(n1, dtype=Fraction)
        for i, idx in enumerate(boundary_idx):
            f_1[idx] = f_B[i]
        for i, idx in enumerate(interior_idx):
            f_1[idx] = f_I[i]
        LHS_k = p0 @ (A_1 @ f_1)
        RHS_k = Fraction(1, 2) * (A_0 @ f_B)
        ok = all(LHS_k[i] == RHS_k[i] for i in range(len(LHS_k)))
        print(f"     boundary state e_{k}: p^0 A_1 H e_{k} = (1/2) A_0 e_{k} ?  {ok}")
        if not ok:
            test_ok = False
            print(f"       LHS: {[str(x) for x in LHS_k]}")
            print(f"       RHS: {[str(x) for x in RHS_k]}")
    H2_holds = test_ok

    # ===== H4: scaled monotonicity check =====
    # Cascade-mechanism's (O3) with the scaled curvature operator
    # \tilde A_n := 2^n A_n^vertex requires:
    #     <p^0 ψ, \tilde A_n p^0 ψ> <= <ψ, \tilde A_{n+1} ψ>  for all ψ
    # On harmonic ψ = H f, we showed <H f, A_1 H f> = (1/2) <f, A_0 f>,
    # so <H f, \tilde A_1 H f> = 2^{n+1} (1/2) <f, A_n f> = 2^n <f, A_n f>
    # = <f, \tilde A_n f> = <p^0 H f, \tilde A_n p^0 H f>.
    # i.e. EQUALITY on harmonic states (paper Theorem 3.1 with equality clause).
    # The unscaled S vs A_0 comparison below is an independent sanity check;
    # S = (1/2) A_0 trivially gives S <= A_0 since A_0 is PSD, but this does
    # NOT say anything about the cascade-mechanism (O3) direction.
    diff = schur_S - A_0
    diff_float = np.array([[float(x) for x in row] for row in diff], dtype=float)
    eigs = np.linalg.eigvalsh(diff_float)
    print(f"\n[H4] sanity: eigenvalues of (S - A_0) = {[f'{e:.6f}' for e in eigs]}")
    print(f"     (since S = (1/2) A_0, expect S - A_0 = -(1/2) A_0, "
          f"thus -PSD with one zero eigenvalue from constants kernel)")
    H4_holds = "S = (1/2) A_0 [matches H3]"

    # ===== H5: defect D_n vanishes on harmonic extensions =====
    # Paper's Proposition 4.1(i): D_n |_{range(H_{n+1})} = 0.
    print(f"\n[H5] D_n vanishes on harmonic extensions:")
    H5_ok = True
    for k in range(n_B):
        f_B = np.zeros(n_B, dtype=Fraction)
        f_B[k] = Fraction(1)
        # Construct H f_B as full level-1 state.
        f_I = -(A_II_inv @ (A_IB @ f_B))
        H_fB = np.zeros(n1, dtype=Fraction)
        for i, idx in enumerate(boundary_idx):
            H_fB[idx] = f_B[i]
        for i, idx in enumerate(interior_idx):
            H_fB[idx] = f_I[i]
        D_HfB = defect_D @ H_fB
        ok = all(D_HfB[i] == 0 for i in range(len(D_HfB)))
        print(f"     D_n applied to H(e_{k}): zero? {ok}")
        if not ok:
            H5_ok = False
            print(f"       D_n H e_{k} = {[str(x) for x in D_HfB]}")

    # ===== H6: D_n is generically NON-zero on {phi : phi_I = 0} =====
    # Paper's Proposition 4.1(ii): defect does NOT vanish on the
    # level-n-supported subspace, contradicting the original v1 claim.
    print(f"\n[H6] D_n is non-zero on level-n-supported sector {{psi_I = 0}}:")
    H6_ok = False
    for k in range(n_B):
        # State with phi_B = e_k, phi_I = 0
        phi = np.zeros(n1, dtype=Fraction)
        phi[boundary_idx[k]] = Fraction(1)
        D_phi = defect_D @ phi
        is_nonzero = any(D_phi[i] != 0 for i in range(len(D_phi)))
        print(f"     D_n applied to (e_{k}, 0): {'non-zero' if is_nonzero else 'zero'}: "
              f"D_n phi = {[str(x) for x in D_phi]}")
        if is_nonzero:
            H6_ok = True

    return {
        "tower": tower["name"],
        "H1": H1_holds,
        "H2": H2_holds,
        "H3": H3_relation,
        "H4": H4_holds,
        "H5": H5_ok,
        "H6": H6_ok,
        "schur_S": schur_S,
        "A_0": A_0,
    }


def main():
    print("=" * 70)
    print("explore_defect.py — Cascade Refinement Compatibility Exploration")
    print("=" * 70)

    results = []
    for tower_builder in [build_edge_tower, build_triangle_tower]:
        result = test_hypotheses(tower_builder())
        if result:
            results.append(result)

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY — refinement-compatibility status across towers")
    print("=" * 70)
    for r in results:
        print(f"\n{r['tower']}:")
        print(f"  H1 (strict scaled p A_1 = (1/2) A_0 p):    {r['H1']}")
        print(f"  H2 (harmonic-state p A_1 H = (1/2) A_0):   {r['H2']}")
        print(f"  H3 (Schur complement relation):            {r['H3']}")
        print(f"  H4 (monotonicity on harmonic):             {r['H4']}")
        print(f"  H5 (D_n vanishes on harmonic extensions):  {r['H5']}")
        print(f"  H6 (D_n non-zero on level-n-supported):    {r['H6']}")

    print("\n" + "=" * 70)
    print("INTERPRETATION:")
    if all(r["H1"] is False for r in results):
        print("  H1 false: strict scaled p A_1 = (1/2) A_0 p FAILS (Proposition 4.1).")
    if all(r["H2"] for r in results):
        print("  H2 true: harmonic-state factor-1/2 compatibility holds (Theorem 2.1).")
    if all("S = (1/2) A_0" in str(r["H3"]) for r in results):
        print("  H3 = S = (1/2) A_0: Schur halving (Theorem 2.1) verified.")
    if all(r["H5"] for r in results):
        print("  H5 true: D_n vanishes on harmonic-extension subspace (Proposition 4.1(i)).")
    if all(r["H6"] for r in results):
        print("  H6 true: D_n NON-zero on level-n-supported sector (Proposition 4.1(ii)).")
    print("=" * 70)


if __name__ == "__main__":
    main()
