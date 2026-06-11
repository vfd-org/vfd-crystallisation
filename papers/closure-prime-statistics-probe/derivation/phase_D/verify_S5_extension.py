#!/usr/bin/env python3
"""
DERIVATION Phase D (extension): derive {1, 1, 5, 5} via S_5 action.

The Z/5 decomposition (computed in verify_K_pole_structure.py) doesn't
directly give {1, 1, 5, 5}.  We need to extend Z/5 → S_5 by finding an
involution h with three properties:

  (1) h permutes V_600 as a set bijection.
  (2) h commutes with the V_600 adjacency matrix A (graph automorphism).
  (3) h induces a TRANSPOSITION on the 5 Schläfli cosets (so ⟨g, h⟩ = S_5).

Then decompose each eigenspace of A under S_5 irrep characters, and
look for {1, 1, 5, 5} multiplicity pattern.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from itertools import combinations
from collections import Counter, defaultdict

import numpy as np

PHI    = (1.0 + 5.0 ** 0.5) / 2.0
INVPHI = 1.0 / PHI
TOL    = 1e-6

OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# Reuse standard helpers from earlier
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


def build_perm_from_action(action_fn, V):
    """action_fn: V_600 vertex (4-vec) → 4-vec.
       Returns array pi such that pi[i] = j where action_fn(V[i]) = V[j].
    """
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


def compute_schlafli_partition(V, g_quat):
    """Build the 5 Schläfli cosets g^k · 2T for k = 0..4.
       Returns: list of 5 sets of V_600 indices.
    """
    n = V.shape[0]
    TwoT = V[:24]  # Type A + Type B
    # Find indices of g^k · 2T elements in V
    classes = [[] for _ in range(5)]
    g_pow = np.array([1.0, 0, 0, 0])
    for k in range(5):
        for t in TwoT:
            target = quat_mul(g_pow, t)
            idx = find_vertex(target, V)
            if idx >= 0:
                if idx not in [c for cls in classes[:k] for c in cls]:
                    classes[k].append(idx)
        g_pow = quat_mul(g_pow, g_quat)
    return classes


def induced_perm_on_schlafli(vertex_perm, schlafli_classes):
    """For each Schläfli class k, where does vertex_perm map most of its
       members?  Returns the 5-element permutation."""
    perm = np.zeros(5, dtype=int)
    for k, members in enumerate(schlafli_classes):
        # Compute image of class k under vertex_perm
        images = [int(vertex_perm[i]) for i in members]
        # Find which class contains these images (majority)
        class_counts = Counter()
        for idx in images:
            for j, other_members in enumerate(schlafli_classes):
                if idx in other_members:
                    class_counts[j] += 1
                    break
        if not class_counts:
            return None
        majority = max(class_counts, key=class_counts.get)
        perm[k] = majority
    return perm


def permutation_signature(perm):
    """Sign of permutation (5-element): +1 even, -1 odd."""
    n = len(perm)
    inversions = 0
    for i in range(n):
        for j in range(i+1, n):
            if perm[i] > perm[j]:
                inversions += 1
    return (-1) ** inversions


def cycle_type(perm):
    """Cycle type as sorted tuple."""
    n = len(perm)
    visited = [False]*n
    cycles = []
    for i in range(n):
        if visited[i]: continue
        cycle_len = 0
        j = i
        while not visited[j]:
            visited[j] = True
            cycle_len += 1
            j = int(perm[j])
        cycles.append(cycle_len)
    return tuple(sorted(cycles, reverse=True))


# S_5 character table (rows = irreps, columns = conjugacy classes)
# Class order: 1^5, 2.1^3, 2^2.1, 3.1^2, 3.2, 4.1, 5
S5_CHAR = {
    "(5)_trivial":      [1, 1, 1, 1, 1, 1, 1],
    "(4,1)_std":        [4, 2, 0, 1, -1, 0, -1],
    "(3,2)_dim5_A":     [5, 1, 1, -1, 1, -1, 0],
    "(3,1,1)_dim6":     [6, 0, -2, 0, 0, 0, 1],
    "(2,2,1)_dim5_B":   [5, -1, 1, -1, -1, 1, 0],
    "(2,1,1,1)_sgnstd": [4, -2, 0, 1, 1, 0, -1],
    "(1^5)_sign":       [1, -1, 1, 1, -1, -1, 1],
}
S5_CLASSES = ["1^5", "2.1^3", "2^2.1", "3.1^2", "3.2", "4.1", "5"]
S5_CLASS_SIZES = [1, 10, 15, 20, 20, 30, 24]  # sums to 120


def cycle_type_to_class(ct):
    if ct == (1, 1, 1, 1, 1):  return "1^5"
    if ct == (2, 1, 1, 1):     return "2.1^3"
    if ct == (2, 2, 1):        return "2^2.1"
    if ct == (3, 1, 1):        return "3.1^2"
    if ct == (3, 2):           return "3.2"
    if ct == (4, 1):           return "4.1"
    if ct == (5,):             return "5"
    return "?"


def s5_irrep_multiplicity(traces_by_class, irrep_chars):
    """For a rep with traces[class] given, compute multiplicity of irrep
       with characters irrep_chars[class]."""
    mult = 0
    for cls, size in zip(S5_CLASSES, S5_CLASS_SIZES):
        i = S5_CLASSES.index(cls)
        mult += size * traces_by_class.get(cls, 0) * irrep_chars[i]
    return mult / 120


# ==============================================================
# Main
# ==============================================================

def main():
    print("=" * 78)
    print("Phase D extension: S_5 decomposition of A_{V_600} eigenspaces")
    print("=" * 78)
    print()

    V = build_v600()
    n = V.shape[0]
    print(f"V_600: {n} unit icosians")

    # Build adjacency + spectrum
    diffs = V[:, None, :] - V[None, :, :]
    d2 = np.sum(diffs * diffs, axis=2)
    pos = d2[d2 > 1e-9]
    min_d2 = pos.min()
    A = (np.abs(d2 - min_d2) < 1e-7).astype(float)
    np.fill_diagonal(A, 0.0)
    eigvals, eigvecs = np.linalg.eigh(A)
    distinct = []
    indices_by_eig = []
    for i, ev in enumerate(eigvals):
        if distinct and abs(ev - distinct[-1]) < 1e-5:
            indices_by_eig[-1].append(i)
        else:
            distinct.append(float(ev))
            indices_by_eig.append([i])
    print(f"  Spectrum: {len(distinct)} distinct eigenvalues, "
          f"multiplicities {[len(ix) for ix in indices_by_eig]}")
    print()

    # Build g (order-5)
    g = np.array([INVPHI/2, PHI/2, 0.5, 0.0])
    g_perm = build_perm_from_action(lambda v: quat_mul(g, v), V)
    G_mat  = perm_to_matrix(g_perm)
    print(f"  g (order 5) builds 5-cycle permutation.")
    schlafli = compute_schlafli_partition(V, g)
    schlafli_sizes = [len(c) for c in schlafli]
    print(f"  Schläfli partition sizes: {schlafli_sizes}")
    print()

    # ----- Find involution h with TRANSPOSITION on Schläfli -----
    print("--- Searching for involution h with transposition on Schläfli ---")
    candidates = []
    # Candidate 1: quaternion conjugation
    candidates.append(("quat_conj", lambda v: np.array([v[0], -v[1], -v[2], -v[3]])))
    # Candidate 2-5: single-axis reflections
    for i in range(4):
        def r_i(v, i=i):
            out = v.copy()
            out[i] = -out[i]
            return out
        candidates.append((f"reflect_axis_{i}", r_i))
    # Candidate 6-11: pair-axis (rotations by 180°)
    for i, j in combinations(range(4), 2):
        def r_ij(v, i=i, j=j):
            out = v.copy()
            out[i] = -out[i]
            out[j] = -out[j]
            return out
        candidates.append((f"rotate_180_{i}_{j}", r_ij))
    # Candidate: triple-axis (= reflect remaining axis, equivalent to single)
    # Candidate: 4-axis (inversion v → -v)
    candidates.append(("inversion", lambda v: -v))
    # Candidate: right-multiplication by V_600 vertex of order 2 (= ±1)
    # (already covered by inversion, since -1 ∈ V_600)
    # Candidate: composition of quat_conj with right-multiplication
    # by various V_600 vertices
    for vert_idx in [0, 1, 8, 24]:  # 1, -1, Type B, Type C
        def conj_then_right_mult(v, h=V[vert_idx]):
            cv = np.array([v[0], -v[1], -v[2], -v[3]])
            return quat_mul(cv, h)
        candidates.append((f"conj_rmul_v{vert_idx}", conj_then_right_mult))
    # Coord permutation involutions (swaps)
    for i, j in combinations(range(4), 2):
        def swap_ij(v, i=i, j=j):
            out = v.copy()
            out[i], out[j] = v[j], v[i]
            return out
        candidates.append((f"swap_coords_{i}_{j}", swap_ij))

    found = []
    for name, fn in candidates:
        pi = build_perm_from_action(fn, V)
        if pi is None: continue
        # Check it's order 2
        pi2 = pi[pi]
        if not np.array_equal(pi2, np.arange(n)):
            continue
        # Check commutes with A
        H = perm_to_matrix(pi)
        AH = A @ H
        HA = H @ A
        if not np.allclose(AH, HA, atol=1e-9):
            continue
        # Compute Schläfli permutation
        sch_perm = induced_perm_on_schlafli(pi, schlafli)
        if sch_perm is None: continue
        sign = permutation_signature(sch_perm)
        ct = cycle_type(sch_perm)
        found.append({
            "name": name, "perm": pi, "matrix": H,
            "schlafli_perm": sch_perm.tolist(),
            "signature": sign,
            "cycle_type": ct,
        })
        print(f"  {name:<25}  Schläfli perm: {sch_perm.tolist()}  "
              f"sign={sign:+d}  cycle_type={ct}")
    print()
    if not found:
        print("  No involution found with all 3 properties.")
        return 1

    # Look for transposition (cycle type (2, 1, 1, 1), odd)
    transpositions = [f for f in found if f["cycle_type"] == (2, 1, 1, 1)]
    print(f"  Transpositions found: {len(transpositions)}")
    if not transpositions:
        # Look for any ODD permutation
        odd_perms = [f for f in found if f["signature"] == -1]
        print(f"  Odd permutations found: {len(odd_perms)}")
        if not odd_perms:
            print("  No odd Schläfli permutations.  ⟨g, h⟩ ⊆ A_5.")
            print("  Cannot generate S_5 with single additional involution.")
            return 1
        # Use the simplest odd permutation
        h = odd_perms[0]
    else:
        h = transpositions[0]
    print(f"  Using h = {h['name']} as S_5 generator.")
    print(f"  h Schläfli perm: {h['schlafli_perm']}, cycle type: {h['cycle_type']}, "
          f"sign: {h['signature']}")
    print()

    # Verify ⟨g, h⟩ = S_5 by checking generated group has 120 elements
    # via Schläfli-permutation level
    print("--- Verify ⟨g, h⟩ generates S_5 on Schläfli classes ---")
    # Generate all permutations of {0..4} from ⟨g, h⟩
    g_sch_perm = induced_perm_on_schlafli(g_perm, schlafli)
    print(f"  g Schläfli perm: {g_sch_perm.tolist()}")
    # BFS to enumerate
    from collections import deque
    seen = {tuple(np.arange(5))}
    queue = deque([np.arange(5)])
    while queue:
        p = queue.popleft()
        for q_perm in (g_sch_perm, h["schlafli_perm"]):
            q_arr = np.asarray(q_perm)
            new_p = q_arr[p]
            key = tuple(new_p)
            if key not in seen:
                seen.add(key)
                queue.append(new_p)
    print(f"  Group generated has order: {len(seen)}")
    print(f"  S_5 has order 120: {'matches' if len(seen) == 120 else 'DOES NOT match'}")
    if len(seen) != 120:
        print(f"  ⟨g, h⟩ is a proper subgroup of S_5.  Decomposition may be partial.")
    print()

    # ----- Decompose each eigenspace under S_5 -----
    print("--- S_5 irrep decomposition of each A_{V_600} eigenspace ---")
    print()
    H_mat = h["matrix"]
    # For each S_5 conjugacy class, pick a representative element
    # built from g and h, compute its trace on each eigenspace
    # Class representatives (group elements as products of g and h):
    # We need representatives of all 7 conjugacy classes.
    # Constructions (informal):
    # - 1^5: identity = I
    # - 5: g
    # - 2.1^3: h (transposition)
    # - 2^2.1: g * h * g^{-1} * h, or compute from Schläfli action
    # - 3.1^2: g * h (gives a 3-cycle if h is right kind)
    # - 3.2: ?
    # - 4.1: ?
    # We brute-force: enumerate words in g, h up to length 8; find one of each class
    print("  Building conjugacy-class representatives...")
    word_to_matrix = {tuple(np.arange(n)): np.eye(n)}
    queue = deque([(np.arange(n), np.eye(n), "")])
    found_classes = {}
    g_sch_arr = np.asarray(g_sch_perm)
    h_sch_arr = np.asarray(h["schlafli_perm"])
    max_word_len = 8
    while queue:
        v_perm, v_mat, word = queue.popleft()
        if len(word) > max_word_len:
            continue
        # Compute Schläfli permutation
        sch_perm = induced_perm_on_schlafli(v_perm, schlafli)
        if sch_perm is None:
            continue
        ct = cycle_type(sch_perm)
        cls_name = cycle_type_to_class(ct)
        if cls_name != "?" and cls_name not in found_classes:
            found_classes[cls_name] = {
                "word": word,
                "v_perm": v_perm,
                "v_mat": v_mat,
                "schlafli_perm": sch_perm.tolist(),
            }
        if len(found_classes) == 7:
            break
        for letter, P, sym in (("g", G_mat, g_perm), ("h", H_mat, h["perm"])):
            new_v_perm = sym[v_perm]   # composition
            new_v_mat = P @ v_mat
            queue.append((new_v_perm, new_v_mat, word + letter))
    print(f"  Found {len(found_classes)} of 7 conjugacy classes:")
    for cls in S5_CLASSES:
        if cls in found_classes:
            print(f"    {cls:<10}  word='{found_classes[cls]['word']}'")
        else:
            print(f"    {cls:<10}  NOT FOUND (word length limit)")
    print()

    # If we have all 7 classes, decompose each eigenspace
    if len(found_classes) < 7:
        print("  Cannot do full S_5 decomposition without all 7 class reps.")
        return 1

    # For each eigenspace, compute trace of each class representative
    print("--- Eigenspace decomposition table ---")
    print()
    decomps = {}
    for ev, indices in zip(distinct, indices_by_eig):
        E = eigvecs[:, indices]  # n x dim
        dim_E = len(indices)
        traces_by_class = {}
        for cls in S5_CLASSES:
            v_mat = found_classes[cls]["v_mat"]
            # Trace of v_mat restricted to E
            G_E = E.T @ v_mat @ E
            traces_by_class[cls] = float(np.trace(G_E))
        # Decompose into irreps
        irrep_mults = {}
        for irrep_name, chars in S5_CHAR.items():
            m = s5_irrep_multiplicity(traces_by_class, chars)
            irrep_mults[irrep_name] = round(m)
        decomps[round(ev, 4)] = {
            "dim": dim_E,
            "traces": traces_by_class,
            "irrep_mults": irrep_mults,
        }

    # Print decomposition
    print(f"  {'eigenvalue':<14} {'dim':<5}  S_5 irrep multiplicities")
    print("  " + "-" * 100)
    for ev, info in decomps.items():
        mults_str = " ".join(f"{name.split('_')[0]}:{m}"
                              for name, m in info["irrep_mults"].items()
                              if m != 0)
        print(f"  {ev:+10.4f}    {info['dim']:<5}  {mults_str}")
    print()

    # ----- Look for {1, 1, 5, 5} pattern -----
    print("--- {1, 1, 5, 5} pattern search ---")
    # Pattern: {trivial: 1, sign: 1, dim5_A: 1, dim5_B: 1} in some eigenspace
    target_irreps = ["(5)_trivial", "(1^5)_sign", "(3,2)_dim5_A", "(2,2,1)_dim5_B"]
    for ev, info in decomps.items():
        mults = info["irrep_mults"]
        # Check the four "{1,1,5,5}" irreps appear with multiplicity ≥ 1 each
        if all(mults.get(irrep, 0) >= 1 for irrep in target_irreps):
            print(f"  λ = {ev}: contains all 4 irreps of {{1, 1, 5, 5}} structure!")
            print(f"    multiplicities: {mults}")
    # Also try: pattern is (1, 1, 1, 1) for the 4 target irreps SPECIFICALLY
    for ev, info in decomps.items():
        mults = info["irrep_mults"]
        if (mults.get("(5)_trivial") == 1 and mults.get("(1^5)_sign") == 1
            and mults.get("(3,2)_dim5_A") == 1 and mults.get("(2,2,1)_dim5_B") == 1
            and all(mults.get(other, 0) == 0
                    for other in S5_CHAR if other not in target_irreps)):
            print(f"  λ = {ev}: EXACTLY {{trivial + sign + dim5_A + dim5_B}}!")
            print(f"    dim = 1 + 1 + 5 + 5 = {info['dim']}")

    # Save
    def clean(x):
        if isinstance(x, dict):  return {str(k): clean(v) for k, v in x.items()}
        if isinstance(x, (list, tuple)): return [clean(v) for v in x]
        if isinstance(x, np.ndarray): return x.tolist()
        if isinstance(x, np.integer): return int(x)
        if isinstance(x, np.floating): return float(x)
        return x
    out_summary = {
        "h_chosen":          h["name"],
        "schlafli_perm":     h["schlafli_perm"],
        "schlafli_signature": int(h["signature"]),
        "schlafli_cycle":    h["cycle_type"],
        "generated_group_order": len(seen),
        "decomps":           {str(k): v for k, v in decomps.items()},
    }
    with open(OUTPUT_DIR / "phase_D_S5_results.json", "w") as f:
        json.dump(clean(out_summary), f, indent=2)
    print()
    print(f"Saved {OUTPUT_DIR / 'phase_D_S5_results.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
