#!/usr/bin/env python3
"""
Exploratory: does the spectral-dimension law of docs/rendering-layer.md §2
hold rung by rung across the cascade?

For each rung substrate, build the nearest-neighbour graph (vertices on the
unit sphere of its division algebra, edges at the canonical inner product),
compute Laplacian eigenvalue multiplicities, and test:

  (a) multiplicities = perfect squares of irrep dims (group rungs)
      / sphere-harmonic dims (loop rung),
  (b) low blocks = harmonic multiplicities of the rung's intrinsic sphere
      [ S^3: (k+1)^2 = 1, 4, 9, ... ;  S^7: 1, 8, 35, ... ],
  (c) harmonic cutoff k_max per rung (resolution ladder),
  (d) dispersion check lambda_k = deg * (1 - chi_k(theta)) where available,
  (e) Weyl slope d/2 from the harmonic blocks (>= 2 points).

Rungs tested:
  H4  rung: V_600  = 2I,  120 unit icosians,   S^3, edges at <v,w> = phi/2
  D4  rung: 24-cell = 2T,  24 Hurwitz units,    S^3, edges at <v,w> = 1/2
  16  rung: tesseract,     16 half-units,       S^3, edges at <v,w> = 1/2
  8/E8 rung: 240 unit octavians (E8 roots/sqrt2), S^7, edges at <v,w> = 1/2

Usage:
    python scripts/explore_rung_dimension_ladder.py
"""
from __future__ import annotations

import itertools
import numpy as np
from pathlib import Path

PHI = (1 + np.sqrt(5)) / 2
DATA_PATH = Path(__file__).resolve().parent / "600cell_data.npz"


def laplacian_blocks(verts, ip_edge, label):
    """Adjacency at inner product ip_edge; return (blocks, degree)."""
    G = verts @ verts.T
    A = (np.abs(G - ip_edge) < 1e-8).astype(float)
    np.fill_diagonal(A, 0.0)
    deg = A.sum(axis=1)
    assert np.allclose(deg, deg[0]), f"{label}: not regular"
    L = np.diag(deg) - A
    evals = np.round(np.linalg.eigvalsh(L), 6)
    blocks = [(float(l), int(np.sum(evals == l))) for l in sorted(set(evals))]
    return blocks, int(deg[0])


def s3_harmonic_dims(kmax):
    return [(k + 1) ** 2 for k in range(kmax + 1)]


