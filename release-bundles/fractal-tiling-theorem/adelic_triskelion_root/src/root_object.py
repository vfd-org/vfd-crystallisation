"""WO-VFD-ADELIC-TRISKELION-ROOT-OBJECT-001 — test the Adelic Triskelion AT=(F,A∞,S,W,I)
as a TESTABLE root object: does each arm reproduce a real piece of the completed-zeta
pipeline, and is each NECESSARY? Honest anchor: this is exactly Riemann(1859)/Tate's
completed-zeta construction (Euler product + Gaussian/Γ + theta self-duality => FE) re-
encoded as a 3-arm normal form. KNOWN math verified, NOT new, NOT a proof of RH."""
import mpmath as mp, math, json
mp.mp.dps=30
def primes_up_to(P):
    out=[]; comp=[False]*(P+1)
    for n in range(2,P+1):
        if not comp[n]:
            out.append(n)
            for m in range(n*n,P+1,n): comp[m]=True
    return out
# ---- Stage 1: finite arm = Euler product ----
def finite_arm(s, P=20000):
    ps=primes_up_to(P); prod=mp.mpf(1)
    for p in ps: prod*= 1/(1-mp.mpf(p)**(-s))
    return prod, abs(prod-mp.zeta(s))/abs(mp.zeta(s))
# ---- Stage 2: archimedean arm = Gaussian Mellin -> 1/2 pi^-s/2 Gamma(s/2) ----
def archimedean_arm(s):
    I=mp.quad(lambda x: mp.e**(-mp.pi*x**2)*x**(s-1), [0,mp.inf])
    target=mp.mpf(1)/2*mp.pi**(-s/2)*mp.gamma(s/2)
    return I, abs(I-target)/abs(target)
# ---- Stage 3: scale arm = theta self-duality theta(t)=t^-1/2 theta(1/t) ----
def theta(t, N=200): return mp.nsum(lambda n: mp.e**(-mp.pi*n**2*t), [-N,N])
def theta_duality(t):
    lhs=theta(t); rhs=t**(mp.mpf(-1)/2)*theta(1/t)
    return abs(lhs-rhs)/abs(lhs)
# ---- Stage 4 + controls + removals: FE residual ----
def fe_residual(K, sig=(0.1,0.2,0.3,0.4,0.6,0.7,0.8,0.9), ts=(2,10,30,60,100)):
    import statistics as st; res=[]
    for s0 in sig:
        for t in ts:
            s=mp.mpc(s0,t); a=K(s); b=K(1-s)
            res.append(float(abs(a-b)/(abs(a)+abs(b)+mp.mpf(10)**-40)))
    return st.median(res)
zeta=lambda s: mp.zeta(s)
def random_dirichlet(seed=5, M=4000):
    import random; r=random.Random(seed); a=[0,0]+[r.choice([-1,1])*(1+r.random()) for _ in range(M)]
    def D(s): return mp.nsum(lambda n: a[int(n)]*mp.mpf(int(n))**(-s) if int(n)<len(a) else 0,[2,M])
    return D
