"""Look-elsewhere effect: how surprising is the 1/12 hit really?

The 1/12 candidate landed at |z|=0.06 against SH0ES H0 AND |z|=0.14
against KiDS S8 — both with the SAME magnitude and physically-motivated
opposite signs.

This script answers: under a null in which I just throw natural-looking
ratios at the tensions, what fraction of candidates would land *both*
within the observed thresholds?

Method:
  1. Enumerate a much larger pool of candidate corrections from
     "natural" mathematical numbers — small integers, small rationals,
     simple combinations of (φ, π, e, integers) — without reference to
     the substrate.
  2. For each, compute the H0 and S8 residuals.
  3. Count how many fall inside |z_H0| < 0.1 AND |z_S8| < 0.2 simultaneously.
  4. Report the joint hit probability under this null.

Look-elsewhere is conservative: the candidate pool is much larger than
the actual cascade-derived shortlist, so the implied false-positive rate
is an upper bound.
"""
from __future__ import annotations

import itertools
import math
from typing import List, Tuple

PHI = (1 + math.sqrt(5)) / 2

# Measurements (same as h0 and sigma8 scripts)
PLANCK_H0, PLANCK_H0_S = 67.36, 0.54
SH0ES_H0,  SH0ES_H0_S  = 73.04, 1.04
PLANCK_S8, PLANCK_S8_S = 0.832, 0.013
KIDS_S8,   KIDS_S8_S   = 0.759, 0.024


def make_pool() -> List[Tuple[str, float]]:
    """Build a large pool of small-rational and constant-based ratios."""
    pool = []
    # Small rationals 1/n for n=2..30
    for n in range(2, 31):
        pool.append((f"1/{n}", 1.0 / n))
    # 2/n for n=3..30
    for n in range(3, 31):
        pool.append((f"2/{n}", 2.0 / n))
    # Squared inverses
    for n in range(2, 16):
        pool.append((f"1/{n}^2", 1.0 / (n * n)))
    # Powers of 1/φ
    for k in range(1, 12):
        pool.append((f"1/φ^{k}", 1.0 / PHI**k))
    # log(φ) / n
    for n in range(1, 16):
        pool.append((f"ln(φ)/{n}", math.log(PHI) / n))
    # 1/(nπ)
    for n in range(1, 16):
        pool.append((f"1/({n}π)", 1.0 / (n * math.pi)))
    # 1/(n·e)
    for n in range(1, 12):
        pool.append((f"1/({n}e)", 1.0 / (n * math.e)))
    # Sums of two small rationals
    for n in range(2, 12):
        for m in range(n, 12):
            pool.append((f"1/{n}+1/{m}", 1.0 / n + 1.0 / m))
    return pool


def z_h0(eps: float) -> float:
    pred = PLANCK_H0 * (1 + eps)
    sigma = math.hypot(PLANCK_H0_S * (1 + eps), SH0ES_H0_S)
    return abs(pred - SH0ES_H0) / sigma


def z_s8(eps: float) -> float:
    pred = PLANCK_S8 * (1 - eps)  # opposite sign of H0
    sigma = math.hypot(PLANCK_S8_S * (1 - eps), KIDS_S8_S)
    return abs(pred - KIDS_S8) / sigma


def main() -> None:
    pool = make_pool()
    print(f"candidate pool size: {len(pool)}")

    h0_thr = 0.10
    s8_thr = 0.20

    h0_hits, s8_hits, both_hits = [], [], []
    for name, eps in pool:
        zh, zs = z_h0(eps), z_s8(eps)
        if zh < h0_thr:
            h0_hits.append((name, eps, zh, zs))
        if zs < s8_thr:
            s8_hits.append((name, eps, zh, zs))
        if zh < h0_thr and zs < s8_thr:
            both_hits.append((name, eps, zh, zs))

    print(f"\nthresholds: |z_H0| < {h0_thr},  |z_S8| < {s8_thr}")
    print(f"  candidates passing H0 threshold:    {len(h0_hits):>3}/{len(pool)}  "
          f"({len(h0_hits)/len(pool):.3%})")
    print(f"  candidates passing S8 threshold:    {len(s8_hits):>3}/{len(pool)}  "
          f"({len(s8_hits)/len(pool):.3%})")
    print(f"  candidates passing BOTH:            {len(both_hits):>3}/{len(pool)}  "
          f"({len(both_hits)/len(pool):.3%})")

    print("\nH0-only hits:")
    for name, eps, zh, zs in sorted(h0_hits, key=lambda r: r[2]):
        print(f"  ε = {eps:.6f}  ({name:<14})  z_H0={zh:.3f}  z_S8={zs:.3f}")

    print("\nS8-only hits:")
    for name, eps, zh, zs in sorted(s8_hits, key=lambda r: r[3]):
        print(f"  ε = {eps:.6f}  ({name:<14})  z_H0={zh:.3f}  z_S8={zs:.3f}")

    print("\nJoint hits (H0 AND S8):")
    for name, eps, zh, zs in sorted(both_hits, key=lambda r: r[2] + r[3]):
        print(f"  ε = {eps:.6f}  ({name:<14})  z_H0={zh:.3f}  z_S8={zs:.3f}")

    # Random-ε null: what fraction of *uniform* ε in a plausible range pass both?
    import numpy as np
    rng = np.random.default_rng(0)
    n_random = 100_000
    eps_rand = rng.uniform(-0.3, 0.3, size=n_random)
    pred_h = PLANCK_H0 * (1 + eps_rand)
    sig_h = np.hypot(PLANCK_H0_S * (1 + eps_rand), SH0ES_H0_S)
    zh_r = np.abs(pred_h - SH0ES_H0) / sig_h
    pred_s = PLANCK_S8 * (1 - eps_rand)
    sig_s = np.hypot(PLANCK_S8_S * (1 - eps_rand), KIDS_S8_S)
    zs_r = np.abs(pred_s - KIDS_S8) / sig_s
    p_h = float(np.mean(zh_r < h0_thr))
    p_s = float(np.mean(zs_r < s8_thr))
    p_both = float(np.mean((zh_r < h0_thr) & (zs_r < s8_thr)))
    print(f"\nUniform-ε null (ε∈[−0.3,0.3], n={n_random}):")
    print(f"  P(|z_H0| < {h0_thr}):           {p_h:.4%}")
    print(f"  P(|z_S8| < {s8_thr}):           {p_s:.4%}")
    print(f"  P(both):                       {p_both:.4%}")
    print(f"  expected indep:                {p_h * p_s:.4%}  "
          f"({p_both/(p_h*p_s):.2f}× independent → near-1 means tensions are close to orthogonal)")


if __name__ == "__main__":
    main()
