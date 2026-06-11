"""Plotting helpers — figures land in `results/figures/`."""
from __future__ import annotations

import os
from typing import Dict, Iterable, Optional

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from .constants import LN_PHI, OMEGA_M_FID, OMEGA_R_FID
from .lcdm import H_lcdm
from .vfd_folding import H_vfd_phi_log, H_vfd_seven_fold, seven_fold_centres


def _ensure(path: str) -> str:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return path


def plot_hz_with_fit(
    z: np.ndarray,
    H_obs: np.ndarray,
    sigma_H: np.ndarray,
    fit_params: Dict[str, float],
    model: str,
    out_path: str,
    title: Optional[str] = None,
) -> str:
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.errorbar(z, H_obs, yerr=sigma_H, fmt="o", ms=3, color="black", label="data")
    z_dense = np.linspace(min(z.min(), 0.0), z.max() * 1.02, 400)
    if model == "LCDM":
        H_fit = H_lcdm(z_dense, H0=fit_params["H0"], omega_m=fit_params["omega_m"])
    elif model == "VFD-A":
        H_fit = H_vfd_phi_log(
            z_dense,
            H0=fit_params["H0"],
            omega_m=fit_params["omega_m"],
            A=fit_params["A"],
            theta=fit_params["theta"],
        )
    elif model == "VFD-B":
        H_fit = H_vfd_seven_fold(
            z_dense,
            H0=fit_params["H0"],
            omega_m=fit_params["omega_m"],
            A=fit_params["A"],
            z0=fit_params["z0"],
            sigma=fit_params["sigma"],
        )
    else:
        raise ValueError(model)
    ax.plot(z_dense, H_fit, "-", color="C0", label=f"{model} fit")
    if model == "VFD-B":
        centres = seven_fold_centres(fit_params["z0"], n=7)
        for c in centres:
            ax.axvline(c, color="C3", lw=0.6, alpha=0.5)
    ax.set_xlabel("z")
    ax.set_ylabel(r"$H(z)\ [\mathrm{km\,s^{-1}\,Mpc^{-1}}]$")
    ax.set_title(title or f"H(z) data vs {model}")
    ax.legend()
    fig.tight_layout()
    fig.savefig(_ensure(out_path), dpi=150)
    plt.close(fig)
    return out_path


def plot_residuals(
    z: np.ndarray,
    H_obs: np.ndarray,
    sigma_H: np.ndarray,
    H_pred: np.ndarray,
    out_path: str,
    title: Optional[str] = None,
) -> str:
    fig, ax = plt.subplots(figsize=(7, 4.0))
    res = (H_obs - H_pred) / sigma_H
    ax.errorbar(z, res, yerr=np.ones_like(res), fmt="o", ms=3, color="black")
    ax.axhline(0, color="C0", lw=1.0)
    ax.set_xlabel("z")
    ax.set_ylabel(r"$(H_{\rm obs}-H_{\rm fit})/\sigma_H$")
    ax.set_title(title or "Residuals (in σ units)")
    fig.tight_layout()
    fig.savefig(_ensure(out_path), dpi=150)
    plt.close(fig)
    return out_path


def plot_log_phi_residuals(
    z: np.ndarray,
    H_obs: np.ndarray,
    sigma_H: np.ndarray,
    H_pred_lcdm: np.ndarray,
    out_path: str,
    title: Optional[str] = None,
) -> str:
    fig, ax = plt.subplots(figsize=(7, 4.0))
    x = np.log(1.0 + z) / LN_PHI
    res = (H_obs - H_pred_lcdm) / sigma_H
    ax.errorbar(x, res, yerr=np.ones_like(res), fmt="o", ms=3, color="black")
    ax.axhline(0, color="C0", lw=1.0)
    ax.set_xlabel(r"$\ln(1+z)/\ln\varphi$")
    ax.set_ylabel(r"$(H_{\rm obs}-H_{\rm \Lambda CDM})/\sigma_H$")
    ax.set_title(title or "ΛCDM residuals on φ-log axis")
    fig.tight_layout()
    fig.savefig(_ensure(out_path), dpi=150)
    plt.close(fig)
    return out_path


def plot_information_criteria(
    rows: Iterable[Dict[str, float]],
    out_path: str,
    title: Optional[str] = None,
) -> str:
    rows = list(rows)
    names = [r["model"] for r in rows]
    aic_vals = np.array([r["aic"] for r in rows], dtype=float)
    bic_vals = np.array([r["bic"] for r in rows], dtype=float)
    aic_d = aic_vals - aic_vals.min()
    bic_d = bic_vals - bic_vals.min()
    x = np.arange(len(names))
    w = 0.4
    fig, ax = plt.subplots(figsize=(7, 4.0))
    ax.bar(x - w / 2, aic_d, width=w, color="C0", label="ΔAIC")
    ax.bar(x + w / 2, bic_d, width=w, color="C3", label="ΔBIC")
    ax.set_xticks(x)
    ax.set_xticklabels(names)
    ax.set_ylabel("Δ vs best (lower is better)")
    ax.set_title(title or "Model comparison")
    ax.legend()
    fig.tight_layout()
    fig.savefig(_ensure(out_path), dpi=150)
    plt.close(fig)
    return out_path
