"""WO-VFD-RH-SIMPLEX-WITNESS-KERNEL-SEARCH-001 — can a simplex-derived positive form A
produce the archimedean completion K_inf(s)=pi^{-s/2}Gamma(s/2) that restores the
zeta functional equation? Honest math anchor: pi^{-s/2}Gamma(s/2) is the Mellin of the
1-D SCALING heat kernel (Jacobi theta of Z); a d-dim form A gives the EPSTEIN zeta of A
(Gamma(s/2) universal from the scaling variable, but completing Z_A not zeta, with
involution s<->d-s and a det(A)^{-s/2} scale that is symmetric ONLY if det A=1 / A
self-dual). Test: self-duality of simplex Grams + FE residual of K_A*zeta."""
import numpy as np, mpmath as mp, math, json
mp.mp.dps=25
PHI=(1+5**0.5)/2
# ---- controls (regression from COMPLETION-KERNEL-001) ----
def fe_residual(K, sig_list, t_list):
    res=[]
    for sig in sig_list:
        for t in t_list:
            s=mp.mpc(sig,t)
            a=K(s); b=K(1-s)
            res.append(float(abs(a-b)/(abs(a)+abs(b)+mp.mpf(10)**-40)))
    import statistics as st
    return dict(median=st.median(res), max=max(res), frac_below_1e6=sum(1 for r in res if r<1e-6)/len(res))
SIG=[0.1,0.2,0.3,0.4,0.6,0.7,0.8,0.9]; T=[2,10,30,60,100]
zeta=lambda s: mp.zeta(s)
controls={
 "raw zeta":               lambda s: zeta(s),
 "K_inf=pi^-s/2 Gamma(s/2)":lambda s: mp.pi**(-s/2)*mp.gamma(s/2)*zeta(s),
 "WRONG Gamma(s/3)":        lambda s: mp.pi**(-s/2)*mp.gamma(s/3)*zeta(s),
 "FAKE exp(0.7 s)":         lambda s: mp.e**(mp.mpf(7)/10*s)*mp.gamma(s/2)*zeta(s),
}
print("="*76); print("WO-VFD-RH-SIMPLEX-WITNESS-KERNEL-SEARCH-001"); print("="*76)
print("\n[Layer 1: controls] (regression)")
for n,K in controls.items():
    r=fe_residual(K,SIG,T); print(f"  {n:28}: median R_FE={r['median']:.2e}  {'PASS' if r['median']<1e-8 else 'FAIL'}")

# ---- simplex-derived positive forms ----
def cartan_A(d):      # Gram of the regular d-simplex edges (A_d Cartan): 2 diag, -1 adjacent
    M=2*np.eye(d)
    for i in range(d-1): M[i,i+1]=M[i+1,i]=-1
    return M
def complete_lap(d):  # graph Laplacian of K_{d+1} restricted to d-dim (deg d, off -1)
    n=d+1; L=n*np.eye(n)-np.ones((n,n)); 
    return L[:d,:d]+np.eye(d)*0   # principal dxd block (SPD)
def phi_weighted(d):  # phi-perturbed simplex Gram
    M=cartan_A(d).copy()
    for i in range(d-1): M[i,i+1]=M[i+1,i]=-1/PHI
    return M
def selfdual_score(A):
    Ai=np.linalg.inv(A)
    nA=A/np.trace(A); nAi=Ai/np.trace(Ai)
    return float(np.linalg.norm(nA-nAi))
print("\n[Layer 2: simplex self-duality + det]  (self-dual <=> A ~ A^-1; needed for a clean single-object FE)")
print(f"  {'form':22}{'d':>3}{'det(A)':>10}{'self-duality score':>20}  {'self-dual?'}")
forms=[]
for d in [2,3,4,5,6,8]:
    for name,fn in [("simplex Gram A_d",cartan_A),("K_{d+1} Laplacian",complete_lap),("phi-simplex",phi_weighted)]:
        A=fn(d); 
        if np.min(np.linalg.eigvalsh(A))<=0: continue
        det=float(np.linalg.det(A)); sd=selfdual_score(A); forms.append((name,d,A,det,sd))
        print(f"  {name:22}{d:>3}{det:>10.3f}{sd:>20.4f}  {'YES' if sd<1e-6 else 'no'}")
