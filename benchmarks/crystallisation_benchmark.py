"""
VFD Crystallisation — Benchmark Engine
========================================

Orchestrates fair comparison across all four models on identical setups.

Usage:
    python benchmarks/crystallisation_benchmark.py
"""

from __future__ import annotations
import sys
import os
import dataclasses
import json
from typing import Optional

import numpy as np
from numpy.typing import NDArray

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from vfd.crystallisation.models import (
    LindbladModel, GRWModel, ORModel, CrystallisationModel,
)
from vfd.crystallisation.benchmark_metrics import (
    outcome_entropy, repeatability_score, transition_time,
    transition_time_variance, trajectory_divergence,
    basin_preference_index, coherence_profile, purity_profile,
    collect_all_metrics, ks_test, bootstrap_ci,
)


# ═══════════════════════════════════════════════════════════════════════
# Benchmark configuration
# ═══════════════════════════════════════════════════════════════════════

@dataclasses.dataclass
class BenchmarkConfig:
    """Configuration for a benchmark scenario."""
    name: str
    n_states: int
    H: NDArray
    rho_init: NDArray
    T: float = 10.0
    dt: float = 0.05
    n_trials: int = 100
    gamma_env: float = 0.05
    lambda_grw: float = 0.01
    or_coupling: float = 0.5
    vfd_lambda: float = 1.0
    vfd_alpha: float = 1.0
    vfd_beta: float = 0.5
    vfd_gamma: float = 0.8
    seed: int = 42


@dataclasses.dataclass
class ModelResult:
    """Results from running one model on a benchmark."""
    model_name: str
    outcomes: NDArray
    transition_times: NDArray
    trajectories: list[list[NDArray]]
    metrics: dict


@dataclasses.dataclass
class BenchmarkResult:
    """Complete benchmark comparison result."""
    config_name: str
    results: dict  # model_name -> ModelResult
    comparisons: dict  # pairwise statistical comparisons


# ═══════════════════════════════════════════════════════════════════════
# Preset scenarios
# ═══════════════════════════════════════════════════════════════════════

def make_qubit_config(seed: int = 42) -> BenchmarkConfig:
    """S1 — Single qubit: equal superposition."""
    H = np.array([[0, 0.1], [0.1, 0]], dtype=np.complex128)
    rho = np.array([[0.5, 0.5], [0.5, 0.5]], dtype=np.complex128)
    return BenchmarkConfig(name="qubit", n_states=2, H=H, rho_init=rho,
                           T=5.0, dt=0.05, n_trials=50, seed=seed)


def make_biased_config(seed: int = 42) -> BenchmarkConfig:
    """S2 — Biased two-state: slight energy asymmetry."""
    H = np.array([[0, 0.1], [0.1, 0.3]], dtype=np.complex128)
    rho = np.array([[0.5, 0.5], [0.5, 0.5]], dtype=np.complex128)
    return BenchmarkConfig(name="biased", n_states=2, H=H, rho_init=rho,
                           T=5.0, dt=0.05, n_trials=50, seed=seed)


def make_multilevel_config(n: int = 4, seed: int = 42) -> BenchmarkConfig:
    """S3 — Multi-level system: n competing states."""
    rng = np.random.default_rng(seed)
    H = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    H = 0.1 * (H + H.conj().T)  # Hermitian
    rho = np.ones((n, n), dtype=np.complex128) / n
    return BenchmarkConfig(name=f"multilevel_{n}", n_states=n, H=H, rho_init=rho,
                           T=8.0, dt=0.05, n_trials=50, seed=seed)


def make_noise_sweep_config(gamma: float, seed: int = 42) -> BenchmarkConfig:
    """S5 — Noise sweep: vary environment coupling."""
    H = np.array([[0, 0.1, 0], [0.1, 0, 0.1], [0, 0.1, 0]], dtype=np.complex128)
    rho = np.ones((3, 3), dtype=np.complex128) / 3
    return BenchmarkConfig(name=f"noise_gamma_{gamma:.2f}", n_states=3,
                           H=H, rho_init=rho, T=6.0, dt=0.05,
                           n_trials=50, gamma_env=gamma, seed=seed)


# ═══════════════════════════════════════════════════════════════════════
# Model factory
# ═══════════════════════════════════════════════════════════════════════

