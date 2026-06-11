# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Lee Smart / Institute of Vibrational Field Dynamics
"""
Explicit 2I edge-space action on V_600 — math derivation + numerical witness.

Closes ACT open item 6 (edge-space decomposition and cascade-selection lift)
and the codex round-9 deferred must-fix on the E_8 ⊕ V_600 product graph
notation.

DERIVATION
==========

V_600 (the 600-cell vertex set) admits a quaternion identification with the
binary icosahedral group 2I:

    V_600 = {120 unit quaternions of 2I} ⊂ S³ ⊂ ℍ.

Identifying R^4 with ℍ via (a, b, c, d) ↔ a + bi + cj + dk, V_600 is closed
under quaternion multiplication and forms the 2I group.

The natural left-action of 2I on itself is the regular action:

    π_g : V_600 → V_600,  v ↦ g · v   (quaternion product).

This action lifts canonically to the edge set E_M of the 600-cell graph:
for an edge {v, w} ∈ E_M, define

    π_g({v, w}) := {g · v, g · w}.

The lifted action is well-defined (V_600 closed under multiplication; edge
adjacency is left-invariant since <gv, gw> = <v, w> for unit quaternion g).

THEOREM (proved numerically below)
----------------------------------
Under the 2I left-action:
  (a) 2I acts freely on V_600 (regular action; stabilizer trivial).
  (b) 2I acts freely on E_M (no edge {v, w} is fixed by any non-identity
      g, because g · v = w forces g² = 1 ⇒ g = -1, but -v ≠ w for
      nearest-neighbour pairs in V_600).
  (c) Therefore E_M decomposes as exactly 6 free 2I-orbits, each of size
      |2I| = 120, giving 6 · 120 = 720 = |E_M|.
  (d) The carrier R^E_M ≅ 6 · R[2I] decomposes as

          R^E_M  ≅  ⊕_{i=1}^{9} (6 · dim ρ_i) · ρ_i

      where {ρ_1, …, ρ_9} are the 9 irreducible representations of 2I
      with dimensions {1, 2, 2, 3, 3, 4, 4, 5, 6} and Σ dim²ρ_i = 120.
      The isotypic component for ρ_i has dimension 6 · (dim ρ_i)² with
      total Σ_i 6·(dim ρ_i)² = 6·120 = 720.

CASCADE-SELECTION CONSEQUENCE
-----------------------------
ACT Hypothesis hyp:cascade-selection requires 2I-equivariance of the
learning rule on the edge space R^{E_M} where W lives. This script
provides the explicit edge-space decomposition that hypothesis was
written to be conditional on. With the 6-orbit / 9-isotypic structure
in hand, the cascade-selection statement promotes from "deferred edge-
space lift" to "edge-space lift delivered; remaining open is the
construction of a Lyapunov potential V(W) compatible with this
decomposition."

EXPECTED OUTPUT
---------------
Reproduces (writes to results.json):

  v600_size           = 120
  is_2I_under_quat    = true     (closed under multiplication; identity present)
  group_law_holds     = true     (π_g ∘ π_h = π_{g·h} on 200 random pairs)
  n_edges             = 720
  edges_preserved     = true     (g·E_M = E_M for all 120 g ∈ 2I)
  edge_orbit_count    = 6        (THEOREM 6-orbit witness)
  edge_orbit_sizes    = [120]·6  (free action; each orbit size = |2I|)
  isotypic_dims       = [6, 24, 24, 54, 54, 96, 96, 150, 216]
  isotypic_dims_sum   = 720      (= |E_M|)
"""
from __future__ import annotations

import json
import math
import os
import sys
from typing import Dict, List, Tuple

import numpy as np

PHI = (1.0 + math.sqrt(5.0)) / 2.0


# ─────────────────────── V_600 vertex construction ────────────────────

