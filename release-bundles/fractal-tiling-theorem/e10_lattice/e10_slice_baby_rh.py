"""
e10_slice_baby_rh.py
Build a CONSTRUCTED 2D slice of the E10 real-root system (the 'star skin' of the
hyperbolic reflection bulk), then run a baby-RH on the slice's adjacency Laplacian.
Honest: non-canonical projection; tests whether the universal self-adjoint->on-line
mechanism holds on yet another object -- it will, for the SLICE's own spectrum.
"""
import numpy as np, os, json
HERE=os.path.dirname(os.path.abspath(__file__))
E8=[(1,3),(3,4),(4,5),(5,6),(6,7),(7,8),(2,4)]; edges=E8+[(8,9),(9,10)]; n=10
A=2*np.eye(n)
for i,j in edges: A[i-1,j-1]=A[j-1,i-1]=-1                 # E10 Cartan matrix
S=[np.eye(n)-np.outer(np.eye(n)[i],A[i]) for i in range(n)]  # simple reflections (root basis)
# BFS the Weyl orbit of the simple roots -> real roots (norm^2 = 2)
seen=set(); roots=[]; frontier=[]
for i in range(n):
    e=np.eye(n)[i].astype(int); seen.add(tuple(e)); roots.append(e); frontier.append(e)
d=0
while frontier and len(roots)<900 and d<10:
    d+=1; nxt=[]
    for x in frontier:
        for Si in S:
            y=np.rint(Si@x).astype(int); t=tuple(y)
            if t not in seen: seen.add(t); roots.append(y); nxt.append(y)
    frontier=nxt
R=np.array(roots,float)
norms=np.array([r@A@r for r in R])
print(f"E10 real roots generated: {len(R)} (all norm^2=2? {np.allclose(norms,2)})")
# embed in standard Lorentzian coords; project spacelike part to 2D (PCA) = the SLICE
w,Q=np.linalg.eigh(A); idx=np.argsort(w); w,Q=w[idx],Q[:,idx]
Y=(np.diag(np.sqrt(np.abs(w)))@Q.T@R.T).T          # y=Tx, col 0 ~ timelike
Ys=Y[:,1:]-Y[:,1:].mean(0); U,Sv,Vt=np.linalg.svd(Ys,full_matrices=False)
P=Ys@Vt[:2].T                                       # 2D slice coords
json.dump({"n_roots":len(R),"slice_coords":P.round(4).tolist()},
          open(os.path.join(HERE,"results","e10_slice.json"),"w"))
try:
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    plt.figure(figsize=(6,6)); plt.scatter(P[:,0],P[:,1],s=5,alpha=0.6)
    plt.gca().set_aspect("equal"); plt.axis("off"); plt.title(f"E10 root slice ({len(R)} roots) — constructed star skin")
    plt.savefig(os.path.join(HERE,"results","e10_slice.png"),dpi=130); print("saved results/e10_slice.png")
except Exception as e: print("(no matplotlib)",e)

# --- baby-RH on the slice adjacency Laplacian (critical line Re(s)=1/2, lambda=s(1-s)) ---
Dm=np.sqrt(((P[:,None,:]-P[None,:,:])**2).sum(2)); np.fill_diagonal(Dm,np.inf)
dnn=np.median(Dm.min(1)); Adj=(Dm<1.6*dnn).astype(float); L=np.diag(Adj.sum(1))-Adj
lam=np.linalg.eigvalsh(L)
s=0.5+np.sqrt(0.25-lam.astype(complex)); on=np.isclose(s.real,0.5,atol=1e-9)|np.isclose(s.imag,0,atol=1e-9)
print(f"\nbaby-RH on E10 slice (Re(s)=1/2, lambda=s(1-s)): <deg>={Adj.sum(1).mean():.1f}")
print(f"  on-line/real: {int(on.sum())}/{len(lam)}  violations: {int((~on).sum())}  holds: {bool(on.all())}")
rng=np.random.default_rng(0); P2=rng.standard_normal((len(L),len(L)))
lam2=np.linalg.eigvals(L+0.3*(P2-P2.T)); s2=0.5+np.sqrt(0.25-lam2)
off=int(np.sum(~(np.isclose(s2.real,0.5,atol=1e-6)|np.isclose(s2.imag,0,atol=1e-6))))
print(f"  break self-adjointness -> off-line {off}/{len(lam)}")
