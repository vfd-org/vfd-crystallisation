"""WO-VFD-PGS-TRACE-BRIDGE-001 — divisor-excess observable -> trace-law bridge test.
Honest core checks built in: the proposed sigma-probe R(sigma)=|Phi(sigma)-Phi(1-sigma)|
vanishes at 1/2 for EVERY weight (no functional equation in a raw Dirichlet series), and
a symmetric tridiagonal operator has real eigenvalues for ANY diagonal -> both flagship
tests are tautological / non-discriminating. We DEMONSTRATE this against null models."""
import numpy as np, math, json
def tau_sieve(N):
    tau=np.zeros(N+1,dtype=np.int64)
    for d in range(1,N+1): tau[d:N+1:d]+=1
    return tau
def mobius_sieve(N):
    mu=np.ones(N+1,dtype=np.int64); prime=np.ones(N+1,bool); mu[0]=0
    for i in range(2,N+1):
        if prime[i]:
            for j in range(i,N+1,i):
                if j>i: prime[j]=False
                mu[j]*=-1
            ii=i*i
            for j in range(ii,N+1,ii): mu[j]=0
    return mu
def vonmangoldt(N):
    lam=np.zeros(N+1); 
    sieve=tau_sieve  # not used; compute via prime powers
    is_comp=np.zeros(N+1,bool)
    for p in range(2,N+1):
        if not is_comp[p]:
            for m in range(p*p,N+1,p): is_comp[m]=True
            pk=p
            while pk<=N: lam[pk]=math.log(p); pk*=p
    return lam
def build_observables(N):
    tau=tau_sieve(N); n=np.arange(N+1); logn=np.zeros(N+1); logn[2:]=np.log(n[2:])
    E=np.zeros(N+1); E[2:]=(tau[2:]/2-1)*logn[2:]
    Z=np.exp(-E); H=logn+E; mu=mobius_sieve(N); lam=vonmangoldt(N)
    is_prime=(tau==2)
    return dict(tau=tau,logn=logn,E=E,Z=Z,H=H,mu=mu,lam=lam,is_prime=is_prime,N=N)
def gap_chambers(obs):
    is_prime=obs['is_prime']; primes=np.where(is_prime)[0]; E=obs['E']
    rows=[]
    for p,q in zip(primes[:-1],primes[1:]):
        interior=np.arange(p+1,q)
        Ei=E[interior] if len(interior) else np.array([0.0])
        # symmetry residual within chamber [p..q]
        seg=E[p:q+1]; rev=seg[::-1]; rsym=float(np.sum(np.abs(seg-rev)))/2
        rsym_norm=rsym/(1+float(seg.sum()))
        rows.append(dict(p=int(p),q=int(q),gap=int(q-p),interior=int(len(interior)),
            minE=float(Ei.min()),maxE=float(Ei.max()),meanE=float(Ei.mean()),sumE=float(Ei.sum()),
            rsym=rsym,rsym_norm=rsym_norm))
    return rows
def chamber_operator_check(obs, which="E", seed=0):
    """build symmetric tridiagonal V-operators per chamber; verify self-adjointness (trivial)."""
    is_prime=obs['is_prime']; primes=np.where(is_prime)[0]; V=obs[which] if which in obs else None
    rng=np.random.default_rng(seed)
    sym_err=0.0; all_real=True; traces=[]
    for p,q in zip(primes[:-1],primes[1:]):
        m=q-p+1
        if m<3: continue
        if which=="random": diag=rng.standard_normal(m)
        else: diag=np.array([V[p+i] for i in range(m)])
        T=np.diag(diag)+np.diag(np.ones(m-1),1)+np.diag(np.ones(m-1),-1)
        sym_err=max(sym_err, float(np.max(np.abs(T-T.T))))
        ev=np.linalg.eigvals(T); 
        if np.max(np.abs(ev.imag))>1e-9: all_real=False
        traces.append(float(np.trace(T)))
        if len(traces)>3000: break
    return dict(which=which, max_symmetry_error=sym_err, all_eigenvalues_real=all_real,
                total_trace=float(sum(traces)), n_chambers=len(traces))
def sigma_probe(obs, weights, sigmas):
    N=obs['N']; n=np.arange(2,N+1).astype(float); out={}
    for name,w in weights.items():
        wv=w[2:N+1]
        def Phi(s): return float(np.sum(wv*n**(-s)))
        R={s: abs(Phi(s)-Phi(1-s)) for s in sigmas}
        smin=min(R,key=R.get)
        out[name]=dict(argmin_sigma=round(float(smin),3), R_at_half=R[min(sigmas,key=lambda s:abs(s-0.5))],
                       R_min=R[smin])
    return out
