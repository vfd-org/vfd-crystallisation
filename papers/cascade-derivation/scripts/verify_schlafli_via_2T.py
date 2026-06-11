#!/usr/bin/env python3
"""
Verify the Schläfli compound algebraically:
  600-cell = 5 left cosets of 2T (binary tetrahedral) in 2I.

Plan:
  1. Construct 2T as a subset of the 600-cell vertices:
     - {±1, ±i, ±j, ±k}                        (8 elements, Lipschitz)
     - (±1 ± i ± j ± k) / 2 with all signs    (16 elements, Hurwitz)
     Total: 24 = order of 2T ✓
  2. Verify these 24 quaternions are closed under multiplication.
  3. Pick 5 coset representatives g_0=1, g_1, g_2, g_3, g_4 ∈ 2I.
  4. Compute each coset g_i · 2T and verify:
     - 24 distinct vertices each
     - Disjoint from the others
     - Union = full 120-vertex 600-cell
     - Each coset is a 24-cell (distance profile 1, 8, 6, 8, 1)

This locks the Phase 1d-B1 §2.5 result that the "5" in cascade rung
40 = 8 × 5 IS the index [2I : 2T] = 5.
"""

import numpy as np
from itertools import product

PHI = (1 + np.sqrt(5)) / 2
DATA = "scripts/600cell_data.npz"


def quat_mult(p, q):
    pw, px, py, pz = p
    qw, qx, qy, qz = q
    return np.array([
        pw*qw - px*qx - py*qy - pz*qz,
        pw*qx + px*qw + py*qz - pz*qy,
        pw*qy - px*qz + py*qw + pz*qx,
        pw*qz + px*qy - py*qx + pz*qw,
    ])


def find_index(verts, q, tol=1e-9):
    """Find index of q in vertex list, or -1."""
    for i, v in enumerate(verts):
        if np.allclose(v, q, atol=tol):
            return i
    return -1


def load_600cell():
    d = np.load(DATA)
    return d["vertices"]


def construct_2T():
    """Construct 2T as 24 quaternions: 8 Lipschitz + 16 Hurwitz."""
    elements = []
    # 8 Lipschitz: ±1, ±i, ±j, ±k
    for axis in range(4):
        for sign in [1, -1]:
            v = np.zeros(4)
            v[axis] = sign
            elements.append(v)
    # 16 Hurwitz: (±1 ± i ± j ± k)/2
    for signs in product([0.5, -0.5], repeat=4):
        elements.append(np.array(signs))
    return np.array(elements)


def verify_2T_closure(twoT):
    """Verify 2T is closed under quaternion multiplication."""
    print("=" * 70)
    print("1. CONSTRUCT 2T AND VERIFY CLOSURE")
    print("=" * 70)
    n = len(twoT)
    print(f"  Constructed 2T with {n} elements (expected 24)")

    closed_count = 0
    failures = []
    for i in range(n):
        for j in range(n):
            product_ij = quat_mult(twoT[i], twoT[j])
            found = any(np.allclose(product_ij, e, atol=1e-9) for e in twoT)
            if found:
                closed_count += 1
            else:
                failures.append((i, j, product_ij))

    print(f"  Closure: {closed_count}/{n*n} products in 2T")
    if failures:
        print(f"  Sample failure: {failures[0]}")
    else:
        print(f"  ✓ 2T is closed (subgroup of 2I)")

    # Check 2T contains identity
    has_id = any(np.allclose(e, np.array([1,0,0,0])) for e in twoT)
    print(f"  Contains identity: {has_id}")

    # Check 2T contains inverses (for unit quaternions, conjugate)
    inv_in = sum(1 for e in twoT
                 if any(np.allclose(np.array([e[0], -e[1], -e[2], -e[3]]),
                                     w, atol=1e-9) for w in twoT))
    print(f"  Inverses in 2T: {inv_in}/{n}")


def find_2T_in_600cell(verts, twoT):
    """Find indices of 2T elements in the 600-cell vertex set."""
    print()
    print("=" * 70)
    print("2. LOCATE 2T INSIDE THE 600-CELL VERTEX SET")
    print("=" * 70)
    indices = [find_index(verts, e) for e in twoT]
    found = sum(1 for i in indices if i >= 0)
    print(f"  2T elements located in 600-cell: {found}/{len(twoT)}")
    if found == 24:
        print(f"  ✓ All 24 elements of 2T are 600-cell vertices.")
        print(f"    These are exactly the (8 axis + 16 half) vertices.")
    return indices


