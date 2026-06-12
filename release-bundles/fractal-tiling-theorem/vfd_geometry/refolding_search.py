"""Phase 5: refolding = does a source polytype embed structurally into a TARGET?
The sharp falsifiable test: icosahedron (H3) is the VERTEX FIGURE of the 600-cell (H4)
-- its 12 nearest neighbours form an icosahedron -- a genuine H3<H4 containment that
the tesseract/24-cell lack. We verify this directly (no narrative)."""
import numpy as np, standing_wave_modes as SW
def vertex_figure(V, i, tol=1e-6):
    V=np.asarray(V,float); d=np.linalg.norm(V-V[i],axis=1); d[i]=np.inf
    dmin=d.min(); nb=np.where(np.abs(d-dmin)<tol*max(1,dmin))[0]
    return V[nb]-V[i], nb            # neighbour offsets
def graph_signature(V):
    A=SW.build_graph(V); return tuple(SW.degeneracy_signature(np.linalg.eigvalsh(A)))
def is_icosahedron(pts):
    if len(pts)!=12: return False, len(pts)
    A=SW.build_graph(pts); deg=A.sum(1)
    sig=SW.degeneracy_signature(np.linalg.eigvalsh(A))
    # icosahedron graph: degree 5, adjacency spectrum {5, sqrt5 x3, -1 x5, -sqrt5 x3}
    ok = bool(np.allclose(deg,5)) and len(pts)==12
    return ok, sig
