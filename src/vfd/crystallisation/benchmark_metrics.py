"""
VFD Crystallisation — Benchmark Metrics
=========================================

Unified metrics applied identically across all models.

MET-1  Outcome entropy
MET-2  Repeatability
MET-3  Transition time
MET-4  Transition-time variance
MET-5  Trajectory divergence
MET-6  Basin preference index
MET-7  Coherence decay profile
"""

from __future__ import annotations
from typing import Optional
import numpy as np
from numpy.typing import NDArray
from scipy import stats as sp_stats


def outcome_entropy(outcomes: NDArray) -> float:
    """MET-1: H = -sum p_i log p_i."""
    _, counts = np.unique(outcomes, return_counts=True)
    probs = counts / counts.sum()
    probs = probs[probs > 0]
    return float(-np.sum(probs * np.log(probs)))


def repeatability_score(outcomes: NDArray) -> float:
    """MET-2: R = N_most_common / N_total."""
    _, counts = np.unique(outcomes, return_counts=True)
    return float(counts.max() / len(outcomes))


def transition_time(
    trajectory: list[NDArray],
    threshold: float = 0.95,
) -> float:
    """MET-3: Time step at which max diagonal element exceeds threshold."""
    for t, rho in enumerate(trajectory):
        diag = np.real(np.diag(rho))
        if diag.max() >= threshold:
            return float(t)
    return float(len(trajectory))


def transition_time_variance(times: NDArray) -> float:
    """MET-4: Variance of transition times across runs."""
    return float(np.var(times))


def trajectory_divergence(traj_a: list[NDArray], traj_b: list[NDArray]) -> float:
    """MET-5: D = integral ||X(t) - Y(t)|| dt (Frobenius norm)."""
    min_len = min(len(traj_a), len(traj_b))
    norms = []
    for t in range(min_len):
        diff = traj_a[t] - traj_b[t]
        norms.append(np.linalg.norm(diff, ord="fro"))
    return float(np.trapz(norms))


def basin_preference_index(outcomes: NDArray, n_basins: int) -> NDArray:
    """MET-6: BPI_k = N_k / N for each basin."""
    counts = np.zeros(n_basins)
    for o in outcomes:
        if 0 <= o < n_basins:
            counts[o] += 1
    total = len(outcomes)
    return counts / total if total > 0 else counts


def coherence_profile(trajectory: list[NDArray]) -> NDArray:
    """MET-7: Off-diagonal norm at each timestep."""
    profile = []
    for rho in trajectory:
        n = rho.shape[0]
        off_diag = 0.0
        for i in range(n):
            for j in range(n):
                if i != j:
                    off_diag += np.abs(rho[i, j])
        profile.append(off_diag)
    return np.array(profile)


def purity_profile(trajectory: list[NDArray]) -> NDArray:
    """Track Tr(rho^2) over time."""
    return np.array([float(np.real(np.trace(rho @ rho))) for rho in trajectory])


# ── Statistical comparison helpers ──

def bootstrap_ci(
    values: NDArray,
    fn=np.mean,
    n_boot: int = 1000,
    alpha: float = 0.05,
    seed: int = 42,
) -> tuple[float, float, float]:
    """Bootstrap confidence interval."""
    rng = np.random.default_rng(seed)
    point = float(fn(values))
    boots = np.array([fn(rng.choice(values, size=len(values), replace=True))
                      for _ in range(n_boot)])
    lo = float(np.percentile(boots, 100 * alpha / 2))
    hi = float(np.percentile(boots, 100 * (1 - alpha / 2)))
    return point, lo, hi


def ks_test(sample_a: NDArray, sample_b: NDArray) -> tuple[float, float]:
    """KS test between two distributions."""
    stat, pval = sp_stats.ks_2samp(sample_a, sample_b)
    return float(stat), float(pval)


def collect_all_metrics(
    outcomes: NDArray,
    transition_times: NDArray,
    trajectories: list[list[NDArray]],
    n_basins: int,
) -> dict:
    """Compute all metrics for a model's results."""
    return {
        "outcome_entropy": outcome_entropy(outcomes),
        "repeatability": repeatability_score(outcomes),
        "transition_time_mean": float(np.mean(transition_times)),
        "transition_time_std": float(np.std(transition_times)),
        "transition_time_variance": transition_time_variance(transition_times),
        "basin_preference": basin_preference_index(outcomes, n_basins),
        "n_trials": len(outcomes),
    }
