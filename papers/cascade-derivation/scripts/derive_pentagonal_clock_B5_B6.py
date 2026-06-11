#!/usr/bin/env python3
"""
Build B5/B6: exact canonicity of the order-10 pentagonal generator τ ∈ 2I
and of the left-multiplication clock convention T_τ: v ↦ τ · v on 2I.

Delivers:
  B5. Enumerate all elements of 2I by order. Verify |2I| = 120,
      orders divide 2·|I| = 60, and the order-10 stratum has
      exact size (classical: 24 elements of order 10 in 2I ≅ SL₂(F₅),
      splitting into TWO conjugacy classes of 12 each — τ and τ⁻¹
      sit in distinct classes when the group lacks an inverting
      automorphism, which is the case here). Test canonicity within
      a class: pick a representative τ, verify its conjugacy class
      has size 12, and read the script's verdict for class
      multiplicity. The choice of τ is canonical up to conjugation
      within the chosen class.
  B6. Cycle-decompose the left-multiplication action T_τ(v) = τ · v
      on 2I. Unweighted sanity: expect 12 cycles of length 10
      (since T_τ is the left translation by an order-10 element of
      a group of order 120). Then verify Fix(T_τ^n) pattern:
        Fix(T^1) = Fix(T^2) = Fix(T^5) = ∅
        Fix(T^10) = 2I (120 vertices)
      and more generally Fix(T^n) = ∅ for n ∈ {1,...,9} \\ {10}.

Refuses floats. All arithmetic in Q(√5) via Fraction pairs.

Depends on run_icosian_exact.py vertex enumeration (imported directly).

STOP conditions (do not hand-tune; report FAIL instead):
  - If |2I| != 120: FAIL
  - If any Hamilton product lands outside 2I: FAIL
  - If order-10 stratum size != 24 (= 2 classes × 12): FAIL
  - If the chosen τ's conjugacy class size != 12: FAIL
  - If cycle decomposition != 12 × 10: FAIL
  - If Fix(T^n) pattern disagrees with the prediction: FAIL

Run: python3 papers/cascade-derivation/scripts/derive_pentagonal_clock_B5_B6.py
"""

from __future__ import annotations

import sys
from pathlib import Path
from fractions import Fraction
from collections import defaultdict

# Import exact Q(√5) / quaternion machinery from run_icosian_exact.py
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
sys.path.insert(0, str(REPO_ROOT / "papers" / "paper-xxii" / "scripts"))

from run_icosian_exact import (  # noqa: E402
    q_zero, q_one, q_neg, q_add, q_sub, q_mul, q_scale,
    qq_mul, qq_conjugate, qq_norm_sq, qq_eq, qq_key,
    build_vertices, vertex_index_map, vertex_index_exact,
    phi, inv_phi, phi_half, inv_2phi,
)


def element_order(g, verts_idx_map, identity_key, max_order=120):
    """Return the order of g in 2I via exact Hamilton products.
    Uses repeated squaring / multiplication; bounded by |2I| = 120."""
    power = g
    for n in range(1, max_order + 1):
        if qq_key(power) == identity_key:
            return n
        power = qq_mul(power, g)
    raise RuntimeError("order not found up to max_order")


def left_mult_cycles(tau, verts, idx_map):
    """Decompose the permutation T_τ: v ↦ τ·v on 2I into cycles.
    Return (cycle_lengths, cycles) where cycles is a list of
    index-tuples."""
    n = len(verts)
    visited = [False] * n
    cycles = []
    for start in range(n):
        if visited[start]:
            continue
        orbit = []
        i = start
        while not visited[i]:
            visited[i] = True
            orbit.append(i)
            new = qq_mul(tau, verts[i])
            j = idx_map[qq_key(new)]
            i = j
        cycles.append(orbit)
    return [len(c) for c in cycles], cycles


def fix_Tn(tau, verts, idx_map, n):
    """Return indices of v in 2I with τ^n · v = v (i.e., τ^n = 1)."""
    # Compute τ^n once, then check per-v
    tau_n = verts[idx_map[qq_key((q_one(), q_zero(), q_zero(), q_zero()))]]  # identity
    # Actually compute τ^n directly
    tau_n = (q_one(), q_zero(), q_zero(), q_zero())
    for _ in range(n):
        tau_n = qq_mul(tau_n, tau)
    identity_key = qq_key((q_one(), q_zero(), q_zero(), q_zero()))
    if qq_key(tau_n) == identity_key:
        # τ^n = 1, so every v is fixed
        return list(range(len(verts)))
    else:
        # τ^n ≠ 1, so τ^n · v = v ⟹ τ^n = 1, contradiction; no fixed points
        return []


