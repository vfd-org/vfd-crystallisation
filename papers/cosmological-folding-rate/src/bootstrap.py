"""Bootstrap-resample fits for parameter robustness."""
from __future__ import annotations

from typing import Callable, Dict, List

import numpy as np


def bootstrap_fit(
    fit_fn: Callable,
    z: np.ndarray,
    H_obs: np.ndarray,
    sigma_H: np.ndarray,
    n_boot: int = 500,
    seed: int = 0,
    track: tuple = ("A",),
) -> Dict[str, np.ndarray]:
    """Run `n_boot` resampled fits and return arrays of tracked parameters.

    Resampling is *with replacement* on the (z, H, σ_H) triples, which is
    the standard non-parametric bootstrap for an iid dataset.
    """
    rng = np.random.default_rng(seed)
    n = len(z)
    results: Dict[str, List[float]] = {p: [] for p in track}
    results["chi2"] = []
    failures = 0
    for _ in range(n_boot):
        idx = rng.integers(0, n, size=n)
        z_b = z[idx]
        H_b = H_obs[idx]
        s_b = sigma_H[idx]
        try:
            res = fit_fn(z_b, H_b, s_b)
        except Exception:
            failures += 1
            continue
        for p in track:
            if p in res.params:
                results[p].append(res.params[p])
        results["chi2"].append(res.chi2)
    out = {k: np.asarray(v, dtype=float) for k, v in results.items()}
    out["failures"] = np.array([failures])
    return out


def summarise(samples: np.ndarray) -> Dict[str, float]:
    if samples.size == 0:
        return {"mean": float("nan"), "std": float("nan"), "p16": float("nan"),
                "p50": float("nan"), "p84": float("nan"), "n": 0}
    return {
        "mean": float(np.mean(samples)),
        "std": float(np.std(samples, ddof=1) if samples.size > 1 else 0.0),
        "p16": float(np.percentile(samples, 16)),
        "p50": float(np.percentile(samples, 50)),
        "p84": float(np.percentile(samples, 84)),
        "n": int(samples.size),
    }
