"""
VFD Crystallisation — Parameter Estimation Framework
=====================================================

Implements:
    - Forward model generation
    - Parameter fitting (least-squares / likelihood-based)
    - Bootstrap uncertainty intervals
    - Profile likelihood
    - Fisher information matrix
    - Identifiability diagnostics
    - Sensitivity analysis / ranking
    - Model comparison (AIC/BIC, likelihood ratio, cross-validation)
"""

from __future__ import annotations

import dataclasses
import warnings
from typing import Callable, Optional, Literal

import numpy as np
from numpy.typing import NDArray
from scipy import optimize as sp_opt
from scipy import stats as sp_stats

from .synthetic_data import (
    ModelParams,
    ExperimentConfig,
    SyntheticDataset,
    simulate_observables,
)
from .falsifiability import (
    outcome_entropy,
    repeatability_score,
    basin_preference_index,
    aic_score,
    bic_score,
)


# ═══════════════════════════════════════════════════════════════════════
# Result containers
# ═══════════════════════════════════════════════════════════════════════

@dataclasses.dataclass(frozen=True)
class FitResult:
    """Result of parameter fitting."""
    theta_hat: ModelParams
    theta_vector: NDArray
    residual_norm: float
    success: bool
    message: str
    n_evaluations: int
    param_names: list


@dataclasses.dataclass(frozen=True)
class BootstrapResult:
    """Bootstrap confidence intervals."""
    point_estimates: NDArray          # (n_params,)
    ci_lower: NDArray                 # (n_params,)
    ci_upper: NDArray                 # (n_params,)
    bootstrap_samples: NDArray        # (n_boot, n_params)
    param_names: list


@dataclasses.dataclass(frozen=True)
class ProfileLikelihoodResult:
    """Profile likelihood for a single parameter."""
    param_name: str
    param_grid: NDArray
    profile_values: NDArray
    mle_value: float
    ci_lower: float
    ci_upper: float


@dataclasses.dataclass(frozen=True)
class IdentifiabilityReport:
    """Identifiability diagnostics."""
    fisher_matrix: NDArray
    condition_number: float
    correlation_matrix: NDArray
    eigenvalues: NDArray
    identifiable_params: list[str]
    problematic_params: list[str]
    param_names: list[str]


@dataclasses.dataclass(frozen=True)
class SensitivityReport:
    """Sensitivity analysis results."""
    local_sensitivities: NDArray       # (n_obs, n_params)
    normalised_sensitivities: NDArray  # (n_obs, n_params)
    observable_names: list[str]
    param_names: list[str]
    ranking: list[tuple[str, float]]   # param_name, total_sensitivity


@dataclasses.dataclass(frozen=True)
class ModelComparisonResult:
    """Model comparison output."""
    model_names: list[str]
    log_likelihoods: list[float]
    n_params: list[int]
    aic_scores: list[float]
    bic_scores: list[float]
    preferred_model: str
    preferred_by: str


# ═══════════════════════════════════════════════════════════════════════
# Objective function
# ═══════════════════════════════════════════════════════════════════════

_OBS_KEYS = [
    "outcome_entropy", "repeatability",
    "transition_time_mean", "transition_time_std",
]


def _obs_to_vector(obs: dict) -> NDArray:
    """Extract a stable vector of scalar observables from an obs dict."""
    vals = [obs.get(k, 0.0) for k in _OBS_KEYS]
    bpi = obs.get("basin_preference", np.array([]))
    vals.extend(bpi.tolist())
    return np.array(vals, dtype=float)


def objective_function(
    theta_vec: NDArray,
    data: SyntheticDataset,
    config: ExperimentConfig,
    psi_init: Optional[NDArray] = None,
    basis: Optional[NDArray] = None,
    weight_vector: Optional[NDArray] = None,
) -> float:
    """
    Weighted sum-of-squares between predicted and observed observables.

    This is the core loss function for parameter estimation.
    """
    theta = ModelParams.from_vector(theta_vec)
    predicted = simulate_observables(theta, config, psi_init, basis)
    observed = data.summary

    if observed is None:
        return np.inf

    pred_vec = _obs_to_vector(predicted)
    obs_vec = _obs_to_vector(observed)

    min_len = min(len(pred_vec), len(obs_vec))
    pred_vec = pred_vec[:min_len]
    obs_vec = obs_vec[:min_len]

    if weight_vector is None:
        weight_vector = np.ones(min_len)
    else:
        weight_vector = weight_vector[:min_len]

    residuals = (pred_vec - obs_vec) * weight_vector
    return float(np.sum(residuals ** 2))


