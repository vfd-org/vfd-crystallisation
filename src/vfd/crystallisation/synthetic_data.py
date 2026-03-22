"""
VFD Crystallisation — Synthetic Data Generator
================================================

Configurable experiment simulators for generating synthetic measurement
data with controllable noise, observation modes, and model misspecification.

Supports:
    SD-1  Noise-free ideal data
    SD-2  Gaussian-noisy observables
    SD-3  Count-based / multinomial trial data
    SD-4  Partial-observation settings
    SD-5  Misspecified model cases (non-VFD baselines)
"""

from __future__ import annotations

import dataclasses
from typing import Optional, Literal

import numpy as np
from numpy.typing import NDArray

from .operator import (
    CrystallisationParams,
    crystallise,
    crystallisation_flow,
    crystallisation_functional,
    closure_residual,
    energy_functional,
    coherence_metric,
)
from .falsifiability import (
    simulate_crystallisation_trials,
    simulate_stochastic_collapse_trials,
    simulate_decoherence_trials,
    outcome_entropy,
    repeatability_score,
    basin_preference_index,
    transition_time_stats,
    ExperimentResult,
)


# ═══════════════════════════════════════════════════════════════════════
# Experiment configuration
# ═══════════════════════════════════════════════════════════════════════

@dataclasses.dataclass(frozen=True)
class ExperimentConfig:
    """Configuration for a synthetic experiment."""
    n_modes: int = 4
    n_trials: int = 500
    n_basins: int = 4
    noise_scale: float = 0.0
    measurement_noise: float = 0.0
    observation_mode: Literal["full", "outcomes_only", "times_only", "summary_only"] = "full"
    max_steps: int = 2000
    seed: int = 42


@dataclasses.dataclass(frozen=True)
class ModelParams:
    """
    Canonical parameter vector Theta for the crystallisation model.

    Theta = (alpha, beta, gamma, lam, eta, Gamma, R_c, kappa_B, kappa_Q)
    """
    alpha: float = 1.0       # residual weight (dimensionless)
    beta: float = 0.5        # energy weight (dimensionless)
    gamma: float = 0.8       # coherence weight (dimensionless)
    lam: float = 1.0         # crystallisation-drive strength (1/time)
    eta: float = 0.003       # relaxation / step size (1/time)
    Gamma: float = 0.0       # environment coupling (1/time)
    R_c: float = 0.0         # critical residual threshold (dimensionless)
    kappa_B: float = 1.0     # boundary mismatch scaling (dimensionless)
    kappa_Q: float = 1.0     # coherence-response scaling (dimensionless)

    def to_crystallisation_params(self, max_steps: int = 5000) -> CrystallisationParams:
        return CrystallisationParams(
            alpha=self.alpha,
            beta=self.beta,
            gamma=self.gamma,
            eta=self.eta,
            max_steps=max_steps,
            tol=1e-8,
        )

    def to_vector(self) -> NDArray:
        return np.array([
            self.alpha, self.beta, self.gamma, self.lam,
            self.eta, self.Gamma, self.R_c, self.kappa_B, self.kappa_Q,
        ])

    @staticmethod
    def from_vector(v: NDArray) -> "ModelParams":
        return ModelParams(
            alpha=float(v[0]), beta=float(v[1]), gamma=float(v[2]),
            lam=float(v[3]), eta=float(v[4]), Gamma=float(v[5]),
            R_c=float(v[6]), kappa_B=float(v[7]), kappa_Q=float(v[8]),
        )

    @staticmethod
    def param_names() -> list[str]:
        return ["alpha", "beta", "gamma", "lam", "eta", "Gamma", "R_c", "kappa_B", "kappa_Q"]

    @staticmethod
    def n_params() -> int:
        return 9


@dataclasses.dataclass(frozen=True)
class SyntheticDataset:
    """Container for synthetic experimental data."""
    outcomes: Optional[NDArray] = None          # (n_trials,) outcome indices
    transition_times: Optional[NDArray] = None  # (n_trials,) times
    trajectories: Optional[list] = None         # list of (T, n) arrays
    basin_counts: Optional[NDArray] = None      # (n_basins,) counts
    summary: Optional[dict] = None              # entropy, repeatability, etc.
    true_params: Optional[ModelParams] = None
    config: Optional[ExperimentConfig] = None
    model_label: str = "VFD_crystallisation"


# ═══════════════════════════════════════════════════════════════════════
# Observable computation from raw experiment results
# ═══════════════════════════════════════════════════════════════════════

