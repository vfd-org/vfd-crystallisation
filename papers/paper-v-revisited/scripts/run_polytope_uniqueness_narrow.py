#!/usr/bin/env python3
"""
Narrow uniqueness theorem: among the 11 regular polytopes in dimensions 3
and 4, the 600-cell is the unique one whose Laplacian spectrum contains both
(i) values in Q(sqrt(5)) \ Q, and (ii) the rational value 15.

Previously: Paper V carried a Remark acknowledging that a naive "unique to
have sqrt(5) eigenvalues" claim is false (icosahedron and dodecahedron also
have sqrt(5) eigenvalues). This script upgrades that Remark to an exact
uniqueness theorem by pairing the sqrt(5) property with the rational-15
property.

Computation:
  - Build the vertex graph of each of the 11 regular polytopes.
  - Compute its graph Laplacian L = D - A.
  - Test (i) presence of a non-rational eigenvalue in Q(sqrt(5)), and
         (ii) presence of the rational eigenvalue 15.
  - Report the joint-match table and the unique member satisfying both.
"""

from __future__ import annotations

import itertools
from fractions import Fraction

import numpy as np


PHI = (1 + np.sqrt(5)) / 2


def _eigs(A):
    L = np.diag(A.sum(axis=1)) - A
    evals = np.sort(np.linalg.eigvalsh(L))
    return evals


def _round_near_integer(evals, tol=1e-6):
    """Round eigenvalues that are extremely close to an integer to exact."""
    out = []
    for e in evals:
        if abs(e - round(e)) < tol:
            out.append(float(round(e)))
        else:
            out.append(float(e))
    return np.array(out)


def _has_sqrt5_component(evals, tol=1e-6):
    """Detect presence of a + b*sqrt(5) with b != 0 integer/half-integer rational.

    Heuristic: for each eigenvalue e, check whether there exist small rationals
    a, b with a + b*sqrt(5) ~ e and b != 0, to tolerance tol.
    """
    for e in evals:
        # Try small denominators
        for denom in (1, 2, 3, 4, 5, 6):
            for b_num in range(-20, 21):
                for a_num in range(-30, 31):
                    a = a_num / denom
                    b = b_num / denom
                    if b == 0:
                        continue
                    if abs(e - (a + b * np.sqrt(5))) < tol:
                        return True, (a, b)
    return False, None


def _has_eigenvalue_15(evals, tol=1e-6):
    return any(abs(e - 15) < tol for e in evals)


# ---------------------------------------------------------------------------
# Polytope vertex constructions
# ---------------------------------------------------------------------------

def _dedup(verts, tol=1e-9):
    out = []
    for v in verts:
        if not any(np.allclose(v, u, atol=tol) for u in out):
            out.append(v)
    return np.array(out)


def tetrahedron():
    # 4 vertices of a tetrahedron; e.g. (1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)
    return np.array([
        [1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]
    ], dtype=float)


def cube():
    return np.array(list(itertools.product([-1, 1], repeat=3)), dtype=float)


def octahedron():
    V = []
    for i in range(3):
        for s in (+1, -1):
            v = [0, 0, 0]
            v[i] = s
            V.append(v)
    return np.array(V, dtype=float)


def dodecahedron():
    V = []
    ip = 1 / PHI
    # 8 vertices: (+-1, +-1, +-1)
    for signs in itertools.product([-1, 1], repeat=3):
        V.append(np.array(signs, dtype=float))
    # 12 vertices: cyclic permutations of (0, +-1/phi, +-phi)
    for cyc in [(0, ip, PHI), (PHI, 0, ip), (ip, PHI, 0)]:
        for s1 in (+1, -1):
            for s2 in (+1, -1):
                v = list(cyc)
                # Apply signs to nonzero positions
                for k in range(3):
                    if cyc[k] == ip:
                        v[k] = s1 * ip
                    elif cyc[k] == PHI:
                        v[k] = s2 * PHI
                V.append(np.array(v, dtype=float))
    V = _dedup(V)
    assert len(V) == 20, f"expected 20 dodecahedron vertices, got {len(V)}"
    return V


