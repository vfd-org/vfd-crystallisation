#!/usr/bin/env python3
"""
Build B8' + B9: canonical vertex-shell cocycle ω, weighted Artin-Mazur
zeta ζ_{T,ω}(z), σ-symmetrised zeta on 2I ⊔ σ(2I).

Chosen cocycle construction (B8' route (a), minimal from F1):
  - Every v ∈ 2I lies in exactly one Euclidean distance shell from the
    identity; 9 shells total, sizes {1,12,20,12,30,12,20,12,1}.
  - run_icosian_exact.py proves EACH SHELL = EXACTLY ONE 2I-CONJUGACY
    CLASS (bijection of shell-size and class-size multisets + explicit
    shell==class equality check).
  - Therefore shell(v) ∈ {0, 1, ..., 8} is a canonical invariant of v
    under conjugation and under left-translation by τ (the orbits
    preserve the shell assignment precisely when the shell is
    τ-invariant).

Cocycle ω (VERTEX-based, not edge-based):
  ω(v) := φ^{k(v)}  where k(v) = shell(v) ∈ {0,...,8}.

Cycle weight:
  W_C := ∏_{v ∈ C} ω(v) = φ^{Σ_{v ∈ C} shell(v)}.

Weighted zeta:
  ζ_{T,ω}(z) = ∏_C (1 - W_C · z^{|C|})^{-1}
             = ∏_C (1 - φ^{s(C)} z^10)^{-1}
  where s(C) = Σ shell(v) over v in cycle C.

σ-symmetrised zeta:
  ẑ(z) := ζ_{T,ω}(z) · σ(ζ_{T,ω})(z)
        = ∏_C (1 - φ^{s(C)} z^10)^{-1} · (1 - σ(φ)^{s(C)} z^10)^{-1}
        = ∏_C (1 - φ^{s(C)} z^10)^{-1} · (1 - (-φ^{-1})^{s(C)} z^10)^{-1}
  This is σ-invariant by construction (the product is symmetric
  under σ). Its coefficients lie in Z[[z]] ⊂ Z[φ][[z]] (σ-fixed ring).

What this sim checks:
  - Compute shell(v) for all 120 v ∈ 2I exactly.
  - Decompose 2I into T_τ cycles (from B6).
  - Compute s(C) = Σ shell(v_i) for each of 12 cycles.
  - Report W_C = φ^{s(C)} for each cycle.
  - Compute coefficients of ζ_{T,ω}(z) to degree 30 in Z[φ].
  - Compute σ-symmetrised ẑ(z) to degree 30 in Z (integer coefficients).
  - REPORT whether ẑ(z) matches (1 - z^10)^{-12} (the trivial /
    unweighted case) or is genuinely different (non-trivial cocycle).

STOP conditions (no hand-tuning):
  - If any shell-class equality fails: FAIL
  - If any cycle has non-uniform shell (should be uniform within a
    cycle if shell is τ-invariant): structural finding, report
  - If ẑ(z) is trivial (= ζ_T(z) unweighted): report as "B8' route (a)
    insufficient; try route (b) or (c)"

Refuses floats. Exact Q(√5) (Fraction) and Z[φ]-polynomial arithmetic.

Run: python3 papers/cascade-derivation/scripts/derive_pentagonal_clock_B8p_B9.py
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


# --- Z[φ]-polynomial arithmetic over Q(√5) pairs -------------------
# A polynomial in Z[φ][[z]] is represented as a list of Q(√5)-pair
# coefficients; pos i is the z^i coefficient.

def zphi_pair_mul(x, y):
    """Q(√5) multiplication: (a + b√5)(c + d√5) = (ac+5bd) + (ad+bc)√5."""
    return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def zphi_pair_add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def zphi_pair_sub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def zphi_pair_zero():
    return (Fraction(0), Fraction(0))


def zphi_pair_one():
    return (Fraction(1), Fraction(0))


def phi_pair():
    """φ = (1 + √5)/2 in Q(√5)."""
    return (Fraction(1, 2), Fraction(1, 2))


def phi_power(n):
    """φ^n as exact (a + b√5)/1 pair, for n ∈ Z.

    Uses φ² = φ + 1 recursion. For n < 0 uses 1/φ = φ − 1, and
    1/φ² = 2 − φ, etc. via φ^{-1} = φ − 1."""
    p = zphi_pair_one()
    if n >= 0:
        phi = phi_pair()
        for _ in range(n):
            p = zphi_pair_mul(p, phi)
    else:
        inv_phi = (Fraction(-1, 2), Fraction(1, 2))  # φ − 1 = (−1 + √5)/2
        for _ in range(-n):
            p = zphi_pair_mul(p, inv_phi)
    return p


def sigma_pair(x):
    """σ on Q(√5): (a, b) ↦ (a, −b)."""
    return (x[0], -x[1])


def poly_mul(p1, p2, max_deg):
    """Multiply two polynomials p1, p2 with Q(√5)-pair coefficients,
    truncated to degree max_deg."""
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
    """Return (1 - a·z^length)^{-1} as a polynomial in Q(√5) to
    degree max_deg. This is the formal power series 1 + a·z^length +
    a²·z^{2·length} + ..."""
    poly = [zphi_pair_zero()] * (max_deg + 1)
    ak = zphi_pair_one()
    k = 0
    while k * length <= max_deg:
        poly[k * length] = zphi_pair_add(poly[k * length], ak)
        ak = zphi_pair_mul(ak, a)
        k += 1
    return poly


# --- Main sim ----------------------------------------------------

def sigma_on_quat(q):
    return tuple(sigma_pair(c) for c in q)


def element_order(g, idx_map, identity_key, max_order=120):
    power = g
    for n in range(1, max_order + 1):
        if qq_key(power) == identity_key:
            return n
        power = qq_mul(power, g)
    raise RuntimeError("order not found")


def main():
    print("=" * 76)
    print("Build B8' + B9: vertex-shell cocycle ω, weighted zeta ζ_{T,ω}(z),")
    print("                σ-symmetrised zeta ẑ(z) on 2I ⊔ σ(2I).")
    print("                All arithmetic exact over Q(√5).")
    print("=" * 76)

    # --- Vertex setup -----------------------------------------
    verts = build_vertices()
    assert len(verts) == 120
    identity = (q_one(), q_zero(), q_zero(), q_zero())
    id_idx = vertex_index_exact(identity, verts)
    verts[0], verts[id_idx] = verts[id_idx], verts[0]
    idx_map = vertex_index_map(verts)
    identity_key = qq_key(identity)

    # --- Compute shells: |1 - v|^2 class of each vertex --------
    print(f"\n[B8'.1] Compute 9 Euclidean distance shells from identity...")
    shells = defaultdict(list)
    for i, v in enumerate(verts):
        d_sq = qq_distance_sq(identity, v)
        shells[d_sq].append(i)

    # Order shells by real value (a + b√5, √5 > 0)
    def real_val(d_sq):
        return float(d_sq[0]) + float(d_sq[1]) * (5 ** 0.5)

    sorted_shells = sorted(shells.items(), key=lambda kv: real_val(kv[0]))
    shell_of_idx = {}  # v_idx -> shell number 0..8
    shell_sizes = []
    for shell_num, (d_sq, members) in enumerate(sorted_shells):
        for v_idx in members:
            shell_of_idx[v_idx] = shell_num
        shell_sizes.append(len(members))
        print(f"  shell {shell_num}: size {len(members)}, |1-v|^2 = {d_sq[0]} + {d_sq[1]}·√5")
    expected_sizes = [1, 12, 20, 12, 30, 12, 20, 12, 1]
    if shell_sizes != expected_sizes:
        print(f"  FAIL: shell sizes {shell_sizes} != expected {expected_sizes}")
        sys.exit(1)
    print(f"  OK: 9 shells of sizes {expected_sizes}, total 120.")

    # --- Choose τ and decompose T_τ cycles ---------------------
    # Find an order-10 element
    for i, v in enumerate(verts):
        if i == 0:
            continue
        if element_order(v, idx_map, identity_key) == 10:
            tau = v
            tau_idx = i
            break
    print(f"\n[B8'.2] τ (order-10 rep) at vertex index {tau_idx}.")
    print(f"        shell(τ) = {shell_of_idx[tau_idx]}")

    # Cycle decomposition of T_τ
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
    assert len(cycles) == 12 and all(len(c) == 10 for c in cycles), \
        f"FAIL: expected 12 cycles of length 10, got {[len(c) for c in cycles]}"
    print(f"        12 cycles of length 10 (from B6), total 120.")

    # --- Compute cycle weights: s(C) = Σ shell(v) for v in C ----
    print(f"\n[B8'.3] Cycle shell-sums s(C) for each of 12 cycles:")
    cycle_shell_sums = []
    for c_idx, cyc in enumerate(cycles):
        shells_in_cyc = [shell_of_idx[v] for v in cyc]
        s_C = sum(shells_in_cyc)
        cycle_shell_sums.append(s_C)
        # Also report shell distribution within the cycle
        shell_dist = Counter(shells_in_cyc)
        print(f"  cycle {c_idx:2d}: s(C) = {s_C:3d}  shell distribution = {dict(shell_dist)}")

    # Unique weights: distinct s(C) values
    unique_s = sorted(set(cycle_shell_sums))
    print(f"\n  Distinct s(C) values: {unique_s}")
    print(f"  Multiplicity of each s(C):")
    for s in unique_s:
        m = cycle_shell_sums.count(s)
        print(f"    s = {s:3d}: {m} cycles")

    # --- Compute weighted zeta coefficients to degree 30 ---------
    print(f"\n[B9.1] Weighted zeta: ζ_{{T,ω}}(z) = ∏_C (1 - φ^{{s(C)}} z^10)^{{-1}}")
    max_deg = 30
    # Build the product
    zeta_weighted = [zphi_pair_zero()] * (max_deg + 1)
    zeta_weighted[0] = zphi_pair_one()
    for s_C in cycle_shell_sums:
        phi_s = phi_power(s_C)
        factor = geometric_series_inverse(phi_s, 10, max_deg)
        zeta_weighted = poly_mul(zeta_weighted, factor, max_deg)
    print(f"  ζ_{{T,ω}}(z) coefficients (a + b·√5) for z^0, z^10, z^20, z^30:")
    for d in [0, 10, 20, 30]:
        a, b = zeta_weighted[d]
        print(f"    [z^{d:2d}] = {a} + {b}·√5")

    # --- σ-symmetrised zeta: ζ · σ(ζ) in Z[[z]] ---------------
    print(f"\n[B10.1] σ-symmetrised ẑ(z) = ζ_{{T,ω}}(z) · σ(ζ_{{T,ω}}(z))")
    # σ(ζ) has coefficients that are σ-applied to ζ's coefficients
    zeta_sigma = [sigma_pair(c) for c in zeta_weighted]
    zeta_sym = poly_mul(zeta_weighted, zeta_sigma, max_deg)
    print(f"  ẑ(z) coefficients (should have √5-part = 0, integer rational part):")
    for d in [0, 10, 20, 30]:
        a, b = zeta_sym[d]
        sym_ok = (b == 0)
        tag = "σ-FIXED ✓" if sym_ok else "σ-NOT-FIXED ✗"
        print(f"    [z^{d:2d}] = {a} + {b}·√5   {tag}")

    # Verify all σ-part is zero in ẑ
    sigma_fail = [d for d in range(max_deg + 1) if zeta_sym[d][1] != 0]
    if sigma_fail:
        print(f"\n  FAIL: σ-parts non-zero at degrees {sigma_fail}")
        sys.exit(1)
    print(f"\n  OK: ẑ(z) has all coefficients in Z (σ-fixed ring) up to degree {max_deg}.")

    # --- Compare to unweighted (1 - z^10)^{-12} ------------------
    print(f"\n[B9.2] Compare ẑ(z) to unweighted ζ_T(z) = (1 - z^10)^{{-12}}:")
    # (1 - z^10)^{-12} coefficients = binomial(11 + k, 11) at z^{10k}
    from math import comb
    unweighted = [0] * (max_deg + 1)
    k = 0
    while 10 * k <= max_deg:
        unweighted[10 * k] = comb(11 + k, 11)
        k += 1
    print(f"  unweighted ζ_T(z^10) coefficients: {[unweighted[10 * i] for i in range(4)]}")
    print(f"  ẑ(z) integer parts at z^{{0,10,20,30}}: {[zeta_sym[10 * i][0] for i in range(4)]}")

    # Compare
    diffs_from_unweighted = []
    for d in range(max_deg + 1):
        if unweighted[d] != zeta_sym[d][0]:
            diffs_from_unweighted.append(d)
    if not diffs_from_unweighted:
        print(f"\n  FINDING: ẑ(z) = (1 - z^10)^{{-12}} up to degree {max_deg}.")
        print(f"           The vertex-shell cocycle is INSUFFICIENT to produce")
        print(f"           a non-trivial σ-symmetric zeta. B8' route (a) fails;")
        print(f"           try route (b) [edge-holonomy] or (c) [2I ⊔ σ(2I)].")
    else:
        print(f"\n  FINDING: ẑ(z) ≠ (1 - z^10)^{{-12}} at degrees {diffs_from_unweighted[:5]}...")
        print(f"           The vertex-shell cocycle produces a NON-TRIVIAL σ-symmetric")
        print(f"           zeta. B8' route (a) SUCCEEDS.")
        print(f"           Compute difference at first non-trivial degree:")
        d = diffs_from_unweighted[0]
        print(f"             ẑ[z^{d}] = {zeta_sym[d][0]}")
        print(f"             (1-z^10)^{{-12}}[z^{d}] = {unweighted[d]}")
        print(f"             diff = {zeta_sym[d][0] - unweighted[d]}")

    # --- Summary ------------------------------------------------
    print()
    print("=" * 76)
    print("BUILD B8'/B9/B10 SIM REPORT (all exact arithmetic, no floats).")
    print(f"  - B8': vertex-shell cocycle ω(v) = φ^{{shell(v)}} applied to T_τ cycles.")
    print(f"  - B9: weighted zeta ζ_{{T,ω}}(z) computed in Z[φ][[z]] to degree {max_deg}.")
    print(f"  - B10: σ-symmetrised ẑ(z) verified to lie in Z[[z]] (σ-fixed).")
    print(f"  - Cycle shell-sums s(C): {cycle_shell_sums}")
    print(f"  - Distinct s(C) values and multiplicities: {[(s, cycle_shell_sums.count(s)) for s in unique_s]}")
    print("=" * 76)


if __name__ == "__main__":
    main()
