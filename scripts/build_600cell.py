#!/usr/bin/env python3
"""
Construct the 600-cell vertex graph from first principles.

This is the computational foundation for all Level 2+ VFD computations.
Every vertex coordinate, every adjacency entry, every eigenvalue is
derived from the mathematical definition of the 600-cell — no physics
input, no SM imports, just geometry.

Outputs:
  - 120 vertex coordinates in R⁴ (unit 3-sphere)
  - 120×120 adjacency matrix
  - Complete Laplacian spectrum with irrep assignments
  - Hopf fiber decomposition (12 fibers × 10 vertices)
  - Verification against Paper XXII spectral data

Usage:
    python scripts/build_600cell.py
"""

import numpy as np
from itertools import product

PHI = (1 + np.sqrt(5)) / 2


def build_vertices():
    """
    Construct the 120 vertices of the 600-cell on the unit 3-sphere in R⁴.

    The vertices are the elements of the binary icosahedral group 2I,
    represented as unit quaternions. They consist of:
    - 8 vertices: permutations of (±1, 0, 0, 0)
    - 16 vertices: (±1/2, ±1/2, ±1/2, ±1/2)
    - 96 vertices: even permutations of (0, ±1/2, ±φ/2, ±1/(2φ))

    Total: 8 + 16 + 96 = 120
    """
    verts = []

    # Type 1: permutations of (±1, 0, 0, 0) — 8 vertices
    for i in range(4):
        for s in [1, -1]:
            v = [0, 0, 0, 0]
            v[i] = s
            verts.append(v)

    # Type 2: (±1/2, ±1/2, ±1/2, ±1/2) — 16 vertices
    for signs in product([0.5, -0.5], repeat=4):
        verts.append(list(signs))

    # Type 3: even permutations of (0, ±1/(2φ), ±1/2, ±φ/2) — 96 vertices
    # The four base values
    a, b, c = 1/(2*PHI), 0.5, PHI/2
    base = [0, a, b, c]

    # Even permutations of 4 elements = 12 permutations
    # (these are the even elements of S₄)
    even_perms = [
        (0,1,2,3), (0,2,3,1), (0,3,1,2),
        (1,0,3,2), (1,2,0,3), (1,3,2,0),
        (2,0,1,3), (2,1,3,0), (2,3,0,1),
        (3,0,2,1), (3,1,0,2), (3,2,1,0),
    ]

    for perm in even_perms:
        coords = [base[perm[i]] for i in range(4)]
        # Apply all sign combinations to the non-zero coordinates
        nonzero_indices = [i for i in range(4) if coords[i] != 0]
        for signs in product([1, -1], repeat=len(nonzero_indices)):
            v = list(coords)
            for idx, s in zip(nonzero_indices, signs):
                v[idx] *= s
            verts.append(v)

    verts = np.array(verts)

    # Remove duplicates (to machine precision)
    unique = []
    for v in verts:
        is_dup = False
        for u in unique:
            if np.linalg.norm(v - u) < 1e-10:
                is_dup = True
                break
        if not is_dup:
            unique.append(v)

    verts = np.array(unique)

    # Normalise to unit sphere
    norms = np.linalg.norm(verts, axis=1)
    verts = verts / norms[:, None]

    return verts


def build_adjacency(verts, tol=1e-8):
    """
    Build the adjacency matrix from vertex coordinates.

    Two vertices are connected (nearest neighbours) if their Euclidean
    distance equals 1/φ (the NN distance on the unit 600-cell).
    """
    N = len(verts)
    d_nn = 1.0 / PHI  # NN distance

    # Compute all pairwise distances
    adj = np.zeros((N, N), dtype=int)
    for i in range(N):
        for j in range(i+1, N):
            d = np.linalg.norm(verts[i] - verts[j])
            if abs(d - d_nn) < tol:
                adj[i, j] = 1
                adj[j, i] = 1

    return adj


