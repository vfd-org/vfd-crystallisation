#!/usr/bin/env python3
"""
WO-SHELL-OFFSET-001: the disciplined attack on (i) the shell-integer rule
and (ii) the offset dynamics — with every outcome, including the nulls,
machine-checked. (docs/shell-rule-wo.md records the conclusions.)

DISCIPLINE. Golden-ratio expressions are flexible enough to "fit" any
mass spectrum; that is the W5 trap this programme's verification gate
exists to kill. So this script does the opposite of fitting: it
enumerates STRUCTURE-DERIVED hypothesis classes (features the framework
has actually derived: generation index, the charge integer N_c of Paper
LVIII, colour, the cascade rung numbers), states exact-match criteria
and information budgets BEFORE judging, accounts for look-elsewhere, and
certifies the negative results as theorems about the data. A PASS below
means "the recorded conclusion — including each null — is reproduced."

Inputs: integer shells N = round(log_phi(m_P/m)) and offsets from
papers/cascade-derivation/cascade-masses.md §E3.1 (PDG 2024).

  SR1  curvature obstruction (PROVEN NULL): the generation curvatures
       (second differences) of the charged-fermion shells are (5, 3, -2)
       for (L, U, D). Any rule N = a_type + f(g) with type-universal f —
       with ANY generation-independent additive features (charge, colour,
       isospin, ...) — is impossible. This kills the entire class
       "polynomial in generation + static quantum numbers".
  SR2  type-linear null: even allowing per-type slopes AND intercepts
       (6 parameters), no exact fit exists (within-type steps unequal).
       The cheapest exact polynomial class is quadratic-per-type =
       9 parameters for 9 integers: zero compression, inadmissible.
  SR3  information budget (the bar for any future rule): the 9 charged-
       fermion integers carry ~42 bits; an admissible rule must spend
       at most ~24 bits of parameters (compression >= 1.7x). Recorded.
  SR4  cascade-residue scan (NULL): residues mod 24 hit the rung numbers
       {0, 8, 16} 4/12 times, binomial P >= 0.05 BEFORE the ~6-modulus
       look-elsewhere discount => no evidence.
  SR5  boson clustering (observation): W, Z, Higgs sit at 82, 82, 81 —
       one electroweak shell-cluster, consistent with a single scale,
       not three independent placements.
  SR6  offset magnitudes track colour/scheme-dependence (the recorded
       pattern): mean |offset| leptons 0.071 < EW bosons 0.184 <
       quarks 0.288 < composite 0.462. Monotone across the four sectors.
  SR7  signed-offset regression vs (Q^2, colour, N): the pre-registered
       null was REFUSED in-sample (R^2 0.86, perm p ~ 0.01; LOO 0.46)
       but the fermion-fitted law fails out-of-sample on the bosons
       (Z predicted +1.3 vs observed -0.05). Verdict: a sector-limited
       LEAD recorded for future work, not a law.
  SR8  lepton RG-log test (NULL): a dressing of the simple form
       delta ~ c * Q^2 * ln(m_P/m) is monotone in ln(m); the lepton
       offsets (+0.079, -0.0002, +0.135) are NOT monotone => the
       simple one-loop-log form is excluded within the lepton sector.

Usage:
    python scripts/explore_shell_rule.py
"""
from __future__ import annotations

import numpy as np
from itertools import product
from math import comb, log2

rng = np.random.default_rng(20260615)

PASS = []
FAIL = []


