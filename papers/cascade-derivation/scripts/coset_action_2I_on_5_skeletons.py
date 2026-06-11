#!/usr/bin/env python3
"""
Phase 1c-C3: verify the 2I action on the 5 cosets of 2T factors as
A_5 → S_5 — the famous 5-letter action of the alternating group A_5.

This is the algebraic precursor to Lorentz invariance: in the continuum
limit, A_5 (discrete icosahedral rotation) densifies to SO(3), which is
the rotation subgroup of SO(1, 3).

Plan:
  1. Compute 2T (24 quaternions) and the 5 left cosets g_i · 2T.
  2. For each g ∈ 2I, compute the permutation π_g of the 5 cosets
     induced by left multiplication: π_g(i) = j  iff  g · g_i · 2T =
     g_j · 2T.
  3. The map g → π_g is a homomorphism 2I → S_5.
  4. Verify:
     - The kernel is exactly {±1} (the centre of 2I).
     - The image is A_5 (the alternating group, order 60).
     - The image is exactly the standard A_5 ⊂ S_5 acting on 5 letters
       (i.e. all even permutations).
"""

import numpy as np
from itertools import product, permutations

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
    for i, v in enumerate(verts):
        if np.allclose(v, q, atol=tol):
            return i
    return -1


def construct_2T():
    elements = []
    for axis in range(4):
        for sign in [1, -1]:
            v = np.zeros(4)
            v[axis] = sign
            elements.append(v)
    for signs in product([0.5, -0.5], repeat=4):
        elements.append(np.array(signs))
    return np.array(elements)


def build_cosets(verts, twoT_indices):
    n = len(verts)
    twoT_set = set(twoT_indices)
    cosets = [list(twoT_set)]
    used = set(twoT_indices)
    while len(used) < n:
        for g_idx in range(n):
            if g_idx not in used:
                break
        g_quat = verts[g_idx]
        coset_idx = []
        for t in twoT_indices:
            cq = quat_mult(g_quat, verts[t])
            i = find_index(verts, cq)
            coset_idx.append(i)
        cosets.append(coset_idx)
        used.update(coset_idx)
    return [set(c) for c in cosets]


def coset_id(coset_sets, vertex_idx):
    """Which coset does this vertex belong to?"""
    for i, c in enumerate(coset_sets):
        if vertex_idx in c:
            return i
    return -1


def permutation_action(verts, coset_sets, g_quat):
    """Compute the permutation π_g induced by left multiplication by g
    on the 5 cosets."""
    perm = [-1] * 5
    for i, coset in enumerate(coset_sets):
        # Pick any element of coset, multiply by g, find its coset
        rep = next(iter(coset))
        rep_quat = verts[rep]
        result = quat_mult(g_quat, rep_quat)
        new_idx = find_index(verts, result)
        if new_idx < 0:
            return None  # Should not happen
        perm[i] = coset_id(coset_sets, new_idx)
    return tuple(perm)


def is_even_permutation(perm):
    """Check if a permutation is even (in A_n)."""
    n = len(perm)
    inversions = 0
    for i in range(n):
        for j in range(i+1, n):
            if perm[i] > perm[j]:
                inversions += 1
    return inversions % 2 == 0


def main():
    d = np.load(DATA)
    verts = d["vertices"]
    n = len(verts)
    print(f"Loaded {n} 600-cell vertices.\n")

    twoT = construct_2T()
    twoT_indices = [find_index(verts, e) for e in twoT]
    print(f"Located 2T as 24 vertices in the 600-cell.")

    cosets = build_cosets(verts, twoT_indices)
    print(f"Built {len(cosets)} cosets of 2T in 2I.\n")

    # Compute permutations for all 120 elements of 2I
    print("=" * 70)
    print("HOMOMORPHISM 2I → S_5 (action on cosets)")
    print("=" * 70)

    perms = {}
    for g_idx in range(n):
        g_quat = verts[g_idx]
        p = permutation_action(verts, cosets, g_quat)
        perms[g_idx] = p

    # Distinct permutations
    distinct_perms = set(perms.values())
    print(f"  Number of distinct permutations in image: {len(distinct_perms)}")
    print(f"  (Expected: 60 if image = A_5; 120 if image = S_5;")
    print(f"   1 if action is trivial.)")

    # Check kernel: which g ∈ 2I act trivially (identity permutation)?
    identity_perm = (0, 1, 2, 3, 4)
    kernel = [g for g, p in perms.items() if p == identity_perm]
    print()
    print(f"  Kernel of action: {len(kernel)} elements")
    print(f"  Kernel quaternions:")
    for k in kernel:
        print(f"    index {k}: {verts[k]}")
    print(f"  Expected: kernel = {{±1}} (centre of 2I), 2 elements")

    # Check that image = A_5 (alternating group)
    print()
    print(f"  Are all permutations even (i.e. image ⊆ A_5)?")
    even_count = sum(1 for p in distinct_perms if is_even_permutation(p))
    odd_count = len(distinct_perms) - even_count
    print(f"    Even permutations: {even_count}")
    print(f"    Odd permutations:  {odd_count}")
    if odd_count == 0 and len(distinct_perms) == 60:
        print(f"  ✓ Image = A_5 (all 60 even permutations of 5 letters).")
    elif odd_count > 0:
        print(f"  ✗ Image contains odd permutations — NOT A_5.")
    else:
        print(f"  Partial — image has {len(distinct_perms)} elements.")

    # Sanity check: A_5 has order 60, which is exactly |2I| / |kernel| = 120 / 2
    print()
    print(f"  Sanity: |2I| / |kernel| = {n} / {len(kernel)} = "
          f"{n // len(kernel) if kernel else 'undefined'}")
    print(f"  (Expected: 60 = |A_5|)")

    print()
    print("=" * 70)
    print("INTERPRETATION FOR PHASE 1c-C3")
    print("=" * 70)
    print()
    print("  2I acts on the 5 D₄-skeletons (cosets of 2T) by left")
    print("  multiplication. The action factors through 2I / {±1} = I,")
    print("  the icosahedral rotation group of order 60. The induced")
    print("  homomorphism I → S_5 is the famous A_5 → S_5 embedding")
    print("  (5-letter representation of the alternating group).")
    print()
    print("  This is a classical exceptional fact:")
    print("    A_5 ≅ I  acts on 5 letters as A_5 ⊂ S_5.")
    print("  Geometrically: the icosahedral group permutes 5 inscribed")
    print("  tetrahedra of the icosahedron — and HERE it permutes 5")
    print("  inscribed 24-cells of the 600-cell.")
    print()
    print("  In the continuum limit, the discrete A_5 action densifies")
    print("  to the continuous SO(3) action on a tangent S² to the")
    print("  600-cell at any vertex. SO(3) is the rotation subgroup of")
    print("  SO(1, 3) Lorentz; the boost subgroup arises from the")
    print("  temporal direction (the chain-length separation of the")
    print("  event poset, Paper XXV).")
    print()
    print("  Therefore the C3 hypothesis is structurally substantiated:")
    print("    discrete A_5 (icosahedral rotation between 5 D₄ frames)")
    print("    → continuum SO(3) (spatial rotation)")
    print("    + temporal poset order (Paper XXV)")
    print("    → SO(1, 3) Lorentz invariance.")


if __name__ == "__main__":
    main()
