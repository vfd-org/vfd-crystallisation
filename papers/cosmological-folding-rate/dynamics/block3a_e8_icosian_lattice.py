"""Block 3a — Build E₈ as the icosian Z-lattice; find 240 roots.

The icosian ring I is the maximal order in the quaternion algebra over Q(√5)
ramified at infinity. As a Z-module, I has rank 8 with canonical basis

    {1, i, j, h, φ, φ·i, φ·j, φ·h}

where h = (1+i+j+k)/2 is the Hurwitz unit and φ = (1+√5)/2.

With the trace inner product

    ⟨v, w⟩ := Tr_{Q(√5)/Q}(v·w̄ + w·v̄) / 2

I becomes a positive-definite even unimodular lattice of rank 8 — namely E₈.

The 240 roots of E₈ = {v ∈ I : ⟨v, v⟩ = 2}.

Note: a previous attempt used Z⟨2I⟩ as the basis, which is a PROPER sub-
lattice of I (missing scalar elements like φ). That sub-lattice has only
120 norm-2 vectors (the unit icosians 2I) and is NOT E₈.

This script:
  1. Builds the canonical Z-basis {1, i, j, h, φ, φi, φj, φh} of I.
  2. Verifies the Gram matrix is integer (so I is an integer lattice).
  3. Verifies all 120 V_600 vertices (= 2I = unit icosians) lie in I.
  4. Enumerates Z-combinations with bounded coefficients to find E₈ roots.
  5. Decomposes the 240 roots: 120 unit icosians + 120 "long" icosians.
"""
from __future__ import annotations

import sys
import time
import itertools
from fractions import Fraction
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "papers" / "paper-xxii" / "scripts"))

from run_icosian_exact import (  # noqa: E402
    q_zero, q_one, q_add, q_sub, q_neg, q_mul, q_scale, phi,
    qq_mul, qq_eq, qq_key, qq_conjugate,
    build_vertices, vertex_index_map,
)


def quat_to_8coords(q):
    return tuple(c for comp in q for c in comp)


def trace_q(q5):
    """Tr_{Q(√5)/Q}(a + b√5) = 2a."""
    return 2 * q5[0]


def trace_inner(v, w):
    """⟨v, w⟩ := Tr(v·w̄ + w·v̄) / 2 = Tr(Re(v·w̄)) ∈ Q."""
    w_conj = qq_conjugate(w)
    prod = qq_mul(v, w_conj)
    real_part = prod[0]  # Q(√5) coefficient of the (1, 0, 0, 0) component
    return trace_q(real_part)


def quat_zero():
    return (q_zero(), q_zero(), q_zero(), q_zero())


def quat_add(a, b):
    return tuple(q_add(a[k], b[k]) for k in range(4))


def quat_scale_int(a, n):
    """Scale quaternion a by integer n."""
    return tuple(q_scale(a[k], Fraction(n)) for k in range(4))


