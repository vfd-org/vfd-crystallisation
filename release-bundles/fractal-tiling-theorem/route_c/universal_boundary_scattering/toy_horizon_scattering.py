"""Toy horizon instance: Poschl-Teller barrier V(x)=V0 sech^2(alpha x) -- the STANDARD
analytic QNM model in black-hole ringdown (Ferrari-Mashhoon; Berti-Cardoso-Starinets).
Schrodinger -psi'' + V psi = omega^2 psi.

Scattering determinant (Gamma-ratio):  Delta(omega) = 1/[Gamma(1/2+i nu - i w)Gamma(1/2-i nu - i w)]
  with w=omega/alpha, nu=sqrt(V0/alpha^2 - 1/4). Zeros of Delta = QNMs.
QNMs:  omega_n = alpha[ +-nu - i(n+1/2) ]  (LOWER half-plane => damped => STABLE,
  GUARANTEED by self-adjointness of a real potential).
Greybody (transmission probability): |T|^2 = sinh^2(pi w)/(sinh^2(pi w)+cosh^2(pi nu)).
Boundary response = digamma psi  (same functional object as the arithmetic archimedean term).
"""
import mpmath as mp, math
mp.mp.dps=25
def nu(V0=1.0,alpha=1.0): return mp.sqrt(mp.mpf(V0)/alpha**2 - mp.mpf(1)/4)
def qnms(V0=1.0,alpha=1.0,N=6):
    n=nu(V0,alpha); out=[]
    for k in range(N):
        out.append(complex(alpha*( n - 1j*(k+0.5))))
        out.append(complex(alpha*(-n - 1j*(k+0.5))))
    return out
def determinant(omega,V0=1.0,alpha=1.0):
    w=mp.mpc(omega)/alpha; n=nu(V0,alpha)
    return 1/(mp.gamma(mp.mpf(1)/2+1j*n-1j*w)*mp.gamma(mp.mpf(1)/2-1j*n-1j*w))
def response(omega,V0=1.0,alpha=1.0):   # -Delta'/Delta = (i/alpha)[psi(1/2+i nu-i w)+psi(1/2-i nu-i w)]
    w=mp.mpc(omega)/alpha; n=nu(V0,alpha)
    return (1j/alpha)*(mp.digamma(mp.mpf(1)/2+1j*n-1j*w)+mp.digamma(mp.mpf(1)/2-1j*n-1j*w))
def greybody(omega,V0=1.0,alpha=1.0):
    w=float(mp.re(omega))/alpha; n=float(nu(V0,alpha).real)
    return math.sinh(math.pi*w)**2/(math.sinh(math.pi*w)**2+math.cosh(math.pi*n)**2)
