import sys, os; sys.path.insert(0, os.getcwd())
from fractions import Fraction
import ideal_classes as ic
import quaternion_order as qo
import ok_arithmetic as ok
import brandt_matrices as bm

def compute_orbits_p(p):
    """Level-p version of ic.compute_orbits (geometric, no arithmetic target)."""
    I = qo.ring()
    spl = ic.LocalSplitting(p)
    pts = spl.p1_points()
    index = {spl.normalize(pt): i for i, pt in enumerate(pts)}
    umats = [spl.iota(u) for u in I.units]
    parent = list(range(len(pts)))
    def find(a):
        while parent[a]!=a: parent[a]=parent[parent[a]]; a=parent[a]
        return a
    def union(a,b):
        ra,rb=find(a),find(b)
        if ra!=rb: parent[ra]=rb
    for M in umats:
        for i,pt in enumerate(pts): union(i, index[spl.act(M,pt)])
    groups={}
    for i in range(len(pts)): groups.setdefault(find(i),[]).append(i)
    orbits=list(groups.values())
    return {"h":len(orbits),"orbits":orbits,"weights":[int(Fraction(60,len(o))) for o in orbits],
            "splitting":spl,"p1_points":pts,"p1_index":index,"orbit_sizes":sorted(len(o) for o in orbits)}

def engine_for(p):
    gate = compute_orbits_p(p)
    eng = bm.BrandtEngine.__new__(bm.BrandtEngine)
    eng.ring=qo.ring(); eng.gate=gate; eng.spl=gate["splitting"]; eng.orbits=gate["orbits"]
    eng.h=gate["h"]; eng.weights=gate["weights"]; eng.mu=[len(o) for o in gate["orbits"]]
    eng.pts=gate["p1_points"]; eng.index=gate["p1_index"]
    eng.orbit_of=[None]*len(eng.pts)
    for oi,o in enumerate(eng.orbits):
        for i in o: eng.orbit_of[i]=oi
    return eng

LEVEL=41
print(f"LEVEL {LEVEL} second-form build (geometry only, no arithmetic target)")
g=compute_orbits_p(LEVEL)
print(f"  P^1(F_{LEVEL}) points = {len(g['p1_points'])} (=N(level)+1={LEVEL+1});  Brandt h = {g['h']};  orbit sizes {g['orbit_sizes']}")
print(f"  cuspidal dim = h-1 = {g['h']-1}  (Dembele: 41 -> dim 1 elliptic)\n")
eng=engine_for(LEVEL)
import math
print(f"  {'N(q)':>5} {'a_q (geom)':>11} {'self-adj':>9} {'integral':>9} {'|a|<=2sqrtN':>13}")
test_primes=[11,19,29,31,59,61,71,79,89]   # coprime to 41
evs={}

# ---- out-of-sample check vs Dembele's E_41 (Table 4: [0,-phi,phi,0,0]) ----
if __name__ == "__main__":
    import point_count_target as pct
    pct.A1=(0,0); pct.A2=(0,-1); pct.A3=(0,1); pct.A4=(0,0); pct.A6=(0,0)
    pct.DELTA=pct._discriminant()
    tgt={}
    for r in pct.compute_target(norm_bound=100):
        if r["norm"]!=41: tgt.setdefault(r["norm"],set()).add(r["a_p"])
    def conj(g): a,b=g; return (a+b,-b)
    eng=engine_for(41)
    print("\nLEVEL-41 OUT-OF-SAMPLE: geometry (both generators) vs point-counted E_41")
    allm=True
    for q in [11,19,29,31,59,61,71,79,89]:
        g=bm.totally_positive_generator(q)
        if g is None or q not in tgt: continue
        gset=sorted({eng.brandt_matrix(g)["cuspidal_eigenvalue"],
                     eng.brandt_matrix(conj(g))["cuspidal_eigenvalue"]})
        tset=sorted(tgt[q]); m=gset==tset; allm&=m
        print(f"  N(q)={q:>3}  geom {str(gset):>12} == E_41 {str(tset):>12}  {m}")
    print(f"  SECOND FORM geometry==point-counted E_41 (no fit): {allm}")
