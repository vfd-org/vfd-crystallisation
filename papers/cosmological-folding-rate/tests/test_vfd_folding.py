import numpy as np
import pytest

from src.constants import PHI
from src.lcdm import H_lcdm
from src.vfd_folding import (
    H_vfd_phi_log,
    H_vfd_seven_fold,
    phi_log_periodic_correction,
    seven_fold_cascade_correction,
    seven_fold_centres,
)


# --------- VFD-A ---------


def test_vfd_phi_log_collapses_to_lcdm_when_A_zero():
    z = np.linspace(0.0, 3.0, 25)
    assert np.allclose(H_vfd_phi_log(z, A=0.0, theta=1.234), H_lcdm(z))


def test_vfd_phi_log_correction_bounded():
    z = np.linspace(0.0, 4.0, 200)
    A = 0.07
    theta = 0.3
    corr = phi_log_periodic_correction(z, A=A, theta=theta)
    assert np.all(corr <= A + 1e-12)
    assert np.all(corr >= -A - 1e-12)


def test_vfd_phi_log_array_and_scalar():
    val = phi_log_periodic_correction(0.5, A=0.05, theta=0.0)
    assert np.isfinite(val)
    arr = phi_log_periodic_correction(np.array([0.1, 0.5]), A=0.05, theta=0.0)
    assert arr.shape == (2,)


# --------- VFD-B ---------


def test_seven_fold_centres_phi_spaced():
    z0 = 0.1
    centres = seven_fold_centres(z0, n=7)
    assert centres.shape == (7,)
    ratios = (1.0 + centres[1:]) / (1.0 + centres[:-1])
    assert np.allclose(ratios, PHI)


def test_seven_fold_centres_starts_at_z0():
    centres = seven_fold_centres(0.07, n=7)
    assert np.isclose(centres[0], 0.07)


def test_vfd_seven_fold_collapses_to_lcdm_when_A_zero():
    z = np.linspace(0.0, 3.0, 30)
    assert np.allclose(H_vfd_seven_fold(z, A=0.0), H_lcdm(z))


def test_vfd_seven_fold_finite():
    z = np.linspace(0.0, 5.0, 200)
    H = H_vfd_seven_fold(z, A=0.1, z0=0.05, sigma=0.4)
    assert np.all(np.isfinite(H))


def test_seven_fold_invalid_sigma():
    with pytest.raises(ValueError):
        seven_fold_cascade_correction(np.array([0.1]), A=0.1, z0=0.0, sigma=-1.0)


def test_seven_fold_weights_shape_check():
    with pytest.raises(ValueError):
        seven_fold_cascade_correction(
            np.array([0.1, 0.5]), A=0.1, z0=0.05, sigma=0.5, weights=np.ones(3)
        )
