"""Phase 4: perturb a polytope (field pressure) and measure degeneracy splitting."""
import numpy as np, standing_wave_modes as SW
def perturb(V, eps, seed=0):
    rng=np.random.default_rng(seed); return np.asarray(V,float)+eps*rng.standard_normal(np.asarray(V).shape)
def degeneracy_splitting(V, eps, seed=0):
    """max spread inside each originally-degenerate adjacency cluster after perturbation."""
    A0=SW.build_graph(V); w0=np.round(np.linalg.eigvalsh(A0),5)
    # cluster indices by original eigenvalue
    clusters={}
    for i,v in enumerate(w0): clusters.setdefault(round(float(v),4),[]).append(i)
    Vp=perturb(V,eps,seed); 
    # keep SAME edge set (topology fixed; weights/positions strain) -> use weighted Laplacian of strained metric
    Vp=np.asarray(Vp); n=len(Vp)
    Dp=np.sqrt(((Vp[:,None,:]-Vp[None,:,:])**2).sum(-1))
    A0e=(A0>0); Aw=np.where(A0e, 1.0/np.maximum(Dp,1e-9), 0.0); Aw=(Aw+Aw.T)/2
    wp=np.sort(np.linalg.eigvalsh(Aw))
    # match counts: measure spread of perturbed spectrum within each degenerate block (by rank order)
    w0s=np.sort(w0); 
    # spread = for each degeneracy>1 block, max-min of corresponding perturbed eigenvalues
    idx=0; splits=[]
    for val,cnt in [(v,len(ix)) for v,ix in sorted(clusters.items())]:
        block=wp[idx:idx+cnt]; idx+=cnt
        if cnt>1: splits.append(float(block.max()-block.min()))
    return max(splits) if splits else 0.0
