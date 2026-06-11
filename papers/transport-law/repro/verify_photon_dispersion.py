# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Lee Smart / Institute of Vibrational Field Dynamics
"""
Massless photon dispersion in the trivial sector of L_{V_600}.

Closes part of transport-law §6: Hypothesis cor:photon — the photon
identification with the λ = 0 eigenmode of L_{V_600}, with the
Schrödinger-limit dispersion of Hypothesis prop:dispersion specialised to
m_ρ² = β · λ_ρ = 0.

DERIVATION
==========

The graph Laplacian L on V_600 has spectrum (multiplicities)
    {0: 1,  λ_1: 4,  λ_2: 9,  9: 16,  12: 25,  14: 36, …, 15.71: 4}.
The unique λ = 0 eigenmode is the constant vector u_0 ∝ (1, 1, …, 1).
Under the Schrödinger-limit evolution iψ̇ = L ψ, eigenmode u_λ evolves as
    u_λ(t)  =  exp(−i λ t) u_λ(0).

For the trivial sector λ = 0:
    u_0(t)  =  u_0(0)        (zero-frequency — massless sector witness;
                              the trivial-sector mode is exactly stationary
                              under iψ̇ = Lψ).
For non-trivial λ > 0:
    u_λ(t)  oscillates at angular frequency  ω_λ = λ
    ⇒ |u_λ(t)|² = const, but the phase rotates at rate λ.

The transport-law dispersion identification is m_ρ² = β λ_ρ; for the
trivial sector λ = 0, m = 0 (massless), and the dispersion specialises to
ω² = c²_eff k² + 0 — the photon dispersion. The script verifies:

  (P1) λ_min = 0 with multiplicity 1; eigenvector ≈ uniform.
  (P2) The trivial-sector projector P_0 satisfies L P_0 = 0 to machine
       precision.
  (P3) For an initial state purely in the trivial sector, the Schrödinger
       evolution is exactly stationary: ψ(t) = ψ(0) (zero-frequency mode).
  (P4) For an initial state purely in a non-trivial eigenmode of L with
       eigenvalue λ > 0, the evolution is ψ(t) = e^{-iλt} ψ(0); the
       extracted oscillation frequency matches λ to floating-point.

EXPECTED OUTPUT (results_photon_dispersion.json)
------------------------------------------------
  v600_size                 = 120
  trivial_eigenvalue        ≈ 0   (within 1e-12)
  trivial_multiplicity      = 1
  trivial_uniform_max_dev   ≲ 1e-15  (eigenvector is uniform)
  L_P0_norm                 ≲ 1e-13  (operator-level zero)
  trivial_propagation_drift ≲ 1e-13
  nontrivial_freq_match     ≲ 1e-12
  pass                      = true
"""
from __future__ import annotations

import json
import math
import os
import sys
from typing import List, Tuple

import numpy as np
from scipy.linalg import expm

PHI = (1.0 + math.sqrt(5.0)) / 2.0


def build_600cell_vertices() -> np.ndarray:
    verts: List[List[float]] = []
    verts.append([1.0, 0.0, 0.0, 0.0])
    verts.append([-1.0, 0.0, 0.0, 0.0])
    for i in range(1, 4):
        for s in (1, -1):
            v = [0.0, 0.0, 0.0, 0.0]
            v[i] = s
            verts.append(v)
    for s0 in (1, -1):
        for s1 in (1, -1):
            for s2 in (1, -1):
                for s3 in (1, -1):
                    verts.append([s0 * 0.5, s1 * 0.5, s2 * 0.5, s3 * 0.5])
    base = [PHI / 2.0, 0.5, 1.0 / (2.0 * PHI), 0.0]
    even_perms = [
        (0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2),
        (1, 0, 3, 2), (1, 2, 0, 3), (1, 3, 2, 0),
        (2, 0, 1, 3), (2, 1, 3, 0), (2, 3, 0, 1),
        (3, 0, 2, 1), (3, 1, 0, 2), (3, 2, 1, 0),
    ]
    for perm in even_perms:
        for s0 in (1, -1):
            for s1 in (1, -1):
                for s2 in (1, -1):
                    vals = [s0 * base[0], s1 * base[1], s2 * base[2], 0.0]
                    v = [0.0, 0.0, 0.0, 0.0]
                    for i, p in enumerate(perm):
                        v[p] = vals[i]
                    verts.append(v)
    arr = np.asarray(verts, dtype=float)
    arr = arr / np.linalg.norm(arr, axis=1, keepdims=True)
    unique: List[np.ndarray] = [arr[0]]
    for v in arr[1:]:
        if all(np.linalg.norm(v - u) > 0.01 for u in unique):
            unique.append(v)
    return np.asarray(unique[:120], dtype=float)


def build_graph_laplacian(verts: np.ndarray) -> np.ndarray:
    n = verts.shape[0]
    target = PHI / 2.0
    tol = 1e-3
    A = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(float(np.dot(verts[i], verts[j])) - target) < tol:
                A[i, j] = 1.0
                A[j, i] = 1.0
    deg = np.diag(A.sum(axis=1))
    return deg - A


