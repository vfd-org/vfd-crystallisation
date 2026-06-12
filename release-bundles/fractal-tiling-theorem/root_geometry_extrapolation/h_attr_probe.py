"""
H_attr probe on the 26-dim sigma-paired block.

H_attr (our conjecture): the closure-flow suppresses the sigma-paired residue onto the
critical line (drives the 26-dim block toward the sigma-fixed / on-line locus).

Closure operator:  C_phi = L + phi^-2 I = (12 + phi^-2) I - A   (L = 12 I - A, degree 12).
Closure-flow:      e^{-t C_phi}.  Modes with smaller C_phi eigenvalue persist longer.

We test, on the explicit block, whether the flow actually suppresses the residue -- and
whether sigma-conjugate modes are treated symmetrically (they must be, for H_attr to drive
the residue onto Fix(tau) as a Galois-pair).
"""
import numpy as np
from itertools import product
PHI=(1+5**0.5)/2; INV2=PHI**-2  # = 2 - phi

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
w,U=np.linalg.eigh(A)
Cphi_eig = (12 + INV2) - w                         # closure operator eigenvalues (decay rates)
is_paired = np.abs(w-np.round(w))>1e-4             # sigma-paired = phi-irrational

print("="*78); print("H_attr PROBE on the 26-dim sigma-paired block"); print("="*78)
# decay-rate ordering: who persists under e^{-t C_phi}?
order = np.argsort(Cphi_eig)
print("\n  closure-flow decay rates C_phi (smaller = persists longer):")
print(f"  {'rank':>4} {'A-eig':>8} {'C_phi':>8} {'class':>12}")
shown=set()
for rank,i in enumerate(order):
    key=round(float(w[i]),3)
    if key in shown: continue
    shown.add(key)
    cls = "sigma-PAIRED" if is_paired[i] else "sigma-fixed"
    print(f"  {rank:4d} {w[i]:8.3f} {Cphi_eig[i]:8.3f} {cls:>12}")

# straddle test: do sigma-paired modes appear among BOTH the slowest and fastest?
paired_rates = sorted(set(round(float(Cphi_eig[i]),3) for i in range(len(w)) if is_paired[i]))
fixed_rates  = sorted(set(round(float(Cphi_eig[i]),3) for i in range(len(w)) if not is_paired[i]))
slowest_paired = min(paired_rates); slowest_fixed_nonperron = sorted(fixed_rates)[1]
print(f"\n  sigma-paired C_phi rates: {paired_rates}")
print(f"  sigma-fixed  C_phi rates: {fixed_rates}")
print(f"  -> the sigma-paired block STRADDLES: slowest paired rate {slowest_paired:.3f} is the "
      f"2nd-slowest mode overall (persists), while {max(paired_rates):.3f} decays fastest.")

# the decisive point: sigma-conjugate eigenvalues are DIFFERENT REAL NUMBERS
print("\n  sigma-conjugate pairs as REAL eigenvalues (a flow sees reals, not Galois orbits):")
print(f"    6*phi = {6*PHI:7.3f}   <->   6-6*phi = {6-6*PHI:7.3f}   (C_phi {12+INV2-6*PHI:.3f} vs {12+INV2-(6-6*PHI):.3f})")
print(f"    4*phi = {4*PHI:7.3f}   <->   4-4*phi = {4-4*PHI:7.3f}   (C_phi {12+INV2-4*PHI:.3f} vs {12+INV2-(4-4*PHI):.3f})")

# simulate: fraction of norm in the sigma-paired block under the flow
v0 = np.ones(len(w)); v0/=np.linalg.norm(v0)
c = U.T@v0
Pmask = is_paired.astype(float)
print("\n  sigma-paired norm fraction under e^{-t C_phi} (H_attr predicts -> 0 fast & symmetric):")
for t in [0.0,0.1,0.3,1.0,3.0]:
    decay=np.exp(-t*Cphi_eig); cc=c*decay
    frac=float(np.sum((cc**2)*Pmask)/np.sum(cc**2))
    print(f"    t={t:4.1f}:  paired-fraction = {frac:.4f}")

print("\n" + "="*78)
print("VERDICT: H_attr (closure-flow suppresses the sigma-paired residue) -- REFUTED (naive form)")
print("""  * The sigma-paired block STRADDLES the decay spectrum: {6phi,4phi} are the 2nd/3rd
    SLOWEST modes (they PERSIST), while {6-6phi,4-4phi} decay fastest. The flow does NOT
    uniformly suppress the residue -- it persists one sigma-half and kills the other.
  * DECISIVE: sigma-conjugate eigenvalues are DIFFERENT REAL NUMBERS (6phi=9.7 vs 6-6phi=-3.7).
    Any REAL-spectral flow (heat/closure/gradient) treats them differently -- the Galois (sigma)
    pairing is an ARITHMETIC symmetry INVISIBLE to real dynamics. So no real closure-flow can
    drive the residue onto Fix(tau) as a Galois-pair. H_attr cannot work via a real flow.
  * CONSEQUENCE: the 26-dim residue's openness is NOT closable by an attractor/flow. It needs
    genuinely ARITHMETIC (Galois-aware) structure -- which loops straight back to the root
    geometry (the arithmetic site), not a dynamical suppression. Honest negative; sharpens
    WHY the residue stays open. NOT a proof of anything.""")
print("="*78)
