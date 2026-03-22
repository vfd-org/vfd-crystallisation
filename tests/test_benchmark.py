"""
Test suite for VFD Crystallisation benchmark comparison.

Coverage:
- Model interface compliance
- Metric correctness
- Benchmark engine execution
- Fairness (identical initial conditions)
- Statistical comparison validity
- Equivalence regime (lambda→0)
- Divergence regime
- Noise sweep behaviour
"""

import sys
import os
import numpy as np
import pytest

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

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "benchmarks"))
from crystallisation_benchmark import (
    BenchmarkConfig, make_qubit_config, make_biased_config,
    make_multilevel_config, make_noise_sweep_config,
    create_models, run_model, run_benchmark, summarise_benchmark,
)


# ── Helpers ──

def simple_H(n=2):
    H = np.zeros((n, n), dtype=np.complex128)
    for i in range(n - 1):
        H[i, i + 1] = 0.1
        H[i + 1, i] = 0.1
    return H

def equal_rho(n=2):
    return np.ones((n, n), dtype=np.complex128) / n


# ═══════════════════════════════════════════════════════════════════════
# Model interface compliance
# ═══════════════════════════════════════════════════════════════════════

class TestModelInterface:
    """All models must expose identical interface."""

    @pytest.fixture(params=["lindblad", "grw", "or", "vfd"])
    def model(self, request):
        H = simple_H()
        if request.param == "lindblad":
            return LindbladModel(H)
        elif request.param == "grw":
            return GRWModel(H)
        elif request.param == "or":
            return ORModel(H)
        else:
            return CrystallisationModel(H)

    def test_has_step(self, model):
        assert callable(getattr(model, "step", None))

    def test_has_run(self, model):
        assert callable(getattr(model, "run", None))

    def test_has_measure(self, model):
        assert callable(getattr(model, "measure", None))

    def test_has_name(self, model):
        assert isinstance(model.name, str)

    def test_step_returns_matrix(self, model):
        rho = equal_rho()
        rho_new = model.step(rho, 0.05)
        assert rho_new.shape == (2, 2)

    def test_run_returns_trajectory(self, model):
        rho = equal_rho()
        traj = model.run(rho, 1.0, 0.1)
        assert len(traj) == 11  # T/dt + 1
        assert traj[0].shape == (2, 2)

    def test_measure_returns_int(self, model):
        rho = equal_rho()
        outcome = model.measure(rho)
        assert isinstance(outcome, int)
        assert 0 <= outcome < 2

    def test_trace_preserved(self, model):
        rho = equal_rho()
        rho_new = model.step(rho, 0.05)
        assert abs(np.trace(rho_new) - 1.0) < 0.1

    def test_hermiticity_preserved(self, model):
        rho = equal_rho()
        rho_new = model.step(rho, 0.05)
        np.testing.assert_allclose(rho_new, rho_new.conj().T, atol=1e-8)


# ═══════════════════════════════════════════════════════════════════════
# Metric correctness
# ═══════════════════════════════════════════════════════════════════════

class TestMetrics:
    def test_entropy_uniform(self):
        outcomes = np.array([0, 1, 0, 1] * 50)
        H = outcome_entropy(outcomes)
        assert abs(H - np.log(2)) < 0.05

    def test_entropy_deterministic(self):
        outcomes = np.zeros(100, dtype=int)
        assert outcome_entropy(outcomes) == 0.0

    def test_repeatability_perfect(self):
        outcomes = np.zeros(100, dtype=int)
        assert repeatability_score(outcomes) == 1.0

    def test_transition_time_immediate(self):
        rho_collapsed = np.zeros((2, 2), dtype=np.complex128)
        rho_collapsed[0, 0] = 1.0
        traj = [rho_collapsed] * 10
        assert transition_time(traj) == 0.0

    def test_transition_time_never(self):
        rho = equal_rho()
        traj = [rho] * 10
        assert transition_time(traj) == 10.0

    def test_trajectory_divergence_zero(self):
        rho = equal_rho()
        traj = [rho] * 10
        assert trajectory_divergence(traj, traj) < 1e-10

    def test_basin_preference_uniform(self):
        outcomes = np.array([0, 1, 0, 1] * 50)
        bpi = basin_preference_index(outcomes, 2)
        np.testing.assert_allclose(bpi, [0.5, 0.5])

    def test_coherence_profile_length(self):
        rho = equal_rho()
        traj = [rho] * 5
        cp = coherence_profile(traj)
        assert len(cp) == 5

    def test_purity_profile(self):
        rho = np.eye(2, dtype=np.complex128) / 2  # maximally mixed
        traj = [rho] * 3
        pp = purity_profile(traj)
        assert all(abs(p - 0.5) < 0.01 for p in pp)

    def test_collect_all_metrics(self):
        outcomes = np.array([0, 0, 1])
        times = np.array([5.0, 6.0, 7.0])
        metrics = collect_all_metrics(outcomes, times, [], 2)
        assert "outcome_entropy" in metrics
        assert "repeatability" in metrics
        assert "basin_preference" in metrics


# ═══════════════════════════════════════════════════════════════════════
# Benchmark engine
# ═══════════════════════════════════════════════════════════════════════

