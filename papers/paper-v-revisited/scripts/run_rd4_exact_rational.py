#!/usr/bin/env python3
"""
Exact rational proof that R_D(4) = 15 on the 600-cell.

Approach: the stabiliser of the BFS root vertex v_0 in H_4 acts transitively
on every (shell, population) orbit, so the random walk is H_4^{v_0}-symmetric
under population lumping. Lumping the 120 vertices by (shell, population)
gives a small Markov chain with *rational* transition probabilities (each
edge count divided by 12). Solving that chain exactly with Python's
fractions module gives closed-form rationals for the first-passage
probabilities.

We:
  1. construct the 600-cell and compute the lumped transition table in
     terms of exact counts (validated against the floating-point script);
  2. solve the resulting absorbing chain symbolically over Q;
  3. report p_in = 15/16, p_out = 1/16 as closed-form rationals;
  4. conclude R_D(4) = 15 exactly.

Runs standalone (only numpy + Python's fractions).
"""

from __future__ import annotations

from fractions import Fraction
from collections import defaultdict

import numpy as np

from run_rd4_absorbing_chain import (
    build_600cell_vertices,
    build_adjacency,
    bfs_shells,
    intersection_numbers,
    classify_populations,
    PHI,
)


def lumped_transition_table(A, dist, pop):
    """Return a dict mapping (shell, population_label) -> {(target_shell, target_pop): integer count}.

    The count is the (orbit-averaged) number of edges per source vertex going to
    a target state. Equivalently, this is the integer block-sum-per-row of the
    lumped adjacency matrix.
    """
    n = len(A)

    # Population label; for shell 0, 1, 5 use singletons.
    def state(v):
        d = int(dist[v])
        if d in (0, 1, 5):
            return (d, "all")
        return (d, pop.get(v))

    # For each source state, group vertices and count outgoing transitions
    # per target state. Check that the count is the same for every source vertex
    # in the orbit (this is the H_4-stabiliser transitivity condition we need).
    states = sorted(set(state(v) for v in range(n)), key=lambda s: (s[0], s[1] or ""))

    counts = {}  # counts[src_state] = {target_state: integer}
    for src_state in states:
        src_verts = [v for v in range(n) if state(v) == src_state]
        # Compute per-vertex count for each target state; check uniformity.
        per_target = None
        for v in src_verts:
            c_this = defaultdict(int)
            for w in range(n):
                if A[v, w]:
                    c_this[state(w)] += 1
            c_this = dict(c_this)
            if per_target is None:
                per_target = c_this
            else:
                assert c_this == per_target, (
                    f"non-uniform edge counts within orbit {src_state}: "
                    f"{per_target} vs {c_this}"
                )
        counts[src_state] = per_target

    # Sanity: row sums should all equal 12 (degree).
    for src_state, tgt_counts in counts.items():
        assert sum(tgt_counts.values()) == 12, (
            f"state {src_state} row sum != 12: {tgt_counts}"
        )
    return states, counts


def solve_rational_absorbing_chain(states, counts, absorbing_states, degree=12):
    """
    Solve the lumped absorbing chain over Q.

    Returns dict giving, for each transient source state, the probability of
    first-passage absorption into each absorbing class.
    """
    transient = [s for s in states if s not in absorbing_states]
    absorbing = list(absorbing_states)

    n_T = len(transient)
    idx = {s: i for i, s in enumerate(transient)}

    Q = [[Fraction(0, 1) for _ in range(n_T)] for _ in range(n_T)]
    R = {a: [Fraction(0, 1) for _ in range(n_T)] for a in absorbing}

    deg = Fraction(degree, 1)
    for src in transient:
        for tgt, c in counts[src].items():
            p = Fraction(c, degree)
            if tgt in absorbing:
                R[tgt][idx[src]] += p
            else:
                Q[idx[src]][idx[tgt]] += p

    # Solve (I - Q) x = R for each absorbing class.
    # Use Fraction-based Gauss-Jordan elimination.
    def inv_identity_minus_Q(Q):
        # Compute I - Q as a mutable list-of-lists
        M = [
            [
                (Fraction(1, 1) if i == j else Fraction(0, 1)) - Q[i][j]
                for j in range(n_T)
            ]
            for i in range(n_T)
        ]
        # Augment with identity
        for i in range(n_T):
            M[i].extend(
                Fraction(1, 1) if j == i else Fraction(0, 1)
                for j in range(n_T)
            )
        # Gauss-Jordan
        for col in range(n_T):
            # find pivot
            piv = None
            for r in range(col, n_T):
                if M[r][col] != 0:
                    piv = r
                    break
            assert piv is not None, f"singular at col {col}"
            if piv != col:
                M[col], M[piv] = M[piv], M[col]
            # normalize row
            inv_piv = Fraction(1) / M[col][col]
            M[col] = [x * inv_piv for x in M[col]]
            # eliminate
            for r in range(n_T):
                if r == col:
                    continue
                if M[r][col] == 0:
                    continue
                factor = M[r][col]
                M[r] = [M[r][j] - factor * M[col][j] for j in range(2 * n_T)]
        # Extract inverse (right half)
        N = [[M[i][n_T + j] for j in range(n_T)] for i in range(n_T)]
        return N

    N = inv_identity_minus_Q(Q)

    result = {}
    for src in transient:
        probs = {}
        for a in absorbing:
            total = Fraction(0, 1)
            for j, other in enumerate(transient):
                total += N[idx[src]][j] * R[a][j]
            probs[a] = total
        result[src] = probs
    return result


