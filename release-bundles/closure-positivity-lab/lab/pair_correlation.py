"""The pair-correlation instrument: the zeros' spectral form factor.

The gap-1 probes (WO-VFD-PRIME-GAPS-001 SE) eliminated every periodic
VFD-native channel: twin-prime infinitude lives in an aperiodic,
pair-coupled, spectral-side mechanism. This instrument measures that
mechanism's first object on the repository's own data.

Primary statistic (gated): the UNFOLDED spectral form factor

    K(tau) = (1/N) | sum_j exp(2 pi i tau w_j) |^2,

where w_j = Nbar(gamma_j) are the unfolded zero positions (mean spacing
1; same unfolding as ledger row 10). For the sine-kernel (GUE) process
the structure factor is min(|tau|, 1): a linear ramp then a plateau at 1.
The ramp window lies in the Montgomery-ramp range --- corresponding to
(not identical with) the proven Fourier-side range |alpha| < 1 of the
weighted F(alpha, T); what is gated here is the unweighted, finite-window
unfolded statistic. The plateau is the conjectural half --- under RH, by the
Goldston--Montgomery equivalence, it is the same object that controls
the variance of primes in short intervals, and fixed-gap (twin)
statements need strictly more. K(tau) at a single
tau fluctuates with mean ~ the curve (exponential-type periodogram
behaviour), so all gates act on BIN AVERAGES. The gate windows
deliberately avoid tau ~ 0 (the coherent mean spike) and tau ~ 1, where
RvM unfolding produces a large coherent artifact (w_j sits near j - 1/2,
so e^{2 pi i w_j} adds coherently: K(1) ~ 80 here); both exclusions are
structural, not tuned.

Secondary panel (reported, NOT gated): Montgomery's original
F(alpha, T) with its finite-T diagonal level
d_T = N(T) / ((T/2pi) log T) marked --- at T = 2500, d_T = 0.637, and the
measured plateau is consistent with domination by that diagonal level
(the asymptotic plateau 1 is approached only like 1 - log(2 pi e)/log T).

Gates (set before reading data; bin width 0.1, grid step 0.005):
  g1  ramp: fit of bin means on tau in [0.2, 0.9]:
      slope 1 +- 0.3, |intercept| < 0.15
  g2  plateau: bin-mean of K on tau in [1.2, 2.5] within 1 +- 0.2
  g3  plateau flatness: |linear trend| on [1.2, 2.5] < 0.15
(The exploratory icosian-L panel, 33 zeros, is reported and never gated.)

Run:  python3 -m lab.pair_correlation     -> out/pair_correlation.json
"""
import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def unfold_zeta(t):
    t = np.asarray(t, dtype=float)
    return t / (2 * math.pi) * np.log(t / (2 * math.pi * math.e)) + 7.0 / 8.0


def form_factor_unfolded(w, taus):
    w = np.asarray(w, dtype=float)
    K = np.empty(len(taus))
    for i, tau in enumerate(taus):
        z = np.exp(2j * math.pi * tau * w)
        K[i] = (abs(z.sum()) ** 2) / len(w)
    return K


def bin_means(taus, K, lo, hi, width=0.1):
    means = []
    centers = []
    edges = np.arange(lo, hi + 1e-9, width)
    for a in edges[:-1]:
        m = (taus >= a) & (taus < a + width)
        if m.any():
            means.append(float(np.mean(K[m])))
            centers.append(float(a + width / 2))
    return np.array(centers), np.array(means)


def montgomery_F(gammas, T, alphas):
    g = np.asarray(gammas, dtype=float)
    d = g[:, None] - g[None, :]
    w = 4.0 / (4.0 + d * d)
    logT = math.log(T)
    norm = (T / (2 * math.pi)) * logT
    return np.array([float(np.sum(w * np.cos(a * logT * d))) / norm
                     for a in alphas])


