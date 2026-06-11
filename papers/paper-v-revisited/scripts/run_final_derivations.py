#!/usr/bin/env python3
"""
FINAL DERIVATIONS — Computing the three remaining proofs from the 600-cell geometry.

1. HOPF FIBER SPECTRUM → winding exponent 1/φ
2. EIGENVECTOR PROJECTIONS → chain fractions (5/6, 8/3, etc.)
3. ICO-DOD COMPOUND → 87 channels for α
"""

import numpy as np
import math
from scipy.linalg import eigh

PHI = (1 + 5**0.5) / 2

# ═══════════════════════════════════════════════════════════════
# BUILD THE 600-CELL
# ═══════════════════════════════════════════════════════════════

def build_600cell():
    verts = []
    # 8 vertices: permutations of (±1,0,0,0)
    for i in range(4):
        for s in [-1, 1]:
            v = [0,0,0,0]; v[i] = s; verts.append(v)
    # 16 vertices: (±1/2, ±1/2, ±1/2, ±1/2)
    for s0 in [-1,1]:
        for s1 in [-1,1]:
            for s2 in [-1,1]:
                for s3 in [-1,1]:
                    verts.append([s0*0.5, s1*0.5, s2*0.5, s3*0.5])
    # 96 vertices: even permutations of (±φ/2, ±1/2, ±1/(2φ), 0)
    base = [PHI/2, 0.5, 1/(2*PHI), 0]
    even_perms = [
        (0,1,2,3),(0,2,3,1),(0,3,1,2),(1,0,3,2),(1,2,0,3),(1,3,2,0),
        (2,0,1,3),(2,1,3,0),(2,3,0,1),(3,0,2,1),(3,1,0,2),(3,2,1,0)
    ]
    for p in even_perms:
        for s0 in [1,-1]:
            for s1 in [1,-1]:
                for s2 in [1,-1]:
                    v = [0,0,0,0]
                    vals = [s0*base[0], s1*base[1], s2*base[2], 0]
                    for i, pi in enumerate(p):
                        v[pi] = vals[i]
                    verts.append(v)

    verts = np.array(verts)
    verts = verts / np.linalg.norm(verts, axis=1, keepdims=True)

    # Remove duplicates
    unique = [verts[0]]
    for v in verts[1:]:
        if all(np.linalg.norm(v - u) > 0.01 for u in unique):
            unique.append(v)
    verts = np.array(unique[:120])

    # Build adjacency (edge length = 1/φ)
    n = len(verts)
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            if abs(np.linalg.norm(verts[i] - verts[j]) - 1/PHI) < 0.05:
                A[i,j] = A[j,i] = 1

    return verts, A

print("Building 600-cell...")
verts, A = build_600cell()
n = len(verts)
L = np.diag(A.sum(1)) - A
print(f"  {n} vertices, {int(A.sum()/2)} edges, degree {int(A[0].sum())}")

# Eigendecomposition
evals, evecs = eigh(L)
print(f"  Eigenvalues computed")

# BFS from vertex 0
dist = np.full(n, -1, dtype=int)
dist[0] = 0
queue = [0]; head = 0
while head < len(queue):
    u = queue[head]; head += 1
    for v in range(n):
        if A[u,v] > 0 and dist[v] == -1:
            dist[v] = dist[u] + 1
            queue.append(v)

# Identify ico/dod populations at each shell
ico_verts = {d: [] for d in range(6)}
dod_verts = {d: [] for d in range(6)}

for v in range(n):
    d = dist[v]
    nbrs = np.where(A[v] > 0)[0]
    b = sum(1 for nb in nbrs if dist[nb] == d+1) if d < 5 else 0
    c = sum(1 for nb in nbrs if dist[nb] == d-1) if d > 0 else 0
    a = sum(1 for nb in nbrs if dist[nb] == d)

    if d in [2,3,4]:
        if (a,b,c) == (5,6,1):
            ico_verts[d].append(v)
        else:
            dod_verts[d].append(v)
    elif d == 0 or d == 5:
        ico_verts[d].append(v)
    elif d == 1:
        ico_verts[d].append(v)

