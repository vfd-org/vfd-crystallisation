#!/usr/bin/env python3
"""
Route C-inner weighted (B13 + B9 + B10):
  T_τ(v) = τ v τ⁻¹ conjugation clock on 2I
  orbits of lengths {1: 10, 5: 22}
  cocycle ω(v) = φ^{κ(v)} where κ(v) = (shell(v) - 4)²
  K(orbit) = Σ κ(v_i) for v_i ∈ orbit
  weighted zeta ζ_C(z) = ∏_orbit (1 - φ^{K} z^{|orbit|})⁻¹
  σ-symmetric ẑ_C(z) = ζ_C(z) · σ(ζ_C(z))

Exact Q(√5) arithmetic.
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


# --- exact Q(√5) helpers --------------------------------------------
def qsq5_less(x, y):
    c = y[0] - x[0]
    d = y[1] - x[1]
    if d == 0:
        return c > 0
    if d > 0:
        if c >= 0:
            return True
        return 5 * d * d > c * c
    if c <= 0:
        return False
    return c * c > 5 * d * d


def sigma_pair(x):
    return (x[0], -x[1])


def zphi_pair_mul(x, y):
    return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def zphi_pair_add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def zphi_pair_zero():
    return (Fraction(0), Fraction(0))


def zphi_pair_one():
    return (Fraction(1), Fraction(0))


def phi_pair():
    return (Fraction(1, 2), Fraction(1, 2))


def phi_power(n):
    p = zphi_pair_one()
    if n >= 0:
        phi = phi_pair()
        for _ in range(n):
            p = zphi_pair_mul(p, phi)
    else:
        inv_phi = (Fraction(-1, 2), Fraction(1, 2))
        for _ in range(-n):
            p = zphi_pair_mul(p, inv_phi)
    return p


def poly_mul(p1, p2, max_deg):
    result = [zphi_pair_zero()] * (max_deg + 1)
    for i, ci in enumerate(p1):
        if i > max_deg:
            break
        if ci == zphi_pair_zero():
            continue
        for j, cj in enumerate(p2):
            if i + j > max_deg:
                break
            result[i + j] = zphi_pair_add(result[i + j], zphi_pair_mul(ci, cj))
    return result


def geometric_series_inverse(a, length, max_deg):
    poly = [zphi_pair_zero()] * (max_deg + 1)
    ak = zphi_pair_one()
    k = 0
    while k * length <= max_deg:
        poly[k * length] = zphi_pair_add(poly[k * length], ak)
        ak = zphi_pair_mul(ak, a)
        k += 1
    return poly


def element_order(g, idx_map, identity_key, max_order=120):
    power = g
    for n in range(1, max_order + 1):
        if qq_key(power) == identity_key:
            return n
        power = qq_mul(power, g)
    raise RuntimeError("order not found")


def conjugation_orbit(g, v, idx_map):
    orbit = []
    current = v
    for _ in range(120):
        idx = idx_map[qq_key(current)]
        if orbit and idx == orbit[0]:
            return orbit
        orbit.append(idx)
        g_inv = qq_conjugate(g)
        current = qq_mul(qq_mul(g, current), g_inv)
    return orbit


def main():
    print("=" * 76)
    print("Route C-inner weighted: T_τ(v) = τvτ⁻¹ with κ cocycle.")
    print("=" * 76)

    verts = build_vertices()
    identity = (q_one(), q_zero(), q_zero(), q_zero())
    id_idx = vertex_index_exact(identity, verts)
    verts[0], verts[id_idx] = verts[id_idx], verts[0]
    idx_map = vertex_index_map(verts)
    identity_key = qq_key(identity)

    # --- shells (exact) -----------------------------------
    shells_by_dist = defaultdict(list)
    for i, v in enumerate(verts):
        d_sq = qq_distance_sq(identity, v)
        shells_by_dist[d_sq].append(i)
    sorted_dists = list(shells_by_dist.keys())
    n_dist = len(sorted_dists)
    for i in range(n_dist):
        for j in range(i + 1, n_dist):
            if qsq5_less(sorted_dists[j], sorted_dists[i]):
                sorted_dists[i], sorted_dists[j] = sorted_dists[j], sorted_dists[i]
    shell_of_idx = {}
    for shell_num, d_sq in enumerate(sorted_dists):
        for v_idx in shells_by_dist[d_sq]:
            shell_of_idx[v_idx] = shell_num
    kappa = {i: (shell_of_idx[i] - 4) ** 2 for i in range(120)}
    print(f"\n[Cw.1] shells built, κ(v) = (shell-4)² assigned.")

    # --- τ ------------------------------------------------
    for i, v in enumerate(verts):
        if i == 0:
            continue
        if element_order(v, idx_map, identity_key) == 10:
            tau = v
            tau_idx = i
            break

    # --- conjugation orbits -------------------------------
    visited = [False] * 120
    orbits = []
    for start in range(120):
        if visited[start]:
            continue
        orb = conjugation_orbit(tau, verts[start], idx_map)
        for idx in orb:
            visited[idx] = True
        orbits.append(orb)

    # --- K values and multiplicities ----------------------
    length_K_mult = Counter()  # (length, K) -> count
    for orb in orbits:
        length = len(orb)
        K = sum(kappa[v] for v in orb)
        length_K_mult[(length, K)] += 1
    print(f"\n[Cw.2] (length, K) distribution of orbits:")
    for (length, K), m in sorted(length_K_mult.items()):
        print(f"  length {length:2d}, K = {K:3d}: {m:2d} orbits  →  weight φ^{K} at z^{length}")

    # --- build weighted zeta ζ_C(z) ------------------------
    print(f"\n[Cw.3] Weighted zeta ζ_C(z) = ∏ (1 - φ^K z^length)^{{-m}}:")
    max_deg = 20
    zeta_C = [zphi_pair_zero()] * (max_deg + 1)
    zeta_C[0] = zphi_pair_one()
    for (length, K), m in length_K_mult.items():
        phi_K = phi_power(K)
        factor = geometric_series_inverse(phi_K, length, max_deg)
        for _ in range(m):
            zeta_C = poly_mul(zeta_C, factor, max_deg)

    print(f"  ζ_C(z) coefficients (a + b·√5):")
    for d in range(min(max_deg + 1, 11)):
        a, b = zeta_C[d]
        print(f"    [z^{d:2d}] = {a}  +  {b}·√5")

    # --- σ-symmetric ẑ_C ----------------------------------
    zeta_C_sigma = [sigma_pair(c) for c in zeta_C]
    zeta_C_sym = poly_mul(zeta_C, zeta_C_sigma, max_deg)
    print(f"\n[Cw.4] σ-symmetric ẑ_C(z) = ζ_C · σ(ζ_C):")
    for d in range(min(max_deg + 1, 11)):
        a, b = zeta_C_sym[d]
        tag = "σ-FIXED ✓" if b == 0 else f"σ-NOT-FIXED ({b})"
        print(f"    [z^{d:2d}] = {a}  +  {b}·√5   {tag}")

    sigma_fail = [d for d in range(max_deg + 1) if zeta_C_sym[d][1] != 0]
    if sigma_fail:
        print(f"  FAIL: σ-parts non-zero at {sigma_fail}")
        sys.exit(1)
    print(f"\n  OK: ẑ_C(z) ∈ Z[[z]] up to degree {max_deg}.")

    # --- structural summary -------------------------------
    print(f"\n[Cw.5] Structure of ẑ_C(z):")
    print(f"  ẑ_C(z) = ∏_{{(length, K, m) ∈ orbits}} (1 - φ^K z^length)^{{-m}}")
    print(f"        · (1 - σ(φ)^K z^length)^{{-m}}")
    print(f"  Factors present (unique (length, K) with multiplicities):")
    for (length, K), m in sorted(length_K_mult.items()):
        print(f"    length={length}, K={K}, mult={m}:  (1 - L_{K} z^{length} + z^{2*length})^{{-{m}}}")

    # Multi-length structure: this IS a multi-prime-like rational function
    lengths = set(l for (l, _) in length_K_mult.keys())
    print(f"\n  Distinct orbit lengths: {sorted(lengths)}")
    if len(lengths) > 1:
        print(f"  FINDING: ẑ_C(z) has MULTIPLE orbit lengths ({sorted(lengths)}) →")
        print(f"           genuine multi-prime rational function (not single local factor).")
        print(f"           Candidate for richer Dirichlet-series analysis (B11).")
    else:
        print(f"  Finding: single orbit length — still local factor.")

    print()
    print("=" * 76)
    print("Route C-inner WEIGHTED complete (exact arithmetic).")
    print("=" * 76)


if __name__ == "__main__":
    main()
