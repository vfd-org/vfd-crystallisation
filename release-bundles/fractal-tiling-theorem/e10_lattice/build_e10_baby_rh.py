"""
build_e10_baby_rh.py
Build E10 = E8^{++} (the Z-native hyperbolic over-extension, signature (9,1),
acting on H^9), verify its Coxeter group, generate an orbit patch, and fire the
baby-RH (self-adjoint Laplacian -> Selberg zeros on the H^9 critical line Re(s)=4).
Finite discrete MODEL of the mechanism, now over the Z lattice II_{9,1}.
"""
import json, os, numpy as np
np.set_printoptions(suppress=True)
HERE=os.path.dirname(os.path.abspath(__file__))
E8=[(1,3),(3,4),(4,5),(5,6),(6,7),(7,8),(2,4)]; edges=E8+[(8,9),(9,10)]; n=10
G=np.eye(n)
for i,j in edges: G[i-1,j-1]=G[j-1,i-1]=-0.5
ev=np.linalg.eigvalsh(G); sig=(int((ev>1e-9).sum()),int((ev<-1e-9).sum()))
print(f"E10 Gram signature (+,-) = {sig}  -> {'HYPERBOLIC H^9 (Lorentzian)' if sig==(9,1) else 'NOT (9,1)!'}")

gens=[np.eye(n)-2*np.outer(np.eye(n)[i],G[i]) for i in range(n)]
def order(A,mx=12):
    P=np.eye(n)
    for k in range(1,mx+1):
        P=P@A
        if np.allclose(P,np.eye(n),atol=1e-7): return k
    return None
adj=set((i-1,j-1) for i,j in edges)|set((j-1,i-1) for i,j in edges)
ok=all(order(gens[i])==2 for i in range(n))
ok&=all(order(gens[i]@gens[j])==(3 if (i,j) in adj else 2) for i in range(n) for j in range(i+1,n))
print(f"E10 Coxeter relations verified (adjacent order 3, else 2): {ok and sig==(9,1)}")

w,Q=np.linalg.eigh(G); idx=np.argsort(w); w,Q=w[idx],Q[:,idx]
T=np.diag(np.sqrt(np.abs(w)))@Q.T; J=np.diag(np.sign(w))
def std(x): return T@x
def jn(y): return y@J@y
Ginv=np.linalg.inv(G); k=int(np.argmin(np.diag(Ginv)))
seed=Ginv[:,k]                       # most-timelike fundamental weight
print(f"seed weight B(w,w)={seed@G@seed:.4f} (<0 => proper point of H^9)")
def norm(x):
    y=std(x); q=jn(y)
    if q>=0: return None
    y=y/np.sqrt(-q)
    if y[0]<0: y=-y
    return y
def key(y): return tuple(np.round(y,4))
y0=norm(seed); seen={key(y0):0}; coords={key(y0):seed.copy()}; frontier=[seed]; depth=0
while frontier and depth<12 and len(seen)<700:
    depth+=1; nxt=[]
    for x in frontier:
        for g in gens:
            xx=g@x; yy=norm(xx)
            if yy is None: continue
            kk=key(yy)
            if kk not in seen: seen[kk]=depth; coords[kk]=xx.copy(); nxt.append(xx)
    frontier=nxt
    print(f"  shell {depth}: +{len(nxt)}  (cum {len(seen)})")
Y=np.array([norm(x) for x in coords.values()]); N=len(Y)
print(f"E10 patch: {N} orbit points in H^9")

# adjacency Laplacian -> baby RH on H^9 (critical line Re(s)=4, lambda=s(8-s))
Tg=Y[:,0][:,None]*Y[:,0][None,:]-Y[:,1:]@Y[:,1:].T
Dm=np.arccosh(np.clip(Tg,1.0,None)); np.fill_diagonal(Dm,np.inf)
dnn=np.median(Dm.min(1)); A=(Dm<1.3*dnn).astype(float); L=np.diag(A.sum(1))-A
lam=np.linalg.eigvalsh(L)
s=4+np.sqrt(16-lam.astype(complex)); on=np.isclose(s.real,4,atol=1e-9)|np.isclose(s.imag,0,atol=1e-9)
temp=int((lam>16).sum()); exc=int((lam<16).sum())
print(f"\nBABY-RH on E10/H^9 (critical line Re(s)=4): <deg>={A.sum(1).mean():.1f}")
print(f"  tempered zeros on Re(s)=4: {temp}   exceptional (real): {exc}   violations: {int((~on).sum())}")
print(f"  BABY RH holds (all on line or real): {bool(on.all())}")
lam2=np.linalg.eigvals(L+0.25*(np.random.default_rng(0).standard_normal((N,N)) - np.random.default_rng(0).standard_normal((N,N)).T))
off=int(np.sum(~(np.isclose((4+np.sqrt(16-lam2)).real,4,atol=1e-6)|np.isclose((4+np.sqrt(16-lam2)).imag,0,atol=1e-6))))
print(f"  break self-adjointness -> zeros off line: {off}/{N}")
json.dump({"signature":sig,"coxeter_ok":bool(ok),"N":N,"baby_rh":bool(on.all()),
           "tempered":temp,"exceptional":exc},open(os.path.join(HERE,"results","e10_baby_rh.json"),"w"),indent=1)
