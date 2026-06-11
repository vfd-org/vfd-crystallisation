#!/usr/bin/env python3
"""
Pure-VFD test of the σ-attractor hypothesis for cascade-RH.

The cascade-RH bridge in attractor form (user reformulation 2026-04-25):
  primes are basin attractors of σ-equivariant cascade closure dynamics;
  their Mellin shadow zeros lie on Re(s) = 1/2 because the σ-fixed locus
  of the Mellin involution s ↦ 1-s IS the critical line.

The bridge reduces to a single sim-testable claim:
  H_attr: the basin attractors of cascade closure dynamics on 2I are
          σ-isolated (each individually σ-fixed, not in non-trivial
          σ-orbits of length 2).

This script tests a strong sufficient condition for H_attr:
  Q1: how much of the 600-cell adjacency Laplacian spectrum is σ-fixed
      (i.e., eigenvalues in Q ⊂ Q(φ))?
  Q2: are the σ-fixed eigenvalues' eigenvectors supported on 2T (the
      24-point σ-fixed vertex set), confirming the attractor location?

If Q1 shows substantial σ-fixed spectral content AND Q2 shows σ-fixed
eigenvectors localised on 2T, the σ-attractor bridge has cascade-internal
empirical support.  If not, we know which sub-conjecture fails and where.

Refuses floats. Exact Q(√5) Fraction arithmetic for adjacency; numpy for
eigendecomposition (where exact arithmetic is unwieldy).
"""

from __future__ import annotations

import sys
from pathlib import Path
from collections import defaultdict, Counter
import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
sys.path.insert(0, str(REPO_ROOT / "papers" / "paper-xxii" / "scripts"))

from run_icosian_exact import (  # noqa: E402
    q_zero, q_one, qq_eq, qq_key,
    build_vertices, vertex_index_map,
    qq_distance_sq,
)

PHI = (1 + np.sqrt(5)) / 2


def sigma_pair(x):
    return (x[0], -x[1])


def sigma_on_quat(q):
    return tuple(sigma_pair(c) for c in q)


def identify_sigma_fixed(verts):
    """Return set of vertex indices i with σ(verts[i]) = verts[i]."""
    fixed = set()
    for i, v in enumerate(verts):
        if qq_eq(sigma_on_quat(v), v):
            fixed.add(i)
    return fixed


def build_adjacency(verts):
    """Build the 12-regular adjacency matrix of the 600-cell."""
    n = len(verts)
    # Find nearest-neighbour squared distance
    min_d = None
    for j in range(1, n):
        d = qq_distance_sq(verts[0], verts[j])
        if min_d is None:
            min_d = d
        else:
            cur_real = float(min_d[0]) + float(min_d[1]) * (5 ** 0.5)
            new_real = float(d[0]) + float(d[1]) * (5 ** 0.5)
            if new_real < cur_real - 1e-12:
                min_d = d
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j and qq_distance_sq(verts[i], verts[j]) == min_d:
                A[i, j] = 1.0
    return A


def is_q_rational(x, tol=1e-8):
    """Heuristic: is x rational (vs in Q(φ)\Q)?
    A value in Q(φ) has the form a + b φ; it is in Q iff b ≈ 0.
    We detect this by checking whether x is well-approximated by a
    small rational."""
    # Use continued-fraction expansion: x is rational iff the CF
    # terminates within reasonable precision.  Heuristic: round to
    # nearest fraction with denominator ≤ 10000 and check residual.
    from fractions import Fraction
    f = Fraction(x).limit_denominator(10000)
    if abs(float(f) - x) < tol:
        return True
    # Also accept if x is a near-integer or simple sqrt-5 multiple
    if abs(x - round(x)) < tol:
        return True
    return False