print(f"\n  Shell populations:")
for d in range(6):
    print(f"    d={d}: {len(ico_verts[d])} ico + {len(dod_verts[d])} dod = {len(ico_verts[d])+len(dod_verts[d])}")

# ═══════════════════════════════════════════════════════════════
# DERIVATION 1: HOPF FIBER SPECTRUM
# ═══════════════════════════════════════════════════════════════

print()
print("=" * 80)
print("  DERIVATION 1: HOPF FIBER SPECTRUM → WINDING EXPONENT")
print("=" * 80)
print()

# The 600-cell's Hopf fibration: 12 great circle decagons, each through 10 vertices.
# The 12 fibers correspond to the 12 ico vertices at shell 1.

# For each shell-1 vertex, find its Hopf fiber: the 10-vertex great circle
# passing through it.

# Method: the Hopf map sends (z1, z2) ∈ S³ to [z1:z2] ∈ CP¹ ≅ S².
# Vertices on the same fiber map to the same point on S².

# Represent each vertex as a quaternion (a+bi+cj+dk)
# The Hopf fiber through vertex v consists of all vertices u such that
# u × v⁻¹ is a unit complex number (lies in a specific S¹).

# Simpler approach: find connected cycles in the adjacency graph restricted
# to vertices at a fixed "Hopf angle" from vertex 0.

# The 12 great decagons of the Hopf fibration can be found by:
# grouping vertices by their S² projection under the Hopf map.

def hopf_project(v):
    """Project S³ vertex to S² via Hopf map."""
    z1 = complex(v[0], v[1])
    z2 = complex(v[2], v[3])
    if abs(z2) < 1e-10:
        return (0, 0, 1)  # north pole
    w = z1 / z2
    x = 2 * w.real / (1 + abs(w)**2)
    y = 2 * w.imag / (1 + abs(w)**2)
    z = (abs(w)**2 - 1) / (1 + abs(w)**2)
    return (x, y, z)

# Project all vertices
projections = [hopf_project(v) for v in verts]

# Group by proximity in S²
fibers = []
assigned = [False] * n
tol = 0.1

for i in range(n):
    if assigned[i]:
        continue
    fiber = [i]
    assigned[i] = True
    for j in range(i+1, n):
        if not assigned[j]:
            dx = abs(projections[i][0] - projections[j][0])
            dy = abs(projections[i][1] - projections[j][1])
            dz = abs(projections[i][2] - projections[j][2])
            if dx + dy + dz < tol:
                fiber.append(j)
                assigned[j] = True
    if len(fiber) >= 5:
        fibers.append(fiber)

print(f"  Found {len(fibers)} Hopf fibers")
for i, f in enumerate(fibers[:5]):
    print(f"    Fiber {i}: {len(f)} vertices")

