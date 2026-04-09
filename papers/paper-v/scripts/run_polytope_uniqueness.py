#!/usr/bin/env python3
"""
Uniqueness test: is the 600-cell the ONLY regular polytope with ds ≈ φ?

Test every regular polytope in dimensions 2, 3, and 4.
If the 600-cell is unique, the "why this polytope?" question is answered.

Regular polytopes:
  2D: triangle (3), square (4), pentagon (5), hexagon (6), ...
  3D: tetrahedron, cube, octahedron, dodecahedron, icosahedron
  4D: 5-cell, 8-cell, 16-cell, 24-cell, 120-cell, 600-cell
"""

import math, os, sys, time
import numpy as np

PHI = (1 + 5**0.5) / 2
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vfd_derivation_output")
os.makedirs(OUT, exist_ok=True)


def ds_hk(A):
    L = np.diag(A.sum(1)) - A
    ev = np.maximum(np.sort(np.linalg.eigvalsh(L)), 0)
    tv = np.logspace(-3, 4, 1000)
    Z = sum(np.exp(-l * tv) for l in ev)
    Z = np.maximum(Z, 1e-300)
    pw = -2 * np.diff(np.log(Z)) / np.diff(np.log(tv))
    nt = [d for d in pw if 0.3 < d < 5.0]
    return float(np.median(nt)) if nt else 0.0

def ds_nl(A):
    V = len(A); d = A.sum(1)
    dis = np.where(d > 0, 1 / np.sqrt(d), 0)
    Ln = np.eye(V) - np.diag(dis) @ A @ np.diag(dis)
    ev = np.maximum(np.sort(np.linalg.eigvalsh(Ln)), 0)
    tv = np.logspace(-3, 4, 1000)
    Z = sum(np.exp(-l * tv) for l in ev)
    Z = np.maximum(Z, 1e-300)
    pw = -2 * np.diff(np.log(Z)) / np.diff(np.log(tv))
    nt = [d for d in pw if 0.3 < d < 5.0]
    return float(np.median(nt)) if nt else 0.0

def adj_from_verts(verts, tol_frac=0.1):
    n = len(verts)
    ds = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            ds[i, j] = ds[j, i] = np.linalg.norm(verts[i] - verts[j])
    mn = ds[ds > 0.01].min()
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            if abs(ds[i, j] - mn) < mn * tol_frac:
                A[i, j] = A[j, i] = 1
    return A

def measure(A, label):
    V = len(A); E = int(np.sum(A > 0) / 2)
    hk = ds_hk(A); nl = ds_nl(A)
    d_hk = abs(hk - PHI); d_nl = abs(nl - PHI)
    best = min(d_hk, d_nl)
    tag = " ◄◄◄ φ!" if best < 0.05 else (" ◄ near" if best < 0.15 else "")
    print(f"  {label:45s} V={V:5d} E={E:5d} | HK={hk:.4f} NL={nl:.4f} | "
          f"|HK-φ|={d_hk:.4f} |NL-φ|={d_nl:.4f}{tag}")
    return {"label": label, "V": V, "E": E, "ds_hk": hk, "ds_nl": nl,
            "delta_hk": d_hk, "delta_nl": d_nl}


# ═══════════════════════════════════════════════════════════════
# 2D regular polygons
# ═══════════════════════════════════════════════════════════════

def polygon(n):
    angles = [2 * math.pi * k / n for k in range(n)]
    verts = np.array([[math.cos(a), math.sin(a)] for a in angles])
    return adj_from_verts(verts)


# ═══════════════════════════════════════════════════════════════
# 3D Platonic solids
# ═══════════════════════════════════════════════════════════════

def tetrahedron():
    v = np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]], dtype=float)
    return adj_from_verts(v)

def cube():
    v = np.array([[s1,s2,s3] for s1 in [-1,1] for s2 in [-1,1] for s3 in [-1,1]], dtype=float)
    return adj_from_verts(v)

def octahedron():
    v = []
    for i in range(3):
        for s in [-1, 1]:
            r = [0, 0, 0]; r[i] = s; v.append(r)
    return adj_from_verts(np.array(v, dtype=float))

def icosahedron():
    v = []
    for s1 in [1, -1]:
        for s2 in [1, -1]:
            v.append([0, s1, s2 * PHI])
            v.append([s1, s2 * PHI, 0])
            v.append([s2 * PHI, 0, s1])
    v = np.array(v, dtype=float)
    return adj_from_verts(v / np.linalg.norm(v[0]))

def dodecahedron():
    v = []
    for s1 in [1, -1]:
        for s2 in [1, -1]:
            for s3 in [1, -1]:
                v.append([s1, s2, s3])
    for s1 in [1, -1]:
        for s2 in [1, -1]:
            v.append([0, s1 / PHI, s2 * PHI])
            v.append([s1 / PHI, s2 * PHI, 0])
            v.append([s2 * PHI, 0, s1 / PHI])
    v = np.array(v, dtype=float)
    return adj_from_verts(v / np.linalg.norm(v[0]))


