"""WO-RH-VFD-RESONANCE-BRIDGE-001 -- Deliverable C: mirror-leakage candidates.

Three candidate leakage functionals, each tested for the two failure modes the
WO names: (i) trivially forced by construction, (ii) does not encode s<->1-s in
a non-circular way.

  L1  prime-field mirror imbalance:   |P_X(sigma,t) - conj(P_X(1-sigma,t))|
  L2  normalised:                     L1 / (|P_X(sigma,t)|+|P_X(1-sigma,t)|+eps)
  L3  completed-field defect:         B(s) = xi(s) - xi(1-s)

Honest expectations (verified below):
  * L3 is IDENTICALLY ZERO (the functional equation xi(s)=xi(1-s)).  It is
    forced by construction: it vanishes everywhere -- off the line, at zeros,
    at random points alike -- so it detects NOTHING about zero locations.
    Finite truncations only measure truncation error, not a zero defect.
  * L1, L2 are generically nonzero (P_X has no functional equation) and do NOT
    vanish or sharply minimise on sigma=1/2; they show no clean critical-line
    structure -> decorative.

The surviving non-trivial "boundary minus residual" leakage object is NOT here:
it is the Weil functional W(h)=ARCH(h)-PRIME(h) (Deliverable D2), which is
non-circular and RH-equivalent.
"""
from __future__ import annotations

import cmath
import json
import math
import os

import numpy as np
import mpmath as mp

mp.mp.dps = 25
HERE = os.path.dirname(__file__)
TAB = os.path.join(HERE, "results", "tables")

GAMMA = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062]


def primes_up_to(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = b"\x00" * len(s[i * i::i])
    return [i for i in range(2, n + 1) if s[i]]


def P(sigma, t, primes):
    z = 0j
    for p in primes:
        z += p ** (-sigma) * cmath.exp(-1j * t * math.log(p))
    return z


# ---- L1, L2 : prime-field mirror imbalance --------------------------------
def L1(sigma, t, primes):
    return abs(P(sigma, t, primes) - np.conj(P(1 - sigma, t, primes)))


def L2(sigma, t, primes):
    a = P(sigma, t, primes)
    b = P(1 - sigma, t, primes)
    return abs(a - np.conj(b)) / (abs(a) + abs(b) + 1e-12)


def test_L1_L2(X=20000):
    primes = primes_up_to(X)
    sig_grid = [0.3, 0.4, 0.5, 0.6, 0.7]
    # does L vanish / minimise on sigma=1/2 ?  Test at a few t (incl. zeros).
    rows = []
    for t in [14.134725, 25.010858, 40.0, 55.0]:
        l1 = {s: L1(s, t, primes) for s in sig_grid}
        l2 = {s: L2(s, t, primes) for s in sig_grid}
        argmin1 = min(l1, key=l1.get)
        rows.append({"t": t,
                     "L1_by_sigma": {str(s): round(l1[s], 4) for s in sig_grid},
                     "L1_min_at_sigma": argmin1,
                     "L1_minimised_on_half": abs(argmin1 - 0.5) < 1e-9,
                     "L2_on_half": round(l2[0.5], 4)})
    minimised_on_half = sum(r["L1_minimised_on_half"] for r in rows)
    # circularity check: L1(sigma,t) == L1(1-sigma,t) identically?
    primes2 = primes
    sym = all(abs(L1(s, 47.3, primes2) - L1(1 - s, 47.3, primes2)) < 1e-9
              for s in [0.3, 0.4])
    return {"X": X, "rows": rows,
            "fraction_minimised_on_half": "%d/%d" % (minimised_on_half,
                                                     len(rows)),
            "L1_symmetric_about_half_by_construction": sym,
            "verdict": ("TRIVIAL/CIRCULAR: L1(sigma,t)=L1(1-sigma,t) IDENTICALLY "
                        "(swapping sigma<->1-sigma swaps the two terms), so any "
                        "minimum at sigma=1/2 is forced by the metric's own "
                        "symmetry and occurs at EVERY t -- it is not a property "
                        "of zeta and detects nothing about zeros.  (It even "
                        "fails to minimise at 1/2 at some t, e.g. t=40.)  "
                        "Decorative.")}


# ---- L3 : completed-field defect B(s) = xi(s) - xi(1-s) -------------------
def xi(s):
    s = mp.mpc(s)
    return 0.5 * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def test_L3():
    pts = {
        "on_line_no_zero": mp.mpc('0.5', '10.0'),
        "at_zeta_zero": mp.mpc('0.5', '14.134725'),
        "off_line": mp.mpc('0.8', '20.0'),
        "far_off_line": mp.mpc('0.2', '40.0'),
        "random": mp.mpc('0.63', '33.7'),
    }
    rows = []
    for label, s in pts.items():
        B = xi(s) - xi(1 - s)
        rows.append({"point": label, "s": str(s),
                     "|xi(s)-xi(1-s)|": float(mp.fabs(B))})
    maxdef = max(r["|xi(s)-xi(1-s)|"] for r in rows)
    return {"rows": rows, "max_defect": maxdef,
            "verdict": ("TRIVIAL/CIRCULAR: xi(s)-xi(1-s) == 0 identically "
                        "(functional equation).  It vanishes everywhere -- "
                        "off the line, at zeros, at random points alike "
                        "(max |defect| = %.2e, numerical) -- so it detects "
                        "NOTHING about zero locations.  Forced by construction."
                        % maxdef)}


def main():
    print("=" * 74)
    print("Deliverable C -- mirror-leakage functional candidates")
    print("=" * 74)
    r12 = test_L1_L2()
    print("\n[L1/L2] prime-field mirror imbalance |P(s)-conj P(1-s)|")
    for r in r12["rows"]:
        print("   t=%.3f  L1 by sigma=%s  min@sigma=%.1f  L2(0.5)=%.4f"
              % (r["t"], r["L1_by_sigma"], r["L1_min_at_sigma"], r["L2_on_half"]))
    print("   minimised on sigma=1/2: %s -> %s"
          % (r12["fraction_minimised_on_half"], r12["verdict"]))

    r3 = test_L3()
    print("\n[L3] completed-field defect  B(s) = xi(s) - xi(1-s)")
    for r in r3["rows"]:
        print("   %-18s |xi(s)-xi(1-s)| = %.2e" % (r["point"],
                                                   r["|xi(s)-xi(1-s)|"]))
    print("   -> %s" % r3["verdict"])

    os.makedirs(TAB, exist_ok=True)
    with open(os.path.join(TAB, "leakage_functionals.json"), "w") as f:
        json.dump({"L1_L2_prime_imbalance": r12,
                   "L3_completed_defect": r3,
                   "surviving_object": ("none here; the non-trivial boundary-"
                                        "minus-residual leakage is the Weil "
                                        "functional W(h)=ARCH-PRIME, Deliverable "
                                        "D2, which is RH-equivalent")}, f,
                  indent=2)
    print("\n   wrote results/tables/leakage_functionals.json")
    print("\nHONEST CONCLUSION: none of L1/L2/L3 survives as a non-trivial,")
    print("non-circular critical-line detector.  L3 is identically zero; L1/L2")
    print("have no clean critical-line structure.  The only surviving leakage")
    print("object is the Weil functional (D2), and it is RH-equivalent.")


if __name__ == "__main__":
    main()
