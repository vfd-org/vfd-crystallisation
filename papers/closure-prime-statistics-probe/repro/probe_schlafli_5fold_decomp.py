#!/usr/bin/env python3
"""
Exploratory probe: find Schlafli 5-partition of V_600 and decompose
spectrum under the 5-fold action.

Strategy:
  1. Build V_600 (120 unit icosian quaternions).
  2. Identify 2T = binary tetrahedral subgroup (24 elements = Type A + Type B).
  3. Construct explicit order-5 element g of 2I.
  4. The 5 cosets of 2T in 2I are {2T, g.2T, g^2.2T, g^3.2T, g^4.2T} ---
     these are the Schlafli 5 disjoint 24-cells.
  5. Assign every V_600 vertex to a Schlafli class.
  6. For each A_{V_600} eigenspace, count how many vertices in each
     Schlafli class contribute (= Schlafli orbit structure of the eigenspace).
  7. Look for {1, 1, 5, 5} as a substructure in the cross-tabulation.

Run:
    python probe_schlafli_5fold_decomp.py
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from itertools import permutations
from collections import Counter

import numpy as np

PHI    = (1.0 + 5.0 ** 0.5) / 2.0
INVPHI = 1.0 / PHI
TOL    = 1e-6

OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def quat_mul(p, q):
    """Standard Hamilton quaternion multiplication.
       q = q0 + q1*i + q2*j + q3*k.
    """
    return np.array([
        p[0]*q[0] - p[1]*q[1] - p[2]*q[2] - p[3]*q[3],
        p[0]*q[1] + p[1]*q[0] + p[2]*q[3] - p[3]*q[2],
        p[0]*q[2] - p[1]*q[3] + p[2]*q[0] + p[3]*q[1],
        p[0]*q[3] + p[1]*q[2] - p[2]*q[1] + p[3]*q[0],
    ])


def quat_conj(q):
    return np.array([q[0], -q[1], -q[2], -q[3]])


def quat_inv(q):
    """For unit quaternion, inverse = conjugate."""
    return quat_conj(q)


def build_v600():
    """Build V_600 = 120 unit icosians, same convention as Paper I sim:
       8 Type-A (axis) + 16 Type-B (half-integer) + 96 Type-C (icosian).
    """
    half = 0.5
    half_phi = PHI / 2.0
    half_phi_inv = 1.0 / (2.0 * PHI)
    vertices = []
    # Type A: 8 axial
    for i in range(4):
        for sign in (1.0, -1.0):
            v = [0.0, 0.0, 0.0, 0.0]
            v[i] = sign
            vertices.append(v)
    # Type B: 16 half-integer
    for s0 in (-1, 1):
        for s1 in (-1, 1):
            for s2 in (-1, 1):
                for s3 in (-1, 1):
                    vertices.append([s0*half, s1*half, s2*half, s3*half])
    # Type C: 96 even permutations of (phi/2, 1/2, (1/phi)/2, 0)
    even_perms = [
        (0,1,2,3),(0,2,3,1),(0,3,1,2),
        (1,0,3,2),(1,2,0,3),(1,3,2,0),
        (2,0,1,3),(2,1,3,0),(2,3,0,1),
        (3,0,2,1),(3,1,0,2),(3,2,1,0),
    ]
    for perm in even_perms:
        for s_a in (-1,1):
            for s_b in (-1,1):
                for s_c in (-1,1):
                    v = [0.0]*4
                    v[perm[0]] = s_a * half_phi
                    v[perm[1]] = s_b * half
                    v[perm[2]] = s_c * half_phi_inv
                    v[perm[3]] = 0.0
                    vertices.append(v)
    return np.array(vertices, dtype=float)


def is_in_set(q: np.ndarray, S: np.ndarray, tol: float = TOL) -> int:
    """Return index of q in S, or -1 if not present."""
    diffs = S - q[None, :]
    norms = np.linalg.norm(diffs, axis=1)
    idx = int(np.argmin(norms))
    return idx if norms[idx] < tol else -1


def verify_order(g: np.ndarray, expected: int = 5):
    """Compute g, g^2, ..., g^expected and check g^expected = 1."""
    cur = np.array([1.0, 0.0, 0.0, 0.0])
    for k in range(expected):
        cur = quat_mul(cur, g)
    diff = np.linalg.norm(cur - np.array([1.0, 0.0, 0.0, 0.0]))
    return diff < TOL, diff


def main():
    print("=" * 78)
    print("Probe: find Schlafli 5-partition of V_600 + decompose spectrum")
    print("=" * 78)
    print()

    # Build V_600
    V = build_v600()
    n = V.shape[0]
    print(f"V_600 built: {n} vertices")
    print()

    # 2T = first 24 vertices (Type A + Type B)
    TwoT = V[:24]
    print(f"2T (binary tetrahedral) = first 24 vertices (Type A + Type B)")
    print(f"  These should be closed under quaternion multiplication...")
    # Verify 2T is a subgroup: pick a couple of products and check membership
    sample_checks = 0
    sample_pass = 0
    for i in range(min(8, 24)):
        for j in range(min(8, 24)):
            sample_checks += 1
            prod = quat_mul(TwoT[i], TwoT[j])
            if is_in_set(prod, TwoT) >= 0:
                sample_pass += 1
    print(f"  Subgroup spot-check: {sample_pass}/{sample_checks} sample products in 2T  "
          f"{'PASS' if sample_pass == sample_checks else 'FAIL'}")
    print()

    # Construct order-5 element g = (phi^-1, phi, 1, 0)/2
    g = np.array([INVPHI/2, PHI/2, 0.5, 0.0])
    print(f"Order-5 element candidate: g = (phi^-1, phi, 1, 0)/2 = "
          f"({g[0]:.4f}, {g[1]:.4f}, {g[2]:.4f}, {g[3]:.4f})")
    print(f"  ||g||^2 = {np.sum(g*g):.6f}  (should be 1)")
    ok, diff = verify_order(g, 5)
    print(f"  g^5 = 1: {ok}  (deviation: {diff:.2e})")

    # Verify g is in V_600
    g_idx = is_in_set(g, V)
    print(f"  g is in V_600: {g_idx >= 0}  (index {g_idx})")
    print()

    # Compute g^0, g^1, ..., g^4
    g_powers = [np.array([1.0, 0.0, 0.0, 0.0])]
    for k in range(1, 5):
        g_powers.append(quat_mul(g_powers[-1], g))

    print("Powers of g:")
    for k, gp in enumerate(g_powers):
        idx = is_in_set(gp, V)
        print(f"  g^{k} = ({gp[0]:+.4f}, {gp[1]:+.4f}, {gp[2]:+.4f}, {gp[3]:+.4f})  "
              f"in V_600: {idx >= 0}")
    print()

    # Build 5 Schlafli classes: class k = g^k . 2T = {g^k * t : t in 2T}
    print("Building Schlafli 5-partition via cosets g^k . 2T ...")
    class_of_vertex = [-1] * n   # class for each vertex
    schlafli_classes = [[] for _ in range(5)]

    # For each k in 0..4, build the coset g^k . 2T (left coset)
    for k in range(5):
        for t in TwoT:
            v_target = quat_mul(g_powers[k], t)
            idx = is_in_set(v_target, V)
            if idx < 0:
                print(f"  WARNING: g^{k} * t not found in V_600")
                continue
            if class_of_vertex[idx] >= 0 and class_of_vertex[idx] != k:
                # Conflict — vertex assigned to two classes
                pass  # might be OK if t==1 and class 0 already assigned
            else:
                class_of_vertex[idx] = k
                if idx not in schlafli_classes[k]:
                    schlafli_classes[k].append(idx)

    # Report class sizes
    sizes = [len(c) for c in schlafli_classes]
    print(f"  Schlafli class sizes: {sizes}")
    print(f"  Sum: {sum(sizes)} (expected 120)")
    print()

    # Check: every vertex assigned exactly once?
    unassigned = [i for i in range(n) if class_of_vertex[i] < 0]
    if unassigned:
        print(f"  UNASSIGNED vertices: {len(unassigned)} (first few: {unassigned[:5]})")
    else:
        print(f"  All {n} vertices assigned to exactly one Schlafli class.  PASS")
    print()

    if min(sizes) != 24 or max(sizes) != 24:
        print(f"  WARNING: Schlafli partition not uniform 5x24. Investigating...")
        # Try right-multiplication instead
        print(f"  Retrying with right-multiplication: class k = 2T . g^k ...")
        class_of_vertex = [-1] * n
        schlafli_classes = [[] for _ in range(5)]
        for k in range(5):
            for t in TwoT:
                v_target = quat_mul(t, g_powers[k])
                idx = is_in_set(v_target, V)
                if idx < 0:
                    continue
                if class_of_vertex[idx] < 0:
                    class_of_vertex[idx] = k
                    schlafli_classes[k].append(idx)
        sizes = [len(c) for c in schlafli_classes]
        print(f"  Schlafli class sizes (right cosets): {sizes}")
        print(f"  Sum: {sum(sizes)} (expected 120)")
        print()

    # Build adjacency of V_600 and compute spectrum
    print("Building A_{V_600} adjacency...")
    diffs = V[:, None, :] - V[None, :, :]
    d2 = np.sum(diffs*diffs, axis=2)
    pos = d2[d2 > 1e-9]
    min_d2 = pos.min()
    A = (np.abs(d2 - min_d2) < 1e-7).astype(float)
    np.fill_diagonal(A, 0.0)
    deg = A.sum(axis=1).astype(int)[0]
    print(f"  Edge length^2 = {min_d2:.6f}, regular degree = {deg}")

    eigvals, eigvecs = np.linalg.eigh(A)
    # Group eigenvalues
    distinct = []
    counts = []
    cols = []
    cur_col_start = 0
    for ev in eigvals:
        if distinct and abs(ev - distinct[-1]) < 1e-5:
            counts[-1] += 1
        else:
            distinct.append(float(ev))
            counts.append(1)
    print(f"  Distinct eigenvalues: {len(distinct)}, total dim {sum(counts)}")
    print()
    print(f"  {'eigenvalue':<14} {'multiplicity':<13}")
    print("  " + "-" * 32)
    for ev, m in zip(distinct, counts):
        print(f"  {ev:+10.6f}    {m:5d}")
    print()

    # For each eigenspace, compute the "Schlafli projection" structure:
    #   for each Schlafli class k, sum_{i in class k} |eigvec_j(i)|^2
    #   summed over j in the eigenspace. This is the "mass" of the
    #   eigenspace on Schlafli class k.
    print("--- Eigenspace decomposition by Schlafli class ---")
    print()

    # Build the projection onto each Schlafli class (as a 120x120 diagonal matrix)
    P_k = np.zeros((5, n))
    for k in range(5):
        for i in schlafli_classes[k]:
            P_k[k, i] = 1.0
    # Sanity: P_k.sum(axis=0) should be all ones (each vertex in one class)
    print(f"  Vertex coverage check: max |P_sum - 1| = "
          f"{np.max(np.abs(P_k.sum(axis=0) - 1)):.2e}")
    print()

    # For each eigenvalue group, compute the Schlafli-class mass distribution
    print(f"  {'eigenvalue':<14} {'mult':<6} {'Schlafli class 0..4 masses':<30}")
    print("  " + "-" * 62)
    idx_start = 0
    eigenspace_schlafli_masses = []
    for ev, m in zip(distinct, counts):
        # Eigenvectors in this eigenspace: columns idx_start..idx_start+m
        # Order in eigvals: ascending. eigvecs[:, j] for j in 0..n-1.
        # Find indices j with |eigvals[j] - ev| < tol
        js = [j for j in range(n) if abs(eigvals[j] - ev) < 1e-5]
        assert len(js) == m, f"expected {m} eigenvectors, found {len(js)}"
        V_basis = eigvecs[:, js]  # n x m
        # Mass on Schlafli class k:  sum over basis vectors of sum over vertices i in class k of |V_basis[i, j]|^2
        masses = np.zeros(5)
        for k in range(5):
            for i in schlafli_classes[k]:
                masses[k] += np.sum(V_basis[i, :] ** 2)
        # Normalize: total mass = m (each basis vector has norm 1)
        masses_str = "  ".join(f"{x:5.2f}" for x in masses)
        print(f"  {ev:+10.6f}    {m:5d}  [{masses_str}]")
        eigenspace_schlafli_masses.append({
            "eigenvalue":   float(ev),
            "multiplicity": int(m),
            "schlafli_masses": [float(x) for x in masses],
        })
    print()

    # Look for {1, 1, 5, 5} pattern in masses
    print("--- Looking for {1, 1, 5, 5} structure ---")
    print("Test: does any eigenspace have mass distribution close to (1, 1, 5, 5, *)")
    print("or permutations thereof?")
    target_patterns = [
        (1, 1, 5, 5, 0),  # one is zero
        (1, 1, 5, 5, 12),  # 12 = sum/2
        (5, 5, 1, 1, 0),
    ]
    found_any = False
    for ev_info in eigenspace_schlafli_masses:
        masses = sorted(ev_info["schlafli_masses"])
        for target in target_patterns:
            target_sorted = sorted(target)
            if max(abs(masses[i] - target_sorted[i]) for i in range(5)) < 0.5:
                print(f"  MATCH at eigenvalue {ev_info['eigenvalue']:+.4f}: "
                      f"masses = {masses}, target {target_sorted}")
                found_any = True
    if not found_any:
        print("  No eigenspace mass distribution matches {1,1,5,5,*}.")
    print()

    # Mass-sums across eigenspaces of same multiplicity
    print("--- Multiplicity-25 eigenspace deeper look (V_600 spectral mult 25) ---")
    for ev_info in eigenspace_schlafli_masses:
        if ev_info["multiplicity"] == 25:
            print(f"  At eigenvalue {ev_info['eigenvalue']:+.4f}, mult 25:")
            print(f"    Schlafli masses: {ev_info['schlafli_masses']}")
            print(f"    Sum: {sum(ev_info['schlafli_masses']):.4f} (should be 25)")
            # If mass is uniform 5+5+5+5+5 = 25, that's 5 copies of "something 5-dim"
            print(f"    Uniformity test: 5 per class?  "
                  f"{all(abs(x - 5) < 0.1 for x in ev_info['schlafli_masses'])}")
    print()

    # Save
    summary = {
        "n_vertices": int(n),
        "schlafli_sizes": sizes,
        "partition_uniform_5x24": all(s == 24 for s in sizes),
        "g_order_5_verified": bool(ok),
        "g_components": [float(x) for x in g],
        "spectrum": [{"eigenvalue": float(e), "multiplicity": int(m)}
                     for e, m in zip(distinct, counts)],
        "eigenspace_schlafli_masses": eigenspace_schlafli_masses,
        "found_1155_pattern": bool(found_any),
    }
    with open(OUTPUT_DIR / "probe_schlafli_results.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Saved {OUTPUT_DIR / 'probe_schlafli_results.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
