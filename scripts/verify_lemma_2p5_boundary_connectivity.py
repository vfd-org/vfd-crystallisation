#!/usr/bin/env python3
"""
Verify Open Lemma 2.5 of docs/kappa-derivation-math.md:

  The induced subgraph G_∂ of V_600 on the 100 σ-paired boundary vertices
  (K-classes 20 and 52 under the pentagonal-clock decomposition) is connected.

Builds on scripts/600cell_data.npz (from scripts/build_600cell.py) for the
V_600 adjacency. Computes:
  - shell index s(v) ∈ {0,...,8} for each vertex via |1-v|² classes
  - kappa(v) = (s(v) - 4)² ∈ {0, 1, 4, 9, 16}
  - 12 cycles of length 10 via T_τ left-multiplication by an order-10
    quaternion τ ∈ V_600 (canonical pentagonal-clock action)
  - K(C) = Σ_{v ∈ C} kappa(v) ∈ {0, 20, 52, 72}
  - σ-paired boundary ∂ = {v : K(cycle of v) ∈ {20, 52}} (|∂| = 100)
  - induced Laplacian on ∂; number of zero eigenvalues

Output: PASS if G_∂ has exactly one zero Laplacian eigenvalue (connected),
        FAIL with diagnostic otherwise.

Usage:
    python scripts/verify_lemma_2p5_boundary_connectivity.py
"""
from __future__ import annotations

import numpy as np
from collections import Counter
from pathlib import Path

PHI = (1 + np.sqrt(5)) / 2

DATA_PATH = Path(__file__).resolve().parent / "600cell_data.npz"


def qmul(q1, q2):
    """Hamilton product of two quaternions (a,b,c,d) = a + bi + cj + dk."""
    a, b, c, d = q1
    e, f, g, h = q2
    return np.array([
        a*e - b*f - c*g - d*h,
        a*f + b*e + c*h - d*g,
        a*g - b*h + c*e + d*f,
        a*h + b*g - c*f + d*e,
    ])


def compute_shells(verts):
    """Compute the shell index s(v) ∈ {0,...,8} via |1 - v|² classes."""
    # Locate the identity vertex (1, 0, 0, 0)
    i_id = int(np.argmin(np.linalg.norm(verts - np.array([1.0, 0, 0, 0]), axis=1)))
    assert np.allclose(verts[i_id], [1.0, 0, 0, 0], atol=1e-8), \
        "identity vertex not found in V_600"
    v0 = verts[i_id]

    d2 = np.sum((verts - v0) ** 2, axis=1)
    d2_rounded = np.round(d2, 6)
    unique_d2 = sorted(set(d2_rounded.tolist()))
    assert len(unique_d2) == 9, f"expected 9 shells, got {len(unique_d2)}"

    shell_of = np.array([unique_d2.index(d) for d in d2_rounded], dtype=int)
    sizes = [int(np.sum(shell_of == s)) for s in range(9)]
    assert sizes == [1, 12, 20, 12, 30, 12, 20, 12, 1], \
        f"shell sizes {sizes} != [1,12,20,12,30,12,20,12,1]"
    return shell_of, sizes, i_id


def find_order10_tau(verts):
    """Find a quaternion τ ∈ V_600 with q^10 = identity (order 10)."""
    identity = np.array([1.0, 0, 0, 0])
    for i, q in enumerate(verts):
        power = q.copy()
        order = None
        for n in range(1, 13):
            if np.allclose(power, identity, atol=1e-8):
                order = n
                break
            power = qmul(power, q)
        if order == 10:
            return i, q
    raise RuntimeError("no order-10 quaternion found in V_600")


def compute_cycles(verts, tau):
    """Decompose V_600 into orbits under T_τ(v) = τ · v."""
    N = len(verts)
    keys = {tuple(np.round(v, 8)): i for i, v in enumerate(verts)}
    visited = np.zeros(N, dtype=bool)
    cycles = []
    for start in range(N):
        if visited[start]:
            continue
        orbit = []
        current = verts[start].copy()
        for _ in range(15):
            key = tuple(np.round(current, 8))
            assert key in keys, f"orbit step left V_600: {current}"
            i = keys[key]
            if visited[i]:
                break
            visited[i] = True
            orbit.append(i)
            current = qmul(tau, current)
        cycles.append(orbit)
    return cycles


