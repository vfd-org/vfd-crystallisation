"""WO-RH-DEBRANGES-KERNEL-001 — de Branges reproducing-kernel cross-check.

Canonical candidate E1(z) = xi(1/2 - i z) + i xi'(1/2 - i z).
If xi's zeros are real (RH), E1 is Hermite-Biehler (zeros in the lower half-
plane) and its de Branges kernel is PSD. We test, as an INDEPENDENT cross-check
of the validated Weil/Connes positive form:
  * Hermite-Biehler condition |E#(z)| < |E(z)| for Im z>0  (<=> RH for this E);
  * de Branges kernel Gram PSD on a real grid;
  * archimedean ablation: zeta-only E (no Gamma) should degrade HB/PSD.
CROSS-CHECK, NOT PROOF: E1 is built from the completed xi (allowed input), which
'contains' the zeros; PSD/HB here REFLECT RH-true-so-far, they do not force it.
Real-grid kernel formulas (E=A-iB, A=Re E, B=-Im E):
  K(x,y) = Im(E(y) conj(E(x))) / (pi (x-y)),   K(x,x) = (A'B - A B')/pi.
"""
import numpy as np, mpmath as mp
mp.mp.dps = 30

def xi(s):
    s = mp.mpc(s)
    if abs(s-1) < mp.mpf(10)**(-12): s = s + mp.mpf(10)**(-12)
    if abs(s) < mp.mpf(10)**(-12):   s = s + mp.mpf(10)**(-12)
    return 0.5*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
def xip(s):  # xi'(s)
    return mp.diff(xi, s)
def zeta_only(s):   # archimedean-ablated proxy: drop the Gamma/pi completion
    s = mp.mpc(s)
    if abs(s-1) < mp.mpf(10)**(-12): s = s + mp.mpf(10)**(-12)
    return mp.zeta(s)
def zeta_only_p(s):
    return mp.diff(zeta_only, s)

def E1(z, comp=False):
    # proper Hermite-Biehler candidate E = A - i A', A(z)=xi(1/2-iz), A'=dA/dz
    if comp:
        A = lambda t: zeta_only(mp.mpf('0.5') - 1j*t)
    else:
        A = lambda t: xi(mp.mpf('0.5') - 1j*t)
    return A(z) + 1j*mp.diff(A, z)   # HB orientation (sign is a convention; see report)
def Esharp(z, comp=False):
    return mp.conj(E1(mp.conj(z), comp))

def hermite_biehler(comp=False, n=60):
    # sample upper half plane, check |E#|<|E|
    pts = [(x, y) for x in (-6,-3,0,3,6) for y in (0.5,1.0,2.0,4.0)]
    viol=0; mx=mp.mpf(0)
    for x,y in pts:
        z=mp.mpc(x,y)
        e=abs(E1(z,comp)); es=abs(Esharp(z,comp))
        if es>=e: viol+=1
        mx=max(mx, es-e)
    return 1-viol/len(pts), float(mx)

def gram(comp=False, grid=None):
    xs=grid
    n=len(xs)
    # precompute E(x) for real x, and A,B,A',B'
    Ev=[E1(mp.mpf(x),comp) for x in xs]
    G=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if i==j:
                x=mp.mpf(xs[i])
                A=lambda t: mp.re(E1(t,comp)); B=lambda t: -mp.im(E1(t,comp))
                val=(mp.diff(A,x)*B(x)-A(x)*mp.diff(B,x))/mp.pi
                G[i,j]=float(val)
            else:
                num=mp.im(Ev[j]*mp.conj(Ev[i]))
                G[i,j]=float(num/(mp.pi*(mp.mpf(xs[i])-mp.mpf(xs[j]))))
    return (G+G.T)/2

def main():
    print("="*64)
    print("WO-RH-DEBRANGES-KERNEL-001  de Branges kernel cross-check")
    print("="*64)
    print("\nCandidate E1(z) = xi(1/2-iz) + i xi'(1/2-iz)")

    pr, mxv = hermite_biehler(False)
    prz, mxz = hermite_biehler(True)
    print(f"\n[Hermite-Biehler] |E#(z)|<|E(z)| on 20 UHP points:")
    print(f"  completed xi : pass ratio = {pr:.2f}  (max |E#|-|E| = {mxv:.2e})")
    print(f"  zeta-only(no Gamma): pass ratio = {prz:.2f}  (max = {mxz:.2e})  [archimedean ablation]")

    grid=[float(v) for v in np.linspace(-8,8,12)]
    G=gram(False, grid); Gz=gram(True, grid)
    ec=np.linalg.eigvalsh(G); ez=np.linalg.eigvalsh(Gz)
    print(f"\n[de Branges kernel Gram, N=12 real grid]")
    print(f"  completed xi : min eig = {ec.min():+.4e}  {'PSD' if ec.min()>-1e-6*abs(ec).max() else 'NOT PSD'}")
    print(f"  zeta-only    : min eig = {ez.min():+.4e}  {'PSD' if ez.min()>-1e-6*abs(ez).max() else 'NOT PSD'}  [ablation]")

    print("""
----------------------------------------------------------------------
SUMMARY (WO-RH-DEBRANGES-KERNEL-001)
----------------------------------------------------------------------
Cross-check from the de Branges side. Read honestly:
 * E1 from the COMPLETED xi: Hermite-Biehler condition and kernel-Gram PSD
   should hold (reflecting the zeros being on the line) -- the SAME positive
   structure the Weil/Connes route found, now in de Branges language.
 * ZETA-ONLY (archimedean ablated): HB/PSD should degrade -> the archimedean
   completion again carries the positivity (consistent with B and C).
This is a CROSS-CHECK, NOT a proof: E1 is built from xi (allowed), which already
encodes the zeros, so PSD/HB REFLECT RH-true-so-far; they do not force it. The
canonical Hermite-Biehler/de Branges function and finite-domain stability remain
the missing object (= WO-DEBRANGES-SPACE-002). No zeros inserted by hand; no phi.
""")

if __name__=="__main__":
    main()
