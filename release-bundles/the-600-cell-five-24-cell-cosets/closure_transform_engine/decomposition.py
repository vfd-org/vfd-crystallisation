"""Exact certificates for the Schläfli decomposition of the 600-cell.

This module establishes — exactly, with no floating-point arithmetic
entering any formal claim — that

    V_600 = C_0 ⊔ C_1 ⊔ C_2 ⊔ C_3 ⊔ C_4,

where V_600 = 2I, each C_i is a right coset of V_24 = 2T inside 2I,
|C_i| = 24, each C_i carries the 24-cell distance structure, and the
induced action of 2I on the five cosets descends through {±1} to a
faithful transitive action of A_5 on five points.

It is the finite-geometric foundation for the 24-600 spectral bridge
(see `closure_transform_engine.keystone`); this module is independent
of that artifact and uses only `vfd_v600` for exact Q(sqrt 5)
arithmetic.
"""
from __future__ import annotations

import math
import os
import sys
from collections import Counter
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Dict, List, Tuple

# Locate vfd_v600 (same robustness as keystone.py).
_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.abspath(os.path.join(_HERE, ".."))
try:
    import vfd_v600  # type: ignore  # noqa: F401
except ImportError:
    for _cand in (
        os.path.join(_REPO),
        os.path.join(_REPO, "papers", "v600-programme", "lib"),
    ):
        if os.path.isdir(os.path.join(_cand, "vfd_v600")):
            if _cand not in sys.path:
                sys.path.insert(0, _cand)
            break

from vfd_v600.group import build_state  # type: ignore
from vfd_v600.symmetry import mobile_orbit_under_v24  # type: ignore
from vfd_v600.sigma import sigma_fixed_set, is_sigma_fixed  # type: ignore
from vfd_v600.icosian import (  # type: ignore
    qq_distance_sq, qq_mul, qq_key, qq_norm_sq, qq_conjugate,
)


_ZERO_D2 = (Fraction(0), Fraction(0))


def _q5_to_float(p) -> float:
    return float(p[0]) + float(p[1]) * math.sqrt(5.0)


# ---------------------------------------------------------------------------
# Section 2 certificates — V_600 = 2I construction.
# ---------------------------------------------------------------------------

def certify_v600_construction(state) -> Dict:
    """Certify the exact V_600 = 2I construction:
      - exactly 120 distinct vertices;
      - every vertex has Q(sqrt 5) squared norm exactly 1;
      - closure under quaternion multiplication;
      - identity present;
      - every element has an inverse inside the set;
      - the set is precisely the binary icosahedral group 2I.
    """
    verts = state["verts"]
    idx_of = state["idx_of"]
    n = state["n"]

    if n != 120:
        return {"passed": False, "reason": f"V_600 has {n} vertices, expected 120"}

    # Distinctness — already enforced by build_state(); restate as a check.
    keys = {qq_key(v) for v in verts}
    if len(keys) != 120:
        return {"passed": False, "reason": f"only {len(keys)} distinct keys (need 120)"}

    # Unit norm: every v in V_600 satisfies |v|^2 = 1 exactly (over Q(sqrt 5)).
    unit_norm_ok = True
    for v in verts:
        nsq = qq_norm_sq(v)
        if nsq != (Fraction(1), Fraction(0)):
            unit_norm_ok = False
            break
    if not unit_norm_ok:
        return {"passed": False, "reason": "some vertex has |v|^2 != 1"}

    # Identity (1, 0, 0, 0).
    one = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )
    if qq_key(one) not in idx_of:
        return {"passed": False, "reason": "identity quaternion not in V_600"}

    # Closure: every product u*v is in V_600.
    closed = True
    for u in verts:
        for v in verts:
            prod = qq_mul(u, v)
            if qq_key(prod) not in idx_of:
                closed = False
                break
        if not closed:
            break
    if not closed:
        return {"passed": False, "reason": "V_600 not closed under multiplication"}

    # Inverses: since |v|^2 = 1, v^{-1} = conj(v).  Check conj(v) ∈ V_600.
    inverses_ok = True
    for v in verts:
        if qq_key(qq_conjugate(v)) not in idx_of:
            inverses_ok = False
            break
    if not inverses_ok:
        return {"passed": False, "reason": "some vertex has no inverse in V_600"}

    return {
        "passed": True,
        "n_vertices": 120,
        "distinct": True,
        "all_unit_norm": True,
        "closed_under_multiplication": True,
        "identity_present": True,
        "inverses_present": True,
        "method": "exact Q(sqrt 5) arithmetic via vfd_v600",
    }


