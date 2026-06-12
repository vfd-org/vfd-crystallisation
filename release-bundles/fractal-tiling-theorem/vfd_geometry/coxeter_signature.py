"""Phase 3+4: Coxeter Gram determinant classifier. Linear diagram [m1,m2,...]:
G_ii=1, G_{i,i+1}=-cos(pi/m_i). det>0 & PD -> spherical(finite); PSD 1 null -> affine;
indefinite -> hyperbolic/infinite. This is the classical Schlafli/Coxeter criterion;
finite closure <-> positive curvature <-> spherical. We RECOVER it and match to orbits."""
import numpy as np, math
def gram(ms):
    n=len(ms)+1; G=np.eye(n)
    for i,m in enumerate(ms):
        c=-math.cos(math.pi/m) if m!=float('inf') else -1.0
        G[i,i+1]=G[i+1,i]=c
    return G
def gram_q(qs):  # diagram where first edges given as q=2cos(pi/m) (q on subdiagonal as -q/2)
    n=len(qs)+1; G=np.eye(n)
    for i,q in enumerate(qs): G[i,i+1]=G[i+1,i]=-q/2
    return G
def classify(G):
    ev=np.linalg.eigvalsh(G); det=float(np.linalg.det(G)); tol=1e-9
    npos=int((ev>tol).sum()); nzero=int((np.abs(ev)<=tol).sum()); nneg=int((ev<-tol).sum())
    if nneg==0 and nzero==0: cls="spherical(finite)"; curv="positive"
    elif nneg==0 and nzero>=1: cls="affine(marginal/inf)"; curv="zero"
    else: cls="hyperbolic/indefinite(inf)"; curv="negative"
    return dict(det=round(det,6), eig_sig=(npos,nzero,nneg), classification=cls, curvature=curv)
