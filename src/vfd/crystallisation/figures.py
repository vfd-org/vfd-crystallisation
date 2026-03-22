"""
VFD Crystallisation — Preprint Figure Generation
==================================================

Deterministic, reproducible figure generation for the preprint.
All figures use seeded RNG and consistent styling.

Figures:
    FIG 1  Functional descent F(t)
    FIG 2  Mode evolution (spectral coefficients)
    FIG 3  Comparison vs decoherence
    FIG 4  Repeatability (stochastic vs crystallisation)
    FIG 5  Basin selection in multi-attractor landscape
    FIG 6  Transition-time scaling
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from numpy.typing import NDArray

from .operator import (
    CrystallisationParams,
    crystallise,
    crystallisation_flow,
    crystallisation_functional,
    closure_residual,
    energy_functional,
    coherence_metric,
    spectral_reweight,
)
from .falsifiability import (
    simulate_crystallisation_trials,
    simulate_stochastic_collapse_trials,
    simulate_decoherence_trials,
    outcome_entropy,
    repeatability_score,
    basin_preference_index,
    transition_time_stats,
    detect_plateaus,
    transition_time_scaling,
    ExperimentResult,
)


# ═══════════════════════════════════════════════════════════════════════
# Style
# ═══════════════════════════════════════════════════════════════════════

_PALETTE = {
    "vfd": "#2166AC",
    "decoherence": "#B2182B",
    "grw": "#D6604D",
    "mode0": "#2166AC",
    "mode1": "#4393C3",
    "mode2": "#92C5DE",
    "mode3": "#D1E5F0",
    "mode4": "#FDDBC7",
    "mode5": "#F4A582",
    "accent": "#1B7837",
    "grid": "#CCCCCC",
}

_MODE_COLORS = [
    "#2166AC", "#4393C3", "#92C5DE", "#D1E5F0",
    "#FDDBC7", "#F4A582", "#D6604D", "#B2182B",
]


def _apply_style(ax: mpl.axes.Axes) -> None:
    ax.grid(True, alpha=0.25, color=_PALETTE["grid"], linewidth=0.5)
    ax.tick_params(direction="in", top=True, right=True)
    for spine in ax.spines.values():
        spine.set_linewidth(0.6)


def _save(fig: mpl.figure.Figure, path: Optional[str], dpi: int = 300) -> None:
    if path:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(path, dpi=dpi, bbox_inches="tight", facecolor="white")


# ═══════════════════════════════════════════════════════════════════════
# Data generation helpers
# ═══════════════════════════════════════════════════════════════════════

def _make_init_state(n: int, seed: int = 42) -> NDArray:
    rng = np.random.default_rng(seed)
    psi = rng.normal(size=n) + 1j * rng.normal(size=n)
    return psi / np.linalg.norm(psi)


# ═══════════════════════════════════════════════════════════════════════
# FIG 1 — Functional Descent
# ═══════════════════════════════════════════════════════════════════════

def plot_functional_descent(
    save_path: Optional[str] = None,
    n: int = 6,
    seed: int = 42,
) -> mpl.figure.Figure:
    """
    F(t) vs time showing monotonic decrease under gradient flow.
    Also shows R(t), E(t), Q(t) decomposition.
    """
    psi = _make_init_state(n, seed)
    params = CrystallisationParams(
        alpha=1.0, beta=0.5, gamma=0.8,
        eta=0.01, max_steps=1000, tol=1e-8,
        record_trajectory=True,
    )
    result = crystallise(psi, params)
    F_traj = result.F_trajectory
    psi_traj = result.psi_trajectory

    # Compute components
    steps = len(F_traj)
    sample_idx = np.linspace(0, steps - 1, min(200, steps), dtype=int)
    R_t = [closure_residual(psi_traj[i]) for i in sample_idx]
    E_t = [energy_functional(psi_traj[i]) for i in sample_idx]
    Q_t = [coherence_metric(psi_traj[i]) for i in sample_idx]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    # Left: F(t)
    ax1.plot(F_traj, color=_PALETTE["vfd"], linewidth=1.2)
    ax1.set_xlabel("Step")
    ax1.set_ylabel(r"$\mathcal{F}[\Psi]$")
    ax1.set_title("(a) Crystallisation functional")
    _apply_style(ax1)

    # Right: components
    ax2.plot(sample_idx, R_t, label=r"$R$ (residual)", color=_PALETTE["decoherence"], linewidth=1.0)
    ax2.plot(sample_idx, E_t, label=r"$E$ (energy)", color="#E08214", linewidth=1.0)
    ax2.plot(sample_idx, Q_t, label=r"$Q$ (coherence)", color=_PALETTE["accent"], linewidth=1.0)
    ax2.set_xlabel("Step")
    ax2.set_ylabel("Value")
    ax2.set_title("(b) Functional components")
    ax2.legend(fontsize=8, framealpha=0.8)
    _apply_style(ax2)

    fig.tight_layout()
    _save(fig, save_path)
    return fig


# ═══════════════════════════════════════════════════════════════════════
# FIG 2 — Mode Evolution
# ═══════════════════════════════════════════════════════════════════════

def plot_mode_evolution(
    save_path: Optional[str] = None,
    n: int = 6,
    seed: int = 42,
) -> mpl.figure.Figure:
    """Spectral coefficients |c_i(t)| showing structured reweighting."""
    psi = _make_init_state(n, seed)
    params = CrystallisationParams(
        alpha=1.0, beta=0.5, gamma=0.8,
        eta=0.01, max_steps=1000, tol=1e-8,
        record_trajectory=True,
    )
    result = crystallise(psi, params)
    psi_traj = np.array(result.psi_trajectory)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    # Amplitudes
    for i in range(n):
        color = _MODE_COLORS[i % len(_MODE_COLORS)]
        ax1.plot(np.abs(psi_traj[:, i]), color=color, linewidth=1.0,
                 label=f"Mode {i}")
    ax1.set_xlabel("Step")
    ax1.set_ylabel(r"$|c_i|$")
    ax1.set_title("(a) Mode amplitudes")
    ax1.legend(fontsize=7, ncol=2, framealpha=0.8)
    _apply_style(ax1)

    # Phases
    for i in range(n):
        color = _MODE_COLORS[i % len(_MODE_COLORS)]
        ax2.plot(np.angle(psi_traj[:, i]), color=color, linewidth=0.8)
    ax2.set_xlabel("Step")
    ax2.set_ylabel(r"$\arg(c_i)$")
    ax2.set_title("(b) Mode phases")
    _apply_style(ax2)

    fig.tight_layout()
    _save(fig, save_path)
    return fig


# ═══════════════════════════════════════════════════════════════════════
# FIG 3 — Comparison vs Decoherence
# ═══════════════════════════════════════════════════════════════════════

def plot_decoherence_comparison(
    save_path: Optional[str] = None,
    n: int = 3,
    n_trials: int = 100,
    seed: int = 42,
) -> mpl.figure.Figure:
    """
    Same initial state evolved under (a) crystallisation and (b) decoherence.
    Shows outcome distributions and transition-time histograms.
    """
    psi = _make_init_state(n, seed)
    basis = np.eye(n, dtype=np.complex128)
    params = CrystallisationParams(eta=0.01, max_steps=500, tol=1e-6)

    vfd = simulate_crystallisation_trials(
        psi, n_trials=n_trials, n_basins=n, basis=basis,
        params=params, noise_scale=0.0, seed=seed,
    )
    dec = simulate_decoherence_trials(
        psi, n_trials=n_trials, n_basins=n, basis=basis, seed=seed,
    )

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    # Outcome distributions
    x = np.arange(n)
    w = 0.35
    bpi_vfd = basin_preference_index(vfd.outcomes, n)
    bpi_dec = basin_preference_index(dec.outcomes, n)
    born = np.array([np.abs(np.vdot(basis[k], psi))**2 for k in range(n)])
    born = born / born.sum()

    axes[0].bar(x - w/2, bpi_vfd, w, label="Crystallisation", color=_PALETTE["vfd"], alpha=0.85)
    axes[0].bar(x + w/2, bpi_dec, w, label="Decoherence", color=_PALETTE["decoherence"], alpha=0.85)
    axes[0].scatter(x, born, color="black", marker="x", s=60, zorder=5, label=r"$|c_k|^2$")
    axes[0].set_xlabel("Outcome")
    axes[0].set_ylabel("Frequency")
    axes[0].set_title("(a) Outcome distributions")
    axes[0].legend(fontsize=8, framealpha=0.8)
    _apply_style(axes[0])

    # Transition times
    axes[1].hist(vfd.transition_times, bins=25, alpha=0.7,
                 color=_PALETTE["vfd"], label="Crystallisation", density=True)
    axes[1].hist(dec.transition_times, bins=25, alpha=0.7,
                 color=_PALETTE["decoherence"], label="Decoherence", density=True)
    axes[1].set_xlabel("Transition time")
    axes[1].set_ylabel("Density")
    axes[1].set_title("(b) Transition-time distributions")
    axes[1].legend(fontsize=8, framealpha=0.8)
    _apply_style(axes[1])

    fig.tight_layout()
    _save(fig, save_path)
    return fig


# ═══════════════════════════════════════════════════════════════════════
# FIG 4 — Repeatability
# ═══════════════════════════════════════════════════════════════════════

def plot_repeatability(
    save_path: Optional[str] = None,
    n: int = 3,
    n_trials: int = 50,
    n_experiments: int = 15,
    seed: int = 42,
) -> mpl.figure.Figure:
    """
    Multiple experiments from same initial state.
    Show spread of outcome entropy for stochastic vs crystallisation.
    """
    psi = _make_init_state(n, seed)
    basis = np.eye(n, dtype=np.complex128)
    params = CrystallisationParams(eta=0.01, max_steps=500, tol=1e-6)

    H_vfd = []
    H_grw = []
    R_vfd = []
    R_grw = []

    for exp in range(n_experiments):
        vfd = simulate_crystallisation_trials(
            psi, n_trials=n_trials, n_basins=n, basis=basis,
            params=params, noise_scale=0.0, seed=seed + exp * 1000,
        )
        grw = simulate_stochastic_collapse_trials(
            psi, n_trials=n_trials, n_basins=n, basis=basis,
            seed=seed + exp * 1000,
        )
        H_vfd.append(outcome_entropy(vfd.outcomes))
        H_grw.append(outcome_entropy(grw.outcomes))
        R_vfd.append(repeatability_score(vfd.outcomes))
        R_grw.append(repeatability_score(grw.outcomes))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    # Entropy
    ax1.scatter(range(n_experiments), H_vfd, color=_PALETTE["vfd"],
                s=30, alpha=0.8, label="Crystallisation")
    ax1.scatter(range(n_experiments), H_grw, color=_PALETTE["decoherence"],
                s=30, alpha=0.8, label="Stochastic collapse")
    ax1.set_xlabel("Experiment index")
    ax1.set_ylabel("Outcome entropy $H$")
    ax1.set_title("(a) Outcome entropy across experiments")
    ax1.legend(fontsize=8, framealpha=0.8)
    _apply_style(ax1)

    # Repeatability
    ax2.scatter(range(n_experiments), R_vfd, color=_PALETTE["vfd"],
                s=30, alpha=0.8, label="Crystallisation")
    ax2.scatter(range(n_experiments), R_grw, color=_PALETTE["decoherence"],
                s=30, alpha=0.8, label="Stochastic collapse")
    ax2.set_xlabel("Experiment index")
    ax2.set_ylabel("Repeatability $R$")
    ax2.set_title("(b) Repeatability across experiments")
    ax2.legend(fontsize=8, framealpha=0.8)
    _apply_style(ax2)

    fig.tight_layout()
    _save(fig, save_path)
    return fig


# ═══════════════════════════════════════════════════════════════════════
# FIG 5 — Basin Selection
# ═══════════════════════════════════════════════════════════════════════

def plot_basin_selection(
    save_path: Optional[str] = None,
    n: int = 4,
    n_inits: int = 15,
    seed: int = 42,
) -> mpl.figure.Figure:
    """
    Multi-attractor landscape: launch from many initial states,
    show which basin each converges to.
    """
    basis = np.eye(n, dtype=np.complex128)
    params = CrystallisationParams(
        alpha=1.0, beta=0.5, gamma=0.8,
        eta=0.01, max_steps=1000, tol=1e-7,
        record_trajectory=True,
    )

    final_basins = []
    final_F = []
    init_labels = []

    for i in range(n_inits):
        psi = _make_init_state(n, seed + i)
        result = crystallise(psi, params)
        overlaps = np.array([
            np.abs(np.vdot(basis[k], result.psi_star))**2
            for k in range(n)
        ])
        basin = int(np.argmax(overlaps))
        final_basins.append(basin)
        final_F.append(result.F_final)
        init_labels.append(i)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    # Basin assignment
    colors = [_MODE_COLORS[b % len(_MODE_COLORS)] for b in final_basins]
    ax1.scatter(init_labels, final_basins, c=colors, s=40, edgecolors="black",
                linewidths=0.5)
    ax1.set_xlabel("Initial condition index")
    ax1.set_ylabel("Final basin")
    ax1.set_yticks(range(n))
    ax1.set_title("(a) Basin assignment")
    _apply_style(ax1)

    # Final F values by basin
    for b in range(n):
        F_vals = [final_F[i] for i in range(n_inits) if final_basins[i] == b]
        if F_vals:
            ax2.scatter([b] * len(F_vals), F_vals,
                        color=_MODE_COLORS[b % len(_MODE_COLORS)],
                        s=30, alpha=0.7)
    ax2.set_xlabel("Basin")
    ax2.set_ylabel(r"$\mathcal{F}^*$")
    ax2.set_xticks(range(n))
    ax2.set_title(r"(b) Final $\mathcal{F}$ by basin")
    _apply_style(ax2)

    fig.tight_layout()
    _save(fig, save_path)
    return fig


# ═══════════════════════════════════════════════════════════════════════
# FIG 6 — Transition-Time Scaling
# ═══════════════════════════════════════════════════════════════════════

def plot_transition_scaling(
    save_path: Optional[str] = None,
    n: int = 3,
    seed: int = 55,
) -> mpl.figure.Figure:
    """
    tau_crys vs constraint parameter, showing structured scaling.
    """
    psi = _make_init_state(n, seed)
    multipliers = np.linspace(0.5, 2.5, 6)
    params = CrystallisationParams(eta=0.01, max_steps=1500, tol=1e-7)

    residuals, times = transition_time_scaling(psi, multipliers, params=params)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    ax1.plot(multipliers, times, "o-", color=_PALETTE["vfd"], markersize=5, linewidth=1.2)
    ax1.set_xlabel("Constraint scale $\\kappa$")
    ax1.set_ylabel(r"Crystallisation time $\tau$")
    ax1.set_title(r"(a) $\tau$ vs constraint scale")
    _apply_style(ax1)

    ax2.plot(residuals, times, "o-", color=_PALETTE["decoherence"], markersize=5, linewidth=1.2)
    ax2.set_xlabel(r"Closure residual $R$")
    ax2.set_ylabel(r"Crystallisation time $\tau$")
    ax2.set_title(r"(b) $\tau$ vs residual magnitude")
    _apply_style(ax2)

    fig.tight_layout()
    _save(fig, save_path)
    return fig


# ═══════════════════════════════════════════════════════════════════════
# Generate all figures
# ═══════════════════════════════════════════════════════════════════════

def generate_preprint_figures(output_dir: str = "figures") -> dict:
    """Generate the 4 flagship preprint figures."""
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    figs = {}
    figs["fig1"] = plot_functional_descent(f"{output_dir}/fig1_functional_descent.png")
    figs["fig2"] = plot_decoherence_comparison(f"{output_dir}/fig2_decoherence_comparison.png")
    figs["fig3"] = plot_basin_selection(f"{output_dir}/fig3_basin_selection.png")
    figs["fig4"] = plot_transition_scaling(f"{output_dir}/fig4_transition_scaling.png")
    plt.close("all")
    return figs


def generate_all_figures(output_dir: str = "figures") -> dict:
    """Generate all 6 figures (preprint + companion)."""
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    figs = {}
    figs["fig1"] = plot_functional_descent(f"{output_dir}/fig1_functional_descent.png")
    figs["fig2"] = plot_mode_evolution(f"{output_dir}/fig2_mode_evolution.png")
    figs["fig3"] = plot_decoherence_comparison(f"{output_dir}/fig3_decoherence_comparison.png")
    figs["fig4"] = plot_repeatability(f"{output_dir}/fig4_repeatability.png")
    figs["fig5"] = plot_basin_selection(f"{output_dir}/fig5_basin_selection.png")
    figs["fig6"] = plot_transition_scaling(f"{output_dir}/fig6_transition_scaling.png")
    plt.close("all")
    return figs
