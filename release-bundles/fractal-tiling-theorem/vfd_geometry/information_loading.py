"""Phase 3: mode-depth / energy / entropy loading on the standing-wave basis."""
import numpy as np
def load(eigvals, m, scheme="mode_depth", seed=0):
    rng=np.random.default_rng(seed); k=len(eigvals)
    a=np.zeros(k); a[:m]=1.0
    if scheme=="random": a[:m]=np.abs(rng.standard_normal(m))
    p=a**2/ (a**2).sum() if a.sum()>0 else a
    energy=float((a**2*eigvals).sum())
    entropy=float(-(p[p>0]*np.log(p[p>0])).sum())
    return dict(scheme=scheme, load_level=m, modal_energy=energy, modal_entropy=entropy)
