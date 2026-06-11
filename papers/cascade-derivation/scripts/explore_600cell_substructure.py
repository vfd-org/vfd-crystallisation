#!/usr/bin/env python3
"""
Explore 600-cell substructures relevant to the cascade rungs.

Goals:
  1. Confirm basic 600-cell structure (120 vertices, 12-regular adjacency)
  2. Map the eigenvalue spectrum and multiplicity structure (irreps of H4)
  3. Look for natural 40-element substructures (cascade rung 40 candidate)
  4. Look for natural 16- and 24-element substructures (D4, 4-cube candidates)

Outputs printed to stdout. Intended as a Phase 1a exploratory pass —
results feed back into cascade-embeddings.md.
"""

import numpy as np
from collections import Counter

PHI = (1 + np.sqrt(5)) / 2

DATA = "scripts/600cell_data.npz"


def load():
    d = np.load(DATA)
    return d["vertices"], d["adjacency"], d["laplacian"], d["eigenvalues"]


def basic_structure(verts, adj):
    print("=" * 70)
    print("1. BASIC STRUCTURE")
    print("=" * 70)
    print(f"  Vertices: {verts.shape[0]} in R^{verts.shape[1]}")
    norms = np.linalg.norm(verts, axis=1)
    print(f"  Vertex norms: min={norms.min():.6f}, max={norms.max():.6f}  (should all be 1)")

    degrees = adj.sum(axis=1)
    print(f"  Vertex degrees: min={degrees.min()}, max={degrees.max()}, "
          f"all-equal={len(set(degrees)) == 1}")
    print(f"    (kissing number of 600-cell = 12)")

    # Edges
    edges = adj.sum() // 2
    print(f"  Edge count: {edges}  (600-cell has 720 edges)")


def spectrum_irreps(eigs):
    print()
    print("=" * 70)
    print("2. EIGENVALUE SPECTRUM (Laplacian irrep multiplicities)")
    print("=" * 70)

    # Round to handle floating-point
    rounded = np.round(eigs, 6)
    counter = Counter(rounded)
    print(f"  Distinct eigenvalues: {len(counter)}")
    print()
    print(f"  {'eigenvalue':>14}  {'multiplicity':>12}")
    print(f"  {'-'*14}  {'-'*12}")
    for ev, mult in sorted(counter.items()):
        print(f"  {ev:>14.6f}  {mult:>12d}")

    print()
    print("  Multiplicity counts:")
    mult_counter = Counter(counter.values())
    for mult, count in sorted(mult_counter.items()):
        print(f"    multiplicity {mult}:  appears {count} time(s)")
    print()
    print(f"  Total multiplicity: {sum(counter.values())}  (should be 120)")

    # Look for multiplicity 40 specifically (cascade rung)
    print()
    print(f"  Cascade-rung candidates in multiplicity:")
    for target in (40, 24, 16, 8):
        hits = [ev for ev, m in counter.items() if m == target]
        if hits:
            print(f"    multiplicity {target}: eigenvalues {sorted(hits)}")
        else:
            print(f"    multiplicity {target}: NONE")


def find_24_cell_inside(verts):
    """The 600-cell vertices include the 24-cell vertices (the 8 axis vertices
    + 16 half-integer vertices form the 24-cell).
    """
    print()
    print("=" * 70)
    print("3. D4 24-CELL EMBEDDING IN 600-CELL")
    print("=" * 70)

    is_axis = np.array([
        sum(1 for c in v if abs(c) > 0.99) == 1 and
        sum(1 for c in v if abs(c) < 1e-6) == 3
        for v in verts
    ])
    is_half = np.array([
        all(abs(abs(c) - 0.5) < 1e-6 for c in v)
        for v in verts
    ])

    n_axis = is_axis.sum()
    n_half = is_half.sum()
    print(f"  Axis vertices (perms of (±1,0,0,0)):    {n_axis}  (expected 8)")
    print(f"  Half vertices ((±1/2,±1/2,±1/2,±1/2)):  {n_half}  (expected 16)")
    print(f"  Combined (D4 24-cell candidate):        {n_axis + n_half}  (expected 24)")

    twentyfour_cell_indices = np.where(is_axis | is_half)[0]
    print(f"  → These 24 vertices form the D4 root polytope (24-cell) inside H4.")
    return twentyfour_cell_indices


def find_tesseract_inside(verts):
    """The 16 half-integer vertices form a 4-cube (tesseract)."""
    print()
    print("=" * 70)
    print("4. TESSERACT (4-CUBE, 16 VERTICES) INSIDE 600-CELL")
    print("=" * 70)

    is_half = np.array([
        all(abs(abs(c) - 0.5) < 1e-6 for c in v)
        for v in verts
    ])
    tess_indices = np.where(is_half)[0]
    print(f"  Half-integer vertices found: {len(tess_indices)}  (expected 16)")
    print(f"  → These form the 4-cube (tesseract) — cascade rung 16.")
    print(f"  → Each vertex labelled by a sign pattern (s1,s2,s3,s4) ∈ {{±}}^4")
    print(f"  → Z_2^4 grading suggests Cl(1,3) Dirac algebra identification.")
    return tess_indices