def verify_structure(verts, adj):
    """Verify the 600-cell structure against known properties."""
    N = len(verts)
    print(f"Number of vertices: {N}")
    assert N == 120, f"Expected 120 vertices, got {N}"

    degrees = adj.sum(axis=1)
    print(f"Degree of each vertex: min={degrees.min()}, max={degrees.max()}")
    assert np.all(degrees == 12), "Not all vertices have degree 12"
    print(f"  All vertices have degree 12 ✓")

    total_edges = adj.sum() // 2
    print(f"Total edges: {total_edges}")
    assert total_edges == 720, f"Expected 720 edges, got {total_edges}"
    print(f"  720 edges ✓")

    # Check that all vertices are on the unit sphere
    norms = np.linalg.norm(verts, axis=1)
    assert np.allclose(norms, 1.0), "Not all vertices on unit sphere"
    print(f"  All vertices on unit S³ ✓")


def compute_spectrum(adj):
    """Compute the full Laplacian spectrum."""
    N = len(adj)
    L = np.diag(adj.sum(axis=1)) - adj
    eigenvalues = np.linalg.eigvalsh(L.astype(float))
    return eigenvalues, L


def classify_spectrum(eigenvalues):
    """Classify eigenvalues into irreps of 2I."""
    # Known exact eigenvalues and their multiplicities
    phi = PHI
    known = [
        (0,              1,  "trivial", True),
        (9 - 3*np.sqrt(5), 4, "2",    False),
        (10 - 2*np.sqrt(5), 9, "3",   False),
        (9,             16,  "4",      True),
        (12,            25,  "5",      True),
        (14,            36,  "6",      True),
        (10 + 2*np.sqrt(5), 9, "3'",  False),
        (15,            16,  "4'",     True),
        (9 + 3*np.sqrt(5), 4, "2'",   False),
    ]

    print("\nSpectral decomposition:")
    print(f"{'Eigenvalue':<18} {'Expected mult':<15} {'Actual mult':<15} {'Irrep':<6} {'Integer?':<10} {'Match?'}")
    print("-" * 80)

    all_match = True
    integer_modes = 0
    for exact_val, expected_mult, irrep_name, is_integer in known:
        # Count eigenvalues near this value
        actual_mult = np.sum(np.abs(eigenvalues - exact_val) < 0.01)
        match = actual_mult == expected_mult
        all_match = all_match and match
        if is_integer:
            integer_modes += actual_mult
        print(f"{exact_val:<18.6f} {expected_mult:<15} {actual_mult:<15} {irrep_name:<6} {'Yes' if is_integer else 'No':<10} {'✓' if match else '✗'}")

    print(f"\nTotal modes: {len(eigenvalues)}")
    print(f"Integer-eigenvalue modes: {integer_modes}")
    print(f"All multiplicities match: {'✓' if all_match else '✗'}")

    return all_match


def find_hopf_fibers(verts, adj):
    """
    Decompose the 120 vertices into 12 Hopf fibers (C₁₀ decagons).

    Each fiber is a great circle of 10 vertices where consecutive
    vertices are connected by NN edges. The 12 fibers correspond to
    12 icosahedral NN directions.
    """
    N = len(verts)
    used = set()
    fibers = []

    for start in range(N):
        if start in used:
            continue

        # Try to trace a 10-cycle from this vertex
        fiber = [start]
        used.add(start)

        current = start
        prev = -1

        for step in range(9):
            # Find a neighbour of current that:
            # 1. Isn't already in this fiber (except start, if we're closing)
            # 2. Isn't prev (don't go backwards)
            # 3. Shares the same "fiber direction" (approximate: closest to
            #    continuing the current direction on S³)

            neighbours = np.where(adj[current] == 1)[0]

            if step == 0:
                # First step: pick any unused neighbour
                candidates = [n for n in neighbours if n not in used]
                if not candidates:
                    break
                # Pick the one that, with the start vertex, defines a great circle
                next_v = candidates[0]
            else:
                # Subsequent steps: continue along the fiber
                # The fiber is a great circle, so the next vertex should be
                # roughly "opposite" to prev relative to current on S³
                candidates = [n for n in neighbours if n not in used]
                if not candidates:
                    # Check if we can close the cycle back to start
                    if adj[current, start] == 1 and len(fiber) == 10:
                        break
                    break

                if prev >= 0:
                    # Choose the candidate that continues the rotation
                    dir_prev = verts[current] - verts[prev]
                    best = None
                    best_score = -np.inf
                    for c in candidates:
                        dir_next = verts[c] - verts[current]
                        # Want to continue rotating: maximize cross-product-like measure
                        # On S³, use the "continuation" heuristic
                        score = np.dot(dir_next, dir_prev)
                        if score > best_score:
                            best_score = score
                            best = c
                    next_v = best
                else:
                    next_v = candidates[0]

            fiber.append(next_v)
            used.add(next_v)
            prev = current
            current = next_v

        if len(fiber) == 10:
            fibers.append(fiber)

    return fibers


