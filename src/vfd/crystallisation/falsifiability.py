"""
VFD Crystallisation — Falsifiability and Statistical Discrimination
====================================================================

Implements metrics, statistical comparison tools, and simulation helpers
for testing the crystallisation operator against competing collapse/decoherence
models.

Signature classes:
    SGT-1  Outcome selection entropy
    SGT-2  Constraint-geometry dependence
    SGT-3  Transition-time scaling
    SGT-4  Basin-of-attraction preference
    SGT-5  Metastable pre-crystallisation regime
    SGT-6  Path-reproducibility signature

Competing models:
    M1  Standard decoherence (Lindblad)
    M2  Effective Copenhagen (projection)
    M3  Many-worlds (unitary, no selection)
    M4  GRW spontaneous collapse
    M5  Penrose OR (gravity threshold)
"""

from __future__ import annotations

import dataclasses
from typing import Callable, Optional, Sequence

import numpy as np
from numpy.typing import NDArray
from scipy import stats as sp_stats

from .operator import (
    CrystallisationParams,
    crystallise,
    crystallisation_flow,
    crystallisation_functional,
    closure_residual,
    coherence_metric,
    energy_functional,
    spectral_reweight,
)


# ═══════════════════════════════════════════════════════════════════════
# Data containers
# ═══════════════════════════════════════════════════════════════════════

@dataclasses.dataclass(frozen=True)
class TrialResult:
    """Single trial outcome."""
    outcome_index: int          # basin / eigenstate index
    transition_time: float      # steps or continuous time to convergence
    final_state: NDArray
    trajectory: Optional[NDArray] = None  # (T, n) state trajectory
    F_trajectory: Optional[NDArray] = None


@dataclasses.dataclass(frozen=True)
class ExperimentResult:
    """Aggregate over many trials."""
    trials: list[TrialResult]
    model_label: str
    n_basins: int

    @property
    def outcomes(self) -> NDArray:
        return np.array([t.outcome_index for t in self.trials])

    @property
    def transition_times(self) -> NDArray:
        return np.array([t.transition_time for t in self.trials])


@dataclasses.dataclass(frozen=True)
class ComparisonResult:
    """Statistical comparison between two models."""
    model_a: str
    model_b: str
    ks_statistic: float
    ks_pvalue: float
    entropy_a: float
    entropy_b: float
    repeatability_a: float
    repeatability_b: float
    trajectory_divergence: Optional[float] = None
    basin_preference_divergence: Optional[float] = None


# ═══════════════════════════════════════════════════════════════════════
# Core metrics
# ═══════════════════════════════════════════════════════════════════════

def outcome_entropy(outcomes: NDArray) -> float:
    """
    H = -sum_i p_i log(p_i)

    Shannon entropy of the outcome distribution.
    Lower entropy under VFD (structured selection) vs stochastic models.
    """
    _, counts = np.unique(outcomes, return_counts=True)
    probs = counts / counts.sum()
    probs = probs[probs > 0]
    return float(-np.sum(probs * np.log(probs)))


def repeatability_score(outcomes: NDArray) -> float:
    """
    R = N_most_common / N_total

    Fraction of trials landing in the most common outcome.
    VFD predicts high repeatability under fixed constraints.
    """
    _, counts = np.unique(outcomes, return_counts=True)
    return float(counts.max() / len(outcomes))


def trajectory_distance(traj_a: NDArray, traj_b: NDArray) -> float:
    """
    D_traj = integral || X(t) - Y(t) || dt

    Integrated L2 distance between two state-space trajectories.
    Approximated by trapezoidal sum over discrete timesteps.
    VFD predicts low D_traj for identical initial conditions.
    """
    min_len = min(len(traj_a), len(traj_b))
    traj_a = traj_a[:min_len]
    traj_b = traj_b[:min_len]
    norms = np.linalg.norm(traj_a - traj_b, axis=1)
    return float(np.trapz(norms))


