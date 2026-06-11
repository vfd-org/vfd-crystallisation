#!/usr/bin/env python3
"""
Extended icosian-norm probe: targeted search for every Z[phi]-prime
up to a chosen norm cutoff (default 200), to establish that the icosian
ring 𝓘 generates the L_4 prime classification cleanly.

Strategy:
  For each target Z[phi]-prime pi = a + b*phi with absolute Galois norm
  <= NORM_MAX, target real value T = a + b*phi.  Search V_600 vertex
  combinations
        alpha = m_1*v_{i_1} + ... + m_K*v_{i_K}
  for small integer coefficients and K in {1, 2, 3}.  Record the first
  alpha that satisfies ||alpha||^2 = T within tolerance.

If every target prime is hit, the norm form is empirically generative
in the tested range.  Becomes the headline sim for Paper A's
generation section.

Run:
    python probe_icosian_full_generation.py [NORM_MAX]
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
TOL    = 1e-6

OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def build_v600():
    half       = 0.5
    half_phi   = PHI / 2.0
    half_phi_i = 1.0 / (2.0 * PHI)
    verts = []
    for i in range(4):
        for s in (1.0, -1.0):
            v = [0.0]*4
            v[i] = s
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
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    r = int(math.isqrt(n))
    for d in range(3, r + 1, 2):
        if n % d == 0:
            return False
    return True


def zphi_norm(a: int, b: int) -> int:
    return a*a + a*b - b*b


def classify_zphi(a: int, b: int) -> dict:
    if a == 0 and b == 0:
        return {"class": "zero"}
    n = abs(zphi_norm(a, b))
    if n == 1:
        return {"class": "unit"}
    if is_prime_int(n):
        p = n
        if p == 5:
            return {"class": "ramified-prime", "rational_prime": p, "norm": p}
        if p % 5 in (1, 4):
            return {"class": "split-prime", "rational_prime": p, "norm": p}
        return {"class": "anomaly", "rational_prime": p, "norm": p}
    sn = int(math.isqrt(n))
    if sn*sn == n and is_prime_int(sn) and sn % 5 in (2, 3):
        return {"class": "inert-prime", "rational_prime": sn, "norm": n}
    return {"class": "composite", "norm": n}


def generate_target_primes(norm_max: int) -> list:
    """All Z[phi]-prime targets (split, inert, ramified) with norm <= norm_max."""
    targets = []
    seen = set()
    for a in range(-50, 51):
        for b in range(-50, 51):
            cls = classify_zphi(a, b)
            if cls.get("class") not in ("split-prime", "inert-prime", "ramified-prime"):
                continue
            if cls["norm"] > norm_max:
                continue
            key = (cls["rational_prime"], cls["class"])
            if key in seen:
                continue
            seen.add(key)
            targets.append({
                "a": a, "b": b, "norm": cls["norm"],
                "class": cls["class"],
                "rational_prime": cls["rational_prime"],
                "target_real":   float(a + b * PHI),
            })
    return sorted(targets, key=lambda t: (t["norm"], t["rational_prime"]))


def search_two_vertex(V, target: float, coef_max: int = 5, tol: float = 1e-5):
    """Try alpha = m*v_i + k*v_j with |m|, |k| <= coef_max."""
    n = V.shape[0]
    coefs = list(range(-coef_max, coef_max + 1))
    for i in range(n):
        for j in range(i, n):
            for m in coefs:
                if m == 0:
                    continue
                for k in coefs:
                    if i == j and k == 0:
                        continue
                    alpha = m * V[i] + (k * V[j] if i != j else 0)
                    if i == j:
                        alpha = m * V[i]  # Already handled
                        if k != 0:
                            continue   # skip — single-vertex case
                    else:
                        alpha = m * V[i] + k * V[j]
                    qn = float(np.sum(alpha * alpha))
                    if abs(qn - target) < tol:
                        coeffs = [(i, m)]
                        if i != j:
                            coeffs.append((j, k))
                        return alpha, coeffs
    return None, None


def search_two_vertex_v2(V, target: float, coef_max: int = 5, tol: float = 1e-5):
    """Cleaner version: alpha = m*v_i + k*v_j, scan all pairs/coefs."""
    n = V.shape[0]
    coefs = [c for c in range(-coef_max, coef_max + 1) if c != 0]
    # Single-vertex
    for i in range(n):
        for m in coefs:
            alpha = m * V[i]
            qn    = float(np.sum(alpha * alpha))
            if abs(qn - target) < tol:
                return alpha, [(i, m)]
    # Two-vertex
    for i in range(n):
        for j in range(i + 1, n):
            for m in coefs:
                for k in coefs:
                    alpha = m * V[i] + k * V[j]
                    qn    = float(np.sum(alpha * alpha))
                    if abs(qn - target) < tol:
                        return alpha, [(i, m), (j, k)]
    return None, None


def search_three_vertex(V, target: float, coef_max: int = 2, tol: float = 1e-5,
                        sample_size: int | None = None):
    """Try alpha = m1*v_i + m2*v_j + m3*v_h with small coefficients.

    For efficiency, restrict to a SAMPLE of triples if sample_size is set.
    """
    n = V.shape[0]
    coefs = [c for c in range(-coef_max, coef_max + 1) if c != 0]
    rng = np.random.default_rng(42)
    # Generate triples
    triples = []
    for i in range(n):
        for j in range(i + 1, n):
            for h in range(j + 1, n):
                triples.append((i, j, h))
    if sample_size is not None and sample_size < len(triples):
        idx = rng.choice(len(triples), size=sample_size, replace=False)
        triples = [triples[i] for i in idx]
    for (i, j, h) in triples:
        for m1 in coefs:
            for m2 in coefs:
                for m3 in coefs:
                    alpha = m1 * V[i] + m2 * V[j] + m3 * V[h]
                    qn    = float(np.sum(alpha * alpha))
                    if abs(qn - target) < tol:
                        return alpha, [(i, m1), (j, m2), (h, m3)]
    return None, None


def main(argv):
    NORM_MAX = int(argv[1]) if len(argv) > 1 else 200

    print("=" * 78)
    print("Extended icosian probe: every Z[phi]-prime <= norm", NORM_MAX)
    print("=" * 78)
    print()

    V = build_v600()
    print(f"V_600: {V.shape[0]} unit icosians")
    print()

    targets = generate_target_primes(NORM_MAX)
    print(f"Z[phi]-prime targets (norm <= {NORM_MAX}): {len(targets)}")
    print()

    results = []
    n_hit_2v_low  = 0
    n_hit_2v_high = 0
    n_hit_3v      = 0
    n_missed      = 0

    print(f"{'rank':<5} {'class':<16} {'p':<5} {'norm':<5} {'a':<4} {'b':<4} {'method':<12} {'alpha':<48}")
    print("-" * 110)

    for rank, t in enumerate(targets):
        target_real = t["target_real"]
        # Try 2-vertex with low coefficients first (fast)
        alpha, coeffs = search_two_vertex_v2(V, target_real, coef_max=3)
        method = "2v ±3"
        if alpha is None:
            alpha, coeffs = search_two_vertex_v2(V, target_real, coef_max=6)
            method = "2v ±6"
            if alpha is not None:
                n_hit_2v_high += 1
            else:
                # Try 3-vertex with coefficients ±2 (limit sample for speed)
                alpha, coeffs = search_three_vertex(V, target_real, coef_max=2,
                                                    sample_size=20000)
                method = "3v ±2 (s)"
                if alpha is not None:
                    n_hit_3v += 1
        else:
            n_hit_2v_low += 1

        if alpha is None:
            method = "MISS"
            n_missed += 1
            alpha_str = "---"
        else:
            alpha_str = f"({alpha[0]:+.3f}, {alpha[1]:+.3f}, {alpha[2]:+.3f}, {alpha[3]:+.3f})"

        print(f"{rank+1:<5} {t['class']:<16} {t['rational_prime']:<5} "
              f"{t['norm']:<5} {t['a']:<4} {t['b']:<4} {method:<12} {alpha_str:<48}")

        results.append({
            "rank":      rank + 1,
            "class":     t["class"],
            "rational_prime": t["rational_prime"],
            "norm":      t["norm"],
            "zphi_rep":  [t["a"], t["b"]],
            "target_real": target_real,
            "method":    method,
            "alpha":     [float(x) for x in alpha.tolist()] if alpha is not None else None,
            "coeffs":    coeffs,
            "hit":       alpha is not None,
        })

    print()
    print("=" * 78)
    print("SUMMARY")
    print("=" * 78)
    n_total = len(targets)
    n_hit   = n_hit_2v_low + n_hit_2v_high + n_hit_3v
    print(f"  Total Z[phi]-prime targets:   {n_total}")
    print(f"  Hit by 2v ±3 (easy):          {n_hit_2v_low}")
    print(f"  Hit by 2v ±6 (medium):        {n_hit_2v_high}")
    print(f"  Hit by 3v ±2 (sampled):       {n_hit_3v}")
    print(f"  Missed:                       {n_missed}")
    print(f"  Total hit:                    {n_hit}/{n_total} "
          f"({100*n_hit/n_total:.1f}%)")
    print()

    # By class
    by_class = defaultdict(lambda: {"total": 0, "hit": 0})
    for r in results:
        by_class[r["class"]]["total"] += 1
        if r["hit"]:
            by_class[r["class"]]["hit"] += 1
    print("By class:")
    for cls in ("ramified-prime", "inert-prime", "split-prime"):
        d = by_class[cls]
        print(f"  {cls:<18}  hit: {d['hit']}/{d['total']}  "
              f"({100*d['hit']/max(d['total'],1):.1f}%)")
    print()

    # Save
    summary = {
        "norm_max":          int(NORM_MAX),
        "n_total_targets":   int(n_total),
        "n_hit":             int(n_hit),
        "n_missed":          int(n_missed),
        "n_hit_2v_low":      int(n_hit_2v_low),
        "n_hit_2v_high":     int(n_hit_2v_high),
        "n_hit_3v":          int(n_hit_3v),
        "by_class":          {k: dict(v) for k, v in by_class.items()},
        "results":           results,
    }
    with open(OUTPUT_DIR / "probe_icosian_full_results.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Saved {OUTPUT_DIR / 'probe_icosian_full_results.json'}")

    return 0 if n_missed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