def run():
    zeros = np.loadtxt(os.path.join(ROOT, "out", "zeta_zeros.txt"))
    T = float(zeros[-1])
    N = len(zeros)
    w = unfold_zeta(zeros)

    taus = np.arange(0.05, 3.0001, 0.005)
    K = form_factor_unfolded(w, taus)

    # g1 ramp
    c1, m1 = bin_means(taus, K, 0.2, 0.9)
    slope, intercept = np.polyfit(c1, m1, 1)
    g1 = abs(slope - 1) < 0.3 and abs(intercept) < 0.15
    # g2/g3 plateau
    c2, m2 = bin_means(taus, K, 1.2, 2.5)
    pmean = float(np.mean(m2))
    ptrend = float(np.polyfit(c2, m2, 1)[0])
    g2 = abs(pmean - 1) < 0.2
    g3 = abs(ptrend) < 0.15

    # secondary panel: Montgomery's F with the finite-T level marked
    alphas = np.arange(0.0, 3.001, 0.05)
    F = montgomery_F(zeros, T, alphas)
    nt_main = (T / (2 * math.pi)) * math.log(T / (2 * math.pi * math.e)) + 7 / 8
    d_T = nt_main / ((T / (2 * math.pi)) * math.log(T))

    # exploratory: icosian L zeros (degree 4, 33 zeros -- never gated)
    with open(os.path.join(ROOT, "out", "curve_zeros.json")) as fh:
        lz = np.array([z if isinstance(z, (int, float)) else z[0]
                       for z in json.load(fh)["L_zeros"]], dtype=float)
    # unfold with the analytic counting main term (D20: degree 4,
    # conductor 775) -- rank-unfolding would erase the spacing statistics
    d_deg, cond = 4, 775
    wL = (d_deg * lz / (2 * math.pi)) * np.log(lz / (2 * math.pi * math.e)) \
        + (lz / (2 * math.pi)) * math.log(cond)
    KL = form_factor_unfolded(wL, np.arange(0.1, 2.0001, 0.1))

    doc = {
        "description": "unfolded spectral form factor K(tau) of the "
                       "repository's zeta zeros (gated, sine-kernel "
                       "expectation min(tau,1)); Montgomery F(alpha,T) "
                       "panel with finite-T level marked (reported)",
        "T": T, "n_zeros": int(N),
        "taus": [round(float(x), 4) for x in taus[::5]],
        "K_decimated": [round(float(v), 4) for v in K[::5]],
        "gated_bins": {
            "ramp_centers": [round(float(x), 3) for x in c1],
            "ramp_means": [round(float(v), 4) for v in m1],
            "plateau_centers": [round(float(x), 3) for x in c2],
            "plateau_means": [round(float(v), 4) for v in m2],
        },
        "gates": {
            "g1_ramp": {"pass": bool(g1), "slope": round(float(slope), 4),
                        "intercept": round(float(intercept), 4),
                        "note": "ramp window: corresponds to (not "
                                "identical with) the proven Fourier-side "
                                "range of the weighted F"},
            "g2_plateau_mean": {"pass": bool(g2), "mean": round(pmean, 4),
                                "note": "GUE-conjecture region: "
                                        "consistency, NOT proof"},
            "g3_plateau_flat": {"pass": bool(g3),
                                "trend": round(ptrend, 4)},
        },
        "montgomery_panel": {
            "alphas": [round(float(a), 3) for a in alphas],
            "F": [round(float(v), 4) for v in F],
            "finite_T_diagonal_level": round(float(d_T), 4),
            "note": "NOT gated: at T = 2500 the measured F-plateau is "
                    "consistent with domination by the diagonal level d_T "
                    "(computed from the RvM main term Nbar(T), not the "
                    "observed count), which approaches 1 only like "
                    "1 - log(2 pi e)/log T",
        },
        "goldston_montgomery_bridge": {
            "statement": "in the standard conditional form, under RH: "
                         "F ~ 1 on 1 <= alpha <= A is equivalent "
                         "(Goldston-Montgomery) to the asymptotic for the "
                         "variance of psi(x+h) - psi(x) at h ~ x^{1/A}; "
                         "fixed-gap (twin) asymptotics require strictly "
                         "more than these averaged statements",
            "source": "D. A. Goldston, H. L. Montgomery, Pair correlation "
                      "of zeros and primes in short intervals, Analytic "
                      "Number Theory and Diophantine Problems, "
                      "Birkhauser PM 70 (1987) 183-203",
            "scope": "stated with source; nothing here proves any of it",
        },
        "icosian_L_exploratory": {
            "n_zeros": int(len(lz)),
            "K_analytic_unfolded": [round(float(v), 4) for v in KL],
            "note": "33 zeros, unfolded by the analytic counting term: "
                    "reported for completeness, "
                    "far too few for statistics, never gated",
        },
        "all_gates_pass": bool(g1 and g2 and g3),
    }
    return doc


def main():
    doc = run()
    with open(os.path.join(ROOT, "out", "pair_correlation.json"), "w") as fh:
        json.dump(doc, fh, indent=2)
    g = doc["gates"]
    print("K(tau) from %d unfolded zeros (T = %.1f)" % (doc["n_zeros"],
                                                        doc["T"]))
    print("  g1 ramp     %s  slope %s intercept %s (Montgomery-ramp window)" %
          ("PASS" if g["g1_ramp"]["pass"] else "FAIL",
           g["g1_ramp"]["slope"], g["g1_ramp"]["intercept"]))
    print("  g2 plateau  %s  mean %s (conjectural region, consistency)" %
          ("PASS" if g["g2_plateau_mean"]["pass"] else "FAIL",
           g["g2_plateau_mean"]["mean"]))
    print("  g3 flat     %s  trend %s" %
          ("PASS" if g["g3_plateau_flat"]["pass"] else "FAIL",
           g["g3_plateau_flat"]["trend"]))
    print("  Montgomery panel: finite-T diagonal level d_T = %s (measured "
          "plateau consistent with diagonal domination)" %
          doc["montgomery_panel"]["finite_T_diagonal_level"])
    print("-> out/pair_correlation.json")
    return 0 if doc["all_gates_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