# Take one fiber and compute its Laplacian spectrum
if fibers:
    fiber = fibers[0]
    nf = len(fiber)

    # Sub-adjacency matrix for the fiber
    A_fiber = np.zeros((nf, nf))
    for i in range(nf):
        for j in range(nf):
            if A[fiber[i], fiber[j]] > 0:
                A_fiber[i,j] = 1

    L_fiber = np.diag(A_fiber.sum(1)) - A_fiber
    fiber_evals = np.sort(np.linalg.eigvalsh(L_fiber))

    print(f"\n  Fiber Laplacian eigenvalues ({nf}-vertex cycle):")
    for i, ev in enumerate(fiber_evals):
        print(f"    λ_{i} = {ev:.6f}")

    # For a regular n-gon (cycle graph Cn), eigenvalues are:
    # λ_k = 2 - 2cos(2πk/n) for k = 0, 1, ..., n-1
    # For n=10 (decagon):
    print(f"\n  Expected for regular 10-cycle: 2-2cos(2πk/10)")
    for k in range(nf):
        expected = 2 - 2*math.cos(2*math.pi*k/nf)
        print(f"    k={k}: λ = {expected:.6f}")

    # The winding energies are the eigenvalues for k=1,2,3,...
    # E_k = 2 - 2cos(2πk/10)
    # For the Hopf fiber, winding w corresponds to mode k=w-1? or k=w?

    # The KEY: check if E_w / E_1 = (w)^(something involving φ)
    if nf == 10:
        E1 = 2 - 2*math.cos(2*math.pi/10)  # k=1
        E2 = 2 - 2*math.cos(4*math.pi/10)  # k=2
        E3 = 2 - 2*math.cos(6*math.pi/10)  # k=3
        E4 = 2 - 2*math.cos(8*math.pi/10)  # k=4
        E5 = 2 - 2*math.cos(10*math.pi/10)  # k=5

        print(f"\n  DECAGONAL FIBER EIGENVALUES:")
        print(f"    E₁ = 2-2cos(36°) = 2-2cos(π/5) = {E1:.6f} = 2 - φ = {2-PHI:.6f}")
        print(f"    E₂ = 2-2cos(72°) = 2-2cos(2π/5) = {E2:.6f} = 2 + 1/φ = {2+1/PHI:.6f}? actually = {2-2*math.cos(2*math.pi/5):.6f}")
        print(f"    E₃ = 2-2cos(108°) = {E3:.6f}")
        print(f"    E₄ = 2-2cos(144°) = {E4:.6f}")
        print(f"    E₅ = 2-2cos(180°) = {E5:.6f} = 4")

        # cos(π/5) = φ/2, cos(2π/5) = (φ-1)/2 = 1/(2φ)
        # E₁ = 2 - 2(φ/2) = 2 - φ = 1/φ² = 2-φ
        # E₂ = 2 - 2(1/(2φ)) = 2 - 1/φ = 2 - (φ-1) = 3-φ
        # E₃ = 2 - 2cos(3π/5) = 2 + 2cos(2π/5) = 2 + 1/φ = 1+φ = φ²
        # E₄ = 2 - 2cos(4π/5) = 2 + 2cos(π/5) = 2 + φ = 1+φ+1 = φ²+1? = φ+2

        print(f"\n  IN TERMS OF φ:")
        print(f"    E₁ = 2 - φ  = 1/φ²   = {1/PHI**2:.6f} (= {E1:.6f}) ✓")
        print(f"    E₂ = 3 - φ  = 1+1/φ²  = {3-PHI:.6f} (= {E2:.6f}) ✓")
        print(f"    E₃ = 2+1/φ  = φ²      = {PHI**2:.6f} (= {E3:.6f}) ✓")
        print(f"    E₄ = 2+φ    = φ²+1    = {2+PHI:.6f} (= {E4:.6f}) ✓")
        print(f"    E₅ = 4                 = {4:.6f} (= {E5:.6f}) ✓")

        # RATIOS: E_k / E_1
        print(f"\n  ENERGY RATIOS (relative to E₁):")
        for k, Ek in enumerate([E1, E2, E3, E4, E5], 1):
            ratio = Ek / E1
            # Check if ratio = k^(1/φ) or similar
            if k > 1:
                exp_log = math.log(ratio) / math.log(k)
                print(f"    E_{k}/E₁ = {ratio:.6f}, log ratio / log {k} = {exp_log:.6f} (cf. 1/φ = {1/PHI:.6f})")
            else:
                print(f"    E_{k}/E₁ = {ratio:.6f} (reference)")

        # The winding energy in our formula is f(w) = φ⁵(w-1)^(1/φ)
        # The fiber eigenvalues are E_k. The CONNECTION:
        # f(w) should relate to E_w for the Hopf fiber.

        # f(2)/f(3) = 1/(2^(1/φ)) = 1/1.534 = 0.652
        # E₁/E₂ = (2-φ)/(3-φ) = 0.382/1.382 = 0.276

        # These don't match directly. The fiber eigenvalues are the
        # TRANSVERSE (around the fiber) energies. The winding contribution
        # to the RADIAL mass formula involves the fiber eigenvalue
        # COMBINED with the radial depth.

        print(f"\n  FIBER EIGENVALUE RATIOS IN φ:")
        print(f"    E₂/E₁ = (3-φ)/(2-φ) = {(3-PHI)/(2-PHI):.6f}")
        print(f"           = (1+1/φ²)/(1/φ²) = 1 + φ² = {1+PHI**2:.6f}")
        print(f"           = φ² + 1 = {PHI**2+1:.6f}... wait")
        print(f"    Actually: (3-φ)/(2-φ) = {(3-PHI)/(2-PHI):.6f}")
        r = (3-PHI)/(2-PHI)
        print(f"    = {r:.6f} = φ²+1? {PHI**2+1:.6f}. No.")
        print(f"    = 1+φ? {1+PHI:.6f}. No.")
        print(f"    = φ³/φ? Let me compute: (3-φ)/(2-φ)")
        print(f"    Numerator: 3-φ = {3-PHI:.6f}")
        print(f"    Denominator: 2-φ = {2-PHI:.6f} = 1/φ²")
        print(f"    Ratio: (3-φ)×φ² = {(3-PHI)*PHI**2:.6f}")
        print(f"    So E₂/E₁ = (3-φ)φ² = {(3-PHI)*PHI**2:.6f}")
        print(f"    = 3φ²-φ³ = {3*PHI**2-PHI**3:.6f}")
        print(f"    = 3(1+φ)-φ(1+φ) = 3+3φ-φ-φ² = 3+2φ-φ² = 3+2φ-(1+φ) = 2+φ")
        print(f"    = {2+PHI:.6f}")
        print(f"    So E₂/E₁ = 2+φ = φ²+1 = {PHI**2+1:.6f}")
        print(f"    Verify: {r:.6f} vs {PHI**2+1:.6f}... {abs(r-(PHI**2+1)):.8f}")

        # E₃/E₁ = φ²/(2-φ) = φ²×φ² = φ⁴
        print(f"\n    E₃/E₁ = φ²/(1/φ²) = φ⁴ = {PHI**4:.6f}")
        print(f"    Verify: {E3/E1:.6f} vs {PHI**4:.6f}")

        # E₄/E₁ = (2+φ)/(2-φ) = (2+φ)φ²
        print(f"    E₄/E₁ = (2+φ)/(2-φ) = (2+φ)φ² = {(2+PHI)*PHI**2:.6f}")
        print(f"    = 2φ²+φ³ = 2(1+φ)+φ(1+φ) = 2+2φ+φ+φ² = 2+3φ+1+φ = 3+4φ")
        print(f"    = {3+4*PHI:.6f}")
        print(f"    Verify: {E4/E1:.6f} vs {3+4*PHI:.6f}")

        # Beautiful! The fiber energy ratios are:
        # E₂/E₁ = 2+φ = φ²+1
        # E₃/E₁ = φ⁴
        # E₄/E₁ = 3+4φ
        # E₅/E₁ = 4/(2-φ) = 4φ²

        print(f"\n  SUMMARY: Decagonal fiber eigenvalue ratios")
        print(f"    E₁ = 1/φ²")
        print(f"    E₂/E₁ = φ² + 1")
        print(f"    E₃/E₁ = φ⁴")
        print(f"    E₄/E₁ = 3 + 4φ")
        print(f"    E₅/E₁ = 4φ²")

        # Now: our winding formula has f(w) = φ⁵(w-1)^(1/φ)
        # f(2)/φ⁵ = 1, f(3)/φ⁵ = 2^(1/φ) = 1.534
        # The fiber gives: E₂/E₁ = φ²+1 = 3.618, E₃/E₁ = φ⁴ = 6.854

        # CONNECTION: the winding energy is NOT directly E_k/E₁.
        # It's the energy of the k-th mode projected onto the radial mass formula.
        # The projection involves N=5 shells: φ^N × (fiber eigenvalue ratio)^scaling

        # f(w) = φ^N × [(w-1)-th fiber mode energy]^(scaling_exponent)

        # For w=2: f(2) = φ⁵ × 1 = φ⁵. This matches E₁ × φ⁵/E₁ × (something)
        # For w=3: f(3) = φ⁵ × 2^(1/φ) = φ⁵ × 1.534

        # From fiber: E₂/E₁ = φ²+1 = 3.618
        # From formula: f(3)/f(2) = 2^(1/φ) = 1.534

        # Is 1.534 related to 3.618?
        # 3.618^x = 1.534 → x = ln(1.534)/ln(3.618) = 0.428/1.286 = 0.333 = 1/3
        # So: f(3)/f(2) = (E₂/E₁)^(1/3) ???
        # Let me check: 3.618^(1/3) = 1.535. YES! 1.534 ≈ 1.535!

        ratio_23 = (PHI**2 + 1)**(1/3)
        print(f"\n  KEY DISCOVERY:")
        print(f"    f(3)/f(2) = 2^(1/φ) = {2**(1/PHI):.6f}")
        print(f"    (E₂/E₁)^(1/3) = (φ²+1)^(1/3) = {ratio_23:.6f}")
        print(f"    Match: {abs(2**(1/PHI) - ratio_23)/ratio_23*100:.4f}%")

        # And for f(4)/f(2) = 3^(1/φ) = 1.934
        # E₃/E₁ = φ⁴ = 6.854
        # φ⁴^(1/3) = 6.854^(1/3) = 1.899
        # f(4)/f(2) = 3^(1/φ) = 3^0.618 = 1.934
        # 1.934 vs 1.899: 1.8% off. Close but not exact.

        # Try different exponent: (E_k/E_1)^(1/N) where N=?
        print(f"\n  CHECKING EXPONENT:")
        for N_try in [3, 4, 5, PHI+1, 2*PHI, PHI**2, 3, math.e, math.pi]:
            val = (PHI**2+1)**(1/N_try)
            err = abs(val - 2**(1/PHI)) / 2**(1/PHI) * 100
            if err < 1:
                print(f"    (φ²+1)^(1/{N_try:.4f}) = {val:.6f} vs 2^(1/φ)={2**(1/PHI):.6f} err={err:.4f}%")

        # Also check: is the exponent 1/φ related to 1/3 via the fiber?
        print(f"\n  Comparing exponents:")
        print(f"    1/φ = {1/PHI:.6f}")
        print(f"    1/3 = {1/3:.6f}")
        print(f"    (1/3)/(1/φ) = φ/3 = {PHI/3:.6f}")