# ---------------------------------------------------------------------------
# Section 3 certificates — V_24 = 2T as the sigma-fixed subset.
# ---------------------------------------------------------------------------

def certify_v24_subgroup(state) -> Dict:
    """Certify V_24 = {v in V_600 : sigma(v) = v} = 2T:
      - exactly 24 sigma-fixed vertices;
      - the subset is closed under quaternion multiplication;
      - identity is sigma-fixed;
      - every element has its inverse sigma-fixed;
      - hence V_24 is a subgroup of V_600 of order 24.
    """
    verts = state["verts"]
    idx_of = state["idx_of"]
    n = state["n"]

    sf = sigma_fixed_set(state)
    if len(sf) != 24:
        return {"passed": False, "reason": f"sigma-fixed set has {len(sf)} elements, expected 24"}

    sf_verts = [verts[i] for i in sf]

    # Subgroup closure: u*v sigma-fixed for u, v sigma-fixed.
    closed = True
    for u in sf_verts:
        for v in sf_verts:
            prod = qq_mul(u, v)
            if not is_sigma_fixed(prod):
                closed = False
                break
            if qq_key(prod) not in {qq_key(w) for w in sf_verts}:
                closed = False
                break
        if not closed:
            break
    if not closed:
        return {"passed": False, "reason": "V_24 not closed under multiplication"}

    # Identity sigma-fixed.
    one = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )
    if not is_sigma_fixed(one) or qq_key(one) not in {qq_key(verts[i]) for i in sf}:
        return {"passed": False, "reason": "identity not in V_24"}

    # Inverses: conj(v) is sigma-fixed iff v is.
    inverses_ok = all(is_sigma_fixed(qq_conjugate(v)) for v in sf_verts)
    if not inverses_ok:
        return {"passed": False, "reason": "some V_24 element has non-sigma-fixed inverse"}

    return {
        "passed": True,
        "n_fixed": 24,
        "closed_under_multiplication": True,
        "identity_present": True,
        "inverses_present": True,
        "index_in_v600": 120 // 24,
        "method": "exact sigma-twist and Q(sqrt 5) arithmetic",
    }


# ---------------------------------------------------------------------------
# Section 4 certificates — the five right cosets.
# ---------------------------------------------------------------------------

def right_cosets(state) -> List[Tuple[int, ...]]:
    """Return the five right cosets of V_24 in V_600 as sorted tuples of indices.

    Coset 0 is V_24 itself (the sigma-fixed orbit).  Cosets 1..4 are the four
    V_24-orbits on the 96 sigma-mobile vertices under left multiplication —
    which are exactly the non-identity right cosets V_24 * g, since for any
    v in V_600 the V_24-orbit { h * v : h in V_24 } = V_24 * v.
    """
    sf = sigma_fixed_set(state)
    mobile = mobile_orbit_under_v24(state)
    cosets = [tuple(sorted(sf))] + [tuple(sorted(o)) for o in mobile]
    assert len(cosets) == 5
    assert all(len(c) == 24 for c in cosets)
    flat: set = set()
    for c in cosets:
        flat.update(c)
    assert flat == set(range(state["n"]))
    return cosets


