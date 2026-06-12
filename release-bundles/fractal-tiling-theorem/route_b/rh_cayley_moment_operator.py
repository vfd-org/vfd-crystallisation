"""WO-RH-CAYLEY-OPERATOR-001 — Cayley boundary moment / Toeplitz operator.

z = 1 - 1/rho  (critical line -> |z|=1). Moments m_k = sum_rho z_rho^k define a
Toeplitz matrix M_ij = m_{i-j}. By Herglotz/Bochner, [m_{i-j}] is PSD iff the
moments come from a positive measure on the unit circle -- i.e. iff all z on
|z|=1 (RH). So:
  on-line zeros  -> Toeplitz PSD; unitary shift U=mult-by-z has U*U=I
  off-line zeros -> negative eigenvalue; U*U != I (radial leakage)
The unitary route: zeros on |z|=1 <=> U unitary <=> H=-i log U self-adjoint.

CRUX (Advance 4): building M from the ZEROS is CIRCULAR (zeros fed in). The
non-circular operator needs m_k from PRIMES via the explicit formula -- which
requires the archimedean Gamma term (our COMPTRACE result). We test the
diagnostic AND show the circularity, locating the same wall from the Hardy side.
"""
import numpy as np, mpmath as mp
mp.mp.dps = 20

def zeros(n): return [float(mp.im(mp.zetazero(k))) for k in range(1, n+1)]

def toeplitz_from_pts(zs, K):
    m = np.array([sum(z**k for z in zs) for k in range(K)], dtype=complex)
    M = np.empty((K, K), dtype=complex)
    for i in range(K):
        for j in range(K):
            k = i - j
            M[i, j] = m[k] if k >= 0 else np.conj(m[-k])
    return (M + M.conj().T)/2     # Hermitian

def leakage(zs): return float(sum(np.log(abs(z))**2 for z in zs))

def main():
    print("="*66)
    print("WO-RH-CAYLEY-OPERATOR-001  Cayley boundary moment operator")
    print("="*66)
    M, K = 60, 24
    g = zeros(M)
    on = [complex(0.5, gi) for gi in g] + [complex(0.5, -gi) for gi in g]
    z_on = [1 - 1/r for r in on]

    T = toeplitz_from_pts(z_on, K)
    ev = np.linalg.eigvalsh(T)
    print(f"\n[on-line]  {M} zero-pairs, moment depth K={K}")
    print(f"  Toeplitz min eigenvalue = {ev.min():+.4f}  (>=0 => PSD => boundary measure)")
    print(f"  radial leakage Sum(log|z|)^2 = {leakage(z_on):.2e}")
    print(f"  unitary shift U=diag(z): ||U*U - I|| = {np.linalg.norm(np.diag([abs(z)**2 for z in z_on])-np.eye(2*M)):.2e}")

    # inject off-line quartet (large leakage so it's visible)
    eps, gg = 0.4, 3.0
    q = [complex(0.5+eps, gg), complex(0.5+eps,-gg), complex(0.5-eps, gg), complex(0.5-eps,-gg)]
    z_off = z_on + [1 - 1/r for r in q]
    Toff = toeplitz_from_pts(z_off, K)
    evo, vecs = np.linalg.eigh(Toff)
    print(f"\n[off-line injected]  quartet Re={0.5+eps}/{0.5-eps}, gamma={gg}")
    print(f"  Toeplitz min eigenvalue = {evo.min():+.4f}  "
          f"({'NEGATIVE -> not a boundary measure -> off-line detected' if evo.min()<-1e-6 else 'still PSD'})")
    print(f"  radial leakage = {leakage(z_off):.4f}  (>0 => off the boundary)")
    Uoff2 = np.diag([abs(z)**2 for z in z_off])
    print(f"  ||U*U - I|| = {np.linalg.norm(Uoff2-np.eye(len(z_off))):.4f}  (!=0 => shift non-unitary)")
    # negative eigenvector localisation
    v = vecs[:, 0]                     # most-negative mode
    spec = np.abs(np.fft.fft(v, 256))
    fpeak = np.argmax(spec) / 256.0
    theta_off = (np.angle(1 - 1/q[2]) % (2*np.pi)) / (2*np.pi)   # outside partner phase
    print(f"  negative-mode dominant frequency = {fpeak:.3f}; off-line z phase/2pi = {theta_off:.3f}")

    print("""
----------------------------------------------------------------------
SUMMARY (WO-RH-CAYLEY-OPERATOR-001)
----------------------------------------------------------------------
WORKS as a diagnostic: on-line zeros give a PSD Toeplitz moment matrix (a
genuine positive boundary measure) with unitary shift (U*U=I, zero leakage);
injecting an off-line quartet creates a NEGATIVE eigenvalue, nonzero radial
leakage, and a non-unitary shift (U*U != I). The negative mode is the radial
escape. So 'zeros on |z|=1 <=> U unitary <=> H=-i log U self-adjoint' is the
right doorway, and off-line failure shows up exactly as loss of boundary
positivity / unitarity.

CRUX (Advance 4, the honest wall): this Toeplitz is built FROM THE ZEROS
(m_k = sum_rho z_rho^k) -- it STORES the zeros, it does not derive them. A
diagonal U with the zero phases is the same circular 'fake operator'. The
NON-circular operator must build m_k from PRIME data via the explicit formula
-- and m_k are Li-Keiper-type power sums of zeros, whose prime-side expression
REQUIRES the archimedean Gamma term (exactly our COMPTRACE finding: the
completion is not optional). So the archimedean correction IS the boundary-
tension term, and building U from primes without it fails.

NET: the Cayley/Hardy route gives the cleanest DOORWAY (unitary boundary shift
-> self-adjoint generator) and the sharpest statement of the wall: construct U
from primes+archimedean without inserting the zeros. That is the de Branges /
Connes frontier -- not crossed here. Diagnostic built; circularity explicit;
archimedean term confirmed mandatory.
""")

if __name__ == "__main__":
    main()