def conjugacy_class_of(g, verts, idx_map):
    """Compute the full conjugacy class of g in 2I by exact conjugation."""
    gk = qq_key(g)
    cls = set()
    for h in verts:
        h_inv = qq_conjugate(h)
        conj = qq_mul(qq_mul(h, g), h_inv)
        cls.add(qq_key(conj))
    return cls


def main():
    print("=" * 72)
    print("Build B5/B6 — canonicity of order-10 generator τ ∈ 2I and")
    print("             cycle decomposition of left-mult clock T_τ.")
    print("             All arithmetic exact over Q(√5) (Fraction pairs).")
    print("=" * 72)

    # --- Step 1: build 120 vertices -----------------------------
    verts = build_vertices()
    assert len(verts) == 120, f"FAIL: got {len(verts)} vertices, expected 120"
    print(f"\n[B5.1] 120 vertices built exactly in Q(√5). OK.")

    # Move identity (1,0,0,0) to index 0
    identity = (q_one(), q_zero(), q_zero(), q_zero())
    id_idx = vertex_index_exact(identity, verts)
    assert id_idx >= 0, "FAIL: identity not in vertex set"
    verts[0], verts[id_idx] = verts[id_idx], verts[0]
    idx_map = vertex_index_map(verts)
    identity_key = qq_key(identity)

    # --- Step 2: compute order of every element ------------------
    print(f"\n[B5.2] Computing exact orders of all 120 elements...")
    orders = defaultdict(list)
    for i, v in enumerate(verts):
        n = element_order(v, idx_map, identity_key)
        orders[n].append(i)
    order_counts = {n: len(lst) for n, lst in sorted(orders.items())}
    print(f"  order multiset: {order_counts}")

    # Classical result for 2I ≅ SL₂(F₅):
    #   order 1: 1 element (identity)
    #   order 2: 1 element (-1, the centre)
    #   order 3: 20 elements
    #   order 4: 30 elements
    #   order 5: 24 elements
    #   order 6: 20 elements
    #   order 10: 24 elements
    # Total: 1+1+20+30+24+20+24 = 120. OK.
    expected_orders = {1: 1, 2: 1, 3: 20, 4: 30, 5: 24, 6: 20, 10: 24}
    if order_counts != expected_orders:
        print(f"  FAIL: order distribution != expected {expected_orders}")
        sys.exit(1)
    print(f"  OK: matches classical 2I ≅ SL₂(F₅) order distribution.")

    # --- Step 3: Are all order-10 elements conjugate? ------------
    print(f"\n[B5.3] Testing conjugacy of order-10 elements...")
    order10 = orders[10]
    print(f"  {len(order10)} elements of order 10.")
    # Pick the first; compute its conjugacy class
    g0 = verts[order10[0]]
    cls0 = conjugacy_class_of(g0, verts, idx_map)
    cls0_indices = {idx_map[k] for k in cls0}
    order10_set = set(order10)
    # Expected: order-10 splits into TWO conjugacy classes of 12 each
    # (τ and τ⁻¹ = τ⁹ are not necessarily conjugate in 2I even though
    #  both have order 10; in SL₂(F₅) the elements of order 10 split
    #  into two rational conjugacy classes, τ and τ⁻¹, but pairs
    #  {τ, τ⁻¹} are conjugate iff the group contains that inversion).
    print(f"  conjugacy class of first order-10 element: size {len(cls0_indices)}")
    if cls0_indices == order10_set:
        print(f"  All {len(order10)} order-10 elements are conjugate (single class).")
        n_order10_classes = 1
    else:
        # Split: find the second class
        remaining = order10_set - cls0_indices
        if not remaining:
            print(f"  FAIL: conjugacy class of order-10 element inconsistent")
            sys.exit(1)
        g1 = verts[next(iter(remaining))]
        cls1 = conjugacy_class_of(g1, verts, idx_map)
        cls1_indices = {idx_map[k] for k in cls1}
        if cls0_indices | cls1_indices == order10_set and cls0_indices.isdisjoint(cls1_indices):
            print(f"  Order-10 splits into 2 conjugacy classes: sizes "
                  f"{len(cls0_indices)} + {len(cls1_indices)} = {len(order10)}")
            n_order10_classes = 2
            if len(cls0_indices) != 12 or len(cls1_indices) != 12:
                print(f"  FAIL: expected 12+12 split, got {len(cls0_indices)}+{len(cls1_indices)}")
                sys.exit(1)
        else:
            print(f"  FAIL: order-10 conjugacy structure unexpected")
            sys.exit(1)

    # Canonicity: τ is canonical up to conjugation within its class
    # (one of 2 classes of 12 elements each). Choose τ = g0 as the
    # canonical representative of its class.
    tau = g0
    print(f"\n[B5.4] Canonical τ chosen as first order-10 element (class 1 rep).")
    print(f"  τ coordinates in Q(√5) (as (a+b√5 per component)):")
    for c_idx, c in enumerate(tau):
        print(f"    τ[{c_idx}] = {c[0]} + {c[1]}·√5")

    # --- Step 4: verify τ⁵ = −1 -----------------------------------
    tau5 = tau
    for _ in range(4):
        tau5 = qq_mul(tau5, tau)
    neg_identity = (q_neg(q_one()), q_zero(), q_zero(), q_zero())
    if not qq_eq(tau5, neg_identity):
        print(f"  FAIL: τ⁵ != -1; got {tau5}")
        sys.exit(1)
    print(f"\n[B5.5] τ⁵ = −1 (central element of 2I). OK.")

    tau10 = qq_mul(tau5, tau5)
    if not qq_eq(tau10, identity):
        print(f"  FAIL: τ¹⁰ != 1")
        sys.exit(1)
    print(f"        τ¹⁰ = 1. OK.")

    # --- Step 5: cycle decomposition of T_τ(v) = τ · v -----------
    print(f"\n[B6.1] Cycle decomposition of left-multiplication T_τ: v ↦ τ·v...")
    cycle_lens, cycles = left_mult_cycles(tau, verts, idx_map)
    cycle_count = {l: cycle_lens.count(l) for l in sorted(set(cycle_lens))}
    print(f"  cycle-length multiset: {cycle_count}")
    expected_cycles = {10: 12}
    if cycle_count != expected_cycles:
        print(f"  FAIL: expected {expected_cycles}, got {cycle_count}")
        sys.exit(1)
    print(f"  OK: exactly 12 cycles of length 10, total 120 vertices.")

    # --- Step 6: Fix(T^n) structure ------------------------------
    print(f"\n[B6.2] Fix(T^n) for n = 1..10:")
    fix_pattern = {}
    for n in range(1, 11):
        fn = fix_Tn(tau, verts, idx_map, n)
        fix_pattern[n] = len(fn)
        tag = "all 120" if len(fn) == 120 else "empty" if len(fn) == 0 else f"{len(fn)} pts"
        print(f"    |Fix(T^{n})| = {len(fn)}  ({tag})")
    expected_fix = {n: 0 for n in range(1, 10)}
    expected_fix[10] = 120
    if fix_pattern != expected_fix:
        print(f"  FAIL: Fix pattern != expected {expected_fix}")
        sys.exit(1)
    print(f"  OK: Fix(T^n) = ∅ for 1 ≤ n < 10; Fix(T^10) = 2I.")

    # --- Summary -------------------------------------------------
    print()
    print("=" * 72)
    print("BUILD B5/B6 COMPLETE (sim-verified).")
    print("  - B5: order-10 class canonical (24 elements = 2 conjugacy")
    print(f"       classes of 12); τ chosen as class-1 rep; τ⁵ = −1.")
    print("  - B6: left-mult clock T_τ decomposes 2I into 12 cycles of")
    print("       length 10; Fix(T^n) = ∅ for 1 ≤ n < 10, Fix(T^10) = 2I.")
    print("  - Unweighted Artin–Mazur zeta sanity:")
    print("       ζ_T(z) = (1 - z^10)^(-12)")
    print("       (12 cycles of length 10, no shorter orbits.)")
    print("=" * 72)
    print()
    print("Next builds needed:")
    print("  B7: local frame attachment at each v ∈ 2I.")
    print("  B8: holonomy cocycle ω: edges → Z[φ]× from B7.")
    print("  B9: weighted zeta ζ_{T,ω}(z) from cycle weights.")
    print("  B10: σ-equivariance theorem.")
    print("  B11: Mellin / critical-line bridge.")
    print("  B12: Dedekind reduction audit vs ζ_K = ζ · L(χ_5).")


if __name__ == "__main__":
    main()