# ═══════════════════════════════════════════════════════════════════════
# Parameter fitting
# ═══════════════════════════════════════════════════════════════════════

_DEFAULT_BOUNDS = [
    (0.01, 10.0),   # alpha
    (0.01, 10.0),   # beta
    (0.01, 10.0),   # gamma
    (0.01, 10.0),   # lam
    (0.0001, 0.1),  # eta
    (0.0, 5.0),     # Gamma
    (0.0, 5.0),     # R_c
    (0.1, 5.0),     # kappa_B
    (0.1, 5.0),     # kappa_Q
]


def fit_parameters(
    data: SyntheticDataset,
    config: ExperimentConfig,
    theta_init: Optional[ModelParams] = None,
    bounds: Optional[list[tuple[float, float]]] = None,
    psi_init: Optional[NDArray] = None,
    basis: Optional[NDArray] = None,
    n_restarts: int = 1,
    seed: int = 42,
) -> FitResult:
    """
    Fit model parameters to observed data via least-squares minimisation.

    Uses L-BFGS-B with optional multi-start.
    """
    if bounds is None:
        bounds = _DEFAULT_BOUNDS
    if theta_init is None:
        theta_init = ModelParams()

    rng = np.random.default_rng(seed)
    best_result = None
    best_cost = np.inf

    for restart in range(n_restarts):
        if restart == 0:
            x0 = theta_init.to_vector()
        else:
            x0 = np.array([
                rng.uniform(lo, hi) for lo, hi in bounds
            ])

        try:
            res = sp_opt.minimize(
                objective_function,
                x0,
                args=(data, config, psi_init, basis),
                method="L-BFGS-B",
                bounds=bounds,
                options={"maxiter": 50, "ftol": 1e-6},
            )
            if res.fun < best_cost:
                best_cost = res.fun
                best_result = res
        except Exception:
            continue

    if best_result is None:
        return FitResult(
            theta_hat=theta_init,
            theta_vector=theta_init.to_vector(),
            residual_norm=np.inf,
            success=False,
            message="All restarts failed",
            n_evaluations=0,
            param_names=ModelParams.param_names(),
        )

    theta_hat = ModelParams.from_vector(best_result.x)
    return FitResult(
        theta_hat=theta_hat,
        theta_vector=best_result.x,
        residual_norm=float(best_result.fun),
        success=bool(best_result.success),
        message=str(best_result.message),
        n_evaluations=int(best_result.nfev),
        param_names=ModelParams.param_names(),
    )


# ═══════════════════════════════════════════════════════════════════════
# Bootstrap uncertainty
# ═══════════════════════════════════════════════════════════════════════

def bootstrap_parameter_ci(
    data: SyntheticDataset,
    config: ExperimentConfig,
    n_boot: int = 100,
    alpha: float = 0.05,
    psi_init: Optional[NDArray] = None,
    basis: Optional[NDArray] = None,
    seed: int = 42,
) -> BootstrapResult:
    """
    Bootstrap confidence intervals on fitted parameters.

    Resamples trial-level data, refits, collects parameter distributions.
    """
    rng = np.random.default_rng(seed)
    n_params = ModelParams.n_params()
    boot_samples = np.zeros((n_boot, n_params))

    outcomes = data.outcomes
    times = data.transition_times

    for b in range(n_boot):
        # Resample trials
        idx = rng.choice(len(outcomes), size=len(outcomes), replace=True)
        resampled_outcomes = outcomes[idx]

        resampled_bpi = basin_preference_index(resampled_outcomes, config.n_basins)
        resampled_summary = dict(data.summary) if data.summary else {}
        resampled_summary["outcome_entropy"] = outcome_entropy(resampled_outcomes)
        resampled_summary["repeatability"] = repeatability_score(resampled_outcomes)
        resampled_summary["basin_preference"] = resampled_bpi

        if times is not None:
            resampled_times = times[idx]
            from .falsifiability import transition_time_stats
            t_stats = transition_time_stats(resampled_times)
            resampled_summary["transition_time_mean"] = t_stats["mean"]
            resampled_summary["transition_time_std"] = t_stats["std"]

        resampled_data = dataclasses.replace(
            data,
            outcomes=resampled_outcomes,
            transition_times=times[idx] if times is not None else None,
            summary=resampled_summary,
        )

        fit = fit_parameters(resampled_data, config, psi_init=psi_init, basis=basis)
        boot_samples[b] = fit.theta_vector

    point = np.median(boot_samples, axis=0)
    ci_lo = np.percentile(boot_samples, 100 * alpha / 2, axis=0)
    ci_hi = np.percentile(boot_samples, 100 * (1 - alpha / 2), axis=0)

    return BootstrapResult(
        point_estimates=point,
        ci_lower=ci_lo,
        ci_upper=ci_hi,
        bootstrap_samples=boot_samples,
        param_names=ModelParams.param_names(),
    )


