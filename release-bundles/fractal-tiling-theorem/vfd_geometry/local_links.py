"""Local-link / vertex-figure extraction (WO-VFD-LOCAL-LINK-GLOBAL-CLOSURE-002).
The link of vertex v = graph on v's nearest neighbours, with link-edges = neighbour
pairs that are themselves at the polytope min-distance (i.e. polytope-adjacent).
This is the classical vertex figure. Honest: known regular-polytope geometry."""
import numpy as np, standing_wave_modes as SW
def link_graph(V, i, tol=1e-6):
    V=np.asarray(V,float); d=np.linalg.norm(V-V[i],axis=1); d[i]=np.inf
    dmin=d.min(); nb=np.where(np.abs(d-dmin)<tol*max(1,dmin))[0]; P=V[nb]
    # link-edges = neighbour pairs at the GLOBAL min distance
    DP=np.sqrt(((P[:,None]-P[None])**2).sum(-1)); np.fill_diagonal(DP,np.inf)
    e=DP.min(); A=(np.abs(DP-e)<tol*max(1,e)).astype(float)
    return P, A
TEMPLATES={  # (n_vertices, common_degree) -> name  (classical vertex figures)
    (3,2):"triangle",(4,2):"square",(5,2):"pentagon",(6,2):"hexagon",
    (4,3):"tetrahedron",(6,4):"octahedron",(8,3):"cube",(12,5):"icosahedron",(20,3):"dodecahedron"}
def classify_link(P,A):
    n=len(P); deg=A.sum(1)
    dcommon=int(round(deg[0])) if np.allclose(deg,deg[0]) else -1
    name=TEMPLATES.get((n,dcommon),"unknown")
    sig=tuple(SW.degeneracy_signature(np.linalg.eigvalsh(A)))
    return dict(n=n, degree=dcommon, name=name, spectrum_sig=sig)
def all_links(V):
    out=[classify_link(*link_graph(V,i)) for i in range(len(V))]
    names={o['name'] for o in out}; sigs={o['spectrum_sig'] for o in out}
    return out, dict(uniform=len(sigs)==1, distinct_names=sorted(names),
                     n_distinct_spectra=len(sigs))
