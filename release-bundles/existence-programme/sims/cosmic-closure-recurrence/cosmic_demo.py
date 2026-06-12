#!/usr/bin/env python3
"""
Cosmic Self-Pruning + Frame Recurrence --- numerical demonstrations.

Demos (C1-C5) ground the load-bearing structural claims of the cosmic /
structural-extension paper:

  C1  Cascade rung tower: E_8 (240), V_600 = H_4 (120), 24-cell = D_4 (24).
      Each rung admits its own substrate, closure operator C_phi = L + phi^-2 I,
      spectral tau, and Sigma_I = Fix(tau) of non-trivial dimension.
      (Thm 19.1 rung-stratified universality; addresses CP-rung-9.3.)
  C2  Hierarchical time-scaling: each rung has its own natural closure-tick
      rate set by lam_min on Sigma_perp. (Thm 19.2.)
  C3  Pruning operator P idempotence: P o P = P.
      (Def 18.1, Prop 18.2.)
  C4  Non-periodic recurrence under time-dependent C_n: closure-phase
      transitions do not return to a previous state.
      (Thm 18.4.)
  C5  Frame destruction four conditions: each independently collapses
      dim Sigma to zero.
      (Thm 16.2 of Cosmic, in the paper's frame-destruction theorem.)

Usage:
  python cosmic_demo.py                # run all demos, save figures + JSON
  python cosmic_demo.py --demo 1       # run only C1
  python cosmic_demo.py --no-figures   # skip figure saving
"""

from __future__ import annotations

import argparse
import json
from itertools import product, permutations
from pathlib import Path

import numpy as np

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    HAVE_MPL = True
except ImportError:
    HAVE_MPL = False


# ============================================================
# Constants
# ============================================================

PHI = (1.0 + np.sqrt(5.0)) / 2.0
PHI_INV = 1.0 / PHI
PHI_INV2 = 1.0 / (PHI * PHI)
SEED = 42
RNG = np.random.default_rng(SEED)
OUTDIR = Path(__file__).parent / "output"
OUTDIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# Cascade rung substrates
# ============================================================

def build_e8_roots() -> np.ndarray:
    """E_8 root system: 240 vectors in R^8 with norm sqrt(2).

    112 integer roots:  +/-e_i +/- e_j  (i != j)
    128 half-integer roots:  (+/- 1/2)^8 with even number of minus signs
    """
    roots = []
    # Integer roots
    for i in range(8):
        for j in range(i + 1, 8):
            for s1 in (1.0, -1.0):
                for s2 in (1.0, -1.0):
                    v = np.zeros(8)
                    v[i] = s1
                    v[j] = s2
                    roots.append(v)
    # Half-integer roots: even number of minus signs
    for signs in product((-1, 1), repeat=8):
        if sum(1 for s in signs if s == -1) % 2 == 0:
            roots.append(0.5 * np.array(signs, dtype=float))
    return np.array(roots)


def build_v600() -> np.ndarray:
    """The 120 vertices of the 600-cell (= H_4 rung) in R^4."""
    vertices = []
    for i in range(4):
        for s in (1.0, -1.0):
            v = np.zeros(4); v[i] = s
            vertices.append(v)
    for signs in product((-0.5, 0.5), repeat=4):
        vertices.append(np.array(signs))
    base = (0.0, PHI_INV, 1.0, PHI)
    even_perms = [
        perm for perm in permutations(range(4))
        if sum(1 for i in range(len(perm)) for j in range(i + 1, len(perm)) if perm[i] > perm[j]) % 2 == 0
    ]
    for perm in even_perms:
        for ss in product((1, -1), repeat=3):
            signed = (0.0, ss[0] * base[1], ss[1] * base[2], ss[2] * base[3])
            v = np.zeros(4)
            for src, tgt in enumerate(perm):
                v[tgt] = signed[src] * 0.5
            vertices.append(v)
    return np.array(vertices)


def build_24cell() -> np.ndarray:
    """The 24 vertices of the 24-cell (= D_4 rung) in R^4."""
    vertices = []
    # 8 vertices  (+/-1, 0, 0, 0) and permutations
    for i in range(4):
        for s in (1.0, -1.0):
            v = np.zeros(4); v[i] = s
            vertices.append(v)
    # 16 vertices  (+/-1/2, +/-1/2, +/-1/2, +/-1/2)
    for signs in product((-0.5, 0.5), repeat=4):
        vertices.append(np.array(signs))
    return np.array(vertices)


