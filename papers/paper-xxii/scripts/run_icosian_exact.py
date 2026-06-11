#!/usr/bin/env python3
"""
Exact-arithmetic verification of the icosian group-structure and Euclidean-
shell = 2I-conjugacy-class statements used in Paper XXII Theorem thm:decoupling.

All computations are carried out in Q(sqrt(5)), represented as pairs
(a, b) with a, b in Python's Fraction type, standing for a + b*sqrt(5).
Every coordinate of a 600-cell vertex lies in Q(sqrt(5)) (coefficients are
0, +-1/2, +-1, and +-(phi)/2 = +-(1 + sqrt(5))/4), and Hamilton products
preserve Q(sqrt(5)) entries; distances squared are rational, so the shell
decomposition can be computed without any floating-point tolerance.

Output confirms EXACTLY (no tolerances) the four computer-assisted lemmas
of Paper XXII Theorem thm:decoupling:
  (L2)  group closure: all 14400 Hamilton products lie in the vertex set;
  (L3a) 9 conjugacy classes of sizes {1, 1, 12, 12, 12, 12, 20, 20, 30};
  (L3b) 9 Euclidean distance shells from the identity with exact squared-
        distance representatives in Q(sqrt(5)) and sizes
        {1, 12, 20, 12, 30, 12, 20, 12, 1};
  (L3c) each Euclidean shell is EXACTLY ONE 2I-conjugacy class, with a
        size-preserving bijection.

Runs with only Python's standard library (fractions).
"""

from __future__ import annotations

import itertools
from fractions import Fraction
from collections import defaultdict


# --- Q(sqrt(5)) as (a, b) -> a + b*sqrt(5), with a, b in Fraction -------

def q_add(x, y):
    return (x[0] + y[0], x[1] + y[1])

def q_sub(x, y):
    return (x[0] - y[0], x[1] - y[1])

def q_neg(x):
    return (-x[0], -x[1])

def q_mul(x, y):
    # (a + b sqrt5)(c + d sqrt5) = ac + 5bd + (ad + bc) sqrt5
    return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])

def q_scale(x, s):
    # s is a Fraction (rational scalar)
    return (x[0] * s, x[1] * s)

def q_zero():
    return (Fraction(0), Fraction(0))

def q_one():
    return (Fraction(1), Fraction(0))

def q_half():
    return (Fraction(1, 2), Fraction(0))

# phi = (1 + sqrt(5))/2  represented in Q(sqrt(5))
def phi():
    return (Fraction(1, 2), Fraction(1, 2))

# 1/phi = phi - 1  (standard identity phi^2 = phi + 1)
def inv_phi():
    p = phi()
    return q_sub(p, q_one())

# phi / 2
def phi_half():
    return (Fraction(1, 4), Fraction(1, 4))

# 1 / (2 phi) = (phi - 1) / 2
def inv_2phi():
    ip = inv_phi()
    return q_scale(ip, Fraction(1, 2))


# --- Quaternion = 4-tuple of Q(sqrt(5)) entries ------------------------

def quat(w, x, y, z):
    return (w, x, y, z)

def qq_eq(a, b):
    return a[0] == b[0] and a[1] == b[1] and a[2] == b[2] and a[3] == b[3]

def qq_key(a):
    # hashable representation for set lookup; exact Q(sqrt5) pair keys
    return tuple((v[0], v[1]) for v in a)

def qq_mul(a, b):
    """Hamilton product of quaternions over Q(sqrt(5))."""
    aw, ax, ay, az = a
    bw, bx, by, bz = b
    # w = aw bw - ax bx - ay by - az bz
    # x = aw bx + ax bw + ay bz - az by
    # y = aw by - ax bz + ay bw + az bx
    # z = aw bz + ax by - ay bx + az bw
    w = q_sub(q_mul(aw, bw),
              q_add(q_add(q_mul(ax, bx), q_mul(ay, by)), q_mul(az, bz)))
    x = q_add(q_add(q_mul(aw, bx), q_mul(ax, bw)),
              q_sub(q_mul(ay, bz), q_mul(az, by)))
    y = q_add(q_sub(q_mul(aw, by), q_mul(ax, bz)),
              q_add(q_mul(ay, bw), q_mul(az, bx)))
    z = q_add(q_add(q_mul(aw, bz), q_mul(ax, by)),
              q_sub(q_mul(az, bw), q_mul(ay, bx)))
    return (w, x, y, z)

