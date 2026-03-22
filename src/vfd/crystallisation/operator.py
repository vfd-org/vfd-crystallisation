"""
VFD Crystallisation Operator
=============================

Implements the crystallisation operator C that maps an unresolved field
configuration Psi on manifold M to a stable coherent configuration Psi*
by constrained minimisation of a closure functional:

    C[Psi] = Psi*  where  Psi* = argmin_{Phi in A} F[Phi]

    F[Phi] = alpha * R[Phi] + beta * E[Phi] - gamma * Q[Phi]

with stability satisfying:

    grad_Phi F[Psi*] = 0,   delta^2 F[Psi*] > 0

R = closure residual (constraint mismatch)
E = energy functional (energetic cost)
Q = coherence metric (phase alignment / symmetry satisfaction)
"""

from __future__ import annotations

import dataclasses
from typing import Optional

import numpy as np
from numpy.typing import NDArray


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

@dataclasses.dataclass(frozen=True)
class CrystallisationParams:
    """Weights and hyperparameters for the crystallisation functional."""
    alpha: float = 1.0    # closure residual weight
    beta: float = 1.0     # energy weight
    gamma: float = 1.0    # coherence weight (subtracted — higher Q is better)
    eta: float = 0.01     # gradient descent step size
    max_steps: int = 5000
    tol: float = 1e-10    # convergence tolerance on |grad F|
    record_trajectory: bool = False


@dataclasses.dataclass(frozen=True)
class CrystallisationResult:
    """Output of the crystallisation operator."""
    psi_star: NDArray[np.complexfloating]   # crystallised state
    F_final: float                           # final functional value
    steps: int                               # iterations taken
    converged: bool
    F_trajectory: Optional[NDArray[np.floating]] = None  # F(t) if recorded
    psi_trajectory: Optional[list[NDArray]] = None


# ---------------------------------------------------------------------------
# Constraint / target matrix — defaults
# ---------------------------------------------------------------------------

def _default_constraint_target(n: int) -> NDArray:
    """Default admissible closure target K = identity (all constraints met)."""
    return np.eye(n, dtype=np.complex128)


def _default_laplacian(n: int) -> NDArray:
    """1-D discrete Laplacian as default coupling matrix L."""
    L = np.zeros((n, n), dtype=np.complex128)
    for i in range(n):
        L[i, i] = 2.0
        if i > 0:
            L[i, i - 1] = -1.0
        if i < n - 1:
            L[i, i + 1] = -1.0
    return L


# ---------------------------------------------------------------------------
# Core functionals
# ---------------------------------------------------------------------------

def closure_residual(
    psi: NDArray,
    K: Optional[NDArray] = None,
) -> float:
    """
    R[Psi] = || G[Psi] - K ||^2

    G[Psi] is taken as the outer product |psi><psi| (density-matrix-like
    constraint projection).  K is the admissible closure target.
    """
    n = psi.shape[0]
    if K is None:
        K = _default_constraint_target(n)
    G = np.outer(psi, np.conj(psi))
    diff = G - K
    return float(np.real(np.trace(diff @ diff.conj().T)))


def energy_functional(
    psi: NDArray,
    L: Optional[NDArray] = None,
) -> float:
    """
    E[Psi] = <Psi| L |Psi>

    L is a coupling / Laplacian / Hamiltonian-proxy matrix.
    """
    n = psi.shape[0]
    if L is None:
        L = _default_laplacian(n)
    return float(np.real(np.conj(psi) @ L @ psi))


def coherence_metric(psi: NDArray) -> float:
    """
    Q[Psi] = sum_{i,j} cos(theta_i - theta_j)

    Measures global phase alignment across components.
    Normalised to [0, 1] by dividing by n^2.
    """
    phases = np.angle(psi)
    n = len(phases)
    # Pairwise cosine of phase differences (vectorised)
    diff = phases[:, None] - phases[None, :]
    return float(np.sum(np.cos(diff)) / (n * n))


