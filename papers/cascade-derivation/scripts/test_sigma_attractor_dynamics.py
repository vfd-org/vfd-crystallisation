#!/usr/bin/env python3
"""
Dynamical-flow sim of the σ-attractor hypothesis H_attr.

KEY STRUCTURAL FACT (caught by failed first attempt):
  σ does NOT act as a permutation on 2I.  Only the 24-point 2T ⊂ 2I
  is σ-stable; for v ∈ 2I\2T, σ(v) lies in the σ-conjugate 600-cell
  outside 2I.  The σ-action on the cascade lives intrinsically in the
  SPECTRAL BASIS of L: σ-fixed L-eigenvalues are in Q ⊂ Q(φ);
  σ-paired L-eigenvalues come in Galois-conjugate pairs (a+bφ, a+b−bφ).

For our spectrum {0, 12-6φ, 12-4φ, 9, 12, 14, 8+4φ, 15, 6+6φ}:
  σ-fixed:  {0, 9, 12, 14, 15}    (rational, 1+16+25+36+16 = 94)
  σ-paired: (12-6φ ↔ 6+6φ),       (mult 4, 4 — total 8)
            (12-4φ ↔ 8+4φ)        (mult 9, 9 — total 18)
  σ-paired total: 26.

The σ-attractor hypothesis H_attr in spectral form:
  Under cascade-equivariant closure dynamics, the stationary attractor
  has mass 0 on all σ-paired spectral subspaces.

This script tests H_attr in three regimes (now spectrally-defined):

  R1: pure σ-equivariant linear flow (no closure projector)
  R2: σ-equivariant flow + EXPLICIT closure projector P_σ
  R3: control — σ-broken flow + closure projector

P_σ is the projector onto the σ-fixed spectral subspace of L
(94-dim out of 120).  Closure dynamics ⇔ project onto P_σ.
"""

from __future__ import annotations

import sys
from pathlib import Path
import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
sys.path.insert(0, str(REPO_ROOT / "papers" / "paper-xxii" / "scripts"))

from run_icosian_exact import build_vertices, qq_distance_sq  # noqa: E402


PHI = (1 + np.sqrt(5)) / 2


def build_adjacency(verts):
    n = len(verts)
    min_d = None
    for j in range(1, n):
        d = qq_distance_sq(verts[0], verts[j])
        if min_d is None:
            min_d = d
        else:
            cur_real = float(min_d[0]) + float(min_d[1]) * (5 ** 0.5)
            new_real = float(d[0]) + float(d[1]) * (5 ** 0.5)
            if new_real < cur_real - 1e-12:
                min_d = d
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j and qq_distance_sq(verts[i], verts[j]) == min_d:
                A[i, j] = 1.0
    return A


def is_sigma_fixed_eigenvalue(lam, tol=1e-6):
    """Eigenvalue is σ-fixed iff it equals one of {0, 9, 12, 14, 15}
    (rational integers in the 600-cell Laplacian spectrum)."""
    return any(abs(lam - r) < tol for r in [0.0, 9.0, 12.0, 14.0, 15.0])


def build_spectral_projectors(eigs, vecs, tol=1e-6):
    """Build orthogonal projectors onto σ-fixed and σ-paired spectral
    subspaces of L using the rationality classification of eigenvalues."""
    n = len(eigs)
    P_fix = np.zeros((n, n))
    P_pair = np.zeros((n, n))
    for i, lam in enumerate(eigs):
        v = vecs[:, i]
        outer = np.outer(v, v)
        if is_sigma_fixed_eigenvalue(lam, tol):
            P_fix += outer
        else:
            P_pair += outer
    return P_fix, P_pair