def main():
    print("Step 1: Build canonical Z-basis of icosian ring I.")
    one = q_one()
    zero = q_zero()
    half = (Fraction(1, 2), Fraction(0))
    p = phi()  # (1/2, 1/2)

    # Quaternion components: each as Q(√5) pair (a, b) ↦ a + b√5
    def make_q(w, x, y, z):
        return (w, x, y, z)

    # Basis 1: 1
    e1 = make_q(one, zero, zero, zero)
    # Basis 2: i
    e2 = make_q(zero, one, zero, zero)
    # Basis 3: j
    e3 = make_q(zero, zero, one, zero)
    # Basis 4: h = (1+i+j+k)/2
    e4 = make_q(half, half, half, half)
    # Basis 5: φ
    e5 = make_q(p, zero, zero, zero)
    # Basis 6: φ·i
    e6 = make_q(zero, p, zero, zero)
    # Basis 7: φ·j
    e7 = make_q(zero, zero, p, zero)
    # Basis 8: φ·h = φ·(1+i+j+k)/2
    p_half = (Fraction(1, 4), Fraction(1, 4))  # φ/2
    e8 = make_q(p_half, p_half, p_half, p_half)

    basis = [e1, e2, e3, e4, e5, e6, e7, e8]
    basis_names = ["1", "i", "j", "h", "φ", "φi", "φj", "φh"]
    for i, b in enumerate(basis):
        print(f"  e_{i+1} = {basis_names[i]}: {b}")

    print()
    print("Step 2: Compute Gram matrix.")
    G = [[trace_inner(basis[i], basis[j]) for j in range(8)] for i in range(8)]
    for i, row in enumerate(G):
        formatted = [f"{str(x):>5s}" for x in row]
        print(f"  e_{i+1}: [{', '.join(formatted)}]")

    all_int = all(g.denominator == 1 for row in G for g in row)
    diag_ok = all(G[i][i] == 2 for i in range(8))
    print()
    print(f"  All Gram entries integer? {all_int}")
    print(f"  Diagonal all 2? {diag_ok}")

    if not all_int:
        print("  ⚠ Gram has non-integer entries — basis spans a non-integer lattice.")
        # In that case, we may need a different basis.
        # But the canonical icosian ring basis should give integer Gram.
        # Let's see the off-diagonals:
        bad = [(i, j, G[i][j]) for i in range(8) for j in range(8)
               if i != j and G[i][j].denominator != 1]
        print(f"  Non-integer entries: {bad}")

    # Compute determinant
    print()
    print("Step 3: Compute Gram determinant.")
    # Use plain Q-arithmetic via Python's Fraction
    M = [list(row) for row in G]
    det = Fraction(1)
    for col in range(8):
        pivot = None
        for r in range(col, 8):
            if M[r][col] != 0:
                pivot = r
                break
        if pivot is None:
            det = Fraction(0)
            break
        if pivot != col:
            M[col], M[pivot] = M[pivot], M[col]
            det = -det
        det *= M[col][col]
        for r in range(col + 1, 8):
            if M[r][col] != 0:
                factor = M[r][col] / M[col][col]
                M[r] = [M[r][cc] - factor * M[col][cc] for cc in range(8)]
    print(f"  det(G) = {det}")
    print(f"  Expected for E₈: ±1.")

    print()
    print("Step 4: Verify 2I ⊂ I (all V_600 vertices are integer Z-combinations).")
    verts = build_vertices()
    n_verts = len(verts)

    # Express each vertex in basis: solve Σ n_α · basis[α] = vertex.
    # Use 8-coord representation.
    basis_8 = [quat_to_8coords(b) for b in basis]
    verts_8 = [quat_to_8coords(v) for v in verts]

    # Build 8x8 matrix M with M[k][i] = basis_8[i][k]; solve M·x = v_8 for each vertex.
    # Then check x is integer.
    M = [[basis_8[i][k] for i in range(8)] for k in range(8)]

    # LU decompose once
    def solve(M_, target):
        n = 8
        aug = [list(M_[k]) + [target[k]] for k in range(n)]
        for col in range(n):
            pivot = None
            for r in range(col, n):
                if aug[r][col] != 0:
                    pivot = r
                    break
            if pivot is None:
                return None
            if pivot != col:
                aug[col], aug[pivot] = aug[pivot], aug[col]
            for r in range(n):
                if r == col:
                    continue
                if aug[r][col] != 0:
                    factor = aug[r][col] / aug[col][col]
                    aug[r] = [aug[r][cc] - factor * aug[col][cc] for cc in range(n + 1)]
        return [aug[i][n] / aug[i][i] for i in range(n)]

    not_in_I = []
    for v_idx, v in enumerate(verts_8):
        sol = solve(M, v)
        if sol is None or any(s.denominator != 1 for s in sol):
            not_in_I.append((v_idx, sol))

    print(f"  Vertices NOT in I (Z-span of canonical basis): {len(not_in_I)}")
    if not_in_I:
        idx, sol = not_in_I[0]
        print(f"  Sample failure: vertex {idx}, Q-coeffs = {sol}")
        return

    print(f"  ✓ All 120 V_600 vertices lie in I as integer Z-combinations.")

    print()
    print("Step 5: Enumerate Z-combinations to find norm-2 vectors.")
    # E₈ in this basis has root coefficients bounded by some N. For E₈ with min
    # vector length 2, in a basis with diag 2, off-diag in [-1, 1], coefficients
    # are bounded by 2 typically (the basis isn't optimal).
    # 5^8 = 390K candidates; each evaluation is ~constant (Fraction arithmetic).
    # Should run in a few minutes.

    N = 2
    n_candidates = (2 * N + 1) ** 8
    print(f"  Trying N = {N} → {n_candidates} candidates…")
    t0 = time.time()
    roots = []
    n_evaluated = 0
    progress_step = 50000
    for coeffs in itertools.product(range(-N, N + 1), repeat=8):
        n_evaluated += 1
        if n_evaluated % progress_step == 0:
            print(f"    ...{n_evaluated}/{n_candidates} (found {len(roots)} so far, "
                  f"t={time.time()-t0:.1f}s)")
        if all(c == 0 for c in coeffs):
            continue
        v = quat_zero()
        for i, c in enumerate(coeffs):
            if c == 0:
                continue
            v = quat_add(v, quat_scale_int(basis[i], c))
        tn = trace_inner(v, v)
        if tn == 2:
            roots.append((coeffs, v))
    elapsed = time.time() - t0
    print(f"  N={N}: found {len(roots)} roots in {elapsed:.1f}s")
    print(f"  Expected: 240 if E₈, 120 if D_8 / sub-lattice.")

    if len(roots) == 240:
        print()
        print("  ✓ 240 roots found — confirmed E₈.")
        # Decompose by Hamilton norm
        from collections import Counter
        norms = Counter()
        for _, v in roots:
            w, x, y, z = v
            n_q5 = q_add(q_add(q_mul(w, w), q_mul(x, x)),
                          q_add(q_mul(y, y), q_mul(z, z)))
            norms[(n_q5[0], n_q5[1])] += 1
        print(f"  Hamilton-norm distribution: {dict(norms)}")

        # Save roots for downstream blocks
        out = Path(__file__).parent / "e8_roots.txt"
        with open(out, "w") as f:
            f.write("# E₈ roots in icosian Z-basis {1, i, j, h, φ, φi, φj, φh}\n")
            f.write("# coeff_1 coeff_2 ... coeff_8\n")
            for coeffs, v in roots:
                f.write(",".join(str(c) for c in coeffs) + "\n")
        print(f"  Roots saved to {out}")

        # Check: are the 120 unit icosians (V_600) among the roots?
        verts_keys = {qq_key(v) for v in verts}
        in_2I = sum(1 for _, v in roots if qq_key(v) in verts_keys)
        print(f"  Roots in 2I (= V_600): {in_2I}")

    elif len(roots) == 120:
        print()
        print("  Found exactly 120 roots — basis spans a sub-lattice (probably 2I-related).")

    else:
        print()
        print(f"  Found {len(roots)} roots — unexpected count.")


if __name__ == "__main__":
    main()