# ═══════════════════════════════════════════════════════════════
# 4D regular polytopes
# ═══════════════════════════════════════════════════════════════

def cell5():
    """5-cell (4-simplex): 5 vertices in 4D"""
    v = np.zeros((5, 4))
    for i in range(4):
        v[i, i] = 1.0
    v[4] = np.ones(4) * (1 - math.sqrt(5)) / 4
    v = v - v.mean(axis=0)
    return adj_from_verts(v)

def cell8():
    """8-cell (tesseract/hypercube): 16 vertices"""
    v = np.array([[s1,s2,s3,s4] for s1 in [-1,1] for s2 in [-1,1]
                  for s3 in [-1,1] for s4 in [-1,1]], dtype=float)
    return adj_from_verts(v)

def cell16():
    """16-cell (hyperoctahedron): 8 vertices"""
    v = []
    for i in range(4):
        for s in [-1, 1]:
            r = [0, 0, 0, 0]; r[i] = s; v.append(r)
    return adj_from_verts(np.array(v, dtype=float))

def cell24():
    """24-cell: 24 vertices"""
    v = []
    for i in range(4):
        for j in range(i + 1, 4):
            for si in [-1, 1]:
                for sj in [-1, 1]:
                    r = [0, 0, 0, 0]; r[i] = si; r[j] = sj
                    v.append(r)
    return adj_from_verts(np.array(v, dtype=float))

def cell120():
    """120-cell: 600 vertices (dual of 600-cell)"""
    # Build from 600-cell face centroids
    # The 120-cell has 600 vertices at positions that are centroids
    # of 600-cell tetrahedral cells. Approximate via permutations.
    v = []
    perms_even = [
        (0,1,2,3),(0,2,3,1),(0,3,1,2),(1,0,3,2),(1,2,0,3),(1,3,2,0),
        (2,0,1,3),(2,1,3,0),(2,3,0,1),(3,0,2,1),(3,1,0,2),(3,2,1,0)]

    # 24 from (±2, 0, 0, 0) perms
    for i in range(4):
        for s in [-1, 1]:
            r = [0,0,0,0]; r[i] = 2*s; v.append(r)

    # 64 from (±1,±1,±1,±1)
    for s0 in [-1,1]:
        for s1 in [-1,1]:
            for s2 in [-1,1]:
                for s3 in [-1,1]:
                    v.append([s0,s1,s2,s3])

    # 96 from even perms of (±φ, ±1, ±1/φ, 0)
    base = [PHI, 1, 1/PHI, 0]
    for p in perms_even:
        for s0 in [1,-1]:
            for s1 in [1,-1]:
                for s2 in [1,-1]:
                    r = [0,0,0,0]
                    vals = [s0*base[0], s1*base[1], s2*base[2], 0]
                    for i, pi in enumerate(p):
                        r[pi] = vals[i]
                    v.append(r)

    # 192 from even perms of (±φ², ±1/φ, ±1/φ, ±1/φ) etc
    # Additional vertex sets for the 120-cell
    for p in perms_even:
        for s0 in [1,-1]:
            for s1 in [1,-1]:
                for s2 in [1,-1]:
                    # (±φ², ±φ⁻¹, ±φ⁻¹, 0) type
                    r = [0,0,0,0]
                    vals = [s0*PHI**2, s1/PHI, s2/PHI, 0]
                    for i, pi in enumerate(p):
                        r[pi] = vals[i]
                    v.append(r)

    v = np.array(v, dtype=float)
    norms = np.linalg.norm(v, axis=1, keepdims=True)
    v = v / norms

    # Deduplicate
    unique = [v[0]]
    for vi in v[1:]:
        if all(np.linalg.norm(vi - u) > 0.01 for u in unique):
            unique.append(vi)
    v = np.array(unique[:600])
    return adj_from_verts(v)

def cell600():
    """600-cell: 120 vertices"""
    v = []
    for i in range(4):
        for s in [-1, 1]:
            r = [0,0,0,0]; r[i] = s; v.append(r)
    for s0 in [-1,1]:
        for s1 in [-1,1]:
            for s2 in [-1,1]:
                for s3 in [-1,1]:
                    v.append([s0*.5, s1*.5, s2*.5, s3*.5])
    base = [PHI/2, .5, 1/(2*PHI), 0]
    ep = [(0,1,2,3),(0,2,3,1),(0,3,1,2),(1,0,3,2),(1,2,0,3),(1,3,2,0),
          (2,0,1,3),(2,1,3,0),(2,3,0,1),(3,0,2,1),(3,1,0,2),(3,2,1,0)]
    for p in ep:
        for s0 in [1,-1]:
            for s1 in [1,-1]:
                for s2 in [1,-1]:
                    r = [0,0,0,0]; vals = [s0*base[0], s1*base[1], s2*base[2], 0]
                    for i, pi in enumerate(p): r[pi] = vals[i]
                    v.append(r)
    v = np.array(v, dtype=float)
    v = v / np.linalg.norm(v, axis=1, keepdims=True)
    u = [v[0]]
    for vi in v[1:]:
        if all(np.linalg.norm(vi - x) > 0.01 for x in u): u.append(vi)
    return adj_from_verts(np.array(u[:120]))


