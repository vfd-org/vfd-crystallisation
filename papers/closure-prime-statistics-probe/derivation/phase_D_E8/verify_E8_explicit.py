#!/usr/bin/env python3
"""
DERIVATION Phase D-E8: explicitly verify (or refute) the cascade → E_8
connection by building 240 minimal vectors of E_8 via the icosian
construction and looking for an explicit {1, 1, 5, 5} stratification.

This addresses a hostile-reviewer critique: the earlier claim
"240 = |E_8| therefore ẑ poles ↔ E_8 roots" is numerology unless an
EXPLICIT map is constructed.

Two routes attempted:

Route 1 — Standard E_8 minimal-vector enumeration (240 vectors in R^8).
  Apply a 5-fold rotation (icosian g acting diagonally on R^8 = R^4 ⊕ R^4).
  Compute orbit structure.  Look for {1, 1, 5, 5} stratification by
  some natural coordinate.

Route 2 — Icosian-flavour E_8: 𝓘 itself as a rank-8 Z-lattice with
  the "twisted" form B_E8(α, β) = Tr(α · conj(β)).  Minimal vectors
  of this form correspond to α ∈ 𝓘 with Tr(N(α)) = 2.  These are
  the 120 units (N=1) + 120 elements with N=2φ = 240.  Apply g·,
  examine orbit structure.

The probe reports HONESTLY: if no explicit {1, 1, 5, 5} morphism
emerges, the E_8 claim is downgraded.
"""

from __future__ import annotations

import json
import math
import sys
from itertools import combinations, product
from pathlib import Path
from collections import Counter, defaultdict

import numpy as np

PHI    = (1.0 + 5.0 ** 0.5) / 2.0
INVPHI = 1.0 / PHI
TOL    = 1e-7

OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# E_8 minimal vectors via the standard ("D_8 + half-integers") construction
# ============================================================

def build_e8_minimal_vectors():
    """E_8 has 240 minimal vectors of norm² = 2:
       - 112 of the form (±1, ±1, 0, 0, 0, 0, 0, 0) permutations
       - 128 of the form (±1/2)^8 with EVEN number of minus signs
    """
    vecs = []
    # Type 1: 112 vectors (±1, ±1, 0, 0, 0, 0, 0, 0)
    for i, j in combinations(range(8), 2):
        for si, sj in product((-1, 1), repeat=2):
            v = [0]*8
            v[i] = si
            v[j] = sj
            vecs.append(v)
    # Type 2: 128 vectors (±1/2)^8 with even sign parity
    for sm in range(256):
        signs = [(-1 if (sm >> k) & 1 else 1) for k in range(8)]
        n_minus = sum(1 for s in signs if s == -1)
        if n_minus % 2 == 0:
            vecs.append([s * 0.5 for s in signs])
    return np.array(vecs, dtype=float)


# ============================================================
# Icosian quaternions (V_600) → embedded E_8 representation
# ============================================================

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


# ============================================================
# Route 1: E_8 in R^8 with diagonal 5-fold rotation
# ============================================================

def diag_5fold_rotation_R8():
    """Build a 5-fold rotation in R^8 that's the natural cascade action.
       One choice: rotate (x_0..x_3) and (x_4..x_7) each by the icosian
       g acting via left-quaternion multiplication.
    """
    g = np.array([INVPHI/2, PHI/2, 0.5, 0.0])
    # Build the 4x4 SO(4) matrix R_g for left-multiplication by g
    R_g = np.zeros((4, 4))
    for i in range(4):
        ei = np.zeros(4); ei[i] = 1.0
        R_g[:, i] = quat_mul(g, ei)
    # Verify R_g^5 = I
    R_pow = np.eye(4)
    for _ in range(5):
        R_pow = R_g @ R_pow
    assert np.allclose(R_pow, np.eye(4), atol=1e-9), "R_g not order 5"
    # Block-diagonal in R^8
    M = np.zeros((8, 8))
    M[:4, :4] = R_g
    M[4:, 4:] = R_g
    return M