def classify_eigenvalue_sigma(lam, tol=1e-6):
    """Classify eigenvalue λ in Q(φ) as σ-fixed (rational) or σ-paired
    (truly in Q(φ)\Q).  σ acts as φ → -1/φ, so σ(a + bφ) = a - b - bφ
    = a - b(1+φ) = a - bφ². For real eigenvalues, σ-fixed means b = 0.
    """
    # Fit λ ≈ a + b·φ for a, b small rationals
    # Strategy: try to express λ as a + b·φ with a, b rationals of
    # bounded denominator
    from fractions import Fraction
    # Search small rationals b such that (λ - b·φ) is rational
    best = None
    for b_num in range(-200, 201):
        for b_den in [1, 2, 3, 4, 5, 6]:
            b = Fraction(b_num, b_den)
            a_approx = lam - float(b) * PHI
            a = Fraction(a_approx).limit_denominator(2000)
            residual = abs(lam - float(a) - float(b) * PHI)
            if residual < tol:
                if best is None or residual < best[2]:
                    best = (a, b, residual)
    if best is None:
        return ("unknown", lam, None, None)
    a, b, res = best
    if b == 0:
        return ("σ-fixed", lam, a, b)
    else:
        # σ(a + bφ) = a - b - bφ = (a-b) + (-b)·φ — distinct from λ
        # unless 2b = 0, which contradicts b ≠ 0
        return ("σ-paired", lam, a, b)


