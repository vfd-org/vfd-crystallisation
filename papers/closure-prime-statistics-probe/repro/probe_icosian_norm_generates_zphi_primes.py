#!/usr/bin/env python3
"""
Empirical anchor for the generative-triad reorganisation:

Does the reduced norm form on the icosian ring 𝓘 generate the Z[phi]-primes?

The 120 unit icosians (= V_600 vertices) have norm 1.  Non-unit icosians
formed by integer combinations of unit icosians have norms in Z[phi].
Standard theory (Conway-Sloane, ch. 8): the norms of irreducible
icosians are exactly the Z[phi]-primes.

This probe:
  1. Enumerates icosian elements by small integer combinations of
     V_600 vertices.
  2. Computes their reduced norms (sums of 4 squares).
  3. Matches each norm to an element (a + b*phi) of Z[phi].
  4. Classifies that element as Z[phi]-prime via Dedekind:
       a + b*phi is prime iff |a^2 + ab - b^2| is either
         (a) a rational prime p with p mod 5 in {1, 4}  -> split prime above p
         (b) a rational prime p with p mod 5 in {2, 3}  -> needs check
                                                          (actually norm should be p^2 for inert)
         (c) = 5                                         -> ramified
  5. Reports which Z[phi]-primes (up to a chosen norm bound) are HIT
     and which are MISSED.

If every small Z[phi]-prime is hit, the norm form is generative.
If primes are missed systematically, the construction needs adjustment.

Run:
    python probe_icosian_norm_generates_zphi_primes.py [N_max]
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from itertools import combinations
from collections import defaultdict

import numpy as np

PHI    = (1.0 + 5.0 ** 0.5) / 2.0
INVPHI = 1.0 / PHI
TOL    = 1e-7

OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def build_v600():
    half       = 0.5
    half_phi   = PHI / 2.0
    half_phi_i = 1.0 / (2.0 * PHI)
    verts = []
    # Type A: 8
    for i in range(4):
        for s in (1.0, -1.0):
            v = [0.0]*4
            v[i] = s
            verts.append(v)
    # Type B: 16
    for s0 in (-1,1):
        for s1 in (-1,1):
            for s2 in (-1,1):
                for s3 in (-1,1):
                    verts.append([s0*half, s1*half, s2*half, s3*half])
    # Type C: 96
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


# ---------- Z[phi] arithmetic helpers ---------------------------------

def find_zphi(x: float, max_b: int = 40) -> tuple | None:
    """Find integers (a, b) such that a + b*phi ~ x.  Returns None if no
       small representation exists within tolerance.
    """
    best = None
    best_err = float('inf')
    for b in range(-max_b, max_b + 1):
        a_real = x - b * PHI
        a = int(round(a_real))
        err = abs(a + b*PHI - x)
        if err < best_err:
            best_err = err
            best = (a, b)
    if best_err < 1e-5:
        return best
    return None


def zphi_norm(a: int, b: int) -> int:
    """Absolute Galois norm of (a + b*phi): N = a^2 + a*b - b^2."""
    return a*a + a*b - b*b


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


def classify_zphi(a: int, b: int) -> dict:
    """Classify a + b*phi as Z[phi]-element:
       - 'zero', 'unit', 'split-prime' (above split p),
       - 'inert-component' (factor of inert p^2),
       - 'ramified-prime' (above 5), 'composite', etc.
    """
    if a == 0 and b == 0:
        return {"class": "zero"}
    n = zphi_norm(a, b)
    abs_n = abs(n)
    if abs_n == 1:
        return {"class": "unit", "norm": int(abs_n)}

    # If |N| is a rational prime p:
    if is_prime_int(abs_n):
        p = abs_n
        if p == 5:
            return {"class": "ramified-prime", "rational_prime": int(p),
                    "norm": int(abs_n)}
        if p % 5 in (1, 4):
            return {"class": "split-prime", "rational_prime": int(p),
                    "norm": int(abs_n)}
        if p % 5 in (2, 3):
            # This shouldn't happen — an inert prime p has Z[phi]-prime of norm p^2,
            # not p.  If we see this, our element is associate to a unit times an
            # inert prime's factor (which doesn't exist), so this is weird.
            return {"class": "anomaly-prime-norm-inert-residue",
                    "rational_prime": int(p), "norm": int(abs_n)}

    # If |N| = p^2 for some inert prime p (p mod 5 in {2,3}):
    sqrt_n = int(math.isqrt(abs_n))
    if sqrt_n * sqrt_n == abs_n and is_prime_int(sqrt_n) and sqrt_n % 5 in (2, 3):
        return {"class": "inert-prime", "rational_prime": int(sqrt_n),
                "norm": int(abs_n)}

    # Otherwise composite
    return {"class": "composite", "norm": int(abs_n)}


# ---------- Probe main ------------------------------------------------

def main(argv):
    print("=" * 78)
    print("Probe: does the icosian norm form generate Z[phi]-primes?")
    print("=" * 78)
    print()

    V = build_v600()
    n = V.shape[0]
    print(f"V_600 built: {n} unit icosians (= V_600 vertices)")
    print()

    # ENUMERATION STRATEGY:
    # Take icosian elements alpha = m*v_i + k*v_j for v_i, v_j in V_600
    # and m, k in {-3, ..., 3}.  Compute reduced norm (= sum of squares).
    # Match to Z[phi] element.  Classify.
    #
    # For each Z[phi]-prime hit, record which (v_i, v_j, m, k) achieved it.

    coeffs = list(range(-3, 4))   # {-3, -2, -1, 0, 1, 2, 3}

    # Z[phi]-primes we are TRYING to hit (the L_4 primes of Paper II up to
    # norm 1000).  Compute the target list.
    target_norms = set()
    target_zphi_primes = []   # list of dicts {a, b, class, rational_prime, norm}
    # Generate Z[phi]-elements (a, b) with small |a|, |b| and check primality
    for a in range(-20, 21):
        for b in range(-20, 21):
            cls = classify_zphi(a, b)
            if cls.get("class") in ("split-prime", "inert-prime", "ramified-prime"):
                if cls["norm"] <= 1000:
                    key = (cls.get("rational_prime"), cls["class"], cls["norm"])
                    # We want to track unique (rational_prime, class) targets
                    target_zphi_primes.append({
                        "a": int(a), "b": int(b),
                        "class": cls["class"],
                        "rational_prime": cls.get("rational_prime"),
                        "norm": cls["norm"],
                    })
                    target_norms.add(cls["norm"])

    # Deduplicate target primes by (rational_prime, class)
    target_by_rp = {}
    for tp in target_zphi_primes:
        key = (tp["rational_prime"], tp["class"])
        if key not in target_by_rp:
            target_by_rp[key] = tp
    print(f"Target Z[phi]-primes (split / inert / ramified) with norm <= 1000: "
          f"{len(target_by_rp)} unique (rational_prime, class) pairs")
    print(f"  Norms in target set: {sorted(target_norms)[:15]} ..."
          f"  (total: {len(target_norms)})")
    print()

    # ENUMERATE icosian sums
    # alpha = m*v_i + k*v_j
    print(f"Enumerating icosians alpha = m*v_i + k*v_j with m,k in {coeffs}, "
          f"v_i,v_j in V_600...")
    hits = defaultdict(list)
    examined = 0
    matched_zphi = 0
    failed_zphi = 0

    # To avoid double-counting and stay within a manageable enumeration,
    # we'll iterate over pairs (i, j) with i <= j and over m, k.
    # For i == j, alpha = (m+k)*v_i, so we only need m+k variation.
    for i in range(n):
        # Single-vertex multiples (m*v_i)
        for m in coeffs:
            if m == 0:
                continue
            alpha = m * V[i]
            qnorm = float(np.sum(alpha * alpha))
            examined += 1
            rep = find_zphi(qnorm)
            if rep is None:
                failed_zphi += 1
                continue
            matched_zphi += 1
            a, b = rep
            cls = classify_zphi(a, b)
            if cls.get("class") in ("split-prime", "inert-prime", "ramified-prime"):
                key = (cls.get("rational_prime"), cls["class"])
                hits[key].append({
                    "alpha": [float(x) for x in alpha.tolist()],
                    "qnorm": float(qnorm),
                    "zphi_rep": [int(a), int(b)],
                    "from": f"{m}*v[{i}]",
                })
        # Two-vertex sums (m*v_i + k*v_j)
        for j in range(i + 1, n):
            for m in coeffs:
                for k in coeffs:
                    if m == 0 and k == 0:
                        continue
                    alpha = m * V[i] + k * V[j]
                    qnorm = float(np.sum(alpha * alpha))
                    examined += 1
                    rep = find_zphi(qnorm)
                    if rep is None:
                        failed_zphi += 1
                        continue
                    matched_zphi += 1
                    a, b = rep
                    cls = classify_zphi(a, b)
                    if cls.get("class") in ("split-prime", "inert-prime",
                                            "ramified-prime"):
                        key = (cls.get("rational_prime"), cls["class"])
                        # Keep one example per key
                        if len(hits[key]) < 2:
                            hits[key].append({
                                "alpha": [float(x) for x in alpha.tolist()],
                                "qnorm": float(qnorm),
                                "zphi_rep": [int(a), int(b)],
                                "from": f"{m}*v[{i}] + {k}*v[{j}]",
                            })

    print(f"  examined: {examined} icosian elements")
    print(f"  matched to Z[phi]: {matched_zphi}  ({100*matched_zphi/max(examined,1):.1f}%)")
    print(f"  failed Z[phi] match: {failed_zphi}")
    print()

    # Compare HITS to TARGETS
    print("=" * 78)
    print("RESULTS: Z[phi]-primes hit by icosian norm form")
    print("=" * 78)
    target_keys = set(target_by_rp.keys())
    hit_keys = set(hits.keys())
    matched_keys = target_keys & hit_keys
    missed_keys = target_keys - hit_keys
    extra_keys  = hit_keys - target_keys

    print(f"Target Z[phi]-primes: {len(target_keys)}")
    print(f"Hit by icosian norm:  {len(matched_keys)}")
    print(f"Missed:               {len(missed_keys)}")
    print(f"Extra (hit but not in target list): {len(extra_keys)}")
    print()

    # Report by class
    for class_label in ("ramified-prime", "split-prime", "inert-prime"):
        targets_class = {k for k in target_keys if k[1] == class_label}
        hits_class    = {k for k in hit_keys    if k[1] == class_label}
        m = targets_class & hits_class
        miss = targets_class - hits_class
        print(f"--- {class_label} ---")
        print(f"  targets: {len(targets_class)}, hit: {len(m)}, missed: {len(miss)}")
        if miss:
            print(f"  MISSED rational primes (showing up to 10): "
                  f"{sorted([k[0] for k in miss])[:10]}")
        if m:
            sample = sorted(m, key=lambda k: k[0])[:8]
            print(f"  HIT examples (first 8 by rational prime):")
            for key in sample:
                rp, cls = key
                example = hits[key][0]
                a, b = example["zphi_rep"]
                print(f"    p = {rp:>4}  norm={zphi_norm(a,b):>5}  "
                      f"alpha = ({example['alpha'][0]:+.3f}, "
                      f"{example['alpha'][1]:+.3f}, "
                      f"{example['alpha'][2]:+.3f}, "
                      f"{example['alpha'][3]:+.3f})  "
                      f"N_quat={example['qnorm']:.3f}  "
                      f"Z[phi]={a}{'+' if b>=0 else ''}{b}*phi")
        print()

    # Save
    results = {
        "n_icosians_examined": int(examined),
        "matched_to_zphi":     int(matched_zphi),
        "failed_zphi":         int(failed_zphi),
        "n_target_primes":     int(len(target_keys)),
        "n_hit":               int(len(matched_keys)),
        "n_missed":            int(len(missed_keys)),
        "missed_examples":     [{"rational_prime": int(k[0]), "class": k[1]}
                                for k in sorted(missed_keys, key=lambda x:x[0])[:20]],
        "hit_by_class": {
            cls: int(len({k for k in hit_keys if k[1] == cls}))
            for cls in ("ramified-prime", "split-prime", "inert-prime")
        },
        "target_by_class": {
            cls: int(len({k for k in target_keys if k[1] == cls}))
            for cls in ("ramified-prime", "split-prime", "inert-prime")
        },
    }
    with open(OUTPUT_DIR / "probe_icosian_norm_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print()
    print(f"Saved {OUTPUT_DIR / 'probe_icosian_norm_results.json'}")

    # Verdict
    print()
    print("=" * 78)
    print("VERDICT")
    print("=" * 78)
    if len(missed_keys) == 0:
        print("ALL target Z[phi]-primes hit by icosian norm form.")
        print("Triad is generative: the norm map N: I -> Z[phi] reaches every")
        print("Z[phi]-prime in the tested range.")
    else:
        # Even partial hit is informative
        print(f"PARTIAL: {len(matched_keys)}/{len(target_keys)} target Z[phi]-primes hit.")
        print(f"Missing primes suggest either (a) larger coefficient range needed,")
        print(f"(b) construction needs the full icosian basis (not just V_600 sums),")
        print(f"or (c) some structural obstruction at these primes.")
    print()

    return 0 if len(missed_keys) == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