def check(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


# data: (type, generation) -> integer shell; offsets
SHELLS = {"L": [107, 96, 90], "U": [104, 91, 81], "D": [102, 96, 88]}
BOSONS = {"W": 82, "Z": 82, "H": 81}
OFFSETS = {
    "e": 0.079, "mu": -0.0002, "tau": 0.135,
    "u": 0.084, "d": 0.481, "s": 0.256, "c": -0.172, "b": 0.357, "t": -0.377,
    "W": 0.213, "Z": -0.049, "H": 0.291, "proton": 0.462,
}
# structure-derived static features (Paper LVIII): charge integer N_c,
# colour (0 singlet / 1 triplet)
NC = {"L": 3, "U": 2, "D": 1}      # charge-magnitude integers x3
COL = {"L": 0, "U": 1, "D": 1}


def sr1_curvature_obstruction():
    print("SR1: curvature obstruction (proven null)")
    curv = {t: ns[2] - 2 * ns[1] + ns[0] for t, ns in SHELLS.items()}
    distinct = len(set(curv.values())) == 3
    # In N = a_type(+ static features) + f(g), the second difference in g
    # is f(3)-2f(2)+f(1), independent of type. Distinct curvatures refute
    # every such rule, for ANY f and ANY static features.
    check("SR1 curvatures (L,U,D) = (5,3,-2) all distinct: every rule "
          "'type-offset + universal f(generation)' is refuted",
          distinct and curv == {"L": 5, "U": 3, "D": -2}, f"{curv}")


def sr2_type_linear_null():
    print("SR2: per-type linear rules (6 params) still fail")
    ok_null = True
    for t, ns in SHELLS.items():
        steps = (ns[1] - ns[0], ns[2] - ns[1])
        if steps[0] == steps[1]:
            ok_null = False
    check("SR2 within-type generation steps are unequal for all three "
          "types: even per-type linear rules have no exact fit; cheapest "
          "exact polynomial class is 9 params for 9 integers (zero "
          "compression, inadmissible)", ok_null,
          f"steps L{tuple(np.diff(SHELLS['L']))} U{tuple(np.diff(SHELLS['U']))} "
          f"D{tuple(np.diff(SHELLS['D']))}")


def sr3_information_budget():
    print("SR3: the bar any future rule must clear")
    ns = [n for t in SHELLS.values() for n in t]
    span = max(ns) - min(ns) + 1
    bits_data = 9 * log2(span)
    bits_budget = bits_data / 1.7
    check("SR3 information budget recorded: 9 integers in a span of "
          f"{span} carry {bits_data:.0f} bits; an admissible rule must "
          f"spend <= {bits_budget:.0f} bits of parameters "
          "(compression >= 1.7x)", True)


def sr4_cascade_residue():
    print("SR4: cascade rung residues (null)")
    parts = {**{f"{t}{g}": SHELLS[t][g - 1] for t in SHELLS for g in (1, 2, 3)},
             **BOSONS}
    hits = sum(1 for v in parts.values() if v % 24 in {0, 8, 16})
    p = sum(comb(12, k) * (3 / 24) ** k * (21 / 24) ** (12 - k)
            for k in range(hits, 13))
    # look-elsewhere: the modulus 24 was chosen post hoc among the rung
    # numbers {8, 16, 24, 40, ...}: ~6 comparable tests
    p_le = min(1.0, 6 * p)
    check("SR4 mod-24 rung-number hits 4/12: raw P = "
          f"{p:.3f}, look-elsewhere-corrected ~{p_le:.2f} => NO evidence",
          hits == 4 and p > 0.01)


def sr5_boson_cluster():
    print("SR5: electroweak shell cluster (observation)")
    check("SR5 W, Z, Higgs sit at shells (82, 82, 81): one EW cluster, "
          "i.e. one scale, not three independent placements",
          BOSONS["W"] == 82 and BOSONS["Z"] == 82 and BOSONS["H"] == 81)


def sr6_sector_magnitudes():
    print("SR6: offset magnitudes track colour/scheme-dependence")
    sec = {
        "leptons": ["e", "mu", "tau"],
        "EW": ["W", "Z", "H"],
        "quarks": ["u", "d", "s", "c", "b", "t"],
        "composite": ["proton"],
    }
    means = {k: float(np.mean([abs(OFFSETS[p]) for p in v]))
             for k, v in sec.items()}
    mono = (means["leptons"] < means["EW"] < means["quarks"]
            < means["composite"])
    check("SR6 mean |offset| monotone: leptons < EW < quarks < composite "
          "(sharp where mass is physical/pole, worst where "
          "scheme-dependent)", mono,
          " < ".join(f"{k} {v:.3f}" for k, v in means.items()))


def sr7_signed_regression_null():
    print("SR7: signed offsets vs (Q^2, colour, N) — permutation test")
    rows = []
    y = []
    for t in SHELLS:
        for g in (1, 2, 3):
            name = {("L", 1): "e", ("L", 2): "mu", ("L", 3): "tau",
                    ("U", 1): "u", ("U", 2): "c", ("U", 3): "t",
                    ("D", 1): "d", ("D", 2): "s", ("D", 3): "b"}[(t, g)]
            rows.append([(NC[t] / 3) ** 2, COL[t], SHELLS[t][g - 1], 1.0])
            y.append(OFFSETS[name])
    X = np.array(rows)
    y = np.array(y)

    def r2(Xm, ym):
        beta, *_ = np.linalg.lstsq(Xm, ym, rcond=None)
        res = ym - Xm @ beta
        return 1 - res @ res / ((ym - ym.mean()) @ (ym - ym.mean()))

    r2_obs = r2(X, y)
    null = [r2(X, rng.permutation(y)) for _ in range(2000)]
    pval = float(np.mean([n >= r2_obs for n in null]))
    # leave-one-out robustness
    loo = []
    for i in range(9):
        m = np.ones(9, bool)
        m[i] = False
        beta, *_ = np.linalg.lstsq(X[m], y[m], rcond=None)
        loo.append(y[i] - X[i] @ beta)
    loo = np.array(loo)
    ss = ((y - y.mean()) ** 2).sum()
    r2_loo = 1 - (loo ** 2).sum() / ss
    # out-of-sample: the bosons were never fitted
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    z_pred = beta @ np.array([0.0, 0, 82, 1.0])
    oos_fails = abs(z_pred - OFFSETS["Z"]) > 0.5
    check("SR7 the offset-vs-structure signal is a LEAD, NOT A LAW: "
          "in-sample R^2 0.86 (perm p ~ 0.01) and LOO R^2 ~ 0.46 within "
          "fermions, but the fermion-fitted law FAILS out-of-sample on "
          "the bosons (Z predicted ~ +1.3 vs observed -0.05)",
          r2_obs > 0.8 and pval < 0.05 and 0.3 < r2_loo < 0.6 and oos_fails,
          f"R^2 = {r2_obs:.2f}, p = {pval:.3f}, LOO = {r2_loo:.2f}, "
          f"Z pred {z_pred:+.2f} vs {OFFSETS['Z']:+.2f}")


def sr8_lepton_log_null():
    print("SR8: simple one-loop-log dressing excluded within leptons")
    lep = [OFFSETS["e"], OFFSETS["mu"], OFFSETS["tau"]]
    # delta ~ c Q^2 ln(m_P/m) = c' * N is monotone in N (decreasing in m);
    # lepton N = 107, 96, 90 so a log form must be monotone e > mu > tau
    # or e < mu < tau. It is not.
    mono = (lep[0] > lep[1] > lep[2]) or (lep[0] < lep[1] < lep[2])
    check("SR8 lepton offsets (+0.079, -0.0002, +0.135) are non-monotone "
          "in shell: delta = c Q^2 ln(m_P/m) is EXCLUDED", not mono)


def sr9_finer_rungs_null():
    print("SR9: is the missing layer just finer rungs? (null)")
    PHI = (1 + 5 ** 0.5) / 2
    LNP = np.log(PHI)
    MP = 0.1056583755 * PHI ** 96
    masses = {"e": 5.1099895e-4, "mu": 0.1056583755, "tau": 1.77686,
              "u": 2.16e-3, "d": 4.67e-3, "s": 0.0934, "c": 1.273,
              "b": 4.18, "t": 172.76, "p": 0.93827209, "W": 80.377,
              "Z": 91.1876, "H": 125.25}
    Nr = np.array([np.log(MP / v) / LNP for v in masses.values()])
    ok = True
    dets = []
    for grid in (1.0, 0.5, 0.25):
        d = np.abs(Nr / grid - np.round(Nr / grid)) * grid
        obs = float(np.mean(d))
        null = np.array([np.mean(np.minimum(u := rng.uniform(0, grid, 13),
                                            grid - u)) for _ in range(4000)])
        pv = float(np.mean(null <= obs))
        dets.append(f"grid {grid}: obs {obs:.3f} vs chance "
                    f"{float(np.mean(null)):.3f}, p {pv:.2f}")
        ok = ok and pv > 0.05
    check("SR9 sub-rung positions are chance-like at integer, half- and "
          "quarter-shell grids: the missing layer is NOT finer geometric "
          "rungs", ok, "; ".join(dets))


def sr11_affine_obstruction():
    print("SR11: the separability obstruction, strengthened to affine")
    # N_T(g) = a_T + b_T f(g) (any universal f; a_T, b_T arbitrary functions
    # of static quantum numbers) forces the anchored ratio
    # (N_T(3)-N_T(1))/(N_T(2)-N_T(1)) = (f(3)-f(1))/(f(2)-f(1))
    # to be type-independent. The observed ratios are distinct.
    ratios = {t: (ns[2] - ns[0]) / (ns[1] - ns[0]) for t, ns in SHELLS.items()}
    distinct = len({round(r, 6) for r in ratios.values()}) == 3
    check("SR11 anchored generation ratios (L,U,D) = (1.545, 1.769, 2.333) "
          "all distinct: every AFFINE-separable rule N = a_T + b_T f(g) is "
          "refuted (subsumes the additive SR1 and the multiplicative case)",
          distinct, f"{ {t: round(r,3) for t,r in ratios.items()} }")


def sr10_ew_decomposition():
    print("SR10: the W deviation = Z placement + the Weinberg angle")
    PHI = (1 + 5 ** 0.5) / 2
    LNP = np.log(PHI)
    dN = np.log(91.1876 / 80.377) / LNP        # W-Z shell split
    pred = -np.log(80.377 / 91.1876) / LNP     # log_phi(1/cos theta_W)
    # an identity, recorded as BOOKKEEPING: m_W = m_Z cos(theta_W) is
    # standard EW physics, so the W carries no independent placement
    # information - its deviation reduces to Z's rung plus the already-
    # named open item (the mixing angle / independent hypercharge).
    sin2 = 1 - (80.377 / 91.1876) ** 2
    check("SR10 (bookkeeping identity) W-Z shell split 0.262 = "
          "log_phi(1/cos theta_W); the EW sector has ONE placement (Z) "
          "+ one named open (the mixing) + Higgs",
          abs(dN - pred) < 1e-12 and abs(sin2 - 0.2231) < 5e-4,
          f"split {dN:.3f}; sin^2(theta_W) = {sin2:.4f} (PDG on-shell 0.2233)")


def main():
    print("=" * 70)
    print("WO-SHELL-OFFSET-001 — shell-integer rule + offset dynamics attack")
    print("(PASS = the recorded conclusion, including each null, reproduces)")
    print("=" * 70)
    sr1_curvature_obstruction()
    sr2_type_linear_null()
    sr3_information_budget()
    sr4_cascade_residue()
    sr5_boson_cluster()
    sr6_sector_magnitudes()
    sr7_signed_regression_null()
    sr8_lepton_log_null()
    sr9_finer_rungs_null()
    sr10_ew_decomposition()
    sr11_affine_obstruction()
    print("=" * 70)
    print(f"SUMMARY: {len(PASS)} PASS, {len(FAIL)} FAIL")
    for name in FAIL:
        print(f"  FAILED: {name}")
    print()
    print("Net: the shell rule is NOT derivable from low-complexity")
    print("polynomial/static-feature classes (SR1-SR2 are proofs, not")
    print("failures to find); the offset-structure correlation is a")
    print("sector-limited lead, not a law (SR7); simple log dressing is")
    print("excluded (SR8); offset magnitudes track scheme-dependence")
    print("(SR6). See docs/shell-rule-wo.md for constraints and routes.")
    return 0 if not FAIL else 1


if __name__ == "__main__":
    raise SystemExit(main())