def certify_right_cosets(state, cosets) -> Dict:
    """Certify the five-coset partition of V_600:
      - exactly 5 right cosets;
      - each has 24 vertices;
      - pairwise disjoint;
      - union equals V_600;
      - C_0 = V_24;
      - C_1..C_4 cover the 96 sigma-mobile vertices.
    """
    if len(cosets) != 5:
        return {"passed": False, "reason": f"have {len(cosets)} cosets, expected 5"}
    sizes = [len(c) for c in cosets]
    if sizes != [24, 24, 24, 24, 24]:
        return {"passed": False, "reason": f"coset sizes {sizes}, expected [24]*5"}

    # Disjointness.
    seen: set = set()
    for ci, c in enumerate(cosets):
        s = set(c)
        if s & seen:
            return {"passed": False, "reason": f"coset {ci} not disjoint from earlier ones"}
        seen |= s
    if seen != set(range(state["n"])):
        return {"passed": False, "reason": "cosets do not cover V_600"}

    # Coset 0 = V_24.
    sf = sigma_fixed_set(state)
    if set(cosets[0]) != sf:
        return {"passed": False, "reason": "C_0 != V_24 (sigma-fixed sublattice)"}

    # Cosets 1..4 cover sigma-mobile.
    mobile = set(range(state["n"])) - sf
    union_mobile_cosets: set = set()
    for c in cosets[1:]:
        union_mobile_cosets |= set(c)
    if union_mobile_cosets != mobile:
        return {"passed": False, "reason": "C_1..C_4 do not cover sigma-mobile"}

    # Membership uniqueness.
    membership = {v: None for v in range(state["n"])}
    for ci, c in enumerate(cosets):
        for v in c:
            if membership[v] is not None:
                return {"passed": False,
                        "reason": f"vertex {v} in cosets {membership[v]} and {ci}"}
            membership[v] = ci
    if any(m is None for m in membership.values()):
        return {"passed": False, "reason": "some vertex not assigned to any coset"}

    return {
        "passed": True,
        "n_cosets": 5,
        "sizes": sizes,
        "disjoint": True,
        "cover_v600": True,
        "c0_equals_v24": True,
        "c1_to_c4_cover_sigma_mobile": True,
    }


# ---------------------------------------------------------------------------
# Section 5 certificates — each coset carries the 24-cell distance structure.
# ---------------------------------------------------------------------------

def distance_shells_v600(state) -> List[Tuple[Tuple[Fraction, Fraction], int]]:
    """Return the distinct non-zero distance^2 values in V_600 + their pair counts.

    Each element is (d^2, count) sorted by float-projected value of d^2.
    """
    verts = state["verts"]
    n = state["n"]
    counts: Dict[Tuple[Fraction, Fraction], int] = {}
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            d = qq_distance_sq(verts[i], verts[j])
            if d == _ZERO_D2:
                continue
            counts[d] = counts.get(d, 0) + 1
    items = sorted(counts.items(), key=lambda kv: _q5_to_float(kv[0]))
    return items


