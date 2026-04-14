#!/usr/bin/env python3
"""
Coupling Structure and UV Finiteness Analysis
===============================================
Paper XXII: Toward the Standard Model from Closure Geometry

This script addresses Gaps 4 and 5:
  Gap 4: Coupling constants from inter-sector graph structure
  Gap 5: UV finiteness from the finite 600-cell mode count

Computes:
1. The inter-sector coupling matrix from A^2 and A^3
2. Three-point and four-point vertex structure between eigenvalue sectors
3. Coupling ratios between the mass-carrying sectors
4. Mode count and effective dimension of the physical sector
5. UV finiteness argument from the finite spectral decomposition

Requirements: numpy, scipy
Usage: python run_coupling_structure.py
"""

import numpy as np
from collections import Counter, defaultdict
from itertools import permutations, product as iproduct
from scipy.spatial.distance import cdist

PHI = (1 + np.sqrt(5)) / 2
SQRT5 = np.sqrt(5)


def generate_600cell():
    """Generate all 120 vertices of the 600-cell."""
    vertices = set()
    for i in range(4):
        for s in [1.0, -1.0]:
            v = [0.0] * 4; v[i] = s
            vertices.add(tuple(round(x, 12) for x in v))
    for signs in iproduct([0.5, -0.5], repeat=4):
        vertices.add(tuple(round(x, 12) for x in signs))
    all_p = list(permutations([0, 1, 2, 3]))
    even_p = [p for p in all_p
              if sum(1 for i in range(4) for j in range(i+1, 4) if p[i] > p[j]) % 2 == 0]
    for perm in even_p:
        for s1 in [1, -1]:
            for s2 in [1, -1]:
                for s3 in [1, -1]:
                    base = [0.0, s1 * 0.5, s2 * PHI / 2, s3 / (2 * PHI)]
                    v = [base[perm.index(i)] for i in range(4)]
                    vertices.add(tuple(round(x, 12) for x in v))
    return np.array(sorted(vertices))