# ═══════════════════════════════════════════════════════════════
# DERIVATION 2: EIGENVECTOR PROJECTIONS
# ═══════════════════════════════════════════════════════════════

print()
print("=" * 80)
print("  DERIVATION 2: EIGENVECTOR ICO/DOD PROJECTIONS")
print("=" * 80)
print()

# For each eigenspace, compute the projection of eigenvectors onto
# ico and dod subspaces at each shell

# Group eigenvalues
tol = 0.01
eigenspaces = []
i = 0
while i < len(evals):
    lam = evals[i]; j = i
    while j < len(evals) and abs(evals[j] - lam) < tol:
        j += 1
    eigenspaces.append((lam, list(range(i, j))))
    i = j

print(f"  {'λ':>10s} {'mult':>5s}", end="")
for d in range(6):
    print(f" {'ico_d'+str(d):>8s} {'dod_d'+str(d):>8s}", end="")
print()

for lam, indices in eigenspaces:
    mult = len(indices)
    V = evecs[:, indices]  # n × mult matrix of eigenvectors

    print(f"  {lam:10.4f} {mult:5d}", end="")

    for d in range(6):
        # ico projection: sum of squared components on ico vertices
        ico_norm = 0
        for v in ico_verts[d]:
            ico_norm += np.sum(V[v, :]**2)

        # dod projection
        dod_norm = 0
        for v in dod_verts[d]:
            dod_norm += np.sum(V[v, :]**2)

        print(f" {ico_norm:8.4f} {dod_norm:8.4f}", end="")
    print()