def certify_each_coset_is_24cell(state, cosets) -> Dict:
    """Certify, for each coset C_i:
      - the shortest non-zero internal squared distance is exactly 1;
      - the d^2=1 graph is 8-regular with 96 edges and 24 vertices;
      - no intra-coset pair has the V_600 shortest distance (3-sqrt 5)/2.
    """
    verts = state["verts"]
    n = state["n"]

    # V_600 shortest non-zero distance^2.
    shells = distance_shells_v600(state)
    if not shells:
        return {"passed": False, "reason": "no non-zero distances"}
    d2_v600 = shells[0][0]

    per_coset = []
    all_good = True
    for ci, c in enumerate(cosets):
        # Pairwise distances within this coset.
        intra_d2: Dict[Tuple[Fraction, Fraction], int] = {}
        for ii in c:
            for jj in c:
                if ii == jj:
                    continue
                d = qq_distance_sq(verts[ii], verts[jj])
                if d == _ZERO_D2:
                    continue
                intra_d2[d] = intra_d2.get(d, 0) + 1
        intra_sorted = sorted(intra_d2.items(), key=lambda kv: _q5_to_float(kv[0]))
        if not intra_sorted:
            per_coset.append({"coset": ci, "passed": False, "reason": "no distances"})
            all_good = False
            continue
        d2_min = intra_sorted[0][0]
        if d2_min != (Fraction(1), Fraction(0)):
            per_coset.append({"coset": ci, "passed": False,
                              "reason": f"shortest d^2 = {d2_min}, expected 1"})
            all_good = False
            continue
        edge_count = intra_d2[d2_min]  # ordered pair count; divide by 2 for edges
        if edge_count != 2 * 96:
            per_coset.append({"coset": ci, "passed": False,
                              "reason": f"edge count {edge_count//2}, expected 96"})
            all_good = False
            continue
        # 8-regular: every vertex in c has 8 d^2=1 neighbours in c.
        per_vertex_deg = Counter()
        for ii in c:
            for jj in c:
                if ii == jj:
                    continue
                if qq_distance_sq(verts[ii], verts[jj]) == d2_min:
                    per_vertex_deg[ii] += 1
        degs = set(per_vertex_deg.values())
        if degs != {8}:
            per_coset.append({"coset": ci, "passed": False,
                              "reason": f"non-8-regular: degree set {sorted(degs)}"})
            all_good = False
            continue
        # No V_600-edge between coset members.
        v600_edges_inside = sum(
            1 for ii in c for jj in c
            if ii != jj and qq_distance_sq(verts[ii], verts[jj]) == d2_v600
        )
        if v600_edges_inside != 0:
            per_coset.append({"coset": ci, "passed": False,
                              "reason": f"{v600_edges_inside} intra-coset V_600 edges"})
            all_good = False
            continue
        per_coset.append({
            "coset": ci,
            "passed": True,
            "min_d2": "(1, 0)",
            "regular_degree": 8,
            "edges": 96,
            "v600_edges_inside": 0,
        })

    return {
        "passed": all_good,
        "v600_d2_shell1": (int(d2_v600[0].numerator), int(d2_v600[0].denominator),
                            int(d2_v600[1].numerator), int(d2_v600[1].denominator)),
        "intra_coset_d2_shell1": "(1, 0)  (i.e. squared distance = 1)",
        "per_coset": per_coset,
    }


# ---------------------------------------------------------------------------
# Section 6 certificates — induced 2I action on the five cosets.
# ---------------------------------------------------------------------------

def right_mult_perm(state, h_idx: int) -> List[int]:
    """Vertex permutation on V_600 induced by right multiplication by verts[h_idx]."""
    verts = state["verts"]
    idx_of = state["idx_of"]
    n = state["n"]
    h = verts[h_idx]
    return [idx_of[qq_key(qq_mul(verts[i], h))] for i in range(n)]


def coset_permutation(coset_of: Dict[int, int], vperm: List[int]) -> Tuple[int, ...]:
    """Read off the induced permutation of the five cosets (well-defined because
    right multiplication maps each coset to one coset)."""
    sample = {}
    for v, ci in coset_of.items():
        if ci not in sample:
            sample[ci] = v
    return tuple(coset_of[vperm[sample[ci]]] for ci in range(5))


def cycle_structure(perm: Tuple[int, ...]) -> Tuple[int, ...]:
    seen = [False] * len(perm)
    cyc: List[int] = []
    for i in range(len(perm)):
        if seen[i]:
            continue
        c = 0
        j = i
        while not seen[j]:
            seen[j] = True
            j = perm[j]
            c += 1
        cyc.append(c)
    return tuple(sorted(cyc))


