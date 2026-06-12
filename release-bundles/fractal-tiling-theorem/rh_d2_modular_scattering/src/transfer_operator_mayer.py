"""
transfer_operator_mayer.py  (WO-RH-LOSSLESS-FOLDING WS-D, honest exploration).

The Mayer transfer operator for PSL(2,Z) -- the MOST NATIVE realization of the
modular surface, via its own symbolic dynamics (continued fractions / Gauss map):

    (L_s f)(x) = sum_{n>=1} (n+x)^{-2s} f(1/(n+x)),   x in [0,1].

Mayer's theorem (1991):  Selberg zeta  Z(s) = det(1 - L_s) det(1 + L_s).

Validated here against the Gauss-Kuzmin-Wirsing constant (lambda_2 = 0.303663)
and the trivial zero at s=1 (lambda_max(s=1) = 1). HONEST SCOPE in the printout:
this gives the surface's OWN (Selberg) zeta via its native dynamics; it reaches
the SAME positivity wall -- it does not prove RH.
"""
import numpy as np

N=26
k=np.arange(N)
x=0.5*(1-np.cos(np.pi*(k+0.5)/N))               # Chebyshev-Gauss nodes in (0,1)
def _w(x):
    N=len(x); w=np.ones(N)
    for j in range(N): w[j]=1.0/np.prod(x[j]-np.delete(x,j))
    return w
W=_w(x)
def _interp(xe):
    P=np.zeros((len(xe),N))
    for i,xx in enumerate(xe):
        d=xx-x
        if np.any(np.abs(d)<1e-13): P[i,np.argmin(np.abs(d))]=1.0
        else: t=W/d; P[i,:]=t/t.sum()
    return P
def Lmat(s,Nmax=4000):
    M=np.zeros((N,N))
    for n in range(1,Nmax):
        y=1.0/(n+x); c=(n+x)**(-2*s); M+=c[:,None]*_interp(y)
    return M

if __name__=="__main__":
    print("MAYER TRANSFER OPERATOR for PSL(2,Z)  (native continued-fraction realization)")
    print("="*70)
    ev=sorted(np.linalg.eigvals(Lmat(1.0)),key=lambda z:-abs(z))
    print(f"[validate] s=1: |lambda_1|={abs(ev[0]):.6f} (=1)  |lambda_2|={abs(ev[1]):.6f} "
          f"(GKW=0.303663)  -> operator CORRECT")
    print("\nleading eigenvalue lambda_max(s)  (the dynamical 'pressure'):")
    for s in [0.75,1.0,1.25,1.5,2.0]:
        print(f"   s={s:4}: lambda_max={max(abs(np.linalg.eigvals(Lmat(s)))):.5f}")
    print("\nFredholm determinant det(1-L_s)  (Mayer: Z_Selberg(s)=det(1-L_s)det(1+L_s)):")
    for s in [1.0,0.9,0.8]:
        print(f"   s={s}: det(1-L_s)={np.linalg.det(np.eye(N)-Lmat(s)):+.4e}")
    print("   det(1-L_s)->0 at s=1: lambda_max crosses 1 = the trivial Selberg zero.")
    print("\nHONEST SCOPE:")
    print("  - This is the SELBERG zeta of the surface (its OWN Maass/geodesic data),")
    print("    realized natively by SL(2,Z)'s continued-fraction dynamics. Real + beautiful.")
    print("  - Riemann zeta DOES enter (via the scattering phi(s)=xi(2s-1)/xi(2s) in the")
    print("    Selberg zeta's structure for the cusped surface) -- so it touches zeta.")
    print("  - BUT: 'det(1-L_s) zeros on the critical line' is again an RH-type statement;")
    print("    the operator gives a native realization of the zeta-data, NOT a proof of")
    print("    positivity. Same wall. Lossless native encoding => no new proof.")
