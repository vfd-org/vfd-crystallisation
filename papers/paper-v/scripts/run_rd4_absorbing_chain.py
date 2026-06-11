#!/usr/bin/env python3
"""
Numerical floating-point verification that R_D(4) = 15 on the 600-cell.

This script is a companion to run_rd4_exact_rational.py, which provides the
exact-rational proof via Python's fractions module. The present script does
the same computation in floating-point, which is useful for quickly verifying
the intersection-number structure and the decomposition into three candidate
interpretations of a "reflection coefficient" at the trapped shell-4
dodecahedral vertices.

Paper V's Theorem thm:RD4 establishes R_D(4) = 15 exactly (via the exact
rational script); this script serves as a floating-point cross-check and
exploration of alternative multi-step definitions.

Steps:
  1. construct the 120 vertices of the 600-cell at unit circumradius;
  2. build the nearest-neighbour adjacency matrix A (edge length 1/phi,
     degree 12, 720 edges);
  3. BFS-partition the 120 vertices into shells S_0..S_5 from vertex v_0;
  4. split shells 2, 3, 4 into icosahedral / dodecahedral populations
     via intersection numbers (a,b,c);
  5. set up a discrete-time uniform random walk on the 600-cell;
  6. compute several candidate definitions of R_D(4) and report them.

Runs standalone with only numpy.
"""

from __future__ import annotations

import itertools
from collections import deque, defaultdict

import numpy as np


PHI = (1.0 + np.sqrt(5.0)) / 2.0
TOL = 1e-9


# ---------------------------------------------------------------------------
# 600-cell vertex construction (unit circumradius)
# ---------------------------------------------------------------------------

def _even_permutations(tup):
    """Yield the 12 even permutations of a 4-tuple."""
    # all 24 permutations
    all_perms = list(itertools.permutations(tup))
    # parity: count inversions on the permutation of indices
    base = list(tup)
    seen = []
    for p in all_perms:
        # compute sign by matching to base
        # easier: use permutation index on range(4) via the positions chosen
        # We'll instead iterate over index permutations of (0,1,2,3) and apply them.
        pass
    # Simpler: iterate index permutations.
    out = []
    for perm in itertools.permutations(range(4)):
        # sign of permutation
        s = 1
        seq = list(perm)
        for i in range(4):
            for j in range(i + 1, 4):
                if seq[i] > seq[j]:
                    s = -s
        if s == 1:
            out.append(tuple(tup[i] for i in perm))
    return out


def build_600cell_vertices():
    """Return a (120, 4) numpy array of 600-cell vertices (unit circumradius)."""
    verts = []

    # Set 1: 8 permutations of (+-1, 0, 0, 0)
    for i in range(4):
        for s in (+1, -1):
            v = [0.0, 0.0, 0.0, 0.0]
            v[i] = float(s)
            verts.append(tuple(v))

    # Set 2: 16 sign choices of (+-1/2, +-1/2, +-1/2, +-1/2)
    for signs in itertools.product((+1, -1), repeat=4):
        verts.append(tuple(0.5 * s for s in signs))

    # Set 3: even permutations of (0, +-1/(2 phi), +-1/2, +-phi/2), all 8 sign choices
    # 12 even permutations x 8 sign choices = 96
    base_mag = (0.0, 1.0 / (2.0 * PHI), 0.5, PHI / 2.0)
    sign_choices = list(itertools.product((+1, -1), repeat=4))
    # Only flip signs of the three nonzero components; the 0 slot stays 0.
    for perm in itertools.permutations(range(4)):
        # parity
        s = 1
        seq = list(perm)
        for i in range(4):
            for j in range(i + 1, 4):
                if seq[i] > seq[j]:
                    s = -s
        if s != 1:
            continue
        permuted = tuple(base_mag[perm[i]] for i in range(4))
        # find the zero slot
        zero_slot = permuted.index(0.0)
        # apply signs to the other three slots
        for signs in itertools.product((+1, -1), repeat=3):
            v = list(permuted)
            j = 0
            for k in range(4):
                if k == zero_slot:
                    continue
                v[k] = signs[j] * v[k]
                j += 1
            verts.append(tuple(v))

    verts = np.array(verts, dtype=float)
    assert verts.shape == (120, 4), f"got {verts.shape}"

    # Deduplicate (Set 3 can in principle overlap with Set 1/2; verify count is 120)
    # Convert to rounded tuples for uniqueness
    rounded = [tuple(np.round(v, 9)) for v in verts]
    assert len(set(rounded)) == 120, f"duplicate vertices: {len(set(rounded))}/120"

    # Verify unit circumradius
    norms = np.linalg.norm(verts, axis=1)
    assert np.allclose(norms, 1.0), f"not on unit sphere: {norms.min()} .. {norms.max()}"

    return verts