# the self-dual control: identity (= 1-D lattice Z, the arithmetic of Q)
A_id=np.eye(3); print(f"  {'identity (Z lattice)':22}{3:>3}{1.0:>10.3f}{selfdual_score(A_id):>20.4f}  {'YES (self-dual)'}")
print("  -> regular simplex Grams are NOT self-dual (det != 1, score > 0). Only the trivial")
print("     identity/Z lattice is self-dual -- and that is the 1-D scaling/arithmetic of Q, NOT a simplex.")

# ---- Layer 2b: the Gamma(s/2) factor is UNIVERSAL (scaling Mellin), det enters as an ASYMMETRIC scale ----
print("\n[Layer 2b: FE residual of K_A*zeta], K_A(s)=pi^{-s/2}Gamma(s/2) det(A)^{-s/2}")
print("  (natural Gaussian-Mellin completion carrying the simplex's scale det(A)):")
for name,d,A,det,sd in forms[:6]+[("identity det=1",3,A_id,1.0,0.0)]:
    K=lambda s,det=det: mp.pi**(-s/2)*mp.gamma(s/2)*mp.mpf(det)**(-s/2)*zeta(s)
    r=fe_residual(K,SIG,T)
    print(f"  {name:22} d={d} det={det:7.3f}: median R_FE={r['median']:.2e}  {'PASS' if r['median']<1e-8 else 'FAIL'}")
print("  -> PASSES iff det(A)=1. The det(A)^{-s/2} factor is asymmetric under s<->1-s unless det=1.")
print("     Gamma(s/2) (the scaling Mellin) is dimension-INDEPENDENT -> it is NOT what the simplex")
print("     supplies; the simplex supplies det(A) and dimension d, which BREAK the zeta FE.")

print("""
----------------------------------------------------------------------
VERDICT: FAIL (and useful). Simplex/tetrahedral geometry does NOT naturally
produce the archimedean completion pi^{-s/2}Gamma(s/2) for zeta.
 * The Gamma(s/2) factor is the Mellin of the 1-D SCALING heat kernel (Jacobi
   theta of Z) -- universal, dimension-independent; ANY Gaussian gives it. It is
   not a simplex feature.
 * A d-dim simplex form A gives the EPSTEIN zeta of A (not zeta), with involution
   s<->d-s and a det(A)^{-s/2} scale; the zeta FE (s<->1-s) is recovered ONLY for
   the 1-D self-dual lattice Z (det=1, self-duality score 0) -- which is the
   arithmetic of Q / the scaling action at the place at infinity, NOT a simplex.
 * Regular simplex Grams are not self-dual (det != 1) and FAIL the FE residual.
=> The witness space is the SCALE / ADELE action on Q (self-dual 1-D), with the
   simplex at most a symbolic projection. Tetrahedral geometry is not enough --
   exactly the missing-substrate conclusion of the prior WOs (the place at infinity
   / arithmetic site), now confirmed from the geometry side. No RH proof; no claim
   a simplex yields the completion.
----------------------------------------------------------------------""")
json.dump(dict(work_order="WO-VFD-RH-SIMPLEX-WITNESS-KERNEL-SEARCH-001",
  controls={n:fe_residual(K,SIG,T)['median'] for n,K in controls.items()},
  simplex_self_duality=[{"form":f[0],"d":f[1],"det":f[3],"selfdual_score":f[4]} for f in forms],
  finding="Gamma(s/2)=universal 1-D scaling Mellin (dimension-independent); simplex supplies det(A)+dimension which give the EPSTEIN zeta (s<->d-s) not zeta; zeta FE recovered ONLY for self-dual 1-D Z (det=1). Regular simplex Grams not self-dual -> FAIL FE.",
  verdict="FAIL-useful: simplex/tetrahedral geometry does NOT produce the zeta archimedean completion; the witness space is the scale/adele action on Q (self-dual 1-D place at infinity), simplex only symbolic. Confirms the missing-substrate finding from the geometry side.",
  no_overclaim="no RH proof; no claim a simplex yields the completion kernel"),
  open("results/result.json","w"), indent=2)
print("[json] results/result.json")
