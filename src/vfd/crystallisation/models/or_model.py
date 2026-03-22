"""
M3 — Penrose OR-style Objective Reduction Proxy

Collapse rate tied to an energy-separation measure:
    tau^{-1} ~ E_sep

When superposition "energy spread" exceeds threshold,
collapse is triggered stochastically with rate proportional to E_sep.

This is a proxy — not a full gravitational self-energy calculation.
"""

from __future__ import annotations
import numpy as np
from numpy.typing import NDArray


class ORModel:
    """Penrose-inspired objective reduction proxy."""

    name = "OR"

    def __init__(
        self,
        H: NDArray,
        gamma: float = 0.05,
        or_coupling: float = 0.5,
        seed: int = 42,
    ):
        """
        Args:
            H: Hamiltonian
            gamma: dephasing rate
            or_coupling: proportionality constant for E_sep -> collapse rate
            seed: RNG seed
        """
        self.H = np.asarray(H, dtype=np.complex128)
        self.n = self.H.shape[0]
        self.gamma = gamma
        self.or_coupling = or_coupling
        self.rng = np.random.default_rng(seed)
        self.eigenvalues = np.real(np.linalg.eigvalsh(self.H))

    def _energy_separation(self, rho: NDArray) -> float:
        """Compute energy spread as proxy for gravitational self-energy."""
        diag = np.real(np.diag(rho))
        diag = np.maximum(diag, 0)
        total = diag.sum()
        if total < 1e-15:
            return 0.0
        probs = diag / total
        E_mean = np.sum(probs * self.eigenvalues[:self.n])
        E_var = np.sum(probs * (self.eigenvalues[:self.n] - E_mean)**2)
        return float(np.sqrt(E_var))

    def step(self, rho: NDArray, dt: float) -> NDArray:
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

        # OR collapse: rate ~ or_coupling * E_sep
        E_sep = self._energy_separation(rho_new)
        collapse_rate = self.or_coupling * E_sep
        if collapse_rate > 0 and self.rng.random() < collapse_rate * dt:
            diag = np.real(np.diag(rho_new))
            diag = np.maximum(diag, 0)
            total = diag.sum()
            if total > 1e-15:
                probs = diag / total
                k = int(self.rng.choice(self.n, p=probs))
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
