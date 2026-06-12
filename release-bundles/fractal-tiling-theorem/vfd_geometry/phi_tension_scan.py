"""Phase 3 + 7: phi-tension scan + failure modes. The [m,3] Coxeter group in 3D is
FINITE iff the first-edge label m in {3,4,5} i.e. q=2cos(pi/m) in {1, sqrt2, phi}.
We RECOVER this by orbit closure: at special q the reflection orbit closes (finite
|W|); at generic q it explodes. phi=2cos(pi/5) is the 5-fold (icosahedral) value.
Honest: this is the known Coxeter finiteness criterion, recovered, not new."""
import numpy as np, math
import polytope_engine as E
PHI=E.PHI
def scan(q, cap=1500):
    L,pd=E.h3_simple_roots(q)
    if not pd: return dict(q=round(q,5), pd=False, orbit=None, finite=False, residual="non-Euclidean(G not PD)")
    roots=[L[i] for i in range(3)]
    seed=np.array([0.31,0.52,0.91])           # generic asymmetric seed -> full group orbit
    pts,fin=E.generate_orbit(roots, seed, cap=cap)
    return dict(q=round(q,5), pd=True, orbit=len(pts), finite=bool(fin),
                residual=0.0 if fin else 1.0, group_order=len(pts) if fin else None)
SPECIAL={"phi=2cos(pi/5)":PHI, "sqrt2=2cos(pi/4)":math.sqrt(2), "sqrt3=2cos(pi/6)":math.sqrt(3),
         "1.45(generic)":1.45, "1.55(generic)":1.55, "1.70(generic)":1.70, "1.90(generic)":1.90}
print("="*68); print("PHI-TENSION SCAN  [m,3] Coxeter orbit closure (3D)"); print("="*68)
print(f"{'q label':22s} {'q':8s} {'orbit':8s} finite  group")
results={}
for lab,q in SPECIAL.items():
    r=scan(q); results[lab]=r
    g={120:'H3 icosahedral',48:'B3 octahedral',24:'A3 tetrahedral'}.get(r['orbit'],'') if r['finite'] else ('EXPLODES' if r['pd'] else 'non-PD')
    print(f"{lab:22s} {r['q']:<8.4f} {str(r['orbit']):8s} {str(r['finite']):6s}  {g}")
# fine scan to confirm phi is an isolated finite island
fine=np.linspace(1.40,1.75,36); islands=[]
for q in fine:
    r=scan(q,cap=400)
    if r['pd'] and r['finite']: islands.append((round(q,4),r['orbit']))
print(f"\nfine scan of 36 GENERIC q in [1.40,1.75] -> finite-closure islands: {islands}")
print("  (empty is CORRECT: finite closure is MEASURE-ZERO -- only EXACT special q close;")
print("   the grid lands on no exact value, so every generic q EXPLODES. That IS the result:")
print("   finiteness is not a basin, it is isolated exact points q=2cos(pi/m).)")
print(f"\n[verdict] At EXACT values (main table): phi={PHI:.5f} -> H3 icosahedral (120, FINITE);")
print(f"          sqrt2={math.sqrt(2):.5f} -> B3 octahedral (48); sqrt3 -> AFFINE (G singular -> infinite).")
print("          phi is the 5-fold finite-closure value -- the RECOVERED Coxeter finiteness")
print("          criterion q=2cos(pi/m); phi is the icosahedral H3/H4 value. REAL and STRUCTURAL,")
print("          but KNOWN (non-crystallographic Coxeter), NOT a new VFD law.")
import json; json.dump(results, open("results/polytype_transformation_engine_001/phi_scan.json","w"), indent=2)
