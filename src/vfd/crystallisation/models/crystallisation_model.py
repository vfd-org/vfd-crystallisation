"""
M4 — VFD Crystallisation Model

    dρ/dt = -i/ħ [H, ρ] + L_env[ρ] - λ ∇_ρ F[ρ]

    F[ρ] = α R[ρ] + β E[ρ] - γ Q[ρ]

Deterministic constraint-driven state selection via closure functional
minimisation. Same interface as all other models.
"""

from __future__ import annotations
import numpy as np
from numpy.typing import NDArray


class CrystallisationModel:
    """VFD crystallisation dynamics on density matrices."""

    name = "VFD_Crystallisation"

    def __init__(
        self,
        H: NDArray,
        gamma_env: float = 0.05,
        lam: float = 1.0,
        alpha: float = 1.0,
        beta: float = 0.5,
        gamma_coherence: float = 0.8,
        seed: int = 42,
    ):
        """
        Args:
            H: Hamiltonian
            gamma_env: dephasing rate (Lindblad environment coupling)
            lam: crystallisation drive strength
            alpha: residual weight
            beta: energy weight
            gamma_coherence: coherence weight
            seed: RNG seed (used only for measure())
        """
        self.H = np.asarray(H, dtype=np.complex128)
        self.n = self.H.shape[0]
        self.gamma_env = gamma_env
        self.lam = lam
        self.alpha = alpha
        self.beta = beta
        self.gamma_c = gamma_coherence
        self.K = np.eye(self.n, dtype=np.complex128)  # constraint target
        self.rng = np.random.default_rng(seed)

    def _closure_residual(self, rho: NDArray) -> float:
        diff = rho - self.K
        return float(np.real(np.trace(diff @ diff.conj().T)))

    def _energy(self, rho: NDArray) -> float:
        return float(np.real(np.trace(self.H @ rho)))

    def _coherence(self, rho: NDArray) -> float:
        off_diag_sum = 0.0
        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    off_diag_sum += np.abs(rho[i, j])
        max_off = self.n * (self.n - 1)
        return float(off_diag_sum / max_off) if max_off > 0 else 0.0

    def _functional(self, rho: NDArray) -> float:
        return (self.alpha * self._closure_residual(rho)
                + self.beta * self._energy(rho)
                - self.gamma_c * self._coherence(rho))

    def _grad_functional(self, rho: NDArray, eps: float = 1e-6) -> NDArray:
        """Numerical gradient of F w.r.t. real and imaginary parts of rho."""
        grad = np.zeros_like(rho)
        for i in range(self.n):
            for j in range(self.n):
                # Real part
                rho_p = rho.copy(); rho_p[i, j] += eps
                rho_m = rho.copy(); rho_m[i, j] -= eps
                grad[i, j] = (self._functional(rho_p) - self._functional(rho_m)) / (2 * eps)
                # Imaginary part
                rho_p = rho.copy(); rho_p[i, j] += 1j * eps
                rho_m = rho.copy(); rho_m[i, j] -= 1j * eps
                grad[i, j] += 1j * (self._functional(rho_p) - self._functional(rho_m)) / (2 * eps)
        return grad

    def step(self, rho: NDArray, dt: float) -> NDArray:
        # Unitary: -i[H, rho]
        commutator = self.H @ rho - rho @ self.H
        drho = -1j * commutator

        # Lindblad dephasing
        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    drho[i, j] -= self.gamma_env * rho[i, j]

        # Crystallisation drive: -λ ∇_ρ F
        grad_F = self._grad_functional(rho)
        drho -= self.lam * grad_F

        rho_new = rho + dt * drho
        # Enforce Hermiticity and trace
        rho_new = 0.5 * (rho_new + rho_new.conj().T)
        tr = np.trace(rho_new)
        if abs(tr) > 1e-15:
            rho_new = rho_new / tr
        return rho_new

    def run(self, initial_state: NDArray, T: float, dt: float) -> list[NDArray]:
        rho = np.asarray(initial_state, dtype=np.complex128).copy()
        n_steps = int(T / dt)
        trajectory = [rho.copy()]
        for _ in range(n_steps):
            rho = self.step(rho, dt)
            trajectory.append(rho.copy())
        return trajectory

    def measure(self, state: NDArray) -> int:
        """Measure: pick maximum diagonal element (deterministic selection)."""
        diag = np.real(np.diag(state))
        return int(np.argmax(diag))