def qq_conjugate(a):
    """Quaternion conjugate (w, x, y, z) -> (w, -x, -y, -z)."""
    w, x, y, z = a
    return (w, q_neg(x), q_neg(y), q_neg(z))

def qq_norm_sq(a):
    """|a|^2 in Q(sqrt(5))."""
    w, x, y, z = a
    return q_add(q_add(q_mul(w, w), q_mul(x, x)),
                 q_add(q_mul(y, y), q_mul(z, z)))

def qq_distance_sq(a, b):
    """|a - b|^2 in Q(sqrt(5))."""
    diff = tuple(q_sub(a[i], b[i]) for i in range(4))
    return qq_norm_sq(diff)

def parity(perm):
    s = 1
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if perm[i] > perm[j]:
                s = -s
    return s


# --- Build the 120 vertices ---------------------------------------------

def build_vertices():
    verts = []

    # Set 1: 8 of (+-1, 0, 0, 0) permutations
    for i in range(4):
        for s in (1, -1):
            v = [q_zero(), q_zero(), q_zero(), q_zero()]
            v[i] = q_scale(q_one(), Fraction(s))
            verts.append(tuple(v))

    # Set 2: 16 of (+-1/2, +-1/2, +-1/2, +-1/2)
    for signs in itertools.product((1, -1), repeat=4):
        v = tuple(q_scale(q_one(), Fraction(s, 2)) for s in signs)
        verts.append(v)

    # Set 3: 96 even permutations of (0, +-1/(2 phi), +-1/2, +-phi/2)
    base = [q_zero(), inv_2phi(), q_scale(q_one(), Fraction(1, 2)), phi_half()]
    for perm in itertools.permutations(range(4)):
        if parity(perm) != 1:
            continue
        permuted = tuple(base[p] for p in perm)
        zero_slot = None
        for idx, elt in enumerate(permuted):
            if elt == q_zero():
                zero_slot = idx
                break
        for signs in itertools.product((1, -1), repeat=3):
            v = list(permuted)
            j = 0
            for k in range(4):
                if k == zero_slot:
                    continue
                v[k] = q_scale(v[k], Fraction(signs[j]))
                j += 1
            verts.append(tuple(v))

    # Deduplicate via exact key
    seen = {}
    unique_verts = []
    for v in verts:
        k = qq_key(v)
        if k not in seen:
            seen[k] = len(unique_verts)
            unique_verts.append(v)
    assert len(unique_verts) == 120, f"got {len(unique_verts)} unique vertices"
    return unique_verts


def vertex_index_exact(v, verts):
    """Return index of v in verts via exact comparison; -1 if not found."""
    for i, u in enumerate(verts):
        if qq_eq(v, u):
            return i
    return -1


def vertex_index_map(verts):
    """Precompute key -> index map for O(1) lookup."""
    return {qq_key(v): i for i, v in enumerate(verts)}