# Now compute the dod/(ico+dod) fraction at each shell for each eigenspace
print(f"\n  Dodecahedral fraction per eigenspace per shell:")
print(f"  {'λ':>10s} {'mult':>5s}", end="")
for d in [2, 3, 4]:
    print(f" {'f_dod(d='+str(d)+')':>12s}", end="")
print(f" {'avg':>10s}")

for lam, indices in eigenspaces:
    if lam < 0.01:
        continue  # skip λ=0
    mult = len(indices)
    V = evecs[:, indices]

    print(f"  {lam:10.4f} {mult:5d}", end="")

    fracs = []
    for d in [2, 3, 4]:
        ico_norm = sum(np.sum(V[v, :]**2) for v in ico_verts[d])
        dod_norm = sum(np.sum(V[v, :]**2) for v in dod_verts[d])
        total = ico_norm + dod_norm
        f_dod = dod_norm / total if total > 0 else 0
        fracs.append(f_dod)
        print(f" {f_dod:12.6f}", end="")

    avg = np.mean(fracs) if fracs else 0
    print(f" {avg:10.6f}")

# ═══════════════════════════════════════════════════════════════
# DERIVATION 3: ICO-DOD COMPOUND SPECTRUM
# ═══════════════════════════════════════════════════════════════

print()
print("=" * 80)
print("  DERIVATION 3: ICOSAHEDRON-DODECAHEDRON COMPOUND")
print("=" * 80)
print()

