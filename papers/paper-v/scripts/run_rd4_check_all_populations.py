#!/usr/bin/env python3
"""
Verify that the first-passage-ratio definition of R_X(d) reproduces every
reflection coefficient used in Paper V, by applying the same absorbing
Markov chain to all shell-2/3/4 populations.

If successful, this shows that R_D(4) = 15 is not an isolated assignment but
a uniform consequence of the same definition that gives R_I(2) = 1/6,
R_D(2) = 1, R_I(3) = 1/6, R_D(3) = 2, R_I(4) = 1, R_D(4) = 15.

Definition used:
  R_X(d) = P(first-passage to shell d-1) / P(first-passage to shell d+1),
  from any vertex in population X at shell d, where shells d-1 and d+1 are
  treated as absorbing states in a uniform random walk on the 600-cell.
"""

from __future__ import annotations

import numpy as np

from run_rd4_absorbing_chain import (
    build_600cell_vertices,
    build_adjacency,
    bfs_shells,
    intersection_numbers,
    classify_populations,
    transition_matrix,
    PHI,
)


def first_passage_ratio(A, dist, v, inward_shell, outward_shell):
    """Compute P(hit inward_shell first) / P(hit outward_shell first) from vertex v.

    Uses the absorbing Markov chain with shells inward_shell and outward_shell
    absorbing, everything else transient.
    """
    n = len(A)
    P = transition_matrix(A)

    absorbing_in = np.array([dist[w] == inward_shell for w in range(n)], dtype=bool)
    absorbing_out = np.array([dist[w] == outward_shell for w in range(n)], dtype=bool)
    transient = ~(absorbing_in | absorbing_out)

    T_idx = np.where(transient)[0]
    n_T = len(T_idx)
    idx_of = {w: k for k, w in enumerate(T_idx)}
    if v not in idx_of:
        raise ValueError(f"vertex {v} is already absorbing, cannot compute ratio")

    Q = np.zeros((n_T, n_T))
    R_in = np.zeros((n_T, 1))
    R_out = np.zeros((n_T, 1))
    for k, u in enumerate(T_idx):
        for w in range(n):
            if P[u, w] == 0:
                continue
            if absorbing_in[w]:
                R_in[k, 0] += P[u, w]
            elif absorbing_out[w]:
                R_out[k, 0] += P[u, w]
            else:
                Q[k, idx_of[w]] = P[u, w]
    N = np.linalg.inv(np.eye(n_T) - Q)
    p_in = float((N @ R_in)[idx_of[v], 0])
    p_out = float((N @ R_out)[idx_of[v], 0])
    return p_in, p_out


def main():
    verts = build_600cell_vertices()
    A = build_adjacency(verts, 1.0 / PHI)
    dist = bfs_shells(A, source=0)
    pop = classify_populations(A, dist)

    print("=" * 72)
    print("First-passage-ratio R_X(d) for all populations at shells 2, 3, 4")
    print("=" * 72)
    print(f"Definition: R = P(first-passage to shell d-1) / P(first-passage to shell d+1)")
    print(f"            on uniform random walk of the 600-cell vertex graph.")
    print()

    # Paper V's table values for comparison.
    claimed = {
        (2, "ico"): (1, 6, "1/6"),
        (2, "dod"): (1, 1, "1"),
        (3, "ico"): (1, 6, "1/6"),
        (3, "dod"): (2, 1, "2"),
        (4, "ico"): (1, 1, "1"),
        (4, "dod"): (15, 1, "15"),
    }

    print(f"{'shell':>6} {'pop':>5} {'(a,b,c)':>10} {'P_in':>10} {'P_out':>10} {'R = P_in/P_out':>16} {'claimed':>10}")
    print("-" * 72)

    from collections import defaultdict
    seen = defaultdict(list)
    for v in range(len(A)):
        d = int(dist[v])
        if d not in (2, 3, 4):
            continue
        p = pop.get(v)
        if p not in ("ico", "dod"):
            continue
        if (d, p) in seen:
            continue  # only need one representative per (shell, pop)
        seen[(d, p)] = True

        a, b, c = intersection_numbers(A, dist, v)
        p_in, p_out = first_passage_ratio(A, dist, v, inward_shell=d - 1, outward_shell=d + 1)
        ratio = p_in / p_out if p_out > 0 else float("inf")
        c_num, c_den, c_str = claimed[(d, p)]
        claimed_val = c_num / c_den
        match = abs(ratio - claimed_val) < 1e-9 if np.isfinite(claimed_val) else ratio == float("inf")
        tag = " OK " if match else "FAIL"
        print(f"{d:>6} {p:>5} {str((a,b,c)):>10} {p_in:>10.6f} {p_out:>10.6f} {ratio:>16.6f} {c_str:>10} {tag}")

    # Also compare against the single-step naive c/b for completeness.
    print()
    print("Single-step naive c/b (as contrast):")
    print(f"{'shell':>6} {'pop':>5} {'(a,b,c)':>10} {'c/b single step':>20}")
    print("-" * 50)
    for (d, p) in [(2, "ico"), (2, "dod"), (3, "ico"), (3, "dod"), (4, "ico"), (4, "dod")]:
        for v in range(len(A)):
            if int(dist[v]) == d and pop.get(v) == p:
                a, b, c = intersection_numbers(A, dist, v)
                naive = "inf" if b == 0 else f"{c}/{b} = {c / b:.6f}"
                print(f"{d:>6} {p:>5} {str((a,b,c)):>10} {naive:>20}")
                break


if __name__ == "__main__":
    main()