def transition_time_stats(times: NDArray) -> dict:
    """
    Statistics on transition/crystallisation times.

    Returns mean, std, median, skewness, and dispersion sigma_tau.
    VFD predicts structured scaling; stochastic models predict broader dispersion.
    """
    times = np.asarray(times, dtype=float)
    return {
        "mean": float(np.mean(times)),
        "std": float(np.std(times)),
        "median": float(np.median(times)),
        "skewness": float(sp_stats.skew(times)) if len(times) > 2 else 0.0,
        "dispersion": float(np.sqrt(np.mean(times**2) - np.mean(times)**2)),
        "min": float(np.min(times)),
        "max": float(np.max(times)),
    }


def basin_preference_index(
    assignments: NDArray,
    n_basins: int,
) -> NDArray:
    """
    BPI_k = N_k / N  for each basin k.

    Returns array of length n_basins with preference fractions.
    Under Born rule: BPI_k ~ |c_k|^2.
    Under VFD: BPI_k determined by basin geometry + constraint structure.
    """
    counts = np.zeros(n_basins)
    for a in assignments:
        if 0 <= a < n_basins:
            counts[a] += 1
    total = len(assignments)
    if total == 0:
        return counts
    return counts / total


def constraint_sensitivity(
    observable_fn: Callable[[NDArray], float],
    psi: NDArray,
    constraint_param_index: int,
    eps: float = 1e-5,
    K: Optional[NDArray] = None,
    L: Optional[NDArray] = None,
    params: Optional[CrystallisationParams] = None,
) -> float:
    """
    chi_C = dO/dC

    Numerical derivative of an observable with respect to a constraint parameter.
    VFD predicts nonzero constraint sensitivity; standard models may not.
    """
    if params is None:
        params = CrystallisationParams()

    # Perturb constraint target K
    n = psi.shape[0]
    if K is None:
        K = np.eye(n, dtype=np.complex128)

    K_plus = K.copy()
    K_minus = K.copy()
    i, j = constraint_param_index // n, constraint_param_index % n
    K_plus[i, j] += eps
    K_minus[i, j] -= eps

    result_plus = crystallise(psi, params, K=K_plus, L=L)
    result_minus = crystallise(psi, params, K=K_minus, L=L)

    O_plus = observable_fn(result_plus.psi_star)
    O_minus = observable_fn(result_minus.psi_star)

    return float((O_plus - O_minus) / (2 * eps))


# ═══════════════════════════════════════════════════════════════════════
# Statistical comparison tools
# ═══════════════════════════════════════════════════════════════════════

def bootstrap_confidence_interval(
    samples: NDArray,
    fn: Callable[[NDArray], float],
    n_boot: int = 1000,
    alpha: float = 0.05,
    seed: int = 42,
) -> tuple[float, float, float]:
    """
    Bootstrap CI for a statistic fn applied to samples.

    Returns (point_estimate, lower_bound, upper_bound).
    """
    rng = np.random.default_rng(seed)
    point = fn(samples)
    boot_vals = np.zeros(n_boot)
    for i in range(n_boot):
        resample = rng.choice(samples, size=len(samples), replace=True)
        boot_vals[i] = fn(resample)
    lower = float(np.percentile(boot_vals, 100 * alpha / 2))
    upper = float(np.percentile(boot_vals, 100 * (1 - alpha / 2)))
    return float(point), lower, upper


def ks_compare(sample_a: NDArray, sample_b: NDArray) -> tuple[float, float]:
    """
    Two-sample Kolmogorov-Smirnov test.

    Returns (KS statistic, p-value).
    Used to compare transition-time distributions between models.
    """
    stat, pval = sp_stats.ks_2samp(sample_a, sample_b)
    return float(stat), float(pval)


