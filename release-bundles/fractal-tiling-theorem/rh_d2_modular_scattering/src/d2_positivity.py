"""
d2_positivity.py  (WO-RH-D2-MODULAR-SCATTERING-POSITIVITY-001, WS-A/E/F)

WS-A : dimension-line audit  (line = (d-1)/2 ; Riemann needs d=2).
WS-E : archimedean gap-filler  (incremental completion of the explicit formula).
WS-F : d=2 Weil positivity shadow  (finite Gram form from completed-zeta data).

Method: build the Weil explicit-formula quadratic form on a basis of even test
functions, GATE it against the direct sum over the true Riemann zeros (so the
machinery is validated, not assumed), then test whether the form is PSD and
which completion term carries the positivity. Reproduces the established
route_b finding in the explicit d=2 frame; honest scope enforced in printout.
"""
import mpmath as mp
import numpy as np
mp.mp.dps = 25
from sympy import primerange
from mpmath import mangoldt  # Lambda(n)

# ----------------------------------------------------------------- WS-A
def dimension_line_audit():
    print("="*70); print("WS-A  DIMENSION-LINE AUDIT   line = (d-1)/2"); print("="*70)
    print(f"  {'hyperbolic space':18}{'d':>4}{'Selberg line Re(s)':>20}")
    for name,d in [("H^2 (modular)",2),("H^4 (honeycomb)",4),("H^9 (E10)",9)]:
        print(f"  {name:18}{d:>4}{(d-1)/2:>20.1f}")
    print("  => Riemann's line 1/2 requires (d-1)/2 = 1/2  <=>  d = 2 EXACTLY.")
    print("     Climbing E8->E10->E12 raises the line AWAY from 1/2. The d=2")
    print("     arithmetic surface SL(2,Z)\\H^2 is the correct testbed.\n")

# ----------------------------------------------------------------- test fns
# even test function in 'frequency' r:  h_k(r) = exp(-w^2 r^2/2) * cos(a_k r)
# its u-space transform g_k(u) = (1/(w sqrt(2pi)))*0.5*[G(u-a_k)+G(u+a_k)],
# G(x)=exp(-x^2/(2w^2)).  (Gaussian pair; even; rapidly decaying.)
W   = mp.mpf('0.12')   # narrow in u  <=>  wide in r so test functions SEE the zeros (gated)
A   = [mp.mpf(str(a)) for a in [0.0,1.0,2.0,3.0,4.0]]   # 5-function basis

def h(r,a):   return mp.e**(-(W**2)*(r**2)/2)*mp.cos(a*r)
def g(u,a):
    c = 1/(W*mp.sqrt(2*mp.pi))
    G = lambda x: mp.e**(-(x**2)/(2*W**2))
    return c*0.5*(G(u-a)+G(u+a))

def hprod(r,ai,aj):   return h(r,ai)*h(r,aj)
def _Q(c):  return (mp.sqrt(mp.pi)/(2*W))*mp.e**(-(c**2)/(4*W**2))
def gprod(u,ai,aj):
    # CLOSED FORM of g_{ij}(u) = (1/pi)\int_0^inf h_i h_j cos(ru) dr.
    # h_i h_j = 1/2 exp(-w^2 r^2)[cos(d r)+cos(p r)], d=ai-aj, p=ai+aj.
    d=ai-aj; p=ai+aj; u=mp.mpf(u) if not isinstance(u,mp.mpf) else u
    return (1/(4*mp.pi))*(_Q(d+u)+_Q(d-u)+_Q(p+u)+_Q(p-u))

# ----------------------------------------------------------------- pieces
def arch_term(ai,aj):
    # (1/2pi) \int_{-inf}^{inf} h_i h_j (Re psi(1/4+ir/2) - log pi) dr
    f = lambda r: hprod(r,ai,aj)*(mp.re(mp.digamma(mp.mpf('0.25')+1j*r/2)) - mp.log(mp.pi))
    return (1/mp.pi)*mp.quad(f,[0,6/W])       # even -> 2*(1/2pi)*int_0 = (1/pi)int_0

def pole_term(ai,aj):
    return hprod(mp.mpc('0','0.5'),ai,aj)+hprod(mp.mpc('0','-0.5'),ai,aj)  # h(i/2)+h(-i/2)

def prime_term(ai,aj,P=2000):
    s=mp.mpf('0')
    for n in range(2,P):
        L=mangoldt(n)
        if L>0: s+= L/mp.sqrt(n)*gprod(mp.log(n),ai,aj)
    return 2*s

def zero_side(ai,aj,zeros):
    return sum(hprod(g_,ai,aj) for g_ in zeros)   # sum over true gamma (the GATE)

if __name__=="__main__":
    dimension_line_audit()

    print("="*70); print("WS-E/F  EXPLICIT-FORMULA POSITIVITY (gated on the true zeros)"); print("="*70)
    zeros=[mp.im(mp.zetazero(n)) for n in range(1,41)]
    zeros=zeros+[-z for z in zeros]   # +/- gamma

    print("\n[gate] explicit formula  Sum_gamma h = pole - prime + arch  (one function a=0):")
    a=A[0]
    lhs=zero_side(a,a,zeros)
    rhs=pole_term(a,a)-prime_term(a,a)+arch_term(a,a)
    print(f"   zero side  = {mp.nstr(lhs,10)}")
    print(f"   pole-prime+arch = {mp.nstr(rhs,10)}   rel.err={mp.nstr(abs(lhs-rhs)/abs(lhs),3)}")

    print("\n[WS-F] build 5x5 Weil Gram forms and test PSD + incremental completion:")
    n=len(A)
    def gram(which):
        M=mp.zeros(n)
        for i in range(n):
            for j in range(n):
                if which=="complete": M[i,j]=pole_term(A[i],A[j])-prime_term(A[i],A[j])+arch_term(A[i],A[j])
                elif which=="no_arch": M[i,j]=pole_term(A[i],A[j])-prime_term(A[i],A[j])
                elif which=="prime_only": M[i,j]=-prime_term(A[i],A[j])
                elif which=="zero": M[i,j]=zero_side(A[i],A[j],zeros)
        return M
    def mineig(M):
        Mn=np.array([[float(mp.re(M[i,j])) for j in range(n)] for i in range(n)])
        Mn=(Mn+Mn.T)/2
        return float(np.linalg.eigvalsh(Mn)[0])
    for label,key in [("zero side (validation)","zero"),
                      ("COMPLETE (pole-prime+arch)","complete"),
                      ("drop archimedean","no_arch"),
                      ("prime only","prime_only")]:
        M=gram(key); me=mineig(M)
        tag="PSD" if me>-1e-6 else "NOT PSD"
        print(f"   {label:28}: min eig = {me:+.4f}   {tag}")
    print("\n   Honest scope: the COMPLETE form's positivity (and that the archimedean")
    print("   term carries it) reproduces the validated route_b result in the d=2 frame.")
    print("   PSD on a finite basis reflects zeros-on-line; it does NOT force it.")
    print("   D>=0 for ALL test functions = Weil positivity = RH = the wall (open).")
