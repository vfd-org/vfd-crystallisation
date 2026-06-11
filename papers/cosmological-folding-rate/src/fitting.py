"""Model fitting helpers built on scipy.optimize.

All fits minimise χ² = Σ_i ((H_obs_i − H_pred_i) / σ_i)² and return a
small dictionary with `params`, `cov`, `chi2`, `n_params`, `n_data`.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict, Sequence, Tuple

import numpy as np
from scipy.optimize import curve_fit

from .lcdm import H_lcdm
from .vfd_folding import H_vfd_phi_log, H_vfd_seven_fold


@dataclass
class FitResult:
    name: str
    params: Dict[str, float]
    cov: np.ndarray
    chi2: float
    n_params: int
    n_data: int

    def to_row(self) -> Dict[str, float]:
        row = {"model": self.name, "chi2": self.chi2, "n_params": self.n_params, "n_data": self.n_data}
        row.update(self.params)
        return row


def chi_square(H_obs: np.ndarray, H_pred: np.ndarray, sigma_H: np.ndarray) -> float:
    H_obs = np.asarray(H_obs, dtype=float)
    H_pred = np.asarray(H_pred, dtype=float)
    sigma_H = np.asarray(sigma_H, dtype=float)
    return float(np.sum(((H_obs - H_pred) / sigma_H) ** 2))


def residuals(H_obs: np.ndarray, H_pred: np.ndarray, sigma_H: np.ndarray) -> np.ndarray:
    return (np.asarray(H_obs) - np.asarray(H_pred)) / np.asarray(sigma_H)


def _bounds_array(bounds: Sequence[Tuple[float, float]]) -> Tuple[np.ndarray, np.ndarray]:
    lo = np.array([b[0] for b in bounds], dtype=float)
    hi = np.array([b[1] for b in bounds], dtype=float)
    return lo, hi


def fit_model(
    model_fn: Callable,
    z: np.ndarray,
    H_obs: np.ndarray,
    sigma_H: np.ndarray,
    p0: Sequence[float],
    bounds: Sequence[Tuple[float, float]],
    param_names: Sequence[str],
    name: str,
) -> FitResult:
    """Generic χ²-minimising fit through scipy curve_fit.

    `model_fn(z, *params)` must take z and the parameters in the order
    given by `param_names`.
    """
    z = np.asarray(z, dtype=float)
    H_obs = np.asarray(H_obs, dtype=float)
    sigma_H = np.asarray(sigma_H, dtype=float)
    lo, hi = _bounds_array(bounds)
    popt, pcov = curve_fit(
        model_fn,
        z,
        H_obs,
        p0=list(p0),
        sigma=sigma_H,
        absolute_sigma=True,
        bounds=(lo, hi),
        maxfev=20_000,
    )
    H_pred = model_fn(z, *popt)
    chi2 = chi_square(H_obs, H_pred, sigma_H)
    params = {n_: float(v) for n_, v in zip(param_names, popt)}
    return FitResult(
        name=name,
        params=params,
        cov=np.asarray(pcov, dtype=float),
        chi2=chi2,
        n_params=len(param_names),
        n_data=int(z.size),
    )


# ---------------------------------------------------------------------------
# Convenience adapters for the three models
# ---------------------------------------------------------------------------


def fit_lcdm(
    z: np.ndarray,
    H_obs: np.ndarray,
    sigma_H: np.ndarray,
    p0: Sequence[float] = (67.4, 0.315),
    bounds: Sequence[Tuple[float, float]] = ((50.0, 90.0), (0.05, 0.6)),
) -> FitResult:
    def model(zz, H0, omega_m):
        return H_lcdm(zz, H0=H0, omega_m=omega_m)

    return fit_model(model, z, H_obs, sigma_H, p0, bounds, ("H0", "omega_m"), "LCDM")


def fit_vfd_phi_log(
    z: np.ndarray,
    H_obs: np.ndarray,
    sigma_H: np.ndarray,
    p0: Sequence[float] = (67.4, 0.315, 0.0, 0.0),
    bounds: Sequence[Tuple[float, float]] = (
        (50.0, 90.0),
        (0.05, 0.6),
        (-0.1, 0.1),
        (0.0, 2.0 * np.pi),
    ),
) -> FitResult:
    def model(zz, H0, omega_m, A, theta):
        return H_vfd_phi_log(zz, H0=H0, omega_m=omega_m, A=A, theta=theta)

    return fit_model(model, z, H_obs, sigma_H, p0, bounds, ("H0", "omega_m", "A", "theta"), "VFD-A")


def fit_vfd_seven_fold(
    z: np.ndarray,
    H_obs: np.ndarray,
    sigma_H: np.ndarray,
    p0: Sequence[float] = (67.4, 0.315, 0.0, 0.1, 0.5),
    bounds: Sequence[Tuple[float, float]] = (
        (50.0, 90.0),
        (0.05, 0.6),
        (-0.5, 0.5),
        (-0.05, 0.5),  # z0 near low redshift; ladder runs upward
        (0.15, 1.5),   # σ regularised away from delta-function overfit
    ),
    multistart: bool = True,
) -> FitResult:
    """Fit VFD-B. The (z0, σ) landscape is multimodal, so by default we
    grid-search those two and refine the lowest-χ² seed."""

    def model(zz, H0, omega_m, A, z0, sigma):
        return H_vfd_seven_fold(zz, H0=H0, omega_m=omega_m, A=A, z0=z0, sigma=sigma)

    if not multistart:
        return fit_model(
            model,
            z,
            H_obs,
            sigma_H,
            p0,
            bounds,
            ("H0", "omega_m", "A", "z0", "sigma"),
            "VFD-B",
        )

    z0_seeds = np.linspace(bounds[3][0] + 1e-3, bounds[3][1] - 1e-3, 6)
    sigma_seeds = np.array([0.20, 0.35, 0.55, 0.85, 1.2])
    best: FitResult = None
    for z0_s in z0_seeds:
        for sig_s in sigma_seeds:
            seed = (p0[0], p0[1], 0.0, float(z0_s), float(sig_s))
            try:
                res = fit_model(
                    model,
                    z,
                    H_obs,
                    sigma_H,
                    seed,
                    bounds,
                    ("H0", "omega_m", "A", "z0", "sigma"),
                    "VFD-B",
                )
            except (RuntimeError, ValueError):
                continue
            if best is None or res.chi2 < best.chi2:
                best = res
    if best is None:
        raise RuntimeError("All VFD-B starts failed to converge")
    return best