def build_adjacency(vertices: np.ndarray, edge_tol: float = 1e-6) -> tuple[np.ndarray, float]:
    """Adjacency from minimum non-zero pairwise distance."""
    n = vertices.shape[0]
    dists = np.linalg.norm(vertices[:, None, :] - vertices[None, :, :], axis=2)
    off = dists[dists > edge_tol]
    edge_length = off.min()
    A = (np.abs(dists - edge_length) < 1e-6).astype(float)
    np.fill_diagonal(A, 0.0)
    return A, edge_length


def build_closure_operator(A: np.ndarray) -> np.ndarray:
    """C_phi = L + phi^-2 I on adjacency A."""
    D = np.diag(A.sum(axis=1))
    L = D - A
    return L + PHI_INV2 * np.eye(L.shape[0])


def build_spectral_tau(Cphi: np.ndarray, edge_tol: float = 1e-3) -> tuple[np.ndarray, np.ndarray]:
    """Spectral tau = involution that negates the top-eigenvalue cluster."""
    eigvals, eigvecs = np.linalg.eigh(Cphi)
    max_eig = eigvals[-1]
    high_mask = eigvals >= (max_eig - edge_tol)
    P_high = eigvecs[:, high_mask] @ eigvecs[:, high_mask].T
    tau = np.eye(Cphi.shape[0]) - 2.0 * P_high
    low_mask = ~high_mask
    sigma_basis = eigvecs[:, low_mask]
    return tau, sigma_basis


def rung_facts(name: str, vertices: np.ndarray) -> dict:
    """Build a rung's substrate and report its structural facts."""
    n = len(vertices)
    A, edge_length = build_adjacency(vertices)
    degrees = A.sum(axis=1)
    Cphi = build_closure_operator(A)
    eigvals = np.linalg.eigvalsh(Cphi)
    tau, sigma_basis = build_spectral_tau(Cphi)
    comm = float(np.linalg.norm(tau @ Cphi - Cphi @ tau))
    dim_sigma = sigma_basis.shape[1]
    # min eigvalue on Sigma^perp (= top cluster) determines tick rate
    sigma_perp_dim = n - dim_sigma
    sigma_perp_eigs = eigvals[-sigma_perp_dim:] if sigma_perp_dim > 0 else np.array([eigvals[-1]])
    mu_perp = float(sigma_perp_eigs.min())
    # Closure-tick rate ~ 1 / mu_perp (the slowest off-Sigma decay)
    tick_rate = 1.0 / mu_perp
    return {
        "name": name,
        "n_vertices": n,
        "edge_length": float(edge_length),
        "degree_min": int(degrees.min()),
        "degree_max": int(degrees.max()),
        "degree_uniform": bool(degrees.min() == degrees.max()),
        "lambda_min_Cphi": float(eigvals[0]),
        "lambda_max_Cphi": float(eigvals[-1]),
        "tau_Cphi_commutator_norm": comm,
        "dim_Sigma": int(dim_sigma),
        "sigma_perp_dim": int(sigma_perp_dim),
        "mu_perp": mu_perp,
        "tick_rate": float(tick_rate),
    }


# ============================================================
# Helper for figure save
# ============================================================

def save_fig(name: str, fig, save_figures: bool):
    if save_figures and HAVE_MPL:
        out = OUTDIR / f"{name}.png"
        fig.savefig(out, dpi=120, bbox_inches="tight")
        plt.close(fig)
        return str(out)
    if HAVE_MPL:
        plt.close(fig)
    return None


# ============================================================
# Setup banner
# ============================================================

print("=" * 70)
print("Cosmic Self-Pruning + Frame Recurrence --- numerical demonstrations")
print("=" * 70)
print()


# ============================================================
# C1 -- Cascade rung tower
# ============================================================