def build_600cell_vertices() -> np.ndarray:
    """120 vertices of the 600-cell on the unit S³.

    Three orbit classes under H_4:
      A:  ±e_i                                                (8 vertices)
      B:  (±½, ±½, ±½, ±½)                                    (16 vertices)
      C:  even-permutations of (±φ/2, ±½, ±1/(2φ), 0)         (96 vertices)

    The vertex at index 0 must be the quaternion identity (1, 0, 0, 0)
    so that the left-multiplication action is referenced from the
    identity vertex; we ensure this by sorting the A class first.
    """
    verts: List[List[float]] = []

    # Class A: ±e_i. Place +e_0 = (1,0,0,0) FIRST so that vertex 0 is the
    # quaternion identity (essential for the 2I action to be referenced
    # from the identity).
    verts.append([1.0, 0.0, 0.0, 0.0])
    for s in (-1,):
        verts.append([s * 1.0, 0.0, 0.0, 0.0])
    for i in range(1, 4):
        for s in (1, -1):
            v = [0.0, 0.0, 0.0, 0.0]
            v[i] = s
            verts.append(v)

    # Class B: (±½, ±½, ±½, ±½)
    for s0 in (1, -1):
        for s1 in (1, -1):
            for s2 in (1, -1):
                for s3 in (1, -1):
                    verts.append([s0 * 0.5, s1 * 0.5, s2 * 0.5, s3 * 0.5])

    # Class C: even-permutations of (±φ/2, ±½, ±1/(2φ), 0)
    base = [PHI / 2.0, 0.5, 1.0 / (2.0 * PHI), 0.0]
    even_perms = [
        (0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2),
        (1, 0, 3, 2), (1, 2, 0, 3), (1, 3, 2, 0),
        (2, 0, 1, 3), (2, 1, 3, 0), (2, 3, 0, 1),
        (3, 0, 2, 1), (3, 1, 0, 2), (3, 2, 1, 0),
    ]
    for perm in even_perms:
        for s0 in (1, -1):
            for s1 in (1, -1):
                for s2 in (1, -1):
                    vals = [s0 * base[0], s1 * base[1], s2 * base[2], 0.0]
                    v = [0.0, 0.0, 0.0, 0.0]
                    for i, p in enumerate(perm):
                        v[p] = vals[i]
                    verts.append(v)

    arr = np.asarray(verts, dtype=float)
    arr = arr / np.linalg.norm(arr, axis=1, keepdims=True)

    unique: List[np.ndarray] = [arr[0]]
    for v in arr[1:]:
        if all(np.linalg.norm(v - u) > 0.01 for u in unique):
            unique.append(v)
    out = np.asarray(unique[:120], dtype=float)
    assert out.shape == (120, 4), f"expected 120 vertices, got {out.shape}"
    # Confirm vertex 0 is the quaternion identity.
    assert np.linalg.norm(out[0] - np.array([1.0, 0.0, 0.0, 0.0])) < 1e-12
    return out


# ─────────────────────── quaternion multiplication ────────────────────

def quat_mul(q1: np.ndarray, q2: np.ndarray) -> np.ndarray:
    """Hamilton product (a + bi + cj + dk)(a' + b'i + c'j + d'k).

    Standard formula; the scalar part is a·a' minus the dot product of
    the vector parts, the vector part is a·v' + a'·v + v × v'.
    """
    a1, b1, c1, d1 = q1
    a2, b2, c2, d2 = q2
    return np.array([
        a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2,
        a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
        a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
        a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2,
    ], dtype=float)


def find_vertex_index(v: np.ndarray, verts: np.ndarray, tol: float = 1e-6) -> int:
    """Return the index of v in verts (within tolerance), or -1 if absent."""
    diffs = np.linalg.norm(verts - v, axis=1)
    j = int(np.argmin(diffs))
    return j if diffs[j] < tol else -1


# ─────────────────────── 2I left-action on V_600 ──────────────────────

def build_left_action_permutations(verts: np.ndarray) -> np.ndarray:
    """Build the 120×120 permutation table π[g, v] = j such that g·v = verts[j].

    Asserts V_600 is closed under quaternion multiplication (i.e. forms a
    subgroup of unit quaternions, which is exactly the 2I subgroup).
    """
    n = verts.shape[0]
    perms = -np.ones((n, n), dtype=np.int64)
    for g_idx in range(n):
        for v_idx in range(n):
            gv = quat_mul(verts[g_idx], verts[v_idx])
            j = find_vertex_index(gv, verts)
            if j < 0:
                raise AssertionError(
                    f"V_600 not closed: verts[{g_idx}] · verts[{v_idx}] = {gv} "
                    f"not in V_600. The vertex set is not the 2I subgroup."
                )
            perms[g_idx, v_idx] = j
    return perms


