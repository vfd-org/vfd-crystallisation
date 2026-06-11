"""Loaders for H(z) datasets and synthetic-data generation."""
from __future__ import annotations

import csv
import os
from typing import Optional, Tuple

import numpy as np

from .constants import H0_FID, OMEGA_M_FID, OMEGA_R_FID
from .lcdm import H_lcdm
from .vfd_folding import H_vfd_phi_log, H_vfd_seven_fold


def load_hz(path: str) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Load CSV with columns z,H,sigma_H,source.

    Returns (z, H, sigma_H, source).
    """
    z, H, sH, src = [], [], [], []
    with open(path, "r", newline="") as fh:
        reader = csv.DictReader(fh)
        required = {"z", "H", "sigma_H"}
        if not required.issubset(reader.fieldnames or set()):
            raise ValueError(f"{path} missing required columns z,H,sigma_H")
        for row in reader:
            z.append(float(row["z"]))
            H.append(float(row["H"]))
            sH.append(float(row["sigma_H"]))
            src.append(row.get("source", ""))
    return (
        np.array(z, dtype=float),
        np.array(H, dtype=float),
        np.array(sH, dtype=float),
        np.array(src, dtype=object),
    )


def write_hz(path: str, z, H, sigma_H, source) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["z", "H", "sigma_H", "source"])
        for zi, Hi, si, sr in zip(z, H, sigma_H, source):
            writer.writerow([f"{zi:.6f}", f"{Hi:.6f}", f"{si:.6f}", sr])


# ---------------------------------------------------------------------------
# Synthetic generators
# ---------------------------------------------------------------------------


def make_synthetic_lcdm(
    n: int = 40,
    z_min: float = 0.05,
    z_max: float = 2.0,
    sigma_frac: float = 0.05,
    H0: float = H0_FID,
    omega_m: float = OMEGA_M_FID,
    omega_r: float = OMEGA_R_FID,
    seed: Optional[int] = 42,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Generate a synthetic ΛCDM H(z) dataset with multiplicative noise."""
    rng = np.random.default_rng(seed)
    z = np.linspace(z_min, z_max, n)
    H_true = H_lcdm(z, H0=H0, omega_m=omega_m, omega_r=omega_r)
    sigma_H = sigma_frac * H_true
    noise = rng.normal(0.0, sigma_H)
    H_obs = H_true + noise
    src = np.array(["synthetic_lcdm"] * n, dtype=object)
    return z, H_obs, sigma_H, src


def make_synthetic_vfd_phi_log(
    n: int = 40,
    z_min: float = 0.05,
    z_max: float = 2.0,
    sigma_frac: float = 0.02,
    A: float = 0.04,
    theta: float = 0.5,
    H0: float = H0_FID,
    omega_m: float = OMEGA_M_FID,
    omega_r: float = OMEGA_R_FID,
    seed: Optional[int] = 7,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    z = np.linspace(z_min, z_max, n)
    H_true = H_vfd_phi_log(z, H0=H0, omega_m=omega_m, omega_r=omega_r, A=A, theta=theta)
    sigma_H = sigma_frac * H_true
    H_obs = H_true + rng.normal(0.0, sigma_H)
    src = np.array(["synthetic_vfdA"] * n, dtype=object)
    return z, H_obs, sigma_H, src


def make_synthetic_vfd_seven_fold(
    n: int = 60,
    z_min: float = 0.05,
    z_max: float = 3.5,
    sigma_frac: float = 0.02,
    A: float = 0.06,
    z0: float = 0.05,
    sigma: float = 0.4,
    H0: float = H0_FID,
    omega_m: float = OMEGA_M_FID,
    omega_r: float = OMEGA_R_FID,
    seed: Optional[int] = 11,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    z = np.linspace(z_min, z_max, n)
    H_true = H_vfd_seven_fold(
        z, H0=H0, omega_m=omega_m, omega_r=omega_r, A=A, z0=z0, sigma=sigma
    )
    sigma_H = sigma_frac * H_true
    H_obs = H_true + rng.normal(0.0, sigma_H)
    src = np.array(["synthetic_vfdB"] * n, dtype=object)
    return z, H_obs, sigma_H, src