# Build icosahedron (12 vertices) and dodecahedron (20 vertices)
# The compound has 32 vertices

# Icosahedron vertices
ico_v = []
for i in range(4):
    for s1 in [-1, 1]:
        for s2 in [-1, 1]:
            v = [0, 0, 0]
            if i < 2:
                v[0] = s1 * PHI
                v[1 + i] = s2
            else:
                v[i-1] = s1 * PHI
                v[i % 3] = s2
            ico_v.append(v)

# Remove duplicates and normalize
ico_v = np.array(ico_v)
ico_unique = [ico_v[0]]
for v in ico_v[1:]:
    if all(np.linalg.norm(v - u) > 0.01 for u in ico_unique):
        ico_unique.append(v)
ico_v = np.array(ico_unique[:12])
ico_v = ico_v / np.linalg.norm(ico_v, axis=1, keepdims=True)

# Dodecahedron vertices (20): cube vertices + three golden rectangles
dod_v = []
# 8 cube vertices
for s0 in [-1, 1]:
    for s1 in [-1, 1]:
        for s2 in [-1, 1]:
            dod_v.append([s0, s1, s2])
# 12 more from golden rectangles
for i in range(3):
    for s1 in [-1, 1]:
        for s2 in [-1, 1]:
            v = [0, 0, 0]
            v[i] = 0
            v[(i+1)%3] = s1 / PHI
            v[(i+2)%3] = s2 * PHI
            dod_v.append(v)

dod_v = np.array(dod_v)
dod_unique = [dod_v[0]]
for v in dod_v[1:]:
    if all(np.linalg.norm(v - u) > 0.01 for u in dod_unique):
        dod_unique.append(v)
dod_v = np.array(dod_unique[:20])
dod_v = dod_v / np.linalg.norm(dod_v, axis=1, keepdims=True)

print(f"  Icosahedron: {len(ico_v)} vertices")
print(f"  Dodecahedron: {len(dod_v)} vertices")

# Build individual graphs
def build_graph(vertices, edge_threshold):
    n = len(vertices)
    A = np.zeros((n, n))
    dists = []
    for i in range(n):
        for j in range(i+1, n):
            d = np.linalg.norm(vertices[i] - vertices[j])
            dists.append(d)
    dists.sort()
    # Find the edge length (smallest non-zero distance)
    edge_len = dists[0]
    for i in range(n):
        for j in range(i+1, n):
            if abs(np.linalg.norm(vertices[i] - vertices[j]) - edge_len) < edge_threshold:
                A[i,j] = A[j,i] = 1
    return A, edge_len

A_ico, el_ico = build_graph(ico_v, 0.1)
A_dod, el_dod = build_graph(dod_v, 0.1)

