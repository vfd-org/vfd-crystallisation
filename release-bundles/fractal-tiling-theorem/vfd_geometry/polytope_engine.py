"""VFD Polytype Transformation Engine — core (WO-VFD-POLYTYPE-TRANSFORMATION-ENGINE-001).
Coxeter reflection-orbit generator + known-polytope anchors + signatures.
Honest framing: this RECOVERS known root-system/Coxeter facts; novelty is only in
whatever survives across families (tested in the scan/folding modules)."""
import numpy as np, itertools, math
PHI=(1+math.sqrt(5))/2
def _round_rows(A,nd=6): return {tuple(np.round(r,nd)) for r in A}
def gram_signature(V):
    V=np.asarray(V,float); G=V@V.T
    norms=np.round(np.unique(np.round((V*V).sum(1),6)),6)
    ips=np.round(np.unique(np.round(G[np.triu_indices(len(V),1)],6)),6)
    ev=np.round(np.linalg.eigvalsh(V.T@V),4)
    return dict(vertex_count=len(V), unique_norms2=norms.tolist(),
                unique_innerproducts=ips.tolist(), gram_rank=int(np.linalg.matrix_rank(V)),
                covariance_eigs=ev.tolist())
# ---- anchors (direct coordinates) ----
def icosahedron():
    # 12 vertices: cyclic perms of (0,±1,±φ)
    V=set()
    for a in (1,-1):
        for c in (PHI,-PHI):
            V|={(0,a,c),(a,c,0),(c,0,a)}
    return np.array(sorted(V))
def cell24():
    # 24-cell = D4 roots: all (±1,±1,0,0) perms
    V=set()
    for i,j in itertools.combinations(range(4),2):
        for si in (1,-1):
            for sj in (1,-1):
                v=[0,0,0,0]; v[i]=si; v[j]=sj; V.add(tuple(v))
    return np.array(sorted(V))
def tesseract():
    return np.array(list(itertools.product([-0.5,0.5],repeat=4)))
def cell16():
    V=[]
    for i in range(4):
        for s in (1,-1):
            v=[0,0,0,0]; v[i]=s; V.append(tuple(v))
    return np.array(V)
def cell600():
    V=set()
    for i in range(4):                                   # 8: (±1,0,0,0)
        for s in (1,-1):
            v=[0,0,0,0]; v[i]=s; V.add(tuple(v))
    for signs in itertools.product([-0.5,0.5],repeat=4): # 16: (±1/2)^4
        V.add(tuple(signs))
    base=(PHI/2,0.5,1/(2*PHI),0.0)                       # 96: even perms, signed
    A4=[p for p in itertools.permutations(range(4)) if _parity(p)==0]
    for p in A4:
        arr=[base[p.index(k)] for k in range(4)]
        # place base values at positions given by even permutation
        for p2 in [p]:
            vec=[0,0,0,0]
            for pos,val in zip(p2,base): vec[pos]=val
            nz=[k for k in range(4) if abs(vec[k])>1e-12]
            for sgn in itertools.product([1,-1],repeat=len(nz)):
                v=list(vec)
                for k,s in zip(nz,sgn): v[k]*=s
                V.add(tuple(np.round(v,9)))
    return np.array(sorted(V))
def _parity(p):
    p=list(p); n=len(p); seen=[False]*n; par=0
    for i in range(n):
        if seen[i]: continue
        j=i; L=0
        while not seen[j]: seen[j]=True; j=p[j]; L+=1
        par+=L-1
    return par%2
def e8_roots():
    V=[]
    for i,j in itertools.combinations(range(8),2):       # 112
        for si in (1,-1):
            for sj in (1,-1):
                v=[0]*8; v[i]=si; v[j]=sj; V.append(tuple(v))
    for signs in itertools.product([-0.5,0.5],repeat=8): # 128 (even # minus)
        if sum(1 for s in signs if s<0)%2==0: V.append(tuple(signs))
    return np.array(V)
# ---- reflection orbit ----
def reflect(v,a): return v-(v@a)*a            # a normalised so a.a=2
def generate_orbit(simple_roots, seed, cap=2000, nd=6):
    R=[np.asarray(a,float) for a in simple_roots]
    seed=np.asarray(seed,float); seen={tuple(np.round(seed,nd))}; frontier=[seed]; pts=[seed]
    while frontier:
        nf=[]
        for v in frontier:
            for a in R:
                w=reflect(v,a); key=tuple(np.round(w,nd))
                if key not in seen:
                    seen.add(key); nf.append(w); pts.append(w)
                    if len(pts)>cap: return np.array(pts), False   # explosion
        frontier=nf
    return np.array(pts), True
def h3_simple_roots(q):
    """Coxeter [m,3] with 2cos(pi/m)=q on the first edge; |alpha|^2=2."""
    G=np.array([[2,-q,0],[-q,2,-1.0],[0,-1,2]])
    # strictly PD (det>tol) => finite/Euclidean reflection group; det=6-2q^2, =0 at q=sqrt3 (affine)
    if np.linalg.det(G) <= 1e-6: return None, False
    try: L=np.linalg.cholesky(G); return L, True
    except np.linalg.LinAlgError: return None, False
