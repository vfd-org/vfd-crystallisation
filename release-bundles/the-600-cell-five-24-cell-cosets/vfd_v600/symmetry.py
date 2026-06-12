"""Concrete subgroup Γ ≤ W(H_4) acting transitively on σ-mobile V_600.

For Paper 2's Hawking-quantum theorem we need a *symmetry-grade* proof
that |v − σ(v)|² is constant across all 96 σ-mobile vertices, not just
a brute-force computation. A clean route: exhibit a concrete group Γ
that

  (i)  acts on V_600 as a permutation group of isometries;
  (ii) commutes with σ;
  (iii) acts transitively on V_600 \\ V_24 (96 vertices).

The V_24 = 2T binary-tetrahedral subgroup of 2I = V_600 supplies this
through the **bilateral** (two-sided) action:

    Γ = { v ↦ g · v · h  :  g, h ∈ V_24 }.

Each generator is an isometry of ℍ_K (left- and right-multiplication by
unit quaternions are isometries) and commutes with σ because every
element of V_24 has σ(g) = g (V_24 is the σ-fixed sublattice). Therefore
σ(g v h) = σ(g)σ(v)σ(h) = g σ(v) h, so Γ commutes with σ on V_600.

The orbits of Γ on V_600 are the V_24-double cosets V_24 v V_24. The
trivial orbit V_24 · 1 · V_24 = V_24 is precisely the σ-fixed set; the
non-trivial part is one single orbit of size 96 — the σ-mobile sector.
This is the orbit-grade fact that forces the Hawking quantum E_q to be
constant.

This module exposes:

  v24_left_action(state)             — left-mult permutations from V_24.
  sigma_commutes_with_left_mul(...)  — σ(gv) = gσ(v) for g ∈ V_24.
  bilateral_v24_orbits(state)        — Γ-orbits on V_600.
  is_bilateral_v24_transitive_on_mobile(state) — the certificate.

Plus a legacy single-side helper (mobile_orbit_under_v24) retained to
report the four V_24 right-cosets that make up σ-mobile under the
weaker one-sided action.
"""

from __future__ import annotations

from .icosian import qq_mul, qq_key
from .sigma import sigma_quat, sigma_fixed_set


def left_mul_perm(state, g_idx):
    """Return the permutation of V_600 induced by left-multiplication by verts[g_idx].

    P[i] = idx_of(verts[g_idx] * verts[i]).  P preserves V_600 because 2I
    is closed under multiplication.
    """
    verts = state["verts"]
    idx_of = state["idx_of"]
    n = state["n"]
    g = verts[g_idx]
    return [idx_of[qq_key(qq_mul(g, verts[i]))] for i in range(n)]


def v24_left_action(state):
    """Return list of |V_24| permutations of V_600, one per V_24 element.

    These form a subgroup of S_120 of order 24, isomorphic to V_24 ≅ 2T.
    """
    sf = sorted(sigma_fixed_set(state))
    return [left_mul_perm(state, g_idx) for g_idx in sf]


def sigma_commutes_with_right_mul(state, h_idx):
    """Verify σ(v · h) = σ(v) · σ(h) for ALL v ∈ V_600.

    Returns True iff equality holds. For h ∈ V_24, σ(h) = h, so
    σ(v·h) = σ(v)·h — i.e., right-multiplication by h commutes with σ.
    """
    verts = state["verts"]
    n = state["n"]
    h = verts[h_idx]
    sh = sigma_quat(h)
    for i in range(n):
        lhs = sigma_quat(qq_mul(verts[i], h))
        rhs = qq_mul(sigma_quat(verts[i]), sh)
        if qq_key(lhs) != qq_key(rhs):
            return False
    return True


def sigma_commutes_with_bilateral(state, g_idx, h_idx):
    """Verify σ(g · v · h) = g · σ(v) · h for ALL v ∈ V_600 when g, h ∈ V_24.

    Combines left- and right-multiplication commutation; required for the
    bilateral V_24 action used in Paper 2's symmetry certificate.
    """
    verts = state["verts"]
    n = state["n"]
    g, h = verts[g_idx], verts[h_idx]
    for i in range(n):
        lhs = sigma_quat(qq_mul(qq_mul(g, verts[i]), h))
        rhs = qq_mul(qq_mul(g, sigma_quat(verts[i])), h)
        if qq_key(lhs) != qq_key(rhs):
            return False
    return True


def sigma_commutes_with_left_mul(state, g_idx):
    """Verify σ(g · v) = σ(g) · σ(v) for ALL v ∈ V_600.

    Returns True iff equality holds. For g ∈ V_24, σ(g) = g, so
    σ(g·v) = g·σ(v) — i.e., left-multiplication by g commutes with σ.
    """
    verts = state["verts"]
    n = state["n"]
    g = verts[g_idx]
    sg = sigma_quat(g)
    for i in range(n):
        lhs = sigma_quat(qq_mul(g, verts[i]))
        rhs = qq_mul(sg, sigma_quat(verts[i]))
        if qq_key(lhs) != qq_key(rhs):
            return False
    return True


def mobile_orbit_under_v24(state):
    """Return list of orbits of V_600 \\ V_24 under left-multiplication by V_24.

    Each orbit is a set of vertex indices.
    """
    sf = sigma_fixed_set(state)
    n = state["n"]
    mobile = set(range(n)) - sf
    perms = v24_left_action(state)
    visited = set()
    orbits = []
    for v in sorted(mobile):
        if v in visited:
            continue
        orbit = set()
        for P in perms:
            orbit.add(P[v])
        orbits.append(orbit)
        visited |= orbit
    return orbits


def is_v24_left_mul_transitive_on_mobile(state):
    """Single-side: V_24 left-mul on σ-mobile partitions into 4 orbits of 24.

    Returns (transitive: bool, orbit_sizes: list[int]).  Note the
    one-sided action is NOT transitive — see bilateral version below.
    """
    orbits = mobile_orbit_under_v24(state)
    sizes = sorted(len(o) for o in orbits)
    return (len(orbits) == 1 and sizes == [96], sizes)


def bilateral_v24_orbits(state):
    """Return list of orbits of V_600 under bilateral V_24 action g·v·h.

    The orbit of v is {g v h : g, h ∈ V_24}.  These are the V_24-double
    cosets V_24 v V_24 in V_600.
    """
    verts = state["verts"]
    idx_of = state["idx_of"]
    n = state["n"]
    sf = sorted(sigma_fixed_set(state))

    visited = set()
    orbits = []
    for v in range(n):
        if v in visited:
            continue
        orbit = set()
        for g_idx in sf:
            for h_idx in sf:
                prod = qq_mul(qq_mul(verts[g_idx], verts[v]), verts[h_idx])
                orbit.add(idx_of[qq_key(prod)])
        orbits.append(orbit)
        visited |= orbit
    return orbits


def is_bilateral_v24_transitive_on_mobile(state):
    """Main certificate: bilateral V_24 action is transitive on σ-mobile.

    Returns (transitive: bool, orbit_sizes: list[int]).  Expected:
    (True, [24, 96]) — the σ-fixed orbit (V_24 itself, size 24) plus a
    single σ-mobile orbit of size 96.
    """
    orbits = bilateral_v24_orbits(state)
    sizes = sorted(len(o) for o in orbits)
    sf = sigma_fixed_set(state)
    mobile_orbits = [o for o in orbits if not (o & sf)]
    transitive = len(mobile_orbits) == 1 and len(mobile_orbits[0]) == 96
    return (transitive, sizes)