def verify_group_law(perms: np.ndarray, n_samples: int = 200,
                     seed: int = 42) -> bool:
    """Spot-check π_g ∘ π_h = π_{g·h} on `n_samples` random pairs.

    The full check is 120³ = 1.7M ops which is feasible but slow; this
    sampling pass is sufficient to catch any structural error.
    """
    rng = np.random.default_rng(seed)
    n = perms.shape[0]
    # Recover the group product from permutations: g·h = π_g(h) when h is
    # a vertex (which it is, since V_600 = 2I as a set).
    for _ in range(n_samples):
        g = int(rng.integers(0, n))
        h = int(rng.integers(0, n))
        v = int(rng.integers(0, n))
        # (g·h)·v
        gh = perms[g, h]                # the index of g·h in V_600
        lhs = perms[gh, v]
        # g·(h·v)
        rhs = perms[g, perms[h, v]]
        if lhs != rhs:
            return False
    return True


# ─────────────────────── edge construction + edge action ──────────────

def build_edges(verts: np.ndarray, target_ip: float = PHI / 2.0,
                tol: float = 1e-3) -> List[Tuple[int, int]]:
    """Edges of the 600-cell graph: pairs with <v, w> = φ/2 (angle 36°)."""
    n = verts.shape[0]
    edges: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(i + 1, n):
            if abs(float(np.dot(verts[i], verts[j])) - target_ip) < tol:
                edges.append((i, j))
    return edges


def edge_action_well_defined(edges: List[Tuple[int, int]],
                             perms: np.ndarray) -> bool:
    """Verify g · {v, w} ∈ E_M for every g ∈ 2I and every edge {v, w}."""
    edge_set = {edge for edge in edges}
    n_group = perms.shape[0]
    for (i, j) in edges:
        for g in range(n_group):
            gi = int(perms[g, i])
            gj = int(perms[g, j])
            new_edge = (min(gi, gj), max(gi, gj))
            if new_edge not in edge_set:
                return False
    return True


def compute_edge_orbits(edges: List[Tuple[int, int]],
                        perms: np.ndarray) -> np.ndarray:
    """Orbit decomposition of E_M under the lifted 2I action.

    Returns array `orbit_id[e]` ∈ {0, …, n_orbits−1} for each edge index.
    """
    edge_index: Dict[Tuple[int, int], int] = {edge: idx for idx, edge in enumerate(edges)}
    n_edges = len(edges)
    orbit_id = -np.ones(n_edges, dtype=np.int64)
    n_group = perms.shape[0]
    next_orbit = 0
    for e_idx, edge in enumerate(edges):
        if orbit_id[e_idx] != -1:
            continue
        orbit_id[e_idx] = next_orbit
        i0, j0 = edge
        for g in range(n_group):
            gi = int(perms[g, i0])
            gj = int(perms[g, j0])
            new_edge = (min(gi, gj), max(gi, gj))
            ne_idx = edge_index.get(new_edge, -1)
            if ne_idx >= 0 and orbit_id[ne_idx] == -1:
                orbit_id[ne_idx] = next_orbit
        next_orbit += 1
    return orbit_id


# ─────────────────────── isotypic-dimension theorem ───────────────────

# Dimensions of the 9 irreducible representations of 2I (binary icosahedral
# group, also known as 2.A_5 or SL(2, F_5)).
IRREP_DIMS_2I = (1, 2, 2, 3, 3, 4, 4, 5, 6)


def expected_isotypic_dims(n_orbits: int = 6) -> List[int]:
    """Closed-form: ρ_i appears in n_orbits · R[2I] with multiplicity
    n_orbits · dim ρ_i, so its isotypic component has dimension
    n_orbits · (dim ρ_i)².
    """
    return [n_orbits * d * d for d in IRREP_DIMS_2I]


