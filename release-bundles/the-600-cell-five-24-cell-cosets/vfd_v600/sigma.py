"""σ-Galois twist (√5 ↦ -√5) on icosian quaternions and the 24-cell.

The 24-cell V_24 ⊂ V_600 is exactly the σ-fixed sublattice: a vertex
v ∈ V_600 lies in V_24 iff every component has zero √5 part. For such
vertices σ(v) = v, hence |v - σ(v)|² = 0.

This module provides:
    sigma_quat(v)        — apply σ to a quaternion.
    is_sigma_fixed(v)    — test membership in V_24.
    sigma_fixed_set(state) — return the 24 σ-fixed vertex indices.
    sigma_pair_energy(v) — |v - σ(v)|²_Euclidean exactly in Q(√5).
"""

from __future__ import annotations

from fractions import Fraction

from .icosian import q_sub, qq_norm_sq


def sigma_quat(v):
    """σ-Galois twist applied to a quaternion (component-wise √5 ↦ -√5)."""
    return tuple((c[0], -c[1]) for c in v)


def is_sigma_fixed(v):
    """True iff v has zero √5 part in every component (i.e. v ∈ V_24)."""
    return all(c[1] == 0 for c in v)


def sigma_fixed_set(state):
    """Return the set of vertex indices in V_24 (= σ-fixed sublattice)."""
    verts = state["verts"]
    return {i for i in range(state["n"]) if is_sigma_fixed(verts[i])}


def sigma_pair_energy(v):
    """E(v) := |v - σ(v)|²_Euclidean.

    Convention: squared icosian-Euclidean distance between v and σ(v).
    For σ-fixed vertices, returns Fraction(0).
    For σ-mobile vertices on V_600, returns Fraction(5, 2)
    (W(H_4)-invariant single value across all 96 σ-mobile vertices).

    Note: prior drafts that wrote `E := |v-σ(v)|² / 2` had an extra
    factor-of-1/2; the canonical convention here uses no such division
    so that the "single quantum gap" value matches programme documents.
    """
    sv = sigma_quat(v)
    diff = tuple(q_sub(v[i], sv[i]) for i in range(4))
    nsq = qq_norm_sq(diff)
    # |v-σ(v)|² is rational (the √5 part vanishes by σ-equivariance).
    assert nsq[1] == 0
    return Fraction(nsq[0])