def crystallisation_functional(
    psi: NDArray,
    params: Optional[CrystallisationParams] = None,
    K: Optional[NDArray] = None,
    L: Optional[NDArray] = None,
) -> float:
    """
    F[Psi] = alpha * R[Psi] + beta * E[Psi] - gamma * Q[Psi]
    """
    if params is None:
        params = CrystallisationParams()
    R = closure_residual(psi, K)
    E = energy_functional(psi, L)
    Q = coherence_metric(psi)
    return params.alpha * R + params.beta * E - params.gamma * Q


# ---------------------------------------------------------------------------
# Gradient computation (numerical, central differences)
# ---------------------------------------------------------------------------

def _numerical_gradient(
    psi: NDArray,
    params: CrystallisationParams,
    K: Optional[NDArray],
    L: Optional[NDArray],
    eps: float = 1e-7,
) -> NDArray:
    """Numerical gradient of F w.r.t. real and imaginary parts of psi."""
    grad = np.zeros_like(psi)
    for i in range(len(psi)):
        # Real part
        psi_p = psi.copy(); psi_p[i] += eps
        psi_m = psi.copy(); psi_m[i] -= eps
        dF_real = (
            crystallisation_functional(psi_p, params, K, L)
            - crystallisation_functional(psi_m, params, K, L)
        ) / (2 * eps)

        # Imaginary part
        psi_p = psi.copy(); psi_p[i] += 1j * eps
        psi_m = psi.copy(); psi_m[i] -= 1j * eps
        dF_imag = (
            crystallisation_functional(psi_p, params, K, L)
            - crystallisation_functional(psi_m, params, K, L)
        ) / (2 * eps)

        grad[i] = dF_real + 1j * dF_imag
    return grad


# ---------------------------------------------------------------------------
# Crystallisation operator  C[Psi] -> Psi*
# ---------------------------------------------------------------------------

def crystallise(
    psi_init: NDArray,
    params: Optional[CrystallisationParams] = None,
    K: Optional[NDArray] = None,
    L: Optional[NDArray] = None,
) -> CrystallisationResult:
    """
    C[Psi] = argmin_Phi F[Phi]

    Gradient descent on the crystallisation functional.
    Returns the crystallised state and diagnostic information.
    """
    if params is None:
        params = CrystallisationParams()

    psi = psi_init.astype(np.complex128).copy()
    F_history = [] if params.record_trajectory else None
    psi_history = [] if params.record_trajectory else None

    converged = False
    step = 0

    for step in range(1, params.max_steps + 1):
        F_val = crystallisation_functional(psi, params, K, L)
        if params.record_trajectory:
            F_history.append(F_val)
            psi_history.append(psi.copy())

        grad = _numerical_gradient(psi, params, K, L)
        grad_norm = float(np.linalg.norm(grad))

        if grad_norm < params.tol:
            converged = True
            break

        psi = psi - params.eta * grad

    F_final = crystallisation_functional(psi, params, K, L)
    if params.record_trajectory:
        F_history.append(F_final)
        psi_history.append(psi.copy())

    return CrystallisationResult(
        psi_star=psi,
        F_final=F_final,
        steps=step,
        converged=converged,
        F_trajectory=np.array(F_history) if F_history is not None else None,
        psi_trajectory=psi_history,
    )


# ---------------------------------------------------------------------------
# Dynamical flow  dPsi/dt = -grad F[Psi]
# ---------------------------------------------------------------------------

def crystallisation_flow(
    psi_init: NDArray,
    dt: float = 0.001,
    num_steps: int = 2000,
    params: Optional[CrystallisationParams] = None,
    K: Optional[NDArray] = None,
    L: Optional[NDArray] = None,
) -> tuple[NDArray, NDArray, NDArray]:
    """
    Integrate dPsi/dt = -grad_Psi F[Psi] via forward Euler.

    Returns:
        psi_final: final state
        F_t: array of F values at each timestep
        psi_t: list of states at each timestep
    """
    if params is None:
        params = CrystallisationParams()

    psi = psi_init.astype(np.complex128).copy()
    F_t = np.zeros(num_steps + 1)
    psi_t = np.zeros((num_steps + 1, len(psi)), dtype=np.complex128)

    F_t[0] = crystallisation_functional(psi, params, K, L)
    psi_t[0] = psi.copy()

    for t in range(1, num_steps + 1):
        grad = _numerical_gradient(psi, params, K, L)
        psi = psi - dt * grad
        F_t[t] = crystallisation_functional(psi, params, K, L)
        psi_t[t] = psi.copy()

    return psi, F_t, psi_t