def icosahedron():
    V = []
    ip = 1 / PHI
    # Cyclic perms of (0, +-1, +-phi)
    for perm in [(0, 1, PHI), (1, PHI, 0), (PHI, 0, 1)]:
        for s1 in (+1, -1):
            for s2 in (+1, -1):
                v = (perm[0] if perm[0] != 0 else 0, s1 * perm[1], s2 * perm[2])
                V.append(v)
        # Also handle permutation with 0 in different positions properly
    # Simpler: even permutations of (0, +-1, +-phi) give 12 vertices
    V = []
    for perm in [(0, 1, PHI), (1, PHI, 0), (PHI, 0, 1)]:
        for s1 in (+1, -1):
            for s2 in (+1, -1):
                v = list(perm)
                # Apply signs to nonzero coords
                for k in range(3):
                    if v[k] == 1 or v[k] == PHI:
                        # assign sign
                        pass
                # Easier: handle directly
                v_tup = [0.0, 0.0, 0.0]
                # put 0 where perm has 0, and +-1 / +-phi as per the signs
                for k in range(3):
                    if perm[k] == 0:
                        v_tup[k] = 0.0
                    elif perm[k] == 1:
                        v_tup[k] = s1 * 1.0
                    else:  # PHI
                        v_tup[k] = s2 * PHI
                V.append(tuple(v_tup))
    V = _dedup([np.array(v, dtype=float) for v in V])
    assert len(V) == 12, f"expected 12 icosahedron vertices, got {len(V)}"
    return V


def fivecell():
    # 5-cell (4-simplex): 5 vertices in R^4 at equal distance from each other.
    # Use 5 standard basis vectors in R^5 and project to R^4 via centering.
    basis = np.eye(5)
    center = np.mean(basis, axis=0)
    V_R5 = basis - center  # sum-zero 4-dimensional subspace
    # Project to R^4 using a random orthonormal basis for the sum-zero subspace.
    # Compute orthonormal basis: use SVD of V_R5 to get the 4-dim range.
    U, S, Vt = np.linalg.svd(V_R5, full_matrices=False)
    V_R4 = V_R5 @ Vt.T[:, :4]  # (5, 4)
    return V_R4


def eightcell():
    # Tesseract: 16 vertices at all sign combinations of (+-1, +-1, +-1, +-1)
    return np.array(list(itertools.product([-1, 1], repeat=4)), dtype=float)


def sixteencell():
    # Cross-polytope in 4D: 8 vertices (+-1,0,0,0) and permutations
    V = []
    for i in range(4):
        for s in (+1, -1):
            v = [0, 0, 0, 0]
            v[i] = s
            V.append(v)
    return np.array(V, dtype=float)


def twentyfourcell():
    # 24 vertices:
    # 8 of the form (+-1, 0, 0, 0) permutations (16-cell)
    # 16 of the form (+-1/2, +-1/2, +-1/2, +-1/2) (tesseract, scaled)
    V = []
    for i in range(4):
        for s in (+1, -1):
            v = [0, 0, 0, 0]
            v[i] = s
            V.append(v)
    for signs in itertools.product([+1, -1], repeat=4):
        V.append([0.5 * s for s in signs])
    V = np.array(V, dtype=float)
    assert V.shape == (24, 4)
    return V


def sixhundredcell():
    # 120 vertices; same construction as run_rd4_absorbing_chain.py
    from run_rd4_absorbing_chain import build_600cell_vertices
    return build_600cell_vertices()


