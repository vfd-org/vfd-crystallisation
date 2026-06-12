"""Standing-wave spectra of polytope graphs (WO-VFD-POLYTYPE-STANDING-WAVE-EXT-001).
Build the 1-skeleton (min-distance adjacency), compute adjacency/Laplacian spectra,
degeneracy signature (= symmetry capacity), spectral gap/entropy. Honest: this is
standard spectral graph theory; degeneracies encode the symmetry group's irreps."""
import numpy as np
def build_graph(V, tol=1e-6):
    V=np.asarray(V,float); n=len(V)
    D=np.sqrt(((V[:,None,:]-V[None,:,:])**2).sum(-1)); np.fill_diagonal(D,np.inf)
    dmin=D.min(); A=(np.abs(D-dmin)<tol*max(1,dmin)).astype(float)
    return A
def spectra(A):
    deg=A.sum(1); L=np.diag(deg)-A
    aw=np.linalg.eigvalsh(A); lw=np.linalg.eigvalsh(L)
    return dict(adjacency=aw, laplacian=lw, degree=deg)
def degeneracy_signature(w, nd=4):
    wr=np.round(w,nd); vals,counts=np.unique(wr,return_counts=True)
    order=np.argsort(-vals)
    return [(float(vals[i]),int(counts[i])) for i in order]
def spectral_entropy(w):
    p=np.abs(w-w.min())+1e-12; p=p/p.sum(); return float(-(p*np.log(p)).sum())
def spectral_gap(A):
    w=np.sort(np.linalg.eigvalsh(A))[::-1]; return float(w[0]-w[1])
def participation(vec):
    p=np.abs(vec)**2; return float((p.sum()**2)/(p**2).sum())