def main():
    print("=" * 76)
    print("σ-ATTRACTOR SPECTRAL TEST")
    print("Pure VFD test of cascade-RH bridge in attractor form.")
    print("Q1: σ-fixed fraction of 600-cell Laplacian spectrum?")
    print("Q2: σ-fixed eigenvectors localised on 2T (σ-fixed vertex set)?")
    print("=" * 76)

    # --- Build 2I and 2T ---
    print("\n[Setup] Build 2I (120 vertices) and 2T (24 σ-fixed)...")
    verts = build_vertices()
    sigma_fixed_verts = identify_sigma_fixed(verts)
    print(f"        |2I| = {len(verts)}, |2T| = {len(sigma_fixed_verts)}")

    # --- Build adjacency Laplacian L = D - A ---
    print("\n[Setup] Build 600-cell adjacency Laplacian L = D - A...")
    A = build_adjacency(verts)
    D = np.diag(A.sum(axis=1))
    L = D - A
    print(f"        L: {L.shape}, edges = {int(A.sum() / 2)}, "
          f"degree = {int(A.sum(axis=1).max())}")

    # --- Eigendecomposition ---
    print("\n[Step 1] Compute eigendecomposition of L...")
    eigs, vecs = np.linalg.eigh(L)
    print(f"        spectrum range: [{eigs[0]:.6f}, {eigs[-1]:.6f}]")
    print(f"        first 10 eigenvalues:")
    for i in range(10):
        print(f"          λ_{i} = {eigs[i]:.10f}")

    # --- Classify each eigenvalue σ-fixed vs σ-paired ---
    print("\n[Step 2] Classify each eigenvalue (σ-fixed vs σ-paired)...")
    classifications = []
    for lam in eigs:
        cls = classify_eigenvalue_sigma(lam)
        classifications.append(cls)

    fixed_count = sum(1 for c in classifications if c[0] == "σ-fixed")
    paired_count = sum(1 for c in classifications if c[0] == "σ-paired")
    unknown_count = sum(1 for c in classifications if c[0] == "unknown")
    print(f"        σ-fixed eigenvalues:  {fixed_count}/{len(eigs)} "
          f"= {fixed_count/len(eigs):.1%}")
    print(f"        σ-paired eigenvalues: {paired_count}/{len(eigs)} "
          f"= {paired_count/len(eigs):.1%}")
    print(f"        unclassified:          {unknown_count}/{len(eigs)}")

    # --- Distinct eigenvalue spectrum ---
    print("\n[Step 3] Distinct eigenvalue spectrum (modulo numerical "
          "degeneracy):")
    distinct = []
    seen = []
    for i, lam in enumerate(eigs):
        if not any(abs(lam - s) < 1e-6 for s in seen):
            seen.append(lam)
            mult = sum(1 for x in eigs if abs(x - lam) < 1e-6)
            cls = classifications[i][0]
            distinct.append((lam, mult, cls))
    print(f"        distinct eigenvalues: {len(distinct)}")
    print(f"        spectrum:")
    for lam, mult, cls in distinct:
        # Express as a + b·φ
        c = classify_eigenvalue_sigma(lam)
        if c[0] != "unknown":
            a, b = c[2], c[3]
            sym = f"{a}" if b == 0 else f"{a} + ({b})·φ"
            print(f"          λ = {lam:13.6f}  mult={mult:3d}  "
                  f"[{cls:10s}]  ≈ {sym}")
        else:
            print(f"          λ = {lam:13.6f}  mult={mult:3d}  "
                  f"[{cls:10s}]  unrecognised")

    # --- Q2: Localisation of σ-fixed eigenvectors on 2T ---
    print("\n[Step 4] σ-fixed eigenvector localisation on 2T...")
    sigma_fixed_indices = sorted(sigma_fixed_verts)
    sigma_paired_indices = [i for i in range(120) if i not in sigma_fixed_verts]

    n_fixed_eig = 0
    total_2T_mass = 0.0
    total_complement_mass = 0.0
    for i, (cls, lam, _, _) in enumerate(classifications):
        if cls == "σ-fixed":
            n_fixed_eig += 1
            v = vecs[:, i]
            # Mass on 2T (σ-fixed vertices)
            mass_2T = np.sum(v[sigma_fixed_indices] ** 2)
            mass_complement = np.sum(v[sigma_paired_indices] ** 2)
            total_2T_mass += mass_2T
            total_complement_mass += mass_complement

    if n_fixed_eig > 0:
        avg_2T = total_2T_mass / n_fixed_eig
        avg_comp = total_complement_mass / n_fixed_eig
        # Baseline: random vector concentrates 24/120 = 20% mass on 2T
        baseline = len(sigma_fixed_verts) / len(verts)
        print(f"        avg σ-fixed eigvec |·|² mass on 2T:  {avg_2T:.4f}")
        print(f"        avg σ-fixed eigvec |·|² mass on 2I\\2T: {avg_comp:.4f}")
        print(f"        baseline (random vector):              {baseline:.4f}")
        if avg_2T > baseline * 1.5:
            print(f"        ** σ-fixed eigvecs LOCALISE on 2T "
                  f"({avg_2T/baseline:.2f}× baseline) **")
        elif avg_2T > baseline * 1.1:
            print(f"        σ-fixed eigvecs MILDLY localise on 2T "
                  f"({avg_2T/baseline:.2f}× baseline)")
        else:
            print(f"        σ-fixed eigvecs DO NOT localise on 2T "
                  f"({avg_2T/baseline:.2f}× baseline)")

    # --- Verdict ---
    print()
    print("=" * 76)
    print("VERDICT — pure VFD σ-attractor spectral test:")
    print()
    print(f"  Q1 σ-fixed fraction:  {fixed_count}/{len(eigs)} = "
          f"{fixed_count/len(eigs):.1%}  (target ≥ 50% for strong support)")
    if n_fixed_eig > 0:
        print(f"  Q2 2T-localisation:   {avg_2T:.3f} vs baseline "
              f"{len(sigma_fixed_verts)/len(verts):.3f}  "
              f"(target ≥ 1.5× baseline)")
    print()
    if fixed_count / len(eigs) >= 0.5:
        print("  Spectral count: majority of the 600-cell adjacency Laplacian")
        print("  spectrum is σ-fixed (rational eigenvalues).  This is a finite")
        print("  spectral diagnostic only; conversion to a critical-line Mellin-")
        print("  shadow zero claim requires the additional spectral-mode → Mellin-")
        print("  zero correspondence (Conjecture conj:spec_to_zero in rh-formal),")
        print("  which is not established by this script.")
    elif fixed_count / len(eigs) >= 0.3:
        print("  PARTIAL support: significant σ-fixed spectral content.")
        print("  σ-paired modes need additional dynamical suppression argument")
        print("  (closure flow stability of σ-fixed states vs σ-paired orbits).")
    else:
        print("  WEAK direct support from spectrum alone: most eigenvalues are")
        print("  σ-paired (in Q(φ)\\Q).  σ-fixity of basin attractors then must")
        print("  rely on dynamical selection (closure flow drives toward σ-fixed)")
        print("  rather than spectral confinement.")
    print("=" * 76)


if __name__ == "__main__":
    main()