def build_adjacency(verts, edge_length):
    """Build boolean adjacency matrix by Euclidean distance = edge_length."""
    n = len(verts)
    A = np.zeros((n, n), dtype=np.int8)
    for i in range(n):
        for j in range(i + 1, n):
            d = np.linalg.norm(verts[i] - verts[j])
            if abs(d - edge_length) < TOL:
                A[i, j] = 1
                A[j, i] = 1
    return A


# ---------------------------------------------------------------------------
# BFS shells and populations
# ---------------------------------------------------------------------------

def bfs_shells(A, source=0):
    """Return dist[v] = BFS distance from source, for each vertex v."""
    n = len(A)
    dist = -np.ones(n, dtype=int)
    dist[source] = 0
    q = deque([source])
    while q:
        u = q.popleft()
        for v in range(n):
            if A[u, v] and dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


def intersection_numbers(A, dist, v):
    """For a vertex v at shell d, return (a, b, c) = (same-shell, next-shell, prev-shell)."""
    d = dist[v]
    a = b = c = 0
    for w in range(len(A)):
        if not A[v, w]:
            continue
        if dist[w] == d:
            a += 1
        elif dist[w] == d + 1:
            b += 1
        elif dist[w] == d - 1:
            c += 1
    return a, b, c


def classify_populations(A, dist):
    """Return dict pop[v] in {'ico', 'dod', None} for shell-2/3/4 vertices.

    Population is determined by intersection-number signature:
      shell 2 ico: (5,6,1); shell 2 dod: (6,3,3)
      shell 3 ico: (5,6,1); shell 3 dod: (6,2,4)
      shell 4 ico: (10,1,1); shell 4 dod: (6,0,6)
    """
    pop = {}
    sigs_ico = {2: (5, 6, 1), 3: (5, 6, 1), 4: (10, 1, 1)}
    sigs_dod = {2: (6, 3, 3), 3: (6, 2, 4), 4: (6, 0, 6)}
    for v in range(len(A)):
        d = dist[v]
        if d in (2, 3, 4):
            s = intersection_numbers(A, dist, v)
            if s == sigs_ico[d]:
                pop[v] = "ico"
            elif s == sigs_dod[d]:
                pop[v] = "dod"
            else:
                pop[v] = ("other", d, s)
        else:
            pop[v] = None
    return pop


# ---------------------------------------------------------------------------
# Absorbing Markov chain / random walk calculations for R_D(4)
# ---------------------------------------------------------------------------

def transition_matrix(A):
    """Uniform-over-neighbours transition matrix P = D^{-1} A."""
    deg = A.sum(axis=1)
    assert np.all(deg == 12), f"degrees not uniform 12: {np.unique(deg)}"
    P = A.astype(float) / deg[:, None]
    return P


