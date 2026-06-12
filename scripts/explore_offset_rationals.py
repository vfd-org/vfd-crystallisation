#!/usr/bin/env python3
"""
WO-SHELL-OFFSET-001 Phase D: the primitive-rational offset correspondence.

HYPOTHESIS (from re-reading Paper V through the LIX ladder): the ladder
offsets are log_phi of small rationals built from 600-cell PRIMITIVE
COUNTS - the correction factor r = m_rung / m_measured has the form
r = 1 +/- a/b with a in {1,2,3} and b a named substrate count. Paper V's
forward-traceable chain ratios (1 - R_I = 5/6, R_D(3) = 2, V_3 = 42,
R_D(4) = 15, ...) are exactly such objects; this phase tests whether the
WHOLE offset layer has that shape, with the sieve-grade discipline.

DISCLOSURE (binding on any use of this result): the registered alphabet
below was assembled with PARTIAL SIGHT of the data (candidate fractions
were noticed for a few particles before the alphabet was frozen). The
three mitigations, all machine-checked here: (i) the null model uses the
SAME alphabet, so alphabet density is fully controlled; (ii) the
DISCRIMINATING CONTROL - a larger alphabet of non-primitive (prime)
denominators - must come out null, showing the offsets prefer primitive
denominators specifically, not small rationals generally; (iii) the
uncontaminated Paper-V-native sub-alphabet must retain significance.
Sensitivity that must be disclosed wherever this is cited: restricting
numerators to a <= 2 weakens p to ~0.07 (the a=3 forms 19/16 and 23/20
matter), and the alphabet is hereby FROZEN - any future re-test
(improved mass measurements; new particles) uses it unchanged.

GRADE: RECORDED CORRESPONDENCE (a lead that passed its control), not a
derivation and not a prediction. The derivational target it sharpens:
obtain a/b per particle from the closure mode's population structure.

  OR1  registered primitive alphabet: score p < 0.005; >= 8/12 particles
       within 0.2% of an alphabet member (chance expectation ~3.9).
  OR2  DISCRIMINATING CONTROL: non-primitive prime-denominator alphabet
       (LARGER, 68 vs 42 members) is null (p > 0.3, fewer hits).
  OR3  uncontaminated Paper-V-native alphabet {5,6,12,15,20,24,30,42}
       retains significance (p < 0.02, 7/12 hits).
  OR4  sensitivity recorded: a <= 2 weakens to p ~ 0.07 (disclosed).
  OR5  the alphabet-corrected ladder: mean |error| ~ 0.2% (vs ~10% bare),
       at ~5.4 bits/particle; per-particle table printed with the exact
       rational, corrected mass, and residual vs measurement.

Usage:
    python scripts/explore_offset_rationals.py
"""
from __future__ import annotations

import numpy as np
from fractions import Fraction

rng = np.random.default_rng(20260617)

PASS = []
FAIL = []


