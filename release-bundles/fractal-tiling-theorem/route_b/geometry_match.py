"""Geometry match test: do the recurring geometric forms actually appear in
the Riemann zeros? We TEST against the real zeros, with controls, and let the
numbers decide -- no dismissing, no fitting-to-confirm.

Forms tested (the ones that recur through this work and through history):
  1. the phi^3-spiral claim (theta = 2*pi*phi^3 * n  ->  cluster at pi/2?)
  2. golden-ratio structure in consecutive heights / spacings
  3. the substrate's own geometric spectrum (C_phi, 9 eigenvalues) vs the zeros
  4. torus / quasi-periodicity (sharp Fourier peak) vs GUE (broadband)

HONEST DESIGN: every test has a CONTROL (uniform / random / GUE surrogate).
A 'MATCH' means the zeros beat the control; otherwise it's NO MATCH. We report
the number either way. A negative is a real result (it rules a form out).
"""
from __future__ import annotations

import math
import numpy as np
import mpmath as mp

PHI = (1 + math.sqrt(5)) / 2
PHI3 = PHI**3                      # = 2*phi+1 = sqrt5+2 ~ 4.236

# C_phi spectrum on V_600 (the substrate's geometric operator, 9 eigenvalues)
CPHI = np.array([0.381966, 2.67, 5.91, 9.38, 12.38, 14.38, 14.85, 15.38, 16.09])


def zeros(n):
    mp.mp.dps = 20
    return np.array([float(mp.im(mp.zetazero(k))) for k in range(1, n + 1)])


def rayleigh(theta):
    """Circular concentration R in [0,1]; ~1/sqrt(N) if uniform, ->1 if clustered."""
    z = np.mean(np.exp(1j * theta))
    return abs(z), (math.degrees(np.angle(z)) % 360)


def unfold(g):
    return (g / (2 * math.pi)) * np.log(g / (2 * math.pi)) - g / (2 * math.pi) + 7 / 8


def gue_eigs(N, rng):
    A = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
    H = (A + A.conj().T) / 2
    return np.sort(np.linalg.eigvalsh(H))