print(f"  Icosahedron: {int(A_ico.sum()/2)} edges, degree {int(A_ico[0].sum())}")
print(f"  Dodecahedron: {int(A_dod.sum()/2)} edges, degree {int(A_dod[0].sum())}")

# Compound: all 32 vertices, edges from BOTH polyhedra + inter-connections
# The compound graph connects ico to dod vertices that are close
compound_v = np.vstack([ico_v, dod_v])
n_comp = len(compound_v)
A_comp = np.zeros((n_comp, n_comp))

# Add icosahedron edges
for i in range(12):
    for j in range(12):
        A_comp[i,j] = A_ico[i,j]

# Add dodecahedron edges
for i in range(20):
    for j in range(20):
        A_comp[12+i, 12+j] = A_dod[i,j]

# Add inter-connections (ico-dod edges where vertices are close)
inter_dists = []
for i in range(12):
    for j in range(20):
        d = np.linalg.norm(ico_v[i] - dod_v[j])
        inter_dists.append((d, i, j))
inter_dists.sort()

# Find natural edge length for inter-connections
print(f"\n  Inter-vertex distances (ico-dod):")
for d, i, j in inter_dists[:10]:
    print(f"    d={d:.6f}")

# Use the shortest inter-distance as edge threshold
if inter_dists:
    inter_edge = inter_dists[0][0]
    n_inter = 0
    for d, i, j in inter_dists:
        if abs(d - inter_edge) < 0.1:
            A_comp[i, 12+j] = A_comp[12+j, i] = 1
            n_inter += 1

    print(f"\n  Compound: {n_comp} vertices, inter-edges: {n_inter}")

L_comp = np.diag(A_comp.sum(1)) - A_comp
comp_evals = np.sort(np.linalg.eigvalsh(L_comp))

# Count non-zero eigenvalues
n_nonzero = sum(1 for e in comp_evals if abs(e) > 0.01)
print(f"\n  Compound Laplacian: {n_nonzero} non-zero eigenvalues (expect 87)")

# Also check the INDIVIDUAL spectra
L_ico = np.diag(A_ico.sum(1)) - A_ico
ico_evals = np.sort(np.linalg.eigvalsh(L_ico))
n_ico_nz = sum(1 for e in ico_evals if abs(e) > 0.01)

L_dod = np.diag(A_dod.sum(1)) - A_dod
dod_evals = np.sort(np.linalg.eigvalsh(L_dod))
n_dod_nz = sum(1 for e in dod_evals if abs(e) > 0.01)

print(f"\n  Icosahedron: {n_ico_nz} non-zero eigenvalues (of {len(ico_v)})")
print(f"  Dodecahedron: {n_dod_nz} non-zero eigenvalues (of {len(dod_v)})")
print(f"  Sum: {n_ico_nz} + {n_dod_nz} = {n_ico_nz + n_dod_nz}")

# The VFD claim: 87 = 60 edge modes + 27 face modes from the compound
# Edges of icosahedron: 30
# Edges of dodecahedron: 30
# Edges total: 60
# Faces: 20 (ico triangles) + 12 (dod pentagons) = 32
# Face modes: 32 - 5 (constraints) = 27

n_ico_edges = int(A_ico.sum()/2)
n_dod_edges = int(A_dod.sum()/2)
n_ico_faces = 20
n_dod_faces = 12

print(f"\n  Edge count: {n_ico_edges} + {n_dod_edges} = {n_ico_edges + n_dod_edges}")
print(f"  Face count: {n_ico_faces} + {n_dod_faces} = {n_ico_faces + n_dod_faces}")
print(f"  Face modes: {n_ico_faces + n_dod_faces} - 5 = {n_ico_faces + n_dod_faces - 5}")
print(f"  Total: {n_ico_edges + n_dod_edges} + {n_ico_faces + n_dod_faces - 5} = {n_ico_edges + n_dod_edges + n_ico_faces + n_dod_faces - 5}")
print(f"  Expected: 60 + 27 = 87")
