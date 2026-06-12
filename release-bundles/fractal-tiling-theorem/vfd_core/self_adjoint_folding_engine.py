"""WO-VFD-SELF-ADJOINT-FOLDING-ENGINE-002. Given a transformation T, search for an
invariant symmetric form B making T self-adjoint:  B T = T^T B  (<=> B T symmetric).
Generalises the mult-by-phi demo. Honest: this RECOVERS the classical symmetrizability
criterion -- a PD invariant form exists IFF T is real-diagonalizable (real spectrum).
It is a TOOL, not new mathematics."""
import numpy as np
def invariant_form_space(T):
    """Null space of B -> T^T B - B T over SYMMETRIC B. Returns (dim, basis_list)."""
    n=T.shape[0]; idx=[(i,j) for i in range(n) for j in range(i,n)]
    cols=[]
    for (a,b) in idx:
        E=np.zeros((n,n)); E[a,b]=1; E[b,a]=1
        cols.append((T.T@E - E@T).flatten())
    M=np.array(cols).T                      # n^2 x k
    # null space of M
    u,s,vt=np.linalg.svd(M)
    tol=1e-9*max(1,s.max() if s.size else 1)
    rank=int((s>tol).sum()); k=len(idx); null=vt[rank:]
    basis=[]
    for coeffs in null:
        B=np.zeros((n,n))
        for c,(a,b) in zip(coeffs,idx):
            B[a,b]+=c; 
            if a!=b: B[b,a]+=c
        basis.append(B)
    return k-rank, basis
def construct_PD_form(T):
    """If T is real-diagonalizable, build PD B with B T symmetric via B=(P^-1)^T(P^-1)."""
    w,P=np.linalg.eig(T)
    if np.max(np.abs(w.imag))>1e-9: return None,"complex spectrum -> no real self-adjoint form"
    if np.linalg.cond(P)>1e12: return None,"defective (non-diagonalizable) -> no PD form"
    P=P.real; S=np.linalg.inv(P); B=S.T@S
    B=(B+B.T)/2
    sa_resid=np.max(np.abs(B@T-(B@T).T))
    pd=np.linalg.eigvalsh(B).min()>1e-12
    return B,(f"PD={pd}, self-adjoint residual |BT-(BT)^T|={sa_resid:.2e}")
def analyze(name,T):
    w=np.linalg.eigvals(T); real=np.max(np.abs(w.imag))<1e-9
    dim,_=invariant_form_space(T); B,msg=construct_PD_form(T)
    found = B is not None and np.linalg.eigvalsh(B).min()>1e-12 and np.max(np.abs(B@T-(B@T).T))<1e-8
    return dict(name=name, eig_real=bool(real), invariant_form_space_dim=int(dim),
                PD_form_found=bool(found), note=msg)
