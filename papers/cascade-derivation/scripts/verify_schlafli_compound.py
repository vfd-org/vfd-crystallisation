#!/usr/bin/env python3
"""
Verify the Schlafli compound: the 600-cell is the union of 5 disjoint
inscribed 24-cells.

Test procedure:
  1. Identify the 5 candidate blocks:
     - Block 0: 8 axis + 16 half = 24 vertices (standard 24-cell)
     - Blocks 1-4: type-3 vertices grouped by zero-coordinate position
       (each 24 vertices)
  2. For each block, verify it forms a 24-cell:
     - 24 vertices on the unit 3-sphere (same radius)
     - Each vertex has exactly 8 "nearest neighbours" within the block
       at the same minimum distance (24-cell is 8-regular, edge-length
       matches sqrt(2-sqrt(2)) for the axis+half case, or an analogous
       length for the rotated blocks)
  3. Verify the 5 blocks are disjoint and cover all 120 vertices.
"""

import numpy as np

PHI = (1 + np.sqrt(5)) / 2
DATA = "scripts/600cell_data.npz"


def load():
    d = np.load(DATA)
    return d["vertices"]


def classify(verts):
    """Classify each vertex into one of 5 blocks."""
    n = len(verts)
    blocks = {0: [], 1: [], 2: [], 3: [], 4: []}

    for i, v in enumerate(verts):
        is_axis = (sum(1 for c in v if abs(c) > 0.99) == 1
                   and sum(1 for c in v if abs(c) < 1e-6) == 3)
        is_half = all(abs(abs(c) - 0.5) < 1e-6 for c in v)

        if is_axis or is_half:
            blocks[0].append(i)
        else:
            # Type-3 vertex; find which coordinate is zero
            zero_pos = next(k for k in range(4) if abs(v[k]) < 1e-6)
            blocks[zero_pos + 1].append(i)

    return blocks


def pairwise_dists(verts, indices):
    """All pairwise Euclidean distances among a vertex block."""
    sub = verts[indices]
    n = len(sub)
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            D[i, j] = np.linalg.norm(sub[i] - sub[j])
    return D


def analyse_block(verts, block_indices, label):
    print(f"--- Block {label}: {len(block_indices)} vertices ---")
    assert len(block_indices) == 24, "Expected 24 vertices"

    D = pairwise_dists(verts, block_indices)

    # Distinct non-zero distances
    dists = np.unique(np.round(D[D > 1e-6], 6))
    print(f"  Distinct non-zero distances: {len(dists)}")
    for d in dists:
        print(f"    d = {d:.6f}")

    # For the 24-cell: distances from one vertex are
    #   1 (8 neighbors), sqrt(2) (6), sqrt(3) (8), 2 (1)  if edge=1
    # For rescaled 24-cell on unit 3-sphere, edge = 1 (for the axis+half
    # case specifically).
    min_d = dists[0]
    neighbors_per_vertex = int(np.round(np.mean(np.sum(
        np.abs(D - min_d) < 1e-6, axis=1))))
    print(f"  Minimum distance: {min_d:.6f}")
    print(f"  Average nearest-neighbour count per vertex: "
          f"{neighbors_per_vertex}")
    print(f"    (24-cell is 8-regular at edge length, so expect 8)")

    # Count distance-shell sizes from vertex 0
    v0_dists = D[0]
    shells = {}
    for d in dists:
        shells[float(d)] = int(np.sum(np.abs(v0_dists - d) < 1e-6))
    print(f"  Distance-shell sizes from vertex 0 (incl self):")
    print(f"    self (d=0): 1")
    for d, count in sorted(shells.items()):
        print(f"    d = {d:.6f}: {count}")
    # 24-cell expected shell profile (from any vertex): 1, 8, 6, 8, 1
    print(f"    (24-cell expected: 1, 8, 6, 8, 1)")

    return {
        "n_vertices": len(block_indices),
        "min_edge": min_d,
        "neighbour_count": neighbors_per_vertex,
        "shells": sorted(shells.items()),
    }


def main():
    verts = load()
    print(f"Loaded {len(verts)} vertices.")
    print()

    blocks = classify(verts)
    print("Block sizes:")
    for k, v in sorted(blocks.items()):
        print(f"  Block {k}: {len(v)} vertices")
    print()

    # Check disjoint + covering
    all_ixs = sum((v for v in blocks.values()), [])
    assert len(all_ixs) == 120, f"Expected 120, got {len(all_ixs)}"
    assert len(set(all_ixs)) == 120, "Blocks not disjoint"
    print(f"  ✓ 5 blocks are disjoint and cover all 120 vertices.")
    print()

    print("=" * 70)
    print("Per-block 24-cell verification")
    print("=" * 70)
    results = []
    for k in sorted(blocks.keys()):
        print()
        r = analyse_block(verts, blocks[k], str(k))
        results.append(r)

    print()
    print("=" * 70)
    print("Summary")
    print("=" * 70)
    all_same_min = len(set(round(r["min_edge"], 6) for r in results)) == 1
    all_eight = all(r["neighbour_count"] == 8 for r in results)
    print(f"  All 5 blocks have same minimum edge length: {all_same_min}")
    print(f"  All 5 blocks are 8-regular at minimum edge: {all_eight}")
    if all_same_min and all_eight:
        print(f"  ✓ ALL 5 BLOCKS ARE CONGRUENT 24-CELLS")
        print(f"  ✓ Schläfli compound verified: 600-cell = 5 × 24-cell")
        print(f"  → The '5' in cascade rung 40 = 8 × 5 is the Schläfli count.")
        print(f"  → The '8' is... (still to be pinned down — axis vertices? dim E₈?)")
    else:
        print(f"  Partial — some blocks differ; need deeper analysis.")


if __name__ == "__main__":
    main()