def onehundredtwentycell():
    # 120-cell has 600 vertices. Construct via the standard coordinates:
    # All permutations of (0, 0, +-2, +-2), (+-1, +-1, +-1, +-sqrt(5)),
    # (+-1/phi^2, +-phi, +-phi, +-phi), and various other combinations.
    # For our purpose (checking eigenvalues 15 and sqrt(5)-valued), we note:
    # the 120-cell is dual to the 600-cell. It has 600 vertices, each of
    # degree 4 (so max Laplacian eigenvalue <= 8). Therefore it CANNOT have
    # 15 as an eigenvalue. This is enough for the narrow theorem.
    # But we still need to detect sqrt(5) presence.
    # Use a placeholder: we return None and handle it by the degree argument.
    return None


def build_adjacency_by_nearest_neighbour(verts, tol=1e-9):
    """Build adjacency by shortest non-zero pairwise distance."""
    n = len(verts)
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            d = np.linalg.norm(verts[i] - verts[j])
            D[i, j] = d
            D[j, i] = d
    # Find min non-zero distance
    nz = D[D > tol]
    d_min = nz.min()
    A = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            if i != j and abs(D[i, j] - d_min) < tol:
                A[i, j] = 1
    return A, d_min


# ---------------------------------------------------------------------------
# Main test
# ---------------------------------------------------------------------------

def main():
    print("=" * 72)
    print("Narrow uniqueness theorem: among 11 regular polytopes in dim 3+4,")
    print("the 600-cell is the unique one whose Laplacian spectrum contains")
    print("BOTH sqrt(5)-valued entries AND the rational value 15.")
    print("=" * 72)

    polytopes = [
        ("tetrahedron",        tetrahedron),
        ("cube",               cube),
        ("octahedron",         octahedron),
        ("dodecahedron",       dodecahedron),
        ("icosahedron",        icosahedron),
        ("5-cell",             fivecell),
        ("8-cell (tesseract)", eightcell),
        ("16-cell",            sixteencell),
        ("24-cell",            twentyfourcell),
        ("600-cell",           sixhundredcell),
    ]
    # The 120-cell we handle by the degree argument (degree 4, max L <= 8, no 15).

    results = []
    for name, build in polytopes:
        verts = build()
        A, dmin = build_adjacency_by_nearest_neighbour(verts)
        degree = int(A.sum(axis=1)[0])
        evals = _round_near_integer(_eigs(A))
        has_sqrt5, sqrt5_form = _has_sqrt5_component(evals)
        has_15 = _has_eigenvalue_15(evals)
        distinct = sorted(set(round(e, 6) for e in evals))
        results.append((name, len(verts), degree, distinct, has_sqrt5, has_15))
        print(f"\n{name}: |V|={len(verts)}, degree={degree}")
        print(f"  distinct eigenvalues: {distinct}")
        print(f"  has sqrt(5)-valued entry: {has_sqrt5} {sqrt5_form if sqrt5_form else ''}")
        print(f"  has rational eigenvalue 15: {has_15}")

    # 120-cell: degree 4, so max L eigenvalue <= 2*4 = 8, which excludes 15.
    # (This is a standard fact: for a d-regular graph, max L eigenvalue <= 2d.)
    print(f"\n120-cell (not built): degree = 4 (dual of 600-cell); max L <= 8, so no 15.")
    results.append(("120-cell", 600, 4, None, None, False))

    # Summarize joint-match:
    print()
    print("=" * 72)
    print("Joint-match table: has sqrt(5) AND has 15")
    print("=" * 72)
    joint = [r for r in results if r[4] is True and r[5] is True]
    for name, nV, deg, _, has_sqrt5, has_15 in results:
        joint_mark = " <-- " if has_sqrt5 and has_15 else ""
        print(f"  {name:<24} sqrt5={str(has_sqrt5):<5}  15={str(has_15):<5}{joint_mark}")
    print()
    if len(joint) == 1 and joint[0][0] == "600-cell":
        print("THEOREM VERIFIED: the 600-cell is the unique member with both properties.")
    else:
        print(f"THEOREM NOT VERIFIED: {len(joint)} match(es) found: {[j[0] for j in joint]}")


if __name__ == "__main__":
    main()
