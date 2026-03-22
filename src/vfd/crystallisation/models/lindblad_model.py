"""
M1 — Standard Lindblad (Baseline)

    dρ/dt = -i/ħ [H, ρ] + L_env[ρ]

No collapse, no selection mechanism. Pure open quantum system evolution.
Off-diagonals decay; diagonal remains a classical mixture.
Outcome selection is by Born-rule sampling from the decohered diagonal.
"""

from __future__ import annotations
import numpy as np
from numpy.typing import NDArray


class LindbladModel:
    """Standard Lindblad master equation evolution."""

    name = "Lindblad"

    def __init__(
        self,
        H: NDArray,
        gamma: float = 0.05,
        seed: int = 42,
    ):
        """
        Args:
            H: Hamiltonian matrix (n x n, Hermitian)
            gamma: dephasing rate (environment coupling)
            seed: RNG seed for measurement sampling
        """
        self.H = np.asarray(H, dtype=np.complex128)
        self.n = self.H.shape[0]
        self.gamma = gamma
        self.rng = np.random.default_rng(seed)

    def step(self, rho: NDArray, dt: float) -> NDArray:
        """Single Euler step of Lindblad evolution."""
        # Unitary part: -i[H, rho]
        commutator = self.H @ rho - rho @ self.H
        drho = -1j * commutator

        # Lindblad dephasing: decay off-diagonals
        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    drho[i, j] -= self.gamma * rho[i, j]

        rho_new = rho + dt * drho
        # Enforce Hermiticity
        rho_new = 0.5 * (rho_new + rho_new.conj().T)
        # Enforce trace = 1
        tr = np.trace(rho_new)
        if abs(tr) > 1e-15:
            rho_new = rho_new / tr
        return rho_new

    def run(self, initial_state: NDArray, T: float, dt: float) -> list[NDArray]:
        """Run evolution for time T, return trajectory of density matrices."""
        rho = np.asarray(initial_state, dtype=np.complex128).copy()
        n_steps = int(T / dt)
        trajectory = [rho.copy()]
        for _ in range(n_steps):
            rho = self.step(rho, dt)
            trajectory.append(rho.copy())
        return trajectory

    def measure(self, state: NDArray) -> int:
        """Sample outcome from diagonal (Born rule on decohered state)."""
        diag = np.real(np.diag(state))
        diag = np.maximum(diag, 0)
        total = diag.sum()
        if total < 1e-15:
            return self.rng.integers(0, self.n)
        probs = diag / total
        return int(self.rng.choice(self.n, p=probs))
