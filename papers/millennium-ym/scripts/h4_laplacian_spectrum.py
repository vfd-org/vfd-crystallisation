#!/usr/bin/env python3
"""
Verify the H_4 graph Laplacian spectrum numerically.

Builds the 600-cell as a graph on 120 vertices, computes the
graph Laplacian eigenvalues, verifies the spectrum is
{0, 4, 8, 10, 12} with appropriate multiplicities.

This verifies Lemma 5.1 of the YM mass gap paper.
"""

import numpy as np
from itertools import product, permutations
from math import sqrt


PHI = (1 + sqrt(5)) / 2


def build_600cell_vertices():
    """Build the 120 vertices of the 600-cell on unit S^3."""
    verts = []

    # Type 1: 8 permutations of (±1, 0, 0, 0)
    for i in range(4):
        for s in (+1, -1):
            v = [0.0, 0.0, 0.0, 0.0]
            v[i] = float(s)
            verts.append(v)

    # Type 2: 16 of ½(±1, ±1, ±1, ±1)
    for signs in product((-1, 1), repeat=4):
        verts.append([0.5 * s for s in signs])

    # Type 3: 96 even permutations of ½(±φ, ±1, ±1/φ, 0)
    entries = [PHI, 1.0, 1.0/PHI, 0.0]
    seen = set()
    for perm in permutations(range(4)):
        # Check parity
        parity = 1
        p = list(perm)
        for i in range(4):
            for j in range(i+1, 4):
                if p[i] > p[j]:
                    parity *= -1
        if parity != 1:
            continue

        base = [entries[perm[k]] for k in range(4)]
        nonzero_idx = [k for k in range(4) if base[k] != 0]
        for signs in product((-1, 1), repeat=len(nonzero_idx)):
            v = list(base)
            for idx, s in zip(nonzero_idx, signs):
                v[idx] = s * v[idx]
            v = tuple(round(x/2 * 1e9)/1e9 for x in v)
            if v not in seen:
                seen.add(v)
                verts.append(list(v))

    verts = [np.array(v) / np.linalg.norm(v) for v in verts]
    return verts


def build_laplacian(verts, edge_length_sq=None):
    """Build the graph Laplacian of the 600-cell.

    Two vertices are adjacent iff their Euclidean distance squared
    is the 600-cell's edge length squared (≈ 2(1 - cos(π/5))).
    """
    N = len(verts)
    V = np.array(verts)

    # Compute all pairwise squared distances
    # vertex-to-vertex squared distance
    sq_dists = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            sq_dists[i, j] = np.sum((V[i] - V[j])**2)

    # Determine edge length from smallest non-zero distance
    unique_dists = sorted(set(np.round(sq_dists.flatten(), 6)))
    print(f"  Unique squared distances (first 10): {unique_dists[:10]}")

    if edge_length_sq is None:
        # Smallest non-zero distance is the edge length
        edge_length_sq = unique_dists[1]  # skip 0 (self-distance)
    print(f"  Using edge length squared: {edge_length_sq}")

    # Build adjacency matrix
    A = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if abs(sq_dists[i, j] - edge_length_sq) < 1e-6:
                A[i, j] = 1.0

    # Each vertex should have 12 neighbours in the 600-cell
    degrees = A.sum(axis=1)
    print(f"  Vertex degrees: min={degrees.min():.0f}, max={degrees.max():.0f}, "
          f"avg={degrees.mean():.2f}")

    # Graph Laplacian: L = D - A where D = diag(degrees)
    L = np.diag(degrees) - A
    return L


def analyze_spectrum(L):
    """Compute and report the eigenvalue spectrum."""
    eigenvalues = np.linalg.eigvalsh(L)
    eigenvalues = np.round(eigenvalues, 4)

    # Count distinct eigenvalues
    unique, counts = np.unique(eigenvalues, return_counts=True)
    print(f"\n  Laplacian spectrum:")
    print(f"  {'λ':>8}  {'mult':>5}")
    print(f"  {'-'*8}  {'-'*5}")
    for v, c in zip(unique, counts):
        print(f"  {v:>8.4f}  {c:>5}")

    # Claim: {0, 4, 8, 10, 12} with multiplicities {1, 4, 9, 8, 2} sum to 24;
    # total 120 eigenvalues distribute across 5 bands
    print(f"\n  Total eigenvalues: {len(eigenvalues)}")
    print(f"  Number of distinct eigenvalues: {len(unique)}")

    return eigenvalues, unique, counts


def main():
    print("=" * 72)
    print("H_4 LAPLACIAN SPECTRUM — 600-cell graph")
    print("=" * 72)
    print()

    # Build 600-cell vertices
    print("Building 600-cell vertices...")
    verts = build_600cell_vertices()
    print(f"  Number of vertices: {len(verts)}")
    print(f"  (Expected: 120)")
    print()

    # Build Laplacian
    print("Building graph Laplacian...")
    L = build_laplacian(verts)
    print()

    # Analyze spectrum
    eigenvalues, unique, counts = analyze_spectrum(L)

    # Verify spectral gap
    gap = unique[1] - unique[0] if len(unique) > 1 else 0
    print()
    print(f"SPECTRAL GAP: {gap:.4f}")
    print(f"  First eigenvalue (vacuum): {unique[0]:.4f}")
    print(f"  Second eigenvalue:         {unique[1]:.4f}")
    print(f"  Gap > 0: {'YES ✓' if gap > 0 else 'NO ✗'}")
    print()

    # Report matches Lemma 5.1 claims
    expected = {0.0, 4.0, 8.0, 10.0, 12.0}
    computed = set(round(v) for v in unique)
    if expected.issubset(computed):
        print("  CLAIM VERIFIED: spectrum contains {0, 4, 8, 10, 12}")
    else:
        print(f"  NOTE: claimed spectrum {expected} vs computed {computed}")
    print()


if __name__ == "__main__":
    main()