# ═══════════════════════════════════════════════════════════════════════
# Profile likelihood
# ═══════════════════════════════════════════════════════════════════════

def profile_likelihood(
    data: SyntheticDataset,
    config: ExperimentConfig,
    param_name: str,
    grid: NDArray,
    psi_init: Optional[NDArray] = None,
    basis: Optional[NDArray] = None,
) -> ProfileLikelihoodResult:
    """
    Compute profile likelihood (actually profile loss) for one parameter.

    For each fixed value of param_name, optimise all other parameters.
    """
    param_idx = ModelParams.param_names().index(param_name)
    bounds = list(_DEFAULT_BOUNDS)
    profile_vals = np.zeros(len(grid))

    for i, val in enumerate(grid):
        # Fix the target parameter, free others
        fixed_bounds = list(bounds)
        fixed_bounds[param_idx] = (val, val)  # pin to grid value

        fit = fit_parameters(
            data, config, bounds=fixed_bounds,
            psi_init=psi_init, basis=basis,
        )
        profile_vals[i] = fit.residual_norm

    mle_idx = np.argmin(profile_vals)
    mle_val = float(grid[mle_idx])

    # Approximate CI from profile: where loss < min + chi2(1,0.95)/2
    threshold = profile_vals[mle_idx] + 1.92  # ~chi2(1, 0.95)/2
    within = grid[profile_vals < threshold]
    ci_lo = float(within[0]) if len(within) > 0 else float(grid[0])
    ci_hi = float(within[-1]) if len(within) > 0 else float(grid[-1])

    return ProfileLikelihoodResult(
        param_name=param_name,
        param_grid=grid,
        profile_values=profile_vals,
        mle_value=mle_val,
        ci_lower=ci_lo,
        ci_upper=ci_hi,
    )


# ═══════════════════════════════════════════════════════════════════════
# Fisher information and identifiability
# ═══════════════════════════════════════════════════════════════════════

def fisher_information(
    theta: ModelParams,
    config: ExperimentConfig,
    psi_init: Optional[NDArray] = None,
    basis: Optional[NDArray] = None,
    eps: float = 1e-4,
) -> NDArray:
    """
    Numerical Fisher information matrix via finite differences of observables.

    F_ij = sum_k (dO_k/dtheta_i)(dO_k/dtheta_j) / sigma_k^2

    Uses unit variance (sigma=1) as default weighting.
    """
    theta_vec = theta.to_vector()
    n_params = len(theta_vec)

    # Compute Jacobian of observables w.r.t. parameters
    obs_base = simulate_observables(theta, config, psi_init, basis)
    obs_vec_base = _obs_to_vector(obs_base)
    n_obs = len(obs_vec_base)

    J = np.zeros((n_obs, n_params))
    for j in range(n_params):
        theta_plus = theta_vec.copy()
        theta_minus = theta_vec.copy()
        theta_plus[j] += eps
        theta_minus[j] -= eps

        # Clip to bounds
        lo, hi = _DEFAULT_BOUNDS[j]
        theta_plus[j] = np.clip(theta_plus[j], lo, hi)
        theta_minus[j] = np.clip(theta_minus[j], lo, hi)
        actual_eps = theta_plus[j] - theta_minus[j]
        if abs(actual_eps) < 1e-12:
            continue

        obs_plus = simulate_observables(
            ModelParams.from_vector(theta_plus), config, psi_init, basis
        )
        obs_minus = simulate_observables(
            ModelParams.from_vector(theta_minus), config, psi_init, basis
        )
        vec_plus = _obs_to_vector(obs_plus)
        vec_minus = _obs_to_vector(obs_minus)

        min_len = min(len(vec_plus), len(vec_minus), n_obs)
        J[:min_len, j] = (vec_plus[:min_len] - vec_minus[:min_len]) / actual_eps

    # Fisher = J^T J (unit variance weighting)
    F = J.T @ J
    return F


