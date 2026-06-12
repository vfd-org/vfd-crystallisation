"""Brandt engine at an arbitrary split prime level (GEOMETRY ONLY).

This module is part of the scanned geometry-construction path (see
no_fit_guard.py): it builds orbits and Brandt operators from the icosian
unit action on P^1(O_K/p) and knows NOTHING about elliptic curves, point
counts, or eigenvalue targets. Comparison against arithmetic targets
happens only in the orchestration scripts (level31_full_ideals.py,
second_form_level41.py, genus2_form_level61.py), which import this module
and the target side separately and let them meet at the comparison line.
"""
import os
import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ideal_classes as ic          # noqa: E402
import quaternion_order as qo       # noqa: E402
import brandt_matrices as bm        # noqa: E402


def galois_conj(g):
    """Galois conjugate of a + b*phi in coordinates (a, b): phi -> 1 - phi."""
    a, b = g
    return (a + b, -b)


def compute_orbits_p(p):
    """Orbit gate of A5 = 2I/{+-1} on P^1(O_K/p) at a split prime p
    (geometric; no arithmetic target anywhere)."""
    I = qo.ring()
    spl = ic.LocalSplitting(p)
    pts = spl.p1_points()
    index = {spl.normalize(pt): i for i, pt in enumerate(pts)}
    umats = [spl.iota(u) for u in I.units]
    parent = list(range(len(pts)))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for M in umats:
        for i, pt in enumerate(pts):
            union(i, index[spl.act(M, pt)])
    groups = {}
    for i in range(len(pts)):
        groups.setdefault(find(i), []).append(i)
    orbits = list(groups.values())
    return {"h": len(orbits), "orbits": orbits,
            "weights": [int(Fraction(60, len(o))) for o in orbits],
            "splitting": spl, "p1_points": pts, "p1_index": index,
            "orbit_sizes": sorted(len(o) for o in orbits)}


def engine_for(p):
    """A BrandtEngine bound to level p (split prime), built from the gate."""
    gate = compute_orbits_p(p)
    eng = bm.BrandtEngine.__new__(bm.BrandtEngine)
    eng.ring = qo.ring()
    eng.gate = gate
    eng.spl = gate["splitting"]
    eng.orbits = gate["orbits"]
    eng.h = gate["h"]
    eng.weights = gate["weights"]
    eng.mu = [len(o) for o in gate["orbits"]]
    eng.pts = gate["p1_points"]
    eng.index = gate["p1_index"]
    eng.orbit_of = [None] * len(eng.pts)
    for oi, o in enumerate(eng.orbits):
        for i in o:
            eng.orbit_of[i] = oi
    return eng


def cuspidal_dimension(p):
    """Cuspidal dimension at split prime level p: Brandt h minus the
    one-dimensional Eisenstein (all-ones) class."""
    return compute_orbits_p(p)["h"] - 1