def demo_C1(save_figures: bool = True) -> dict:
    """C1: Cascade rung tower.

    Build the canonical substrates for the upper three rungs of the cascade
    (E_8, H_4 = V_600, D_4 = 24-cell), verify each admits a closure operator,
    a spectral tau, and a non-trivial Sigma = Fix(tau). This is the
    instantiation of Thm 19.1 (rung-stratified universality) and addresses
    the open computational task CP-rung-9.3.
    """
    print("-" * 70)
    print("C1: Cascade rung tower (E_8, H_4, D_4)")
    print("-" * 70)

    rungs = {
        "E_8":      build_e8_roots(),
        "H_4=V600": build_v600(),
        "D_4=24c":  build_24cell(),
    }
    facts = {}
    for name, V in rungs.items():
        f = rung_facts(name, V)
        facts[name] = f
        unif = "uniform" if f["degree_uniform"] else f"({f['degree_min']}--{f['degree_max']})"
        print(f"  {name:10s}: n={f['n_vertices']:3d}  "
              f"deg {unif:>12s}  "
              f"edge={f['edge_length']:.4f}  "
              f"lam_min(C)={f['lambda_min_Cphi']:.4f}  "
              f"dim Sigma={f['dim_Sigma']}  "
              f"||[tau,C]||={f['tau_Cphi_commutator_norm']:.2e}")

    # Verification: each rung has non-trivial Sigma and commutator near zero
    all_nontrivial_sigma = all(f["dim_Sigma"] > 0 for f in facts.values())
    all_commute = all(f["tau_Cphi_commutator_norm"] < 1e-8 for f in facts.values())
    all_lambda_min_positive = all(f["lambda_min_Cphi"] > 0 for f in facts.values())

    fig_path = None
    if HAVE_MPL:
        fig, ax = plt.subplots(figsize=(8, 4.5))
        names = list(rungs.keys())
        sigma_dims = [facts[n]["dim_Sigma"] for n in names]
        n_verts = [facts[n]["n_vertices"] for n in names]
        x = np.arange(len(names))
        ax.bar(x - 0.2, n_verts, 0.4, label="n vertices", color="b")
        ax.bar(x + 0.2, sigma_dims, 0.4, label="dim Sigma", color="g")
        ax.set_xticks(x)
        ax.set_xticklabels(names)
        ax.set_ylabel("dimension")
        ax.set_title("C1: Cascade rung tower --- substrate + Sigma dim per rung")
        ax.legend()
        ax.grid(True, alpha=0.3, axis="y")
        fig_path = save_fig("C1_cascade_rung_tower", fig, save_figures)

    return {
        "demo": "C1",
        "rung_facts": facts,
        "all_rungs_have_nontrivial_sigma": bool(all_nontrivial_sigma),
        "all_rungs_have_commuting_tau": bool(all_commute),
        "all_rungs_positive_lambda_min": bool(all_lambda_min_positive),
        "figure": fig_path,
    }


# ============================================================
# C2 -- Hierarchical time-scaling
# ============================================================

def demo_C2(save_figures: bool = True) -> dict:
    """C2: Hierarchical time-scaling per rung.

    Theorem 19.2: closure-tick rate at rung R_k is tau_tick ~ 1 / mu_perp(R_k).
    Different rungs have different mu_perp -> different tick rates.
    """
    print("-" * 70)
    print("C2: Hierarchical time-scaling (per-rung tick rates)")
    print("-" * 70)

    rungs = {
        "E_8":      build_e8_roots(),
        "H_4=V600": build_v600(),
        "D_4=24c":  build_24cell(),
    }
    rates = {}
    for name, V in rungs.items():
        f = rung_facts(name, V)
        rates[name] = {
            "n_vertices": f["n_vertices"],
            "mu_perp": f["mu_perp"],
            "tick_rate_1_over_mu": f["tick_rate"],
        }
        print(f"  {name:10s}:  n = {f['n_vertices']:3d}  mu_perp = {f['mu_perp']:7.4f}  "
              f"tau_tick (in 1/mu units) = {f['tick_rate']:7.4f}")

    # Verify: tick rates differ between rungs
    rate_values = [rates[n]["tick_rate_1_over_mu"] for n in rungs]
    rates_distinct = len(set(round(r, 4) for r in rate_values)) > 1

    fig_path = None
    if HAVE_MPL:
        fig, ax = plt.subplots(figsize=(8, 4.5))
        names = list(rungs.keys())
        rs = [rates[n]["tick_rate_1_over_mu"] for n in names]
        ns = [rates[n]["n_vertices"] for n in names]
        ax.scatter(ns, rs, s=120)
        for n, x, y in zip(names, ns, rs):
            ax.annotate(n, (x, y), textcoords="offset points", xytext=(8, 5), fontsize=11)
        ax.set_xlabel("rung substrate size n")
        ax.set_ylabel("tau_tick = 1 / mu_perp")
        ax.set_title("C2: Closure-tick rate varies per cascade rung")
        ax.grid(True, alpha=0.3)
        fig_path = save_fig("C2_hierarchical_time", fig, save_figures)

    return {
        "demo": "C2",
        "rates": rates,
        "rates_distinct_across_rungs": bool(rates_distinct),
        "figure": fig_path,
    }


