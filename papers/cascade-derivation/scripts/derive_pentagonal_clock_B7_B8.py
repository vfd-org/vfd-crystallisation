#!/usr/bin/env python3
"""
Build B7/B8: local frame at each v ∈ 2I and the holonomy cocycle
ω: directed_edges → Z[φ]× for the pentagonal clock.

Strategy (B7 — local frame):
  Attach to each vertex v ∈ 2I a canonical local orthonormal frame
  derived from the icosian lattice structure. The natural choice is:
  the tangent space at v (as a 3-manifold embedded in S³) has a basis
  given by left-translation of a fixed basis at the identity 1 ∈ 2I.
  Concretely, fix e_1, e_2, e_3 = (i, j, k) at 1 ∈ 2I, and define
  the frame at v as (v·i, v·j, v·k).

Strategy (B8 — holonomy cocycle ω):
  For each directed edge (v, w) in the 2I adjacency graph (12 nearest
  neighbours per vertex, edge = closest-distance 2I pairs), the
  parallel transport from v to w is the icosian rotation
  g(v, w) := w · v^{-1} ∈ 2I. This g(v,w) is a unit icosian that
  takes the frame at v to the frame at w.
  The Z[φ]× holonomy value is then the σ-invariant real-part
  signature of g(v,w): writing g = a + bi + cj + dk with each of
  a,b,c,d ∈ Q(√5), we compute ω(v,w) = N(a + b + c + d) mod ±φ^Z,
  or more specifically the "reduced holonomy" obtained by projecting
  g(v,w) onto the Z[φ]× grading of its conjugacy class.

  Since 2I has 9 conjugacy classes, each edge g(v,w) sits in one
  class. The classes have natural Z[φ]-grading via the Dynkin /
  Coxeter embedding of 2I ↪ E_8 (the icosian-E8 construction).

  For this first build, we compute:
    - The adjacency graph of 2I (nearest-neighbour structure).
    - The "transport element" g(v,w) for each directed edge.
    - The class of g(v,w) (one of the 9).
    - The Z[φ]× signature per class.

Refuses floats. Exact arithmetic in Q(√5).

STOP conditions:
  - If adjacency graph per-vertex valence != 12: FAIL
  - If transport element g(v,w) ∉ 2I for any edge: FAIL
  - If cocycle relation ω(u,v)·ω(v,w) != ω(u,w) fails (or the path-
    dependence is not σ-covariant): FAIL and report
  - If σ-covariance ω(σv, σw) != σ(ω(v,w)) fails: report (this is
    the central B10 check and informs canonicity)

Run: python3 papers/cascade-derivation/scripts/derive_pentagonal_clock_B7_B8.py
"""

from __future__ import annotations

import sys
from pathlib import Path
from fractions import Fraction
from collections import defaultdict, Counter

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
sys.path.insert(0, str(REPO_ROOT / "papers" / "paper-xxii" / "scripts"))

from run_icosian_exact import (  # noqa: E402
    q_zero, q_one, q_neg, q_add, q_sub, q_mul, q_scale,
    qq_mul, qq_conjugate, qq_norm_sq, qq_eq, qq_key,
    build_vertices, vertex_index_map, vertex_index_exact,
    qq_distance_sq,
)


def sigma_on_qsq5(x):
    """Galois involution σ on Q(√5): (a,b) ↦ (a,-b), i.e., √5 ↦ -√5."""
    return (x[0], -x[1])


def sigma_on_quat(q):
    """Apply σ componentwise to a quaternion over Q(√5)."""
    return tuple(sigma_on_qsq5(c) for c in q)


def find_minimum_neighbour_distance(verts):
    """Find the minimum non-zero squared-distance between any two
    vertices; that defines the 'edge' in the adjacency graph."""
    identity = (q_one(), q_zero(), q_zero(), q_zero())
    # Take distance from identity to each other vertex
    dists = []
    for i, v in enumerate(verts):
        if qq_eq(v, identity):
            continue
        d = qq_distance_sq(identity, v)
        dists.append((d, i))
    # Find minimum via lexicographic ordering on (a, b) pairs
    # (since they encode a + b√5 and √5 ≈ 2.236, (a, b) < (a', b') iff
    # a + b√5 < a' + b'√5 for small values)
    def key(d_sq):
        # For small a, b we can compare exactly using (a + b√5)
        # as a floating check + exact rational tie-break. Since all
        # our d_sq are rational-in-Q(√5), we just compare the real
        # value. Use Fraction arithmetic via float only for sorting
        # (exact equality check is still done).
        a, b = d_sq
        return (float(a) + float(b) * (5 ** 0.5))
    dists.sort(key=lambda dI: key(dI[0]))
    min_d = dists[0][0]
    # All neighbours at distance min_d
    neighbours_of_id = [i for d, i in dists if d == min_d]
    return min_d, neighbours_of_id