def main():
    print("=" * 70)
    print("LEMMA 2.5: σ-paired boundary subgraph connectivity on V_600")
    print("=" * 70)

    if not DATA_PATH.exists():
        print(f"\nFAIL: {DATA_PATH} not found. Run scripts/build_600cell.py first.")
        return 1

    data = np.load(DATA_PATH)
    verts = data["vertices"]      # 120 × 4
    adj = data["adjacency"]        # 120 × 120
    N = len(verts)
    assert N == 120, f"expected 120 vertices, got {N}"
    print(f"\nLoaded V_600: {N} vertices, {int(adj.sum()) // 2} edges")

    # Step 1: shells and kappa
    print("\n--- Step 1: shell decomposition and κ(v) = (s(v) - 4)² ---")
    shell_of, sizes, i_id = compute_shells(verts)
    print(f"  identity at index {i_id}")
    print(f"  shell sizes: {sizes}  (expected [1,12,20,12,30,12,20,12,1])")
    kappa = (shell_of - 4) ** 2
    kappa_counter = Counter(kappa.tolist())
    print(f"  κ-multiset: {dict(sorted(kappa_counter.items()))}")
    # Expected: 2 vertices with kappa=16 (shells 0, 8), 24 with kappa=9 (shells 1, 7),
    # 40 with kappa=4 (shells 2, 6), 24 with kappa=1 (shells 3, 5), 30 with kappa=0 (shell 4)

    # Step 2: order-10 generator τ
    print("\n--- Step 2: locate order-10 generator τ ∈ V_600 ---")
    tau_idx, tau = find_order10_tau(verts)
    print(f"  τ at index {tau_idx}: {tau}")
    print(f"  shell(τ) = {shell_of[tau_idx]}")

    # Step 3: pentagonal-clock cycles
    print("\n--- Step 3: cycles of T_τ on V_600 ---")
    cycles = compute_cycles(verts, tau)
    lens = [len(c) for c in cycles]
    print(f"  number of cycles: {len(cycles)}")
    print(f"  cycle lengths: {sorted(lens)}  (expected [10]*12)")
    if sorted(lens) != [10] * 12:
        print(f"  FAIL: cycle decomposition not 12 × 10")
        return 1

    # Step 4: K(C) per cycle
    print("\n--- Step 4: K(C) per cycle ---")
    K_per_cycle = [int(sum(kappa[v] for v in c)) for c in cycles]
    K_counter = Counter(K_per_cycle)
    print(f"  K-multiset over cycles: {dict(sorted(K_counter.items()))}")
    print(f"  expected: {{0: 1, 72: 1, 52: 5, 20: 5}}")
    expected_K = {0: 1, 72: 1, 52: 5, 20: 5}
    if dict(K_counter) != expected_K:
        print(f"  FAIL: K-multiset mismatch")
        return 1

    # Step 5: σ-paired boundary
    print("\n--- Step 5: σ-paired boundary ∂ (K ∈ {20, 52}) ---")
    boundary = set()
    bulk = set()
    for c, K in zip(cycles, K_per_cycle):
        if K in (20, 52):
            boundary.update(c)
        else:
            bulk.update(c)
    print(f"  |∂| = {len(boundary)}  (expected 100)")
    print(f"  |B| = {len(bulk)}  (expected 20)")
    assert len(boundary) == 100, f"|∂| = {len(boundary)} != 100"
    assert len(bulk) == 20, f"|B| = {len(bulk)} != 20"

    # Step 6: induced subgraph on ∂
    print("\n--- Step 6: induced subgraph G_∂ ---")
    boundary_list = sorted(boundary)
    sub_adj = adj[np.ix_(boundary_list, boundary_list)]
    sub_n_edges = int(sub_adj.sum()) // 2
    sub_degrees = sub_adj.sum(axis=1)
    print(f"  |V(G_∂)| = {len(boundary_list)}")
    print(f"  |E(G_∂)| = {sub_n_edges}")
    print(f"  degree range: min={int(sub_degrees.min())}, max={int(sub_degrees.max())}")
    print(f"  mean degree: {sub_degrees.mean():.3f}")

    # Step 7: connectivity via Laplacian
    print("\n--- Step 7: connectivity check ---")
    sub_L = np.diag(sub_adj.sum(axis=1)) - sub_adj
    eigs = np.linalg.eigvalsh(sub_L.astype(float))
    n_zero = int(np.sum(eigs < 1e-8))
    lambda_2 = float(eigs[1])  # algebraic connectivity
    print(f"  zero eigenvalues: {n_zero}")
    print(f"  λ₁ = {eigs[0]:.10f}")
    print(f"  λ₂ (algebraic connectivity) = {lambda_2:.6f}")
    print(f"  λ_max = {eigs[-1]:.6f}")

    if n_zero == 1 and lambda_2 > 1e-8:
        verdict = "PASS: G_∂ is connected"
    else:
        verdict = f"FAIL: G_∂ has {n_zero} connected components"

    # BFS cross-check
    print("\n--- Step 8: BFS cross-check ---")
    visited_bfs = {boundary_list[0]}
    queue = [boundary_list[0]]
    sub_neighbors = {v: [boundary_list[j] for j in range(len(boundary_list))
                         if sub_adj[boundary_list.index(v), j]]
                     for v in boundary_list}
    while queue:
        v = queue.pop(0)
        for u in sub_neighbors[v]:
            if u not in visited_bfs:
                visited_bfs.add(u)
                queue.append(u)
    print(f"  BFS reaches {len(visited_bfs)} of {len(boundary_list)} vertices")
    bfs_connected = (len(visited_bfs) == len(boundary_list))

    print("\n" + "=" * 70)
    print(f"VERDICT: {verdict}")
    print(f"BFS confirmation: {'connected' if bfs_connected else 'disconnected'}")
    print("=" * 70)

    return 0 if (n_zero == 1 and bfs_connected) else 1


if __name__ == "__main__":
    raise SystemExit(main())
