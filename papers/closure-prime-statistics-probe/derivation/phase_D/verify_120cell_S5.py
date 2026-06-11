#!/usr/bin/env python3
"""
DERIVATION Phase D-bis: 120-cell S_5 probe.

Goal: investigate whether the 120-cell (dual of V_600) admits an S_5
action via graph automorphisms.  If yes, decompose its eigenspaces
under S_5 and look for {1, 1, 5, 5}.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from itertools import combinations, permutations
from collections import Counter, deque

import numpy as np

PHI    = (1.0 + 5.0 ** 0.5) / 2.0
INVPHI = 1.0 / PHI
PHI2   = PHI * PHI
PHI_NEG2 = INVPHI * INVPHI
SQRT5  = 5.0 ** 0.5
TOL    = 1e-6

OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def quat_mul(p, q):
    return np.array([
        p[0]*q[0] - p[1]*q[1] - p[2]*q[2] - p[3]*q[3],
        p[0]*q[1] + p[1]*q[0] + p[2]*q[3] - p[3]*q[2],
        p[0]*q[2] - p[1]*q[3] + p[2]*q[0] + p[3]*q[1],
        p[0]*q[3] + p[1]*q[2] - p[2]*q[1] + p[3]*q[0],
    ], dtype=float)


def even_perms_4():
    out = []
    for p in permutations(range(4)):
        inv = 0
        for i in range(4):
            for j in range(i+1, 4):
                if p[i] > p[j]: inv += 1
        if inv % 2 == 0: out.append(p)
    return out


def build_120cell():
    """Standard 600-vertex 120-cell construction."""
    verts = []
    # Type 1: 24 of (0, 0, ±2, ±2)
    for positions in combinations(range(4), 2):
        for s0 in (-1, 1):
            for s1 in (-1, 1):
                v = [0.0]*4
                v[positions[0]] = 2.0 * s0
                v[positions[1]] = 2.0 * s1
                verts.append(v)
    # Type 2: 64 of (±1, ±1, ±1, ±√5)
    for sqrt5_pos in range(4):
        for sm in range(16):
            s = [(-1 if (sm >> i) & 1 else 1) for i in range(4)]
            v = [s[i] * 1.0 for i in range(4)]
            v[sqrt5_pos] = s[sqrt5_pos] * SQRT5
            verts.append(v)
    # Type 3: 64 of (±φ², ±φ⁻¹, ±φ⁻¹, ±φ⁻¹)
    for phi2_pos in range(4):
        for sm in range(16):
            s = [(-1 if (sm >> i) & 1 else 1) for i in range(4)]
            v = [s[i] * INVPHI for i in range(4)]
            v[phi2_pos] = s[phi2_pos] * PHI2
            verts.append(v)
    # Type 4: 64 of (±φ, ±φ, ±φ, ±φ⁻²)
    for phi_neg2_pos in range(4):
        for sm in range(16):
            s = [(-1 if (sm >> i) & 1 else 1) for i in range(4)]
            v = [s[i] * PHI for i in range(4)]
            v[phi_neg2_pos] = s[phi_neg2_pos] * PHI_NEG2
            verts.append(v)
    ep = even_perms_4()
    # Type 5: 96 even perms of (0, ±φ⁻², ±1, ±φ²)
    for p in ep:
        for s0 in (-1, 1):
            for s1 in (-1, 1):
                for s2 in (-1, 1):
                    v = [0.0]*4
                    v[p[1]] = s0 * PHI_NEG2
                    v[p[2]] = s1 * 1.0
                    v[p[3]] = s2 * PHI2
                    verts.append(v)
    # Type 6: 96 even perms of (0, ±φ⁻¹, ±φ, ±√5)
    for p in ep:
        for s0 in (-1, 1):
            for s1 in (-1, 1):
                for s2 in (-1, 1):
                    v = [0.0]*4
                    v[p[1]] = s0 * INVPHI
                    v[p[2]] = s1 * PHI
                    v[p[3]] = s2 * SQRT5
                    verts.append(v)
    # Type 7: 192 even perms of (±φ⁻¹, ±1, ±φ, ±2)
    for p in ep:
        for sm in range(16):
            s = [(-1 if (sm >> i) & 1 else 1) for i in range(4)]
            v = [0.0]*4
            v[p[0]] = s[0] * INVPHI
            v[p[1]] = s[1] * 1.0
            v[p[2]] = s[2] * PHI
            v[p[3]] = s[3] * 2.0
            verts.append(v)
    V = np.array(verts, dtype=float)
    # Dedupe
    rounded = np.round(V / 1e-7).astype(np.int64)
    seen = set(); idx = []
    for i, r in enumerate(rounded):
        key = tuple(r)
        if key not in seen:
            seen.add(key)
            idx.append(i)
    return V[idx]


def find_vertex(target, V, tol=TOL):
    diffs = V - target[None, :]
    d = np.linalg.norm(diffs, axis=1)
    i = int(np.argmin(d))
    return i if d[i] < tol else -1


def build_perm_from_action(action_fn, V):
    n = V.shape[0]
    pi = np.zeros(n, dtype=int)
    for i in range(n):
        target = action_fn(V[i])
        idx = find_vertex(target, V)
        if idx < 0:
            return None
        pi[i] = idx
    return pi


def perm_to_matrix(pi):
    n = len(pi)
    P = np.zeros((n, n))
    for j in range(n):
        P[int(pi[j]), j] = 1.0
    return P


def cycle_structure(pi):
    n = len(pi)
    visited = [False]*n
    cycles = []
    for i in range(n):
        if visited[i]: continue
        l = 0
        j = i
        while not visited[j]:
            visited[j] = True
            l += 1
            j = int(pi[j])
        cycles.append(l)
    return Counter(cycles)


def main():
    print("=" * 78)
    print("Phase D-bis: 120-cell S_5 probe")
    print("=" * 78)
    print()

    V = build_120cell()
    n = V.shape[0]
    print(f"120-cell: {n} vertices (expected 600)")

    # Adjacency
    diffs = V[:, None, :] - V[None, :, :]
    d2 = np.sum(diffs * diffs, axis=2)
    pos = d2[d2 > 1e-9]
    min_d2 = pos.min()
    A = (np.abs(d2 - min_d2) < 1e-5).astype(float)
    np.fill_diagonal(A, 0.0)
    edge_len = float(min_d2 ** 0.5)
    deg = int(A.sum(axis=1)[0])
    print(f"  edge length: {edge_len:.4f}, regular degree: {deg}")

    eigvals, eigvecs = np.linalg.eigh(A)
    distinct = []
    indices_by_eig = []
    for i, ev in enumerate(eigvals):
        if distinct and abs(ev - distinct[-1]) < 1e-5:
            indices_by_eig[-1].append(i)
        else:
            distinct.append(float(ev))
            indices_by_eig.append([i])
    print(f"  spectrum: {len(distinct)} distinct eigenvalues, "
          f"multiplicities: {sorted([len(ix) for ix in indices_by_eig])}")
    print()

    # Apply g (order-5 element from V_600 / 2I)
    g_quat = np.array([INVPHI/2, PHI/2, 0.5, 0.0])
    print(f"  Applying g = (φ⁻¹/2, φ/2, 1/2, 0) to 120-cell vertices...")
    g_perm = build_perm_from_action(lambda v: quat_mul(g_quat, v), V)
    if g_perm is None:
        print(f"  g does NOT preserve 120-cell!")
        return 1
    print(f"  g permutes 120-cell vertices.")
    cs = cycle_structure(g_perm)
    print(f"  Cycle structure: {dict(cs)}")
    print(f"  (Expected for order-5 in 600 vertices: 120 cycles of length 5)")
    # Check g commutes with A
    G_mat = perm_to_matrix(g_perm)
    commutes = np.allclose(A @ G_mat, G_mat @ A, atol=1e-9)
    print(f"  g commutes with A_{120-cell}: {commutes}")
    print()

    # 5-partition of 120-cell
    # The 5 orbits under <g> have size 5 each, total 120 orbits, NOT a 5-partition.
    # For a natural 5-partition: 600 = 5 × 120, we need a different structure.
    # One natural choice: 5 inscribed 600-cells in the 120-cell.
    # Each is a W(H_4)-orbit of size 120 under a specific subgroup.
    print("--- Natural 5-partition of the 120-cell ---")
    print("  600 = 5 × 120: 5 inscribed 600-cells.")
    print("  Constructing via right-cosets of a 120-element subgroup of W(H_4)...")
    # We could use the 5 inscribed 600-cells: each is generated by an order-2
    # subgroup of W(H_4)/2I = S_3 acting on 5 elements.  Implementation:
    # take the orbits of V under the FULL <g> action (each orbit has 5 elements,
    # giving 120 orbits).  That's NOT a 5-partition though.
    #
    # Alternative: each vertex of the 120-cell is incident to a specific
    # subset of the 5 inscribed 600-cells.  Group vertices by which 600-cell
    # they "belong to."
    #
    # SIMPLEST: use vertex TYPE (we built 7 types). They have sizes
    # {24, 64, 64, 64, 96, 96, 192}. No 5-partition there directly.
    #
    # An ad-hoc choice: pick 5 orbits-of-vertex-orbits whose union spans V.
    # Since orbits under <g> have size 5 and we have 120 orbits, we'd need
    # a 24-class structure that groups orbits into 5 sets of 24 orbits each.
    # That's the dual of V_600's Schläfli.
    print()

    # Try: for each vertex v, compute v mod some lattice → 5 cosets
    # This is non-trivial geometrically. Skip detailed partition for now.

    # Instead: search for involutions that commute with A and check
    # whether they exhibit odd-permutation behaviour on g-orbits.
    print("--- Searching for involutions h commuting with A on 120-cell ---")
    candidates = []
    candidates.append(("quat_conj", lambda v: np.array([v[0], -v[1], -v[2], -v[3]])))
    for i in range(4):
        def r_i(v, i=i):
            out = v.copy(); out[i] = -out[i]; return out
        candidates.append((f"reflect_axis_{i}", r_i))
    for i, j in combinations(range(4), 2):
        def r_ij(v, i=i, j=j):
            out = v.copy(); out[i] = -out[i]; out[j] = -out[j]; return out
        candidates.append((f"rotate_180_{i}_{j}", r_ij))
    candidates.append(("inversion", lambda v: -v))
    for i, j in combinations(range(4), 2):
        def swap_ij(v, i=i, j=j):
            out = v.copy(); out[i], out[j] = v[j], v[i]; return out
        candidates.append((f"swap_coords_{i}_{j}", swap_ij))

    valid_involutions = []
    for name, fn in candidates:
        pi = build_perm_from_action(fn, V)
        if pi is None: continue
        # Order 2 check
        if not np.array_equal(pi[pi], np.arange(n)): continue
        # Commute with A
        H = perm_to_matrix(pi)
        if not np.allclose(A @ H, H @ A, atol=1e-9): continue
        # Action on g-orbit space (120 orbits)
        # Compute the orbit each vertex belongs to
        orbit_id = np.zeros(n, dtype=int)
        visited = [False]*n
        oid = 0
        for i in range(n):
            if visited[i]: continue
            j = i
            while not visited[j]:
                visited[j] = True
                orbit_id[j] = oid
                j = int(g_perm[j])
            oid += 1
        # Permutation on 120 orbits
        orbit_perm = np.zeros(oid, dtype=int)
        for k in range(oid):
            # Pick a representative
            rep_idx = next(i for i in range(n) if orbit_id[i] == k)
            mapped = int(pi[rep_idx])
            orbit_perm[k] = orbit_id[mapped]
        # Number of fixed orbits, cycle structure
        op_cycles = cycle_structure(orbit_perm)
        valid_involutions.append({
            "name": name, "h_perm": pi,
            "h_matrix": H,
            "orbit_perm": orbit_perm.tolist(),
            "orbit_cycle_structure": dict(op_cycles),
        })
        print(f"  {name:<25}  orbit cycle structure: {dict(op_cycles)}")
    print()
    print(f"  Found {len(valid_involutions)} valid involutions commuting with A.")
    print()

    # Look for involutions giving "transposition-like" action.
    # On 120 orbits, a single transposition means 1 swap + 118 fixed.
    # A double-transposition: 2 swaps + 116 fixed.
    # We need ODD permutation = odd number of transpositions.
    print("--- Looking for ODD-permutation involutions ---")
    for inv in valid_involutions:
        cs = inv["orbit_cycle_structure"]
        # Count number of 2-cycles
        n2 = cs.get(2, 0)
        # Odd permutation iff odd number of transpositions
        if n2 % 2 == 1:
            print(f"  {inv['name']:<25}  has {n2} transpositions (ODD permutation)!")
    print()
    print("  (Even permutations on 120 orbits have an EVEN number of 2-cycles.)")
    print()

    # Save
    out_summary = {
        "n_vertices_120cell":   int(n),
        "n_distinct_eigs":      int(len(distinct)),
        "g_commutes_A":         bool(commutes),
        "valid_involutions":    [
            {"name": inv["name"],
             "orbit_cycle_structure": inv["orbit_cycle_structure"]}
            for inv in valid_involutions
        ],
        "g_orbits":             int(oid) if valid_involutions else None,
    }
    with open(OUTPUT_DIR / "phase_D_120cell_S5_results.json", "w") as f:
        json.dump(out_summary, f, indent=2)
    print(f"Saved {OUTPUT_DIR / 'phase_D_120cell_S5_results.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
