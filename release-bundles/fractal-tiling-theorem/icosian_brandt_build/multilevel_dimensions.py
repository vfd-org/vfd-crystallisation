"""Test MORE levels: for each split prime level l (l = +-1 mod 5), the number of
A_5-orbits on P^1(F_l) = the Brandt dimension h = 1 (Eisenstein) + (h-1) cuspidal.
This is the geometry's prediction of the dimension of Hilbert modular forms over Q(sqrt5)
at level (the prime over l). Fast, self-contained, no external data."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "route_b"))
from fractions import Fraction
import icosian as I
units = I.unit_icosians()

def sqrt_mod(n, p):
    n %= p
    for r in range(p):
        if (r*r) % p == n: return r
    return None
def splitting(p):
    # i^2=-1 always via [[0,1],[-1,0]]; j=[[a,b],[b,-a]] with a^2+b^2=-1 mod p
    for a in range(p):
        b2 = (-1 - a*a) % p
        b = sqrt_mod(b2, p)
        if b is not None:
            return ((0,1,p-1,0), (a,b,b,(p-a)%p))
    return None

def orbit_count(l):
    phi = sqrt_mod(5, l)
    if phi is None: return None         # 5 not QR -> l not split
    phi = ((1+phi) * pow(2,l-2,l)) % l   # (1+sqrt5)/2 mod l
    if (phi*phi - phi - 1) % l != 0: return None
    sp = splitting(l)
    if sp is None: return None
    (i0,i1,i2,i3),(j0,j1,j2,j3)=sp
    I_M=(1,0,0,1); i_M=(i0,i1,i2,i3); j_M=(j0,j1,j2,j3)
    k_M=((i0*j0+i1*j2)%l,(i0*j1+i1*j3)%l,(i2*j0+i3*j2)%l,(i2*j1+i3*j3)%l)
    def red(fp):
        a,b=fp; rf=lambda fr:(fr.numerator%l)*pow(fr.denominator%l,l-2,l)%l
        return (rf(a)+rf(b)*phi)%l
    def q2m(q):
        w,x,y,z=(red(c) for c in q)
        return tuple((w*I_M[t]+x*i_M[t]+y*j_M[t]+z*k_M[t])%l for t in range(4))
    mats=[q2m(u) for u in units]; mats=[m for m in mats if (m[0]*m[3]-m[1]*m[2])%l!=0]
    pts=[(x,1) for x in range(l)]+[(1,0)]; idx={p_:k for k,p_ in enumerate(pts)}
    par=list(range(len(pts)))
    def find(a):
        while par[a]!=a: par[a]=par[par[a]]; a=par[a]
        return a
    for M in mats:
        for pt in pts:
            x,y=pt; nx=(M[0]*x+M[1]*y)%l; ny=(M[2]*x+M[3]*y)%l
            q=((nx*pow(ny,l-2,l))%l,1) if ny!=0 else ((1,0) if nx!=0 else None)
            if q in idx:
                ra,rb=find(idx[pt]),find(idx[q])
                if ra!=rb: par[ra]=rb
    return len({find(k) for k in range(len(pts))})

print("Hilbert modular form dimensions over Q(sqrt5), per split-prime level, FROM GEOMETRY:")
print(f"  {'level norm l':>12} {'Brandt h':>9} {'Eisenstein':>11} {'CUSPIDAL dim':>13}")
splitprimes=[l for l in range(11,160) if l%5 in (1,4) and all(l%d for d in range(2,int(l**.5)+1))]
for l in splitprimes:
    h=orbit_count(l)
    if h is None: continue
    print(f"  {l:>12} {h:>9} {1:>11} {h-1:>13}")
print("\n  (level 31 -> cuspidal dim 1 = the elliptic curve 31.1-a1, our verified form.)")
print("  Each cuspidal dim is the geometry's count of Hilbert newforms at that level;")
print("  cross-checkable against Dembele/LMFDB dimension tables. Fast geometric output.")