def main():
    print("=" * 70)
    print("BUILDING THE 600-CELL VERTEX GRAPH")
    print("=" * 70)

    # Step 1: Construct vertices
    print("\n--- Step 1: Constructing 120 vertices ---")
    verts = build_vertices()
    print(f"  Generated {len(verts)} unique vertices on S³")

    # Step 2: Build adjacency matrix
    print("\n--- Step 2: Building adjacency matrix ---")
    adj = build_adjacency(verts)

    # Step 3: Verify structure
    print("\n--- Step 3: Verifying 600-cell structure ---")
    verify_structure(verts, adj)

    # Step 4: Compute spectrum
    print("\n--- Step 4: Computing Laplacian spectrum ---")
    eigenvalues, L = compute_spectrum(adj)

    # Step 5: Classify spectrum
    print("\n--- Step 5: Classifying into 2I irreps ---")
    match = classify_spectrum(eigenvalues)

    # Step 6: Key derived quantities
    print("\n--- Step 6: Key derived quantities ---")
    phi = PHI

    # α⁻¹ from eigenvalue algebra
    lam = [9, 12, 14, 15]
    alpha_inv = (lam[0]-1)*(lam[1]-1) - 1 + sum(lam)
    print(f"\n  α⁻¹ (tree) = ({lam[0]}-1)({lam[1]}-1) - 1 + Σλ = {alpha_inv}")

    # Triple overdetermination of 87
    print(f"  87 = (9-1)(12-1)-1 = {(9-1)*(12-1)-1}")
    print(f"  87 = 3(14+15) = {3*(14+15)}")

    # sin²θ_W
    sin2_W = lam[0] / (lam[0] + lam[3])
    print(f"\n  sin²θ_W = {lam[0]}/({lam[0]}+{lam[3]}) = {sin2_W} = 3/8")

    # Permeability gap
    d1 = 1/phi
    d2 = 1.0
    print(f"\n  d₁ = 1/φ = {d1:.6f}")
    print(f"  d₂ = 1")
    print(f"  Permeability gap: d₂² - d₁² = {d2**2 - d1**2:.6f} = 1/φ = {1/phi:.6f}")

    # Distance shell structure
    print("\n--- Step 7: Distance shell verification ---")
    dists = []
    for j in range(1, len(verts)):
        d = np.linalg.norm(verts[0] - verts[j])
        dists.append(d)
    dists = sorted(set(np.round(dists, 6)))
    print(f"  Distinct distances from vertex 0: {len(dists)}")
    for d in dists:
        count = np.sum(np.abs(np.linalg.norm(verts[0:1] - verts[1:], axis=1) - d) < 0.001)
        print(f"    d = {d:.6f}  count = {count}")

    # Step 8: Hopf fiber decomposition
    print("\n--- Step 8: Hopf fiber decomposition ---")
    fibers = find_hopf_fibers(verts, adj)
    print(f"  Found {len(fibers)} fibers")
    for i, f in enumerate(fibers):
        print(f"    Fiber {i}: {len(f)} vertices: {f}")

    vertices_in_fibers = sum(len(f) for f in fibers)
    print(f"  Total vertices in fibers: {vertices_in_fibers}")

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"  Vertices: {len(verts)} ✓")
    print(f"  Edges: {adj.sum()//2} ✓")
    print(f"  Degree: 12 (uniform) ✓")
    print(f"  Spectrum: {'matches Paper XXII ✓' if match else 'MISMATCH ✗'}")
    print(f"  Integer eigenvalue modes: 93 (+ 1 trivial = 94)")
    print(f"  α⁻¹ (tree) = {alpha_inv}")
    print(f"  sin²θ_W = {sin2_W}")

    # Save for downstream computations
    np.savez(
        "scripts/600cell_data.npz",
        vertices=verts,
        adjacency=adj,
        laplacian=L,
        eigenvalues=eigenvalues,
    )
    print(f"\n  Data saved to scripts/600cell_data.npz")

    return verts, adj, L, eigenvalues


if __name__ == "__main__":
    main()
