"""Information-criterion helpers for model comparison."""
from __future__ import annotations

from typing import Dict

import numpy as np


def reduced_chi_square(chi2: float, n_data: int, n_params: int) -> float:
    dof = n_data - n_params
    if dof <= 0:
        return float("nan")
    return float(chi2 / dof)


def aic(chi2: float, n_params: int) -> float:
    return float(chi2 + 2.0 * n_params)


def bic(chi2: float, n_params: int, n_data: int) -> float:
    return float(chi2 + n_params * np.log(n_data))


def delta_metric(candidate: float, baseline: float) -> float:
    """Return candidate − baseline.  Negative ⇒ candidate is preferred."""
    return float(candidate - baseline)


def metrics_row(name: str, chi2: float, n_params: int, n_data: int) -> Dict[str, float]:
    return {
        "model": name,
        "chi2": chi2,
        "n_params": n_params,
        "n_data": n_data,
        "chi2_red": reduced_chi_square(chi2, n_data, n_params),
        "aic": aic(chi2, n_params),
        "bic": bic(chi2, n_params, n_data),
    }