def is_even_permutation(perm: Tuple[int, ...]) -> bool:
    n = len(perm)
    visited = [False] * n
    sign = 1
    for i in range(n):
        if visited[i]:
            continue
        j = i
        cycle_len = 0
        while not visited[j]:
            visited[j] = True
            j = perm[j]
            cycle_len += 1
        if cycle_len % 2 == 0:
            sign = -sign
    return sign == 1


def certify_a5_coset_action(state, cosets) -> Dict:
    """Certify the induced action of 2I on the 5 cosets:
      - 60 distinct permutations;
      - transitive (orbit of C_0 = all 5 cosets);
      - kernel exactly {+1, -1};
      - every image element is even (image ⊂ A_5);
      - image equals A_5 (size 60, transitive, all even, subgroup of S_5).
    """
    n = state["n"]
    verts = state["verts"]
    coset_of: Dict[int, int] = {v: ci for ci, c in enumerate(cosets) for v in c}

    perms: List[Tuple[int, ...]] = []
    kernel_indices: List[int] = []
    for h_idx in range(n):
        vperm = right_mult_perm(state, h_idx)
        cperm = coset_permutation(coset_of, vperm)
        perms.append(cperm)
        if cperm == (0, 1, 2, 3, 4):
            kernel_indices.append(h_idx)

    distinct = set(perms)
    if len(distinct) != 60:
        return {"passed": False, "reason": f"image has {len(distinct)} permutations, expected 60"}

    # All even.
    odd_perms = [p for p in distinct if not is_even_permutation(p)]
    if odd_perms:
        return {"passed": False, "reason": f"{len(odd_perms)} odd permutations in image"}

    # Transitive: orbit of 0 covers {0,..,4}.
    orbit = {0}
    changed = True
    while changed:
        changed = False
        for p in distinct:
            for x in list(orbit):
                if p[x] not in orbit:
                    orbit.add(p[x])
                    changed = True
    if orbit != {0, 1, 2, 3, 4}:
        return {"passed": False, "reason": f"action not transitive (orbit {sorted(orbit)})"}

    # Kernel = {±1}.
    if len(kernel_indices) != 2:
        return {"passed": False,
                "reason": f"kernel has {len(kernel_indices)} elements, expected 2"}
    kernel_verts = [verts[i] for i in kernel_indices]
    plus_one = (
        (Fraction(1), Fraction(0)), (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0)), (Fraction(0), Fraction(0)),
    )
    minus_one = (
        (Fraction(-1), Fraction(0)), (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0)), (Fraction(0), Fraction(0)),
    )
    kernel_keys = {qq_key(v) for v in kernel_verts}
    if kernel_keys != {qq_key(plus_one), qq_key(minus_one)}:
        return {"passed": False, "reason": "kernel is not {+1, -1}"}

    # Conjugacy class sizes by cycle structure (and orbit for 5-cycles).
    base_by_struct = {
        (1, 1, 1, 1, 1): "1A", (1, 2, 2): "2A", (1, 1, 3): "3A", (5,): "5*",
    }
    # Split 5-cycles into 5A / 5B by A_5 conjugacy orbit.
    def perm_compose(p, q):
        return tuple(p[q[i]] for i in range(5))

    def perm_inverse(p):
        inv = [0] * 5
        for i, x in enumerate(p):
            inv[x] = i
        return tuple(inv)

    cls_buckets: Dict[str, set] = {"1A": set(), "2A": set(), "3A": set(),
                                    "5A": set(), "5B": set()}
    five_cyc = [p for p in distinct if cycle_structure(p) == (5,)]
    if five_cyc:
        seed = five_cyc[0]
        orb = set()
        for g in distinct:
            gi = perm_inverse(g)
            orb.add(perm_compose(perm_compose(g, seed), gi))
        for p in distinct:
            struct = cycle_structure(p)
            base = base_by_struct[struct]
            if base == "5*":
                cls = "5A" if p in orb else "5B"
            else:
                cls = base
            cls_buckets[cls].add(p)
    else:
        for p in distinct:
            cls_buckets[base_by_struct[cycle_structure(p)]].add(p)

    class_sizes = {cls: len(b) for cls, b in cls_buckets.items()}
    expected = {"1A": 1, "2A": 15, "3A": 20, "5A": 12, "5B": 12}
    if class_sizes != expected:
        return {"passed": False,
                "reason": f"class sizes {class_sizes} != expected {expected}"}

    return {
        "passed": True,
        "n_distinct_permutations": 60,
        "transitive": True,
        "kernel_size": 2,
        "kernel_is_plus_minus_one": True,
        "all_even": True,
        "class_sizes": class_sizes,
        "image_is_A5": True,
    }


