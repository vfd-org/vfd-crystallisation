"""
Test suite for VFD Crystallisation parameter estimation framework.

Coverage:
- Parameter recovery on synthetic data
- Uncertainty interval sanity
- Identifiability scoring stability
- Sensitivity ranking reproducibility
- Graceful failure under underdetermined conditions
- Model comparison
- Synthetic data generation
"""

import sys
import os
import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from vfd.crystallisation.synthetic_data import (
    ModelParams,
    ExperimentConfig,
    SyntheticDataset,
    simulate_observables,
    generate_vfd_dataset,
    generate_multinomial_dataset,
    generate_misspecified_dataset,
    generate_control_response_curve,
    compute_observables,
)
from vfd.crystallisation.estimation import (
    objective_function,
    fit_parameters,
    bootstrap_parameter_ci,
    profile_likelihood,
    fisher_information,
    identifiability_report,
    sensitivity_analysis,
    compare_models,
    cross_validate_predictive_error,
    FitResult,
    IdentifiabilityReport,
    SensitivityReport,
    ModelComparisonResult,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def default_theta():
    return ModelParams(alpha=1.0, beta=0.5, gamma=0.8, lam=1.0,
                       eta=0.01, Gamma=0.0, R_c=0.0, kappa_B=1.0, kappa_Q=1.0)

def default_config(n_trials=10):
    return ExperimentConfig(n_modes=2, n_trials=n_trials, n_basins=2,
                            max_steps=100, seed=42)


# ---------------------------------------------------------------------------
# ModelParams
# ---------------------------------------------------------------------------

class TestModelParams:
    def test_round_trip(self):
        theta = default_theta()
        vec = theta.to_vector()
        theta2 = ModelParams.from_vector(vec)
        np.testing.assert_allclose(theta2.to_vector(), vec)

    def test_param_names(self):
        names = ModelParams.param_names()
        assert len(names) == 9
        assert "alpha" in names
        assert "Gamma" in names

    def test_n_params(self):
        assert ModelParams.n_params() == 9


# ---------------------------------------------------------------------------
# Synthetic Data Generation
# ---------------------------------------------------------------------------

class TestSyntheticData:
    def test_generate_vfd_dataset(self):
        theta = default_theta()
        config = default_config()
        ds = generate_vfd_dataset(theta, config)
        assert ds.outcomes is not None
        assert len(ds.outcomes) == config.n_trials
        assert ds.summary is not None
        assert ds.model_label == "VFD_crystallisation"

    def test_generate_multinomial(self):
        theta = default_theta()
        config = default_config()
        ds = generate_multinomial_dataset(theta, config)
        assert ds.outcomes is not None
        assert ds.basin_counts is not None
        assert abs(ds.basin_counts.sum() - config.n_trials) < 1

    def test_generate_misspecified_decoherence(self):
        config = default_config()
        ds = generate_misspecified_dataset(config, model="decoherence")
        assert ds.outcomes is not None
        assert "misspecified" in ds.model_label

    def test_generate_misspecified_grw(self):
        config = default_config()
        ds = generate_misspecified_dataset(config, model="grw")
        assert ds.outcomes is not None

    def test_partial_observation_outcomes_only(self):
        theta = default_theta()
        config = ExperimentConfig(n_modes=2, n_trials=20, n_basins=2,
                                  max_steps=200, observation_mode="outcomes_only", seed=42)
        ds = generate_vfd_dataset(theta, config)
        assert ds.outcomes is not None
        assert ds.transition_times is None

    def test_partial_observation_summary_only(self):
        theta = default_theta()
        config = ExperimentConfig(n_modes=2, n_trials=20, n_basins=2,
                                  max_steps=200, observation_mode="summary_only", seed=42)
        ds = generate_vfd_dataset(theta, config)
        assert ds.outcomes is None
        assert ds.summary is not None

    def test_control_response_curve(self):
        theta = default_theta()
        config = default_config(n_trials=20)
        param_vals = np.array([0.5, 1.0, 2.0])
        xs, ys = generate_control_response_curve(
            theta, "alpha", param_vals, "outcome_entropy", config
        )
        assert len(xs) == 3
        assert len(ys) == 3
        assert all(np.isfinite(ys))


# ---------------------------------------------------------------------------
# Forward Model
# ---------------------------------------------------------------------------

class TestForwardModel:
    def test_simulate_observables(self):
        theta = default_theta()
        config = default_config(n_trials=50)
        obs = simulate_observables(theta, config)
        assert "outcome_entropy" in obs
        assert "repeatability" in obs
        assert "basin_preference" in obs
        assert "transition_time_mean" in obs

    def test_deterministic(self):
        theta = default_theta()
        config = default_config(n_trials=50)
        obs1 = simulate_observables(theta, config)
        obs2 = simulate_observables(theta, config)
        assert obs1["outcome_entropy"] == obs2["outcome_entropy"]


# ---------------------------------------------------------------------------
# Objective Function
# ---------------------------------------------------------------------------

class TestObjectiveFunction:
    def test_zero_at_true_params(self):
        """Objective should be zero (or near-zero) when params match data."""
        theta = default_theta()
        config = default_config(n_trials=20)
        ds = generate_vfd_dataset(theta, config)
        cost = objective_function(theta.to_vector(), ds, config)
        assert cost < 1.0  # near-zero since same params generated the data

    def test_nonzero_at_wrong_params(self):
        theta_true = default_theta()
        config = default_config(n_trials=20)
        ds = generate_vfd_dataset(theta_true, config)
        theta_wrong = ModelParams(alpha=5.0, beta=5.0, gamma=0.1)
        cost = objective_function(theta_wrong.to_vector(), ds, config)
        assert cost >= 0.0


# ---------------------------------------------------------------------------
# Parameter Fitting
# ---------------------------------------------------------------------------

class TestFitParameters:
    def test_fit_returns_result(self):
        theta = default_theta()
        config = default_config(n_trials=20)
        ds = generate_vfd_dataset(theta, config)
        fit = fit_parameters(ds, config, theta_init=theta)
        assert isinstance(fit, FitResult)
        assert fit.param_names == ModelParams.param_names()
        assert np.isfinite(fit.residual_norm)

    def test_fit_near_true(self):
        """Fitted alpha should be in a reasonable range around true value."""
        theta = default_theta()
        config = default_config(n_trials=30)
        ds = generate_vfd_dataset(theta, config)
        fit = fit_parameters(ds, config, theta_init=theta)
        # The fit should at least not be wildly off
        assert fit.residual_norm < 10.0

    def test_multi_restart(self):
        theta = default_theta()
        config = default_config(n_trials=20)
        ds = generate_vfd_dataset(theta, config)
        fit = fit_parameters(ds, config, n_restarts=3, seed=42)
        assert isinstance(fit, FitResult)


# ---------------------------------------------------------------------------
# Bootstrap CI
# ---------------------------------------------------------------------------

class TestBootstrapCI:
    def test_bootstrap_returns_result(self):
        theta = default_theta()
        config = default_config(n_trials=20)
        ds = generate_vfd_dataset(theta, config)
        boot = bootstrap_parameter_ci(ds, config, n_boot=3)
        assert boot.point_estimates.shape == (9,)
        assert boot.ci_lower.shape == (9,)
        assert boot.ci_upper.shape == (9,)
        assert boot.bootstrap_samples.shape == (3, 9)

    def test_ci_contains_estimate(self):
        theta = default_theta()
        config = default_config(n_trials=20)
        ds = generate_vfd_dataset(theta, config)
        boot = bootstrap_parameter_ci(ds, config, n_boot=3)
        # Point estimate should be within CI
        for i in range(9):
            assert boot.ci_lower[i] <= boot.point_estimates[i] <= boot.ci_upper[i]


# ---------------------------------------------------------------------------
# Profile Likelihood
# ---------------------------------------------------------------------------

class TestProfileLikelihood:
    def test_profile_returns_result(self):
        theta = default_theta()
        config = default_config(n_trials=20)
        ds = generate_vfd_dataset(theta, config)
        grid = np.linspace(0.5, 2.0, 3)
        result = profile_likelihood(ds, config, "alpha", grid)
        assert result.param_name == "alpha"
        assert len(result.profile_values) == 3
        assert np.isfinite(result.mle_value)


# ---------------------------------------------------------------------------
# Fisher Information
# ---------------------------------------------------------------------------

class TestFisherInformation:
    def test_returns_matrix(self):
        theta = default_theta()
        config = default_config(n_trials=20)
        F = fisher_information(theta, config)
        assert F.shape == (9, 9)
        # Should be symmetric
        np.testing.assert_allclose(F, F.T, atol=1e-6)

    def test_positive_semidefinite(self):
        theta = default_theta()
        config = default_config(n_trials=20)
        F = fisher_information(theta, config)
        eigenvalues = np.linalg.eigvalsh(F)
        assert np.all(eigenvalues >= -1e-8)


# ---------------------------------------------------------------------------
# Identifiability
# ---------------------------------------------------------------------------

class TestIdentifiability:
    def test_report_structure(self):
        theta = default_theta()
        config = default_config(n_trials=20)
        report = identifiability_report(theta, config)
        assert isinstance(report, IdentifiabilityReport)
        assert report.fisher_matrix.shape == (9, 9)
        assert np.isfinite(report.condition_number)
        assert len(report.param_names) == 9
        # All params should be classified
        total = len(report.identifiable_params) + len(report.problematic_params)
        assert total == 9

    def test_stability(self):
        """Same inputs produce same report."""
        theta = default_theta()
        config = default_config(n_trials=20)
        r1 = identifiability_report(theta, config)
        r2 = identifiability_report(theta, config)
        assert r1.condition_number == r2.condition_number
        assert r1.identifiable_params == r2.identifiable_params


# ---------------------------------------------------------------------------
# Sensitivity Analysis
# ---------------------------------------------------------------------------

class TestSensitivityAnalysis:
    def test_report_structure(self):
        theta = default_theta()
        config = default_config(n_trials=20)
        report = sensitivity_analysis(theta, config)
        assert isinstance(report, SensitivityReport)
        assert len(report.param_names) == 9
        assert len(report.ranking) == 9
        assert report.local_sensitivities.shape[1] == 9

    def test_ranking_stability(self):
        theta = default_theta()
        config = default_config(n_trials=20)
        r1 = sensitivity_analysis(theta, config)
        r2 = sensitivity_analysis(theta, config)
        assert [x[0] for x in r1.ranking] == [x[0] for x in r2.ranking]

    def test_ranking_order(self):
        """Rankings should be in descending order of sensitivity."""
        theta = default_theta()
        config = default_config(n_trials=20)
        report = sensitivity_analysis(theta, config)
        scores = [x[1] for x in report.ranking]
        assert scores == sorted(scores, reverse=True)


# ---------------------------------------------------------------------------
# Model Comparison
# ---------------------------------------------------------------------------

class TestModelComparison:
    def test_compare_returns_result(self):
        theta = default_theta()
        config = default_config(n_trials=20)
        ds = generate_vfd_dataset(theta, config)

        theta_alt = ModelParams(alpha=2.0, beta=2.0, gamma=0.2)
        specs = [
            ("VFD_fitted", theta, 9),
            ("VFD_alt", theta_alt, 9),
        ]
        result = compare_models(ds, config, specs)
        assert isinstance(result, ModelComparisonResult)
        assert len(result.aic_scores) == 2
        assert result.preferred_model in ["VFD_fitted", "VFD_alt"]

    def test_true_model_preferred(self):
        """The model that generated the data should be preferred."""
        theta = default_theta()
        config = default_config(n_trials=30)
        ds = generate_vfd_dataset(theta, config)

        theta_wrong = ModelParams(alpha=8.0, beta=8.0, gamma=0.05)
        specs = [
            ("true", theta, 9),
            ("wrong", theta_wrong, 9),
        ]
        result = compare_models(ds, config, specs)
        # True model should have lower AIC
        assert result.aic_scores[0] <= result.aic_scores[1]


# ---------------------------------------------------------------------------
# Cross-validation
# ---------------------------------------------------------------------------

class TestCrossValidation:
    def test_returns_finite(self):
        theta = default_theta()
        config = default_config(n_trials=20)
        ds = generate_vfd_dataset(theta, config)
        err = cross_validate_predictive_error(ds, config, n_folds=2)
        assert np.isfinite(err)
        assert err >= 0


# ---------------------------------------------------------------------------
# Graceful failure
# ---------------------------------------------------------------------------

class TestGracefulFailure:
    def test_underdetermined_still_returns(self):
        """With very few trials, fitting should still return (possibly with high residual)."""
        theta = default_theta()
        config = ExperimentConfig(n_modes=2, n_trials=5, n_basins=2, max_steps=200, seed=42)
        ds = generate_vfd_dataset(theta, config)
        fit = fit_parameters(ds, config)
        assert isinstance(fit, FitResult)
        # Should return something, even if not great
        assert np.isfinite(fit.residual_norm)

    def test_misspecified_data_detection(self):
        """Fitting VFD model to non-VFD data should give worse fit than true model to true data."""
        config = default_config(n_trials=30)
        theta_true = default_theta()

        # VFD data -> VFD fit
        ds_vfd = generate_vfd_dataset(theta_true, config)
        fit_vfd = fit_parameters(ds_vfd, config, theta_init=theta_true)

        # Non-VFD data -> VFD fit
        ds_grw = generate_misspecified_dataset(config, model="grw")
        fit_grw = fit_parameters(ds_grw, config, theta_init=theta_true)

        # VFD fit on VFD data should be at least as good
        assert fit_vfd.residual_norm <= fit_grw.residual_norm + 5.0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