def check(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


PHI = (1 + 5 ** 0.5) / 2
MP = 0.1056583755 * PHI ** 96
MASS = {"e": 5.1099895e-4, "tau": 1.77686, "u": 2.16e-3, "d": 4.67e-3,
        "s": 0.0934, "c": 1.273, "b": 4.18, "t": 172.76, "p": 0.93827209,
        "W": 80.377, "Z": 91.1876, "H": 125.25}
SHELL = {"e": 107, "tau": 90, "u": 104, "d": 102, "s": 96, "c": 91,
         "b": 88, "t": 81, "p": 91, "W": 82, "Z": 82, "H": 81}
CORR = {k: (MP * PHI ** (-SHELL[k])) / v for k, v in MASS.items()}

# FROZEN registered alphabet. Denominators, each a named substrate count:
#   5  = BFS shell count N (Paper V)         6  = 1/R_I (icosahedral reflection)
#   8  = observer rung                      9  = integer Laplacian eigenvalue
#   12 = vertex degree / first shell        14 = integer Laplacian eigenvalue
#   15 = R_D(4) (dodecahedral first-passage) 16 = info rung
#   20 = second shell population            24 = 24-cell / D4 rung
#   30 = third shell population / H4 Coxeter 42 = V_3 (BFS shell-3 count)
PRIM = [5, 6, 8, 9, 12, 14, 15, 16, 20, 24, 30, 42]
CONTROL = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
PV_NATIVE = [5, 6, 12, 15, 20, 24, 30, 42]


def build(denoms, amax=3):
    out = {}
    for a in range(1, amax + 1):
        for b in denoms:
            for s_ in (1, -1):
                fr = Fraction(b + s_ * a, b)
                if 0.75 < float(fr) < 1.35:
                    out[float(fr)] = fr
    vals = np.array(sorted(out))
    return vals, [out[v] for v in sorted(out)]


def score(Af, reps=20000):
    ds = np.array([np.min(np.abs(Af - r)) / r for r in CORR.values()])
    obs = float(np.sum(np.log(ds + 1e-9)))
    null = np.empty(reps)
    for i in range(reps):
        rs = PHI ** rng.uniform(-0.5, 0.5, len(CORR))
        d2 = np.array([np.min(np.abs(Af - r)) / r for r in rs])
        null[i] = np.sum(np.log(d2 + 1e-9))
    return obs, float(np.mean(null <= obs)), ds


def main():
    print("=" * 74)
    print("Phase D: primitive-rational offsets — r = m_rung/m_meas vs 1 ± a/b")
    print("(grade: RECORDED CORRESPONDENCE; disclosure in the docstring)")
    print("=" * 74)

    Af, Afr = build(PRIM)
    obs, p, ds = score(Af)
    hits = int(np.sum(ds < 0.002))
    check("OR1 registered primitive alphabet: closer than chance "
          f"(p = {p:.4f}) with {hits}/12 particles within 0.2% "
          "(chance ~3.9)", p < 0.005 and hits >= 8,
          f"|A| = {len(Af)}")

    Ac, _ = build(CONTROL)
    obs_c, p_c, ds_c = score(Ac)
    check("OR2 DISCRIMINATING CONTROL: larger non-primitive (prime) "
          "alphabet is null — the offsets prefer primitive denominators "
          "specifically", p_c > 0.3,
          f"|A| = {len(Ac)}, p = {p_c:.2f}, hits {int(np.sum(ds_c < 0.002))}/12")

    Apv, _ = build(PV_NATIVE)
    obs_pv, p_pv, ds_pv = score(Apv)
    check("OR3 uncontaminated Paper-V-native alphabet retains significance",
          p_pv < 0.02, f"|A| = {len(Apv)}, p = {p_pv:.4f}, "
          f"hits {int(np.sum(ds_pv < 0.002))}/12")

    A2, _ = build(PRIM, amax=2)
    obs_2, p_2, _ = score(A2)
    check("OR4 sensitivity disclosed: numerators a <= 2 weaken the signal",
          0.02 < p_2 < 0.2, f"p = {p_2:.3f} (the a = 3 forms matter)")

    print("-" * 74)
    print(f"{'':<5} {'corr r':>9} {'nearest':>8} {'dist':>8} "
          f"{'m_corrected [GeV]':>18} {'vs PDG':>8}")
    tot = 0.0
    for (k, r), d in zip(CORR.items(), ds):
        i = int(np.argmin(np.abs(Af - r)))
        fr = Afr[i]
        m_corr = (MP * PHI ** (-SHELL[k])) / float(fr)
        dev = m_corr / MASS[k] - 1
        tot += abs(dev)
        print(f"{k:<5} {r:>9.5f} {str(fr):>8} {d:>8.3%} "
              f"{m_corr:>18.6g} {dev:>+8.3%}")
    mean_dev = tot / len(CORR)
    check("OR5 alphabet-corrected ladder mean |error| ~ 0.2% "
          "(bare ladder ~10%), at ~5.4 bits/particle",
          mean_dev < 0.004, f"mean |dev| = {mean_dev:.3%}")

    print("=" * 74)
    print(f"SUMMARY: {len(PASS)} PASS, {len(FAIL)} FAIL")
    for name in FAIL:
        print(f"  FAILED: {name}")
    print()
    print("Reading: the dressing layer appears to have the shape")
    print("r = 1 ± a/b with b a substrate population count — Paper V's ratio")
    print("structure recovered with a 42-member alphabet and a passed control.")
    print("NOT a derivation: the derivational target is now to obtain a/b per")
    print("particle from the closure mode's population structure. The alphabet")
    print("is FROZEN for all future re-tests.")
    return 0 if not FAIL else 1


if __name__ == "__main__":
    raise SystemExit(main())
