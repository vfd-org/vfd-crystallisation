# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Lee Smart / Institute of Vibrational Field Dynamics
"""
U(1) conservation: explicit current + pointwise continuity equation on V_600.

Closes part of transport-law open item 5: Hypothesis 3.2 (discrete continuity)
and Proposition 4.2 (U(1) total-probability conservation), in the
Schrödinger-limit reduction of the Madelung pair (Paper XVIII).

DERIVATION
==========

For a self-adjoint operator H acting on C^V_600 (we take H = L, the standard
600-cell graph Laplacian, as the canonical exact-symmetry Hermitian operator
in the closure-functional commutant; see transport-law §2 Definition 2.1
which requires L_C to be a real self-adjoint operator in the polynomial
algebra of shell adjacencies — L itself satisfies this), the
Schrödinger-limit evolution is

    i ψ̇  =  H ψ.

The local probability density ρ_v = |ψ_v|² satisfies (real-symmetric
nearest-neighbour-supported H so that the sum below restricts to w ~ v;
the graph Laplacian L = D − A is the canonical example)

    ρ̇_v  =  d/dt |ψ_v|²
          =  2 Re(ψ_v* · ψ̇_v)
          =  2 Re(ψ_v* · (−i H ψ)_v)
          = +2 Im(ψ_v* · (H ψ)_v)             [since Re(−i z) = Im(z)]
          = +Σ_{w ~ v} 2 Im(ψ_v* H_{vw} ψ_w).

Define the edge current with the SIGN-CORRECT convention

    j_{v → w}  :=  −2 Im(ψ_v* H_{vw} ψ_w).

Then ρ̇_v + Σ_{w ~ v} j_{v → w} = 0  (pointwise continuity equation,
Hypothesis 3.2 with this explicit current).  Antisymmetry j_{w → v}
= −j_{v → w} follows from H_{wv} = H_{vw} (H is real symmetric).
Summing over v gives dQ/dt = 0 with Q = Σ_v ρ_v (Theorem thm:u1-explicit
of transport-law.tex, unconditional in the Schrödinger limit on H = L).

This script:
  (1) builds V_600 and the graph Laplacian L (matches transport-law §2.1);
  (2) initialises a localised complex test state ψ_0 with Q = 1;
  (3) evolves under U(t) = exp(−i L t) for n_steps small steps Δt;
  (4) at each tick, computes the explicit current j_{v→w} (with the
      sign-correct convention above), the analytic continuity residual
      ρ̇_v + Σ_{w~v} j_{v→w}, and Q;
  (5) verifies (a) the analytic continuity residual is at machine precision
      (the residual is computed from analytic ρ̇ = +2 Im(ψ* Hψ), not
      finite-difference ρ̇, so it is exactly zero up to round-off),
      (b) total Q is conserved to machine precision (~1e-14),
      (c) current antisymmetry j_{v→w} + j_{w→v} = 0 to machine precision.

EXPECTED OUTPUT (to results_u1_conservation.json)
-------------------------------------------------
  v600_size                  = 120
  n_edges                    = 720
  n_steps                    = 200
  dt                         = 0.05
  Q_initial                  = 1.0
  Q_final                    = 1.0  (drift < 1e-13)
  max_Q_drift                ≲ 1e-13
  max_continuity_residual    ≲ 1e-15  (analytic ρ̇; machine precision)
  max_antisymmetry_violation ≲ 1e-15
  pass                       = true
"""
from __future__ import annotations

import json
import math
import os
import sys
from typing import List, Tuple

import numpy as np
from scipy.linalg import expm

PHI = (1.0 + math.sqrt(5.0)) / 2.0


# ─────────────────────── 600-cell substrate (matches paper §2.1) ──────

def build_600cell_vertices() -> np.ndarray:
    verts: List[List[float]] = []
    verts.append([1.0, 0.0, 0.0, 0.0])
    verts.append([-1.0, 0.0, 0.0, 0.0])
    for i in range(1, 4):
        for s in (1, -1):
            v = [0.0, 0.0, 0.0, 0.0]
            v[i] = s
            verts.append(v)
    for s0 in (1, -1):
        for s1 in (1, -1):
            for s2 in (1, -1):
                for s3 in (1, -1):
                    verts.append([s0 * 0.5, s1 * 0.5, s2 * 0.5, s3 * 0.5])
    base = [PHI / 2.0, 0.5, 1.0 / (2.0 * PHI), 0.0]
    even_perms = [
        (0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2),
        (1, 0, 3, 2), (1, 2, 0, 3), (1, 3, 2, 0),
        (2, 0, 1, 3), (2, 1, 3, 0), (2, 3, 0, 1),
        (3, 0, 2, 1), (3, 1, 0, 2), (3, 2, 1, 0),
    ]
    for perm in even_perms:
        for s0 in (1, -1):
            for s1 in (1, -1):
                for s2 in (1, -1):
                    vals = [s0 * base[0], s1 * base[1], s2 * base[2], 0.0]
                    v = [0.0, 0.0, 0.0, 0.0]
                    for i, p in enumerate(perm):
                        v[p] = vals[i]
                    verts.append(v)
    arr = np.asarray(verts, dtype=float)
    arr = arr / np.linalg.norm(arr, axis=1, keepdims=True)
    unique: List[np.ndarray] = [arr[0]]
    for v in arr[1:]:
        if all(np.linalg.norm(v - u) > 0.01 for u in unique):
            unique.append(v)
    return np.asarray(unique[:120], dtype=float)