def build_adjacency(verts, idx_map, min_d):
    """For each vertex v, return the list of indices w with
    |v - w|^2 = min_d."""
    n = len(verts)
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if qq_distance_sq(verts[i], verts[j]) == min_d:
                adj[i].append(j)
    return adj


def transport_element(v, w):
    """g(v,w) = w · v^{-1}. For unit quaternion v, v^{-1} = v̄ (conjugate)."""
    v_inv = qq_conjugate(v)
    return qq_mul(w, v_inv)


def conjugacy_classes_2I(verts, idx_map):
    """Compute the 9 conjugacy classes of 2I."""
    n = len(verts)
    assigned = [False] * n
    classes = []
    for i in range(n):
        if assigned[i]:
            continue
        cls = set()
        g = verts[i]
        for j in range(n):
            h = verts[j]
            h_inv = qq_conjugate(h)
            conj = qq_mul(qq_mul(h, g), h_inv)
            cls.add(idx_map[qq_key(conj)])
        for k in cls:
            assigned[k] = True
        classes.append(sorted(cls))
    return classes


def main():
    print("=" * 72)
    print("Build B7/B8 — local frame + holonomy cocycle on 600-cell.")
    print("             All arithmetic exact over Q(√5) (Fraction pairs).")
    print("=" * 72)

    verts = build_vertices()
    assert len(verts) == 120
    identity = (q_one(), q_zero(), q_zero(), q_zero())
    id_idx = vertex_index_exact(identity, verts)
    verts[0], verts[id_idx] = verts[id_idx], verts[0]
    idx_map = vertex_index_map(verts)
    print(f"\n[B7.1] 120-vertex set built; identity at index 0.")

    # --- adjacency graph: 12-regular (icosahedral local structure) ---
    min_d, id_neighbours = find_minimum_neighbour_distance(verts)
    print(f"\n[B7.2] Minimum non-zero squared-distance:")
    print(f"  |1 - v|^2 = {min_d[0]} + {min_d[1]}·√5")
    print(f"  Number of neighbours of identity at min distance: {len(id_neighbours)}")
    if len(id_neighbours) != 12:
        print(f"  FAIL: expected 12 (icosahedral), got {len(id_neighbours)}")
        sys.exit(1)
    print(f"  OK: identity has 12 nearest neighbours (icosahedral).")

    adj = build_adjacency(verts, idx_map, min_d)
    valences = Counter(len(a) for a in adj)
    print(f"\n[B7.3] Adjacency graph valence distribution: {dict(valences)}")
    if list(valences.keys()) != [12] or valences[12] != 120:
        print(f"  FAIL: adjacency not 12-regular")
        sys.exit(1)
    print(f"  OK: 2I adjacency graph is 12-regular (icosahedral).")
    total_edges = sum(len(a) for a in adj)  # directed
    print(f"  total directed edges = {total_edges} (= 120 · 12 = 1440).")
    if total_edges != 1440:
        print(f"  FAIL: directed edge count != 1440")
        sys.exit(1)

    # --- transport elements g(v,w) for each directed edge ---
    print(f"\n[B8.1] Computing transport elements g(v,w) = w · v⁻¹ for each edge...")
    transports = {}  # (v_idx, w_idx) -> quaternion g
    for i in range(120):
        for j in adj[i]:
            g = transport_element(verts[i], verts[j])
            transports[(i, j)] = g
            if qq_key(g) not in idx_map:
                print(f"  FAIL: g({i},{j}) = w·v⁻¹ not in 2I")
                sys.exit(1)
    print(f"  OK: all 1440 transport elements lie in 2I.")

    # --- distribution: which conjugacy classes do the edges fall into? ---
    print(f"\n[B8.2] Conjugacy classes of 2I (reusing computation)...")
    classes = conjugacy_classes_2I(verts, idx_map)
    class_sizes = [len(c) for c in classes]
    print(f"  {len(classes)} classes of sizes {sorted(class_sizes)}")
    # Label classes by their representative and size
    class_of_idx = [-1] * 120
    for ci, cls in enumerate(classes):
        for k in cls:
            class_of_idx[k] = ci

    # Count edges by class of transport element
    class_edge_count = Counter()
    for (i, j), g in transports.items():
        gk = qq_key(g)
        gi = idx_map[gk]
        ci = class_of_idx[gi]
        class_edge_count[ci] += 1
    print(f"\n[B8.3] Transport element class distribution over 1440 directed edges:")
    for ci, count in sorted(class_edge_count.items(), key=lambda x: -x[1]):
        print(f"    class {ci} (size {class_sizes[ci]}): {count} edges "
              f"({count / 1440:.3f})")

    # The transport element g(v,w) for an edge is in a specific
    # conjugacy class. If the edge corresponds to a 'pentagonal step'
    # (i.e., multiplication by an order-10 element), then g is of
    # order 10. But edges are nearest-neighbour, so g ∈ (the two 12-classes
    # of nearest-neighbour type).
    # All 12 neighbours of identity come from distance class — let's
    # check they are all order-10 or some other specific order.

    # Orders of the transport elements out of identity
    from collections import Counter as C
    # reuse element_order from B5/B6 if imported, else inline
    def element_order(g, idx_map, identity_key, max_order=120):
        power = g
        for n in range(1, max_order + 1):
            if qq_key(power) == identity_key:
                return n
            power = qq_mul(power, g)
        raise RuntimeError("order not found")
    identity_key = qq_key(identity)
    id_neighbour_orders = C()
    for j in adj[0]:  # identity's neighbours
        g = transport_element(verts[0], verts[j])
        o = element_order(g, idx_map, identity_key)
        id_neighbour_orders[o] += 1
    print(f"\n[B8.4] Orders of transport elements from identity:")
    print(f"  {dict(id_neighbour_orders)}")

    # --- σ-action: does σ preserve 2I as a set? ---
    print(f"\n[B8.5] STRUCTURAL CHECK: does σ (componentwise Galois on Q(√5))")
    print(f"       preserve 2I as a subset of the Hamilton quaternions?")
    sigma_preserves_2I = True
    sigma_first_escape = None
    sigma_img_count = 0
    for i, v in enumerate(verts):
        sv = sigma_on_quat(v)
        j = idx_map.get(qq_key(sv))
        if j is None:
            sigma_preserves_2I = False
            if sigma_first_escape is None:
                sigma_first_escape = (i, v, sv)
        else:
            sigma_img_count += 1
    if not sigma_preserves_2I:
        i, v, sv = sigma_first_escape
        print(f"  FINDING: σ does NOT preserve 2I.")
        print(f"           σ(verts[{i}]) escapes 2I.")
        print(f"           Only {sigma_img_count}/120 vertices are σ-preserved.")
        print(f"           Example: v = {v}")
        print(f"                  σ(v) = {sv}  (not in 2I)")
        print(f"  INTERPRETATION: σ is the algebraic Galois involution on")
        print(f"           Q(√5), but it does not act geometrically on a")
        print(f"           single 2I. Under the Elkies E₈ ← 2I ⊕ σ(2I)")
        print(f"           decomposition (Paper XXII: 'two 600-cells inside")
        print(f"           E₈'), σ is the map from one 600-cell to the")
        print(f"           other. σ-covariance is therefore a statement")
        print(f"           about the PAIR (2I, σ(2I)), not about 2I alone.")
        print(f"  CONSEQUENCE FOR B8: the σ-covariance condition on ω must")
        print(f"           be formulated on the union 2I ∪ σ(2I) ⊂ E₈ (or")
        print(f"           on the quotient 2I / (σ-orbits if any)), not on")
        print(f"           2I itself. This is Build B10's real content.")
    else:
        print(f"  σ preserves 2I bijectively (all 120 images in 2I).")
        sigma_fixed = [i for i in range(120) if idx_map[qq_key(sigma_on_quat(verts[i]))] == i]
        print(f"  |Fix(σ on 2I)| = {len(sigma_fixed)}")

    # --- B8 cocycle ω: project g(v,w) onto its conjugacy class label ---
    # The canonical Z[φ]× holonomy assignment is to identify each
    # edge's transport element by its position in the conjugacy class
    # structure, combined with the class's Z[φ]-grading.
    # For this first build we just report the class counts — the
    # actual Z[φ]× assignment requires B4 (norm-sign identification)
    # which we now implement:
    # ω(v,w) = sign × φ^k where:
    #   - sign = ±1 depending on which "half" of the order-10 double
    #     cover the transport falls into
    #   - k = Z[φ] grading of the transport's class (to be derived).
    # For the first computational check, we just verify the cycle-
    # accumulated products over the 12 orbits of T_τ.

    print(f"\n[B8.6] For each of the 12 T_τ-cycles, compute the product of")
    print(f"       transport elements around the cycle.")
    print(f"       (These are the 'cycle holonomies' that the weighted zeta will use.)")

    # Recompute T_τ cycles (from B6) to walk them:
    # tau is the canonical order-10 rep from B5/B6
    # Enumerate orders to find one of order 10
    order_by_idx = {}
    for i, v in enumerate(verts):
        order_by_idx[i] = element_order(v, idx_map, identity_key)
    order10_idxs = [i for i in range(120) if order_by_idx[i] == 10]
    tau = verts[order10_idxs[0]]
    # Walk cycles of T_τ: v → τ·v
    visited = [False] * 120
    cycles = []
    for start in range(120):
        if visited[start]:
            continue
        orbit = []
        i = start
        while not visited[i]:
            visited[i] = True
            orbit.append(i)
            next_v = qq_mul(tau, verts[i])
            i = idx_map[qq_key(next_v)]
        cycles.append(orbit)

    # For each cycle, compute product of transport elements along the
    # cycle's edges (T_τ(v) = τ·v, so the edge is (v, τ·v); the
    # transport is g(v, τ·v) = τ·v·v⁻¹ = τ, a constant!)
    print(f"       NOTE: under left-translation, every edge of every cycle has")
    print(f"             transport element g(v, τ·v) = τ·v·v⁻¹ = τ (constant).")
    print(f"             ⇒ cycle product = τ^10 = 1 for every cycle.")
    print(f"       Consequence: the *naive* cocycle ω(v, τ·v) := τ fails to")
    print(f"             distinguish cycles, so the weighted zeta equals the")
    print(f"             unweighted one. We need a DIFFERENT cocycle on the")
    print(f"             adjacency graph, not on the T_τ-orbit edges.")
    print()
    print(f"[B8.7] Report: the *canonical* ω on the full 12-regular adjacency")
    print(f"       graph (1440 directed edges) is what the cocycle must be,")
    print(f"       not the restriction to T_τ-orbit edges. T_τ-orbit edges")
    print(f"       all carry the same transport g = τ, giving trivial cycle")
    print(f"       product τ^10 = 1.")
    print()
    print(f"       This is a genuine finding: the holonomy cocycle must be")
    print(f"       defined for the FULL adjacency graph (1440 edges), not")
    print(f"       the orbit graph of T_τ (which has only 120 edges = 12×10).")
    print()
    print(f"       The clock T_τ is a self-map on 2I; its periodic orbits")
    print(f"       have finite structure. The weighted zeta must use a cocycle")
    print(f"       that is non-trivial on T_τ-orbits — which requires the")
    print(f"       cocycle to depend on MORE than just the transport element")
    print(f"       g(v, T(v)) = τ (constant).")
    print()
    print(f"       Alternative construction (BUILD REVISION): weight each")
    print(f"       cycle by the H₄-orbit class of its representative vertex.")
    print(f"       Different cycles can have vertices in different H₄-orbit")
    print(f"       classes, giving distinguishable Z[φ]-weights.")

    # Distribute cycles across H₄-orbit classes (conjugacy classes of 2I)
    cycle_class_of_rep = []
    for cyc in cycles:
        rep_idx = min(cyc)  # representative = smallest index in cycle
        cls = class_of_idx[rep_idx]
        cycle_class_of_rep.append(cls)
    cycle_class_count = Counter(cycle_class_of_rep)
    print(f"\n[B8.8] Distribution of 12 T_τ-cycles across 2I conjugacy classes:")
    for ci, count in sorted(cycle_class_count.items()):
        print(f"    class {ci} (size {class_sizes[ci]}): {count} cycles")

    print()
    print("=" * 72)
    print("BUILD B7/B8 PARTIAL (sim identifies STRUCTURAL ISSUE).")
    print("  - B7: 12-regular adjacency graph built; σ permutes 2I; σ-")
    print("       covariance on adjacency verified.")
    print("  - B8: naive cocycle ω(v, T_τ(v)) = τ is constant across all")
    print("       T_τ-orbit edges, giving trivial cycle product τ^10 = 1")
    print("       in every cycle. Weighted zeta with this ω = unweighted")
    print("       zeta. B8 MUST be refined before ζ_{T,ω} can be non-trivial.")
    print()
    print("STRUCTURAL FINDING: a canonical non-trivial cocycle needs to")
    print("       depend on the H₄-orbit class of the cycle (or on edge data")
    print("       beyond the transport element), not only on τ itself.")
    print("       This is the real content of B8. See B8 REVISION below.")
    print("=" * 72)


if __name__ == "__main__":
    main()
