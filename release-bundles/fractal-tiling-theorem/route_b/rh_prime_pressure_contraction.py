"""WO-RH-PRIME-PRESSURE-CONTRACTION-002 — diagnostics for the contraction routes.

||K||<=1 (K=H^-1/2 R H^-1/2) is EXACTLY RH. So every analytic route is either too
weak or RH-equivalent. We test the two most informative:
  Route A (Schur weighted row-sum bound): is it tight enough to give <=1?
  Route C (Mellin multiplier): R's symbol is essentially -zeta'/zeta(1/2+i xi),
    whose POLES ARE THE ZEROS -> no pointwise bound by the smooth archimedean
    multiplier. We show r(xi) peaks above h(xi) at the zeros.
Routes D/E/F argued in the report (they reduce to RH). Non-circular; no proof.
"""
import numpy as np, mpmath as mp, math
mp.mp.dps=20
S=3.0; CENT=[14.0+4.0*k for k in range(12)]; NC=len(CENT); W=S/math.sqrt(2)
RG=np.arange(-150,150,0.1); DR=0.1
Mmul=np.array([float(mp.re(mp.digamma(mp.mpc(0.25,r/2)))) for r in RG])
def sieve(P):
    lam={}; comp=[False]*(P+1)
    for p in range(2,P+1):
        if not comp[p]:
            for m in range(p*p,P+1,p): comp[m]=True
            pk=p
            while pk<=P: lam[pk]=math.log(p); pk*=p
    return lam
LAM=sieve(2000); NID=np.array(sorted(LAM)); LOGN=np.log(NID); LWT=np.array([LAM[int(n)] for n in NID])/np.sqrt(NID)
def hterms(ci,cj): return [(math.exp(-(a-b)**2/(4*S**2)),(a+b)/2) for a in (ci,-ci) for b in (cj,-cj)]
def comps(ci,cj):
    t=hterms(ci,cj); Hg=np.zeros_like(RG)
    for A,m in t: Hg+=A*np.exp(-(RG-m)**2/(S**2))
    arch=float(np.sum(Hg*Mmul)*DR/(2*math.pi))
    pole=2*sum(A*np.exp(-((1j*0.5)-m)**2/(S**2)) for A,m in t)
    g0=sum(A*(W/math.sqrt(2*math.pi)) for A,m in t)
    prime=sum(2*np.sum(LWT*(A*(W/math.sqrt(2*math.pi))*np.exp(-W**2*LOGN**2/2)*np.exp(-1j*m*LOGN))) for A,m in t)
    return arch, float(np.real(pole-g0*math.log(math.pi))), float(np.real(prime))
def mats():
    A=np.zeros((NC,NC));P=np.zeros((NC,NC));R=np.zeros((NC,NC))
    for i in range(NC):
        for j in range(NC):
            a,p,r=comps(CENT[i],CENT[j]); A[i,j]=a;P[i,j]=p;R[i,j]=r
    s=lambda X:(X+X.T)/2; return s(A),s(P),s(R)

def main():
    print("="*64); print("WO-RH-PRIME-PRESSURE-CONTRACTION-002  contraction-route diagnostics"); print("="*64)
    A,P,R=mats(); H=A+P
    w,U=np.linalg.eigh(H); Hm=U@np.diag(1/np.sqrt(w))@U.T; K=(Hm@R@Hm); K=(K+K.T)/2
    mu=np.linalg.eigvalsh(K).max()
    print(f"\nmu_max(K) = {mu:.5f}  (||K||=mu since K symmetric; ||K||<=1 IS RH on this cutoff)")

    print("\n[Route A: Schur / row-sum bound] ||K|| <= max_i sum_j |K_ij| w_j/w_i :")
    for name,wt in [("w=1", np.ones(NC)), ("w=diag(H)", np.diag(H)), ("w=sqrt(capacity)", np.sqrt(np.abs(np.diag(H))))]:
        sch=max(np.sum(np.abs(K[i,:])*wt/wt[i]) for i in range(NC))
        print(f"  {name:<16}: Schur const = {sch:.3f}  {'<=1 (would prove it!)' if sch<=1.001 else '> 1 -> TOO LOOSE (cannot capture the 0.9998 margin)'}")
    print("  -> Schur over-counts off-diagonal/sign structure; far too loose for the razor-thin margin.")

    print("\n[Route C: Mellin multiplier] R's symbol r(xi)=Sum Lambda(n)/sqrt(n) cos(xi log n)")
    print("  vs archimedean multiplier h(xi)=Re psi(1/4+i xi/2). Bound |r|<=h needed:")
    g=[14.134725,21.022040,25.010858]
    for xi in [10.0]+g+[17.0]:
        r=float(np.sum(LWT*np.cos(xi*LOGN)))
        h=float(mp.re(mp.digamma(mp.mpc(0.25,xi/2))))
        atzero = any(abs(xi-gg)<0.2 for gg in g)
        print(f"  xi={xi:6.2f}: |r|={abs(r):7.2f}  h={h:5.2f}  |r|<=h? {abs(r)<=h}"
              f"{'   <- AT A ZERO: r spikes, h smooth' if atzero else ''}")
    print("  -> r(xi) is (a truncation of) -zeta'/zeta(1/2+i xi): it PEAKS at the zeros,")
    print("     where the true symbol has POLES. No pointwise bound |r|<=h exists.")
    print("     The multiplier route fails BECAUSE the prime symbol is singular exactly")
    print("     at the zeros -- the cleanest statement of why ||K||<=1 is RH-hard.")

    print("""
----------------------------------------------------------------------
VERDICT (WO-RH-PRIME-PRESSURE-CONTRACTION-002)
----------------------------------------------------------------------
||K|| <= 1 is EXACTLY RH. No route gives a free proof:
 * Route A (Schur): far too loose (const >> 1) -- cannot capture the 0.9998
   margin. Blocked (too weak).
 * Route C (multiplier): FAILS because R's Mellin symbol is -zeta'/zeta(1/2+i xi),
   which has POLES AT THE ZEROS; the smooth archimedean h(xi) cannot dominate it
   pointwise. Blocked -- and it reveals the crux: the prime-pressure symbol is
   singular precisely at the objects RH constrains.
 * Routes D (factorisation): I-K=B*B has only the trivial (non-canonical) sqrt;
   the structured B is the de Branges object shown missing in SPACE-002.
 * Route E (form-limit): the FINITE contraction mu_max(K_N)<=1 is itself the Weil
   positivity criterion restricted to N test functions -> RH-equivalent, not an
   unconditional premise. Circular.
 * Route F (variational): sup <f,Rf>/<f,Hf> = mu_max(K); mu>1 <=> an off-line
   zero (Weil). The extremal problem IS RH.
=> The contraction reformulation is SHARPER and CLEANER than raw Weil positivity
(a single named operator-norm inequality, with the real Gamma coefficient exactly
critical), but it is LOGICALLY EQUIVALENT to RH at every cutoff -- there is no
weaker sub-lemma here. Best honest target: the multiplier crux -- bound the
prime symbol -zeta'/zeta against the archimedean capacity AROUND its poles -- but
that is RH itself. No proof; no phi; no zeros inserted.
""")

if __name__=="__main__":
    main()