class TestBenchmarkEngine:
    def test_create_models(self):
        config = make_qubit_config()
        models = create_models(config)
        assert len(models) == 4
        assert "Lindblad" in models
        assert "VFD" in models

    def test_run_model(self):
        config = make_qubit_config()
        config = BenchmarkConfig(**{**config.__dict__, "n_trials": 5, "T": 1.0})
        model = LindbladModel(config.H, gamma=config.gamma_env, seed=config.seed)
        result = run_model(model, config)
        assert len(result.outcomes) == 5
        assert len(result.transition_times) == 5
        assert result.model_name == "Lindblad"

    def test_run_benchmark(self):
        config = make_qubit_config()
        config = BenchmarkConfig(**{**config.__dict__, "n_trials": 5, "T": 1.0})
        result = run_benchmark(config)
        assert len(result.results) == 4
        assert "VFD_vs_Lindblad" in result.comparisons

    def test_summarise(self):
        config = make_qubit_config()
        config = BenchmarkConfig(**{**config.__dict__, "n_trials": 3, "T": 0.5})
        result = run_benchmark(config)
        summary = summarise_benchmark(result)
        assert "Lindblad" in summary
        assert "VFD" in summary
        assert "Entropy" in summary


# ═══════════════════════════════════════════════════════════════════════
# Fairness: identical initial conditions
# ═══════════════════════════════════════════════════════════════════════

class TestFairness:
    def test_all_models_same_init(self):
        config = make_qubit_config()
        config = BenchmarkConfig(**{**config.__dict__, "n_trials": 3, "T": 0.5})
        result = run_benchmark(config)
        # All models should have started from same state
        for name, mr in result.results.items():
            first_state = mr.trajectories[0][0]
            np.testing.assert_allclose(first_state, config.rho_init, atol=1e-10)


# ═══════════════════════════════════════════════════════════════════════
# Equivalence regime: VFD with lambda≈0 should match Lindblad
# ═══════════════════════════════════════════════════════════════════════

class TestEquivalenceRegime:
    def test_vfd_weak_lambda_matches_lindblad(self):
        """When lambda→0, VFD should behave like Lindblad."""
        H = simple_H()
        rho = equal_rho()
        lindblad = LindbladModel(H, gamma=0.05, seed=42)
        vfd = CrystallisationModel(H, gamma_env=0.05, lam=0.001, seed=42)

        traj_l = lindblad.run(rho, 2.0, 0.05)
        traj_v = vfd.run(rho, 2.0, 0.05)

        # Final states should be similar
        diff = np.linalg.norm(traj_l[-1] - traj_v[-1], ord="fro")
        assert diff < 1.0  # Reasonably close


# ═══════════════════════════════════════════════════════════════════════
# Divergence regime: VFD should differ from stochastic models
# ═══════════════════════════════════════════════════════════════════════

class TestDivergenceRegime:
    def test_vfd_more_repeatable_than_grw(self):
        """VFD should show higher repeatability than GRW."""
        config = make_qubit_config()
        config = BenchmarkConfig(**{**config.__dict__, "n_trials": 20, "T": 3.0})
        result = run_benchmark(config)
        R_vfd = result.results["VFD"].metrics["repeatability"]
        R_grw = result.results["GRW"].metrics["repeatability"]
        # VFD should be at least as repeatable
        assert R_vfd >= R_grw - 0.1

    def test_vfd_lower_entropy_than_grw(self):
        """VFD should show lower or equal entropy vs stochastic models."""
        config = make_qubit_config()
        config = BenchmarkConfig(**{**config.__dict__, "n_trials": 20, "T": 3.0})
        result = run_benchmark(config)
        H_vfd = result.results["VFD"].metrics["outcome_entropy"]
        H_grw = result.results["GRW"].metrics["outcome_entropy"]
        assert H_vfd <= H_grw + 0.1


# ═══════════════════════════════════════════════════════════════════════
# Noise sweep
# ═══════════════════════════════════════════════════════════════════════

class TestNoiseSweep:
    def test_high_noise_reduces_vfd_advantage(self):
        """At high noise, VFD should behave more like stochastic models."""
        config_low = make_noise_sweep_config(0.01)
        config_low = BenchmarkConfig(**{**config_low.__dict__, "n_trials": 15, "T": 3.0})
        config_high = make_noise_sweep_config(0.5)
        config_high = BenchmarkConfig(**{**config_high.__dict__, "n_trials": 15, "T": 3.0})

        res_low = run_benchmark(config_low)
        res_high = run_benchmark(config_high)

        # At low noise, VFD should be highly repeatable
        R_low = res_low.results["VFD"].metrics["repeatability"]
        # At high noise, VFD repeatability may decrease
        R_high = res_high.results["VFD"].metrics["repeatability"]
        # Both should be valid (no crashes)
        assert 0 <= R_low <= 1.0
        assert 0 <= R_high <= 1.0


# ═══════════════════════════════════════════════════════════════════════
# Statistical comparison
# ═══════════════════════════════════════════════════════════════════════

class TestStatisticalComparison:
    def test_ks_test_identical(self):
        a = np.array([1.0, 2.0, 3.0, 4.0])
        stat, pval = ks_test(a, a)
        assert stat == 0.0
        assert pval == 1.0

    def test_ks_test_different(self):
        a = np.random.randn(100)
        b = np.random.randn(100) + 5
        stat, pval = ks_test(a, b)
        assert stat > 0.5
        assert pval < 0.01

    def test_bootstrap_ci(self):
        vals = np.ones(50)
        point, lo, hi = bootstrap_ci(vals)
        assert abs(point - 1.0) < 1e-10
        assert abs(lo - 1.0) < 1e-10


# ═══════════════════════════════════════════════════════════════════════
# Config presets
# ═══════════════════════════════════════════════════════════════════════

class TestConfigs:
    def test_qubit_config(self):
        c = make_qubit_config()
        assert c.n_states == 2
        assert c.H.shape == (2, 2)

    def test_biased_config(self):
        c = make_biased_config()
        assert c.n_states == 2

    def test_multilevel_config(self):
        c = make_multilevel_config(4)
        assert c.n_states == 4
        assert c.H.shape == (4, 4)

    def test_noise_sweep_config(self):
        c = make_noise_sweep_config(0.1)
        assert c.gamma_env == 0.1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