# ---------------------------------------------------------------------------
# Top-level orchestrator.
# ---------------------------------------------------------------------------

@dataclass
class DecompositionResult:
    n_vertices: int
    coset_sizes: List[int]
    v600_construction: Dict
    v24_subgroup: Dict
    right_cosets_certificate: Dict
    each_coset_is_24cell: Dict
    a5_action: Dict
    distance_shells: List[Dict] = field(default_factory=list)
    cosets: List[List[int]] = field(default_factory=list)
    coset_action_table: List[Dict] = field(default_factory=list)

    @property
    def verdict(self) -> str:
        ok = (
            self.v600_construction.get("passed")
            and self.v24_subgroup.get("passed")
            and self.right_cosets_certificate.get("passed")
            and self.each_coset_is_24cell.get("passed")
            and self.a5_action.get("passed")
        )
        return "SCHLAEFLI_DECOMPOSITION_CERTIFIED" if ok else "FAIL"

    def to_dict(self) -> Dict:
        return {
            "n_vertices": self.n_vertices,
            "coset_sizes": list(self.coset_sizes),
            "v600_construction": dict(self.v600_construction),
            "v24_subgroup": dict(self.v24_subgroup),
            "right_cosets_certificate": dict(self.right_cosets_certificate),
            "each_coset_is_24cell": dict(self.each_coset_is_24cell),
            "a5_action": dict(self.a5_action),
            "verdict": self.verdict,
        }


def run_decomposition() -> DecompositionResult:
    """Run every certificate and return a structured result."""
    state = build_state()
    cosets = right_cosets(state)

    v600 = certify_v600_construction(state)
    v24 = certify_v24_subgroup(state)
    rc = certify_right_cosets(state, cosets)
    cc = certify_each_coset_is_24cell(state, cosets)
    a5 = certify_a5_coset_action(state, cosets)

    # Distance shells of V_600 (for the docs/outputs CSV).
    shells = distance_shells_v600(state)
    shells_for_dict = [
        {
            "shell": i + 1,
            "d2_rational": f"{d[0]} + {d[1]}*sqrt(5)",
            "d2_float": _q5_to_float(d),
            "pair_count_directed": count,
            "edges_undirected": count // 2,
        }
        for i, (d, count) in enumerate(shells)
    ]

    # Coset action table (one row per element of 2I).
    coset_of = {v: ci for ci, c in enumerate(cosets) for v in c}
    action_rows = []
    for h_idx in range(state["n"]):
        vperm = right_mult_perm(state, h_idx)
        cperm = coset_permutation(coset_of, vperm)
        action_rows.append({
            "h_index": h_idx,
            "coset_permutation": list(cperm),
            "cycle_structure": list(cycle_structure(cperm)),
            "is_identity": cperm == (0, 1, 2, 3, 4),
            "is_even": is_even_permutation(cperm),
        })

    return DecompositionResult(
        n_vertices=state["n"],
        coset_sizes=[len(c) for c in cosets],
        v600_construction=v600,
        v24_subgroup=v24,
        right_cosets_certificate=rc,
        each_coset_is_24cell=cc,
        a5_action=a5,
        distance_shells=shells_for_dict,
        cosets=[list(c) for c in cosets],
        coset_action_table=action_rows,
    )