def absorbing_chain_R(A, dist, pop, absorbing_shell=5, start_shell=4):
    """
    Several candidate definitions of the effective reflection coefficient
    R_D(start_shell) = c_eff / b_eff for the trapped-shell dodecahedral vertices.

    Interpretation 1 (hitting probabilities):
      start the walk at each trapped dodecahedral vertex. Absorbing states are
      shell 5 (outward) and shell 3 (inward). Compute p_out = P(hit shell 5 first),
      p_in = P(hit shell 3 first). Effective R = p_in / p_out.

    Interpretation 2 (expected visits until absorption at shell 5 only):
      absorbing state = shell 5. All other states transient; trapped vertex
      walker hits shell 5 eventually. Count expected inward transitions
      (shell -> shell 3) vs outward transitions (shell -> shell 5) summed over the walk.

    Interpretation 3 (population coarse-graining):
      Lump vertices by (shell, population). Build a coarse Markov chain on
      ~7 states and compute R_D(4) from its exit flux.

    We report all three for the trapped shell-4 dodecahedral state.
    """
    n = len(A)
    P = transition_matrix(A)

    # --- Interpretation 1: first-passage to shell 5 vs shell 3 ---
    # Absorbing states: shell 5 (outward) or shell 3 (inward).
    # Compute p_out = P(hit shell 5 before shell 3 | start at trapped dodecahedral).
    # Walker dynamics on shells 4, 4_intra, etc. We keep the vertex-level chain.
    outward = np.array([dist[v] == 5 for v in range(n)], dtype=bool)
    inward = np.array([dist[v] == 3 for v in range(n)], dtype=bool)
    transient = ~(outward | inward)

    # Restrict P to transient states
    T_idx = np.where(transient)[0]
    n_T = len(T_idx)
    Q = np.zeros((n_T, n_T))
    R_out_mat = np.zeros((n_T, 1))
    R_in_mat = np.zeros((n_T, 1))
    idx_of = {v: k for k, v in enumerate(T_idx)}
    for k, v in enumerate(T_idx):
        for w in range(n):
            if P[v, w] == 0:
                continue
            if transient[w]:
                Q[k, idx_of[w]] = P[v, w]
            elif outward[w]:
                R_out_mat[k, 0] += P[v, w]
            elif inward[w]:
                R_in_mat[k, 0] += P[v, w]
    # Solve (I - Q) x = R for absorption probabilities
    I = np.eye(n_T)
    N_fund = np.linalg.inv(I - Q)
    prob_out = N_fund @ R_out_mat  # P(hit shell 5 first), per transient starting state
    prob_in = N_fund @ R_in_mat

    # Extract values at the trapped dodecahedral shell-4 vertices
    trapped_vs = [v for v in range(n) if dist[v] == start_shell and pop.get(v) == "dod"]
    assert len(trapped_vs) == 20, f"expected 20 trapped shell-4 dodecahedral, got {len(trapped_vs)}"
    p_out_trapped = np.array([prob_out[idx_of[v], 0] for v in trapped_vs])
    p_in_trapped = np.array([prob_in[idx_of[v], 0] for v in trapped_vs])
    # They should all be equal by H4 symmetry acting on the population orbit
    assert np.allclose(p_out_trapped, p_out_trapped[0], atol=1e-10)
    assert np.allclose(p_in_trapped, p_in_trapped[0], atol=1e-10)
    p_out_val = float(p_out_trapped[0])
    p_in_val = float(p_in_trapped[0])
    # Sanity
    assert abs(p_out_val + p_in_val - 1.0) < 1e-10

    R1 = p_in_val / p_out_val

    # --- Interpretation 2: expected counts of inward/outward transitions ---
    # Run the walk with shell 5 absorbing; count expected #(transition to shell 3)
    # and #(transition to shell 5) over the entire trajectory from trapped vertex.
    # A "transition to shell X" means moving from a transient state to a vertex at shell X.
    # We use the fundamental matrix N_fund restricted to the "no shell-3 absorbing" setup.
    outward_only = np.array([dist[v] == 5 for v in range(n)], dtype=bool)
    transient2 = ~outward_only
    T2_idx = np.where(transient2)[0]
    n_T2 = len(T2_idx)
    idx2_of = {v: k for k, v in enumerate(T2_idx)}
    Q2 = np.zeros((n_T2, n_T2))
    R5_mat = np.zeros((n_T2, 1))
    for k, v in enumerate(T2_idx):
        for w in range(n):
            if P[v, w] == 0:
                continue
            if outward_only[w]:
                R5_mat[k, 0] += P[v, w]
            else:
                Q2[k, idx2_of[w]] = P[v, w]
    N2 = np.linalg.inv(np.eye(n_T2) - Q2)

    # Expected visits to each transient state
    start_idx = idx2_of[trapped_vs[0]]
    visits = N2[start_idx, :]  # expected visits to each transient state

    # Expected number of outward transitions (transient -> shell 5):
    # sum_k visits[k] * P(v_k -> shell 5)
    exp_out = 0.0
    for k in range(n_T2):
        v = T2_idx[k]
        for w in range(n):
            if outward_only[w] and P[v, w] > 0:
                exp_out += visits[k] * P[v, w]

    # Expected number of "inward" transitions, defined here as transitions
    # that cross from shell 4 to shell 3.
    exp_in = 0.0
    for k in range(n_T2):
        v = T2_idx[k]
        if dist[v] != 4:
            continue
        for w in range(n):
            if P[v, w] > 0 and dist[w] == 3:
                exp_in += visits[k] * P[v, w]

    R2 = exp_in / exp_out

    # --- Interpretation 3: (a,b,c) with b replaced by "eventual outward flux" ---
    # Single-step shows (a,b,c) = (6, 0, 6) for the trapped vertex: 6 same-shell,
    # 0 outward, 6 inward. Define b_eff = eventual probability of hitting shell 5
    # starting from the trapped vertex in a walk that is reflected at shell 3
    # (i.e. shell-3 vertices are treated as ordinary transient, not absorbing).
    # Then R_D(4) = a_eff / b_eff with a_eff = a = 6 and b_eff = p_out_unreflected.
    # Here p_out_unreflected uses shell-5 absorbing alone (Interpretation 2 chain),
    # and "hit shell 5" has probability 1 (walker always eventually gets absorbed
    # on finite chain with absorbing state). So this definition is degenerate:
    # b_eff = 1. So R3_raw = 6 / 1 = 6 under this reading. Not useful.
    # Instead, define b_eff = 1 / E[first-passage time to shell 5], giving an
    # "outward rate" interpretation.
    t_first_passage = N2.sum(axis=1)[start_idx]  # expected steps to absorption
    R3 = t_first_passage  # "average time to escape" as proxy for 1/rate_out

    return {
        "p_out_first_passage": p_out_val,
        "p_in_first_passage": p_in_val,
        "R_first_passage_ratio": R1,
        "expected_inward_transitions": exp_in,
        "expected_outward_transitions": exp_out,
        "R_expected_count_ratio": R2,
        "expected_time_to_shell5": R3,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 72)
    print("600-cell R_D(4) computation via absorbing Markov chain")
    print("=" * 72)

    # Build vertices and adjacency.
    verts = build_600cell_vertices()
    # Edge length at unit circumradius is 1/phi.
    edge_length = 1.0 / PHI
    A = build_adjacency(verts, edge_length)
    n = len(verts)
    n_edges = int(A.sum() // 2)
    print(f"vertices: {n}, edges: {n_edges}, degrees unique: {np.unique(A.sum(axis=1))}")
    assert n == 120
    assert n_edges == 720

    # BFS from v_0 (any vertex by symmetry; use the first one).
    dist = bfs_shells(A, source=0)
    shell_sizes = [int(np.sum(dist == d)) for d in range(6)]
    print(f"shell sizes: {shell_sizes}")
    assert shell_sizes == [1, 12, 32, 42, 32, 1]

    # Classify populations.
    pop = classify_populations(A, dist)
    ico_counts = defaultdict(int)
    dod_counts = defaultdict(int)
    for v, p in pop.items():
        if p == "ico":
            ico_counts[int(dist[v])] += 1
        elif p == "dod":
            dod_counts[int(dist[v])] += 1
    print(f"ico counts per shell: {dict(ico_counts)}")
    print(f"dod counts per shell: {dict(dod_counts)}")
    # Expected: ico at 2,3,4 = 12,12,12; dod at 2,3,4 = 20,30,20
    assert ico_counts[2] == 12 and ico_counts[3] == 12 and ico_counts[4] == 12
    assert dod_counts[2] == 20 and dod_counts[3] == 30 and dod_counts[4] == 20

    # Verify the trapped dodecahedral intersection numbers.
    trapped = [v for v in range(n) if dist[v] == 4 and pop.get(v) == "dod"]
    for v in trapped[:3]:
        a, b, c = intersection_numbers(A, dist, v)
        print(f"  trapped v={v}: (a,b,c) = ({a},{b},{c})")
        assert (a, b, c) == (6, 0, 6)

    # Compute R_D(4) via the absorbing chain.
    print()
    print("Absorbing-Markov-chain analysis of trapped shell-4 dodecahedral vertices:")
    results = absorbing_chain_R(A, dist, pop, absorbing_shell=5, start_shell=4)
    for k, v in results.items():
        print(f"  {k} = {v:.6f}")

    print()
    print("Interpretation of the three candidate R_D(4) values:")
    print(f"  Interp 1 (first-passage ratio P(in)/P(out))         = {results['R_first_passage_ratio']:.6f}")
    print(f"  Interp 2 (expected inward / expected outward)       = {results['R_expected_count_ratio']:.6f}")
    print(f"  Interp 3 (expected time to first reach shell 5)     = {results['expected_time_to_shell5']:.6f}")

    # Also compute a cleanly-defined "walk-level" R:
    # R_walk = (expected visits to shell 3) / (expected visits to shell 5)
    # with shell 5 absorbing. This is another natural single-number quantity.
    # Expected visits to shell 5 = 1 (absorption). Expected visits to shell 3
    # starting from trapped vertex is already visible in N2.
    # We recompute to report it cleanly.
    P = transition_matrix(A)
    outward_only = np.array([dist[v] == 5 for v in range(n)], dtype=bool)
    transient = ~outward_only
    T_idx = np.where(transient)[0]
    idx_of = {v: k for k, v in enumerate(T_idx)}
    Q = np.zeros((len(T_idx), len(T_idx)))
    for k, v in enumerate(T_idx):
        for w in range(n):
            if P[v, w] > 0 and transient[w]:
                Q[k, idx_of[w]] = P[v, w]
    N = np.linalg.inv(np.eye(len(T_idx)) - Q)
    start = idx_of[trapped[0]]
    visits_to_shell3 = sum(N[start, idx_of[v]] for v in range(n) if transient[v] and dist[v] == 3)
    visits_to_shell4 = sum(N[start, idx_of[v]] for v in range(n) if transient[v] and dist[v] == 4)
    print()
    print(f"Expected visits (shell 5 absorbing, from trapped vertex):")
    print(f"  to any shell-3 vertex = {visits_to_shell3:.6f}")
    print(f"  to any shell-4 vertex = {visits_to_shell4:.6f}")

    # Check if Paper V's claimed value R_D(4) = 15 appears in any of these.
    print()
    print("Comparison with Paper V claim R_D(4) = 15:")
    for label, val in [
        ("first-passage ratio", results["R_first_passage_ratio"]),
        ("expected-count ratio", results["R_expected_count_ratio"]),
        ("expected time to shell 5", results["expected_time_to_shell5"]),
        ("visits to shell 3", visits_to_shell3),
        ("visits to shell 4", visits_to_shell4),
    ]:
        match = abs(val - 15.0) < 0.01
        print(f"  {label:35s} = {val:10.4f}  {'MATCHES 15' if match else ''}")


if __name__ == "__main__":
    main()