def measure_attractor(W, P_fix, P_pair, P_nonzero,
                      n_steps=5000, n_warmup=500,
                      sigma_noise=0.1, explicit_closure=False, seed=42):
    """Iterate ψ_{t+1} = W ψ_t + ξ_t and measure stationary covariance.

    The zero Laplacian mode is projected out at each step (P_nonzero):
    for W = I - dt L, the zero mode has W-eigenvalue 1 and would
    accumulate noise without bound, dominating the empirical covariance
    artificially.  Stationary analysis requires its removal.
    """
    rng = np.random.default_rng(seed)
    n = W.shape[0]
    psi = rng.standard_normal(n) * 0.1
    psi = P_nonzero @ psi                       # project out zero mode
    samples = []
    for t in range(n_steps):
        xi = rng.standard_normal(n) * sigma_noise
        xi = P_nonzero @ xi                     # noise also lives in non-zero subspace
        psi = W @ psi + xi
        psi = P_nonzero @ psi                   # keep ψ orthogonal to zero mode
        if explicit_closure:
            psi = P_fix @ psi                   # closure: project to σ-fixed
            psi = P_nonzero @ psi               # re-orthogonalise
        if t >= n_warmup:
            samples.append(psi.copy())
    samples = np.asarray(samples)
    C = samples.T @ samples / len(samples)
    # Mass ratios on the nonzero subspace
    fix_mass = np.trace(C @ P_fix @ P_nonzero) / max(np.trace(C), 1e-30)
    pair_mass = np.trace(C @ P_pair @ P_nonzero) / max(np.trace(C), 1e-30)
    return {
        'fix_mass': float(fix_mass),
        'pair_mass': float(pair_mass),
        'trace_C': float(np.trace(C)),
    }


