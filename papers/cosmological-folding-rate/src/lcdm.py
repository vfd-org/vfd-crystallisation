"""Flat ΛCDM expansion rate H(z).

H(z)^2 = H0^2 [Ω_m (1+z)^3 + Ω_r (1+z)^4 + Ω_Λ]

with Ω_Λ = 1 − Ω_m − Ω_r.
"""
from __future__ import annotations

from typing import Union

import numpy as np

from .constants import H0_FID, OMEGA_M_FID, OMEGA_R_FID

ArrayLike = Union[float, np.ndarray]


def omega_lambda(omega_m: float, omega_r: float = OMEGA_R_FID) -> float:
    """Flat-universe dark-energy density parameter."""
    return 1.0 - omega_m - omega_r


def E_lcdm(z: ArrayLike, omega_m: float = OMEGA_M_FID, omega_r: float = OMEGA_R_FID) -> ArrayLike:
    """Dimensionless expansion rate H(z) / H0 for flat ΛCDM."""
    z = np.asarray(z, dtype=float)
    one_plus_z = 1.0 + z
    om_l = omega_lambda(omega_m, omega_r)
    e2 = omega_m * one_plus_z**3 + omega_r * one_plus_z**4 + om_l
    return np.sqrt(e2)


def H_lcdm(
    z: ArrayLike,
    H0: float = H0_FID,
    omega_m: float = OMEGA_M_FID,
    omega_r: float = OMEGA_R_FID,
) -> ArrayLike:
    """Hubble rate H(z) for flat ΛCDM in km s⁻¹ Mpc⁻¹."""
    return H0 * E_lcdm(z, omega_m=omega_m, omega_r=omega_r)
