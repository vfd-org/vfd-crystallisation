"""WO-VFD-RH-CAPACITY-OPERATOR-LIMIT-001 core. Builds the centre's capacity operators
A (archimedean), P (pole), R (reflection/prime), H=A+P, Q=H-R, K=H^{-1/2}RH^{-1/2}.
Convention: Q_W = H^{1/2}(I-K)H^{1/2}, K symmetric, positivity <=> ||K||=mu_max(K)<=1.
(route_b / Weil-Connes; KNOWN, not new.)"""
import numpy as np, mpmath as mp, math
mp.mp.dps=18
def components(NC=12,S=3.0,P=2000,arch="real",primes="real",seed=0):
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
    if primes=="shuffle": lw=np.random.default_rng(seed).permutation(lw)
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
    sym=lambda X:(X+X.T)/2; return sym(A),sym(Pm),sym(Rm),CENT
def operators(A,Pm,Rm):
    H=A+Pm; w,U=np.linalg.eigh(H)
    out=dict(H=H,Q=A+Pm-Rm,H_min_eig=float(w.min()),Q_min_eig=float(np.linalg.eigvalsh(A+Pm-Rm).min()))
    if w.min()>1e-9:
        Hm=U@np.diag(1/np.sqrt(w))@U.T; K=Hm@Rm@Hm; K=(K+K.T)/2
        ev,V=np.linalg.eigh(K); out.update(K=K,Kmax=float(ev.max()),Qeig=np.linalg.eigvalsh(out['Q']))
        qv,qV=np.linalg.eigh(out['Q']); out['nearnull_vec']=qV[:,0]; out['nearnull_eig']=float(qv[0])
    return out
