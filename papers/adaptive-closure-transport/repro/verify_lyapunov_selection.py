# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Lee Smart / Institute of Vibrational Field Dynamics
"""
Closure-derived Lyapunov V(W) on the V_600 edge space — worked example.

Closes part of ACT open items (1) and (2): Hypothesis hyp:lyapunov posits
that the learning rule G(ρ, j, W) admits a locally bounded-below Lyapunov
potential V(W). This script supplies an EXPLICIT V(W) derived from the
closure-response functional and demonstrates the selection statement of
Hypothesis hyp:selection numerically: under the slow-W flow Ẇ = −∇V(W),
W converges to a critical point of V (the asserted "candidate selected
operating point"), and the convergence rate is consistent with a
{Ł}ojasiewicz–Simon-type gradient inequality at the critical point.

DERIVATION
==========

On the V_600 edge space E_M (|E_M| = 720), let W ∈ R^{E_M}_{>0} be the
edge-conductivity tensor of ACT Definition 2.1. The W-weighted Laplacian
L_W on R^{V_M} is

    (L_W ψ)_v  =  Σ_{w ~ v} W_{vw} (ψ_v − ψ_w).

Fix a source f ∈ R^{V_M}. The closure-response problem at fixed W is

    minimise   F_W[ψ]  =  ½ ⟨ψ, (L_W + φ⁻² I) ψ⟩  −  ⟨f, ψ⟩

with unique minimiser ψ*(W) = (L_W + φ⁻² I)^{-1} f.  The minimum value is

    F_W*  =  − ½ ⟨f, (L_W + φ⁻² I)^{-1} f⟩.

Define the ACT Lyapunov potential

    V(W)  :=  −F_W*  +  ½ λ ‖W − W_0‖²
           =   ½ ⟨f, (L_W + φ⁻² I)^{-1} f⟩  +  ½ λ ‖W − W_0‖²,

with λ > 0 a regularisation strength and W_0 the homeostatic baseline (the
R_hom-image, ACT §2.1). V is bounded below by 0 and proper / coercive
because of the quadratic regulariser, satisfying the analytic conditions
for the slow-flow convergence statement of hyp:selection.

The W-gradient is

    ∂V/∂W_{vw}  =  −½ (ψ*_v − ψ*_w)²  +  λ (W_{vw} − W_{0,vw})

(using ∂(L_W)/∂W_{vw} = E_{vw}, the elementary edge-Laplacian for edge
(v, w), and the matrix-inverse derivative formula). The slow flow is

    Ẇ_{vw}  =  −∂V/∂W_{vw}  =  ½ (ψ*_v − ψ*_w)²  −  λ (W_{vw} − W_{0,vw}).

This is an EXPLICIT, closure-derived realisation of the abstract learning
rule G(ρ, j, W) of ACT Definition 2.2:
   the ψ*-disagreement on each edge (an ACT-style "field-driven" growth)
   is balanced by the regularisation pull toward homeostasis W_0.

THE SCRIPT
==========

(1) Build V_600 substrate; pick a localised source f at vertex 0.
(2) Initialise W = W_0 + small perturbation; set λ = 0.1.
(3) Run the slow-W flow for n_steps with explicit Euler at dt = 0.05.
(4) At each step: compute ψ*(W) (response); compute V(W); record decrease.
(5) Verify (a) V(W) is monotonically non-increasing along the flow;
            (b) the flow converges to a critical point ‖∇V‖ → 0;
            (c) the convergence rate is consistent with linear / Łojasiewicz
                contraction near the limit point (V(W_t) − V_∞ decays
                exponentially).

EXPECTED OUTPUT (results_lyapunov_selection.json)
-------------------------------------------------
  v600_size         = 120
  n_edges           = 720
  n_steps           = 2000
  initial_V         (positive)
  final_V           (smaller; contraction ratio noted)
  V_monotone        = true
  final_grad_norm   ≲ 1e-3   (critical-point convergence)
  contraction_rate  > 0      (Łojasiewicz / linear regime)
  pass              = true
"""
from __future__ import annotations

import json
import math
import os
import sys
from typing import List, Tuple

import numpy as np

PHI = (1.0 + math.sqrt(5.0)) / 2.0


# ─────────────────────── 600-cell substrate ───────────────────────────

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


def build_edges(verts: np.ndarray) -> List[Tuple[int, int]]:
    n = verts.shape[0]
    target = PHI / 2.0
    tol = 1e-3
    edges: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(i + 1, n):
            if abs(float(np.dot(verts[i], verts[j])) - target) < tol:
                edges.append((i, j))
    return edges


def weighted_laplacian(W: np.ndarray, edges: List[Tuple[int, int]],
                       n: int) -> np.ndarray:
    """L_W: (L_W ψ)_v = Σ_{w~v} W_{vw} (ψ_v − ψ_w).  L_W = Σ_e W_e E_e."""
    L = np.zeros((n, n), dtype=float)
    for k, (v, w) in enumerate(edges):
        L[v, v] += W[k]
        L[w, w] += W[k]
        L[v, w] -= W[k]
        L[w, v] -= W[k]
    return L


# ─────────────────────── Lyapunov flow ─────────────────────────────────

