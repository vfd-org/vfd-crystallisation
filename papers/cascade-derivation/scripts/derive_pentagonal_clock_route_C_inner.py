#!/usr/bin/env python3
"""
Route C-inner (Build B13): conjugation clock on 2I with varying
orbit lengths.

Motivation (B11/B12 analytic finding, 2026-04-24):
Left-translation T_τ gives all orbits length 10 (single orbit
length), hence ẑ(z) is a rational function in z¹⁰ — a local factor
at one prime, not a full Dirichlet-series zeta. To get a zeta
with a proper critical line, we need orbits of multiple lengths.

Conjugation clock:
  T_g: 2I → 2I, T_g(v) = g·v·g⁻¹

This action has:
  - Fix(T_g) = C_2I(g) (centralizer of g in 2I).
  - Orbit sizes = |2I| / |stabilizer of v under T_g|
                = conjugacy-class sizes of elements in 2I.

For g = τ (order 10):
  - Fix(T_τ^n) = C(τ^n) for each n = 1, ..., 10.
  - Orbit of v under T_τ = {g^k v g^{-k} : k ∈ Z}.

Since 2I has 9 conjugacy classes with sizes {1, 1, 20, 30, 24, 20, 24}
(wait, that's sizes of CONJUGACY CLASSES, not orbit-of-conjugation-by-τ
sizes. Let me clarify.)

Actually, T_τ(v) = τ v τ^{-1} is the permutation induced by τ acting
on 2I via conjugation (inner automorphism). Fixed points of T_τ^n
are elements v with τ^n v τ^{-n} = v, i.e., v ∈ C_2I(τ^n).

Orbit of v under T_τ is the τ-conjugation orbit: {τ^k v τ^{-k} : k ∈ Z}.
The orbit length divides ord(τ) = 10. Specifically, orbit length
= 10 / |{k mod 10 : τ^k v τ^{-k} = v}| = 10 / [C_2I(τ) : C_2I(τ, v)]
... this gets complex. Just compute.

Deliverables:
  - Enumerate conjugation orbits of T_τ on 2I.
  - Compute orbit-length multiset.
  - Compute Fix(T_τ^n) for n = 1..10.
  - Form unweighted Artin-Mazur zeta ζ_{T_τ,conj}(z).
  - Apply κ-cocycle weighting per orbit.
  - Form σ-symmetric ẑ_{conj}(z).
  - Check whether ẑ_{conj}(z) has multiple orbit lengths (⇒ non-trivial
    Dirichlet-series structure) or single length (⇒ same local-factor
    limitation as left-translation case).

Exact Q(√5) arithmetic. No floats.

Run: python3 papers/cascade-derivation/scripts/derive_pentagonal_clock_route_C_inner.py
"""

from __future__ import annotations

import sys
from pathlib import Path
from fractions import Fraction
from collections import defaultdict, Counter
from math import comb

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
sys.path.insert(0, str(REPO_ROOT / "papers" / "paper-xxii" / "scripts"))

from run_icosian_exact import (  # noqa: E402
    q_zero, q_one, q_neg, q_add, q_sub, q_mul, q_scale,
    qq_mul, qq_conjugate, qq_norm_sq, qq_eq, qq_key,
    build_vertices, vertex_index_map, vertex_index_exact,
    qq_distance_sq,
)


def element_order(g, idx_map, identity_key, max_order=120):
    power = g
    for n in range(1, max_order + 1):
        if qq_key(power) == identity_key:
            return n
        power = qq_mul(power, g)
    raise RuntimeError("order not found")


def conjugation_orbit(g, v, idx_map):
    """Orbit of v under T_g: {g^k v g^{-k}}. Returns list of indices."""
    orbit = []
    current = v
    for _ in range(120):  # bounded
        idx = idx_map[qq_key(current)]
        if orbit and idx == orbit[0]:
            return orbit
        orbit.append(idx)
        # Next: g · current · g^{-1}
        g_inv = qq_conjugate(g)
        current = qq_mul(qq_mul(g, current), g_inv)
    return orbit