def main():
    print("=" * 76)
    print("DYNAMICAL σ-ATTRACTOR TEST (spectral basis, cascade closure on 2I)")
    print("Structural fact: σ acts on the cascade via the SPECTRAL basis of L")
    print("(σ-fixed eigenvalues are rational, σ-paired are in Q(φ)\\Q).")
    print("=" * 76)

    # --- Build 2I and L ---
    print("\n[Setup] Build 2I and Laplacian L = D - A...")
    verts = build_vertices()
    A = build_adjacency(verts)
    D = np.diag(A.sum(axis=1))
    L = D - A
    eigs, vecs = np.linalg.eigh(L)

    # --- Build σ-fixed and σ-paired projectors ---
    P_fix, P_pair = build_spectral_projectors(eigs, vecs)
    fix_dim = round(np.trace(P_fix))
    pair_dim = round(np.trace(P_pair))
    print(f"        σ-fixed subspace dim:  {fix_dim} (expected 94)")
    print(f"        σ-paired subspace dim: {pair_dim} (expected 26)")

    # --- Build projector onto non-zero modes of L ---
    # The zero mode (eigenvalue 0, multiplicity 1) is the constant
    # vector; under W = I - dt L it has eigenvalue 1 and accumulates
    # noise without bound, so we project it out for stationary analysis.
    P_nonzero = np.eye(120)
    for i, lam in enumerate(eigs):
        if abs(lam) < 1e-9:
            v = vecs[:, i]
            P_nonzero -= np.outer(v, v)
    nz_dim = round(np.trace(P_nonzero))
    print(f"        non-zero L-mode subspace dim: {nz_dim} (expected 119)")

    # --- Discrete heat-equation flow: W = I - dt L (contractive) ---
    dt = 0.5 / max(eigs[-1], 1.0)
    W = np.eye(120) - dt * L
    print(f"        dt = {dt:.4f},  W = I - dt·L")
    sigma_noise = 0.1
    n_steps, n_warmup = 5000, 500

    # --- ANALYTICAL baseline: stationary mass per eigenvalue ---
    # Under ψ_{t+1} = (1 - dt λ_i) ψ_t,i + ξ_i with isotropic noise σ²,
    # stationary variance at mode i is σ² / (2 dt λ_i - (dt λ_i)²).
    # Aggregate by σ-fixed/paired classification.
    print("\n[Analytical] Stationary mass per spectral subspace under "
          "isotropic noise:")
    fix_analytic = 0.0
    pair_analytic = 0.0
    for lam in eigs:
        if abs(lam) < 1e-9:                # zero mode: special case (uniform)
            continue
        wlam = 1.0 - dt * lam
        if abs(wlam) >= 1.0:
            continue                        # divergent mode (shouldn't happen)
        var_lam = sigma_noise ** 2 / (1.0 - wlam ** 2)
        if is_sigma_fixed_eigenvalue(lam):
            fix_analytic += var_lam
        else:
            pair_analytic += var_lam
    total_analytic = fix_analytic + pair_analytic
    print(f"        σ-fixed mass fraction (analytic):  "
          f"{fix_analytic/total_analytic:.4f}")
    print(f"        σ-paired mass fraction (analytic): "
          f"{pair_analytic/total_analytic:.4f}")
    print(f"        baseline (uniform): fix = {fix_dim/120:.4f}, "
          f"pair = {pair_dim/120:.4f}")
    print(f"        — diffusive dynamics shifts mass toward LOW-freq modes")

    # --- R1: σ-equivariant flow, NO closure projector ---
    print()
    print("=" * 76)
    print("R1: σ-equivariant diffusive flow + isotropic noise + NO closure")
    print("=" * 76)
    r1 = measure_attractor(W, P_fix, P_pair, P_nonzero,
                           n_steps=n_steps, n_warmup=n_warmup,
                           sigma_noise=sigma_noise,
                           explicit_closure=False, seed=42)
    print(f"  σ-fixed mass     = {r1['fix_mass']:.4f}  "
          f"(analytic prediction: {fix_analytic/total_analytic:.4f})")
    print(f"  σ-paired mass    = {r1['pair_mass']:.4f}")
    print(f"  H_attr support   = "
          f"{'YES' if r1['fix_mass'] > 0.95 else 'NO (substantial pair mass)'}")

    # --- R2: σ-equivariant flow + EXPLICIT closure projector ---
    print()
    print("=" * 76)
    print("R2: σ-equivariant flow + isotropic noise + EXPLICIT closure (P_σ)")
    print("=" * 76)
    r2 = measure_attractor(W, P_fix, P_pair, P_nonzero,
                           n_steps=n_steps, n_warmup=n_warmup,
                           sigma_noise=sigma_noise,
                           explicit_closure=True, seed=42)
    print(f"  σ-fixed mass     = {r2['fix_mass']:.4f}")
    print(f"  σ-paired mass    = {r2['pair_mass']:.4f}")
    print(f"  H_attr support   = "
          f"{'YES (full)' if r2['fix_mass'] > 0.99 else 'partial'}")

    # --- R3: σ-BROKEN flow + closure projector (control) ---
    print()
    print("=" * 76)
    print("R3 (CONTROL): σ-BROKEN flow + closure projector")
    print("=" * 76)
    rng = np.random.default_rng(123)
    perturbation = rng.standard_normal((120, 120)) * 0.05
    perturbation = (perturbation + perturbation.T) / 2
    W_broken = W + perturbation * dt        # break σ-equivariance of W
    r3 = measure_attractor(W_broken, P_fix, P_pair, P_nonzero,
                           n_steps=n_steps, n_warmup=n_warmup,
                           sigma_noise=sigma_noise,
                           explicit_closure=True, seed=42)
    print(f"  σ-fixed mass     = {r3['fix_mass']:.4f}")
    print(f"  σ-paired mass    = {r3['pair_mass']:.4f}")
    print(f"  H_attr support   = "
          f"{'YES' if r3['fix_mass'] > 0.95 else 'NO/partial'}")
    print(f"  Note: closure projector forces P_fix support EVEN FOR BROKEN W,")
    print(f"  so we expect ~1.0 here too (closure dominates).  The interesting")
    print(f"  contrast is R1 vs R2: closure mechanism is what enforces H_attr.")

    # --- Verdict ---
    print()
    print("=" * 76)
    print("VERDICT — H_attr architectural status:")
    print()
    print(f"  R1 (σ-equiv flow alone):         fix_mass = {r1['fix_mass']:.4f}")
    print(f"  R2 (σ-equiv + closure):           fix_mass = {r2['fix_mass']:.4f}")
    print(f"  R3 (σ-broken + closure):          fix_mass = {r3['fix_mass']:.4f}")
    print()
    if r1['fix_mass'] > 0.95:
        print("  H_attr is ARCHITECTURALLY automatic for σ-equivariant flow.")
        print("  σ-equivariance alone forces stationary attractor onto σ-fixed")
        print("  spectral support, even without explicit closure.")
    elif r2['fix_mass'] > 0.99 and r1['fix_mass'] < 0.95:
        print("  H_attr REQUIRES the closure mechanism (the Δθ → 0 / σ-symmetric")
        print("  projection of the cascade closure functional). σ-equivariance")
        print("  alone is INSUFFICIENT — diffusive dynamics shifts mass toward")
        print("  low-frequency σ-paired modes. The closure operator is the ")
        print("  essential ingredient that enforces H_attr.")
        print()
        print("  Architecturally: F1 forces σ-equivariance; the cascade closure")
        print("  functional F provides the closure projector; their COMPOSITION")
        print("  is what gives H_attr. This is consistent with the H4O law")
        print("  (cascade-h4-oscillator-law.md): closure = phase-coherence")
        print("  selection (Δθ → 0), which in spectral form is projection onto")
        print("  the σ-fixed (σ-symmetric) subspace.")
    print("=" * 76)


if __name__ == "__main__":
    main()
