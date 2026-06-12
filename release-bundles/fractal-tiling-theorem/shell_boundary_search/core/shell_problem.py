"""
General Shell-Boundary Search framework.

A shell-boundary problem is P = (X, T, h, B, Q):
  X  state space      T transformation      h: X -> R shell index
  B  positive form    Q capacity (containment - leakage)

The driver classifies the outcome of repeated T relative to the shell boundary
h -> infinity into:  CLOSED / CRITICAL / ESCAPING / WRONG_BOUNDARY / UNKNOWN.

HONEST GUARDRAIL (must stay attached): this is a REDUCTION/SEARCH method, not an
oracle. Failure to find a certificate may mean: the problem is open, the shell is
wrong, the certificate class is too weak, or no certificate exists in the chosen
formal system. It solves nothing automatically.
"""
import numpy as np


def classify_linear(T, eps=1e-6):
    """Shell = log-norm; drift sign from spectral radius. Reuses the certificate
    criteria (Lyapunov / invariant form) from closure_certificate_theory."""
    w = np.linalg.eigvals(np.asarray(T, float))
    rho = float(np.max(np.abs(w)))
    if rho < 1 - eps:
        return dict(rho=rho, outcome="CLOSED", mode="DISSIPATIVE",
                    certificate="Lyapunov form B (rho<1): inward shell drift")
    if rho > 1 + eps:
        return dict(rho=rho, outcome="ESCAPING", mode="NONE",
                    certificate="none: rho>1, orbits leave every magnitude shell")
    # rho == 1
    try:
        condV = float(np.linalg.cond(np.linalg.eig(np.asarray(T, float))[1]))
    except Exception:
        condV = np.inf
    if condV > 1e8:
        return dict(rho=rho, outcome="CRITICAL", mode="CRITICAL",
                    certificate="none (defective rho=1): polynomial shell growth")
    return dict(rho=rho, outcome="CLOSED", mode="ISOMETRIC",
                certificate="invariant inner product (rho=1, diagonalizable): bounded shells")


def capacity_outcome(Qbar, eps=1e-3):
    if Qbar > eps:
        return "CLOSED"
    if Qbar < -eps:
        return "ESCAPING"
    return "CRITICAL"