# ---------------------------------------------------------------------------
# Spectral formulation
# ---------------------------------------------------------------------------

def spectral_reweight(
    c: NDArray,
    R: NDArray,
    E: NDArray,
    Q: NDArray,
    mu: float = 1.0,
    nu: float = 1.0,
    rho: float = 1.0,
) -> NDArray:
    """
    Spectral crystallisation: reweight mode coefficients.

    c_tilde_i = c_i * exp(-mu*R_i - nu*E_i + rho*Q_i) / Z

    Modes with poor closure get suppressed; modes with high coherence
    get amplified. The result is the coherent crystal that survives
    the constraint filter.
    """
    log_weights = -mu * R - nu * E + rho * Q
    # Numerical stability: shift by max
    log_weights = log_weights - np.max(log_weights)
    weights = np.exp(log_weights)
    c_tilde = c * weights
    Z = np.sum(np.abs(c_tilde))
    if Z < 1e-30:
        return c_tilde
    return c_tilde / Z


# ---------------------------------------------------------------------------
# Crystallisation timescale
# ---------------------------------------------------------------------------

def crystallisation_timescale(
    psi: NDArray,
    a: float = 1.0,
    b: float = 1.0,
    c: float = 1.0,
    K: Optional[NDArray] = None,
    L: Optional[NDArray] = None,
    params: Optional[CrystallisationParams] = None,
) -> float:
    """
    tau_crys = 1 / Omega[Psi]

    Omega[Psi] = a*R[Psi] + b*Q[Psi] + c*|grad V(Psi)|

    Higher mismatch or stronger coherence gradient -> faster crystallisation.
    """
    if params is None:
        params = CrystallisationParams()
    R = closure_residual(psi, K)
    Q = coherence_metric(psi)
    grad = _numerical_gradient(psi, params, K, L)
    grad_norm = float(np.linalg.norm(grad))
    omega = a * R + b * Q + c * grad_norm
    if omega < 1e-30:
        return float("inf")
    return 1.0 / omega


# ---------------------------------------------------------------------------
# Hessian check (stability verification)
# ---------------------------------------------------------------------------

def hessian_check(
    psi: NDArray,
    params: Optional[CrystallisationParams] = None,
    K: Optional[NDArray] = None,
    L: Optional[NDArray] = None,
    eps: float = 1e-5,
) -> tuple[bool, NDArray]:
    """
    Check delta^2 F[Psi*] > 0 (positive definite Hessian).

    Uses numerical second derivatives on real-parameterised F.
    Returns (is_stable, eigenvalues_of_hessian).
    """
    if params is None:
        params = CrystallisationParams()

    # Flatten to real parameters: [Re(psi), Im(psi)]
    n = len(psi)
    dim = 2 * n

    def _to_complex(x: NDArray) -> NDArray:
        return x[:n] + 1j * x[n:]

    def _F_real(x: NDArray) -> float:
        return crystallisation_functional(_to_complex(x), params, K, L)

    x0 = np.concatenate([np.real(psi), np.imag(psi)])
    H = np.zeros((dim, dim))

    for i in range(dim):
        for j in range(i, dim):
            x_pp = x0.copy(); x_pp[i] += eps; x_pp[j] += eps
            x_pm = x0.copy(); x_pm[i] += eps; x_pm[j] -= eps
            x_mp = x0.copy(); x_mp[i] -= eps; x_mp[j] += eps
            x_mm = x0.copy(); x_mm[i] -= eps; x_mm[j] -= eps
            H[i, j] = (_F_real(x_pp) - _F_real(x_pm) - _F_real(x_mp) + _F_real(x_mm)) / (4 * eps * eps)
            H[j, i] = H[i, j]

    eigenvalues = np.linalg.eigvalsh(H)
    is_stable = bool(np.all(eigenvalues > -1e-8))
    return is_stable, eigenvalues
