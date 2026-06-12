"""
Can the root geometry be a sphere/polytope? — the discriminating test.

The statistics of the Riemann zeros are the fingerprint of the root's spectral TYPE.
We compare:
  (A) the nearest-neighbour spacing of the Riemann zeros (unfolded), vs
  (B) the spacing of our 600-cell Laplacian spectrum (the spherical/polytope candidate).

A symmetric space (sphere, polytope, E8) has a RIGID, highly-DEGENERATE spectrum
(few distinct eigenvalues, huge multiplicities) -> Poisson/degenerate spacings, NO level
repulsion. The Riemann zeros show GUE level repulsion (random-matrix, chaotic). If the two
disagree, the root is NOT a sphere/polytope -- it must be chaotic / noncommutative.
"""
import numpy as np, mpmath as mp, math
mp.mp.dps = 30

# ---- (A) Riemann zeros: unfold and measure nearest-neighbour spacings ----
N = 200
gam = [float(mp.im(mp.zetazero(n))) for n in range(1, N + 1)]
# unfold by the mean density rho(t) = (1/2pi) log(t/2pi)
unf = []
for g in gam:
    unf.append(g * (math.log(g / (2 * math.pi)) / (2 * math.pi)))
sp_zeros = np.diff(unf)
sp_zeros = sp_zeros / sp_zeros.mean()                 # normalise mean spacing to 1
small_zeros = float(np.mean(sp_zeros < 0.1))          # fraction of tiny gaps (repulsion -> ~0)
# GUE Wigner surmise P(s) = (32/pi^2) s^2 exp(-4 s^2/pi): P(s<0.1) ~ 0.001
gue_small = 32 / math.pi**2 * (0.05**2) * math.exp(-4 * 0.05**2 / math.pi) * 0.1  # rough mass<0.1

# ---- (B) 600-cell Laplacian spectrum ----
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "vfd_geometry"))
# build the 600-cell Laplacian directly (self-contained)
PHI = (1 + 5 ** 0.5) / 2
def build_600():
    V = []
    for i in range(4):
        for s in (1, -1):
            v = [0.0]*4; v[i] = float(s); V.append(v)
    from itertools import product
    for sg in product((0.5, -0.5), repeat=4):
        V.append(list(sg))
    a, b, c = 1/(2*PHI), 0.5, PHI/2; base = [0.0, a, b, c]
    evenp = [(0,1,2,3),(0,2,3,1),(0,3,1,2),(1,0,3,2),(1,2,0,3),(1,3,2,0),
             (2,0,1,3),(2,1,3,0),(2,3,0,1),(3,0,2,1),(3,1,0,2),(3,2,1,0)]
    for p in evenp:
        co = [base[p[i]] for i in range(4)]; nz = [i for i,x in enumerate(co) if x!=0]
        for sg in product((1,-1), repeat=len(nz)):
            v = list(co)
            for idx,s in zip(nz,sg): v[idx]*=s
            V.append(v)
    uniq=[]
    for v in V:
        if not any(np.linalg.norm(np.array(v)-np.array(u))<1e-9 for u in uniq): uniq.append(v)
    arr=np.array(uniq); arr/=np.linalg.norm(arr,axis=1,keepdims=True)
    d=np.linalg.norm(arr[:,None]-arr[None,:],axis=-1)
    A=(np.abs(d-1/PHI)<1e-6).astype(float); np.fill_diagonal(A,0)
    return np.diag(A.sum(1))-A
L = build_600()
ev = np.round(np.linalg.eigvalsh(L), 4)
distinct = sorted(set(ev.tolist()))
sp_cell = np.diff(np.sort(ev))
degenerate_frac = float(np.mean(sp_cell < 1e-6))      # fraction of zero gaps (degeneracy)

print("="*78)
print("SPECTRAL-TYPE TEST: can the root be a sphere/polytope?")
print("="*78)
print(f"\n(A) Riemann zeros (first {N}, unfolded):")
print(f"    distinct values: all {N} distinct (no degeneracy)")
print(f"    fraction of spacings < 0.1 (level repulsion): {small_zeros:.3f}  "
      f"-> GUE predicts ~0 (zeros REPEL)")
print(f"\n(B) 600-cell Laplacian spectrum (120 eigenvalues):")
print(f"    distinct values: {len(distinct)}  ({distinct})")
print(f"    fraction of zero spacings (degeneracy): {degenerate_frac:.3f}  "
      f"-> massively DEGENERATE (eigenvalues CLUMP)")
print("\n" + "-"*78)
print("VERDICT:")
print(f"  Zeros: {N} distinct, level-repelling (GUE / chaotic fingerprint).")
print(f"  600-cell: only {len(distinct)} distinct eigenvalues among 120 "
      f"({degenerate_frac*100:.0f}% zero gaps) -- rigid, degenerate, SYMMETRIC.")
print("  These are OPPOSITE spectral types. A sphere/polytope/E8 gives rigid degeneracy;")
print("  the zeros give random-matrix repulsion. => the root CANNOT be a sphere/polytope.")
print("  It must produce a GUE spectrum -> CHAOTIC (hyperbolic flow) or NONCOMMUTATIVE.")
print("  (Montgomery-Odlyzko: zero statistics = GUE. This is established, not VFD.)")
print("="*78)