# ─────────────────────── main verification ────────────────────────────

def main() -> int:
    print("=" * 72)
    print("  Explicit 2I edge-space action on V_600 (ACT open item 6)")
    print("=" * 72)

    print("\n[1/6] building V_600 and verifying quaternion-identity at index 0…")
    verts = build_600cell_vertices()
    print(f"      |V_600| = {verts.shape[0]}; verts[0] = {verts[0].tolist()}")

    print("\n[2/6] building 2I left-action permutations (120×120)…")
    perms = build_left_action_permutations(verts)
    is_2i = True                     # asserted inside build_left_action_permutations
    print(f"      V_600 is closed under quaternion multiplication: {is_2i}")
    print(f"      → V_600 = 2I (binary icosahedral group), |2I| = 120 ✓")

    print("\n[3/6] verifying group law π_g ∘ π_h = π_{g·h} on 200 random samples…")
    group_law_ok = verify_group_law(perms)
    print(f"      group_law_holds: {group_law_ok}")

    print("\n[4/6] building short-edge adjacency (<v, w> = φ/2)…")
    edges = build_edges(verts)
    print(f"      |E_M| = {len(edges)}")

    print("\n[5/6] verifying edge action well-defined (g · E_M ⊆ E_M for all g)…")
    edges_preserved = edge_action_well_defined(edges, perms)
    print(f"      edges_preserved: {edges_preserved}")

    print("\n[6/6] computing edge orbits under 2I action…")
    orbit_id = compute_edge_orbits(edges, perms)
    n_orbits = int(orbit_id.max()) + 1
    orbit_sizes = [int((orbit_id == k).sum()) for k in range(n_orbits)]
    print(f"      number of 2I-orbits on E_M: {n_orbits}")
    print(f"      orbit sizes: {orbit_sizes}")
    print(f"      sum of orbit sizes: {sum(orbit_sizes)} (expected {len(edges)})")

    expected_iso = expected_isotypic_dims(n_orbits)
    print(f"\n  Isotypic decomposition (closed form, n_orbits · (dim ρ_i)²):")
    print(f"  irrep dims of 2I:        {list(IRREP_DIMS_2I)}")
    print(f"  isotypic component dim:  {expected_iso}")
    print(f"  Σ dim:                   {sum(expected_iso)} (expected {len(edges)})")

    free_action = all(s == perms.shape[0] for s in orbit_sizes)
    n_orbits_correct = (n_orbits == 6)
    iso_sum_correct = (sum(expected_iso) == len(edges))

    all_pass = (is_2i and group_law_ok and edges_preserved and
                free_action and n_orbits_correct and iso_sum_correct)

    print(f"\n  ═══ THEOREM CHECK: {6 if all_pass else 'FAIL'}/6 conditions met ═══")
    print(f"     V_600 = 2I:             {is_2i}")
    print(f"     group law on V_600:     {group_law_ok}")
    print(f"     edge action defined:    {edges_preserved}")
    print(f"     2I acts freely on E_M:  {free_action}")
    print(f"     n_orbits == 6:          {n_orbits_correct}")
    print(f"     isotypic dims sum 720:  {iso_sum_correct}")

    results = {
        "v600_size": int(verts.shape[0]),
        "is_2I_under_quat": bool(is_2i),
        "group_law_holds": bool(group_law_ok),
        "n_edges": int(len(edges)),
        "edges_preserved": bool(edges_preserved),
        "edge_orbit_count": int(n_orbits),
        "edge_orbit_sizes": orbit_sizes,
        "irrep_dims_2I": list(IRREP_DIMS_2I),
        "isotypic_dims": expected_iso,
        "isotypic_dims_sum": int(sum(expected_iso)),
        "free_action_on_edges": bool(free_action),
        "all_six_conditions_pass": bool(all_pass),
    }
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "results_2I_edge_action.json")
    with open(out_path, "w") as fh:
        json.dump(results, fh, indent=2)
    print(f"\n  Wrote {out_path}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
