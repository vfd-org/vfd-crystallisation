"""WO-RH-ARITHMETIC-HORIZON-INVARIANT-001 — does the maximal prime-pressure mode
of K = H^-1/2 R H^-1/2 define a STABLE, PRIME-SPECIFIC pressure envelope Pi(log n)?

Hunting two honest failure modes:
 (i) BASIS ARTEFACT  — envelope just tracks the test-function damping exp(-W^2 log^2 n /2)
     (smallest primes dominate because they sit near log n=0). Tested by varying width S.
 (ii) GENERIC not prime-specific — smoothed-PNT control (weight 1/sqrt(n) on EVERY
     integer) reproduces the envelope/mu_max. Then the horizon law is generic capacity
     and prime-specificity (the zeros = RH) is the FLUCTUATION, not the envelope.
Non-circular: primes + archimedean + pole only; NO zeros in construction.
"""
import numpy as np, mpmath as mp, math
mp.mp.dps=18
RG=np.arange(-150,150,0.1); DR=0.1
SQ2PI=math.sqrt(2*math.pi)
def archmul(): return np.array([float(mp.re(mp.digamma(mp.mpc(0.25,r/2)))) for r in RG])
MUL=archmul()
def sieve(P):
    lam={}; comp=[False]*(P+1)
    for p in range(2,P+1):
        if not comp[p]:
            for m in range(p*p,P+1,p): comp[m]=True
            pk=p
            while pk<=P: lam[pk]=math.log(p); pk*=p
    return lam
PCUT=2000; LAM=sieve(PCUT)
# weight builders: dict n-> weight  (raw weight = arithmetic part; sqrt(n) folded in)
def w_real():   return {n:LAM[n]/math.sqrt(n) for n in LAM}
def w_primesonly():
    out={}
    for n in LAM:
        # prime iff Lambda(n)=log n exactly (p^1)
        if abs(LAM[n]-math.log(n))<1e-9: out[n]=LAM[n]/math.sqrt(n)
    return out
def w_lowremoved(thr=11): return {n:LAM[n]/math.sqrt(n) for n in LAM if n>=thr}
def w_pnt():    return {n:1.0/math.sqrt(n) for n in range(2,PCUT+1)}      # smoothed PNT: avg Lambda=1 on ALL integers
def w_shuffled(seed):
    rng=np.random.default_rng(seed); ns=sorted(LAM); vals=[LAM[n] for n in ns]
    rng.shuffle(vals)
    targets=rng.choice(np.arange(2,PCUT+1),size=len(ns),replace=False)
    return {int(t):v/math.sqrt(int(t)) for t,v in zip(targets,vals)}

def basis(N,step=4.0,first=14.0): return [first+step*k for k in range(N)]
def hterms(ci,cj,S): return [(math.exp(-(a-b)**2/(4*S**2)),(a+b)/2) for a in (ci,-ci) for b in (cj,-cj)]
def build(N,S,wdict,first=14.0):
    CENT=basis(N,4.0,first); W=S/math.sqrt(2)
    ns=np.array(sorted(wdict)); logn=np.log(ns); wv=np.array([wdict[int(n)] for n in ns])
    damp=np.exp(-W**2*logn**2/2)*(W/SQ2PI)          # test-fn magnitude envelope
    A=np.zeros((N,N));P=np.zeros((N,N));R=np.zeros((N,N))
    # per-n prime kernel pieces for envelope extraction (store for max mode later)
    perN={}
    for i in range(N):
        for j in range(N):
            t=hterms(CENT[i],CENT[j],S)
            Hg=np.zeros_like(RG)
            for a,m in t: Hg+=a*np.exp(-(RG-m)**2/(S**2))
            A[i,j]=float(np.sum(Hg*MUL)*DR/(2*math.pi))
            pole=2*sum(a*np.exp(-((1j*0.5)-m)**2/(S**2)) for a,m in t)
            g0=sum(a*(W/SQ2PI) for a,m in t)
            P[i,j]=float(np.real(pole-g0*math.log(math.pi)))
            # prime: sum_n 2 * wv * damp * Re( sum_{a,m} a exp(-i m logn) )
            phase=np.zeros_like(ns,dtype=complex)
            for a,m in t: phase+=a*np.exp(-1j*m*logn)
            rn=2*wv*damp*np.real(phase)
            R[i,j]=float(np.sum(rn)); perN[(i,j)]=rn
    sym=lambda X:(X+X.T)/2
    return sym(A),sym(P),sym(R),perN,ns,logn
def KofHR(A,P,R):
    H=A+P; w,U=np.linalg.eigh(H)
    if w.min()<=1e-9: return None,H,None
    Hm=U@np.diag(1/np.sqrt(w))@U.T; K=(Hm@R@Hm); K=(K+K.T)/2
    return K,H,Hm
def horizon_mode(A,P,R):
    K,H,Hm=KofHR(A,P,R)
    if K is None: return None
    ev,V=np.linalg.eigh(K); mu=ev[-1]; g=V[:,-1]; f=Hm@g
    Qp=float(f@R@f); Qc=float(f@H@f); return dict(mu=mu,f=f,g=g,Qp=Qp,Qc=Qc,C=Qp/Qc)
def envelope(perN,f,ns):
    N=len(f); q=np.zeros(len(ns))
    for i in range(N):
        for j in range(N): q+=f[i]*f[j]*perN[(i,j)]
    return q     # q_n[f], sum = Q_prime[f]