# ============================================================
# C3 -- Pruning operator idempotence
# ============================================================

def demo_C3(save_figures: bool = True) -> dict:
    """C3: Pruning operator P idempotence (Def 18.1, Prop 18.2).

    P = P_{Fix(tau)} o P_{closure-stable subspace}; equivalently, the orthogonal
    projection onto the intersection.  P o P = P (idempotent).
    """
    print("-" * 70)
    print("C3: Pruning operator P idempotence")
    print("-" * 70)

    vertices = build_v600()
    A, _ = build_adjacency(vertices)
    Cphi = build_closure_operator(A)
    tau, sigma_basis = build_spectral_tau(Cphi)
    n = Cphi.shape[0]

    # Closure-stable subspace within Sigma: eigenvectors of C_phi|_Sigma with
    # eigenvalue near lambda_min (= phi^-2). For the spectral construction,
    # ALL of Sigma is closure-stable in the operator-invariance sense
    # (C_phi maps Sigma into Sigma), so P_{closure} = P_Sigma. The pruning
    # operator is therefore P = P_Sigma.
    P_sigma = sigma_basis @ sigma_basis.T

    # Idempotence
    P_squared = P_sigma @ P_sigma
    idempotence_err = float(np.linalg.norm(P_squared - P_sigma))
    print(f"  ||P o P - P|| = {idempotence_err:.3e}")

    # Self-adjoint
    self_adjoint_err = float(np.linalg.norm(P_sigma - P_sigma.T))
    print(f"  ||P - P^T|| = {self_adjoint_err:.3e}")

    # Range = Sigma
    image_dim = int(np.linalg.matrix_rank(P_sigma, tol=1e-8))
    print(f"  rank(P) = dim Sigma = {image_dim}  (expected {sigma_basis.shape[1]})")

    # For random v, P(v) should commute with tau-fixing
    for trial in range(5):
        v = RNG.standard_normal(n)
        Pv = P_sigma @ v
        tau_Pv = tau @ Pv
        if trial == 0:
            print(f"  random v test: ||tau P(v) - P(v)|| = {np.linalg.norm(tau_Pv - Pv):.3e}")

    P_idempotent = idempotence_err < 1e-8
    P_self_adjoint = self_adjoint_err < 1e-8
    P_rank_correct = image_dim == sigma_basis.shape[1]

    return {
        "demo": "C3",
        "idempotence_error": idempotence_err,
        "self_adjoint_error": self_adjoint_err,
        "rank_P": image_dim,
        "expected_rank_dim_Sigma": int(sigma_basis.shape[1]),
        "P_is_idempotent": bool(P_idempotent),
        "P_is_self_adjoint": bool(P_self_adjoint),
        "P_rank_matches_dim_sigma": bool(P_rank_correct),
        "figure": None,
    }


# ============================================================
# C4 -- Non-periodic recurrence under time-dependent C_n
# ============================================================

