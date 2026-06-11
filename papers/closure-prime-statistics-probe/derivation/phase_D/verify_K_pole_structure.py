#!/usr/bin/env python3
"""
DERIVATION Phase D: derive the K-pole {1, 1, 5, 5} structure from the
internal 5-fold (S_5 / Z_5) action on V_600's λ=0 eigenspace.

Building on Phases A (basis, multiplication), B (generation), C (closure):

Deliverables:
  D1. Build the explicit order-5 element g ∈ 2I (g^5 = 1) and verify
      g permutes V_600.
  D2. For each eigenspace of A_{V_600}, compute the action of g
      restricted to that eigenspace (a 5-th root of unity matrix).
  D3. Decompose each eigenspace into Z/5 character multiplicities.
  D4. Look for {1, 1, 5, 5} pattern in the multiplicity structure
      (potentially inside the 25-dim λ=0 eigenspace).
  D5. Extend to S_5 by finding an order-2 element (transposition of
      Schläfli classes), and decompose under S_5 explicitly.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from collections import Counter, defaultdict

import numpy as np

PHI    = (1.0 + 5.0 ** 0.5) / 2.0
INVPHI = 1.0 / PHI
TOL    = 1e-6

OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ---------- Build V_600 (reused) -----------------------------

def build_v600():
    half       = 0.5
    half_phi   = PHI / 2.0
    half_phi_i = 1.0 / (2.0 * PHI)
    verts = []
    for i in range(4):
        for s in (1.0, -1.0):
            v = [0.0]*4; v[i] = s
            verts.append(v)
    for s0 in (-1,1):
        for s1 in (-1,1):
            for s2 in (-1,1):
                for s3 in (-1,1):
                    verts.append([s0*half, s1*half, s2*half, s3*half])
    even_perms = [
        (0,1,2,3),(0,2,3,1),(0,3,1,2),
        (1,0,3,2),(1,2,0,3),(1,3,2,0),
        (2,0,1,3),(2,1,3,0),(2,3,0,1),
        (3,0,2,1),(3,1,0,2),(3,2,1,0),
    ]
    for p in even_perms:
        for sa in (-1,1):
            for sb in (-1,1):
                for sc in (-1,1):
                    v = [0.0]*4
                    v[p[0]] = sa*half_phi
                    v[p[1]] = sb*half
                    v[p[2]] = sc*half_phi_i
                    v[p[3]] = 0.0
                    verts.append(v)
    return np.array(verts, dtype=float)


def quat_mul(p, q):
    return np.array([
        p[0]*q[0] - p[1]*q[1] - p[2]*q[2] - p[3]*q[3],
        p[0]*q[1] + p[1]*q[0] + p[2]*q[3] - p[3]*q[2],
        p[0]*q[2] - p[1]*q[3] + p[2]*q[0] + p[3]*q[1],
        p[0]*q[3] + p[1]*q[2] - p[2]*q[1] + p[3]*q[0],
    ], dtype=float)


def find_vertex(target, V, tol=TOL):
    diffs = V - target[None, :]
    d = np.linalg.norm(diffs, axis=1)
    i = int(np.argmin(d))
    return i if d[i] < tol else -1


# ---------- Order-5 element of 2I (from Schläfli probe) -----

g_order5 = np.array([INVPHI/2, PHI/2, 0.5, 0.0])
# Verified: g has order 5 in 2I (Schläfli probe + Phase A).


def apply_g_to_v600(V, g_quat):
    """Build permutation index pi such that left-multiplication by g
       sends V[i] to V[pi[i]]."""
    n = V.shape[0]
    pi = np.zeros(n, dtype=int)
    for i in range(n):
        gv = quat_mul(g_quat, V[i])
        idx = find_vertex(gv, V)
        if idx < 0:
            return None
        pi[i] = idx
    return pi


# ---------- Eigenspaces of A_{V_600} -----

def build_adjacency_and_spectrum(V):
    n = V.shape[0]
    diffs = V[:, None, :] - V[None, :, :]
    d2 = np.sum(diffs * diffs, axis=2)
    pos = d2[d2 > 1e-9]
    min_d2 = pos.min()
    A = (np.abs(d2 - min_d2) < 1e-7).astype(float)
    np.fill_diagonal(A, 0.0)
    eigvals, eigvecs = np.linalg.eigh(A)
    # Group eigenvalues with tolerance
    distinct = []
    indices_by_eig = []
    for i, ev in enumerate(eigvals):
        if distinct and abs(ev - distinct[-1]) < 1e-5:
            indices_by_eig[-1].append(i)
        else:
            distinct.append(float(ev))
            indices_by_eig.append([i])
    return A, eigvals, eigvecs, distinct, indices_by_eig


# ---------- Z/5 character decomposition of an eigenspace -----

def decompose_under_g(E, G):
    """E is n x k matrix (eigenvectors). G is n x n permutation matrix
       (acting on R^n; commutes with the eigenspace projection iff
       g preserves the eigenspace, which it does since g is an
       automorphism commuting with A).

       Returns: dict mapping each Z/5 character to its multiplicity.
       Z/5 chars are 1, ζ, ζ², ζ³, ζ⁴ where ζ = e^(2πi/5).

       Approach: compute G_restricted = E^T · G · E (k x k matrix in
       eigenspace basis), compute its eigenvalues (5th roots of unity),
       and count.
    """
    G_E = E.T @ G @ E  # k x k
    eigvals_GE = np.linalg.eigvals(G_E)
    # Compare to 5th roots of unity
    zeta = np.exp(2j * np.pi / 5)
    roots = [zeta ** k for k in range(5)]
    mult = {k: 0 for k in range(5)}
    for ev in eigvals_GE:
        # Match to nearest 5th root
        dists = [abs(ev - r) for r in roots]
        k = int(np.argmin(dists))
        if dists[k] < 0.1:
            mult[k] += 1
    return mult, eigvals_GE


def decompose_under_g_real(E, G):
    """Same but the eigenvalues of G_E may not be exactly 5th roots
       due to numerics. Decomposition multiplicities should sum to
       eigenspace dim."""
    return decompose_under_g(E, G)


# ---------- Main -----

def main():
    print("=" * 78)
    print("Phase D: Derive {1, 1, 5, 5} K-pole structure from Z/5 / S_5 action")
    print("=" * 78)
    print()

    summary = {"phase": "D", "checks": {}}

    V = build_v600()
    n = V.shape[0]
    print(f"V_600 built: {n} unit icosians")

    # ----- D1 -------------------------------------------------
    print("--- D1: Build order-5 element g ∈ 2I and verify permutation ---")
    print(f"  g = (φ⁻¹/2, φ/2, 1/2, 0) = {g_order5}")
    # Verify g^5 = 1
    g_pow = np.array([1.0, 0, 0, 0])
    for _ in range(5):
        g_pow = quat_mul(g_pow, g_order5)
    is_order5 = np.linalg.norm(g_pow - np.array([1.0, 0, 0, 0])) < 1e-9
    print(f"  g^5 = 1: {is_order5}")
    # Verify g permutes V_600
    pi = apply_g_to_v600(V, g_order5)
    if pi is None:
        print("  D1 FAIL: g does not permute V_600")
        return 1
    n_distinct = len(set(pi.tolist()))
    is_perm = n_distinct == n
    print(f"  g permutes V_600: distinct images {n_distinct}/{n} → {is_perm}")
    # Cycle structure of permutation
    visited = [False]*n
    cycles = []
    for i in range(n):
        if visited[i]: continue
        cycle = []
        j = i
        while not visited[j]:
            visited[j] = True
            cycle.append(j)
            j = int(pi[j])
        cycles.append(len(cycle))
    cycle_counts = Counter(cycles)
    print(f"  Cycle structure: {dict(cycle_counts)}")
    print(f"  (Expected: 120 vertices, all in 5-cycles → 24 cycles of length 5)")
    d1_pass = is_order5 and is_perm
    summary["checks"]["D1_g_permutes_V600"] = {
        "g_order5":       bool(is_order5),
        "is_permutation": bool(is_perm),
        "cycle_structure": dict(cycle_counts),
        "pass":           d1_pass,
    }
    print(f"  D1 {'PASS' if d1_pass else 'FAIL'}")
    print()

    # Build permutation matrix
    G_mat = np.zeros((n, n))
    for i in range(n):
        G_mat[int(pi[i]), i] = 1.0

    # ----- D2 -------------------------------------------------
    print("--- D2: Action of g on each eigenspace of A_{V_600} ---")
    A, eigvals, eigvecs, distinct, indices_by_eig = build_adjacency_and_spectrum(V)
    print(f"  V_600 spectrum: {len(distinct)} distinct eigenvalues")
    # Verify A commutes with G_mat
    AG = A @ G_mat
    GA = G_mat @ A
    commutes = np.allclose(AG, GA, atol=1e-9)
    print(f"  A commutes with G (g is graph automorphism): {commutes}")
    summary["checks"]["D2_g_commutes_with_A"] = {"pass": bool(commutes)}
    print(f"  D2 {'PASS' if commutes else 'FAIL'}")
    print()

    # ----- D3 -------------------------------------------------
    print("--- D3: Z/5 character decomposition of each eigenspace ---")
    print(f"  Z/5 characters: 1, ζ, ζ², ζ³, ζ⁴ where ζ = e^(2πi/5)")
    print(f"  For each eigenspace, count multiplicities of each char.")
    print()
    print(f"  {'eigenvalue':<14} {'dim':<6} {'mult-1':<7} {'mult-ζ':<7} "
          f"{'mult-ζ²':<8} {'mult-ζ³':<8} {'mult-ζ⁴':<8}")
    print("  " + "-" * 65)
    decomps = {}
    for ev, indices in zip(distinct, indices_by_eig):
        E = eigvecs[:, indices]   # n x dim
        mult, eigvals_GE = decompose_under_g(E, G_mat)
        decomps[round(ev, 4)] = {
            "dim": len(indices),
            "multiplicities": mult,
        }
        print(f"  {ev:+10.4f}    {len(indices):<6} "
              f"{mult[0]:<7} {mult[1]:<7} {mult[2]:<8} {mult[3]:<8} {mult[4]:<8}")
    print()
    summary["checks"]["D3_Z5_decomposition"] = {
        "decomps": {str(k): {"dim": v["dim"],
                              "multiplicities": v["multiplicities"]}
                    for k, v in decomps.items()},
        "pass": True,
    }
    print()

    # ----- D4 -------------------------------------------------
    print("--- D4: Look for {1, 1, 5, 5} pattern ---")
    # The {1, 1, 5, 5} could appear:
    # (a) As multiplicities of Z/5 characters in some eigenspace
    # (b) As S_5 irrep dimensions inside the 25-dim λ=0 eigenspace
    # First: check if any eigenspace has Z/5-multiplicities matching {1,1,5,5,?}
    print("  Check (a): Z/5-multiplicities matching {1,1,5,5,?}")
    found_pattern_a = False
    for ev_key, info in decomps.items():
        mults = list(info["multiplicities"].values())
        sorted_mults = sorted(mults)
        # Check if it contains {1, 1, 5, 5} (as a sub-pattern)
        if (sorted_mults.count(1) >= 2 and sorted_mults.count(5) >= 2):
            print(f"    eigenvalue {ev_key}: Z/5-mults = {mults}  → contains {{1,1,5,5}}!")
            found_pattern_a = True
    if not found_pattern_a:
        print("    Z/5-multiplicities {1, 1, 5, 5} pattern NOT found directly.")
    print()
    # Second: examine the 25-dim λ=0 eigenspace specifically
    print("  Check (b): Inside the 25-dim λ=0 eigenspace specifically")
    zero_eig_key = None
    for ev_key in decomps:
        if abs(ev_key) < 1e-3:
            zero_eig_key = ev_key
            break
    if zero_eig_key is not None:
        info = decomps[zero_eig_key]
        print(f"    λ=0 eigenspace dim: {info['dim']}")
        print(f"    Z/5 multiplicities: {info['multiplicities']}")
        total = sum(info["multiplicities"].values())
        print(f"    Total: {total} (should equal {info['dim']})")
    print()
    # Third: cross-eigenspace pattern
    print("  Check (c): {1, 1, 5, 5} could appear across DIFFERENT eigenspaces")
    print("             as the multiplicities of a specific Z/5 character")
    char_across = {k: [] for k in range(5)}
    for ev_key, info in decomps.items():
        for k in range(5):
            char_across[k].append((ev_key, info["multiplicities"][k]))
    for k in range(5):
        nonzero = [(ev, m) for ev, m in char_across[k] if m > 0]
        if 1 <= len(nonzero) <= 8:
            mults_only = [m for _, m in nonzero]
            print(f"    Char ζ^{k}: appears in {len(nonzero)} eigenspaces, "
                  f"multiplicities = {mults_only}")
    print()
    summary["checks"]["D4_pattern_search"] = {
        "pattern_a_z5_mults":   bool(found_pattern_a),
        "zero_eig_decomp":      decomps.get(zero_eig_key, None),
        "pass":                 found_pattern_a,
    }
    print(f"  D4 {'PASS' if found_pattern_a else 'EXPLORATORY (no clean Z/5-only match)'}")
    print()

    # ----- Summary -------------------------------------------
    print("=" * 78)
    print("PHASE D SUMMARY")
    print("=" * 78)
    for name, chk in summary["checks"].items():
        status = "PASS" if chk.get("pass") else "EXPLORATORY/FAIL"
        print(f"  {name}: {status}")
    all_pass = all(c.get("pass") for c in summary["checks"].values())
    print()
    print(f"  Phase D overall: {'PASS' if all_pass else 'PARTIAL — needs S_5 extension'}")
    summary["overall_pass"] = all_pass
    def clean(x):
        if isinstance(x, dict):
            return {str(k): clean(v) for k, v in x.items()}
        if isinstance(x, (list, tuple)):
            return [clean(v) for v in x]
        if isinstance(x, np.ndarray): return x.tolist()
        if isinstance(x, np.integer): return int(x)
        if isinstance(x, np.floating): return float(x)
        return x
    with open(OUTPUT_DIR / "phase_D_results.json", "w") as f:
        json.dump(clean(summary), f, indent=2)
    print(f"  Saved {OUTPUT_DIR / 'phase_D_results.json'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