def main():
    print("=" * 70)
    print("COUPLING STRUCTURE AND UV FINITENESS ANALYSIS")
    print("Paper XXII: Toward the Standard Model from Closure Geometry")
    print("=" * 70)

    # Build 600-cell graph
    V = generate_600cell()
    dists = cdist(V, V)
    np.fill_diagonal(dists, np.inf)
    nn_dist = np.min(dists)
    A = (np.abs(dists - nn_dist) < 1e-6).astype(float)

    # Eigendecomposition
    eigenvalues, eigenvectors = np.linalg.eigh(A)

    # Group by eigenvalue
    eig_sectors = {}
    for i, ev in enumerate(eigenvalues):
        key = round(ev, 2)
        if key not in eig_sectors:
            eig_sectors[key] = []
        eig_sectors[key].append(i)

    # Projection matrices onto each sector
    projectors = {}
    for alpha, indices in eig_sectors.items():
        V_sec = eigenvectors[:, indices]
        projectors[alpha] = V_sec @ V_sec.T  # 120x120 projector

    # ================================================================
    print("\n" + "=" * 70)
    print("PART 1: INTER-SECTOR COUPLING STRUCTURE (Gap 4)")
    print("=" * 70)

    # The adjacency matrix A connects vertices. In the eigenbasis,
    # A is diagonal (eigenvalue alpha on each sector).
    # But A^2 (two-step paths) and A^3 (three-step paths) encode
    # higher-order coupling structure.

    A2 = A @ A  # two-step paths
    A3 = A @ A @ A  # three-step paths

    print("\n[1] GRAPH POWERS (multi-step paths)")
    print(f"    A:  {int(A.sum())} total connections (degree 12 × 120 = {12*120})")
    print(f"    A²: encodes 2-step paths")
    print(f"    A³: encodes 3-step paths (3-vertex interactions)")

    # In the eigenbasis, A^n has eigenvalue alpha^n on each sector.
    # But the PHYSICAL coupling between sectors comes from the
    # REAL-SPACE structure of the graph, not just eigenvalues.

    # The key quantity for coupling: given three eigenvalue sectors
    # alpha_1, alpha_2, alpha_3, the three-point coupling is:
    #   C_{123} = Tr(P_1 A P_2 A P_3) / sqrt(m_1 m_2 m_3)
    # where P_i is the projector onto sector i and m_i is multiplicity.

    print("\n[2] THREE-POINT COUPLING MATRIX")
    print(f"    C_{{ijk}} = Tr(P_i A P_j A P_k) / sqrt(m_i m_j m_k)")
    print(f"    This measures the amplitude for a 3-vertex process")
    print(f"    connecting sectors i, j, k through the graph.\n")

    # Focus on the integer (mass-carrying) sectors
    integer_alphas = [3.0, 0.0, -2.0, -3.0]  # lambda = 9, 12, 14, 15
    integer_names = {3.0: "λ=9 (dim4)", 0.0: "λ=12 (dim5)",
                     -2.0: "λ=14 (dim6)", -3.0: "λ=15 (dim4')"}

    # Two-point coupling (propagator structure): C_ij = Tr(P_i A^2 P_j) / sqrt(m_i m_j)
    print(f"    {'':>14}", end="")
    for a2 in integer_alphas:
        print(f" {integer_names[a2]:>14}", end="")
    print()

    coupling_2pt = {}
    for a1 in integer_alphas:
        print(f"    {integer_names[a1]:>14}", end="")
        for a2 in integer_alphas:
            P1 = projectors[a1]
            P2 = projectors[a2]
            m1 = len(eig_sectors[a1])
            m2 = len(eig_sectors[a2])
            # Two-point coupling through A^2
            c = np.trace(P1 @ A2 @ P2) / np.sqrt(m1 * m2)
            coupling_2pt[(a1, a2)] = c
            print(f" {c:14.4f}", end="")
        print()

    # Three-point coupling (vertex structure)
    print(f"\n[3] THREE-POINT COUPLINGS (3-vertex interaction amplitudes)")
    print(f"    Normalised by sector dimensions.\n")

    three_pt = {}
    for i, a1 in enumerate(integer_alphas):
        for j, a2 in enumerate(integer_alphas):
            if j < i:
                continue
            for k, a3 in enumerate(integer_alphas):
                if k < j:
                    continue
                P1 = projectors[a1]
                P2 = projectors[a2]
                P3 = projectors[a3]
                m1 = len(eig_sectors[a1])
                m2 = len(eig_sectors[a2])
                m3 = len(eig_sectors[a3])
                # Three-point: Tr(P1 A P2 A P3)
                c = np.trace(P1 @ A @ P2 @ A @ P3) / (m1 * m2 * m3) ** (1/3)
                three_pt[(a1, a2, a3)] = c
                if abs(c) > 0.01:
                    n1 = integer_names[a1]
                    n2 = integer_names[a2]
                    n3 = integer_names[a3]
                    print(f"    C({n1}, {n2}, {n3}) = {c:.6f}")

    # Coupling ratios
    print(f"\n[4] COUPLING RATIOS BETWEEN SECTORS")

    # The physically relevant couplings are:
    # gauge-matter-matter vertices (how gauge bosons couple to matter)
    # In the SM, the gauge sector would be in one eigenvalue sector
    # and matter in others.

    # Self-coupling ratios
    diag_couplings = [(a, coupling_2pt[(a, a)]) for a in integer_alphas]
    if diag_couplings[0][1] != 0:
        print(f"    Diagonal (self-coupling) ratios relative to λ=9:")
        ref = abs(diag_couplings[0][1])
        for a, c in diag_couplings:
            ratio = abs(c) / ref if ref > 0 else 0
            print(f"      {integer_names[a]:>14}: {ratio:.6f}")

    # Off-diagonal ratios
    print(f"\n    Off-diagonal coupling ratios:")
    off_diag = []
    for a1 in integer_alphas:
        for a2 in integer_alphas:
            if a1 >= a2:
                continue
            c = abs(coupling_2pt[(a1, a2)])
            if c > 0.001:
                off_diag.append((a1, a2, c))
                print(f"      {integer_names[a1]} ↔ {integer_names[a2]}: {c:.6f}")

    if len(off_diag) >= 2:
        ref = off_diag[0][2]
        print(f"\n    Ratio structure (normalised to first):")
        for a1, a2, c in off_diag:
            print(f"      {integer_names[a1]} ↔ {integer_names[a2]}: {c/ref:.6f}")

    # ================================================================
    print(f"\n{'='*70}")
    print("PART 2: UV FINITENESS (Gap 5)")
    print(f"{'='*70}")

    print(f"\n[5] MODE COUNT BY SECTOR")
    total_modes = 0
    integer_modes = 0
    irrational_modes = 0

    print(f"\n    {'Sector':>14} {'alpha':>8} {'lambda':>8} {'mult':>6} {'type':>10}")
    print(f"    {'-'*50}")

    for alpha in sorted(eig_sectors.keys(), reverse=True):
        lam = 12 - alpha
        mult = len(eig_sectors[alpha])
        is_int = abs(lam - round(lam)) < 0.01
        total_modes += mult
        if is_int:
            integer_modes += mult
            label = "INTEGER"
        else:
            irrational_modes += mult
            label = "irrational"
        print(f"    {'':>14} {alpha:8.2f} {lam:8.2f} {mult:6d} {label:>10}")

    print(f"\n    Total modes:       {total_modes}")
    print(f"    Integer sector:    {integer_modes}")
    print(f"    Irrational sector: {irrational_modes}")

    print(f"\n[6] EFFECTIVE HAMILTONIAN DIMENSION")
    print(f"    The Witten Hamiltonian in the tight-binding approximation")
    print(f"    is a {total_modes}×{total_modes} matrix (full 600-cell).")
    print(f"    Restricted to the physical (integer) sector:")
    print(f"    it is a {integer_modes}×{integer_modes} matrix.")
    print(f"")
    print(f"    This is FINITE-DIMENSIONAL.")
    print(f"    No UV divergence is possible in the target-space sector.")

    # Build the effective Hamiltonian on the integer sector
    int_indices = []
    for alpha in sorted(eig_sectors.keys(), reverse=True):
        lam = 12 - alpha
        if abs(lam - round(lam)) < 0.01:
            int_indices.extend(eig_sectors[alpha])

    int_indices = sorted(int_indices)
    H_int = A[np.ix_(int_indices, int_indices)]

    # Actually we should use the eigenvector projection
    # The physical-sector effective Hamiltonian in the eigenbasis
    # is block-diagonal with eigenvalues {12, 3, 0, -2, -3}
    print(f"\n[7] PHYSICAL-SECTOR EFFECTIVE HAMILTONIAN")

    # Project A onto the integer eigenspaces
    P_int = np.zeros((120, 120))
    for alpha in sorted(eig_sectors.keys(), reverse=True):
        lam = 12 - alpha
        if abs(lam - round(lam)) < 0.01:
            P_int += projectors[alpha]

    H_phys = P_int @ A @ P_int
    H_phys_eigs = np.linalg.eigvalsh(H_phys)
    nonzero_eigs = H_phys_eigs[np.abs(H_phys_eigs) > 0.01]

    print(f"    Projected Hamiltonian eigenvalues (nonzero):")
    eig_counts = Counter(np.round(nonzero_eigs, 2))
    for ev in sorted(eig_counts.keys(), reverse=True):
        lam = 12 - ev
        print(f"      alpha = {ev:8.2f} (lambda = {lam:8.2f}): multiplicity {eig_counts[ev]}")

    print(f"\n    Physical-sector Hilbert space dimension: {integer_modes}")
    print(f"    Number of distinct energy levels: {len(eig_counts)}")
    print(f"    Rank of H_phys: {np.linalg.matrix_rank(H_phys, tol=0.01)}")

    print(f"\n[8] UV FINITENESS ARGUMENT")
    print(f"""
    The 600-cell target-space theory has exactly {total_modes} modes.
    The physical (integer) sector has {integer_modes} modes.
    The effective Hamiltonian is a finite {integer_modes}×{integer_modes} matrix.

    Consequences for UV structure:
    1. TARGET-SPACE UV: automatically finite ({integer_modes} modes, no continuum limit).
    2. SPATIAL UV: requires separate treatment. If the spatial dimensions
       emerge from the closure manifold (Papers IX-X), they may also be
       finite. If not, standard spatial UV renormalisation is needed.
    3. TOTAL UV: if both target and spatial dimensions are closure-derived,
       the total mode count is finite and the theory is UV-complete.

    The 600-cell provides a natural UV cutoff for the target-space sector.
    The highest eigenvalue (lambda = {12 - min(eig_sectors.keys()):.2f})
    sets the maximum target-space energy scale.
    """)

    # Spectral gap structure
    print(f"[9] SPECTRAL GAP STRUCTURE")
    sorted_lambdas = sorted(set(round(12 - a, 4) for a in eig_sectors.keys()))
    print(f"    Laplacian eigenvalues: {sorted_lambdas}")
    print(f"    Gaps between consecutive eigenvalues:")
    for i in range(1, len(sorted_lambdas)):
        gap = sorted_lambdas[i] - sorted_lambdas[i-1]
        is_int_pair = (abs(sorted_lambdas[i] - round(sorted_lambdas[i])) < 0.01 and
                       abs(sorted_lambdas[i-1] - round(sorted_lambdas[i-1])) < 0.01)
        marker = " [integer pair]" if is_int_pair else ""
        print(f"      {sorted_lambdas[i-1]:.4f} -> {sorted_lambdas[i]:.4f}: "
              f"gap = {gap:.4f}{marker}")

    # The largest gap in the integer sector
    int_lambdas = sorted(l for l in sorted_lambdas if abs(l - round(l)) < 0.01)
    int_gaps = [int_lambdas[i+1] - int_lambdas[i] for i in range(len(int_lambdas)-1)]
    if int_gaps:
        print(f"\n    Integer-sector eigenvalues: {int_lambdas}")
        print(f"    Integer-sector gaps: {int_gaps}")
        print(f"    Largest gap: {max(int_gaps)} (between λ={int_lambdas[int_gaps.index(max(int_gaps))]} "
              f"and λ={int_lambdas[int_gaps.index(max(int_gaps))+1]})")

    print(f"\n{'='*70}")
    print("COMPUTATION COMPLETE")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