def main() -> int:
    print("=" * 72)
    print("  Massless photon dispersion: λ = 0 sector of L_{V_600}")
    print("  (transport-law Hypothesis cor:photon + prop:dispersion at λ=0)")
    print("=" * 72)

    print("\n[1/4] building L_{V_600} and computing spectrum…")
    verts = build_600cell_vertices()
    n = verts.shape[0]
    L = build_graph_laplacian(verts)
    eigvals, eigvecs = np.linalg.eigh(L)
    # Multiplicity-grouped spectrum
    rounded = np.round(eigvals, 6)
    unique_vals, mults = np.unique(rounded, return_counts=True)
    print(f"      |V_600| = {n}; spectrum (eigval, mult):")
    for v, m in zip(unique_vals, mults):
        print(f"        λ = {v:8.4f}   ×{m}")

    print("\n[2/4] (P1) verifying λ_min = 0, multiplicity 1, uniform eigenvector…")
    lam_min = float(eigvals[0])
    lam_min_pass = abs(lam_min) < 1e-10
    P1_mult = int(np.sum(np.abs(eigvals) < 1e-10))
    P1_mult_pass = (P1_mult == 1)
    u0 = eigvecs[:, 0]
    u0 = u0 / np.linalg.norm(u0)
    uniform_value = float(u0.mean())
    uniform_dev = float(np.max(np.abs(u0 - uniform_value)))
    P1_uniform_pass = uniform_dev < 1e-12
    print(f"      λ_min = {lam_min:.3e}            (expect ~0)")
    print(f"      mult(λ=0) = {P1_mult}                        (expect 1)")
    print(f"      uniform-eigenvector deviation = {uniform_dev:.3e} (expect ~0)")

    print("\n[3/4] (P2) verifying trivial-sector projector annihilates L…")
    P0 = np.outer(u0, u0)
    LP0_norm = float(np.linalg.norm(L @ P0))
    P2_pass = LP0_norm < 1e-12
    print(f"      ‖L · P_0‖_F = {LP0_norm:.3e}    (operator-level zero)")

    print("\n[4/4] (P3, P4) Schrödinger evolution: trivial mode stationary,"
          " non-trivial mode rotates at e^{-iλt}…")
    dt = 0.1
    n_ticks = 50
    U = expm(-1j * L * dt)

    # P3: pure trivial-mode initial state — should be stationary
    psi_triv = u0.astype(complex)
    psi_t = psi_triv.copy()
    max_dev_triv = 0.0
    for _ in range(n_ticks):
        psi_t = U @ psi_t
        max_dev_triv = max(max_dev_triv,
                           float(np.linalg.norm(psi_t - psi_triv)))
    print(f"      (P3) max |ψ(t) − ψ(0)| in trivial sector = "
          f"{max_dev_triv:.3e}  (expect ~0)")
    P3_pass = max_dev_triv < 1e-12

    # P4: pure eigenmode for some non-trivial λ — should rotate at exactly λ
    # Pick the second eigenvalue (smallest positive)
    nz_idx = int(np.argmax(np.abs(eigvals) > 1e-10))   # first nonzero
    lam_nz = float(eigvals[nz_idx])
    u_nz = eigvecs[:, nz_idx].astype(complex)
    psi_t = u_nz.copy()
    # After total time T = n_ticks * dt, expected ψ = e^{-i λ T} u_nz
    T = n_ticks * dt
    for _ in range(n_ticks):
        psi_t = U @ psi_t
    expected = np.exp(-1j * lam_nz * T) * u_nz
    freq_match_dev = float(np.linalg.norm(psi_t - expected))
    print(f"      (P4) non-trivial λ = {lam_nz:.4f},"
          f" T = {T:.1f}, |ψ(T) − e^{{-iλT}} u_λ| = {freq_match_dev:.3e}")
    P4_pass = freq_match_dev < 1e-10

    all_pass = lam_min_pass and P1_mult_pass and P1_uniform_pass and P2_pass and P3_pass and P4_pass

    print(f"\n  ═══ {6 if all_pass else 'FAIL'}/6 photon-sector criteria verified ═══")
    print(f"     λ_min ≈ 0                                  {lam_min_pass}")
    print(f"     mult(λ=0) = 1                              {P1_mult_pass}")
    print(f"     trivial eigenvector uniform                 {P1_uniform_pass}")
    print(f"     L · P_0 ≈ 0 (operator-level zero)            {P2_pass}")
    print(f"     trivial-sector evolution stationary         {P3_pass}")
    print(f"     non-trivial mode ω = λ exact                {P4_pass}")

    results = {
        "v600_size": int(n),
        "spectrum_eigenvalues": [float(x) for x in unique_vals.tolist()],
        "spectrum_multiplicities": [int(m) for m in mults.tolist()],
        "lam_min": float(lam_min),
        "trivial_multiplicity": int(P1_mult),
        "trivial_eigenvector_uniform_dev": float(uniform_dev),
        "L_P0_frobenius_norm": float(LP0_norm),
        "trivial_propagation_max_dev": float(max_dev_triv),
        "non_trivial_eigenvalue_tested": float(lam_nz),
        "non_trivial_freq_match_dev": float(freq_match_dev),
        "all_six_pass": bool(all_pass),
    }
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "results_photon_dispersion.json")
    with open(out_path, "w") as fh:
        json.dump(results, fh, indent=2)
    print(f"\n  Wrote {out_path}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