def identifiability_report(
    theta: ModelParams,
    config: ExperimentConfig,
    psi_init: Optional[NDArray] = None,
    basis: Optional[NDArray] = None,
    condition_threshold: float = 1e6,
    correlation_threshold: float = 0.95,
) -> IdentifiabilityReport:
    """
    Full identifiability diagnostic.

    Computes Fisher matrix, condition number, correlation matrix,
    and flags problematic parameters.
    """
    F = fisher_information(theta, config, psi_init, basis)
    names = ModelParams.param_names()

    # Eigenvalues
    eigenvalues = np.linalg.eigvalsh(F)
    eigenvalues_safe = np.maximum(eigenvalues, 0)

    # Condition number
    eig_max = eigenvalues_safe.max() if eigenvalues_safe.max() > 0 else 1.0
    eig_min = eigenvalues_safe[eigenvalues_safe > 1e-15].min() if np.any(eigenvalues_safe > 1e-15) else 1e-15
    cond = float(eig_max / eig_min)

    # Correlation matrix from inverse Fisher (approximate covariance)
    diag = np.diag(F)
    diag_safe = np.where(diag > 1e-15, diag, 1e-15)
    D_inv = np.diag(1.0 / np.sqrt(diag_safe))
    corr = D_inv @ F @ D_inv

    # Flag problematic parameters
    identifiable = []
    problematic = []
    for i, name in enumerate(names):
        if diag[i] < 1e-10:
            problematic.append(name)
        else:
            # Check high correlation with others
            high_corr = False
            for j in range(len(names)):
                if i != j and abs(corr[i, j]) > correlation_threshold:
                    high_corr = True
                    break
            if high_corr:
                problematic.append(name)
            else:
                identifiable.append(name)

    return IdentifiabilityReport(
        fisher_matrix=F,
        condition_number=cond,
        correlation_matrix=corr,
        eigenvalues=eigenvalues,
        identifiable_params=identifiable,
        problematic_params=problematic,
        param_names=names,
    )


# ═══════════════════════════════════════════════════════════════════════
# Sensitivity analysis
# ═══════════════════════════════════════════════════════════════════════

def sensitivity_analysis(
    theta: ModelParams,
    config: ExperimentConfig,
    psi_init: Optional[NDArray] = None,
    basis: Optional[NDArray] = None,
    eps: float = 1e-4,
) -> SensitivityReport:
    """
    Local and normalised sensitivity of each observable to each parameter.

    SA-1: S_i = dO/dtheta_i
    SA-2: S_tilde_i = (theta_i / O) * dO/dtheta_i
    """
    theta_vec = theta.to_vector()
    n_params = len(theta_vec)
    names = ModelParams.param_names()

    obs_base = simulate_observables(theta, config, psi_init, basis)
    obs_vec_base = _obs_to_vector(obs_base)
    n_obs = len(obs_vec_base)
    obs_names = list(_OBS_KEYS) + [f"bpi_{i}" for i in range(n_obs - len(_OBS_KEYS))]

    local_sens = np.zeros((n_obs, n_params))
    norm_sens = np.zeros((n_obs, n_params))

    for j in range(n_params):
        theta_plus = theta_vec.copy()
        theta_minus = theta_vec.copy()
        theta_plus[j] += eps
        theta_minus[j] -= eps

        lo, hi = _DEFAULT_BOUNDS[j]
        theta_plus[j] = np.clip(theta_plus[j], lo, hi)
        theta_minus[j] = np.clip(theta_minus[j], lo, hi)
        actual_eps = theta_plus[j] - theta_minus[j]
        if abs(actual_eps) < 1e-12:
            continue

        obs_plus = _obs_to_vector(
            simulate_observables(ModelParams.from_vector(theta_plus), config, psi_init, basis)
        )
        obs_minus = _obs_to_vector(
            simulate_observables(ModelParams.from_vector(theta_minus), config, psi_init, basis)
        )

        min_len = min(len(obs_plus), len(obs_minus), n_obs)
        deriv = (obs_plus[:min_len] - obs_minus[:min_len]) / actual_eps
        local_sens[:min_len, j] = deriv

        # Normalised: (theta_j / O_k) * dO_k/dtheta_j
        for k in range(min_len):
            if abs(obs_vec_base[k]) > 1e-12:
                norm_sens[k, j] = theta_vec[j] / obs_vec_base[k] * deriv[k]

    # Ranking by total normalised sensitivity
    total_sens = np.sum(np.abs(norm_sens), axis=0)
    ranking = sorted(
        zip(names, total_sens.tolist()),
        key=lambda x: x[1],
        reverse=True,
    )

    return SensitivityReport(
        local_sensitivities=local_sens,
        normalised_sensitivities=norm_sens,
        observable_names=obs_names,
        param_names=names,
        ranking=ranking,
    )


# ═══════════════════════════════════════════════════════════════════════
# Model comparison
# ═══════════════════════════════════════════════════════════════════════

