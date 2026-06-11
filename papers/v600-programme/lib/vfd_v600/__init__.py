"""vfd_v600 — shared verification library for the V_600 programme.

Modules:
    icosian   — exact Q(sqrt(5)) arithmetic + quaternion / vertex routines.
    group     — V_600 vertex set, T_τ-cycles, K-class structure, Dic_5 bulk.
    sigma     — σ-Galois twist, 24-cell as σ-fixed sublattice.
    tau_sigma — canonical involution τ_σ : V_600 → V_600 (loaded from data).
    operators — K-class projectors, identity-correction operators on cycle space.

Single source of truth for the five-paper programme. Every paper's
verify.py imports from here.
"""

from . import icosian, group, sigma, tau_sigma, operators, symmetry

__version__ = "1.0.0"
__all__ = ["icosian", "group", "sigma", "tau_sigma", "operators", "symmetry"]
