#!/usr/bin/env python3
"""
The Montgomery-Odlyzko test for cascade T_ζ-Laplacian:
  Do the eigenvalue spacings of T_ζ = A + P_σ on 600-cell follow GUE
  (matching classical Riemann ζ-zero spacings)?

Background:
  Montgomery (1973) + Odlyzko (1987) showed that imaginary parts γ_n
  of Riemann ζ-zeros on the critical line have nearest-neighbour
  spacing distribution matching the Gaussian Unitary Ensemble (GUE)
  of random matrix theory. This is one of the strongest empirical
  signatures that ζ-zeros come from a self-adjoint Hermitian operator
  (the Hilbert-Pólya conjecture).

  Atas-Bogomolny-Giraud-Roux 2013: ratio statistic ⟨r̃⟩ = ⟨min(r,1/r)⟩
    where r = s_{i+1}/s_i. Reference values:
      Poisson  (random): ⟨r̃⟩ = 2 ln 2 - 1 ≈ 0.3863
      GOE (real symm.):  ⟨r̃⟩ ≈ 0.5359
      GUE (Hermitian):   ⟨r̃⟩ ≈ 0.6027

If cascade T_ζ has GUE spacings → cascade ζ-operator IS in the same
universality class as classical ζ. By proxy, the spectral content
encodes the same statistical structure.

This test isolates Test 3 (graph Laplacians) from aria-chess's
run_zeta_gue_test.py, since we don't have EEG access here.
"""

from __future__ import annotations

import sys
from pathlib import Path
import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
sys.path.insert(0, str(REPO_ROOT / "papers" / "paper-xxii" / "scripts"))

from run_icosian_exact import (  # noqa: E402
    q_zero, q_one, q_neg, q_add, q_sub, q_mul, q_scale,
    qq_mul, qq_conjugate, qq_norm_sq, qq_eq, qq_key,
    build_vertices, vertex_index_map, vertex_index_exact,
    qq_distance_sq,
)


R_POISSON = 2 * np.log(2) - 1   # ≈ 0.3863
R_GOE = 0.5359                   # Wigner β=1
R_GUE = 0.6027                   # Wigner β=2


def r_tilde_stat(eigs, drop_first=0):
    """⟨r̃⟩ = ⟨min(r, 1/r)⟩ over consecutive spacings of sorted eigs."""
    eigs = np.sort(np.asarray(eigs, dtype=float))
    if drop_first > 0:
        eigs = eigs[drop_first:]
    eigs = eigs[eigs > 1e-10 * np.max(np.abs(eigs))]
    s = np.diff(eigs)
    s = s[s > 0]
    if len(s) < 3:
        return {"n_eigs": len(eigs), "n_spacings": len(s),
                "r_tilde_mean": float("nan")}
    r = s[1:] / s[:-1]
    r_tilde = np.minimum(r, 1.0 / r)
    return {
        "n_eigs": int(len(eigs)),
        "n_spacings": int(len(s)),
        "r_tilde_mean": float(np.mean(r_tilde)),
        "r_tilde_median": float(np.median(r_tilde)),
        "r_tilde_std": float(np.std(r_tilde)),
    }


def classify(r_mean):
    candidates = {"Poisson": R_POISSON, "GOE": R_GOE, "GUE": R_GUE}
    d = {k: abs(v - r_mean) for k, v in candidates.items()}
    nearest = min(d, key=d.get)
    return f"{nearest} (|Δ| = {d[nearest]:.4f})"


def sigma_pair(x):
    return (x[0], -x[1])


def sigma_on_quat(q):
    return tuple(sigma_pair(c) for c in q)


