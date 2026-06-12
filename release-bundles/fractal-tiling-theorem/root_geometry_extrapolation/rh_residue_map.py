"""
Map the 26 sigma-paired (phi-irrational) modes and where the RH-residue lives.

The 600-cell adjacency A_1 has 9 distinct eigenvalues. Galois sigma (sqrt5 <-> -sqrt5)
splits them: integer eigenvalues are sigma-FIXED (rational); phi-irrational ones are
sigma-PAIRED. We compute the exact split, the sigma-conjugate pairing, and identify the
26-dim residue block -- the part where the RH-analog is OPEN.
"""
import numpy as np
from collections import Counter
from itertools import product
PHI=(1+5**0.5)/2

def vertices():
    V=[]
    for i in range(4):
        for s in (1,-1):
            v=[0.]*4; v[i]=float(s); V.append(v)
    for sg in product((.5,-.5),repeat=4): V.append(list(sg))
    a,b,c=1/(2*PHI),.5,PHI/2; base=[0.,a,b,c]
    EP=[(0,1,2,3),(0,2,3,1),(0,3,1,2),(1,0,3,2),(1,2,0,3),(1,3,2,0),
        (2,0,1,3),(2,1,3,0),(2,3,0,1),(3,0,2,1),(3,1,0,2),(3,2,1,0)]
    for p in EP:
        co=[base[p[i]] for i in range(4)]; nz=[i for i,x in enumerate(co) if x!=0]
        for sg in product((1,-1),repeat=len(nz)):
            v=list(co)
            for idx,s in zip(nz,sg): v[idx]*=s
            V.append(v)
    u=[]
    for v in V:
        if not any(np.linalg.norm(np.array(v)-np.array(w))<1e-9 for w in u): u.append(v)
    arr=np.array(u); return arr/np.linalg.norm(arr,axis=1,keepdims=True)
Vx=vertices(); D=np.linalg.norm(Vx[:,None]-Vx[None,:],axis=-1)
A=(np.abs(D-1/PHI)<1e-6).astype(float); np.fill_diagonal(A,0)
ev=np.linalg.eigvalsh(A)
# bucket eigenvalues (round to 3dp), express in a+b*phi form
def as_aphi(x):
    # solve x = a + b*phi with small integers a,b
    for b in range(-8,9):
        a = x - b*PHI
        if abs(a-round(a))<1e-3: return (int(round(a)), b)
    return None
buckets=Counter(np.round(ev,3))
rows=[]
for val,mult in sorted(buckets.items()):
    ab=as_aphi(val); rows.append((val,mult,ab))

print("="*78); print("600-cell adjacency spectrum: sigma split (94 fixed + 26 paired)"); print("="*78)
print(f"\n  {'eigenvalue':>11} {'mult':>4} {'a+b*phi':>10} {'sigma-class':>14}")
fixed=paired=0
paired_modes=[]
for val,mult,ab in rows:
    if ab is None: continue
    a,b=ab
    if b==0:
        cls="FIXED (rational)"; fixed+=mult
    else:
        cls="PAIRED (irrat.)"; paired+=mult; paired_modes.append((a,b,mult,val))
    lab=f"{a}" if b==0 else f"{a}{'+' if b>=0 else ''}{b}*phi"
    print(f"  {val:11.3f} {mult:4d} {lab:>10} {cls:>14}")
print(f"\n  sigma-FIXED total : {fixed}  (= 1+16+25+36+16, the integer eigenvalues)")
print(f"  sigma-PAIRED total: {paired}  (the phi-irrational residue = the 26-dim block)")

print("\n  sigma-conjugate pairing of the residue (sigma: phi -> 1-phi):")
seen=set()
for a,b,mult,val in paired_modes:
    key=tuple(sorted([(a,b),(a+b,-b)]))
    if key in seen: continue
    seen.add(key)
    conj_val=(a+b)+(-b)*PHI
    print(f"    {a}{'+' if b>=0 else ''}{b}*phi (mult {mult})  <->  "
          f"{a+b}{'-' if b>0 else '+'}{abs(b)}*phi (conjugate)   [{val:.3f} <-> {conj_val:.3f}]")
half=sum(m for a,b,m,v in paired_modes if b>0)
print(f"  -> {half}+{paired-half} split (13+13): {half}=6phi(4)+4phi(9), {paired-half}=conjugates")

print("\n" + "="*78)
print("WHERE THE RH-RESIDUE LIVES")
print("="*78)
print(f"""  94 sigma-FIXED (rational, integer eigenvalues):
      Eisenstein/rational layer. Provably on Fix(tau) = critical line
      (per-observer-zero-line T5.1/5.2, unconditional MODULO Galois). RH-analog: CLOSED here.

  26 sigma-PAIRED (phi-irrational) = the 26-dim block:
      the NON-rational, cuspidal-candidate residue. Two sigma-conjugate halves (13+13):
        {{6phi (m4), 4phi (m9)}}  <->  {{6-6phi (m4), 4-4phi (m9)}}.
      This is exactly the block the (fitted) Hecke probes targeted. The RH-analog for THIS
      object = whether the closure-flow (H_attr) suppresses this residue onto Fix(tau).
      For the 94: proven. For these 26: OPEN. ===> RH lives in the 26-dim sigma-paired block.

  HONEST CHAIN to classical RH(zeta):
      sigma-fixed/Eisenstein part  ->  ζ_K(s)ζ_K(s-1)  (Dedekind zeta of Q(sqrt5); VERIFIED)
      sigma-paired/26-block part   ->  the cuspidal HMF over Q(sqrt5)  (RH-analog OPEN; the
                                       geometric generator = icosian Brandt = UNBUILT)
      Q(sqrt5) automorphic RH      ->  classical RH(zeta)  (further step; the root geometry)
  So 'RH lives in the 26' is the RH-ANALOG for the icosian object; the bridge to RH(zeta)
  runs through the open/unbuilt steps. A precise LOCALISATION, not a proof.""")
print("="*78)