def centralizer_size(g, verts, idx_map):
    """Number of v ∈ 2I with g v = v g."""
    count = 0
    for v in verts:
        if qq_eq(qq_mul(g, v), qq_mul(v, g)):
            count += 1
    return count


def main():
    print("=" * 76)
    print("Route C-inner (B13): conjugation clock T_τ(v) = τ v τ⁻¹.")
    print("=" * 76)

    verts = build_vertices()
    identity = (q_one(), q_zero(), q_zero(), q_zero())
    id_idx = vertex_index_exact(identity, verts)
    verts[0], verts[id_idx] = verts[id_idx], verts[0]
    idx_map = vertex_index_map(verts)
    identity_key = qq_key(identity)

    # Find τ of order 10
    for i, v in enumerate(verts):
        if i == 0:
            continue
        if element_order(v, idx_map, identity_key) == 10:
            tau = v
            tau_idx = i
            break
    print(f"\n[C.1] τ at index {tau_idx}, order 10.")

    # --- Conjugation orbits of T_τ on 2I ----------------------
    print(f"\n[C.2] Conjugation-orbit decomposition of T_τ on 2I:")
    visited = [False] * 120
    orbits = []
    for start in range(120):
        if visited[start]:
            continue
        orbit = conjugation_orbit(tau, verts[start], idx_map)
        for idx in orbit:
            visited[idx] = True
        orbits.append(orbit)

    orbit_lens = Counter(len(o) for o in orbits)
    print(f"  orbit-length multiset: {dict(orbit_lens)}")
    print(f"  total orbits: {len(orbits)}")
    total = sum(len(o) for o in orbits)
    if total != 120:
        print(f"  FAIL: orbit total {total} != 120")
        sys.exit(1)
    print(f"  OK: orbits partition 2I (total 120).")

    # --- Fix(T_τ^n) --------------------------------------------
    print(f"\n[C.3] Fix(T_τ^n) = centralizer of τ^n for n=1..10:")
    tau_pow = identity
    for n in range(1, 11):
        tau_pow = qq_mul(tau_pow, tau)
        c_size = centralizer_size(tau_pow, verts, idx_map)
        order_n = element_order(tau_pow, idx_map, identity_key)
        print(f"  n={n:2d}: τ^n has order {order_n:2d}; |C(τ^n)| = {c_size}")

    # --- Unweighted Artin-Mazur zeta ---------------------------
    # ζ_{T_τ,conj}(z) = ∏_{orbit O} (1 - z^{|O|})^{-1}
    print(f"\n[C.4] Unweighted Artin-Mazur zeta:")
    print(f"  ζ_{{T_τ,conj}}(z) = ", end="")
    parts = []
    for length in sorted(orbit_lens.keys()):
        m = orbit_lens[length]
        parts.append(f"(1 - z^{length})^{{-{m}}}")
    print(" · ".join(parts))
    if len(orbit_lens) > 1:
        print(f"\n  FINDING: MULTIPLE orbit lengths present: {sorted(orbit_lens.keys())}")
        print(f"           ζ is a GENUINE multi-prime rational function, not a")
        print(f"           single-local-factor. Candidate for richer zeta analysis.")
    else:
        single = list(orbit_lens.keys())[0]
        print(f"\n  FINDING: only orbit length {single} appears. ζ is again a")
        print(f"           single-local-factor rational function in z^{single}.")

    # Report orbits in detail for small orbit lengths (potential fixed points)
    print(f"\n[C.5] Orbit structure detail:")
    for length in sorted(orbit_lens.keys()):
        m = orbit_lens[length]
        print(f"  length {length}: {m} orbits")
        if length <= 2:
            for orb in orbits:
                if len(orb) == length:
                    # Show the representative vertex
                    v = verts[orb[0]]
                    print(f"    representative vertex index {orb[0]}: {v}")


if __name__ == "__main__":
    main()