def find_vec_index(target, V, tol=1e-6):
    diffs = V - target[None, :]
    d = np.linalg.norm(diffs, axis=1)
    i = int(np.argmin(d))
    return i if d[i] < tol else -1


def compute_orbits(V, action_matrix, max_order=10):
    """For each vector in V, compute its orbit under repeated application
       of action_matrix.  Return list of orbits (each as list of indices).
    """
    n = V.shape[0]
    visited = [False] * n
    orbits = []
    for i in range(n):
        if visited[i]: continue
        orbit = []
        cur = V[i].copy()
        visited[i] = True
        orbit.append(i)
        for _ in range(max_order - 1):
            cur = action_matrix @ cur
            idx = find_vec_index(cur, V)
            if idx < 0:
                # Doesn't preserve V — abort this orbit
                break
            if idx == orbit[0]:
                break
            visited[idx] = True
            orbit.append(idx)
        orbits.append(orbit)
    return orbits


def main():
    print("=" * 78)
    print("Phase D-E8: explicit E_8 + cascade 5-fold action")
    print("=" * 78)
    print()

    summary = {"phase": "D_E8", "routes": {}}

    # ----- Route 1: standard E_8 in R^8 -----
    print("--- Route 1: standard E_8 minimal vectors with R^8 = R^4 ⊕ R^4 ---")
    E8 = build_e8_minimal_vectors()
    print(f"  Built {E8.shape[0]} minimal vectors (expected 240)")
    norms = np.sum(E8 * E8, axis=1)
    print(f"  All have norm² = 2: {np.allclose(norms, 2.0)}")
    # Compute Type 1 vs Type 2 partition
    n_type1 = sum(1 for v in E8 if any(abs(c) > 0.7 for c in v))
    n_type2 = E8.shape[0] - n_type1
    print(f"  Type 1 ((±1,±1,0,...) perms): {n_type1}")
    print(f"  Type 2 ((±1/2)^8 even parity): {n_type2}")
    print()

    # Apply 5-fold rotation diag(R_g, R_g)
    M = diag_5fold_rotation_R8()
    print(f"  5-fold rotation M = diag(R_g, R_g) where R_g is icosian g")
    print(f"  M^5 = I: {np.allclose(np.linalg.matrix_power(M, 5), np.eye(8), atol=1e-9)}")
    # Check whether M preserves the E_8 set
    n_preserved = 0
    for v in E8:
        if find_vec_index(M @ v, E8) >= 0:
            n_preserved += 1
    print(f"  M preserves E_8 minimal vectors: {n_preserved}/{E8.shape[0]}")
    if n_preserved == 240:
        orbits = compute_orbits(E8, M, max_order=10)
        cycle_lens = Counter(len(o) for o in orbits)
        print(f"  Orbit cycle structure: {dict(cycle_lens)}")
        print(f"  Number of orbits: {len(orbits)}")
    else:
        print(f"  M doesn't preserve standard E_8 — Route 1 partial.")
        orbits = []
        cycle_lens = {}
    print()

    # ----- Route 2: icosian-flavour E_8 -----
    print("--- Route 2: icosian-flavour E_8 = 𝓘 with form Tr(α·conj(α)) ---")
    print()
    print("  E_8 ≅ 𝓘 as Z-module of rank 8.")
    print("  E_8 minimal vectors = {α ∈ 𝓘 : Tr(N(α)) = 2}")
    print()
    print("  Two subsets contribute 120 each:")
    print("    (a) N(α) = 1:   the 120 unit icosians = V_600")
    print("    (b) N(α) = 2φ:  120 icosians with this specific norm")
    print("  Total: 240 = |E_8 minimal vectors|")
    print()
    # Construct (b): find icosians α with reduced norm = 2φ (real value 2φ ≈ 3.236)
    # Build via rank-8 enumeration
    BETA = np.array([
        [1.0,    0.0,        0.0,        0.0],
        [0.0,    1.0,        0.0,        0.0],
        [0.5,    0.5,        0.5,        0.5],
        [PHI/2,  0.5,        1.0/(2*PHI), 0.0],
    ])
    target_norm = 2.0 * PHI   # = 2φ ≈ 3.236
    coefs_arr = np.arange(-2, 3, dtype=float)
    norm2phi_alphas = []
    seen_coords = set()
    for m_idx in product(range(5), repeat=4):
        m_vals = [coefs_arr[i] for i in m_idx]
        ng = np.meshgrid(coefs_arr, coefs_arr, coefs_arr, coefs_arr, indexing='ij')
        n_flat = np.stack([g.flatten() for g in ng], axis=1)
        m_flat = np.broadcast_to(m_vals, n_flat.shape)
        c_real = m_flat + n_flat * PHI
        alphas = c_real @ BETA
        norms = np.sum(alphas * alphas, axis=1)
        for idx in range(len(norms)):
            if abs(norms[idx] - target_norm) < 1e-6:
                key = tuple(np.round(alphas[idx], 5))
                if key not in seen_coords:
                    seen_coords.add(key)
                    norm2phi_alphas.append(alphas[idx].copy())
    n_2phi = len(norm2phi_alphas)
    print(f"  Found {n_2phi} icosians with reduced norm = 2φ")
    print(f"  (Expected 120 if the construction is correct.)")
    print()

    # Combine: 120 V_600 (norm 1) + the norm-2φ set
    V600 = build_v600()
    if n_2phi > 0:
        # Build 240-element set in R^4 (not R^8)
        # We'll examine these together
        norm2phi_arr = np.array(norm2phi_alphas)
        # Apply g action
        g = np.array([INVPHI/2, PHI/2, 0.5, 0.0])

        # For V_600 ∪ {norm-2φ set}: apply g·v
        # Build combined set:
        combined = np.vstack([V600, norm2phi_arr])
        print(f"  Combined set size: {combined.shape[0]} (= |V_600| + |norm-2φ|)")

        # Apply g
        g_action = lambda v: quat_mul(g, v)
        # Check g preserves combined set
        n_preserved_combined = 0
        for v in combined:
            target = g_action(v)
            if find_vec_index(target, combined, tol=1e-6) >= 0:
                n_preserved_combined += 1
        print(f"  g preserves combined set: {n_preserved_combined}/{combined.shape[0]}")
        # Compute orbit structure
        if n_preserved_combined == combined.shape[0]:
            # Build g action as permutation
            pi = np.zeros(combined.shape[0], dtype=int)
            for i, v in enumerate(combined):
                target = g_action(v)
                idx = find_vec_index(target, combined, tol=1e-6)
                pi[i] = idx
            # Orbit structure
            visited = [False] * combined.shape[0]
            orbit_lens = []
            for i in range(combined.shape[0]):
                if visited[i]: continue
                l = 0; j = i
                while not visited[j]:
                    visited[j] = True; l += 1; j = int(pi[j])
                orbit_lens.append(l)
            print(f"  Orbit structure on combined: {dict(Counter(orbit_lens))}")
    else:
        print(f"  Route 2 partial — couldn't find 120 norm-2φ elements with K=2 enumeration.")
        print(f"  Need to extend search or use different basis.")
    print()

    # ----- Attempt explicit K-stratification -----
    print("--- Attempt: K-stratification of E_8 under 5-fold action ---")
    print()
    print("  For each E_8 minimal vector, define K = some discrete cascade-")
    print("  natural invariant.  Look for {1, 1, 5, 5} multiplicity pattern.")
    print()
    # Try: K = number of E_8 vectors in the same g-orbit (= 5 always for length-5 orbits)
    # This is trivial; doesn't give {1, 1, 5, 5}.
    # Try: K = sum of coordinates of a representative.
    if n_preserved == 240:
        # Group E_8 vectors by their orbit representative's "K-coordinate"
        # Define K = orbit's representative's first-coordinate-sign weighted by index
        # This is exploratory.
        orbit_first_coords = []
        for orbit in orbits:
            rep = E8[orbit[0]]
            # K could be many things; try: index of first non-zero coord
            for k in range(8):
                if abs(rep[k]) > 0.1:
                    orbit_first_coords.append(k)
                    break
            else:
                orbit_first_coords.append(-1)
        first_coord_counts = Counter(orbit_first_coords)
        print(f"  Orbit first-non-zero-coord histogram: {dict(first_coord_counts)}")
        print(f"  (Looking for {{1, 1, 5, 5}} pattern — likely not present in this naive grouping)")
    print()

    # ----- HONEST REPORT ON E_8 ↔ {1, 1, 5, 5} -----
    print("=" * 78)
    print("HONEST VERDICT — DOES E_8 ↔ {1, 1, 5, 5} HOLD?")
    print("=" * 78)
    print()
    # Did we find an EXPLICIT bijection?
    route_1_works = (n_preserved == 240)
    found_explicit_K_stratification = False  # we'd need 4 strata with sizes {20, 20, 20, 20}
    # and weights {1, 1, 5, 5}
    if route_1_works and len(orbits) == 48:
        # 48 orbits of length 5 — uniform, not {1,1,5,5}
        # Try to stratify the 48 orbits into 4 groups of 12 — but {1,1,5,5} sums to 12, not 48
        # 240 / (1+1+5+5) = 240/12 = 20 — so 4 strata of 20 vectors each, with
        # multiplicities corresponding to the F1 formula's pole orders.
        # But the natural orbit count is 48, not 4.  The mismatch suggests
        # {1,1,5,5} isn't an orbit-multiplicity structure.
        print("  Route 1: 5-fold rotation gives 48 length-5 orbits (uniform).")
        print("  This does NOT give {1, 1, 5, 5} as orbit multiplicities.")
        print()
    print("  Conclusion: numerical coincidence 20·(1+1+5+5) = 240 = |E_8| holds,")
    print("  but no EXPLICIT morphism (E_8 minimal vector → ẑ pole) has been")
    print("  constructed by this probe.")
    print()
    print("  The E_8 connection remains SUGGESTIVE but not DERIVED.")
    print()
    print("  Honest scope demarcation for Paper A:")
    print("    • V_600 = 120 unit icosians (1/2 of E_8 by Conway-Sloane) — TRUE.")
    print("    • E_8 ≅ 𝓘 as Z-module — TRUE (standard result).")
    print("    • 240 = |E_8| and 20·(1+1+5+5) = 240 — NUMERICAL COINCIDENCE.")
    print("    • Explicit bijection (E_8 root → ẑ pole) commuting with cascade")
    print("      Z/5 and σ-Galois actions — NOT CONSTRUCTED in this probe.")
    print("    • The narrative '{1,1,5,5} are E_8 root multiplicities under")
    print("      cascade 5-fold action' — UNVERIFIED.")
    print()

    summary["honest_verdict"] = {
        "e8_count_matches":   240 == E8.shape[0],
        "numerical_match":    "20·(1+1+5+5) = 240 = |E_8|",
        "explicit_map":       False,
        "route_1_orbits":     dict(cycle_lens),
        "route_1_n_orbits":   len(orbits) if route_1_works else None,
        "K_stratification_found": False,
        "scope_demarcation":  ("Numerical coincidence holds. Explicit morphism "
                               "not constructed in this probe. E_8 narrative is "
                               "SUGGESTIVE only.")
    }
    summary["overall_pass"] = False  # honest

    def clean(x):
        if isinstance(x, dict): return {str(k): clean(v) for k, v in x.items()}
        if isinstance(x, (list, tuple)): return [clean(v) for v in x]
        if isinstance(x, np.ndarray): return x.tolist()
        if isinstance(x, np.integer): return int(x)
        if isinstance(x, np.floating): return float(x)
        if isinstance(x, np.bool_): return bool(x)
        return x
    with open(OUTPUT_DIR / "phase_D_E8_explicit_results.json", "w") as f:
        json.dump(clean(summary), f, indent=2)
    print(f"Saved {OUTPUT_DIR / 'phase_D_E8_explicit_results.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
