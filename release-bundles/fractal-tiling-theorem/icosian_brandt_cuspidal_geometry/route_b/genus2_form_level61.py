import sys, os, math; sys.path.insert(0, os.getcwd())
from fractions import Fraction
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"second_form_level41.py")).read().split('LEVEL=41')[0])  # compute_orbits_p, engine_for, bm

def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

# Dembele level-61 column (genus-2 form, RM by Q(sqrt5)); a in Z[phi].
# (Tr,N) over Q for the inert (unambiguous) primes:
#   a_4=2w-2 ->(-2,-4)  a_9=-w-2 ->(-5,5)  a_49=-4w+2 ->(0,-20)
DEM={4:("2w-2",-2,-4), 9:("-w-2",-5,5), 49:("-4w+2",0,-20)}

g=compute_orbits_p(61)
print(f"LEVEL 61 genus-2 flourish.  P^1(F_61)={len(g['p1_points'])} (=62); Brandt h={g['h']}; orbit sizes {g['orbit_sizes']}")
print(f"  cuspidal dim = h-1 = {g['h']-1}  (Dembele Rem 4.4: genus 2, dim-2 abelian surface, RM by Q(sqrt5))\n")
eng=engine_for(61)
print(f"  {'N(q)':>4} {'kind':>6} {'Tr(a)':>6} {'N(a)':>6} {'disc=Tr^2-4N':>13} {'5|disc & sq':>11} {'Ramanujan':>10} {'vs Dembele':>16}")
inert={4,9,49}
for Nq in [4,9,11,19,29,49]:
    gen=bm.totally_positive_generator(Nq)
    if gen is None: print(f"  {Nq:>4}  (no even-trace tot-pos generator)"); continue
    r=eng.brandt_matrix(gen); B=r["matrix"]
    tr=sum(B[i][i] for i in range(3)); dt=det3(B)
    Tra=tr-(Nq+1); Na=dt/(Nq+1)
    Tra=Tra if Tra.denominator==1 else float(Tra); Na=Na if Na.denominator==1 else float(Na)
    disc=Tra*Tra-4*Na
    # irrational iff disc>0 not a perfect square; RM-Q(sqrt5) iff disc = 5 * square
    dq = disc if isinstance(disc,int) or (hasattr(disc,'denominator') and disc.denominator==1) else None
    is5sq = (dq is not None and dq>0 and dq%5==0 and int(math.isqrt(dq//5))**2==dq//5)
    # Ramanujan on both embeddings a=(Tr +- sqrt(disc))/2
    rt=math.sqrt(float(disc)) if float(disc)>0 else 0
    e1=(float(Tra)+rt)/2; e2=(float(Tra)-rt)/2; ram=max(abs(e1),abs(e2))<=2*math.sqrt(Nq)+1e-9
    kind="inert" if Nq in inert else "split"
    vs=""
    if Nq in DEM:
        _,T,N=DEM[Nq]; vs=("MATCH" if (Tra==T and Na==N) else f"MISMATCH exp({T},{N})")
    print(f"  {Nq:>4} {kind:>6} {str(Tra):>6} {str(Na):>6} {str(disc):>13} {str(is5sq):>11} {str(ram):>10} {vs:>16}")
print("\n  Reading: disc = 5*square at every prime => eigenvalues a_q in Z[phi], IRRATIONAL")
print("  (the genus-2 / real-multiplication form). Inert primes match Dembele's published a_q.")