def compute_observables(
    result: ExperimentResult,
    measurement_noise: float = 0.0,
    rng: Optional[np.random.Generator] = None,
) -> dict:
    """Compute observable summary from an ExperimentResult."""
    if rng is None:
        rng = np.random.default_rng(42)

    outcomes = result.outcomes
    times = result.transition_times

    # Add measurement noise to transition times
    if measurement_noise > 0:
        times = times + rng.normal(scale=measurement_noise, size=len(times))
        times = np.maximum(times, 0.0)

    bpi = basin_preference_index(outcomes, result.n_basins)
    t_stats = transition_time_stats(times)

    return {
        "outcome_entropy": outcome_entropy(outcomes),
        "repeatability": repeatability_score(outcomes),
        "basin_preference": bpi,
        "transition_time_mean": t_stats["mean"],
        "transition_time_std": t_stats["std"],
        "transition_time_median": t_stats["median"],
        "transition_time_skewness": t_stats["skewness"],
        "n_trials": len(outcomes),
        "n_basins": result.n_basins,
    }


# ═══════════════════════════════════════════════════════════════════════
# Forward model: params -> observables
# ═══════════════════════════════════════════════════════════════════════

def simulate_observables(
    theta: ModelParams,
    config: ExperimentConfig,
    psi_init: Optional[NDArray] = None,
    basis: Optional[NDArray] = None,
    K: Optional[NDArray] = None,
    L: Optional[NDArray] = None,
) -> dict:
    """
    Forward model: given parameters and experiment config, produce observables.

    This is the core function for parameter estimation — it maps
    Theta -> predicted observables.
    """
    n = config.n_modes
    rng = np.random.default_rng(config.seed)

    if psi_init is None:
        psi_init = rng.normal(size=n) + 1j * rng.normal(size=n)
        psi_init = psi_init / np.linalg.norm(psi_init)
    if basis is None:
        basis = np.eye(n, dtype=np.complex128)

    # Scale constraint target by kappa_B
    if K is None:
        K = np.eye(n, dtype=np.complex128) * theta.kappa_B

    params = theta.to_crystallisation_params(max_steps=config.max_steps)

    # Run trials with environment noise scaled by Gamma
    noise = theta.Gamma * 0.1  # map Gamma to noise scale
    result = simulate_crystallisation_trials(
        psi_init, n_trials=config.n_trials, n_basins=config.n_basins,
        basis=basis, params=params, K=K, L=L,
        noise_scale=noise + config.noise_scale, seed=config.seed,
    )

    return compute_observables(result, config.measurement_noise, rng)


# ═══════════════════════════════════════════════════════════════════════
# Synthetic dataset generators
# ═══════════════════════════════════════════════════════════════════════

def generate_vfd_dataset(
    theta: ModelParams,
    config: ExperimentConfig,
    psi_init: Optional[NDArray] = None,
    basis: Optional[NDArray] = None,
    K: Optional[NDArray] = None,
    L: Optional[NDArray] = None,
) -> SyntheticDataset:
    """SD-1/SD-2: Generate VFD crystallisation data with optional noise."""
    n = config.n_modes
    rng = np.random.default_rng(config.seed)

    if psi_init is None:
        psi_init = rng.normal(size=n) + 1j * rng.normal(size=n)
        psi_init = psi_init / np.linalg.norm(psi_init)
    if basis is None:
        basis = np.eye(n, dtype=np.complex128)
    if K is None:
        K = np.eye(n, dtype=np.complex128) * theta.kappa_B

    params = theta.to_crystallisation_params(max_steps=config.max_steps)
    noise = theta.Gamma * 0.1 + config.noise_scale

    record_traj = config.observation_mode == "full"
    cp = CrystallisationParams(
        alpha=theta.alpha, beta=theta.beta, gamma=theta.gamma,
        eta=theta.eta, max_steps=config.max_steps, tol=1e-8,
        record_trajectory=record_traj,
    )

    result = simulate_crystallisation_trials(
        psi_init, n_trials=config.n_trials, n_basins=config.n_basins,
        basis=basis, params=cp, K=K, L=L,
        noise_scale=noise, seed=config.seed,
        record_trajectories=record_traj,
    )

    outcomes = result.outcomes
    times = result.transition_times

    if config.measurement_noise > 0:
        times = times + rng.normal(scale=config.measurement_noise, size=len(times))
        times = np.maximum(times, 0.0)

    trajectories = None
    if record_traj:
        trajectories = [t.trajectory for t in result.trials if t.trajectory is not None]

    obs = compute_observables(result, config.measurement_noise, rng)

    return _apply_observation_mode(SyntheticDataset(
        outcomes=outcomes,
        transition_times=times,
        trajectories=trajectories,
        basin_counts=basin_preference_index(outcomes, config.n_basins) * config.n_trials,
        summary=obs,
        true_params=theta,
        config=config,
        model_label="VFD_crystallisation",
    ), config)