def s7_harmonic_dims(kmax):
    # dim H_k(S^7) = (2k+6)(k+5)! / (k! 6!)
    out = []
    for k in range(kmax + 1):
        num = (2 * k + 6) * np.math.factorial(k + 5)
        out.append(int(num // (np.math.factorial(k) * 720)))
    return out


def find_harmonic_chain(blocks, dims):
    """Greedy: find dims[0], dims[1], ... as multiplicities in increasing-
    lambda order; return list of (dim, lambda) found."""
    found, idx = [], 0
    for d in dims:
        hit = None
        for j in range(idx, len(blocks)):
            if blocks[j][1] == d:
                hit = j
                break
        if hit is None:
            break
        found.append((d, blocks[hit][0]))
        idx = hit + 1
    return found


def weyl_slope(found):
    """Slope of log N(lambda) vs log lambda over the harmonic chain (k>=1)."""
    if len(found) < 3:
        return None
    lam = np.array([l for _, l in found][1:])
    N = np.cumsum([d for d, _ in found])[1:]
    return float(np.polyfit(np.log(lam), np.log(N.astype(float)), 1)[0])


def report(label, sphere, blocks, deg, dims, theta=None):
    print(f"\n--- {label}  (degree {deg}, arena {sphere}) ---")
    print("  spectrum: " + ", ".join(f"{l:.4f}:{m}" for l, m in blocks))
    mults = [m for _, m in blocks]
    found = find_harmonic_chain(blocks, dims)
    kmax = len(found) - 1
    print(f"  harmonic chain {sphere}: "
          + ", ".join(f"k={k} dim {d} @ lam {l:.4f}" for k, (d, l) in enumerate(found))
          + f"   -> cutoff k_max = {kmax}")
    used = sum(d for d, _ in found)
    print(f"  resolved fraction: {used}/{sum(mults)}  "
          f"(folded remainder {sum(mults) - used})")
    if theta is not None and len(found) > 1:
        # SU(2) character dispersion: lam_k = deg(1 - sin((k+1)theta)/((k+1)sin theta))
        pred = [deg * (1 - np.sin((k + 1) * theta) / ((k + 1) * np.sin(theta)))
                for k in range(len(found))]
        obs = [l for _, l in found]
        ok = np.allclose(pred, obs, atol=1e-6)
        print(f"  dispersion lam_k = {deg}[1 - sin((k+1)theta)/((k+1)sin theta)], "
              f"theta = {theta/np.pi:.3f}*pi: {'EXACT' if ok else 'MISMATCH'}"
              f"  predicted {np.round(pred, 4)}")
    s = weyl_slope(found)
    if s is not None:
        print(f"  Weyl slope d/2 = {s:.3f}  ->  spectral dimension d = {2*s:.2f}")
    else:
        print(f"  Weyl slope: needs >= 3 harmonic blocks (cutoff too low)")
    return kmax


def main():
    print("=" * 72)
    print("RUNG DIMENSION LADDER (exploratory)")
    print("=" * 72)

    # H4 rung: load canonical V_600
    data = np.load(DATA_PATH)
    v600 = data["vertices"]
    blocks, deg = laplacian_blocks(v600, PHI / 2, "V_600")
    report("H4 rung: V_600 (2I, unit icosians)", "S^3", blocks, deg,
           s3_harmonic_dims(8), theta=np.pi / 5)

    # D4 rung: 24-cell = Hurwitz units
    hurwitz = []
    for i in range(4):
        for s in (1.0, -1.0):
            v = np.zeros(4); v[i] = s
            hurwitz.append(v)
    for signs in itertools.product((0.5, -0.5), repeat=4):
        hurwitz.append(np.array(signs))
    hurwitz = np.array(hurwitz)
    assert len(hurwitz) == 24
    blocks, deg = laplacian_blocks(hurwitz, 0.5, "24-cell")
    report("D4 rung: 24-cell (2T, Hurwitz units)", "S^3", blocks, deg,
           s3_harmonic_dims(6), theta=np.pi / 3)

    # 16 rung: tesseract (half-integer units)
    tess = np.array([np.array(s) for s in itertools.product((0.5, -0.5), repeat=4)])
    blocks, deg = laplacian_blocks(tess, 0.5, "tesseract")
    report("16 rung: tesseract (Cl(1,3)-even)", "S^3", blocks, deg,
           s3_harmonic_dims(4), theta=np.pi / 3)

    # 8 / E8 rung: 240 unit octavians (E8 roots / sqrt 2) on S^7
    roots = []
    for i, j in itertools.combinations(range(8), 2):
        for si, sj in itertools.product((1.0, -1.0), repeat=2):
            v = np.zeros(8); v[i] = si; v[j] = sj
            roots.append(v)
    for signs in itertools.product((0.5, -0.5), repeat=8):
        if sum(1 for s in signs if s < 0) % 2 == 0:
            roots.append(np.array(signs))
    roots = np.array(roots) / np.sqrt(2)
    assert len(roots) == 240, len(roots)
    blocks, deg = laplacian_blocks(roots, 0.5, "E8 roots")
    report("8/E8 rung: 240 unit octavians (E8 roots)", "S^7", blocks, deg,
           s7_harmonic_dims(4))

    print("\n" + "=" * 72)
    print("Ladder summary: cutoff k_max per rung above; same-arena rungs are")
    print("resolution levels of one S^3; the octonionic rung changes arena to S^7.")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
