"""
M2 — GRW-style Stochastic Collapse Proxy

Discrete random jumps at Poisson rate lambda_GRW.
Between jumps: unitary + Lindblad dephasing.
At jump: random projection onto a basis state with Born-rule probability.
"""

from __future__ import annotations
import numpy as np
from numpy.typing import NDArray


class GRWModel:
    """GRW-style spontaneous collapse model."""

    name = "GRW"

    def __init__(
        self,
        H: NDArray,
        gamma: float = 0.05,
        lambda_grw: float = 0.01,
        seed: int = 42,
    ):
        """
        Args:
            H: Hamiltonian
            gamma: dephasing rate
            lambda_grw: collapse rate (probability of collapse per dt)
            seed: RNG seed
        """
        self.H = np.asarray(H, dtype=np.complex128)
        self.n = self.H.shape[0]
        self.gamma = gamma
        self.lambda_grw = lambda_grw
        self.rng = np.random.default_rng(seed)

    def step(self, rho: NDArray, dt: float) -> NDArray:
        """Single step: Lindblad evolution + possible GRW collapse."""
        # Unitary + dephasing
        commutator = self.H @ rho - rho @ self.H
        drho = -1j * commutator
        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    drho[i, j] -= self.gamma * rho[i, j]

        rho_new = rho + dt * drho
        rho_new = 0.5 * (rho_new + rho_new.conj().T)
        tr = np.trace(rho_new)
        if abs(tr) > 1e-15:
            rho_new = rho_new / tr

        # GRW collapse event (Poisson process)
        if self.rng.random() < self.lambda_grw * dt:
            diag = np.real(np.diag(rho_new))
            diag = np.maximum(diag, 0)
            total = diag.sum()
            if total > 1e-15:
                probs = diag / total
                k = int(self.rng.choice(self.n, p=probs))
                # Project onto state k
                rho_new = np.zeros_like(rho_new)
                rho_new[k, k] = 1.0

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
        diag = np.real(np.diag(state))
        diag = np.maximum(diag, 0)
        total = diag.sum()
        if total < 1e-15:
            return self.rng.integers(0, self.n)
        probs = diag / total
        return int(self.rng.choice(self.n, p=probs))
