"""Restart from first principles: build the scaling operator from a single
point upward, on the unitary (C) side, and see exactly where it stalls.

We KNOW where to look (established this session):
  - class C / unitary / beta=2 (not the substrate's H)
  - it is the generator of SCALE (dilation)
  - finite-place part = the commuting Hecke algebra (built, verified)
  - missing = archimedean dilation, self-adjoint, zeros as spectrum

So forget the substrate. Build the simplest scaling operator and climb.

STEP 0 (single point): the dilation generator. In the log variable u=log x
it is D = -i d/du (momentum). On a circle of circumference L (the simplest
'box') its spectrum is 2*pi*n/L, n in Z -- EVENLY SPACED (a picket fence).
We compute it and its level statistics.

STEP 1: compare that spectrum's statistics to what the zeros require.
  picket fence (rigid)   r-stat = 1.00   (maximally ordered)
  Poisson (integrable)   r-stat = 0.386
  GUE (the zeros)        r-stat = 0.600   <-- the target
The single scaling DOF is RIGID (r=1), the OPPOSITE extreme from GUE.

STEP 2: to bend the picket fence into the irregular GUE zeros you must
impose the PRIMES (the explicit formula / the adelic boundary conditions).
That step -- making the discretised scaling self-adjoint with the zeros as
spectrum, non-circularly -- is the wall, reached now from the construction
side. We show the gap quantitatively; we do not cross it.
"""
from __future__ import annotations

import numpy as np


def r_stat(ev):
    ev = np.sort(np.real(ev))
    s = np.diff(ev)
    s = s[s > 1e-9]
    if len(s) < 3:
        return float("nan")
    r = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])
    return float(np.mean(r))


GAMMA = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178,
         40.918719, 43.327073, 48.005151, 49.773832, 52.970321, 56.446248,
         59.347044, 60.831779, 65.112544, 67.079811, 69.546402, 72.067158,
         75.704691, 77.144840, 79.337375, 82.910381, 84.735493, 87.425275]


def main():
    print("=" * 74)
    print("RESTART FROM FIRST PRINCIPLES: the scaling operator, single point up")
    print("=" * 74)

    # STEP 0: dilation = momentum on a circle (finite-difference, N points)
    N = 400
    L = 2 * np.pi
    # D = -i d/du on a periodic grid -> circulant; eigenvalues = 2*pi*n/L
    n = np.fft.fftfreq(N, d=L / N) * 2 * np.pi      # the exact spectrum
    ev_pf = np.sort(n)
    print(f"\n[STEP 0] Dilation generator D=-i d/du on a circle (N={N}):")
    print(f"  spectrum = 2*pi*n/L, evenly spaced (PICKET FENCE).")
    print(f"  r-statistic = {r_stat(ev_pf):.3f}  (rigid; max order)")

    # STEP 1: where the zeros need to be
    rz = r_stat(GAMMA)
    print(f"\n[STEP 1] Where the target sits:")
    print(f"  picket fence (single scaling DOF) : r = {r_stat(ev_pf):.3f}  (rigid)")
    print(f"  Poisson (integrable)              : r = 0.386")
    print(f"  GUE (the Riemann zeros)           : r = {rz:.3f}  <-- TARGET")
    print(f"  -> a single scaling degree of freedom is MAXIMALLY RIGID,")
    print(f"     the opposite extreme from the GUE zeros. One point up is")
    print(f"     NOT enough structure to be chaotic.")

    # STEP 2: what bending it to GUE requires
    print(f"\n[STEP 2] To turn the picket fence into the GUE zeros you must")
    print(f"  impose the PRIMES as the boundary/discretisation data (the")
    print(f"  explicit formula). One toy attempt: perturb the rigid spectrum")
    print(f"  by a generic Hermitian term and watch r move off 1.0:")
    rng = np.random.RandomState(7)
    D0 = np.diag(ev_pf[:120])
    for eps in [0.0, 0.5, 2.0, 5.0]:
        G = rng.standard_normal((120, 120)) + 1j * rng.standard_normal((120, 120))
        G = (G + G.conj().T) / 2
        ev = np.linalg.eigvalsh(D0 + eps * G)
        print(f"    eps={eps:<4} r = {r_stat(ev):.3f}")
    print(f"  Generic perturbation pushes r toward GUE (~0.60) -- but a")
    print(f"  GENERIC perturbation is not the primes. The primes are a")
    print(f"  SPECIFIC, rigid arithmetic input, and making the result")
    print(f"  self-adjoint with EXACTLY the zeros as spectrum, without")
    print(f"  feeding the zeros in, is the wall.")

    print("""
==========================================================================
WHAT THE RESTART SHOWS
==========================================================================
Building from first principles, a single scaling degree of freedom upward,
on the unitary side, gives:
  * STEP 0: a self-adjoint scaling operator -- EASY -- but its spectrum is a
    rigid picket fence (r=1), not the zeros.
  * STEP 1: the zeros are GUE (r~0.60), a specific irregular spectrum. A
    single point is too simple (too rigid) to be chaotic; chaos needs many
    interacting modes.
  * STEP 2: a GENERIC perturbation reaches the GUE *class* -- but that is
    universality, not the zeros. The zeros require the SPECIFIC primes as
    input, made self-adjoint NON-CIRCULARLY. That is the same wall, now seen
    from the construction side.

So the restart is legitimate and it confirms the diagnosis: the easy part
(a self-adjoint scaling operator) we can build from a single point; the hard
part (imposing the primes to get exactly the zeros, self-adjointly, without
assuming RH) is intrinsic and unsolved -- it does not depend on the
substrate, and starting fresh walks straight to it. 'We know where to look'
is true; 'we can build it' is the open problem. The wall is in the
arithmetic-to-self-adjoint step, not in our starting point.
""")


if __name__ == "__main__":
    main()