def build_graph(verts: np.ndarray) -> Tuple[np.ndarray, List[Tuple[int, int]]]:
    """Adjacency A and edge list (i, j) with <v_i, v_j> = φ/2."""
    n = verts.shape[0]
    target = PHI / 2.0
    tol = 1e-3
    A = np.zeros((n, n), dtype=float)
    edges: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(i + 1, n):
            if abs(float(np.dot(verts[i], verts[j])) - target) < tol:
                A[i, j] = 1.0
                A[j, i] = 1.0
                edges.append((i, j))
    return A, edges


# ─────────────────────── U(1) conservation witness ────────────────────

def compute_current(psi: np.ndarray, H: np.ndarray,
                    edges: List[Tuple[int, int]]) -> np.ndarray:
    """j_{v→w} := −2 Im(ψ_v* H_{vw} ψ_w) for each oriented edge.

    Sign-correct definition: with ρ̇_v = +2 Im(ψ_v* (Hψ)_v) (the standard
    Schrödinger-current identity for i ψ̇ = H ψ), the continuity convention
    ρ̇_v + Σ_w j_{v→w} = 0 forces j_{v→w} = −2 Im(ψ_v* H_{vw} ψ_w).
    Antisymmetry: j_{w→v} = −2 Im(ψ_w* H_{wv} ψ_v) = +2 Im(ψ_v* H_{vw} ψ_w)
    = −j_{v→w} (using H real-symmetric, H_{wv} = H_{vw}).
    """
    j = np.zeros(len(edges), dtype=float)
    for k, (v, w) in enumerate(edges):
        j[k] = -2.0 * float(np.imag(np.conj(psi[v]) * H[v, w] * psi[w]))
    return j


def edge_current_sum_at_vertex(j: np.ndarray, edges: List[Tuple[int, int]],
                               n: int) -> np.ndarray:
    """Σ_w j_{v→w} for each vertex v.

    Each undirected edge (v, w) contributes j_{v→w} to the v-sum and
    j_{w→v} = −j_{v→w} to the w-sum (antisymmetry).
    """
    div = np.zeros(n, dtype=float)
    for k, (v, w) in enumerate(edges):
        div[v] += j[k]
        div[w] -= j[k]
    return div