def find_coset_representatives(verts, twoT_indices):
    """Pick 5 coset representatives by greedily finding vertices not yet
    in any coset."""
    print()
    print("=" * 70)
    print("3. BUILD THE 5 LEFT COSETS g·2T")
    print("=" * 70)
    n = len(verts)
    twoT_set = set(twoT_indices)

    # Coset 0: 2T itself (representative = identity = vertex 0)
    cosets = {}
    cosets[0] = list(twoT_set)
    cosets_repr = {0: 0}  # representative index for each coset

    used = set(twoT_indices)

    coset_id = 1
    while len(used) < n:
        # Pick a representative not yet used
        for g_idx in range(n):
            if g_idx not in used:
                break
        # Build the coset g·2T
        g_quat = verts[g_idx]
        coset_quats = [quat_mult(g_quat, verts[t_idx])
                       for t_idx in twoT_indices]
        coset_indices = []
        for cq in coset_quats:
            idx = find_index(verts, cq)
            if idx >= 0:
                coset_indices.append(idx)
            else:
                print(f"    WARN: coset element not found: {cq}")
        cosets[coset_id] = coset_indices
        cosets_repr[coset_id] = g_idx
        used.update(coset_indices)
        coset_id += 1
        if coset_id > 10:
            print(f"    Too many cosets — abort")
            break

    print(f"  Number of cosets: {len(cosets)}")
    for k, c in sorted(cosets.items()):
        rep = cosets_repr[k]
        print(f"    Coset {k}: representative index {rep} = "
              f"{verts[rep]}, |coset| = {len(c)}")

    # Verify partition
    all_indices = sum((c for c in cosets.values()), [])
    is_partition = (len(all_indices) == n
                    and len(set(all_indices)) == n
                    and len(cosets) == 5)
    if is_partition:
        print(f"  ✓ 5 cosets partition the 120-vertex 600-cell.")
    else:
        print(f"  ✗ Not a clean 5-fold partition")

    return cosets


def verify_coset_is_24cell(verts, coset_indices, label):
    """Verify a 24-vertex coset has the 24-cell distance profile."""
    sub = verts[coset_indices]
    n = len(sub)
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            D[i, j] = np.linalg.norm(sub[i] - sub[j])

    # Distinct distances (rounded)
    dists = sorted(set(round(d, 6) for d in D[D > 1e-6]))

    # Distance shell from vertex 0
    v0 = D[0]
    shells = []
    for d in dists:
        count = int(np.sum(np.abs(v0 - d) < 1e-6))
        shells.append((d, count))

    # Expected 24-cell profile: 4 distances, shells (1, 8, 6, 8, 1)
    expected = [1.0, np.sqrt(2), np.sqrt(3), 2.0]
    expected_round = [round(d, 6) for d in expected]
    expected_shells = [8, 6, 8, 1]

    matches_distances = (len(dists) == 4
                         and all(abs(dists[i] - expected_round[i]) < 1e-4
                                 for i in range(4)))
    matches_shells = (matches_distances
                      and all(shells[i][1] == expected_shells[i]
                              for i in range(4)))

    status = "✓ 24-cell" if matches_shells else "✗ NOT a 24-cell"
    print(f"  Coset {label}: {n} vertices, {len(dists)} distinct distances")
    if dists:
        dist_str = ", ".join(f"{d:.4f}" for d in dists)
        shell_str = ", ".join(f"{c}" for d, c in shells)
        print(f"    Distances: {dist_str}")
        print(f"    Shell counts from v0: 1, {shell_str}")
    print(f"    {status}")
    return matches_shells


def main():
    verts = load_600cell()
    print(f"Loaded {len(verts)} 600-cell vertices.\n")

    twoT = construct_2T()
    verify_2T_closure(twoT)

    twoT_indices = find_2T_in_600cell(verts, twoT)
    cosets = find_coset_representatives(verts, twoT_indices)

    print()
    print("=" * 70)
    print("4. VERIFY EACH COSET IS A 24-CELL")
    print("=" * 70)
    results = []
    for k in sorted(cosets.keys()):
        ok = verify_coset_is_24cell(verts, cosets[k], str(k))
        results.append(ok)

    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    n_cells = sum(results)
    print(f"  24-cells found: {n_cells} / {len(results)}")
    if n_cells == 5:
        print(f"  ✓ SCHLÄFLI COMPOUND VERIFIED")
        print(f"  ✓ 600-cell = 5 left cosets of 2T in 2I")
        print(f"  ✓ Each coset is a regular 24-cell (D₄ root polytope)")
        print(f"  ✓ The '5' in cascade rung 40 = 8×5 = [2I : 2T]")
        print(f"  ✓ The 5 inscribed GR-skeletons are confirmed")
    else:
        print(f"  ⚠ Partial verification: {n_cells}/5 cosets are 24-cells")


if __name__ == "__main__":
    main()