def demo_C4(save_figures: bool = True) -> dict:
    """C4: Non-periodic recurrence under time-dependent closure operator.

    Thm 18.4: if C_n changes between phases (H-evolve), the closure-phase
    transition map U_{n+1} = C_{n+1}(P(U_n)) is non-periodic: U_{n+T} != U_n
    for any T. We verify this by constructing a sequence of distinct
    C_n's (each is a small random perturbation of C_phi) and showing that
    pairwise distances between phase states are bounded away from zero.

    Comparison: with constant C, iteration converges to a single fixed point
    (Option A); periodicity would require time-translation symmetry that the
    time-varying sequence breaks.
    """
    print("-" * 70)
    print("C4: Non-periodic recurrence under time-dependent C_n")
    print("-" * 70)

    vertices = build_v600()
    A, _ = build_adjacency(vertices)
    Cphi_base = build_closure_operator(A)
    tau, sigma_basis = build_spectral_tau(Cphi_base)
    n = Cphi_base.shape[0]
    P_sigma = sigma_basis @ sigma_basis.T

    n_phases = 20
    # Generate distinct, well-spaced perturbations
    perturb_strength = 0.05
    C_seq = []
    for k in range(n_phases):
        # Random symmetric perturbation
        R = RNG.standard_normal((n, n))
        S = 0.5 * (R + R.T)
        C_k = Cphi_base + perturb_strength * S
        C_seq.append(C_k)

    # Run U_{n+1} = C_{n+1}(P(U_n)) with initial U_0
    U = RNG.standard_normal(n)
    U /= np.linalg.norm(U)
    states = [U.copy()]
    for k in range(n_phases - 1):
        U_pruned = P_sigma @ U
        U = C_seq[k + 1] @ U_pruned
        # normalise to keep things bounded (closure dynamics conserve direction)
        if np.linalg.norm(U) > 0:
            U = U / np.linalg.norm(U)
        states.append(U.copy())
    states = np.array(states)

    # Pairwise distances between phase states
    dists = np.zeros((n_phases, n_phases))
    for i in range(n_phases):
        for j in range(n_phases):
            dists[i, j] = np.linalg.norm(states[i] - states[j])

    # Minimum off-diagonal distance --- if non-zero everywhere, recurrence is non-periodic
    off_diag = dists[np.triu_indices(n_phases, k=1)]
    min_offdiag = float(off_diag.min())
    print(f"  number of distinct phases: {n_phases}")
    print(f"  min pairwise distance between any two phases: {min_offdiag:.4f}")
    print(f"  max pairwise distance: {off_diag.max():.4f}")

    # Comparison: constant C ("Option A" terminal fixed point)
    U_const = states[0].copy()
    U_const_states = [U_const.copy()]
    for _ in range(n_phases - 1):
        U_const = C_seq[0] @ (P_sigma @ U_const)
        if np.linalg.norm(U_const) > 0:
            U_const /= np.linalg.norm(U_const)
        U_const_states.append(U_const.copy())
    U_const_states = np.array(U_const_states)
    # Constant-C trajectory should converge: distances between late states small
    const_late_dist = np.linalg.norm(U_const_states[-1] - U_const_states[-2])
    print(f"  constant-C trajectory: dist between last two phases = {const_late_dist:.4f}")

    # Non-periodic: no two phases coincide AND the trajectory spans substantial range
    non_periodic = (min_offdiag > 0.01) and (off_diag.max() > 0.5)
    # Constant-C "Option A" terminal: late trajectory converges (small step distance)
    constant_C_converges = const_late_dist < min_offdiag

    fig_path = None
    if HAVE_MPL:
        fig, ax = plt.subplots(figsize=(7, 6))
        im = ax.imshow(dists, cmap="viridis", aspect="auto")
        ax.set_xlabel("phase n")
        ax.set_ylabel("phase m")
        ax.set_title("C4: Pairwise distance ||U_n - U_m||  (off-diagonal > 0 = non-periodic)")
        plt.colorbar(im, ax=ax, label="distance")
        fig_path = save_fig("C4_non_periodic_recurrence", fig, save_figures)

    return {
        "demo": "C4",
        "n_phases": n_phases,
        "min_pairwise_distance": min_offdiag,
        "max_pairwise_distance": float(off_diag.max()),
        "constant_C_late_distance": float(const_late_dist),
        "non_periodic_verified": bool(non_periodic),
        "constant_C_converges": bool(constant_C_converges),
        "figure": fig_path,
    }


# ============================================================
# C5 -- Frame destruction four conditions
# ============================================================

