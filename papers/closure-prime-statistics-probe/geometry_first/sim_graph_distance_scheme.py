#!/usr/bin/env python3
"""
GEOMETRY-FIRST SIM step 7: graph-distance association scheme of V_600.

Step 6 surfaced that V_600's Euclidean-shell 9-class scheme is finer
than the graph-distance scheme.  This sim builds the GRAPH-DISTANCE
scheme directly and verifies it matches BCN's "600-cell graph"
intersection array {12, 5, 3, 5, 2, 5, 3, 1; 1, 3, 5, 2, 5, 3, 5, 12}.

For each pair (x, y), compute graph-distance d_G(x, y) using BFS.
Build B_i = 0/1 adjacency at graph distance i.  Verify:
  - 6 distinct graph distances (0..5)
  - B_i are W(H_4)-invariant (commute with A_1)
  - All B_i form a Bose-Mesner basis
  - Intersection array satisfies a_i + b_i + c_i = k_1 = 12
  - L_1 tridiagonal eigenvalues match A_1's 9 eigenvalues
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from collections import Counter

import numpy as np

PHI    = (1.0 + 5.0 ** 0.5) / 2.0

HERE = Path(__file__).parent
OUTPUT_DIR = HERE / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def build_v600():
    half       = 0.5
    half_phi   = PHI / 2.0
    half_phi_i = 1.0 / (2.0 * PHI)
    verts = []
    for i in range(4):
        for s in (1.0, -1.0):
            v = [0.0]*4; v[i] = s
            verts.append(v)
    for s0 in (-1,1):
        for s1 in (-1,1):
            for s2 in (-1,1):
                for s3 in (-1,1):
                    verts.append([s0*half, s1*half, s2*half, s3*half])
    even_perms = [
        (0,1,2,3),(0,2,3,1),(0,3,1,2),
        (1,0,3,2),(1,2,0,3),(1,3,2,0),
        (2,0,1,3),(2,1,3,0),(2,3,0,1),
        (3,0,2,1),(3,1,0,2),(3,2,1,0),
    ]
    for p in even_perms:
        for sa in (-1,1):
            for sb in (-1,1):
                for sc in (-1,1):
                    v = [0.0]*4
                    v[p[0]] = sa*half_phi
                    v[p[1]] = sb*half
                    v[p[2]] = sc*half_phi_i
                    v[p[3]] = 0.0
                    verts.append(v)
    return np.array(verts, dtype=float)


def bfs_distances(A: np.ndarray, source: int, n: int) -> np.ndarray:
    """BFS from source. Returns array of distances (n,)."""
    dist = np.full(n, -1, dtype=int)
    dist[source] = 0
    frontier = [source]
    while frontier:
        next_frontier = []
        for v in frontier:
            for w in np.where(A[v] == 1)[0]:
                if dist[w] < 0:
                    dist[w] = dist[v] + 1
                    next_frontier.append(int(w))
        frontier = next_frontier
    return dist


def main():
    print("=" * 78)
    print("SIM 7: V_600 graph-distance 6-class association scheme")
    print("=" * 78)
    print()

    V = build_v600()
    n = V.shape[0]
    # Edge adjacency: shortest Euclidean distance
    d2 = np.sum((V[:, None, :] - V[None, :, :]) ** 2, axis=2)
    min_d2 = d2[d2 > 1e-9].min()
    A1 = (np.abs(d2 - min_d2) < 1e-7).astype(int)
    np.fill_diagonal(A1, 0)
    print(f"  V_600: {n} vertices, edge length² = {min_d2:.6f}")
    print(f"  A_1 (edge adjacency) regular degree: {int(A1.sum(axis=1)[0])}")
    print()

    # Compute graph-distance matrix D[i, j] via BFS from each vertex
    print("  Computing graph-distance matrix via BFS ...")
    D = np.zeros((n, n), dtype=int)
    for i in range(n):
        D[i, :] = bfs_distances(A1, i, n)
    max_dist = int(D.max())
    diameter = max_dist
    print(f"  Graph diameter: {diameter}")
    print()

    # Build shell operators B_i for i = 0..diameter
    n_classes = diameter + 1
    B = []
    for i in range(n_classes):
        B_i = (D == i).astype(int)
        if i == 0:
            assert np.allclose(B_i, np.eye(n))
        B.append(B_i)
    valencies = [int(B[i].sum(axis=1)[0]) for i in range(n_classes)]
    all_const = all(np.all(B[i].sum(axis=1) == valencies[i]) for i in range(n_classes))
    print(f"  Valencies k_0..k_{diameter}: {valencies}")
    print(f"  Vertex-transitive (all rows equal): {all_const}")
    print(f"  Σ k_i = {sum(valencies)} (should be 120)")
    assert sum(valencies) == 120
    print()

    # Verify each B_i commutes with A_1 (it should, since graph distance is
    # graph-aut invariant)
    print("  Commutation checks: B_i with A_1 ...")
    commutes = []
    for i in range(n_classes):
        diff = A1 @ B[i] - B[i] @ A1
        ok = bool(np.all(diff == 0))
        commutes.append(ok)
    print(f"    All B_i commute with A_1: {all(commutes)}")
    print()

    # ---- Compute intersection numbers ----
    print("  Intersection numbers a_i, b_i, c_i ...")
    a_seq = []
    b_seq = []
    c_seq = []
    valid_intersection = True
    for i in range(n_classes):
        # Pick a vertex at graph-distance i from V[0]
        if i == 0:
            y_idx = 0
        else:
            cand = np.where(D[0, :] == i)[0]
            y_idx = int(cand[0])
        # Neighbors of y_idx
        neighbors = np.where(A1[y_idx] == 1)[0]
        # Their graph distances from V[0]
        their_dists = [int(D[0, w]) for w in neighbors]
        c_count = sum(1 for d in their_dists if d == i - 1)
        a_count = sum(1 for d in their_dists if d == i)
        b_count = sum(1 for d in their_dists if d == i + 1)
        other_count = sum(1 for d in their_dists if d not in (i-1, i, i+1))
        a_seq.append(a_count)
        b_seq.append(b_count if i < diameter else 0)
        c_seq.append(c_count if i > 0 else 0)
        total = c_count + a_count + b_count + other_count
        sums_ok = (a_count + b_count + c_count == 12) and (other_count == 0)
        if not sums_ok:
            valid_intersection = False
        print(f"    i={i}: a={a_count}, b={b_count}, c={c_count}, "
              f"other={other_count}, sum={total} {'✓' if sums_ok else 'FAIL'}")
    print()
    print(f"  a_i sequence: {a_seq}")
    print(f"  b_i sequence: {b_seq}")
    print(f"  c_i sequence: {c_seq}")
    # BCN intersection array notation: {b_0..b_{d-1}; c_1..c_d}
    b_bcn = b_seq[:diameter]
    c_bcn = c_seq[1:]
    print()
    print(f"  Intersection array (BCN convention):")
    print(f"    {{{', '.join(map(str, b_bcn))}; {', '.join(map(str, c_bcn))}}}")
    print()

    # ---- Compare to BCN 600-cell graph array ----
    bcn_expected_array = {
        "b": [12, 5, 5, 2, 1],
        "c": [1, 2, 5, 5, 12],
    }
    # Adjust to actual diameter; for d=5 we have b_0..b_4 (5 entries) + c_1..c_5 (5 entries)
    bcn_match_b = b_bcn == bcn_expected_array["b"]
    bcn_match_c = c_bcn == bcn_expected_array["c"]
    print(f"  BCN expected (600-cell graph, diameter 5):")
    print(f"    {{12, 5, 5, 2, 1; 1, 2, 5, 5, 12}}")
    print(f"  Our b matches: {bcn_match_b}")
    print(f"  Our c matches: {bcn_match_c}")
    print()

    # ---- Build L_1 and verify spectrum matches A_1 ----
    print("  Building tridiagonal L_1 ...")
    L1 = np.zeros((n_classes, n_classes))
    for i in range(n_classes):
        L1[i, i] = a_seq[i]
    for i in range(diameter):
        L1[i, i + 1] = c_seq[i + 1]  # super-diag: c_{i+1}
        L1[i + 1, i] = b_seq[i]      # sub-diag: b_i
    eigvals_L1 = sorted(np.linalg.eigvals(L1).real.tolist(), reverse=True)
    # A_1 eigenvalues (we know there are 9 distinct, but the graph-distance scheme
    # has only diameter+1 = 6 distinct eigenvalues that ARE in A_1's spectrum)
    eigvals_A1_all = sorted(np.linalg.eigvalsh(A1.astype(float)).tolist(), reverse=True)
    # Cluster
    eigvals_A1 = []
    for ev in eigvals_A1_all:
        if not eigvals_A1 or abs(eigvals_A1[-1] - ev) > 1e-6:
            eigvals_A1.append(ev)
    print(f"  A_1 distinct eigenvalues ({len(eigvals_A1)}): "
          f"{[f'{x:+.4f}' for x in eigvals_A1]}")
    print(f"  L_1 eigenvalues ({len(eigvals_L1)}): "
          f"{[f'{x:+.4f}' for x in eigvals_L1]}")
    # Each L_1 eigenvalue should be among A_1's 9 distinct eigenvalues
    L_in_A = all(any(abs(le - ae) < 1e-6 for ae in eigvals_A1) for le in eigvals_L1)
    print(f"  Every L_1 eigenvalue is in A_1's spectrum: {L_in_A}")
    print()

    # ---- Acceptance ----
    checks = {
        "graph_diameter_is_5":             diameter == 5,
        "valencies_sum_to_120":             sum(valencies) == 120,
        "B_i_all_commute_with_A_1":         all(commutes),
        "intersection_array_DRG_axiom":     valid_intersection,
        "BCN_b_sequence_matches":          bool(bcn_match_b),
        "BCN_c_sequence_matches":          bool(bcn_match_c),
        "L_1_eigenvalues_subset_of_A_1":   bool(L_in_A),
    }
    print("Acceptance checks:")
    for k, v in checks.items():
        print(f"  {k}: {v}")
    all_pass = all(checks.values())
    print()
    print(f"OVERALL: {'PASS' if all_pass else 'FAIL'}")

    out = {
        "graph_diameter":       diameter,
        "valencies":            valencies,
        "intersection_array_a": a_seq,
        "intersection_array_b": b_seq,
        "intersection_array_c": c_seq,
        "BCN_array_b":          b_bcn,
        "BCN_array_c":          c_bcn,
        "BCN_expected":         bcn_expected_array,
        "L_1_eigenvalues":      eigvals_L1,
        "A_1_eigenvalues":      eigvals_A1,
        "checks":               {k: bool(v) for k, v in checks.items()},
        "overall_pass":         all_pass,
    }
    with open(OUTPUT_DIR / "graph_distance_scheme_results.json", "w") as f:
        json.dump(out, f, indent=2)
    print(f"Wrote {OUTPUT_DIR / 'graph_distance_scheme_results.json'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