def find_third_type_count(verts):
    """The 96 type-3 vertices ((0, ±1/(2φ), ±1/2, ±φ/2) even perms)."""
    print()
    print("=" * 70)
    print("5. TYPE-3 VERTICES (the φ-bearing 96)")
    print("=" * 70)

    a = 1 / (2 * PHI)
    b = 0.5
    c = PHI / 2
    base = sorted([0.0, a, b, c])

    is_type3 = []
    for v in verts:
        sorted_abs = sorted(abs(x) for x in v)
        match = all(abs(sorted_abs[i] - base[i]) < 1e-6 for i in range(4))
        is_type3.append(match)
    is_type3 = np.array(is_type3)
    n3 = is_type3.sum()
    print(f"  Type-3 vertices: {n3}  (expected 96)")
    print(f"  → Carry the φ structure explicitly (1/(2φ), 1/2, φ/2)")
    print()
    print(f"  Total breakdown: 8 (axis) + 16 (half) + 96 (φ-bearing) = {8+16+96}")


def look_for_40(verts, adj, eigs):
    """Look for natural 40-element substructures."""
    print()
    print("=" * 70)
    print("6. LOOKING FOR THE CASCADE RUNG 40")
    print("=" * 70)

    # 6a. Check eigenvalue multiplicity 40
    rounded = np.round(eigs, 6)
    counter = Counter(rounded)
    mults = [m for m in counter.values()]
    if 40 in mults:
        print(f"  ✓ An eigenvalue of multiplicity 40 EXISTS in the H4 Laplacian.")
        for ev, m in counter.items():
            if m == 40:
                print(f"    eigenvalue = {ev:.6f}, multiplicity = {m}")
    else:
        print(f"  ✗ No eigenvalue of multiplicity 40 in the H4 Laplacian.")
        print(f"    (Multiplicities present: {sorted(set(mults))})")

    # 6b. 96 / 40 ratio? 120 / 40 = 3 — orbit structure under triality-like S_3?
    print()
    print(f"  120 / 40 = 3  →  three orbits of 40 vertices?")
    print(f"  96 / 3 = 32, 8 + 16 + 96 = 120, so a 3-orbit decomposition")
    print(f"  must NOT respect the (8,16,96) classification.")
    print()

    # 6c. Type-3 vertices: 96, partition into permutation classes?
    a = 1 / (2 * PHI)
    b = 0.5
    c = PHI / 2

    # Each type-3 vertex has one zero coordinate. Group by which coord is zero.
    print(f"  Partitioning the 96 type-3 vertices by zero-coordinate position:")
    zero_pos_count = Counter()
    for v in verts:
        sorted_abs = sorted(abs(x) for x in v)
        if all(abs(sorted_abs[i] - sorted([0.0, a, b, c])[i]) < 1e-6 for i in range(4)):
            zero_pos = next(i for i in range(4) if abs(v[i]) < 1e-6)
            zero_pos_count[zero_pos] += 1
    for pos, ct in sorted(zero_pos_count.items()):
        print(f"    zero in coord {pos}: {ct} vertices")
    print(f"    Total: {sum(zero_pos_count.values())}")
    if all(v == 24 for v in zero_pos_count.values()):
        print(f"  → 96 splits as 4 × 24 by zero-position. (D4 24-cell-like blocks?)")

    # 6d. Cell count for the Hopf-fibre interpretation
    print()
    print(f"  600 cells / 40 = 15  →  15 icosahedral fibres of 40 cells")
    print(f"  This is the Hopf foliation interpretation (Conway-Sloane).")
    print(f"  We don't have cell data here, only vertex/adjacency.")
    print(f"  → Open task: build cell list and verify 15 × 40 fibration.")

    # 6e. Look at second-neighbours, third-neighbours, etc.
    print()
    print(f"  Distance-shell sizes from a fixed vertex:")
    A = adj.astype(int)
    visited = np.zeros(120, dtype=bool)
    visited[0] = True
    shell = np.array([0])
    for r in range(1, 7):
        new = np.zeros(120, dtype=bool)
        for v in shell:
            new |= (A[v] > 0)
        new &= ~visited
        shell = np.where(new)[0]
        visited |= new
        if len(shell) == 0:
            break
        print(f"    shell radius {r}: {len(shell)} vertices  (cumulative {visited.sum()})")
    print(f"    (600-cell shell sizes from one vertex are: 1, 12, 20, 12, 30, 12, 20, 12, 1)")


def main():
    verts, adj, lap, eigs = load()
    basic_structure(verts, adj)
    spectrum_irreps(eigs)
    find_24_cell_inside(verts)
    find_tesseract_inside(verts)
    find_third_type_count(verts)
    look_for_40(verts, adj, eigs)
    print()
    print("=" * 70)
    print("DONE")
    print("=" * 70)


if __name__ == "__main__":
    main()
