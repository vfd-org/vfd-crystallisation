#!/usr/bin/env python3
"""
Empirical landing for Theorem 4.1 of docs/kappa-derivation-math.md:

The discrete boundary Green function on V_600's σ-paired subgraph G_∂
should fall as 1/d in graph distance at intermediate d, matching the
continuum 1/r law that produces Newton's potential.

Method:
  1. Build V_600, identify σ-paired boundary ∂ (100 vertices), restrict
     to induced adjacency.
  2. Compute the Moore–Penrose pseudo-inverse of L_∂ (well-defined on
     the orthogonal complement of the constant zero mode by Lemma 2.5).
  3. Pick a fixed source vertex v_0 ∈ ∂. Compute ψ(v) = (L_∂)^+ δ_{v_0}.
  4. Compute graph distance d(v_0, v) for all v ∈ ∂ via BFS.
  5. Plot / fit ψ(v) vs 1/d.

If ψ ~ A/d for intermediate d (1 < d < diameter/2), Theorem 4.1's
continuum approximation has a clean discrete witness.

Bonus: compute (L_∂)^+ for the bulk-mode contribution and compare
spectral decomposition of L_∂ against expected continuum eigenvalues
on S³.

Usage:
    python scripts/verify_boundary_green_function.py
"""
from __future__ import annotations

import numpy as np
from collections import Counter, deque
from pathlib import Path

PHI = (1 + np.sqrt(5)) / 2

DATA_PATH = Path(__file__).resolve().parent / "600cell_data.npz"


def qmul(q1, q2):
    a, b, c, d = q1
    e, f, g, h = q2
    return np.array([
        a*e - b*f - c*g - d*h,
        a*f + b*e + c*h - d*g,
        a*g - b*h + c*e + d*f,
        a*h + b*g - c*f + d*e,
    ])


def compute_shells(verts):
    i_id = int(np.argmin(np.linalg.norm(verts - np.array([1.0, 0, 0, 0]), axis=1)))
    v0 = verts[i_id]
    d2 = np.round(np.sum((verts - v0) ** 2, axis=1), 6)
    unique_d2 = sorted(set(d2.tolist()))
    return np.array([unique_d2.index(d) for d in d2], dtype=int)


def find_order10_tau(verts):
    identity = np.array([1.0, 0, 0, 0])
    for i, q in enumerate(verts):
        power = q.copy()
        for n in range(1, 13):
            if np.allclose(power, identity, atol=1e-8):
                if n == 10:
                    return i, q
                break
            power = qmul(power, q)
    raise RuntimeError("no order-10 quaternion found")


def compute_cycles(verts, tau):
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
            i = keys[key]
            if visited[i]:
                break
            visited[i] = True
            orbit.append(i)
            current = qmul(tau, current)
        cycles.append(orbit)
    return cycles


def bfs_distances(adj, source):
    """Graph distance from source to all vertices via BFS."""
    N = adj.shape[0]
    dist = np.full(N, -1, dtype=int)
    dist[source] = 0
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for v in range(N):
            if adj[u, v] and dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist


def main():
    print("=" * 70)
    print("THEOREM 4.1: discrete 1/d Green function on G_∂")
    print("=" * 70)

    data = np.load(DATA_PATH)
    verts = data["vertices"]
    adj = data["adjacency"]

    # Build σ-paired boundary
    shell_of = compute_shells(verts)
    kappa = (shell_of - 4) ** 2
    _, tau = find_order10_tau(verts)
    cycles = compute_cycles(verts, tau)
    boundary = sorted({v for c in cycles
                       for v in c
                       if sum(kappa[u] for u in c) in (20, 52)})
    assert len(boundary) == 100

    # Induced subgraph
    sub_adj = adj[np.ix_(boundary, boundary)].astype(float)
    n = len(boundary)

    # Boundary Laplacian and pseudo-inverse
    sub_L = np.diag(sub_adj.sum(axis=1)) - sub_adj
    print(f"\nBoundary Laplacian: {n}×{n}, rank {np.linalg.matrix_rank(sub_L, tol=1e-8)}")

    eigvals, eigvecs = np.linalg.eigh(sub_L)
    print(f"Smallest eigenvalues: {eigvals[:5]}")
    print(f"Largest eigenvalues:  {eigvals[-3:]}")

    # Moore–Penrose: invert nonzero eigenvalues, zero on the zero-mode
    inv_eig = np.where(eigvals > 1e-8, 1.0 / np.where(eigvals > 1e-8, eigvals, 1.0), 0.0)
    L_pinv = eigvecs @ np.diag(inv_eig) @ eigvecs.T

    # Sanity: L_∂ L_∂^+ should be projection onto orthogonal complement of constants
    P = sub_L @ L_pinv
    P_expected = np.eye(n) - np.ones((n, n)) / n
    err = np.linalg.norm(P - P_expected)
    print(f"||L L^+ − (I − J/n)|| = {err:.2e}")

    # Pick source v_0 = boundary[0]; compute ψ = L^+ (δ_{v_0} − 1/n · 1)
    # We subtract the constant component so the source is in the range of L
    source_idx = 0
    source_vec = np.zeros(n)
    source_vec[source_idx] = 1.0
    source_vec -= source_vec.mean()  # project onto range
    psi = L_pinv @ source_vec

    # Graph distances from source within G_∂
    dist = bfs_distances(sub_adj > 0, source_idx)
    diameter = int(dist.max())
    print(f"\nDiameter of G_∂: {diameter}")
    print(f"Distance histogram: {dict(sorted(Counter(dist.tolist()).items()))}")

    # ψ(v) by distance shell
    print(f"\n--- ψ(v) by graph-distance shell from source ---")
    print(f"{'d':>4} {'count':>6} {'mean ψ':>14} {'std ψ':>14}")
    shells_psi = {}
    for d in range(diameter + 1):
        mask = (dist == d)
        if mask.sum() == 0:
            continue
        vals = psi[mask]
        shells_psi[d] = (mask.sum(), vals.mean(), vals.std())
        print(f"{d:>4} {mask.sum():>6} {vals.mean():>14.6f} {vals.std():>14.6f}")

    # Fit ψ = A/d + B for d = 1, ..., diameter-1
    print(f"\n--- 1/d fit for ψ at d = 1..{diameter-1} ---")
    ds = np.array([d for d in shells_psi if d >= 1])
    psi_means = np.array([shells_psi[d][1] for d in ds])

    X = np.column_stack([1.0 / ds, np.ones_like(ds, dtype=float)])
    coef, residuals, rank, sv = np.linalg.lstsq(X, psi_means, rcond=None)
    A, B = coef
    pred = X @ coef
    ss_res = np.sum((psi_means - pred) ** 2)
    ss_tot = np.sum((psi_means - psi_means.mean()) ** 2)
    R2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
    print(f"  ψ(d) ≈ {A:.6f} / d + {B:.6f}")
    print(f"  R² = {R2:.6f}")
    print(f"  residuals per shell:")
    for d, pm, pr in zip(ds, psi_means, pred):
        print(f"    d={d}: ψ_mean={pm:+.5f}  fit={pr:+.5f}  Δ={pm-pr:+.5f}")

    # Compare to alternative fits
    print(f"\n--- Alternative-decay comparisons ---")
    for power, label in [(2.0, "1/d²"), (0.5, "1/√d"), (1.0, "1/d")]:
        X_alt = np.column_stack([1.0 / ds**power, np.ones_like(ds, dtype=float)])
        coef_alt, *_ = np.linalg.lstsq(X_alt, psi_means, rcond=None)
        pred_alt = X_alt @ coef_alt
        ss_alt = np.sum((psi_means - pred_alt) ** 2)
        R2_alt = 1.0 - ss_alt / ss_tot
        print(f"  ψ(d) ≈ {coef_alt[0]:+.5f} × {label} + {coef_alt[1]:+.5f}   R²={R2_alt:.6f}")

    # Continuum-spectrum sanity check: compare L_∂ eigenvalues to scalar
    # Laplacian on S³ spectrum L(L+2) for L=0,1,2,...
    print(f"\n--- L_∂ spectrum vs scalar Laplacian on S³ (continuum) ---")
    print("S³ scalar-Laplacian eigenvalues are L(L+2) with multiplicity (L+1)²")
    s3_modes = []
    for L in range(7):
        eig_cont = L * (L + 2)
        mult = (L + 1) ** 2
        s3_modes.append((eig_cont, mult))
        print(f"  L={L}: eigenvalue {eig_cont}, multiplicity {mult}")

    print(f"\nGrouped L_∂ eigenvalues (rounded to 0.01):")
    grouped = Counter(np.round(eigvals, 2).tolist())
    print(f"  {dict(sorted(grouped.items()))}")

    print("\n" + "=" * 70)
    if R2 > 0.95:
        print(f"VERDICT: 1/d fit holds with R² = {R2:.4f} — discrete Newton confirmed")
    else:
        print(f"VERDICT: 1/d fit weaker than expected (R² = {R2:.4f}); see breakdown above")
    print("=" * 70)


if __name__ == "__main__":
    main()