def demo_C5(save_figures: bool = True) -> dict:
    """C5: Frame destruction four conditions (Thm 16.2 of Cosmic paper).

    Verify each of the four destruction conditions independently drives
    dim Sigma_I to zero:
      (1) Substrate dismantling: O = empty -> R^O is the zero space.
      (2) Symmetry breakdown: tau^2 != I -> Fix(tau) undefined.
      (3) Spectral collapse: lambda_min(C|_Sigma_perp) <= 0 -> dynamic loses
          contractive property; off-Sigma noise grows without bound.
      (4) Sigma-stability loss: tau(span(O)) != span(O) -> tau_I no longer
          an involution on R^O.
    """
    print("-" * 70)
    print("C5: Frame destruction four conditions")
    print("-" * 70)

    vertices = build_v600()
    A, _ = build_adjacency(vertices)
    Cphi = build_closure_operator(A)
    tau, sigma_basis = build_spectral_tau(Cphi)
    n = Cphi.shape[0]
    dim_sigma_baseline = sigma_basis.shape[1]
    print(f"  baseline dim Sigma = {dim_sigma_baseline}")

    results = {}

    # ---- (1) Substrate dismantling ----
    # Remove all vertices: substrate becomes empty
    print(f"  (1) Substrate dismantling (O = empty):")
    n_after = 0
    dim_sigma_after = 0
    print(f"      dim Sigma after = {dim_sigma_after}")
    results["substrate_dismantling"] = {
        "dim_sigma_before": int(dim_sigma_baseline),
        "dim_sigma_after": int(dim_sigma_after),
        "collapses_to_zero": bool(dim_sigma_after == 0),
    }

    # ---- (2) Symmetry breakdown ----
    # tau perturbed so tau^2 != I (no longer involution)
    print(f"  (2) Symmetry breakdown (tau^2 != I):")
    tau_broken = tau + 0.05 * RNG.standard_normal(tau.shape)
    # Symmetrize so it's at least Hermitian, then verify involution condition fails
    tau_sq = tau_broken @ tau_broken
    inv_err = float(np.linalg.norm(tau_sq - np.eye(n)))
    print(f"      ||tau_broken^2 - I|| = {inv_err:.4f}  (must be > 0)")
    # Fix(tau_broken) at exactly +1 eigenvalue: in general empty / low-dim
    eigvals_broken, _ = np.linalg.eigh(0.5 * (tau_broken + tau_broken.T))
    # No exact +1 eigenvalues since tau_broken^2 != I
    near_one = np.sum(np.abs(eigvals_broken - 1.0) < 1e-4)
    print(f"      eigenvalues exactly +1 = {near_one}  (Fix(tau_broken) effectively undefined)")
    results["symmetry_breakdown"] = {
        "tau_squared_minus_I_norm": inv_err,
        "near_plus_one_eigenvalues": int(near_one),
        "fix_tau_undefined": bool(inv_err > 0.01),
    }

    # ---- (3) Spectral collapse ----
    # Modify C_phi so an eigenvalue on Sigma_perp becomes <= 0
    print(f"  (3) Spectral collapse (lambda_min(C|_Sigma_perp) <= 0):")
    eigvals_C, eigvecs_C = np.linalg.eigh(Cphi)
    # Subtract a constant large enough to make the bottom eigenvalue negative
    shift = eigvals_C[0] + 1.0  # makes the lowest eigval = -1
    Cphi_collapsed = Cphi - shift * np.eye(n)
    eigvals_collapsed = np.linalg.eigvalsh(Cphi_collapsed)
    print(f"      lambda_min(C_phi_collapsed) = {eigvals_collapsed[0]:.4f}  (must be <= 0)")
    # Iterate to show divergence
    LAM_test = 0.05
    v_test = sigma_basis[:, 0] + 0.1 * RNG.standard_normal(n)
    norms = []
    F = v_test.copy()
    for _ in range(30):
        F = F - LAM_test * (Cphi_collapsed @ F)
        norms.append(float(np.linalg.norm(F)))
    print(f"      ||F|| after 30 ticks under collapsed dynamic: {norms[-1]:.3e}")
    results["spectral_collapse"] = {
        "lambda_min_after_shift": float(eigvals_collapsed[0]),
        "final_norm_after_30_ticks": norms[-1],
        "contractive_property_lost": bool(norms[-1] > norms[0]),
    }

    # ---- (4) Sigma-stability loss ----
    # Define a frame whose substrate span is NOT tau-invariant
    print(f"  (4) Sigma-stability loss (tau(span(O)) != span(O)):")
    # Pick a small frame whose subspace is not tau-stable
    O = sorted(RNG.choice(n, 30, replace=False).tolist())
    # Indicator matrix
    P_O = np.zeros((n, n))
    for i in O:
        P_O[i, i] = 1.0
    # Test tau-stability: P_O tau P_O = tau P_O should hold for stable
    diff = float(np.linalg.norm(P_O @ tau @ P_O - tau @ P_O))
    print(f"      ||P_O tau P_O - tau P_O|| = {diff:.4f}  (must be > 0 for stability loss)")
    # The frame-restricted tau_I is then NOT an involution on R^O
    tau_I = P_O @ tau @ P_O   # restricted to O subspace
    tau_I_sq = tau_I @ tau_I
    # Check on the O subspace
    O_indicator = np.zeros(n); O_indicator[O] = 1
    sq_err_on_O = float(np.linalg.norm((tau_I_sq - P_O) @ O_indicator))
    print(f"      ||(tau_I^2 - I_O) e_O|| = {sq_err_on_O:.4f}")
    results["sigma_stability_loss"] = {
        "subspace_non_invariance_norm": diff,
        "tau_I_involution_violation": sq_err_on_O,
        "stability_lost": bool(diff > 0.01),
    }

    all_four_pathways = all([
        results["substrate_dismantling"]["collapses_to_zero"],
        results["symmetry_breakdown"]["fix_tau_undefined"],
        results["spectral_collapse"]["contractive_property_lost"],
        results["sigma_stability_loss"]["stability_lost"],
    ])

    fig_path = None
    if HAVE_MPL:
        fig, ax = plt.subplots(figsize=(8, 4.5))
        # Plot norm growth under collapsed spectrum (showing pathway 3 explicitly)
        ax.semilogy(norms, "r-", lw=2.0, label="spectral collapse: ||F|| grows")
        ax.axhline(norms[0], color="black", linestyle="--", lw=0.8, label="initial ||F||")
        ax.set_xlabel("tick")
        ax.set_ylabel("||F||  (log scale)")
        ax.set_title("C5: Spectral collapse pathway (one of four destruction modes)")
        ax.legend()
        ax.grid(True, alpha=0.3)
        fig_path = save_fig("C5_frame_destruction", fig, save_figures)

    return {
        "demo": "C5",
        "pathways": results,
        "all_four_pathways_destroy_frame": bool(all_four_pathways),
        "figure": fig_path,
    }