def main():
    print("=" * 72)
    print("Exact rational proof: R_D(4) = 15 via lumped absorbing chain")
    print("=" * 72)

    verts = build_600cell_vertices()
    A = build_adjacency(verts, 1.0 / PHI)
    dist = bfs_shells(A, source=0)
    pop = classify_populations(A, dist)

    states, counts = lumped_transition_table(A, dist, pop)
    print(f"lumped states ({len(states)}): {states}")
    print()
    print("Lumped transition counts (each count divided by degree 12 gives probability):")
    for s in states:
        row = counts[s]
        parts = ", ".join(f"{t}: {c}" for t, c in sorted(row.items(), key=lambda x: (x[0][0], x[0][1] or '')))
        print(f"  {s} -> {{ {parts} }}")

    # Verify trapped dod-shell-4 has no direct shell-5 neighbour (b=0) and
    # exactly 6 shell-3 neighbours (c=6), with the shell-4 intra-shell neighbours
    # splitting as 3 ico + 3 dod (discovered by the lumped computation).
    key = (4, "dod")
    trapped_row = counts[key]
    intra_dod = trapped_row.get((4, "dod"), 0)
    intra_ico = trapped_row.get((4, "ico"), 0)
    shell3_ico = trapped_row.get((3, "ico"), 0)
    shell3_dod = trapped_row.get((3, "dod"), 0)
    shell5 = trapped_row.get((5, "all"), 0)
    assert shell5 == 0, f"trapped vertex should have no shell-5 neighbour; got {shell5}"
    assert shell3_ico + shell3_dod == 6, f"expected 6 shell-3 neighbours total; got {shell3_ico + shell3_dod}"
    assert intra_ico + intra_dod == 6, f"expected 6 intra-shell-4 neighbours; got {intra_ico + intra_dod}"
    print()
    print(f"Trapped (4, 'dod') lumped transition row: {dict(trapped_row)}")
    print(f"  of the 6 shell-4 intra-shell neighbours: {intra_ico} ico + {intra_dod} dod")
    print(f"  of the 6 shell-3 neighbours:             {shell3_ico} ico + {shell3_dod} dod")

    # Set up absorbing chain: shell 3 (both populations) + shell 5 absorbing.
    absorbing = {(3, "ico"), (3, "dod"), (5, "all")}
    results = solve_rational_absorbing_chain(states, counts, absorbing, degree=12)

    # From the trapped state (4, "dod"), compute p_in and p_out.
    trapped_state = (4, "dod")
    probs = results[trapped_state]
    p_shell3_ico = probs[(3, "ico")]
    p_shell3_dod = probs[(3, "dod")]
    p_shell5 = probs[(5, "all")]
    p_in = p_shell3_ico + p_shell3_dod
    p_out = p_shell5
    print()
    print(f"Exact first-passage probabilities from trapped state (4, 'dod'):")
    print(f"  P(hit shell 3 ico) = {p_shell3_ico} = {float(p_shell3_ico):.6f}")
    print(f"  P(hit shell 3 dod) = {p_shell3_dod} = {float(p_shell3_dod):.6f}")
    print(f"  P(hit shell 5)     = {p_shell5} = {float(p_shell5):.6f}")
    print(f"  P(hit shell 3)     = {p_in} = {float(p_in):.6f}")
    print(f"  P(hit shell 5)     = {p_out} = {float(p_out):.6f}")
    print(f"  sum check = {p_in + p_out}")
    assert p_in + p_out == Fraction(1, 1)

    R_D4 = p_in / p_out
    print()
    print(f"R_D(4) = P(shell 3) / P(shell 5) = {p_in} / {p_out} = {R_D4}")
    print()

    if R_D4 == Fraction(15, 1):
        print("THEOREM CONFIRMED: R_D(4) = 15 exactly (as rational number).")
    else:
        print(f"R_D(4) = {R_D4} (not 15 exactly; paper claim would need revision).")

    # Also compute R from each other transient state (sanity / cross-check).
    print()
    print("All first-passage probabilities from transient states:")
    print(f"{'state':>15} {'P(shell3)':>12} {'P(shell5)':>12} {'R = in/out':>15}")
    print("-" * 60)
    for s in sorted(results.keys(), key=lambda s: (s[0], s[1] or "")):
        probs = results[s]
        p_in_s = probs[(3, "ico")] + probs[(3, "dod")]
        p_out_s = probs[(5, "all")]
        if p_out_s == 0:
            R = "inf"
        else:
            R = f"{p_in_s / p_out_s}"
        print(f"{str(s):>15} {str(p_in_s):>12} {str(p_out_s):>12} {R:>15}")


if __name__ == "__main__":
    main()