def main():
    print("=" * 76)
    print("Montgomery-Odlyzko GUE test for cascade T_ζ-Laplacian on 600-cell.")
    print("Does cascade ζ-operator match the classical Riemann ζ-zero spacing")
    print("distribution? If yes, structural identity is empirically supported.")
    print("=" * 76)

    print(f"\nReference values:")
    print(f"  Poisson (random):    ⟨r̃⟩ = {R_POISSON:.4f}")
    print(f"  GOE (real symm):     ⟨r̃⟩ = {R_GOE:.4f}")
    print(f"  GUE (Hermitian):     ⟨r̃⟩ = {R_GUE:.4f}")

    # --- Build 600-cell adjacency ---
    print(f"\n[1] Build 600-cell adjacency (12-regular).")
    verts = build_vertices()
    identity = (q_one(), q_zero(), q_zero(), q_zero())
    id_idx = vertex_index_exact(identity, verts)
    verts[0], verts[id_idx] = verts[id_idx], verts[0]
    idx_map = vertex_index_map(verts)

    # Find nearest-neighbour distance (edge condition)
    min_d = None
    for j in range(1, 120):
        d = qq_distance_sq(verts[0], verts[j])
        if min_d is None:
            min_d = d
        else:
            cur_real = float(min_d[0]) + float(min_d[1]) * (5 ** 0.5)
            new_real = float(d[0]) + float(d[1]) * (5 ** 0.5)
            if new_real < cur_real - 1e-12:
                min_d = d

    A = np.zeros((120, 120))
    for i in range(120):
        for j in range(120):
            if i != j and qq_distance_sq(verts[i], verts[j]) == min_d:
                A[i, j] = 1.0
    print(f"    Adjacency built: {int(A.sum() / 2)} undirected edges = "
          f"{120 * 12 // 2} expected.")

    # --- Test 1: bare H₄ Laplacian ---
    print(f"\n[2] Test 1: bare 600-cell graph Laplacian L = D - A")
    D = np.diag(A.sum(axis=1))
    L = D - A
    eigs_L = np.linalg.eigvalsh(L)
    stat_L = r_tilde_stat(eigs_L, drop_first=1)
    stat_L["classify"] = classify(stat_L["r_tilde_mean"])
    print(f"    n_eigs = {stat_L['n_eigs']}, n_spacings = {stat_L['n_spacings']}")
    print(f"    ⟨r̃⟩ = {stat_L['r_tilde_mean']:.4f} → {stat_L['classify']}")

    # --- Test 2: cascade T_ζ = A + P_σ ---
    print(f"\n[3] Test 2: cascade T_ζ-Laplacian = D' - (A + P_σ)")
    print(f"    where P_σ is the σ-permutation matrix on 2I.")
    # Build σ-permutation: P_σ[v, σ(v)] = 1 for σ-orbit pairs
    P = np.zeros((120, 120))
    for i in range(120):
        sv = sigma_on_quat(verts[i])
        if qq_key(sv) in idx_map:
            j = idx_map[qq_key(sv)]
            P[i, j] = 1.0
        # else: σ takes v outside 2I, no entry (P[i,*] = 0 row)
    # Note: only 24 vertices map to 2I under σ; others are zero rows
    P_diag = P.diagonal()
    n_self_fixed = int(P_diag.sum())
    n_paired = int(((P + P.T) > 0).sum() // 2 - n_self_fixed)
    print(f"    σ-self-fixed (P[v,v]=1): {n_self_fixed}")
    print(f"    σ-paired (P[v,σv]=1, σv≠v): {n_paired}")
    print(f"    σ-undefined (σ(v) outside 2I): {120 - int(P.sum())}")

    A_zeta = A + P
    D_zeta = np.diag(A_zeta.sum(axis=1))
    L_zeta = D_zeta - A_zeta
    # L_zeta is not symmetric in general (P may be asymmetric);
    # use real eigenvalues as a Hermitian-class spectrum
    L_zeta_sym = (L_zeta + L_zeta.T) / 2
    eigs_Lz = np.linalg.eigvalsh(L_zeta_sym)
    stat_Lz = r_tilde_stat(eigs_Lz, drop_first=1)
    stat_Lz["classify"] = classify(stat_Lz["r_tilde_mean"])
    print(f"    n_eigs = {stat_Lz['n_eigs']}, n_spacings = {stat_Lz['n_spacings']}")
    print(f"    ⟨r̃⟩ = {stat_Lz['r_tilde_mean']:.4f} → {stat_Lz['classify']}")

    # --- Test 3: classical Riemann γ_n (first 50) ---
    print(f"\n[4] Test 3: classical Riemann ζ-zero imaginary parts γ_n (first 50)")
    gamma_n = np.array([
        14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862, 40.9187, 43.3271,
        48.0052, 49.7738, 52.9703, 56.4462, 59.3470, 60.8318, 65.1125, 67.0798,
        69.5464, 72.0672, 75.7047, 77.1448, 79.3374, 82.9104, 84.7355, 87.4253,
        88.8091, 92.4919, 94.6513, 95.8706, 98.8312, 101.3179, 103.7256, 105.4466,
        107.1686, 111.0295, 111.8746, 114.3202, 116.2267, 118.7907, 121.3702, 122.9468,
        124.2569, 127.5167, 129.5787, 131.0879, 133.4978, 134.7565, 138.1160, 139.7362,
        141.1237, 143.1118,
    ])
    stat_g = r_tilde_stat(gamma_n)
    stat_g["classify"] = classify(stat_g["r_tilde_mean"])
    print(f"    n_eigs = {stat_g['n_eigs']}, n_spacings = {stat_g['n_spacings']}")
    print(f"    ⟨r̃⟩ = {stat_g['r_tilde_mean']:.4f} → {stat_g['classify']}")

    # --- Verdict ---
    print()
    print("=" * 76)
    print("VERDICT — does cascade T_ζ-Laplacian match classical Riemann ζ statistics?")
    print()
    print(f"  Bare 600-cell H₄ Laplacian:    {stat_L['classify']}")
    print(f"  Cascade T_ζ = A + P_σ:          {stat_Lz['classify']}")
    print(f"  Classical Riemann γ_n (50):     {stat_g['classify']}")
    print()
    delta_zeta = abs(stat_Lz['r_tilde_mean'] - stat_g['r_tilde_mean'])
    print(f"  T_ζ ↔ Riemann γ_n distance:    |Δ⟨r̃⟩| = {delta_zeta:.4f}")
    print()
    if delta_zeta < 0.05:
        print(f"  ✓✓✓ STRONG MATCH: cascade T_ζ statistics match classical Riemann.")
        print(f"      The cascade ζ-operator and the Riemann ζ are in the SAME")
        print(f"      universality class. Empirical evidence for the identity.")
    elif delta_zeta < 0.10:
        print(f"  ✓ PARTIAL MATCH: cascade T_ζ within 10% of classical Riemann.")
        print(f"      Suggestive but not decisive. More data needed.")
    else:
        print(f"  ✗ NO MATCH: cascade T_ζ statistics differ from classical Riemann.")
        print(f"      The two are NOT in the same universality class.")
    print("=" * 76)


if __name__ == "__main__":
    main()
