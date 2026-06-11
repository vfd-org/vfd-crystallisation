#!/usr/bin/env python3
"""
Paper I --- verify_typology_levels.py

Deterministic sim verification of the L_0 and L_2 unconditional
structural counts of the closure-irreducibility typology.

  L_0: |V_600| = 120, regular degree 12, edge length 1/phi.
  L_2: A_{V_600} has 9 distinct eigenvalues; the +6phi eigenspace
       has dimension 4 (this is the sigma-paired dipole class of
       Paper I of the existence programme).

L_1 (sigma-orbit count: 94 fixed + 13 paired) is cited from
\\cite{SmartExistenceClosure} and \\cite{rhFormalSmart}; it depends
on the icosian-quaternion construction not reproduced here.

L_3 (pentagonal-clock K-poles {0, 20, 52, 72} with multiplicities
{1, 1, 5, 5}) is sim-verified in rh-formal's M1 computer check
\\cite{rhFormalSmart}.

Run:
    python verify_typology_levels.py

Outputs (deterministic at seed 42):
    output/typology_L0_L2.json     numeric verification
    output/L0_degree.png             vertex degree histogram
    output/L2_spectrum.png           A_{V_600} eigenvalue spectrum
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from collections import Counter

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

SEED = 42
PHI = (1.0 + 5.0 ** 0.5) / 2.0
OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def build_v600_vertices() -> np.ndarray:
    """Return the 120 unit-norm vertices of the 600-cell in R^4.

    Standard construction:
      - Type A (8):  +/-e_i  (permutations of (+/-1, 0, 0, 0))
      - Type B (16): (+/-1/2)^4
      - Type C (96): even permutations of (+/-phi/2, +/-1/2, +/-(1/phi)/2, 0)
    """
    half = 0.5
    half_phi = PHI / 2.0
    half_phi_inv = 1.0 / (2.0 * PHI)
    vertices = []
    # Type A
    for i in range(4):
        for sign in (1.0, -1.0):
            v = [0.0, 0.0, 0.0, 0.0]
            v[i] = sign
            vertices.append(v)
    # Type B
    for s0 in (-1, 1):
        for s1 in (-1, 1):
            for s2 in (-1, 1):
                for s3 in (-1, 1):
                    vertices.append([s0 * half, s1 * half, s2 * half, s3 * half])
    # Type C: even permutations of (phi/2, 1/2, (1/phi)/2, 0)
    # The 12 even permutations of (0,1,2,3):
    even_perms = [
        (0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2),
        (1, 0, 3, 2), (1, 2, 0, 3), (1, 3, 2, 0),
        (2, 0, 1, 3), (2, 1, 3, 0), (2, 3, 0, 1),
        (3, 0, 2, 1), (3, 1, 0, 2), (3, 2, 1, 0),
    ]
    for perm in even_perms:
        for s_a in (-1, 1):
            for s_b in (-1, 1):
                for s_c in (-1, 1):
                    v = [0.0, 0.0, 0.0, 0.0]
                    v[perm[0]] = s_a * half_phi
                    v[perm[1]] = s_b * half
                    v[perm[2]] = s_c * half_phi_inv
                    v[perm[3]] = 0.0
                    vertices.append(v)
    return np.array(vertices, dtype=float)


def build_v600_adjacency(V: np.ndarray, tol: float = 1e-7) -> tuple:
    """Edge length = nearest-neighbour distance = 1/phi.
    Returns (A, edge_length, degree_counts)."""
    n = V.shape[0]
    diffs = V[:, None, :] - V[None, :, :]
    dists = np.linalg.norm(diffs, axis=2)
    pos = dists[dists > 1e-9]
    edge_len = pos.min()
    A = (np.abs(dists - edge_len) < tol).astype(float)
    np.fill_diagonal(A, 0.0)
    degrees = A.sum(axis=1).astype(int)
    deg_counts = Counter(degrees.tolist())
    return A, float(edge_len), deg_counts


def spectral_decomposition(A: np.ndarray, tol: float = 1e-5) -> tuple:
    """Return (sorted distinct eigenvalues, multiplicities, total)."""
    eigvals = np.linalg.eigvalsh(A)
    # Group eigenvalues within tolerance
    distinct: list[float] = []
    counts: list[int] = []
    for ev in sorted(eigvals.tolist()):
        if distinct and abs(ev - distinct[-1]) < tol:
            counts[-1] += 1
        else:
            distinct.append(ev)
            counts.append(1)
    return distinct, counts, int(sum(counts))


def sigma_paired_class_dimension(A: np.ndarray, target: float, tol: float = 1e-5) -> int:
    """Return dimension of eigenspace of A at eigenvalue `target`."""
    eigvals = np.linalg.eigvalsh(A)
    return int(np.sum(np.abs(eigvals - target) < tol))


def main() -> int:
    print("=" * 70)
    print("Paper I sim --- verify L_0 and L_2 unconditional structural counts")
    print("Deterministic at seed 42 (no randomness used; seed for record only).")
    print("=" * 70)
    print()

    results: dict = {"seed": SEED, "phi": PHI}

    # L0 verification
    print("--- L_0: V_600 substrate ---")
    V = build_v600_vertices()
    n_vertices = V.shape[0]
    print(f"  vertex count: {n_vertices} (expected 120) "
          f"{'PASS' if n_vertices == 120 else 'FAIL'}")

    A, edge_len, deg_counts = build_v600_adjacency(V)
    expected_edge = 1.0 / PHI
    print(f"  edge length:  {edge_len:.6f} "
          f"(expected 1/phi = {expected_edge:.6f}) "
          f"{'PASS' if abs(edge_len - expected_edge) < 1e-9 else 'FAIL'}")

    distinct_degrees = sorted(deg_counts.keys())
    is_regular = len(distinct_degrees) == 1
    common_deg = distinct_degrees[0] if is_regular else None
    print(f"  graph regular: {is_regular} (single degree value present)")
    print(f"  vertex degree distribution: {dict(deg_counts)}")
    print(f"  expected: every vertex has degree 12 "
          f"{'PASS' if is_regular and common_deg == 12 else 'FAIL'}")
    print()

    results["L0"] = {
        "vertex_count": int(n_vertices),
        "edge_length": float(edge_len),
        "edge_length_expected": float(expected_edge),
        "regular": bool(is_regular),
        "common_degree": int(common_deg) if common_deg is not None else None,
        "expected_degree": 12,
        "pass": (n_vertices == 120 and is_regular and common_deg == 12),
    }

    # L2 verification: spectral decomposition
    print("--- L_2: A_{V_600} spectral decomposition ---")
    distinct, mults, total = spectral_decomposition(A)
    print(f"  number of distinct eigenvalues: {len(distinct)} (expected 9)")
    print(f"  total dimension: {total} (expected 120)")
    print(f"  eigenvalue | multiplicity")
    for ev, m in zip(distinct, mults):
        in_terms_of_phi = ev / PHI if PHI != 0 else 0
        annot = ""
        if abs(ev - 6 * PHI) < 1e-5:
            annot = "  <- +6 phi (sigma-paired dipole class)"
        elif abs(ev + 6 * PHI) < 1e-5:
            annot = "  <- -6 phi"
        elif abs(ev - 6) < 1e-5:
            annot = "  <- +6 (degree, leading eigenvalue ... actually degree = 12)"
        print(f"    {ev:+9.4f}  | {m:3d}   ({ev/PHI:+6.3f} * phi){annot}")

    dim_6phi = sigma_paired_class_dimension(A, 6 * PHI)
    print()
    print(f"  +6 phi eigenspace dimension: {dim_6phi} (expected 4) "
          f"{'PASS' if dim_6phi == 4 else 'FAIL'}")

    distinct_count_pass = (len(distinct) == 9)
    total_pass = (total == 120)
    print(f"  9 distinct eigenvalues:    {'PASS' if distinct_count_pass else 'FAIL'}")
    print(f"  total dim = 120:           {'PASS' if total_pass else 'FAIL'}")
    print()

    results["L2"] = {
        "n_distinct_eigenvalues": int(len(distinct)),
        "total_dimension": int(total),
        "distinct_eigenvalues": [float(ev) for ev in distinct],
        "multiplicities": [int(m) for m in mults],
        "sigma_paired_class_dimension": int(dim_6phi),
        "pass": (dim_6phi == 4 and distinct_count_pass and total_pass),
    }

    # L1, L3 status (cited, not re-verified here)
    print("--- L_1: sigma-orbit count (cited from Paper I + rh-formal) ---")
    print("  Expected: 94 sigma-fixed orbits + 13 sigma-paired orbit-pairs = 107 orbits total.")
    print("  Verification: depends on icosian-quaternion construction (Paper I, rh-formal).")
    print("  Not re-derived in this sim.")
    print()

    print("--- L_3: K-pole multiplicities (cited from rh-formal M1) ---")
    print("  Expected: K in {0, 20, 52, 72} with multiplicities {1, 1, 5, 5} for")
    print("  the cascade pentagonal-clock structure of zhat(z) (rh-formal Theorem M1).")
    print("  Sim-verified externally in rh-formal scripts.")
    print()

    results["L1_status"] = "cited from Paper I + rh-formal (icosian construction); not re-derived here"
    results["L3_status"] = "cited from rh-formal M1; sim-verified externally"

    # Save JSON
    with open(OUTPUT_DIR / "typology_L0_L2.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"saved {OUTPUT_DIR / 'typology_L0_L2.json'}")

    # Figures
    # L0 degree histogram
    fig, ax = plt.subplots(figsize=(7, 4))
    degs = sorted(deg_counts.keys())
    counts = [deg_counts[d] for d in degs]
    ax.bar(degs, counts, color="#3a7cd9", edgecolor="black")
    ax.set_xlabel("vertex degree")
    ax.set_ylabel("count")
    ax.set_title(f"L_0: V_600 vertex-degree distribution\n"
                 f"(120 vertices, all with degree 12: {'PASS' if is_regular and common_deg == 12 else 'FAIL'})")
    ax.grid(alpha=0.3, axis="y")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "L0_degree.png", dpi=120)
    plt.close()
    print(f"saved {OUTPUT_DIR / 'L0_degree.png'}")

    # L2 spectrum
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.bar(range(len(distinct)), mults, color="#9467bd",
           edgecolor="black", linewidth=0.5)
    ax.set_xticks(range(len(distinct)))
    ax.set_xticklabels([f"{ev:+.3f}" for ev in distinct], rotation=45, ha="right")
    ax.set_xlabel(r"eigenvalue of $A_{V_{600}}$")
    ax.set_ylabel("multiplicity")
    ax.set_title(rf"L_2: $A_{{V_{{600}}}}$ spectral decomposition "
                 rf"({len(distinct)} distinct eigenvalues, total dim {total})")
    # Mark the +6phi eigenspace
    for i, ev in enumerate(distinct):
        if abs(ev - 6 * PHI) < 1e-5:
            ax.bar(i, mults[i], color="#cd3a3a", edgecolor="black", linewidth=0.5,
                   label=rf"+6$\varphi$ (dim {mults[i]})")
            ax.legend()
            break
    ax.grid(alpha=0.3, axis="y")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "L2_spectrum.png", dpi=120)
    plt.close()
    print(f"saved {OUTPUT_DIR / 'L2_spectrum.png'}")
    print()

    # Summary
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    all_pass = (results["L0"]["pass"] and results["L2"]["pass"])
    print(f"  L_0 (vertex count + regularity):     {'PASS' if results['L0']['pass'] else 'FAIL'}")
    print(f"  L_2 (spectral decomposition):        {'PASS' if results['L2']['pass'] else 'FAIL'}")
    print(f"  L_1 (sigma-orbits):                  cited (Paper I, rh-formal)")
    print(f"  L_3 (K-poles):                       cited (rh-formal M1)")
    print()
    print(f"  Overall: {'ALL UNCONDITIONAL CHECKS PASS' if all_pass else 'FAILURE'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
