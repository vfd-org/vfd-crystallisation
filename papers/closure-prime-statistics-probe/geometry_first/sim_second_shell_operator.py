#!/usr/bin/env python3
"""
GEOMETRY-FIRST SIM step 3: Second-shell adjacency operator A_2.

Implements WO_second_shell_operator.md.  Builds the 0/1 adjacency at
the second-smallest non-zero squared distance on V_600, verifies it
commutes with A and with the 5 W(H_4) generators g1..g5, and computes
A_2's eigenvalues restricted to each of A's 9 eigenspaces.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np

PHI    = (1.0 + 5.0 ** 0.5) / 2.0
INVPHI = 1.0 / PHI

HERE = Path(__file__).parent
OUTPUT_DIR = HERE / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


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


def find_vertex(target, V, tol=1e-8):
    diffs = V - target[None, :]
    d = np.linalg.norm(diffs, axis=1)
    i = int(np.argmin(d))
    return i if d[i] < tol else -1


def build_perm_from_action(action_fn, V):
    n = V.shape[0]
    pi = np.zeros(n, dtype=int)
    for j in range(n):
        target = action_fn(V[j])
        idx = find_vertex(target, V)
        if idx < 0:
            return None
        pi[j] = idx
    return pi


def perm_to_matrix(pi):
    n = len(pi)
    P = np.zeros((n, n))
    for j in range(n):
        P[int(pi[j]), j] = 1.0
    return P


def main():
    print("=" * 78)
    print("SIM 3: Second-shell adjacency A_2 and joint diagonalisation")
    print("=" * 78)
    print()

    V = build_v600()
    n = V.shape[0]
    print(f"  V_600: {n} vertices")

    # Pairwise squared distances
    diffs = V[:, None, :] - V[None, :, :]
    d2 = np.sum(diffs * diffs, axis=2)
    distinct_d2 = sorted(set(round(float(x), 6) for x in d2.flatten()))
    print(f"  Distinct squared distances: {distinct_d2}")
    # Should be {0, ~0.382, 1, ~1.382, 2, ~2.618, 3, ~3.618, 4}
    expected = [0.0, 0.381966, 1.0, 1.381966, 2.0, 2.618034, 3.0, 3.618034, 4.0]
    match = all(abs(d - e) < 1e-5 for d, e in zip(distinct_d2, expected))
    print(f"  Match expected 9-shell pattern: {match}")
    assert match, "distance pattern mismatch"

    # ---- Build A (first shell, squared distance = 0.382) ----
    A = (np.abs(d2 - distinct_d2[1]) < 1e-7).astype(float)
    np.fill_diagonal(A, 0.0)
    print(f"  A (shell 1, d²≈{distinct_d2[1]:.4f}): degree = {int(A.sum(axis=1)[0])}")

    # ---- Build all shell operators A_2..A_8 ----
    # The 8 non-zero shells give 8 commuting operators (Bose-Mesner algebra
    # generators). For CSCO completeness we likely need several.
    shell_operators = {}  # name -> matrix
    shell_distances = {}
    for k in range(1, 9):
        d2_k = distinct_d2[k]   # k-th non-zero squared distance
        A_k = (np.abs(d2 - d2_k) < 1e-7).astype(float)
        np.fill_diagonal(A_k, 0.0)
        deg_k = int(A_k.sum(axis=1)[0])
        if k == 1:
            print(f"  A (shell 1, d²={d2_k:.4f}): degree = {deg_k}")
        else:
            shell_operators[f"A_{k}"] = A_k
            shell_distances[f"A_{k}"] = d2_k
            sym = bool(np.allclose(A_k, A_k.T))
            print(f"  A_{k} (shell {k}, d²={d2_k:.4f}): degree = {deg_k}, "
                  f"symmetric: {sym}")
    A2 = shell_operators["A_2"]
    A2_symmetric = bool(np.allclose(A2, A2.T))
    print()

    # ---- Verify A_2 commutes with A ----
    AA2 = A @ A2
    A2A = A2 @ A
    A_A2_commute = np.allclose(AA2, A2A, atol=1e-8)
    max_dev_AA2 = float(np.max(np.abs(AA2 - A2A)))
    print(f"  A · A_2 = A_2 · A: {A_A2_commute} (max |diff| = {max_dev_AA2:.2e})")

    # ---- Build W(H_4) generators g1..g5 (same as step 1) ----
    print()
    print("  Building W(H_4) generators (g1..g5) ...")
    q1 = np.array([0.5, 0.5, 0.5, 0.5])
    g5q = np.array([INVPHI/2, PHI/2, 0.5, 0.0])
    q2 = -g5q
    q_i = np.array([0.0, 1.0, 0.0, 0.0])
    r_diag = np.array([0.5, 0.5, 0.5, 0.5])

    def g1(v): return quat_mul(q1, v)
    def g2(v): return quat_mul(q2, v)
    def g3(v): return quat_mul(v, q1)
    def g4(v): return quat_mul(q_i, v)
    def g5(v): return v - 2.0 * np.dot(v, r_diag) * r_diag

    gens = {"g1": g1, "g2": g2, "g3": g3, "g4": g4, "g5": g5}
    perm_mats = {}
    commute_with_A2 = {}
    for name, fn in gens.items():
        pi = build_perm_from_action(fn, V)
        if pi is None:
            print(f"  {name}: does NOT preserve V_600")
            return 1
        P = perm_to_matrix(pi)
        perm_mats[name] = P
        # Check P · A_2 = A_2 · P
        PA2 = P @ A2
        A2P = A2 @ P
        commute = bool(np.allclose(PA2, A2P, atol=1e-8))
        commute_with_A2[name] = commute
    print(f"  Commutation of A_2 with g_i:")
    for name, ok in commute_with_A2.items():
        print(f"    {name}: {ok}")
    print()

    # ---- Diagonalise A and compute A_2 restriction ----
    eigvals_A_raw, eigvecs_A = np.linalg.eigh(A)
    # Cluster eigenvalues
    eigvals_A = []
    eigenspace_indices = []
    cur_val = eigvals_A_raw[0]
    cur_idx = [0]
    for k in range(1, n):
        if abs(eigvals_A_raw[k] - cur_val) < 1e-6:
            cur_idx.append(k)
        else:
            eigvals_A.append(float(cur_val))
            eigenspace_indices.append(cur_idx)
            cur_val = eigvals_A_raw[k]
            cur_idx = [k]
    eigvals_A.append(float(cur_val))
    eigenspace_indices.append(cur_idx)
    n_eig = len(eigvals_A)
    print(f"  A has {n_eig} distinct eigenvalues")
    print()

    # For each A-eigenspace, compute each shell operator's scalar
    # (all shell operators commute with A and W(H_4); on each
    # A-eigenspace they act as scalars).
    results = []
    print(f"  {'eigval_A':<12} {'dim':<5} {'A_2':<9} {'A_3':<9} {'A_4':<9} "
          f"{'A_5':<9} {'A_6':<9} {'A_7':<9} {'A_8':<9}")
    print("  " + "-" * 86)
    shell_names = [f"A_{k}" for k in range(2, 9)]
    for k in range(n_eig):
        idx = eigenspace_indices[k]
        B_lam = eigvecs_A[:, idx]   # 120 x dim
        shell_scalars = {}
        for sh in shell_names:
            A_sh_E = B_lam.T @ shell_operators[sh] @ B_lam
            eigvals_sh = np.linalg.eigvalsh(A_sh_E)
            scalar_val = round(float(np.mean(eigvals_sh)), 6)
            shell_scalars[sh] = scalar_val
        results.append({
            "eigenvalue_A":   float(eigvals_A[k]),
            "dim":            len(idx),
            "shell_scalars":  shell_scalars,
        })
        scalar_str = " ".join(f"{shell_scalars[sh]:+8.3f}" for sh in shell_names)
        print(f"  {eigvals_A[k]:+10.4f}  {len(idx):<5} {scalar_str}")
    print()

    # ---- Find minimum k for which (A, A_2, ..., A_k) is a CSCO ----
    print(f"  CSCO depth analysis: how many shells distinguish all 9 eigenspaces?")
    by_dim = {}
    for r in results:
        by_dim.setdefault(r["dim"], []).append(r)
    pair_dims = sorted(d for d, rs in by_dim.items() if len(rs) == 2)

    # Find which shell distinguishes each pair
    pair_distinguishing_shells = {}
    for d in pair_dims:
        r0, r1 = by_dim[d]
        shell_diffs = []
        for sh in shell_names:
            if abs(r0["shell_scalars"][sh] - r1["shell_scalars"][sh]) > 1e-6:
                shell_diffs.append(sh)
        pair_distinguishing_shells[f"dim_{d}"] = shell_diffs
        print(f"    dim-{d} pair (eigvals {r0['eigenvalue_A']:+.4f} and "
              f"{r1['eigenvalue_A']:+.4f}):")
        for sh in shell_names:
            v0 = r0["shell_scalars"][sh]
            v1 = r1["shell_scalars"][sh]
            diff = "✓ distinguishes" if abs(v0 - v1) > 1e-6 else "·"
            print(f"      {sh}: {v0:+8.3f} vs {v1:+8.3f}  {diff}")
        print(f"      Shells that distinguish this pair: {shell_diffs}")

    # Minimum CSCO depth: smallest k such that adding shells A_2..A_k
    # distinguishes all 3 pairs.
    all_pairs_distinguished = all(len(shells) > 0
                                    for shells in pair_distinguishing_shells.values())
    print()
    print(f"  All 3 pairs distinguished by some shell subset: {all_pairs_distinguished}")
    print()

    # Find the minimal subset of shells {A_2, ..., A_8} that distinguishes ALL pairs
    if all_pairs_distinguished:
        # Greedy: pick shells until all pairs distinct
        chosen_shells = []
        unresolved = set(pair_distinguishing_shells.keys())
        for sh in shell_names:
            new_unresolved = set()
            for p in unresolved:
                if sh not in pair_distinguishing_shells[p]:
                    new_unresolved.add(p)
            if len(new_unresolved) < len(unresolved):
                chosen_shells.append(sh)
                unresolved = new_unresolved
            if not unresolved:
                break
        print(f"  Minimal shell set giving (A, ...) CSCO: A, {chosen_shells}")
    else:
        chosen_shells = []
        print(f"  CANNOT achieve CSCO with shell operators alone — need extra operators.")
    print()

    pair_distinct = {k: bool(len(v) > 0)
                     for k, v in pair_distinguishing_shells.items()}

    # ---- Acceptance ----
    checks = {
        "A_2_commutes_with_A":                       A_A2_commute,
        "A_2_commutes_with_all_g_i":                 all(commute_with_A2.values()),
        "all_same_dim_pairs_distinguished_by_shells": all(pair_distinct.values()),
        "minimal_shell_set":                         chosen_shells,
    }
    print("Acceptance checks:")
    for k, v in checks.items():
        print(f"  {k}: {v}")
    all_pass = all(checks.values())
    print()
    print(f"OVERALL: {'PASS' if all_pass else 'FAIL'}")

    # ---- Write outputs ----
    out_json = {
        "v600_count":              120,
        "distinct_squared_distances": distinct_d2,
        "shell_2_squared_distance": distinct_d2[2],
        "A_2_degree":              int(shell_operators["A_2"].sum(axis=1)[0]),
        "A_2_symmetric":           bool(A2_symmetric),
        "shell_degrees":           {sh: int(shell_operators[sh].sum(axis=1)[0])
                                      for sh in shell_names},
        "commutation": {
            "A_2_with_A":          bool(A_A2_commute),
            "A_2_with_generators": commute_with_A2,
        },
        "joint_eigenspaces":       results,
        "pair_distinct_under_A_2": pair_distinct,
        "checks":                  checks,
        "overall_pass":            all_pass,
    }
    with open(OUTPUT_DIR / "second_shell_results.json", "w") as f:
        json.dump(out_json, f, indent=2)

    A2_deg = int(shell_operators["A_2"].sum(axis=1)[0])
    md_lines = ["# Shell-operator joint diagonalisation of V_600 eigenspaces", "",
                f"A_2 = 0/1 adjacency at squared distance d² = {distinct_d2[2]:.4f}",
                f"A_2 degree per vertex: {A2_deg}", "",
                f"## Joint (A, A_2..A_8) eigenspace scalars", "",
                "| eigenvalue_A | dim | " +
                " | ".join(shell_names) + " |",
                "|" + "---|" * (2 + len(shell_names))]
    for r in results:
        scalars_str = " | ".join(f"{r['shell_scalars'][sh]:+.4f}" for sh in shell_names)
        md_lines.append(f"| {r['eigenvalue_A']:+.4f} | {r['dim']} | "
                         f"{scalars_str} |")
    md_lines.append("")
    md_lines.append("## Acceptance")
    for k, v in checks.items():
        md_lines.append(f"- `{k}`: **{v}**")
    with open(OUTPUT_DIR / "second_shell_results.md", "w") as f:
        f.write("\n".join(md_lines))
    print()
    print(f"Wrote:")
    print(f"  {OUTPUT_DIR / 'second_shell_results.md'}")
    print(f"  {OUTPUT_DIR / 'second_shell_results.json'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
