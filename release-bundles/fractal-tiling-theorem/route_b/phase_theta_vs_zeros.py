"""Phase-Theta operator spectrum vs the Riemann zeros -- controlled test.

CONFIRMED ON THE REAL OPERATOR (2026-05-31): the actual
tranformation-engine/aria_runtime/algebra/phase_theta_field.py was loaded and
run. With void_init(K=200, r=50) the real hermitian_gram() is RANK-1 (one
nonzero eigenvalue = 200, plus 199 exact zeros), because void_init gives every
concept the same sin(k*pi/phi) pattern times a per-concept phase => Z is a
rank-1 outer product. affine RMSE to the zeros = 104 vs GUE-control 8.9.
NO MATCH, even more degenerate than the reconstruction below.

This file is a FAITHFUL RECONSTRUCTION of the operator (used when the real file
was not yet located):
  * RotatE-style phase embedding: N entities, each a length-d vector of
    unit-modulus complex numbers e^{i theta};
  * void-phase initialisation theta ~ sin(k*pi/phi) (as reported);
  * Hermitian Gram coupling operator G = Z Z^dagger (exactly Hermitian,
    real spectrum -- automatically, for any complex Z).

Question: does the spectrum of G match the Riemann zeros better than controls?
Controls: (a) random-phase Gram (no sin init); (b) GUE eigenvalues.
Honest design: a MATCH must beat the controls; otherwise NO MATCH.

Expected on structural grounds (stated before running): NO MATCH -- G's
nonzero eigenvalues are singular-values-squared of a bounded phase matrix
(a bounded clump + a large rank-deficiency 'null'), while the zeros grow ~
n log n (unbounded) with GUE spacing. No arithmetic enters G, so no channel
links it to zeta. We run it to confirm, not to assume.
"""
from __future__ import annotations

import math
import numpy as np
import mpmath as mp

PHI = (1 + math.sqrt(5)) / 2


def zeros(n):
    mp.mp.dps = 20
    return np.array([float(mp.im(mp.zetazero(k))) for k in range(1, n + 1)])


def r_stat(ev):
    ev = np.sort(np.real(ev))
    s = np.diff(ev); s = s[s > 1e-9]
    if len(s) < 3:
        return float("nan")
    r = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])
    return float(np.mean(r))


def phase_embedding(N, d, rng, void_init=True):
    """N entities x d complex unit-modulus coords; void-phase or random init."""
    if void_init:
        k = np.arange(1, N * d + 1).reshape(N, d)
        theta = 2 * math.pi * np.sin(k * math.pi / PHI)        # 'void' sin init
    else:
        theta = rng.uniform(0, 2 * math.pi, (N, d))
    return np.exp(1j * theta)                                   # Z (N x d)


def gram_spectrum(Z):
    G = Z @ Z.conj().T                                         # Hermitian N x N
    asym = np.linalg.norm(G - G.conj().T)                     # ~0 by construction
    ev = np.linalg.eigvalsh(G)                                # real spectrum
    return ev, asym


def gue_eigs(N, rng):
    A = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
    H = (A + A.conj().T) / 2
    return np.sort(np.linalg.eigvalsh(H))


def affine_rmse(x, y):
    """min RMSE of a*x+b -> y over sorted x (len = len y)."""
    x = np.sort(np.real(x))[-len(y):]                         # top-|y| eigenvalues
    A = np.vstack([x, np.ones_like(x)]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    return math.sqrt(np.mean((A @ coef - y) ** 2))


def main():
    print("=" * 74)
    print("PHASE-THETA OPERATOR SPECTRUM vs RIEMANN ZEROS (reconstruction)")
    print("=" * 74)
    N, d = 200, 32
    rng = np.random.RandomState(31)
    g = zeros(N)

    Z = phase_embedding(N, d, rng, void_init=True)
    ev, asym = gram_spectrum(Z)
    nz = np.sum(ev > 1e-8)
    print(f"\nReconstructed phase-Theta Gram G=ZZ^dag  (N={N}, d={d})")
    print(f"  Hermitian check ||G - G^dag|| = {asym:.2e}  (self-adjoint, trivially)")
    print(f"  spectrum: {nz} nonzero eigenvalues + {N-nz} ZERO eigenvalues "
          f"(the 'null'); range [{ev.min():.2f}, {ev.max():.2f}]")
    print(f"  -> bounded (max {ev.max():.1f}); zeros are unbounded "
          f"(gamma_{N}={g[-1]:.0f}, -> infinity)")

    # spacing statistic <r>
    r_phase = r_stat(ev[ev > 1e-8])
    r_zero = r_stat(g)
    r_gue = r_stat(gue_eigs(N, rng))
    print(f"\nSpacing ratio <r> (unfolding-free):")
    print(f"  phase-Theta nonzero spectrum : {r_phase:.3f}")
    print(f"  Riemann zeros                : {r_zero:.3f}")
    print(f"  GUE                          : {r_gue:.3f}  (zeros' true class)")

    # best affine fit to first N zeros, vs controls
    rmse_phase = affine_rmse(ev, g)
    Zr = phase_embedding(N, d, rng, void_init=False)
    evr, _ = gram_spectrum(Zr)
    rmse_rand = affine_rmse(evr, g)
    rmse_gue = affine_rmse(gue_eigs(N, rng), g)
    print(f"\nBest affine fit of spectrum -> the {N} zeros (RMSE, lower=better):")
    print(f"  phase-Theta (sin/void init): {rmse_phase:.2f}")
    print(f"  random-phase control       : {rmse_rand:.2f}")
    print(f"  GUE control                : {rmse_gue:.2f}")

    beats = rmse_phase < 0.5 * min(rmse_rand, rmse_gue)
    matches_class = abs(r_phase - r_zero) < 0.05
    print("\n" + "-" * 74)
    print(f"VERDICT (fit): {'MATCH' if beats else 'NO MATCH'} -- phase-Theta "
          f"{'beats' if beats else 'does NOT beat'} the controls at tracking the zeros")
    print(f"VERDICT (class): {'same spacing class' if matches_class else 'different spacing class'} "
          f"(phase <r>={r_phase:.3f} vs zeros {r_zero:.3f})")
    print("""
==========================================================================
WHAT THE DATA SAYS
==========================================================================
The phase-Theta operator is self-adjoint -- trivially (any ZZ^dag is). But its
spectrum is a BOUNDED clump of singular-values-squared plus a large block of
exact-zero eigenvalues (the 'null' = rank deficiency, d<N). The Riemann zeros
are UNBOUNDED and GUE-spaced. There is no affine rescaling that tracks them
(it does not beat random/GUE controls), and the spacing class differs.

This is the same structural verdict as the substrate's C_phi (TEST 3 of
geometry_match): a finite/bounded semantic operator cannot encode the infinite
arithmetic spectrum of the zeros. The shared words -- 'self-adjoint', 'void',
'kernel', 'null' -- do not make the objects the same. The phase-Theta field is
a good SEMANTIC operator; it is not the Riemann operator, and its spectrum
carries no image of the zeros. No mechanism links them, and the controlled
test confirms it.
""")


if __name__ == "__main__":
    main()