def _gaussian_log_likelihood(
    observed: NDArray,
    predicted: NDArray,
    sigma: float = 1.0,
) -> float:
    """Gaussian log-likelihood."""
    min_len = min(len(observed), len(predicted))
    residuals = observed[:min_len] - predicted[:min_len]
    return float(-0.5 * np.sum((residuals / sigma) ** 2) - min_len * np.log(sigma * np.sqrt(2 * np.pi)))


def compare_models(
    data: SyntheticDataset,
    config: ExperimentConfig,
    model_specs: list[tuple[str, ModelParams, int]],
    psi_init: Optional[NDArray] = None,
    basis: Optional[NDArray] = None,
) -> ModelComparisonResult:
    """
    Compare multiple fitted models via AIC/BIC.

    model_specs: list of (model_name, fitted_params, n_free_params)
    """
    obs_vec = _obs_to_vector(data.summary)
    n_obs = len(obs_vec)

    names = []
    log_liks = []
    n_params_list = []
    aic_list = []
    bic_list = []

    for name, params, n_free in model_specs:
        pred = simulate_observables(params, config, psi_init, basis)
        pred_vec = _obs_to_vector(pred)
        ll = _gaussian_log_likelihood(obs_vec, pred_vec)

        names.append(name)
        log_liks.append(ll)
        n_params_list.append(n_free)
        aic_list.append(aic_score(ll, n_free))
        bic_list.append(bic_score(ll, n_free, n_obs))

    best_aic_idx = int(np.argmin(aic_list))
    best_bic_idx = int(np.argmin(bic_list))

    if best_aic_idx == best_bic_idx:
        preferred = names[best_aic_idx]
        preferred_by = "AIC+BIC"
    else:
        preferred = names[best_bic_idx]
        preferred_by = f"BIC (AIC prefers {names[best_aic_idx]})"

    return ModelComparisonResult(
        model_names=names,
        log_likelihoods=log_liks,
        n_params=n_params_list,
        aic_scores=aic_list,
        bic_scores=bic_list,
        preferred_model=preferred,
        preferred_by=preferred_by,
    )


def cross_validate_predictive_error(
    data: SyntheticDataset,
    config: ExperimentConfig,
    n_folds: int = 5,
    psi_init: Optional[NDArray] = None,
    basis: Optional[NDArray] = None,
    seed: int = 42,
) -> float:
    """
    K-fold cross-validated prediction error.

    Splits trials, fits on training set, evaluates on holdout.
    Returns mean squared prediction error.
    """
    rng = np.random.default_rng(seed)
    n = len(data.outcomes)
    indices = np.arange(n)
    rng.shuffle(indices)
    folds = np.array_split(indices, n_folds)

    errors = []
    for fold_idx in range(n_folds):
        test_idx = folds[fold_idx]
        train_idx = np.concatenate([folds[j] for j in range(n_folds) if j != fold_idx])

        # Build train dataset
        train_outcomes = data.outcomes[train_idx]
        train_times = data.transition_times[train_idx] if data.transition_times is not None else None

        train_summary = {}
        train_summary["outcome_entropy"] = outcome_entropy(train_outcomes)
        train_summary["repeatability"] = repeatability_score(train_outcomes)
        train_summary["basin_preference"] = basin_preference_index(train_outcomes, config.n_basins)
        if train_times is not None:
            from .falsifiability import transition_time_stats
            t_stats = transition_time_stats(train_times)
            train_summary["transition_time_mean"] = t_stats["mean"]
            train_summary["transition_time_std"] = t_stats["std"]

        train_data = dataclasses.replace(data, outcomes=train_outcomes,
                                          transition_times=train_times,
                                          summary=train_summary)

        # Fit on training
        fit = fit_parameters(train_data, config, psi_init=psi_init, basis=basis)

        # Evaluate on test
        test_outcomes = data.outcomes[test_idx]
        test_times = data.transition_times[test_idx] if data.transition_times is not None else None
        test_summary = {}
        test_summary["outcome_entropy"] = outcome_entropy(test_outcomes)
        test_summary["repeatability"] = repeatability_score(test_outcomes)
        test_summary["basin_preference"] = basin_preference_index(test_outcomes, config.n_basins)
        if test_times is not None:
            from .falsifiability import transition_time_stats
            t_stats = transition_time_stats(test_times)
            test_summary["transition_time_mean"] = t_stats["mean"]
            test_summary["transition_time_std"] = t_stats["std"]

        pred = simulate_observables(fit.theta_hat, config, psi_init, basis)
        pred_vec = _obs_to_vector(pred)
        test_vec = _obs_to_vector(test_summary)

        min_len = min(len(pred_vec), len(test_vec))
        errors.append(float(np.mean((pred_vec[:min_len] - test_vec[:min_len])**2)))

    return float(np.mean(errors))
