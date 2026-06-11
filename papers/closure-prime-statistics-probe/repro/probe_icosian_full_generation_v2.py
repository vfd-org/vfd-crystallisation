#!/usr/bin/env python3
"""
Extended icosian-norm probe v2 (vectorized).

Strategy:
  1. Pre-compute the SET of achievable ||alpha||^2 values for
     alpha = m_1*v_{i_1} + ... + m_K*v_{i_K} with V_600 vertices v
     and small integer coefficients.  Use numpy vectorization.
  2. For each Z[phi]-prime target with norm <= NORM_MAX, look up
     the target value in the achievable-norms set.
  3. Also record an explicit alpha for each hit.

This is much faster than nested per-target search.

Run:
    python probe_icosian_full_generation_v2.py [NORM_MAX]
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from itertools import product, combinations
from collections import defaultdict

import numpy as np

PHI    = (1.0 + 5.0 ** 0.5) / 2.0
INVPHI = 1.0 / PHI
TOL    = 1e-5

OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def build_v600():
    half       = 0.5
    half_phi   = PHI / 2.0
    half_phi_i = 1.0 / (2.0 * PHI)
    verts = []
    for i in range(4):
        for s in (1.0, -1.0):
            v = [0.0]*4; v[i] = s
            verts.append(v)
    for s0 in (-1,1):
        for s1 in (-1,1):
            for s2 in (-1,1):
                for s3 in (-1,1):
                    verts.append([s0*half, s1*half, s2*half, s3*half])
    even_perms = [
        (0,1,2,3),(0,2,3,1),(0,3,1,2),
        (1,0,3,2),(1,2,0,3),(1,3,2,0),
        (2,0,1,3),(2,1,3,0),(2,3,0,1),
        (3,0,2,1),(3,1,0,2),(3,2,1,0),
    ]
    for p in even_perms:
        for sa in (-1,1):
            for sb in (-1,1):
                for sc in (-1,1):
                    v = [0.0]*4
                    v[p[0]] = sa*half_phi
                    v[p[1]] = sb*half
                    v[p[2]] = sc*half_phi_i
                    v[p[3]] = 0.0
                    verts.append(v)
    return np.array(verts, dtype=float)


def is_prime_int(n: int) -> bool:
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0: return False
    r = int(math.isqrt(n))
    for d in range(3, r + 1, 2):
        if n % d == 0: return False
    return True


def zphi_norm(a: int, b: int) -> int:
    return a*a + a*b - b*b


def classify_zphi(a: int, b: int) -> dict:
    n = abs(zphi_norm(a, b))
    if n == 0:   return {"class": "zero"}
    if n == 1:   return {"class": "unit"}
    if is_prime_int(n):
        p = n
        if p == 5:        return {"class": "ramified-prime", "rational_prime": p, "norm": p}
        if p % 5 in (1,4): return {"class": "split-prime", "rational_prime": p, "norm": p}
        return {"class": "anomaly"}
    sn = int(math.isqrt(n))
    if sn*sn == n and is_prime_int(sn) and sn % 5 in (2,3):
        return {"class": "inert-prime", "rational_prime": sn, "norm": n}
    return {"class": "composite"}


def generate_target_primes(norm_max: int) -> list:
    """Build CANONICAL representatives for each (rational_prime, class) pair.

    For each prime, we want a small (a, b) representation that gives a
    target_real in a reachable range (not microscopic associates from
    multiplication by phi^-n).  We try ALL small (a,b) reps and search
    for the icosian against ANY of them.
    """
    # First, find ALL prime (a, b) reps with small coefficients
    reps_by_key: dict = {}   # key -> list of (a, b, target_real)
    for a in range(-15, 16):
        for b in range(-15, 16):
            cls = classify_zphi(a, b)
            if cls.get("class") not in ("split-prime", "inert-prime", "ramified-prime"):
                continue
            if cls["norm"] > norm_max:
                continue
            target_real = a + b * PHI
            if target_real <= 0:
                continue
            key = (cls["rational_prime"], cls["class"])
            reps_by_key.setdefault(key, []).append((a, b, target_real))

    # For each prime, pick the rep with smallest |a| + |b|
    targets = []
    for key, reps in reps_by_key.items():
        reps.sort(key=lambda r: (abs(r[0]) + abs(r[1]), r[2]))
        a, b, target_real = reps[0]
        cls = classify_zphi(a, b)
        targets.append({
            "a": int(a), "b": int(b), "norm": cls["norm"],
            "class": cls["class"],
            "rational_prime": cls["rational_prime"],
            "target_real":   float(target_real),
            "all_reps":      [{"a": int(r[0]), "b": int(r[1]),
                               "target_real": float(r[2])}
                              for r in reps[:6]],
        })
    return sorted(targets, key=lambda t: (t["norm"], t["rational_prime"]))


def precompute_2vertex_norms(V: np.ndarray, coef_max: int = 5):
    """Returns dict {rounded_norm: example_alpha} for all 2-vertex sums."""
    n = V.shape[0]
    coefs = [c for c in range(-coef_max, coef_max + 1) if c != 0]
    n_coef = len(coefs)
    norms_map: dict[float, np.ndarray] = {}

    print(f"  Pre-computing 2-vertex norms, |coef| <= {coef_max} ...")
    # Single-vertex first (1v)
    for i in range(n):
        for m in coefs:
            alpha = m * V[i]
            qn = float(np.sum(alpha * alpha))
            key = round(qn, 5)
            if key not in norms_map:
                norms_map[key] = alpha
    # Two-vertex (i < j)
    coefs_arr = np.array(coefs, dtype=float)
    for i in range(n):
        # vectorize over j and (m, k)
        for j in range(i + 1, n):
            # build (n_coef, n_coef, 4) tensor of m*V[i] + k*V[j]
            mv = coefs_arr[:, None, None] * V[i][None, None, :]
            kv = coefs_arr[None, :, None] * V[j][None, None, :]
            alpha = mv + kv  # shape (n_coef, n_coef, 4)
            qn = np.sum(alpha * alpha, axis=2)  # (n_coef, n_coef)
            # Add to map
            for a in range(n_coef):
                for b in range(n_coef):
                    key = round(float(qn[a, b]), 5)
                    if key not in norms_map:
                        norms_map[key] = alpha[a, b].copy()
        if (i + 1) % 30 == 0:
            print(f"    progress: {i+1}/{n} vertices, {len(norms_map)} distinct norms so far")
    print(f"  2-vertex pre-computation done: {len(norms_map)} distinct norms")
    return norms_map


def precompute_3vertex_norms_for_targets(V: np.ndarray, targets: list,
                                          existing: dict,
                                          coef_max: int = 2,
                                          time_budget_s: float = 300.0):
    """For each target whose norm is NOT in `existing`, search 3-vertex sums
       within time budget. Returns updated map."""
    import time
    start = time.time()
    n = V.shape[0]
    coefs = [c for c in range(-coef_max, coef_max + 1) if c != 0]
    n_coef = len(coefs)
    coefs_arr = np.array(coefs, dtype=float)

    # Targets still missing
    missing_targets = []
    for t in targets:
        key = round(t["target_real"], 5)
        if key not in existing:
            missing_targets.append((key, t))
    if not missing_targets:
        print("  No targets missing; skipping 3-vertex search.")
        return existing
    missing_keys = {k for k, _ in missing_targets}
    print(f"  3-vertex search for {len(missing_targets)} missing targets "
          f"(coef <= {coef_max}, time budget {time_budget_s:.0f}s)...")

    found_in_3v = 0
    checked = 0
    for i in range(n):
        if time.time() - start > time_budget_s:
            print(f"    time budget exceeded after {i}/{n} outer iterations")
            break
        for j in range(i + 1, n):
            for h in range(j + 1, n):
                # build (n_coef, n_coef, n_coef, 4) tensor of m1*V[i] + m2*V[j] + m3*V[h]
                a1 = coefs_arr[:, None, None, None] * V[i][None, None, None, :]
                a2 = coefs_arr[None, :, None, None] * V[j][None, None, None, :]
                a3 = coefs_arr[None, None, :, None] * V[h][None, None, None, :]
                alpha = a1 + a2 + a3
                qn = np.sum(alpha * alpha, axis=3)
                checked += n_coef ** 3
                # Check if any norms match missing targets
                qn_keys = np.round(qn, 5).flatten()
                for idx, key in enumerate(qn_keys):
                    fkey = float(key)
                    if fkey in missing_keys and fkey not in existing:
                        # flat index -> (a, b, c)
                        a_idx = idx // (n_coef * n_coef)
                        b_idx = (idx // n_coef) % n_coef
                        c_idx = idx % n_coef
                        existing[fkey] = alpha[a_idx, b_idx, c_idx].copy()
                        found_in_3v += 1
                        if all(round(t["target_real"], 5) in existing for _, t in missing_targets):
                            print(f"    All missing targets hit after {i}/{n} outer iterations.")
                            return existing
            if time.time() - start > time_budget_s:
                break
    print(f"    3-vertex search: {found_in_3v} additional targets hit, "
          f"{checked} triples checked")
    return existing


def main(argv):
    NORM_MAX = int(argv[1]) if len(argv) > 1 else 200

    print("=" * 78)
    print(f"Extended icosian probe v2: every Z[phi]-prime <= norm {NORM_MAX}")
    print("=" * 78)
    print()

    V = build_v600()
    print(f"V_600: {V.shape[0]} unit icosians")

    targets = generate_target_primes(NORM_MAX)
    print(f"Z[phi]-prime targets (norm <= {NORM_MAX}): {len(targets)}")
    print()

    # Stage 1: 2-vertex sums with |coef| <= 5
    print("--- Stage 1: 2-vertex sums, |coef| <= 5 ---")
    norms_map = precompute_2vertex_norms(V, coef_max=5)
    print()

    # Stage 2: 3-vertex sums for missing targets, time-budgeted
    print("--- Stage 2: 3-vertex sums for missing targets, |coef| <= 2 ---")
    norms_map = precompute_3vertex_norms_for_targets(V, targets, norms_map,
                                                      coef_max=2,
                                                      time_budget_s=240.0)
    print()

    # Look up each target — check ALL associate representatives
    print("=" * 78)
    print("RESULTS")
    print("=" * 78)
    print(f"{'rk':<4} {'class':<16} {'p':<5} {'norm':<5} {'a':<4} {'b':<4} "
          f"{'hit':<5} {'rep used':<14} {'alpha example':<48}")
    print("-" * 112)
    results = []
    n_hit = 0
    by_class = defaultdict(lambda: {"total": 0, "hit": 0})
    for rk, t in enumerate(targets, 1):
        # Try the canonical rep first, then all stored associates
        alpha = None
        rep_used = None
        # Canonical
        key = round(t["target_real"], 5)
        alpha = norms_map.get(key)
        if alpha is not None:
            rep_used = f"({t['a']},{t['b']})"
        else:
            # Try other small associates
            for rep in t.get("all_reps", []):
                k2 = round(rep["target_real"], 5)
                alpha = norms_map.get(k2)
                if alpha is not None:
                    rep_used = f"({rep['a']},{rep['b']})"
                    break
        hit = alpha is not None
        if hit:
            n_hit += 1
            astr = f"({alpha[0]:+.3f}, {alpha[1]:+.3f}, {alpha[2]:+.3f}, {alpha[3]:+.3f})"
        else:
            astr = "---"
        by_class[t["class"]]["total"] += 1
        if hit:
            by_class[t["class"]]["hit"] += 1
        print(f"{rk:<4} {t['class']:<16} {t['rational_prime']:<5} "
              f"{t['norm']:<5} {t['a']:<4} {t['b']:<4} "
              f"{'YES' if hit else 'no':<5} {astr:<48}")
        results.append({
            "rank":           rk,
            "class":          t["class"],
            "rational_prime": t["rational_prime"],
            "norm":           t["norm"],
            "zphi_rep":       [t["a"], t["b"]],
            "target_real":    t["target_real"],
            "hit":            hit,
            "alpha":          [float(x) for x in alpha.tolist()] if hit else None,
        })

    print()
    print("=" * 78)
    print("SUMMARY")
    print("=" * 78)
    n_total = len(targets)
    print(f"  Total Z[phi]-prime targets: {n_total}")
    print(f"  Hit:                        {n_hit}/{n_total} ({100*n_hit/n_total:.1f}%)")
    print(f"  Missed:                     {n_total - n_hit}")
    print()
    print("  By class:")
    for cls in ("ramified-prime", "inert-prime", "split-prime"):
        d = by_class[cls]
        print(f"    {cls:<18}  {d['hit']}/{d['total']}  "
              f"({100*d['hit']/max(d['total'],1):.1f}%)")
    print()

    summary = {
        "norm_max":       int(NORM_MAX),
        "n_total":        int(n_total),
        "n_hit":          int(n_hit),
        "n_missed":       int(n_total - n_hit),
        "by_class":       {k: dict(v) for k, v in by_class.items()},
        "results":        results,
    }
    with open(OUTPUT_DIR / "probe_icosian_full_v2_results.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Saved {OUTPUT_DIR / 'probe_icosian_full_v2_results.json'}")
    return 0 if n_hit == n_total else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
