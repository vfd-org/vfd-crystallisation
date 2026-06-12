"""
coxeter_star_projection.py
Coxeter-plane (Petrie) projection of the exceptional root systems E6,E7,E8 ->
the canonical star/mandala patterns. Honest scope: finite-system visualization;
E10 (hyperbolic, infinite) has no finite Coxeter plane -- only a constructed slice.
"""
import numpy as np, json, itertools, os
HERE=os.path.dirname(os.path.abspath(__file__))

def e8_roots():
    R=[]
    for i,j in itertools.combinations(range(8),2):
        for si in (1,-1):
            for sj in (1,-1):
                v=np.zeros(8); v[i]=si; v[j]=sj; R.append(v)         # 112
    for signs in itertools.product((0.5,-0.5),repeat=8):
        if sum(1 for s in signs if s<0)%2==0: R.append(np.array(signs))  # 128 (even # of -)
    return np.array(R)

def subsystem(R, normals):
    """roots orthogonal to given normal roots -> E7 (1 normal), E6 (2 normals)."""
    keep=[r for r in R if all(abs(r@n)<1e-9 for n in normals)]
    return np.array(keep)

def simple_roots(R):
    f=np.array([np.pi**k for k in range(R.shape[1])])              # generic functional
    pos=[r for r in R if f@r>1e-9]
    posset={tuple(np.round(r,6)) for r in pos}
    simp=[]
    for r in pos:
        decomp=any(tuple(np.round(r-p,6)) in posset for p in pos if f@p>1e-9 and f@(r-p)>1e-9)
        if not decomp: simp.append(r)
    return np.array(simp)

def reflect(x,a): return x - 2*(x@a)/(a@a)*a

def coxeter_plane(R, h):
    S=simple_roots(R); n=len(S)
    C=np.eye(R.shape[1])
    for a in S: C = np.array([reflect(C[:,k],a) for k in range(C.shape[1])]).T  # apply s_a to columns
    ev,V=np.linalg.eig(C)
    targ=np.exp(2j*np.pi/h)
    k=int(np.argmin(np.abs(ev-targ)))
    v=V[:,k]; a=np.real(v); b=np.imag(v)
    a/=np.linalg.norm(a); b=b-(b@a)*a; b/=np.linalg.norm(b)
    return a,b,n

def project(name,R,h):
    a,b,n=coxeter_plane(R,h)
    P=np.array([[r@a, r@b] for r in R])
    rad=np.round(np.linalg.norm(P,axis=1),4); rings=sorted(set(rad[rad>1e-6]))
    print(f"  {name}: {len(R)} roots, rank {n}, Coxeter number h={h}, "
          f"{len(rings)} concentric rings -> {h}-fold star")
    return P

if __name__=="__main__":
    E8=e8_roots()
    # E7 = roots orthogonal to one E8 root; E6 = orthogonal to an A2 pair (dot=-1)
    r0=E8[0]; E7=subsystem(E8,[r0])
    r1=next(r for r in E8 if abs(r@r0+1)<1e-9)      # r0,r1 form A2 (dot=-1); complement=E6
    E6=subsystem(E8,[r0, r1])
    print("COXETER-PLANE (PETRIE) STAR PROJECTIONS of the exceptional root systems:")
    out={}
    for name,R,h in [("E6",E6,12),("E7",E7,18),("E8",E8,30)]:
        P=project(name,R,h); out[name]={"h":h,"n_roots":len(R),"coords":P.round(5).tolist()}
    json.dump(out,open(os.path.join(HERE,"coxeter_star_coords.json"),"w"))
    # save a PNG if matplotlib present
    try:
        import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
        fig,ax=plt.subplots(1,3,figsize=(15,5))
        for k,(name,R,h) in enumerate([("E6",E6,12),("E7",E7,18),("E8",E8,30)]):
            P=np.array(out[name]["coords"])
            ax[k].scatter(P[:,0],P[:,1],s=8); 
            for p in P: ax[k].plot([0,p[0]],[0,p[1]],lw=0.2,color="gray",alpha=0.5)
            ax[k].set_aspect("equal"); ax[k].axis("off"); ax[k].set_title(f"{name}: {len(R)} roots, {h}-fold")
        plt.tight_layout(); plt.savefig(os.path.join(HERE,"coxeter_stars.png"),dpi=130)
        print("  saved coxeter_stars.png (E6/E7/E8 mandalas)")
    except Exception as e:
        print("  (matplotlib unavailable; coords saved to coxeter_star_coords.json)", e)