def generate_multinomial_dataset(
    theta: ModelParams,
    config: ExperimentConfig,
    psi_init: Optional[NDArray] = None,
    basis: Optional[NDArray] = None,
) -> SyntheticDataset:
    """SD-3: Count-based / multinomial trial data."""
    n = config.n_modes
    rng = np.random.default_rng(config.seed)

    if psi_init is None:
        psi_init = rng.normal(size=n) + 1j * rng.normal(size=n)
        psi_init = psi_init / np.linalg.norm(psi_init)
    if basis is None:
        basis = np.eye(n, dtype=np.complex128)

    # Run single crystallisation to get basin preference
    obs = simulate_observables(theta, config, psi_init, basis)
    bpi = obs["basin_preference"]

    # Generate multinomial counts
    counts = rng.multinomial(config.n_trials, bpi)
    outcomes = np.repeat(np.arange(config.n_basins), counts)
    rng.shuffle(outcomes)

    return SyntheticDataset(
        outcomes=outcomes,
        basin_counts=counts.astype(float),
        summary=obs,
        true_params=theta,
        config=config,
        model_label="VFD_multinomial",
    )


def generate_misspecified_dataset(
    config: ExperimentConfig,
    model: Literal["decoherence", "grw"] = "decoherence",
    psi_init: Optional[NDArray] = None,
    basis: Optional[NDArray] = None,
    gamma_env: float = 0.05,
) -> SyntheticDataset:
    """SD-5: Data from non-VFD model for false-positive testing."""
    n = config.n_modes
    rng = np.random.default_rng(config.seed)

    if psi_init is None:
        psi_init = rng.normal(size=n) + 1j * rng.normal(size=n)
        psi_init = psi_init / np.linalg.norm(psi_init)
    if basis is None:
        basis = np.eye(n, dtype=np.complex128)

    if model == "decoherence":
        result = simulate_decoherence_trials(
            psi_init, n_trials=config.n_trials, n_basins=config.n_basins,
            basis=basis, gamma_env=gamma_env, seed=config.seed,
        )
    else:
        result = simulate_stochastic_collapse_trials(
            psi_init, n_trials=config.n_trials, n_basins=config.n_basins,
            basis=basis, seed=config.seed,
        )

    outcomes = result.outcomes
    times = result.transition_times
    obs = compute_observables(result, config.measurement_noise, rng)

    return SyntheticDataset(
        outcomes=outcomes,
        transition_times=times,
        basin_counts=basin_preference_index(outcomes, config.n_basins) * config.n_trials,
        summary=obs,
        true_params=None,
        config=config,
        model_label=f"misspecified_{model}",
    )


def _apply_observation_mode(
    dataset: SyntheticDataset,
    config: ExperimentConfig,
) -> SyntheticDataset:
    """SD-4: Apply partial observation constraints."""
    if config.observation_mode == "full":
        return dataset
    elif config.observation_mode == "outcomes_only":
        return dataclasses.replace(dataset, transition_times=None, trajectories=None)
    elif config.observation_mode == "times_only":
        return dataclasses.replace(dataset, outcomes=None, trajectories=None, basin_counts=None)
    elif config.observation_mode == "summary_only":
        return dataclasses.replace(
            dataset, outcomes=None, transition_times=None,
            trajectories=None, basin_counts=None,
        )
    return dataset


# ═══════════════════════════════════════════════════════════════════════
# Control-response curve generation
# ═══════════════════════════════════════════════════════════════════════

def generate_control_response_curve(
    theta_base: ModelParams,
    param_name: str,
    param_values: NDArray,
    observable_name: str,
    config: ExperimentConfig,
    psi_init: Optional[NDArray] = None,
    basis: Optional[NDArray] = None,
) -> tuple[NDArray, NDArray]:
    """
    Sweep one parameter and record how an observable changes.

    Returns (param_values, observable_values).
    """
    obs_values = []
    for val in param_values:
        theta_dict = dataclasses.asdict(theta_base)
        theta_dict[param_name] = float(val)
        theta = ModelParams(**theta_dict)
        obs = simulate_observables(theta, config, psi_init, basis)
        obs_values.append(obs.get(observable_name, np.nan))
    return np.array(param_values), np.array(obs_values)