def create_models(config: BenchmarkConfig) -> dict:
    """Create all four models with matched parameters."""
    return {
        "Lindblad": LindbladModel(
            H=config.H, gamma=config.gamma_env, seed=config.seed,
        ),
        "GRW": GRWModel(
            H=config.H, gamma=config.gamma_env,
            lambda_grw=config.lambda_grw, seed=config.seed,
        ),
        "OR": ORModel(
            H=config.H, gamma=config.gamma_env,
            or_coupling=config.or_coupling, seed=config.seed,
        ),
        "VFD": CrystallisationModel(
            H=config.H, gamma_env=config.gamma_env,
            lam=config.vfd_lambda, alpha=config.vfd_alpha,
            beta=config.vfd_beta, gamma_coherence=config.vfd_gamma,
            seed=config.seed,
        ),
    }


# ═══════════════════════════════════════════════════════════════════════
# Run single model
# ═══════════════════════════════════════════════════════════════════════

def run_model(model, config: BenchmarkConfig) -> ModelResult:
    """Run one model for n_trials, collect outcomes and trajectories."""
    outcomes = []
    times = []
    trajectories = []

    for trial in range(config.n_trials):
        # Reset RNG per trial for stochastic models
        if hasattr(model, 'rng'):
            model.rng = np.random.default_rng(config.seed + trial)

        traj = model.run(config.rho_init, config.T, config.dt)
        outcome = model.measure(traj[-1])
        t_time = transition_time(traj)

        outcomes.append(outcome)
        times.append(t_time)
        trajectories.append(traj)

    outcomes = np.array(outcomes)
    times = np.array(times, dtype=float)
    metrics = collect_all_metrics(outcomes, times, trajectories, config.n_states)

    return ModelResult(
        model_name=model.name,
        outcomes=outcomes,
        transition_times=times,
        trajectories=trajectories,
        metrics=metrics,
    )


# ═══════════════════════════════════════════════════════════════════════
# Run full benchmark
# ═══════════════════════════════════════════════════════════════════════

def run_benchmark(config: BenchmarkConfig) -> BenchmarkResult:
    """Run all four models on the same config and compare."""
    models = create_models(config)
    results = {}

    for name, model in models.items():
        results[name] = run_model(model, config)

    # Pairwise comparisons (VFD vs each baseline)
    comparisons = {}
    vfd_result = results["VFD"]
    for baseline in ["Lindblad", "GRW", "OR"]:
        bl_result = results[baseline]
        ks_stat, ks_pval = ks_test(
            vfd_result.transition_times, bl_result.transition_times
        )
        comparisons[f"VFD_vs_{baseline}"] = {
            "ks_statistic": ks_stat,
            "ks_pvalue": ks_pval,
            "entropy_vfd": vfd_result.metrics["outcome_entropy"],
            "entropy_baseline": bl_result.metrics["outcome_entropy"],
            "repeatability_vfd": vfd_result.metrics["repeatability"],
            "repeatability_baseline": bl_result.metrics["repeatability"],
        }

    return BenchmarkResult(
        config_name=config.name,
        results=results,
        comparisons=comparisons,
    )


def summarise_benchmark(result: BenchmarkResult) -> str:
    """Generate a text summary of benchmark results."""
    lines = [f"=== Benchmark: {result.config_name} ===\n"]

    for name, mr in result.results.items():
        lines.append(f"  {name}:")
        lines.append(f"    Entropy:       {mr.metrics['outcome_entropy']:.4f}")
        lines.append(f"    Repeatability: {mr.metrics['repeatability']:.4f}")
        lines.append(f"    Transition μ:  {mr.metrics['transition_time_mean']:.2f}")
        lines.append(f"    Transition σ:  {mr.metrics['transition_time_std']:.2f}")
        lines.append(f"    Basin pref:    {mr.metrics['basin_preference']}")
        lines.append("")

    lines.append("  Comparisons (VFD vs baselines):")
    for comp_name, comp in result.comparisons.items():
        lines.append(f"    {comp_name}:")
        lines.append(f"      KS stat={comp['ks_statistic']:.4f}, p={comp['ks_pvalue']:.4f}")
        lines.append(f"      Entropy: VFD={comp['entropy_vfd']:.4f} vs {comp['entropy_baseline']:.4f}")
        lines.append(f"      Repeat:  VFD={comp['repeatability_vfd']:.4f} vs {comp['repeatability_baseline']:.4f}")

    return "\n".join(lines)


# ═══════════════════════════════════════════════════════════════════════
# CLI entry point
# ═══════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    configs = [
        make_qubit_config(),
        make_biased_config(),
        make_multilevel_config(4),
        make_noise_sweep_config(0.01),
        make_noise_sweep_config(0.1),
        make_noise_sweep_config(0.5),
    ]

    for config in configs:
        print(f"\nRunning: {config.name}")
        result = run_benchmark(config)
        print(summarise_benchmark(result))
