"""
Genuine icosian Brandt build, step 2: the Hecke operator T_{q1} at q=11 (split), on the
2-dim Brandt module from genus_level31.py. Cuspidal eigenvalue must match the point-count
a_P for norm 11 (= -4 or +4), out-of-sample, NO fitting.

Method: enumerate icosian quaternions of reduced norm pi_1 = 3+2phi (a totally-positive
generator of a prime over 11, even trace so it lies in the ring), dedupe to the 12 left-U
cosets (= the 12 right ideals of norm q1 = N(q1)+1). Reduce each mod p31 -> matrix in
GL_2(F31); act on the 2 orbits; build the 2x2 Brandt matrix; eigenvalues.
GATE: Eisenstein eigenvalue must equal N(q1)+1 = 12.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "route_b"))
from fractions import Fraction
import icosian as I

P=31; PHI_MOD=19; 
def zmul(a,b): 
    return I.zmf(a,b)
SUB=lambda a,b:(a[0]-b[0],a[1]-b[1]); ADD=lambda a,b:(a[0]+b[0],a[1]+b[1])
def qm(p,q): return I.qmul(p,q,I.zmf,ADD,SUB)
def nrd(q): return I.nrd(q,I.zmf,ADD,SUB)

F=lambda a,b=0:(Fraction(a),Fraction(b))
units=I.unit_icosians()
# seed of nrd = 3+2phi:  (phi,1,phi,0)
seed=(F(0,1),F(1,0),F(0,1),F(0,0))
assert nrd(seed)==(Fraction(3),Fraction(2)), nrd(seed)
TARGET=(Fraction(3),Fraction(2))

# pool of norm-pi1 elements: u * seed * u'
pool=set()
for u in units:
    us=qm(u,seed)
    for v in units:
        x=qm(us,v)
        if nrd(x)==TARGET:
            pool.add(tuple((c[0],c[1]) for c in x))
print(f"norm-(3+2phi) icosian quaternions found: {len(pool)}")

# dedupe by LEFT unit equivalence: alpha ~ u*alpha  -> right ideals O*alpha
pool=[tuple((Fraction(c[0]),Fraction(c[1])) for c in q) for q in pool]
reps=[]; seen=set()
for a in pool:
    key=tuple((c[0],c[1]) for c in a)
    if key in seen: continue
    # mark all u*a
    for u in units:
        ua=qm(u,a); seen.add(tuple((c[0],c[1]) for c in ua))
    reps.append(a)
print(f"left-U cosets (= right ideals of norm q1, expect N(q1)+1 = 12): {len(reps)}")

# --- reduce mod p31 and act on the 2 orbits (recompute orbits) ---
inv=lambda d: pow(d%P,P-2,P)
def red(fp):
    a,b=fp
    def rf(fr): return (fr.numerator%P)*pow(fr.denominator%P,P-2,P)%P
    return (rf(a)+rf(b)*PHI_MOD)%P
I_MAT=((1,0),(0,1)); i_MAT=((0,1),(P-1,0)); j_MAT=((5,6),(6,26)); k_MAT=((6,26),(26,25))
def q2m(q):
    w,x,y,z=(red(c) for c in q)
    def s(c,M): return ((c*M[0][0])%P,(c*M[0][1])%P,(c*M[1][0])%P,(c*M[1][1])%P)
    a=s(w,I_MAT); b=s(x,i_MAT); cc=s(y,j_MAT); d=s(z,k_MAT)
    return tuple((a[t]+b[t]+cc[t]+d[t])%P for t in range(4))
def act(M,pt):
    x,y=pt; nx=(M[0]*x+M[1]*y)%P; ny=(M[2]*x+M[3]*y)%P
    if ny!=0: return ((nx*inv(ny))%P,1)
    return (1,0) if nx!=0 else None
# orbits of the unit group (from genus step)
umats=[q2m(u) for u in units]
pts=[(x,1) for x in range(P)]+[(1,0)]; idx={p:k for k,p in enumerate(pts)}
par=list(range(len(pts)))
def find(a):
    while par[a]!=a: par[a]=par[par[a]]; a=par[a]
    return a
for M in umats:
    for p in pts:
        q=act(M,p)
        if q in idx:
            ra,rb=find(idx[p]),find(idx[q])
            if ra!=rb: par[ra]=rb
orb={}
for k in range(len(pts)): orb.setdefault(find(k),[]).append(k)
orbits=list(orb.values()); orbits.sort(key=len)
which={}
for oi,o in enumerate(orbits):
    for k in o: which[k]=oi
print(f"orbits sizes: {[len(o) for o in orbits]}")

# Brandt matrix: B[i][j] = # of the 12 reps alpha with alpha . (rep point of orbit i) in orbit j
import numpy as np
B=np.zeros((2,2))
hmats=[q2m(a) for a in reps]
for i,o in enumerate(orbits):
    x_i=pts[o[0]]
    for M in hmats:
        q=act(M,x_i)
        if q in idx: B[i][ which[idx[q]] ]+=1
print("Brandt matrix B(q1) on the 2 orbits:\n", B.astype(int))
print("row sums (must be 12):", B.sum(1).astype(int))
evals=sorted(np.linalg.eigvals(B).real)
print("eigenvalues:", [round(e,3) for e in evals])
eis = 12 in [round(e) for e in evals]
cusp=[round(e) for e in evals if round(e)!=12]
print(f"\nGATE Eisenstein eigenvalue == 12: {'PASS' if eis else 'FAIL'}")
print(f"cuspidal eigenvalue candidate: {cusp}   (point-count target for norm 11: -4 or +4)")
match = any(c in (-4,4) for c in cusp)
print(f"GATE cuspidal matches point-count a_P in {{-4,+4}}: {'PASS -> GEOMETRY GENERATES a_q OUT OF SAMPLE' if match else 'no'}")
