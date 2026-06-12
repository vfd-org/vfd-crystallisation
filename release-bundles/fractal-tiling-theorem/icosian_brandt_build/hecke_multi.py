"""Out-of-sample robustness: icosian Brandt cuspidal eigenvalues a_q for several split
primes vs the genuine point-count targets. NO fitting; gate Eisenstein==N(q)+1 each time."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "route_b"))
from fractions import Fraction
import icosian as I
import numpy as np
P=31; PHI_MOD=19
ADD=lambda a,b:(a[0]+b[0],a[1]+b[1]); SUB=lambda a,b:(a[0]-b[0],a[1]-b[1])
qm=lambda p,q: I.qmul(p,q,I.zmf,ADD,SUB); nrd=lambda q: I.nrd(q,I.zmf,ADD,SUB)
Fp=lambda a,b=0:(Fraction(a),Fraction(b))
units=I.unit_icosians()
inv=lambda d: pow(d%P,P-2,P)
I_MAT=((1,0),(0,1)); i_MAT=((0,1),(P-1,0)); j_MAT=((5,6),(6,26)); k_MAT=((6,26),(26,25))
def red(fp):
    a,b=fp; rf=lambda fr:(fr.numerator%P)*pow(fr.denominator%P,P-2,P)%P
    return (rf(a)+rf(b)*PHI_MOD)%P
def q2m(q):
    w,x,y,z=(red(c) for c in q); s=lambda c,M:((c*M[0][0])%P,(c*M[0][1])%P,(c*M[1][0])%P,(c*M[1][1])%P)
    a,b,cc,d=s(w,I_MAT),s(x,i_MAT),s(y,j_MAT),s(z,k_MAT)
    return tuple((a[t]+b[t]+cc[t]+d[t])%P for t in range(4))
def act(M,pt):
    x,y=pt; nx=(M[0]*x+M[1]*y)%P; ny=(M[2]*x+M[3]*y)%P
    if ny!=0: return ((nx*inv(ny))%P,1)
    return (1,0) if nx!=0 else None
pts=[(x,1) for x in range(P)]+[(1,0)]; idx={p:k for k,p in enumerate(pts)}
par=list(range(len(pts)))
def find(a):
    while par[a]!=a: par[a]=par[par[a]]; a=par[a]
    return a
for M in [q2m(u) for u in units]:
    for p in pts:
        q=act(M,p)
        if q in idx:
            ra,rb=find(idx[p]),find(idx[q])
            if ra!=rb: par[ra]=rb
orb={}
for k in range(len(pts)): orb.setdefault(find(k),[]).append(k)
orbits=sorted(orb.values(),key=len); which={k:oi for oi,o in enumerate(orbits) for k in o}

# (prime q, seed quaternion, nrd target a+b phi, point-count target set)
cases=[
 (11,((0,1),(1,0),(0,1),(0,0)),(3,2),{-4,4}),
 (19,((1,1),(1,1),(1,0),(0,0)),(5,6),{-4,4}),
 (29,((1,1),(0,1),(1,0),(1,0)),(5,4),{-2}),
 (41,((1,2),(1,0),(1,0),(0,0)),(7,8),{-6}),
]
print(f"{'q':>3} {'cosets':>6} {'rowsum':>6} {'eigenvalues':>16} {'Eis gate':>9} {'cusp':>5} {'target':>9} {'match':>6}")
allok=True
for q,seedint,tgt,pcs in cases:
    seed=tuple(Fp(a,b) for (a,b) in seedint)
    assert nrd(seed)==(Fraction(tgt[0]),Fraction(tgt[1])), (q,nrd(seed))
    TARGET=(Fraction(tgt[0]),Fraction(tgt[1]))
    pool=set()
    for u in units:
        us=qm(u,seed)
        for v in units:
            x=qm(us,v)
            if nrd(x)==TARGET: pool.add(tuple((c[0],c[1]) for c in x))
    pool=[tuple((Fraction(c[0]),Fraction(c[1])) for c in q_) for q_ in pool]
    reps=[]; seen=set()
    for a in pool:
        if tuple((c[0],c[1]) for c in a) in seen: continue
        for u in units: seen.add(tuple((c[0],c[1]) for c in qm(u,a)))
        reps.append(a)
    B=np.zeros((2,2)); hm=[q2m(a) for a in reps]
    for i,o in enumerate(orbits):
        xi=pts[o[0]]
        for M in hm:
            r=act(M,xi)
            if r in idx: B[i][which[idx[r]]]+=1
    ev=sorted(np.linalg.eigvals(B).real)
    eis = (q+1) in [round(e) for e in ev]
    cusp=[round(e) for e in ev if round(e)!=q+1]
    m = any(c in pcs for c in cusp)
    allok &= (eis and m and len(reps)==q+1 and all(abs(s-(q+1))<1e-9 for s in B.sum(1)))
    print(f"{q:>3} {len(reps):>6} {int(B.sum(1)[0]):>6} {str([round(e,2) for e in ev]):>16} "
          f"{'PASS' if eis else 'FAIL':>9} {str(cusp):>5} {str(sorted(pcs)):>9} {'YES' if m else 'NO':>6}")
print(f"\nALL out-of-sample primes: cosets=N(q)+1, Eisenstein gate, cuspidal matches point-count: {allok}")
