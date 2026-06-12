"""WO-VFD-RH-POSITIVE-ADELIC-WITNESS-OPERATOR-001 — core.
Honest scaffold for the positive witness operator at the centre of the Adelic Triskelion.
This is the Weil/Connes positivity criterion (KNOWN) re-encoded in witness-operator
language; finite-cutoff positivity is NOT a proof of RH (the near-null mode is the wall)."""
import numpy as np, mpmath as mp, math
mp.mp.dps=20
# ---------- Stage A: witness space + involution J ----------
def witness_grid(U=8.0, N=512):
    u=np.linspace(-U,U,N); return u, u[1]-u[0]
def involution_apply(f):                # (Jf)(u)=f(-u)
    return f[::-1]
def even_odd_split(f):
    Jf=f[::-1]; return (f+Jf)/2, (f-Jf)/2
# ---------- Stage B: scale generator D=-i d/du ----------
def scale_generator(N, du):
    # central-difference -i d/du; super-diag = conj(sub-diag) -> Hermitian by construction
    off=np.ones(N-1)/(2*du)
    return np.diag(-1j*off,1)+np.diag(1j*off,-1)
# ---------- Stage C: completed-kernel regression ----------
def gaussian_mellin(s):
    I=mp.quad(lambda x: mp.e**(-mp.pi*x**2)*x**(s-1),[0,mp.inf])
    tgt=mp.mpf(1)/2*mp.pi**(-s/2)*mp.gamma(s/2); return abs(I-tgt)/abs(tgt)
def theta_duality(t,Nn=200):
    th=lambda tt: mp.nsum(lambda n: mp.e**(-mp.pi*n**2*tt),[-Nn,Nn])
    return abs(th(t)-t**(mp.mpf(-1)/2)*th(1/t))/abs(th(t))
def fe_residual(K,sig=(0.2,0.4,0.6,0.8),ts=(4,20,60)):
    import statistics as st; r=[]
    for s0 in sig:
        for t in ts:
            s=mp.mpc(s0,t); a=K(s); b=K(1-s); r.append(float(abs(a-b)/(abs(a)+abs(b)+mp.mpf(10)**-40)))
    return st.median(r)
# ---------- Stage D: Riemann-Weil explicit-formula balance ----------
def explicit_formula_balance(sigma=1.0, Nz=40, P=3000, lam_weights=None):
    g0=lambda u: math.exp(-u*u/(2*sigma**2))
    h=lambda r: sigma*math.sqrt(2*math.pi)*math.exp(-sigma**2*r*r/2)
    zeros=[float(mp.im(mp.zetazero(k))) for k in range(1,Nz+1)]
    ZeroSide=2*sum(h(g) for g in zeros)
    PoleSide=2*sigma*math.sqrt(2*math.pi)*math.exp(sigma**2/8)        # 2 h(i/2)
    rg=np.arange(-200,200,0.05)
    Hr=sigma*math.sqrt(2*math.pi)*np.exp(-sigma**2*rg**2/2)
    Mr=np.array([float(mp.re(mp.digamma(mp.mpc(0.25,r/2)))) for r in rg])
    ArchSide=float(np.sum(Hr*Mr)*0.05/(2*math.pi))
    # primes / von Mangoldt
    lam={}; comp=[False]*(P+1)
    for p in range(2,P+1):
        if not comp[p]:
            for m in range(p*p,P+1,p): comp[m]=True
            pk=p
            while pk<=P: lam[pk]=math.log(p); pk*=p
    if lam_weights=="shuffle":
        import random; rnd=random.Random(3); ks=list(lam); vs=[lam[k] for k in ks]; rnd.shuffle(vs); lam=dict(zip(ks,vs))
    PrimeSide=2*sum(lam[n]/math.sqrt(n)*g0(math.log(n)) for n in lam)
    ConstSide=math.log(math.pi)*g0(0.0)
    rhs=PoleSide+ArchSide-PrimeSide-ConstSide
    return dict(ZeroSide=ZeroSide, rhs=rhs, residual=abs(ZeroSide-rhs)/abs(ZeroSide))
# ---------- Stage E/F: Weil positivity form (route_b A+P-R) ----------
def weil_form(NC=12, S=3.0, P=2000, arch="real", primes="real"):
    CENT=[14.0+4.0*k for k in range(NC)]; W=S/math.sqrt(2); RG=np.arange(-150,150,0.1)
    if arch=="real": M=np.array([float(mp.re(mp.digamma(mp.mpc(0.25,r/2)))) for r in RG])
    elif arch=="none": M=np.zeros_like(RG)
    elif arch=="fake": M=np.array([float(mp.re(mp.digamma(mp.mpc(0.25,r/3)))) for r in RG])
    lam={}; comp=[False]*(P+1)
    for p in range(2,P+1):
        if not comp[p]:
            for m in range(p*p,P+1,p): comp[m]=True
            pk=p
            while pk<=P: lam[pk]=math.log(p); pk*=p
    nid=np.array(sorted(lam)); logn=np.log(nid); lw=np.array([lam[int(n)] for n in nid])/np.sqrt(nid)
    if primes=="shuffle":
        import numpy.random as nr; lw=nr.default_rng(3).permutation(lw)
    def terms(ci,cj): return [(math.exp(-(a-b)**2/(4*S**2)),(a+b)/2) for a in (ci,-ci) for b in (cj,-cj)]
    A=np.zeros((NC,NC));Pm=np.zeros((NC,NC));Rm=np.zeros((NC,NC))
    for i in range(NC):
        for j in range(NC):
            t=terms(CENT[i],CENT[j]); Hg=np.zeros_like(RG)
            for a,m in t: Hg+=a*np.exp(-(RG-m)**2/(S**2))
            A[i,j]=float(np.sum(Hg*M)*0.1/(2*math.pi))
            pole=2*sum(a*np.exp(-((1j*0.5)-m)**2/(S**2)) for a,m in t); g0=sum(a*(W/math.sqrt(2*math.pi)) for a,m in t)
            Pm[i,j]=float(np.real(pole-g0*math.log(math.pi)))
            pr=0j
            for a,m in t: pr+=2*np.sum(lw*(a*(W/math.sqrt(2*math.pi))*np.exp(-W**2*logn**2/2)*np.exp(-1j*m*logn)))
            Rm[i,j]=float(np.real(pr))
    sym=lambda X:(X+X.T)/2; A,Pm,Rm=sym(A),sym(Pm),sym(Rm); D=A+Pm-Rm
    return dict(D=D, min_eig=float(np.linalg.eigvalsh(D).min()), eigs=np.linalg.eigvalsh(D))