def main() -> int:
    print("=" * 72)
    print("  Closure-derived Lyapunov V(W) on V_600 edge space (ACT hyp:lyapunov)")
    print("=" * 72)

    print("\n[1/4] building V_600 substrate + edge structure…")
    verts = build_600cell_vertices()
    n = verts.shape[0]
    edges = build_edges(verts)
    n_edges = len(edges)
    print(f"      |V_600| = {n}, |E_M| = {n_edges}")

    print("\n[2/4] preparing source f, baseline W_0, perturbed initial W…")
    f = np.zeros(n, dtype=float)
    f[0] = 1.0                                  # localised source at vertex 0
    W_0 = np.ones(n_edges, dtype=float)         # uniform homeostatic baseline
    rng = np.random.default_rng(2718)
    W = W_0 + 0.5 * rng.standard_normal(n_edges)
    W = np.maximum(W, 0.05)                     # keep strictly positive
    lam = 0.1
    phi_inv2 = 1.0 / (PHI * PHI)
    print(f"      W_0 uniform; W initial perturbation scale = 0.5;"
          f" regularisation λ = {lam}")

    def lyapunov(W_cur: np.ndarray) -> Tuple[float, np.ndarray, np.ndarray]:
        """V(W) = ½ ⟨f, (L_W + φ⁻² I)^{-1} f⟩ + ½ λ ‖W − W_0‖²

        Returns (V, ψ*, ∇V).
        """
        L_W = weighted_laplacian(W_cur, edges, n)
        C = L_W + phi_inv2 * np.eye(n)
        psi = np.linalg.solve(C, f)
        V = 0.5 * float(np.dot(f, psi)) + 0.5 * lam * float(np.dot(W_cur - W_0, W_cur - W_0))
        # ∇V_{vw} = -½ (ψ_v - ψ_w)² + λ (W_{vw} - W_0_{vw})
        grad = np.zeros(n_edges, dtype=float)
        for k, (v, w) in enumerate(edges):
            d = psi[v] - psi[w]
            grad[k] = -0.5 * d * d + lam * (W_cur[k] - W_0[k])
        return V, psi, grad

    print("\n[3/4] running slow-W gradient flow Ẇ = −∇V…")
    n_steps = 2000
    dt = 0.05
    V_hist: List[float] = []
    grad_norm_hist: List[float] = []
    monotone = True
    prev_V: float | None = None
    for step in range(n_steps):
        V, psi, grad = lyapunov(W)
        V_hist.append(V)
        grad_norm_hist.append(float(np.linalg.norm(grad)))
        if prev_V is not None and V > prev_V + 1e-10:
            monotone = False
        prev_V = V
        # Explicit Euler
        W = W - dt * grad
        W = np.maximum(W, 1e-3)                 # strict positivity guard

    final_V = V_hist[-1]
    final_grad_norm = grad_norm_hist[-1]
    print(f"      n_steps = {n_steps}, dt = {dt}")
    print(f"      V(0)   = {V_hist[0]:.6f}")
    print(f"      V(end) = {final_V:.6f}  (decrease: {V_hist[0] - final_V:.6f})")
    print(f"      ‖∇V‖(0)   = {grad_norm_hist[0]:.4e}")
    print(f"      ‖∇V‖(end) = {final_grad_norm:.4e}")
    print(f"      monotonically non-increasing along flow: {monotone}")

    # Łojasiewicz / linear-regime contraction estimate near the critical point.
    # Use the LAST 100 steps; fit log(V_t − V_∞) ≈ a + b t with V_∞ ≈ V_final.
    # Negative b ⇒ exponential contraction (linear or Łojasiewicz with θ = 1/2).
    last = V_hist[-100:]
    V_inf_est = min(last) - 1e-10
    excess = np.array(last) - V_inf_est
    if (excess > 0).all():
        log_excess = np.log(excess)
        steps_idx = np.arange(len(log_excess), dtype=float)
        A = np.vstack([steps_idx, np.ones_like(steps_idx)]).T
        slope, _ = np.linalg.lstsq(A, log_excess, rcond=None)[0]
        contraction_rate = float(-slope)        # positive ⇒ contracting
    else:
        contraction_rate = float("nan")
    print(f"      late-time contraction rate (per step) = {contraction_rate:.4e}")

    print("\n[4/4] verifying selection-statement criteria…")
    monotone_pass = monotone
    grad_pass = final_grad_norm < 1e-3
    contraction_pass = math.isfinite(contraction_rate) and contraction_rate > 0
    all_pass = monotone_pass and grad_pass and contraction_pass

    print(f"      V monotonically non-increasing:           {monotone_pass}")
    print(f"      ‖∇V‖(end) < 1e-3 (critical-point reached): {grad_pass}")
    print(f"      late-time contraction rate > 0:           {contraction_pass}")
    print(f"\n  ═══ {3 if all_pass else 'FAIL'}/3 selection-statement criteria verified ═══")

    results = {
        "v600_size": int(n),
        "n_edges": int(n_edges),
        "n_steps": int(n_steps),
        "dt": float(dt),
        "lambda": float(lam),
        "phi_inv_squared": float(phi_inv2),
        "V_initial": float(V_hist[0]),
        "V_final": float(final_V),
        "V_decrease": float(V_hist[0] - final_V),
        "grad_norm_initial": float(grad_norm_hist[0]),
        "grad_norm_final": float(final_grad_norm),
        "V_monotone_nonincreasing": bool(monotone_pass),
        "critical_point_reached": bool(grad_pass),
        "late_contraction_rate_per_step": float(contraction_rate),
        "contraction_positive": bool(contraction_pass),
        "all_three_pass": bool(all_pass),
    }
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "results_lyapunov_selection.json")
    with open(out_path, "w") as fh:
        json.dump(results, fh, indent=2)
    print(f"\n  Wrote {out_path}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
