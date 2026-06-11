"""VFD folding-rate corrections layered on flat ΛCDM.

Two falsifiable corrections are exposed:

VFD-A — log-periodic φ-rhythm
    H_VFD-A(z) = H_ΛCDM(z) · (1 + A · sin(2π · ln(1+z)/ln φ + θ))

VFD-B — seven-fold cascade with φ-spaced log-z centres
    H_VFD-B(z) = H_ΛCDM(z) · (1 + A · C7(z))
    C7(z) = Σ_k w_k · exp[ −(ln(1+z) − ln(1+z_k))² / (2 σ²) ]
    1+z_{k+1} = φ · (1+z_k)

If A = 0, both models collapse to the ΛCDM baseline exactly.
"""
from __future__ import annotations

from typing import Optional, Union

import numpy as np

from .constants import LN_PHI, OMEGA_M_FID, OMEGA_R_FID, PHI, H0_FID
from .lcdm import H_lcdm

ArrayLike = Union[float, np.ndarray]

# ---------------------------------------------------------------------------
# Model A — φ log-periodic correction
# ---------------------------------------------------------------------------


def phi_log_periodic_correction(z: ArrayLike, A: float, theta: float) -> ArrayLike:
    """Return the multiplicative correction A · sin(2π · ln(1+z)/ln φ + θ).

    Bounded by ±|A|.
    """
    z = np.asarray(z, dtype=float)
    phase = 2.0 * np.pi * np.log(1.0 + z) / LN_PHI + theta
    return A * np.sin(phase)


def H_vfd_phi_log(
    z: ArrayLike,
    H0: float = H0_FID,
    omega_m: float = OMEGA_M_FID,
    omega_r: float = OMEGA_R_FID,
    A: float = 0.0,
    theta: float = 0.0,
) -> ArrayLike:
    """VFD-A H(z) = H_ΛCDM · (1 + A sin(2π ln(1+z)/ln φ + θ))."""
    base = H_lcdm(z, H0=H0, omega_m=omega_m, omega_r=omega_r)
    return base * (1.0 + phi_log_periodic_correction(z, A, theta))


# ---------------------------------------------------------------------------
# Model B — seven-fold cascade
# ---------------------------------------------------------------------------


def seven_fold_centres(z0: float, n: int = 7) -> np.ndarray:
    """φ-spaced redshift centres: 1+z_{k+1} = φ · (1+z_k), starting at z0."""
    if z0 <= -1.0:
        raise ValueError("z0 must satisfy 1+z0 > 0")
    base = 1.0 + z0
    factors = PHI ** np.arange(n, dtype=float)
    return base * factors - 1.0


def seven_fold_cascade_correction(
    z: ArrayLike,
    A: float,
    z0: float,
    sigma: float,
    weights: Optional[np.ndarray] = None,
    n: int = 7,
) -> ArrayLike:
    """Sum of n φ-spaced log-z Gaussians, scaled by A."""
    if sigma <= 0.0:
        raise ValueError("sigma must be > 0")
    z = np.asarray(z, dtype=float)
    centres = seven_fold_centres(z0, n=n)
    if weights is None:
        w = np.ones(n, dtype=float) / n
    else:
        w = np.asarray(weights, dtype=float)
        if w.shape != (n,):
            raise ValueError("weights must have shape (n,)")
    log_one_plus_z = np.log(1.0 + z)
    log_one_plus_centres = np.log(1.0 + centres)
    delta = log_one_plus_z[..., None] - log_one_plus_centres[None, ...]
    g = np.exp(-0.5 * (delta / sigma) ** 2)
    cascade = (g * w[None, ...]).sum(axis=-1)
    return A * cascade


def H_vfd_seven_fold(
    z: ArrayLike,
    H0: float = H0_FID,
    omega_m: float = OMEGA_M_FID,
    omega_r: float = OMEGA_R_FID,
    A: float = 0.0,
    z0: float = 0.1,
    sigma: float = 0.5,
    weights: Optional[np.ndarray] = None,
    n: int = 7,
) -> ArrayLike:
    """VFD-B H(z) = H_ΛCDM · (1 + A · C_n(z))."""
    base = H_lcdm(z, H0=H0, omega_m=omega_m, omega_r=omega_r)
    correction = seven_fold_cascade_correction(z, A=A, z0=z0, sigma=sigma, weights=weights, n=n)
    return base * (1.0 + correction)