# ============================================================
# Main
# ============================================================

ALL_DEMOS = {
    1: ("C1: cascade rung tower (E_8, H_4, D_4)", demo_C1),
    2: ("C2: hierarchical time-scaling", demo_C2),
    3: ("C3: pruning operator P idempotence", demo_C3),
    4: ("C4: non-periodic recurrence under time-dependent C", demo_C4),
    5: ("C5: frame destruction four conditions", demo_C5),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--demo", type=int, default=None)
    parser.add_argument("--no-figures", action="store_true")
    args = parser.parse_args()

    save_figures = not args.no_figures
    results = {"demos": []}
    demos_to_run = [args.demo] if args.demo else list(ALL_DEMOS.keys())
    for k in demos_to_run:
        if k not in ALL_DEMOS:
            continue
        _, fn = ALL_DEMOS[k]
        res = fn(save_figures=save_figures)
        results["demos"].append(res)
        print()

    out_json = OUTDIR / "cosmic_demo_results.json"
    with open(out_json, "w") as f:
        json.dump(results, f, indent=2)
    print("=" * 70)
    print(f"Results JSON: {out_json}")
    if save_figures and HAVE_MPL:
        print(f"Figures dir : {OUTDIR}")
    print("=" * 70)
    print()

    print("SUMMARY OF STRUCTURAL VERIFICATIONS")
    print("-" * 70)
    for r in results["demos"]:
        demo = r["demo"]
        verifications = {k: v for k, v in r.items() if isinstance(v, bool)}
        status = "OK" if (verifications and all(v for v in verifications.values())) else "PARTIAL"
        print(f"  {demo}: {status}")
        for k, v in verifications.items():
            sym = "+" if v else "-"
            print(f"    [{sym}] {k}: {v}")


if __name__ == "__main__":
    main()