def main():
    print("=" * 72)
    print("Exact-arithmetic verification (Q(sqrt(5))) of Paper XXII Theorem")
    print("thm:decoupling computer-assisted lemmas (L2), (L3a), (L3c).")
    print("=" * 72)

    verts = build_vertices()
    print(f"\n[L1] 120 vertices constructed; all coordinates in Q(sqrt(5)).")

    # Move identity (1,0,0,0) to index 0.
    identity = (q_one(), q_zero(), q_zero(), q_zero())
    id_idx = vertex_index_exact(identity, verts)
    assert id_idx >= 0
    verts[0], verts[id_idx] = verts[id_idx], verts[0]
    print(f"  identity placed at index 0.")

    idx_map = vertex_index_map(verts)

    # --- (L2) Group closure: all 14400 products lie in the vertex set ---
    print(f"\n[L2] Verifying group closure by exhaustive exact Hamilton products...")
    n = len(verts)
    fail = 0
    for i in range(n):
        for j in range(n):
            prod = qq_mul(verts[i], verts[j])
            k = idx_map.get(qq_key(prod))
            if k is None:
                fail += 1
    if fail:
        print(f"  FAIL: {fail} products landed outside the vertex set")
        return
    print(f"  OK: all {n * n} = 14400 Hamilton products lie in the vertex set (exact).")

    # --- (L3a) Conjugacy classes of 2I ---------------------------------
    print(f"\n[L3a] Computing 2I conjugacy classes by exact Hamilton conjugation...")
    classes = []
    assigned = [False] * n
    for i in range(n):
        if assigned[i]:
            continue
        cls = set()
        g = verts[i]
        for j in range(n):
            h = verts[j]
            h_inv = qq_conjugate(h)  # For unit quaternions, inverse = conjugate
            conj = qq_mul(qq_mul(h, g), h_inv)
            k = idx_map.get(qq_key(conj))
            assert k is not None, "conjugate not in vertex set"
            cls.add(k)
        for k in cls:
            assigned[k] = True
        classes.append(sorted(cls))
    class_sizes = sorted(len(c) for c in classes)
    print(f"  OK: {len(classes)} conjugacy classes with sizes {class_sizes}.")
    assert class_sizes == [1, 1, 12, 12, 12, 12, 20, 20, 30]

    # --- (L3c) Euclidean shells from identity, matched exactly to classes ---
    print(f"\n[L3b] Computing Euclidean distance shells from identity (exact |1 - v|^2)...")
    # Use |1 - v|^2 as the shell key; this is rational for all v (since all
    # coordinates are rational, so is w*w + x*x + y*y + z*z, and so is |1 - v|^2
    # after subtraction). Actually |1 - v|^2 is in Q(sqrt(5)); we use the exact pair.
    shells = defaultdict(list)
    for i, v in enumerate(verts):
        d_sq = qq_distance_sq(identity, v)
        shells[d_sq].append(i)

    print(f"  {len(shells)} distinct Euclidean squared-distances from identity:")
    shell_items = sorted(shells.items(), key=lambda kv: (float(kv[0][0]) + float(kv[0][1]) * 5 ** 0.5))
    for d_sq, members in shell_items:
        a, b = d_sq
        print(f"    |1 - v|^2 = {a} + {b}*sqrt(5)  ->  {len(members)} vertices")

    print(f"\n[L3c] Shell-class matching (each Euclidean shell = one conjugacy class)...")
    shell_sizes = sorted(len(m) for m in shells.values())
    print(f"  shell sizes: {shell_sizes}")
    print(f"  class sizes: {class_sizes}")
    assert shell_sizes == class_sizes, "shell-size multiset != class-size multiset"

    # Verify each shell is exactly one class
    all_match = True
    for d_sq, shell in shell_items:
        shell_set = set(shell)
        matched_class = None
        for cls in classes:
            cls_set = set(cls)
            if cls_set == shell_set:
                matched_class = cls
                break
            if cls_set.issubset(shell_set) and cls_set != shell_set:
                # shell is union of multiple classes
                print(f"  FAIL: shell of size {len(shell)} is union of multiple classes")
                all_match = False
                break
            if not cls_set.isdisjoint(shell_set) and not cls_set.issubset(shell_set):
                print(f"  FAIL: shell of size {len(shell)} splits a class")
                all_match = False
                break
        if matched_class is None and all_match:
            # Shell size matches a class size but no single class equals it
            # This can happen if multiple classes of the same size exist. Check unions.
            for cls in classes:
                if set(cls) == shell_set:
                    matched_class = cls
                    break
            if matched_class is None:
                print(f"  Shell of size {len(shell)} does not equal any single class exactly")
                all_match = False

    if all_match:
        print(f"  OK: every Euclidean distance shell from identity is EXACTLY ONE")
        print(f"      2I conjugacy class (exact equality, no tolerance).")
    else:
        print(f"  FAIL")
        return

    print()
    print("=" * 72)
    print("EXACT VERIFICATION COMPLETE")
    print("Lemmas (L2), (L3a), (L3b), (L3c) of Paper XXII Theorem thm:decoupling")
    print("are verified by exact arithmetic over Q(sqrt(5)). No floating-point")
    print("tolerance is used at any step.")
    print("=" * 72)


if __name__ == "__main__":
    main()