def compare_model_predictions(
    observed: ExperimentResult,
    predicted: ExperimentResult,
) -> ComparisonResult:
    """
    Full statistical comparison between observed and predicted experiment results.
    """
    ks_stat, ks_pval = ks_compare(
        observed.transition_times, predicted.transition_times
    )

    entropy_obs = outcome_entropy(observed.outcomes)
    entropy_pred = outcome_entropy(predicted.outcomes)

    repeat_obs = repeatability_score(observed.outcomes)
    repeat_pred = repeatability_score(predicted.outcomes)

    # Trajectory divergence (average over paired trials if available)
    traj_div = None
    paired = min(len(observed.trials), len(predicted.trials))
    if paired > 0 and observed.trials[0].trajectory is not None and predicted.trials[0].trajectory is not None:
        divs = []
        for i in range(paired):
            if observed.trials[i].trajectory is not None and predicted.trials[i].trajectory is not None:
                divs.append(trajectory_distance(
                    observed.trials[i].trajectory,
                    predicted.trials[i].trajectory,
                ))
        if divs:
            traj_div = float(np.mean(divs))

    # Basin preference divergence (KL divergence)
    basin_div = None
    n_basins = max(observed.n_basins, predicted.n_basins)
    if n_basins > 0:
        bpi_obs = basin_preference_index(observed.outcomes, n_basins)
        bpi_pred = basin_preference_index(predicted.outcomes, n_basins)
        # Add small epsilon for numerical stability
        eps = 1e-10
        bpi_obs_safe = bpi_obs + eps
        bpi_pred_safe = bpi_pred + eps
        bpi_obs_safe /= bpi_obs_safe.sum()
        bpi_pred_safe /= bpi_pred_safe.sum()
        basin_div = float(np.sum(bpi_obs_safe * np.log(bpi_obs_safe / bpi_pred_safe)))

    return ComparisonResult(
        model_a=observed.model_label,
        model_b=predicted.model_label,
        ks_statistic=ks_stat,
        ks_pvalue=ks_pval,
        entropy_a=entropy_obs,
        entropy_b=entropy_pred,
        repeatability_a=repeat_obs,
        repeatability_b=repeat_pred,
        trajectory_divergence=traj_div,
        basin_preference_divergence=basin_div,
    )


def aic_score(log_likelihood: float, n_params: int) -> float:
    """Akaike Information Criterion: AIC = 2k - 2ln(L)."""
    return 2 * n_params - 2 * log_likelihood


def bic_score(log_likelihood: float, n_params: int, n_obs: int) -> float:
    """Bayesian Information Criterion: BIC = k*ln(n) - 2*ln(L)."""
    return n_params * np.log(n_obs) - 2 * log_likelihood


def permutation_test_repeatability(
    outcomes_a: NDArray,
    outcomes_b: NDArray,
    n_perm: int = 5000,
    seed: int = 42,
) -> tuple[float, float]:
    """
    Permutation test for difference in repeatability scores.

    Returns (observed_difference, p_value).
    """
    rng = np.random.default_rng(seed)
    obs_diff = repeatability_score(outcomes_a) - repeatability_score(outcomes_b)
    combined = np.concatenate([outcomes_a, outcomes_b])
    n_a = len(outcomes_a)
    count = 0
    for _ in range(n_perm):
        rng.shuffle(combined)
        perm_a = combined[:n_a]
        perm_b = combined[n_a:]
        perm_diff = repeatability_score(perm_a) - repeatability_score(perm_b)
        if abs(perm_diff) >= abs(obs_diff):
            count += 1
    pval = (count + 1) / (n_perm + 1)
    return float(obs_diff), float(pval)


# ═══════════════════════════════════════════════════════════════════════
# Model simulators (competing models)
# ═══════════════════════════════════════════════════════════════════════