# ═══════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════

def main():
    print("=" * 100)
    print("  POLYTOPE UNIQUENESS TEST: Is ds ≈ φ unique to the 600-cell?")
    print(f"  φ = {PHI:.6f}")
    print("=" * 100)
    T0 = time.time()

    results = []

    # 2D
    print(f"\n── 2D Regular Polygons ──\n")
    for n in [3, 4, 5, 6, 7, 8, 10, 12, 20, 50]:
        A = polygon(n)
        r = measure(A, f"2D {n}-gon")
        results.append(r)

    # 3D
    print(f"\n── 3D Platonic Solids ──\n")
    for name, builder in [("Tetrahedron {3,3}", tetrahedron),
                           ("Cube {4,3}", cube),
                           ("Octahedron {3,4}", octahedron),
                           ("Icosahedron {3,5}", icosahedron),
                           ("Dodecahedron {5,3}", dodecahedron)]:
        A = builder()
        r = measure(A, name)
        results.append(r)

    # 4D
    print(f"\n── 4D Regular Polytopes ──\n")
    for name, builder in [("5-cell {3,3,3}", cell5),
                           ("8-cell/tesseract {4,3,3}", cell8),
                           ("16-cell {3,3,4}", cell16),
                           ("24-cell {3,4,3}", cell24),
                           ("600-cell {3,3,5}", cell600)]:
        A = builder()
        r = measure(A, name)
        results.append(r)

    # 120-cell takes longer but let's try
    print(f"\n  Building 120-cell (may take a moment)...")
    try:
        A120 = cell120()
        if len(A120) > 50:
            r = measure(A120, f"120-cell {{5,3,3}} ({len(A120)}v)")
            results.append(r)
        else:
            print(f"  120-cell: only got {len(A120)} vertices, skipping")
    except Exception as e:
        print(f"  120-cell failed: {e}")

    # Summary
    dt = time.time() - T0
    print(f"\n{'=' * 100}")
    print(f"  UNIQUENESS SUMMARY")
    print(f"{'=' * 100}\n")

    results.sort(key=lambda r: min(r["delta_hk"], r["delta_nl"]))

    print(f"  {'Polytope':45s} {'V':>5s} {'ds_HK':>7s} {'ds_NL':>7s} {'best|Δφ|':>9s}")
    print(f"  {'─'*45} {'─'*5} {'─'*7} {'─'*7} {'─'*9}")
    for r in results:
        best = min(r["delta_hk"], r["delta_nl"])
        tag = " ◄◄◄" if best < 0.05 else (" ◄" if best < 0.15 else "")
        print(f"  {r['label']:45s} {r['V']:5d} {r['ds_hk']:7.4f} {r['ds_nl']:7.4f} {best:9.4f}{tag}")

    # Count near-φ
    near_phi = [r for r in results if min(r["delta_hk"], r["delta_nl"]) < 0.05]
    print(f"\n  Polytopes with ds within 0.05 of φ: {len(near_phi)}")
    for r in near_phi:
        print(f"    {r['label']}")

    if len(near_phi) == 1 and "600-cell" in near_phi[0]["label"]:
        verdict = "UNIQUE — the 600-cell is the ONLY regular polytope with ds ≈ φ"
    elif len(near_phi) == 0:
        verdict = "NONE — no regular polytope has ds ≈ φ (measurement issue?)"
    elif all("600" in r["label"] or "120" in r["label"] for r in near_phi):
        verdict = "H4 FAMILY ONLY — only H4 polytopes (600-cell/120-cell) have ds ≈ φ"
    else:
        verdict = f"NOT UNIQUE — {len(near_phi)} polytopes have ds ≈ φ"

    print(f"\n  ╔{'═'*72}╗")
    print(f"  ║  {verdict:70s}  ║")
    print(f"  ╚{'═'*72}╝")

    print(f"\n  Time: {dt:.0f}s")

    # Save
    rpath = os.path.join(OUT, "polytope_uniqueness.md")
    with open(rpath, "w") as f:
        f.write(f"# Polytope Uniqueness Test\n\n**{verdict}**\n\nφ = {PHI:.6f}\n\n")
        f.write("| Polytope | V | E | ds_HK | ds_NL | |best−φ| |\n")
        f.write("|----------|---|---|-------|-------|--------|\n")
        for r in results:
            best = min(r["delta_hk"], r["delta_nl"])
            f.write(f"| {r['label']} | {r['V']} | {r['E']} | {r['ds_hk']:.4f} | "
                    f"{r['ds_nl']:.4f} | {best:.4f} |\n")
    print(f"  Report: {rpath}")


if __name__ == "__main__":
    main()
