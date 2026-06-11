import numpy as np

from src.constants import H0_FID, OMEGA_M_FID, OMEGA_R_FID
from src.lcdm import E_lcdm, H_lcdm, omega_lambda


def test_h0_at_z_zero():
    assert np.isclose(H_lcdm(0.0), H0_FID)


def test_E_at_z_zero():
    assert np.isclose(E_lcdm(0.0), 1.0)


def test_monotonic_increase():
    z = np.linspace(0.0, 5.0, 50)
    H = H_lcdm(z)
    diffs = np.diff(H)
    assert np.all(diffs > 0), "H(z) must be strictly increasing for standard ΛCDM"


def test_flatness_relation():
    omega_l = omega_lambda(OMEGA_M_FID, OMEGA_R_FID)
    assert np.isclose(omega_l + OMEGA_M_FID + OMEGA_R_FID, 1.0)
    assert 0.0 < omega_l < 1.0


def test_array_input_supported():
    z = np.array([0.1, 0.5, 1.0, 2.0])
    H = H_lcdm(z)
    assert H.shape == z.shape
    assert np.all(np.isfinite(H))