def simulate_crystallisation_trials(
    psi_init: NDArray,
    n_trials: int,
    n_basins: int,
    basis: NDArray,
    params: Optional[CrystallisationParams] = None,
    K: Optional[NDArray] = None,
    L: Optional[NDArray] = None,
    noise_scale: float = 0.0,
    seed: int = 42,
    record_trajectories: bool = False,
) -> ExperimentResult:
    """
    Simulate repeated crystallisation from (optionally noisy) initial conditions.

    Args:
        psi_init: base initial state
        n_trials: number of repetitions
        n_basins: number of attractor basins (basis states)
        basis: (n_basins, n) array of basis/attractor states
        params: crystallisation parameters
        noise_scale: magnitude of per-trial noise on initial state
        seed: RNG seed
        record_trajectories: whether to store full trajectories
    """
    if params is None:
        params = CrystallisationParams(
            eta=0.003, max_steps=5000, tol=1e-8,
            record_trajectory=record_trajectories,
        )

    rng = np.random.default_rng(seed)
    trials = []

    for t in range(n_trials):
        psi = psi_init.copy()
        if noise_scale > 0:
            noise = rng.normal(scale=noise_scale, size=psi.shape) + \
                    1j * rng.normal(scale=noise_scale, size=psi.shape)
            psi = psi + noise

        result = crystallise(psi, params, K=K, L=L)

        # Assign to nearest basin
        overlaps = np.array([
            np.abs(np.vdot(basis[k], result.psi_star))**2
            for k in range(n_basins)
        ])
        outcome = int(np.argmax(overlaps))

        traj = None
        if result.psi_trajectory is not None:
            traj = np.array(result.psi_trajectory)

        trials.append(TrialResult(
            outcome_index=outcome,
            transition_time=float(result.steps),
            final_state=result.psi_star,
            trajectory=traj,
            F_trajectory=result.F_trajectory,
        ))

    return ExperimentResult(
        trials=trials,
        model_label="VFD_crystallisation",
        n_basins=n_basins,
    )


def simulate_stochastic_collapse_trials(
    psi_init: NDArray,
    n_trials: int,
    n_basins: int,
    basis: NDArray,
    noise_scale: float = 0.0,
    seed: int = 42,
) -> ExperimentResult:
    """
    Simulate GRW-style stochastic collapse: random eigenstate selection
    weighted by |c_k|^2 (Born rule).

    Transition time is drawn from an exponential distribution.
    """
    rng = np.random.default_rng(seed)
    trials = []

    for t in range(n_trials):
        psi = psi_init.copy()
        if noise_scale > 0:
            noise = rng.normal(scale=noise_scale, size=psi.shape) + \
                    1j * rng.normal(scale=noise_scale, size=psi.shape)
            psi = psi + noise

        # Born-rule probabilities
        overlaps = np.array([np.abs(np.vdot(basis[k], psi))**2 for k in range(n_basins)])
        probs = overlaps / overlaps.sum()
        outcome = int(rng.choice(n_basins, p=probs))

        # Exponential collapse time (GRW-style)
        tau = float(rng.exponential(scale=100.0))

        trials.append(TrialResult(
            outcome_index=outcome,
            transition_time=tau,
            final_state=basis[outcome].copy(),
            trajectory=None,
        ))

    return ExperimentResult(
        trials=trials,
        model_label="GRW_stochastic_collapse",
        n_basins=n_basins,
    )


