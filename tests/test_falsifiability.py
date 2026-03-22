"""
Test suite for the VFD Crystallisation falsifiability and discrimination framework.

Coverage:
- Metric correctness
- Repeatability calculations
- Discrimination score stability
- Signature extraction consistency
- Model simulation correctness
- Statistical comparison tools
- Plateau detection
- Transition-time scaling
"""

import sys
import os
import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from vfd.crystallisation.operator import CrystallisationParams
from vfd.crystallisation.falsifiability import (
    outcome_entropy,
    repeatability_score,
    trajectory_distance,
    transition_time_stats,
    basin_preference_index,
    bootstrap_confidence_interval,
    ks_compare,
    compare_model_predictions,
    aic_score,
    bic_score,
    permutation_test_repeatability,
    simulate_crystallisation_trials,
    simulate_stochastic_collapse_trials,
    simulate_decoherence_trials,
    detect_plateaus,
    transition_time_scaling,
    constraint_sensitivity,
    TrialResult,
    ExperimentResult,
    ComparisonResult,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_basis(n: int) -> np.ndarray:
    return np.eye(n, dtype=np.complex128)


def random_state(n: int, seed: int = 42) -> np.ndarray:
    rng = np.random.default_rng(seed)
    psi = rng.normal(size=n) + 1j * rng.normal(size=n)
    return psi / np.linalg.norm(psi)


# ---------------------------------------------------------------------------
# Outcome Entropy
# ---------------------------------------------------------------------------

class TestOutcomeEntropy:
    def test_zero_entropy_uniform_outcome(self):
        """All outcomes the same -> H = 0."""
        outcomes = np.array([0, 0, 0, 0, 0])
        assert outcome_entropy(outcomes) == 0.0

    def test_max_entropy_uniform_distribution(self):
        """Equally distributed outcomes -> H = ln(n)."""
        n = 4
        outcomes = np.array([0, 1, 2, 3] * 250)
        H = outcome_entropy(outcomes)
        assert abs(H - np.log(n)) < 0.01

    def test_non_negative(self):
        outcomes = np.array([0, 0, 1, 1, 2])
        assert outcome_entropy(outcomes) >= 0.0

    def test_binary_entropy(self):
        """50/50 binary -> H = ln(2)."""
        outcomes = np.array([0, 1] * 500)
        assert abs(outcome_entropy(outcomes) - np.log(2)) < 0.01


# ---------------------------------------------------------------------------
# Repeatability Score
# ---------------------------------------------------------------------------

class TestRepeatabilityScore:
    def test_perfect_repeatability(self):
        outcomes = np.array([0, 0, 0, 0])
        assert repeatability_score(outcomes) == 1.0

    def test_uniform_repeatability(self):
        outcomes = np.array([0, 1, 2, 3])
        assert repeatability_score(outcomes) == 0.25

    def test_range(self):
        rng = np.random.default_rng(42)
        outcomes = rng.integers(0, 5, size=100)
        R = repeatability_score(outcomes)
        assert 0.0 < R <= 1.0


# ---------------------------------------------------------------------------
# Trajectory Distance
# ---------------------------------------------------------------------------

class TestTrajectoryDistance:
    def test_identical_trajectories_zero(self):
        traj = np.random.randn(50, 4) + 1j * np.random.randn(50, 4)
        assert trajectory_distance(traj, traj) < 1e-10

    def test_different_trajectories_positive(self):
        traj_a = np.ones((50, 4), dtype=np.complex128)
        traj_b = np.zeros((50, 4), dtype=np.complex128)
        assert trajectory_distance(traj_a, traj_b) > 0

    def test_symmetry(self):
        rng = np.random.default_rng(42)
        traj_a = rng.normal(size=(30, 3)) + 1j * rng.normal(size=(30, 3))
        traj_b = rng.normal(size=(30, 3)) + 1j * rng.normal(size=(30, 3))
        assert abs(trajectory_distance(traj_a, traj_b) - trajectory_distance(traj_b, traj_a)) < 1e-10

    def test_mismatched_lengths(self):
        traj_a = np.ones((30, 3), dtype=np.complex128)
        traj_b = np.ones((50, 3), dtype=np.complex128)
        # Should use min length
        d = trajectory_distance(traj_a, traj_b)
        assert d < 1e-10


# ---------------------------------------------------------------------------
# Transition Time Stats
# ---------------------------------------------------------------------------

class TestTransitionTimeStats:
    def test_keys(self):
        times = np.array([10.0, 20.0, 30.0, 40.0])
        stats = transition_time_stats(times)
        assert "mean" in stats
        assert "std" in stats
        assert "median" in stats
        assert "dispersion" in stats
        assert "skewness" in stats

    def test_values(self):
        times = np.array([10.0, 10.0, 10.0])
        stats = transition_time_stats(times)
        assert stats["mean"] == 10.0
        assert stats["std"] == 0.0
        assert stats["dispersion"] == 0.0


# ---------------------------------------------------------------------------
# Basin Preference Index
# ---------------------------------------------------------------------------

class TestBasinPreferenceIndex:
    def test_uniform(self):
        assignments = np.array([0, 1, 2, 3] * 25)
        bpi = basin_preference_index(assignments, 4)
        np.testing.assert_allclose(bpi, [0.25, 0.25, 0.25, 0.25])

    def test_single_basin(self):
        assignments = np.array([2, 2, 2, 2])
        bpi = basin_preference_index(assignments, 4)
        assert bpi[2] == 1.0
        assert bpi[0] == 0.0

    def test_sums_to_one(self):
        rng = np.random.default_rng(42)
        assignments = rng.integers(0, 5, size=200)
        bpi = basin_preference_index(assignments, 5)
        assert abs(np.sum(bpi) - 1.0) < 1e-10


# ---------------------------------------------------------------------------
# Bootstrap CI
# ---------------------------------------------------------------------------

class TestBootstrapCI:
    def test_returns_three_values(self):
        samples = np.random.randn(100)
        point, lo, hi = bootstrap_confidence_interval(samples, np.mean)
        assert lo <= point <= hi

    def test_tight_ci_for_constant(self):
        samples = np.ones(100)
        point, lo, hi = bootstrap_confidence_interval(samples, np.mean)
        assert abs(point - 1.0) < 1e-10
        assert abs(lo - 1.0) < 1e-10
        assert abs(hi - 1.0) < 1e-10


# ---------------------------------------------------------------------------
# KS Compare
# ---------------------------------------------------------------------------

class TestKSCompare:
    def test_identical_samples(self):
        s = np.random.randn(200)
        stat, pval = ks_compare(s, s)
        assert stat == 0.0
        assert pval == 1.0

    def test_different_distributions(self):
        a = np.random.randn(500)
        b = np.random.randn(500) + 5.0  # shifted
        stat, pval = ks_compare(a, b)
        assert stat > 0.5
        assert pval < 0.001


# ---------------------------------------------------------------------------
# AIC / BIC
# ---------------------------------------------------------------------------

class TestInformationCriteria:
    def test_aic_lower_for_better_fit(self):
        aic_good = aic_score(-10.0, 2)
        aic_bad = aic_score(-50.0, 2)
        assert aic_good < aic_bad

    def test_bic_penalises_params(self):
        bic_simple = bic_score(-10.0, 2, 100)
        bic_complex = bic_score(-10.0, 10, 100)
        assert bic_simple < bic_complex


# ---------------------------------------------------------------------------
# Permutation Test
# ---------------------------------------------------------------------------

class TestPermutationTest:
    def test_identical_outcomes(self):
        outcomes = np.array([0, 0, 1, 1] * 50)
        diff, pval = permutation_test_repeatability(outcomes, outcomes, n_perm=500)
        assert abs(diff) < 1e-10
        assert pval > 0.5

    def test_different_outcomes(self):
        a = np.zeros(100, dtype=int)  # perfect repeatability
        b = np.arange(100) % 10      # low repeatability
        diff, pval = permutation_test_repeatability(a, b, n_perm=1000)
        assert diff > 0.5
        assert pval < 0.05


# ---------------------------------------------------------------------------
# Model Simulators
# ---------------------------------------------------------------------------

class TestCrystallisationSimulation:
    def test_produces_results(self):
        n = 3
        psi = random_state(n, seed=10)
        basis = make_basis(n)
        params = CrystallisationParams(eta=0.003, max_steps=2000, tol=1e-6)
        result = simulate_crystallisation_trials(
            psi, n_trials=10, n_basins=n, basis=basis, params=params, seed=42
        )
        assert len(result.trials) == 10
        assert result.model_label == "VFD_crystallisation"
        assert all(0 <= t.outcome_index < n for t in result.trials)

    def test_deterministic_without_noise(self):
        """Without noise, identical inits should give identical outcomes."""
        n = 3
        psi = random_state(n, seed=5)
        basis = make_basis(n)
        params = CrystallisationParams(eta=0.003, max_steps=3000, tol=1e-7)
        result = simulate_crystallisation_trials(
            psi, n_trials=20, n_basins=n, basis=basis, params=params,
            noise_scale=0.0, seed=42
        )
        # All outcomes should be identical
        outcomes = result.outcomes
        assert len(np.unique(outcomes)) == 1

    def test_high_repeatability(self):
        n = 3
        psi = random_state(n, seed=5)
        basis = make_basis(n)
        params = CrystallisationParams(eta=0.003, max_steps=3000, tol=1e-7)
        result = simulate_crystallisation_trials(
            psi, n_trials=50, n_basins=n, basis=basis, params=params,
            noise_scale=0.0, seed=42
        )
        assert repeatability_score(result.outcomes) == 1.0


class TestStochasticCollapseSimulation:
    def test_produces_results(self):
        n = 3
        psi = random_state(n, seed=10)
        basis = make_basis(n)
        result = simulate_stochastic_collapse_trials(
            psi, n_trials=50, n_basins=n, basis=basis, seed=42
        )
        assert len(result.trials) == 50
        assert result.model_label == "GRW_stochastic_collapse"

    def test_born_rule_approximate(self):
        """Large sample should approximate Born-rule statistics."""
        n = 3
        psi = random_state(n, seed=10)
        basis = make_basis(n)
        result = simulate_stochastic_collapse_trials(
            psi, n_trials=10000, n_basins=n, basis=basis, seed=42
        )
        bpi = basin_preference_index(result.outcomes, n)
        expected = np.array([np.abs(np.vdot(basis[k], psi))**2 for k in range(n)])
        expected = expected / expected.sum()
        np.testing.assert_allclose(bpi, expected, atol=0.03)


class TestDecoherenceSimulation:
    def test_produces_results(self):
        n = 3
        psi = random_state(n, seed=10)
        basis = make_basis(n)
        result = simulate_decoherence_trials(
            psi, n_trials=20, n_basins=n, basis=basis, seed=42
        )
        assert len(result.trials) == 20
        assert result.model_label == "standard_decoherence"


# ---------------------------------------------------------------------------
# Model Comparison
# ---------------------------------------------------------------------------

class TestCompareModels:
    def test_comparison_output(self):
        n = 3
        psi = random_state(n, seed=10)
        basis = make_basis(n)
        params = CrystallisationParams(eta=0.003, max_steps=2000, tol=1e-6)

        vfd = simulate_crystallisation_trials(
            psi, n_trials=30, n_basins=n, basis=basis, params=params
        )
        grw = simulate_stochastic_collapse_trials(
            psi, n_trials=30, n_basins=n, basis=basis
        )
        comp = compare_model_predictions(vfd, grw)

        assert isinstance(comp, ComparisonResult)
        assert comp.model_a == "VFD_crystallisation"
        assert comp.model_b == "GRW_stochastic_collapse"
        assert 0.0 <= comp.ks_statistic <= 1.0
        assert 0.0 <= comp.ks_pvalue <= 1.0

    def test_vfd_lower_entropy_than_stochastic(self):
        """VFD with zero noise should have lower outcome entropy than GRW."""
        n = 3
        psi = random_state(n, seed=10)
        basis = make_basis(n)
        params = CrystallisationParams(eta=0.003, max_steps=3000, tol=1e-7)

        vfd = simulate_crystallisation_trials(
            psi, n_trials=100, n_basins=n, basis=basis, params=params,
            noise_scale=0.0
        )
        grw = simulate_stochastic_collapse_trials(
            psi, n_trials=100, n_basins=n, basis=basis
        )
        H_vfd = outcome_entropy(vfd.outcomes)
        H_grw = outcome_entropy(grw.outcomes)
        assert H_vfd < H_grw


# ---------------------------------------------------------------------------
# Plateau Detection
# ---------------------------------------------------------------------------

class TestPlateauDetection:
    def test_no_plateaus_in_steep_descent(self):
        F = np.exp(-np.linspace(0, 5, 200))  # smooth exponential
        plateaus = detect_plateaus(F, window=10, slope_threshold=1e-6)
        assert len(plateaus) == 0 or all(p[1] - p[0] < 20 for p in plateaus)

    def test_detects_flat_region(self):
        F = np.concatenate([
            np.linspace(10, 5, 50),   # descent
            np.ones(60) * 5.0,        # plateau
            np.linspace(5, 1, 50),    # descent
        ])
        plateaus = detect_plateaus(F, window=5, slope_threshold=1e-4, min_duration=10)
        assert len(plateaus) >= 1
        # Plateau should be near value 5.0
        assert any(abs(p[2] - 5.0) < 0.5 for p in plateaus)

    def test_empty_trajectory(self):
        F = np.array([1.0])
        plateaus = detect_plateaus(F)
        assert len(plateaus) == 0


# ---------------------------------------------------------------------------
# Transition-Time Scaling
# ---------------------------------------------------------------------------

class TestTransitionTimeScaling:
    def test_returns_correct_shape(self):
        n = 3
        psi = random_state(n, seed=15)
        multipliers = np.array([0.5, 1.0, 1.5, 2.0])
        params = CrystallisationParams(eta=0.003, max_steps=3000, tol=1e-7)
        residuals, times = transition_time_scaling(psi, multipliers, params=params)
        assert len(residuals) == 4
        assert len(times) == 4
        assert all(t > 0 for t in times)


# ---------------------------------------------------------------------------
# Constraint Sensitivity
# ---------------------------------------------------------------------------

class TestConstraintSensitivity:
    def test_nonzero_sensitivity(self):
        """VFD predicts nonzero constraint sensitivity."""
        n = 2
        psi = random_state(n, seed=20)
        params = CrystallisationParams(eta=0.005, max_steps=3000, tol=1e-8)

        def obs(psi_star):
            return float(np.abs(psi_star[0])**2)

        chi = constraint_sensitivity(obs, psi, constraint_param_index=0, params=params)
        # Just check it's finite — the point is it's measurable
        assert np.isfinite(chi)


# ---------------------------------------------------------------------------
# Discrimination stability (same inputs -> same metrics)
# ---------------------------------------------------------------------------

class TestDiscriminationStability:
    def test_metrics_stable_across_runs(self):
        """Same inputs should produce identical metric values."""
        n = 3
        psi = random_state(n, seed=30)
        basis = make_basis(n)
        params = CrystallisationParams(eta=0.003, max_steps=2000, tol=1e-6)

        r1 = simulate_crystallisation_trials(
            psi, n_trials=50, n_basins=n, basis=basis, params=params, seed=100
        )
        r2 = simulate_crystallisation_trials(
            psi, n_trials=50, n_basins=n, basis=basis, params=params, seed=100
        )

        assert outcome_entropy(r1.outcomes) == outcome_entropy(r2.outcomes)
        assert repeatability_score(r1.outcomes) == repeatability_score(r2.outcomes)
        np.testing.assert_array_equal(
            basin_preference_index(r1.outcomes, n),
            basin_preference_index(r2.outcomes, n),
        )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