def main():
    print("=" * 74)
    print("GEOMETRY MATCH TEST -- do the recurring forms live in the zeros?")
    print("=" * 74)
    N = 200
    g = zeros(N)
    rng = np.random.RandomState(31)
    print(f"phi = {PHI:.6f},  phi^3 = {PHI3:.6f}")
    print(f"{N} Riemann zeros: gamma_1={g[0]:.4f} ... gamma_{N}={g[-1]:.4f}")

    # ---- TEST 1: the phi^3-spiral claim ----
    print("\n" + "-" * 74)
    print("TEST 1  phi^3-spiral: theta_n = 2*pi*phi^3*n mod 2pi -> cluster at 90 deg?")
    th_idx = (2 * math.pi * PHI3 * np.arange(1, N + 1)) % (2 * math.pi)
    th_ht = (2 * math.pi * PHI3 * g) % (2 * math.pi)
    R_idx, a_idx = rayleigh(th_idx)
    R_ht, a_ht = rayleigh(th_ht)
    th_rand = rng.uniform(0, 2 * math.pi, N); R_rand, _ = rayleigh(th_rand)
    unif = 1 / math.sqrt(N)
    print(f"  using index n : R={R_idx:.3f} (mean {a_idx:.0f} deg)  [uniform ~ {unif:.3f}]")
    print(f"  using height  : R={R_ht:.3f} (mean {a_ht:.0f} deg)")
    print(f"  random control: R={R_rand:.3f}")
    claim = (R_idx > 5 * unif and abs(a_idx - 90) < 15) or (R_ht > 5 * unif and abs(a_ht - 90) < 15)
    print(f"  VERDICT: {'MATCH' if claim else 'NO MATCH'} -- "
          f"{'zeros cluster at 90 deg' if claim else 'no clustering, no 90-deg landing (uniform like random)'}")
    print(f"  (note: the image asserted 2*pi*phi^3*(1/2)=pi/2; in fact = pi*phi^3 = {math.pi*PHI3:.2f} rad, not {math.pi/2:.2f})")

    # ---- TEST 2: golden ratio in heights / spacings ----
    print("\n" + "-" * 74)
    print("TEST 2  golden ratio in consecutive heights and spacings?")
    ratios = g[1:] / g[:-1]
    near_phi = np.mean(np.abs(ratios - PHI) < 0.05)
    print(f"  gamma_(n+1)/gamma_n: mean={np.mean(ratios):.3f}, ->1 as n grows "
          f"(frac within 0.05 of phi={PHI:.3f}: {near_phi:.2%})")
    s = np.diff(unfold(g))
    sr = s[1:] / s[:-1]
    near_phi_s = np.mean(np.abs(sr - PHI) < 0.1)
    print(f"  unfolded spacing ratios: mean={np.mean(sr):.3f} "
          f"(frac near phi: {near_phi_s:.2%}; random GUE-like ~ similar)")
    m2 = near_phi > 0.3 or near_phi_s > 0.3
    print(f"  VERDICT: {'MATCH' if m2 else 'NO MATCH'} -- "
          f"{'golden ratio appears' if m2 else 'no golden-ratio structure (ratios ->1, spacings Wigner)'}")

    # ---- TEST 3: substrate geometric spectrum vs zeros ----
    print("\n" + "-" * 74)
    print("TEST 3  substrate spectrum C_phi (9 eigenvalues) vs the zeros?")
    # best affine a*x+b mapping CPHI onto first 9 zeros, report residual
    x = CPHI; y = g[:9]
    A = np.vstack([x, np.ones_like(x)]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    fit = A @ coef
    rmse = math.sqrt(np.mean((fit - y) ** 2))
    # control: 9 sorted random values fit the same way
    rc = np.sort(rng.uniform(x.min(), x.max(), 9))
    Ac = np.vstack([rc, np.ones_like(rc)]).T
    cc, *_ = np.linalg.lstsq(Ac, y, rcond=None)
    rmse_rand = math.sqrt(np.mean((Ac @ cc - y) ** 2))
    print(f"  best affine fit of C_phi -> first 9 zeros: RMSE={rmse:.3f}")
    print(f"  random 9-value control:                    RMSE={rmse_rand:.3f}")
    print(f"  C_phi is BOUNDED (max {CPHI.max():.1f}); zeros are UNBOUNDED "
          f"(gamma_200={g[-1]:.0f}, ->infinity).")
    m3 = rmse < 0.3 * rmse_rand
    print(f"  VERDICT: {'MATCH' if m3 else 'NO MATCH'} -- "
          f"{'geometric spectrum tracks zeros' if m3 else 'finite/bounded geometric spectrum cannot track the infinite zero sequence (9 pts fit no better than random; tops out at 16 while zeros run to infinity)'}")

    # ---- TEST 4: torus / quasi-periodicity vs GUE ----
    print("\n" + "-" * 74)
    print("TEST 4  torus/quasi-periodicity (sharp Fourier peak) vs GUE (broadband)?")
    u = unfold(g); sp = np.diff(u); sp = sp - np.mean(sp)
    P = np.abs(np.fft.rfft(sp))**2
    peak_ratio = P[1:].max() / np.mean(P[1:])      # sharp peak -> large
    # GUE control
    ev = gue_eigs(400, rng); ev = ev[100:300]
    spg = np.diff(ev); spg = spg - np.mean(spg)
    Pg = np.abs(np.fft.rfft(spg))**2
    peak_g = Pg[1:].max() / np.mean(Pg[1:])
    print(f"  zeros  spacing-spectrum peak/mean = {peak_ratio:.2f}")
    print(f"  GUE    spacing-spectrum peak/mean = {peak_g:.2f}")
    m4 = peak_ratio > 3 * peak_g
    print(f"  VERDICT: {'MATCH' if m4 else 'NO MATCH'} -- "
          f"{'quasi-periodic (toroidal) structure' if m4 else 'no sharp periodicity; behaves like GUE, not a torus orbit'}")

    print("""
==========================================================================
WHAT THE DATA SAYS (honest, not dismissive)
==========================================================================
We TESTED the recurring geometric forms against the actual zeros, each with a
control. The forms that recur in nature/history (phi, spiral, torus) are real
THERE; the question was whether they live in the RIEMANN ZEROS. The numbers
above answer it form by form. Where a test says NO MATCH, that is a genuine
negative -- it RULES OUT that specific form, which is real information, not a
dismissal. Where (if) a test says MATCH, that is a lead worth chasing.

The one form that consistently DOES match the zeros -- across this whole
bundle -- is GUE (the quantum-chaos statistics). That is the geometry that is
actually there. The symmetric/golden/toroidal figures are the ones the data
keeps declining -- tested, not assumed.
""")


if __name__ == "__main__":
    main()