def stats(q,ns,logn):
    a=np.abs(q); tot=a.sum()
    if tot==0: return dict(peak=0,cent=0,var=0,ent=0,pr=0)
    w=a/tot; peak=float(logn[np.argmax(a)]); cent=float(np.sum(w*logn))
    var=float(np.sum(w*(logn-cent)**2)); ent=float(-np.sum(w[w>0]*np.log(w[w>0])))
    pr=float((a.sum()**2)/np.sum(a**2)); pk_n=int(ns[np.argmax(a)])
    return dict(peak=peak,peak_n=pk_n,cent=cent,var=var,ent=ent,pr=pr)
def alpha_c(A,P,R):
    f=lambda a:np.linalg.eigvalsh(a*A+P-R).min(); lo,hi=0.0,3.0
    for _ in range(40):
        m=(lo+hi)/2
        if f(m)>=0: hi=m
        else: lo=m
    return hi

print("="*70); print("WO-RH-ARITHMETIC-HORIZON-INVARIANT-001  prime-pressure envelope"); print("="*70)

# --- 1. real-prime horizon mode + envelope (N=12,S=3 reference) ---
A,P,R,perN,ns,logn=build(12,3.0,w_real())
hm=horizon_mode(A,P,R); q=envelope(perN,hm['f'],ns); st=stats(q,ns,logn)
print(f"\n[1] REAL primes, N=12 S=3: mu_max={hm['mu']:.5f}  C[f]={hm['C']:.5f}  Q_prime={hm['Qp']:.4f} Q_cap={hm['Qc']:.4f}")
print(f"    envelope: peak at n={st['peak_n']} (log n={st['peak']:.2f}), centroid={st['cent']:.2f}, entropy={st['ent']:.2f}, participation={st['pr']:.2f}")
# which primes carry the pressure
order=np.argsort(-np.abs(q))[:8]
print("    top pressure-carrying n:  "+", ".join(f"n={int(ns[k])}({q[k]:+.3f})" for k in order))

# --- 2. BASIS-WIDTH artefact test: does the peak move with S? ---
print("\n[2] BASIS-WIDTH artefact test (does envelope just track exp(-W^2 log^2 n/2)?):")
for S in [2.0,3.0,4.0]:
    a2,p2,r2,pn2,n2,l2=build(12,S,w_real()); h2=horizon_mode(a2,p2,r2)
    q2=envelope(pn2,h2['f'],n2); s2=stats(q2,n2,l2)
    print(f"    S={S}: mu={h2['mu']:.4f}  envelope peak n={s2['peak_n']} log n={s2['peak']:.2f} centroid={s2['cent']:.2f} (W={S/math.sqrt(2):.2f})")
print("    -> if peak/centroid SHIFT with S, the envelope tracks the BASIS, not the prime field.")

# --- 3. N-scaling stability of mu_max and envelope shape ---
print("\n[3] N-scaling (S=3, real primes): does mu_max + envelope stabilise?")
prev=None
for N in [8,12,16,24]:
    a3,p3,r3,pn3,n3,l3=build(N,3.0,w_real()); h3=horizon_mode(a3,p3,r3)
    q3=envelope(pn3,h3['f'],n3); s3=stats(q3,n3,l3)
    ov="" 
    if prev is not None:
        c=np.dot(q3/np.linalg.norm(q3),prev/np.linalg.norm(prev)); ov=f" env-overlap-vs-prev={c:+.3f}"
    prev=q3.copy()
    print(f"    N={N:2d}: mu_max={h3['mu']:.5f}  C={h3['C']:.5f}  peak n={s3['peak_n']} entropy={s3['ent']:.2f}{ov}")

# --- 4. CONTROLS: real vs smoothed-PNT vs shuffled vs primes-only vs low-removed ---
print("\n[4] CONTROLS (N=12 S=3): is the horizon law PRIME-SPECIFIC?")
ctrls=[("real          ",w_real()),("smoothed-PNT   ",w_pnt()),("primes-only    ",w_primesonly()),
       ("low<11-removed ",w_lowremoved(11)),("shuffled-Lambda",w_shuffled(7)),("shuffled(seed2)",w_shuffled(23))]
ref_q=None; ref_n=None
for name,wd in ctrls:
    a4,p4,r4,pn4,n4,l4=build(12,3.0,wd); h4=horizon_mode(a4,p4,r4)
    q4=envelope(pn4,h4['f'],n4); s4=stats(q4,n4,l4)
    if name.startswith("real"): ref_q,ref_n=q4.copy(),n4
    # envelope overlap vs real on common support
    ov=""
    if ref_q is not None and not name.startswith("real"):
        common=np.intersect1d(ref_n,n4)
        ra=np.array([ref_q[np.where(ref_n==c)[0][0]] for c in common])
        qa=np.array([q4[np.where(n4==c)[0][0]] for c in common])
        if np.linalg.norm(ra)>0 and np.linalg.norm(qa)>0:
            ov=f"  env-overlap-vs-real={np.dot(ra/np.linalg.norm(ra),qa/np.linalg.norm(qa)):+.3f}"
    print(f"    {name}: mu_max={h4['mu']:.5f}  C={h4['C']:.5f}  alpha_c={alpha_c(a4,p4,r4):.4f}  peak n={s4['peak_n']}{ov}")

print("""
----------------------------------------------------------------------
READ THE DATA -> verdict written in the report. Key questions:
 [2] does envelope peak move with S?  (basis artefact?)
 [3] does mu_max + envelope stabilise with N?
 [4] does smoothed-PNT match real?    (generic vs prime-specific?)
     does shuffled-Lambda DEGRADE?     (genuine prime signal?)
----------------------------------------------------------------------""")
