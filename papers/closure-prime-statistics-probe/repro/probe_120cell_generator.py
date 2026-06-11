#!/usr/bin/env python3
"""
Exploratory probe: is the 120-cell {5,3,3} the geometric generator of
the cascade's pentagonal-clock z-hat?

The 120-cell is the Poincare dual of the 600-cell V_600.
  V_600 = {3,3,5}:  120 vertices, 720 edges, 1200 triangle faces, 600 cells
  120-cell = {5,3,3}:  600 vertices, 1200 edges, 720 pentagon faces, 120 cells

Hypothesis: the K-pole structure of z-hat(z) at K in {0, 20, 52, 72}
with multiplicities {1, 1, 5, 5} (summing to 12) emerges naturally from
the spectral / character structure of the 120-cell.

Things to compute and look for:
  1. Vertex count of 120-cell:  600  (sanity)
  2. Adjacency matrix at edge length, vertex degree
  3. Full Laplacian / adjacency spectrum (600 eigenvalues)
  4. Multiplicity distribution
  5. Specific look for {1, 1, 5, 5} pattern as a substructure
  6. Compare to V_600 spectrum (9 eigenvalues with multiplicities
     {4, 16, 9, 36, 25, 16, 9, 4, 1} summing to 120)
  7. Look for 5-fold structure (Schlafli decomposition into
     5 disjoint 24-cells, or pentagonal-face count 720)

Run:
    python probe_120cell_generator.py
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from collections import Counter
from itertools import combinations, permutations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

PHI       = (1.0 + 5.0 ** 0.5) / 2.0
INVPHI    = 1.0 / PHI                  # = phi - 1
PHI2      = PHI * PHI                  # = phi + 1
PHI_NEG2  = INVPHI * INVPHI            # = 2 - phi
SQRT5     = 5.0 ** 0.5

OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def even_permutations_4():
    """Return the 12 even permutations of (0, 1, 2, 3)."""
    out = []
    for p in permutations(range(4)):
        # Count inversions
        inv = 0
        for i in range(4):
            for j in range(i + 1, 4):
                if p[i] > p[j]:
                    inv += 1
        if inv % 2 == 0:
            out.append(p)
    return out


def build_120cell_vertices() -> np.ndarray:
    """Build the 600 vertices of the 120-cell at standard scale.

    Sources: Coxeter, Regular Polytopes; the 600-vertex set with
    circumradius 2*sqrt(2) consists of:

      Type 1: 24 perms of (0, 0, +/-2, +/-2)
      Type 2: 64 perms of (+/-1, +/-1, +/-1, +/-sqrt(5))
      Type 3: 64 perms of (+/-phi^2, +/-phi^-1, +/-phi^-1, +/-phi^-1)
              [phi^2 in one of 4 positions]
      Type 4: 64 perms of (+/-phi, +/-phi, +/-phi, +/-phi^-2)
              [phi^-2 in one of 4 positions]
      Type 5: 96 even perms of (0, +/-phi^-2, +/-1, +/-phi^2)
      Type 6: 96 even perms of (0, +/-phi^-1, +/-phi, +/-sqrt(5))
      Type 7: 192 even perms of (+/-phi^-1, +/-1, +/-phi, +/-2)

    Total: 24 + 64*3 + 96*2 + 192 = 24 + 192 + 192 + 192 = 600.
    """
    verts: list[list[float]] = []

    # --- Type 1: 24 of (0, 0, +/-2, +/-2)  -----------------------------
    for positions in combinations(range(4), 2):
        for s0 in (-1, 1):
            for s1 in (-1, 1):
                v = [0.0] * 4
                v[positions[0]] = 2.0 * s0
                v[positions[1]] = 2.0 * s1
                verts.append(v)
    # 6 * 4 = 24

    # --- Type 2: 64 of (+/-1, +/-1, +/-1, +/-sqrt5) --------------------
    for sqrt5_pos in range(4):
        for sm in range(16):
            s = [(-1 if (sm >> i) & 1 else 1) for i in range(4)]
            v = [s[i] * 1.0 for i in range(4)]
            v[sqrt5_pos] = s[sqrt5_pos] * SQRT5
            verts.append(v)
    # 4 * 16 = 64

    # --- Type 3: 64 of (+/-phi^2, +/-phi^-1, +/-phi^-1, +/-phi^-1) -----
    for phi2_pos in range(4):
        for sm in range(16):
            s = [(-1 if (sm >> i) & 1 else 1) for i in range(4)]
            v = [s[i] * INVPHI for i in range(4)]
            v[phi2_pos] = s[phi2_pos] * PHI2
            verts.append(v)

    # --- Type 4: 64 of (+/-phi, +/-phi, +/-phi, +/-phi^-2) -------------
    for phi_neg2_pos in range(4):
        for sm in range(16):
            s = [(-1 if (sm >> i) & 1 else 1) for i in range(4)]
            v = [s[i] * PHI for i in range(4)]
            v[phi_neg2_pos] = s[phi_neg2_pos] * PHI_NEG2
            verts.append(v)

    # --- Type 5: 96 even perms of (0, +/-phi^-2, +/-1, +/-phi^2) -------
    ep = even_permutations_4()
    for p in ep:
        for s0 in (-1, 1):
            for s1 in (-1, 1):
                for s2 in (-1, 1):
                    v = [0.0] * 4
                    v[p[0]] = 0.0
                    v[p[1]] = s0 * PHI_NEG2
                    v[p[2]] = s1 * 1.0
                    v[p[3]] = s2 * PHI2
                    verts.append(v)
    # 12 * 8 = 96

    # --- Type 6: 96 even perms of (0, +/-phi^-1, +/-phi, +/-sqrt5) -----
    for p in ep:
        for s0 in (-1, 1):
            for s1 in (-1, 1):
                for s2 in (-1, 1):
                    v = [0.0] * 4
                    v[p[0]] = 0.0
                    v[p[1]] = s0 * INVPHI
                    v[p[2]] = s1 * PHI
                    v[p[3]] = s2 * SQRT5
                    verts.append(v)

    # --- Type 7: 192 even perms of (+/-phi^-1, +/-1, +/-phi, +/-2) ----
    for p in ep:
        for sm in range(16):
            s = [(-1 if (sm >> i) & 1 else 1) for i in range(4)]
            v = [0.0] * 4
            v[p[0]] = s[0] * INVPHI
            v[p[1]] = s[1] * 1.0
            v[p[2]] = s[2] * PHI
            v[p[3]] = s[3] * 2.0
            verts.append(v)
    # 12 * 16 = 192

    V = np.array(verts, dtype=float)
    return V


def deduplicate(V: np.ndarray, tol: float = 1e-7) -> np.ndarray:
    """Round to tolerance, dedupe, return unique vertices."""
    rounded = np.round(V / tol).astype(np.int64)
    seen = set()
    out_idx = []
    for i, r in enumerate(rounded):
        key = tuple(r)
        if key not in seen:
            seen.add(key)
            out_idx.append(i)
    return V[out_idx]


def build_adjacency_at_nearest(V: np.ndarray, tol: float = 1e-5):
    """Compute pairwise distances, find the smallest, build adjacency."""
    n = V.shape[0]
    # Compute pairwise squared distances
    diffs = V[:, None, :] - V[None, :, :]
    d2 = np.sum(diffs * diffs, axis=2)
    pos = d2[d2 > 1e-9]
    min_d2 = pos.min()
    edge_length = float(min_d2 ** 0.5)
    A = (np.abs(d2 - min_d2) < tol).astype(float)
    np.fill_diagonal(A, 0.0)
    degrees = A.sum(axis=1).astype(int)
    return A, edge_length, degrees


def spectral_summary(A: np.ndarray, tol: float = 1e-5):
    eigvals = np.linalg.eigvalsh(A)
    distinct = []
    counts = []
    for ev in sorted(eigvals.tolist()):
        if distinct and abs(ev - distinct[-1]) < tol:
            counts[-1] += 1
        else:
            distinct.append(ev)
            counts.append(1)
    return distinct, counts


def look_for_pattern(distinct, mults, target_pattern=(1, 1, 5, 5)):
    """Check if the multiset of multiplicities contains the pattern."""
    mc = Counter(mults)
    tc = Counter(target_pattern)
    found = True
    for v, n in tc.items():
        if mc[v] < n:
            found = False
            break
    return found


def cosine_K_match(distinct, K_values=(0, 20, 52, 72), denom=120):
    """For each eigenvalue, see if it matches 2*cos(2*pi*K/denom) for
       some K in K_values."""
    matches = []
    for ev in distinct:
        for K in K_values:
            target = 2.0 * math.cos(2.0 * math.pi * K / denom)
            if abs(ev - target) < 1e-3:
                matches.append((float(ev), int(K), float(target),
                                float(abs(ev - target))))
    return matches


def main():
    print("=" * 78)
    print("Probe: is the 120-cell {5,3,3} the geometric generator of z-hat(z)?")
    print("=" * 78)
    print()

    # Build vertices
    print("--- Building 120-cell vertices ---")
    V_raw = build_120cell_vertices()
    print(f"  raw vertex count (with possible duplicates): {V_raw.shape[0]}")

    V = deduplicate(V_raw)
    print(f"  deduplicated vertex count: {V.shape[0]}")

    if V.shape[0] != 600:
        print(f"  WARNING: expected 600 vertices, got {V.shape[0]}")

    # Norms
    norms = np.linalg.norm(V, axis=1)
    print(f"  vertex norm: min = {norms.min():.6f}, max = {norms.max():.6f}, "
          f"all-equal = {norms.max() - norms.min() < 1e-6}")
    expected_norm = (2.0 * SQRT5)**0.5 * (2.0)  # circumradius 2*sqrt(2) -> norm
    # Actually circumradius = ||v|| for v a vertex if vertices on a sphere
    # Standard scaling: circumradius = 2*sqrt(2) ~ 2.828
    print(f"  expected circumradius for this scaling: 2*sqrt(2) = "
          f"{2.0 * 2.0**0.5:.6f}")
    print()

    # Adjacency
    print("--- Building adjacency matrix at nearest-neighbour distance ---")
    A, edge_len, degs = build_adjacency_at_nearest(V)
    print(f"  edge length: {edge_len:.6f}")
    # Expected: edge length for 120-cell at this scale should be 3 - sqrt(5)
    #           (= 2 / phi^2) or similar
    print(f"  reference: 3 - sqrt(5) = {3 - SQRT5:.6f}")
    print(f"  reference: 1/phi^2     = {1/PHI**2:.6f}")
    print(f"  reference: phi - 1     = {PHI - 1:.6f}")

    deg_counts = Counter(degs.tolist())
    print(f"  degree distribution: {dict(deg_counts)}")
    is_regular = (len(deg_counts) == 1)
    deg = list(deg_counts.keys())[0] if is_regular else None
    print(f"  regular: {is_regular}, common degree: {deg}")
    print(f"  reference: 120-cell vertex degree should be 4 "
          f"(each vertex has 4 nearest neighbours)")
    print()

    # Spectrum
    print("--- Computing adjacency spectrum (600 x 600 matrix) ---")
    distinct, mults = spectral_summary(A)
    print(f"  distinct eigenvalues: {len(distinct)}")
    print(f"  total multiplicity: {sum(mults)} (expected 600)")
    print()
    print(f"  {'eigenvalue':<14} {'multiplicity':<14} {'value/phi':<14}")
    print("  " + "-" * 42)
    for ev, m in zip(distinct, mults):
        print(f"  {ev:+10.6f}    {m:5d}          {ev/PHI:+8.4f} phi")
    print()

    # Multiplicity distribution
    mc = Counter(mults)
    print("--- Multiplicity histogram ---")
    for mult_value in sorted(mc.keys()):
        print(f"  multiplicity {mult_value:>4}: appears {mc[mult_value]} time(s)")
    print()

    # Look for {1, 1, 5, 5}
    pattern = (1, 1, 5, 5)
    print(f"--- Pattern search: does the spectrum contain {pattern}? ---")
    pattern_found = look_for_pattern(distinct, mults, pattern)
    print(f"  Pattern {pattern} found in multiplicity set: {pattern_found}")
    if pattern_found:
        # Identify which eigenvalues carry these multiplicities
        for ev, m in zip(distinct, mults):
            if m == 1 or m == 5:
                print(f"    eigenvalue {ev:+.6f} has multiplicity {m}")
    print()

    # K-cosine match
    print("--- Eigenvalue match to 2*cos(2*pi*K/120) for K in {0, 20, 52, 72} ---")
    for K in (0, 20, 52, 72):
        target = 2.0 * math.cos(2.0 * math.pi * K / 120.0)
        target_norm = target / 1.0
        print(f"  K = {K:>3}: 2*cos(2*pi*K/120) = {target:+.6f}")
    matches = cosine_K_match(distinct, K_values=(0, 20, 52, 72), denom=120)
    if matches:
        print(f"  Matches (eigenvalue near 2*cos(K)):")
        for ev, K, target, err in matches:
            print(f"    eigenvalue {ev:+.6f}  K = {K:>3}  target {target:+.6f}  "
                  f"err {err:.2e}")
    else:
        print("  No matches at tolerance 1e-3.")
    print()

    # Comparison to V_600 spectrum
    print("--- Comparison to V_600 (600-cell) spectrum ---")
    print("  V_600 spectrum (from Paper I sim):")
    v600_data = [
        (-3.7082, 4),  (-3.0000, 16), (-2.4721, 9),  (-2.0000, 36),
        ( 0.0000, 25), (+3.0000, 16), (+6.4721, 9),  (+9.7082, 4),
        (+12.0000, 1)
    ]
    for ev, m in v600_data:
        print(f"    {ev:+9.4f}  mult {m:3d}")
    print(f"  Total: 120 dimensions, 9 distinct eigenvalues, "
          f"multiplicity multiset = {sorted([m for _, m in v600_data])}")
    print()
    print("  120-cell multiplicity multiset (this probe):")
    print(f"    {sorted(mults)}")
    print()

    # Summary
    print("=" * 78)
    print("PROBE SUMMARY")
    print("=" * 78)
    summary = {
        "n_vertices":        int(V.shape[0]),
        "n_vertices_expected": 600,
        "vertex_count_ok":   V.shape[0] == 600,
        "edge_length":       float(edge_len),
        "regular":           bool(is_regular),
        "common_degree":     int(deg) if deg is not None else None,
        "degree_expected":   4,
        "degree_ok":         is_regular and deg == 4,
        "n_distinct_eigs":   int(len(distinct)),
        "total_dim":         int(sum(mults)),
        "distinct_eigs":     [float(e) for e in distinct],
        "multiplicities":    [int(m) for m in mults],
        "mult_multiset":     sorted(mults),
        "pattern_1155_found": bool(pattern_found),
        "K_cosine_matches":  [{"eig": float(e), "K": int(k),
                               "target": float(t), "err": float(er)}
                              for e, k, t, er in matches],
    }
    with open(OUTPUT_DIR / "probe_120cell_results.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(f"  Vertex count: {V.shape[0]} (expected 600) "
          f"{'PASS' if V.shape[0] == 600 else 'FAIL'}")
    print(f"  Regular degree: {deg} (expected 4) "
          f"{'PASS' if is_regular and deg == 4 else 'FAIL'}")
    print(f"  Distinct eigenvalues: {len(distinct)}")
    print(f"  Pattern {{1,1,5,5}} present in multiplicities: {pattern_found}")
    print(f"  K-cosine matches: {len(matches)}")
    print(f"  Total spectrum dim: {sum(mults)}")
    print()
    print(f"  Saved {OUTPUT_DIR / 'probe_120cell_results.json'}")

    # Spectrum figure
    fig, ax = plt.subplots(figsize=(11, 5))
    x = np.arange(len(distinct))
    ax.bar(x, mults, color="#cd3a3a", edgecolor="black", linewidth=0.5)
    ax.set_xticks(x)
    ax.set_xticklabels([f"{e:+.3f}" for e in distinct], rotation=60, ha="right", fontsize=8)
    ax.set_xlabel("adjacency eigenvalue")
    ax.set_ylabel("multiplicity")
    ax.set_title(f"120-cell {{5,3,3}} adjacency spectrum  "
                 f"({len(distinct)} distinct, total dim {sum(mults)})")
    ax.grid(alpha=0.3, axis="y")
    # Annotate 1,5 multiplicities specially
    for i, (ev, m) in enumerate(zip(distinct, mults)):
        if m in (1, 5):
            ax.text(i, m + max(mults) * 0.02, str(m), ha="center",
                    fontweight="bold", color="darkred", fontsize=9)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "probe_120cell_spectrum.png", dpi=120)
    plt.close()
    print(f"  Saved {OUTPUT_DIR / 'probe_120cell_spectrum.png'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
