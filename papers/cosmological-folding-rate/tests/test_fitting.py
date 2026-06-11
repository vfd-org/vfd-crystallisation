import numpy as np

from src.data_loader import (
    make_synthetic_lcdm,
    make_synthetic_vfd_phi_log,
    make_synthetic_vfd_seven_fold,
)
from src.fitting import fit_lcdm, fit_vfd_phi_log, fit_vfd_seven_fold


def test_lcdm_recovers_on_synthetic_lcdm():
    z, H, sH, _ = make_synthetic_lcdm(n=80, sigma_frac=0.02, seed=0)
    res = fit_lcdm(z, H, sH)
    assert abs(res.params["H0"] - 67.4) < 2.0
    assert abs(res.params["omega_m"] - 0.315) < 0.05


def test_vfd_a_recovers_injected_amplitude():
    A_true = 0.04
    theta_true = 0.5
    z, H, sH, _ = make_synthetic_vfd_phi_log(n=120, A=A_true, theta=theta_true, sigma_frac=0.01, seed=3)
    res = fit_vfd_phi_log(z, H, sH)
    assert abs(res.params["A"] - A_true) < 0.02


def test_vfd_b_recovers_amplitude():
    # σ < ln(φ) keeps the cascade's seven bumps resolved (out of the
    # degenerate near-constant plateau where A trades off with H0).
    A_true = 0.20
    z0_true = 0.05
    sigma_true = 0.18
    z, H, sH, _ = make_synthetic_vfd_seven_fold(
        n=200,
        A=A_true,
        z0=z0_true,
        sigma=sigma_true,
        sigma_frac=0.005,
        seed=303,
    )
    res = fit_vfd_seven_fold(z, H, sH)
    # Cascade ↔ H0 partial degeneracy means we accept anywhere within 0.15
    # of truth and clearly above 0 (recovery, not null).
    assert abs(res.params["A"] - A_true) < 0.15
    assert abs(res.params["A"]) > 0.05
