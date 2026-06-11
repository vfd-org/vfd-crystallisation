"""Physical and mathematical constants used throughout the module."""
from __future__ import annotations

import numpy as np

PHI: float = (1.0 + np.sqrt(5.0)) / 2.0
LN_PHI: float = float(np.log(PHI))

C_LIGHT: float = 299_792.458  # km/s

# Fiducial flat-ΛCDM parameters (Planck 2018 TT,TE,EE+lowE+lensing-ish defaults).
H0_FID: float = 67.4
OMEGA_M_FID: float = 0.315
OMEGA_R_FID: float = 9.0e-5