def main() -> int:
    print("=" * 72)
    print("  U(1) conservation + explicit continuity current on V_600")
    print("  (transport-law Hypothesis 3.2 + Proposition 4.2, Schrödinger limit)")
    print("=" * 72)

    print("\n[1/5] building V_600 substrate…")
    verts = build_600cell_vertices()
    n = verts.shape[0]
    print(f"      |V_600| = {n}")

    print("\n[2/5] building graph Laplacian L = D − A…")
    A, edges = build_graph(verts)
    deg = np.diag(A.sum(axis=1))
    L = deg - A
    H = L                                  # canonical real-symmetric Hermitian operator
    n_edges = len(edges)
    print(f"      |E_M| = {n_edges}; degree = {int(A.sum(axis=1).max())} (uniform)")

    print("\n[3/5] preparing localised initial state and evolution operator…")
    rng = np.random.default_rng(1729)
    psi = rng.standard_normal(n) + 1j * rng.standard_normal(n)
    psi = psi / np.linalg.norm(psi)
    Q0 = float(np.real(np.vdot(psi, psi)))
    print(f"      Q(0) = {Q0:.12f}")

    dt = 0.05
    n_steps = 200
    U = expm(-1j * H * dt)                 # exact one-step propagator
    print(f"      n_steps = {n_steps}, dt = {dt}")

    print("\n[4/5] evolving and recording per-tick diagnostics…")
    print("       (continuity is checked ANALYTICALLY:"
          " ρ̇_v = +2 Im(ψ_v* (Hψ)_v) and j_{v→w} = −2 Im(ψ_v* H_{vw} ψ_w),"
          " so ρ̇_v + Σ_w j_{v→w} = 0 exactly. This is the Schrödinger-limit"
          " identity that promotes Hypothesis 3.2 to a theorem with the"
          " explicit current.)")
    Q_history = [Q0]
    max_continuity_resid = 0.0
    for step in range(n_steps):
        # Analytic ρ̇ from the Schrödinger equation (no finite-difference error):
        # i ψ̇ = H ψ ⇒ ψ̇ = -i H ψ ⇒ ρ̇_v = ∂_t |ψ_v|² = +2 Im(ψ_v* (H ψ)_v).
        H_psi = H @ psi
        rho_dot = +2.0 * np.imag(np.conj(psi) * H_psi)
        # Explicit current divergence at this time:
        # j_{v→w} = −2 Im(ψ_v* H_{vw} ψ_w) (sign-correct definition above).
        j = compute_current(psi, H, edges)
        div_j = edge_current_sum_at_vertex(j, edges, n)
        # Continuity residual: ρ̇_v + Σ_w j_{v→w} = 0 (algebraic identity).
        residual = rho_dot + div_j
        max_continuity_resid = max(max_continuity_resid,
                                    float(np.max(np.abs(residual))))
        # Step
        psi = U @ psi
        Q_history.append(float(np.real(np.vdot(psi, psi))))

    Q_final = Q_history[-1]
    max_Q_drift = float(np.max(np.abs(np.array(Q_history) - Q0)))
    print(f"      Q({n_steps * dt:.1f}) = {Q_final:.12f}")
    print(f"      max |Q(t) − Q(0)| over evolution = {max_Q_drift:.3e}")
    print(f"      max pointwise continuity residual (analytic ρ̇; "
          f"machine precision) = {max_continuity_resid:.3e}")

    # Antisymmetry: with j_{v→w} = −2 Im(ψ_v* H_{vw} ψ_w),
    # j_{w→v} = −2 Im(ψ_w* H_{wv} ψ_v) = −2 Im(conj(ψ_v* H_{vw} ψ_w))
    #        = +2 Im(ψ_v* H_{vw} ψ_w) = −j_{v→w}.
    # Numerical check: compute j on (v,w) and on the swapped (w,v) using the
    # SAME definition; their sum should be zero.
    j = compute_current(psi, H, edges)
    j_reverse = np.zeros(len(edges), dtype=float)
    for k, (v, w) in enumerate(edges):
        j_reverse[k] = -2.0 * float(np.imag(np.conj(psi[w]) * H[w, v] * psi[v]))
    max_antisym_violation = float(np.max(np.abs(j + j_reverse)))
    print(f"\n[5/5] verifying current antisymmetry j_{{v→w}} + j_{{w→v}} = 0…")
    print(f"      max |j(v→w) + j(w→v)| = {max_antisym_violation:.3e}")

    # Pass criteria:
    #   Q_drift  < 1e-12  (machine precision over 10 units of unitary evolution)
    #   continuity residual < 1e-12  (algebraic identity; machine precision)
    #   antisymmetry violation < 1e-14  (algebraically exact for real H)
    Q_pass = max_Q_drift < 1e-12
    cont_pass = max_continuity_resid < 1e-12
    antisym_pass = max_antisym_violation < 1e-14
    all_pass = Q_pass and cont_pass and antisym_pass

    print(f"\n  ═══ RESULTS ═══")
    print(f"     Q conservation (drift < 1e-12):           {Q_pass}")
    print(f"     pointwise continuity (resid < 1e-12):     {cont_pass}")
    print(f"     current antisymmetry (viol < 1e-14):      {antisym_pass}")
    print(f"     overall: {3 if all_pass else 'FAIL'}/3 verified")

    results = {
        "v600_size": int(n),
        "n_edges": int(n_edges),
        "n_steps": int(n_steps),
        "dt": float(dt),
        "Q_initial": float(Q0),
        "Q_final": float(Q_final),
        "max_Q_drift": float(max_Q_drift),
        "max_continuity_residual": float(max_continuity_resid),
        "max_antisymmetry_violation": float(max_antisym_violation),
        "Q_conservation_pass": bool(Q_pass),
        "continuity_pointwise_pass": bool(cont_pass),
        "antisymmetry_pass": bool(antisym_pass),
        "all_three_pass": bool(all_pass),
    }
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "results_u1_conservation.json")
    with open(out_path, "w") as fh:
        json.dump(results, fh, indent=2)
    print(f"\n  Wrote {out_path}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