def simulate_decoherence_trials(
    psi_init: NDArray,
    n_trials: int,
    n_basins: int,
    basis: NDArray,
    gamma_env: float = 0.05,
    dt: float = 0.1,
    max_steps: int = 500,
    noise_scale: float = 0.0,
    seed: int = 42,
) -> ExperimentResult:
    """
    Simulate standard decoherence: density matrix evolves under Lindblad-like
    dephasing until off-diagonal elements decay, then outcome sampled from
    diagonal (Born rule on decohered state).

    Simplified model: off-diagonals decay as exp(-gamma * t).
    """
    rng = np.random.default_rng(seed)
    n = len(psi_init)
    trials = []

    for t_idx in range(n_trials):
        psi = psi_init.copy()
        if noise_scale > 0:
            noise = rng.normal(scale=noise_scale, size=psi.shape) + \
                    1j * rng.normal(scale=noise_scale, size=psi.shape)
            psi = psi + noise

        # Build density matrix in basis representation
        c = np.array([np.vdot(basis[k], psi) for k in range(n_basins)])
        rho = np.outer(c, np.conj(c))

        # Dephase
        transition_time = max_steps
        for step in range(1, max_steps + 1):
            time = step * dt
            decay = np.exp(-gamma_env * time)
            rho_decohered = rho.copy()
            for i in range(n_basins):
                for j in range(n_basins):
                    if i != j:
                        rho_decohered[i, j] *= decay
            # Check if effectively decohered
            off_diag = np.sum(np.abs(rho_decohered) - np.diag(np.diag(np.abs(rho_decohered))))
            if off_diag < 1e-6:
                transition_time = step
                break

        # Sample from diagonal
        diag = np.real(np.diag(rho_decohered))
        diag = np.maximum(diag, 0)
        diag = diag / diag.sum()
        outcome = int(rng.choice(n_basins, p=diag))

        trials.append(TrialResult(
            outcome_index=outcome,
            transition_time=float(transition_time * dt),
            final_state=basis[outcome].copy(),
        ))

    return ExperimentResult(
        trials=trials,
        model_label="standard_decoherence",
        n_basins=n_basins,
    )


# ═══════════════════════════════════════════════════════════════════════
# Metastable plateau detection (SGT-5)
# ═══════════════════════════════════════════════════════════════════════

def detect_plateaus(
    F_trajectory: NDArray,
    window: int = 20,
    slope_threshold: float = 1e-5,
    min_duration: int = 10,
) -> list[tuple[int, int, float]]:
    """
    Detect metastable plateaus in F(t) trajectory.

    A plateau is a contiguous region where |dF/dt| < slope_threshold.

    Returns list of (start_idx, end_idx, plateau_F_value).
    """
    if len(F_trajectory) < window + 1:
        return []

    # Compute rolling slope magnitude
    slopes = np.zeros(len(F_trajectory) - window)
    for i in range(len(slopes)):
        segment = F_trajectory[i:i + window]
        slope = (segment[-1] - segment[0]) / window
        slopes[i] = abs(slope)

    # Find plateau regions
    is_plateau = slopes < slope_threshold
    plateaus = []
    start = None

    for i, p in enumerate(is_plateau):
        if p and start is None:
            start = i
        elif not p and start is not None:
            if i - start >= min_duration:
                plateau_val = float(np.mean(F_trajectory[start:i]))
                plateaus.append((start, i, plateau_val))
            start = None

    if start is not None and len(is_plateau) - start >= min_duration:
        plateau_val = float(np.mean(F_trajectory[start:len(is_plateau)]))
        plateaus.append((start, len(is_plateau), plateau_val))

    return plateaus


# ═══════════════════════════════════════════════════════════════════════
# Transition-time scaling analysis (SGT-3)
# ═══════════════════════════════════════════════════════════════════════

def transition_time_scaling(
    psi_init: NDArray,
    residual_multipliers: NDArray,
    params: Optional[CrystallisationParams] = None,
    K: Optional[NDArray] = None,
    L: Optional[NDArray] = None,
) -> tuple[NDArray, NDArray]:
    """
    Measure crystallisation time as constraint residual is scaled.

    tau_crys ~ 1 / (a*R + b*Q + c*B + d*Gamma)

    Returns (residual_values, transition_times).
    """
    if params is None:
        params = CrystallisationParams(eta=0.003, max_steps=8000, tol=1e-8)

    n = psi_init.shape[0]
    if K is None:
        K = np.eye(n, dtype=np.complex128)

    times = []
    residuals = []

    for mult in residual_multipliers:
        K_scaled = K * mult
        R_val = closure_residual(psi_init, K_scaled)
        result = crystallise(psi_init, params, K=K_scaled, L=L)
        times.append(result.steps)
        residuals.append(R_val)

    return np.array(residuals), np.array(times, dtype=float)
