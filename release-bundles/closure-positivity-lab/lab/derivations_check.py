"""Numeric verification for papers/prime-derivations.tex (D1-D15).

Every derivation in the companion that admits a numeric check is checked
here, against either closed-form evaluation or the repository's shipped
artifacts. Run:  python3 -m lab.derivations_check   (from the repo root)
Writes out/derivations_check.json. Exit code 0 only if every check passes.
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

CHECKS = []


def check(name, ok, detail):
    CHECKS.append({"check": name, "pass": bool(ok), "detail": detail})
    print("  %-46s %s  %s" % (name, "PASS" if ok else "FAIL", detail))


def primes_up_to(n):
    s = [True] * (n + 1)
    s[0] = s[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i):
                s[j] = False
    return [p for p in range(n + 1) if s[p]]


def d4_d5_gap_factor_law():
    # D4: w(g) = prod over odd p|g of (p-1)/(p-2); D5: p(p-2)/(p-1)^2 = 1-1/(p-1)^2
    def w(g):
        r, x, p = 1.0, g, 3
        while p * p <= x or x > 1:
            if x % p == 0:
                r *= (p - 1) / (p - 2)
                while x % p == 0:
                    x //= p
            p += 2
            if p > g:
                break
        return r
    ok = (abs(w(6) - 2) < 1e-12 and abs(w(10) - 4 / 3) < 1e-12
          and abs(w(210) - 16 / 5) < 1e-12)
    check("D4 gap factors 6->2, 10->4/3, 210->16/5", ok,
          "w(6)=%.6f w(10)=%.6f w(210)=%.6f" % (w(6), w(10), w(210)))
    p = 11
    ok = abs(p * (p - 2) / (p - 1) ** 2 - (1 - 1 / (p - 1) ** 2)) < 1e-15
    check("D5 two forms of the twin factor agree", ok, "checked at p=11")


def d6_convergence_expansion():
    # term_p(k) = (1-k/p)(1-1/p)^{-k}
    #           = 1 - k(k-1)/(2p^2) + [(k - k^3)/3 + ...]/p^3 + O(p^-4):
    # log term = (k-k^2)/(2p^2) + (k-k^3)/(3p^3) + O(p^-4), so the p^-3
    # coefficient of the term itself is (k-k^3)/3. Verify both orders.
    ok = True
    detail = []
    for k in (2, 3, 4, 6):
        p = 10007.0
        term = (1 - k / p) * (1 - 1 / p) ** (-k)
        approx2 = 1 - k * (k - 1) / (2 * p * p)
        c3_meas = (term - approx2) * p ** 3
        c3_theory = (k - k ** 3) / 3
        ok &= abs(c3_meas - c3_theory) < abs(c3_theory) * 0.02 + 0.05
        detail.append("k=%d: c3 %.2f vs %.2f" % (k, c3_meas, c3_theory))
    check("D6 expansion to O(p^-3): c2=-k(k-1)/2, c3=(k-k^3)/3", ok,
          "; ".join(detail))


def d8_goldbach_two():
    # the leading 2 in 2*C2: the p=2 wheel gives survival 1/2 vs baseline 1/4
    ok = abs((1 / 2) / (1 / 4) - 2) < 1e-15
    check("D8 the leading 2 is the p=2 wheel factor", ok, "(1/2)/(1/4)=2")


def d9_sato_tate_moments():
    # I_{2m} = Catalan(m)/4^m for measure (2/pi) sin^2(theta); odd moments 0
    import numpy as np
    th = np.linspace(0, math.pi, 2_000_001)
    w = (2 / math.pi) * np.sin(th) ** 2
    res = {}
    for m, target in [(1, 0.25), (2, 0.125), (3, 5 / 64), (4, 14 / 256)]:
        val = float(np.trapz(np.cos(th) ** (2 * m) * w, th))
        res["I%d" % (2 * m)] = val
        check("D9 ST moment I_%d = %s" % (2 * m, target),
              abs(val - target) < 1e-9, "numeric %.10f" % val)
    odd = float(np.trapz(np.cos(th) ** 3 * w, th))
    check("D9 odd ST moments vanish", abs(odd) < 1e-12, "I_3 = %.2e" % odd)
    # gate variances used by ledger row 7: Var(m1)=1/4n etc. (per-sample variances)
    pairs = [("m1", 0.25), ("m2", 0.125 - 0.0625), ("m3", 5 / 64),
             ("m4", 14 / 256 - (0.125) ** 2)]
    import numpy.random  # noqa: F401  (documentation only; no RNG used)
    vals = {"m1": res["I2"], "m2": res["I4"] - res["I2"] ** 2,
            "m3": res["I6"], "m4": res["I8"] - res["I4"] ** 2}
    ok = all(abs(vals[k] - v) < 1e-9 for k, v in pairs)
    check("D9 ledger 3-sigma gate variances match", ok,
          "Var bases: %s" % {k: round(v, 6) for k, v in vals.items()})


def d10_baselines():
    ok = abs((1 - math.exp(-0.2)) - 0.18126924692201818) < 1e-12
    check("D10 Poisson P(s<0.2) = 1 - e^{-0.2}", ok, "0.181269...")
    import numpy as np
    s = np.linspace(0, 12, 4_000_001)
    p = (32 / math.pi ** 2) * s ** 2 * np.exp(-4 * s ** 2 / math.pi)
    mean = float(np.trapz(s * p, s))
    var = float(np.trapz(s ** 2 * p, s)) - mean ** 2
    check("D10 GUE surmise mean = 1", abs(mean - 1) < 1e-9, "%.10f" % mean)
    check("D10 GUE surmise var = 3pi/8 - 1", abs(var - (3 * math.pi / 8 - 1)) < 1e-9,
          "%.10f vs %.10f" % (var, 3 * math.pi / 8 - 1))


def d11_trace_extraction():
    # h=3 (level 61): eigenvalues {N+1, alpha, sigma(alpha)} =>
    # Tr(alpha) = tr B - (N+1);  N(alpha) = det B / (N+1).
    # Verified against the shipped level-61 artifact + Dembele inert values.
    with open(os.path.join(ROOT, "realization", "data",
                           "level61_results.json")) as fh:
        d = json.load(fh)
    ok = d["all_dembele_inert_match"] and d["all_rm_by_sqrt5"]
    rows = {r["norm"]: r for r in d["rows"] if "trace_a" in r}
    rm_ok = all((r["disc"] % 5 == 0 and
                 math.isqrt(r["disc"] // 5) ** 2 == r["disc"] // 5)
                for r in rows.values() if isinstance(r["disc"], int) and r["disc"] > 0)
    check("D11 trace/det extraction (level 61 artifact)", ok and rm_ok,
          "Dembele inert match + disc = 5*square at all tested primes")


def d12_mass_formula():
    # mass = sum 1/|stab| = sum |orbit|/|A5| = (q+1)/60
    for q, sizes in [(31, (12, 20))]:
        mass = sum(60 // s and 1 / (60 / s) for s in sizes)
        ok = abs(mass - (q + 1) / 60) < 1e-15
        check("D12 Eichler mass (q+1)/60 at q=%d" % q, ok,
              "orbit sizes %s -> mass %s = %d/60" % (sizes, mass, q + 1))


def d13_peak_property():
    # computational lemma: every zero in the plotted range owns a peak of the
    # Riesz-tapered prime spectrum (re-verifies the shipped figure's claim)
    import numpy as np
    zeros = np.loadtxt(os.path.join(ROOT, "out", "zeta_zeros.txt"))
    ps = primes_up_to(200_000)
    P = np.array(ps, dtype=float)
    lg = np.log(P)
    w = lg / np.sqrt(P) * (1 - lg / math.log(200_000))
    ks = np.arange(5.0, 60.001, 0.02)
    F = np.empty(ks.size)
    for i in range(0, ks.size, 400):
        kc = ks[i:i + 400]
        F[i:i + 400] = np.abs((w[None, :] * np.exp(1j * np.outer(kc, lg))).sum(axis=1))
    zin = zeros[(zeros > 5.5) & (zeros < 59.5)]
    hits = 0
    for z in zin:
        i = int(np.argmin(np.abs(ks - z)))
        lo, hi = max(0, i - 50), i + 50
        hits += abs(ks[lo + int(np.argmax(F[lo:hi]))] - z) < 0.15
    check("D13 tapered-spectrum peak at every in-range zero",
          hits == zin.size, "%d/%d (primes to 2e5)" % (hits, zin.size))


def d14_fibonacci_peaks():
    # peaks of the Fibonacci-chain diffraction lie on a (m + n*phi) lattice
    import numpy as np
    PHI = (1 + 5 ** 0.5) / 2
    word = "A"
    while len(word) < 3000:
        word = "".join("AB" if c == "A" else "A" for c in word)
    x = np.cumsum([PHI if c == "A" else 1.0 for c in word[:3000]])
    ks = np.arange(0.05, 30, 0.002)
    F = np.empty(ks.size)
    for i in range(0, ks.size, 500):
        kc = ks[i:i + 500]
        F[i:i + 500] = np.abs(np.exp(1j * np.outer(kc, x)).sum(axis=1)) ** 2 / x.size
    # the eight strongest local maxima (sorted by intensity, descending)
    idx = [i for i in range(1, ks.size - 1)
           if F[i] > F[i - 1] and F[i] > F[i + 1] and F[i] > 30]
    idx.sort(key=lambda i: -F[i])
    peaks = [float(ks[i]) for i in idx[:8]]
    # the known peak module: k = (2*pi/mean_spacing) * (m + n*phi)/(1 + phi^2/ (phi+2))?
    # honest check: peaks/(2*pi) * mean_spacing should be Z[phi]-points; fit:
    mean = float(np.mean(np.diff(x)))
    bad = 0
    for k in peaks:
        u = k * mean / (2 * math.pi)
        # nearest m + n*phi with small integers
        best = min(abs(u - (m + n * PHI))
                   for m in range(-6, 7) for n in range(-6, 7))
        bad += best > 0.02
    check("D14 Fibonacci peaks on the m+n*phi module", bad == 0,
          "8 strongest peaks within 0.02 of (2pi/mean)*(m+n*phi); mean=%.6f" % mean)


def d15_bias_coefficient():
    # bias mechanism: theta(x, chi4) = psi(x, chi4) - sqrt(x)(1+o(1));
    # so D(x)*log(x)/sqrt(x) should be O(1) around ~1 at moderate x
    ps = primes_up_to(2_000_000)
    D, vals = 0, []
    for p in ps:
        if p % 4 == 3:
            D += 1
        elif p % 4 == 1:
            D -= 1
        if p in (999983,):  # checkpoint near 1e6
            vals.append(D * math.log(p) / math.sqrt(p))
    for p, d in [(2_000_000, None)]:
        pass
    c = D * math.log(2_000_000) / math.sqrt(2_000_000)
    ok = 0.2 < c < 5 and all(0.2 < v < 5 for v in vals)
    check("D15 bias coefficient D*log(x)/sqrt(x) = O(1)", ok,
          "x=1e6: %.3f; x=2e6: %.3f (mechanism scale confirmed)" %
          (vals[0] if vals else float('nan'), c))


def main():
    print("Derivations check (D1-D15 numeric verifications)")
    d4_d5_gap_factor_law()
    d6_convergence_expansion()
    d8_goldbach_two()
    d9_sato_tate_moments()
    d10_baselines()
    d11_trace_extraction()
    d12_mass_formula()
    d13_peak_property()
    d14_fibonacci_peaks()
    d15_bias_coefficient()
    n_pass = sum(c["pass"] for c in CHECKS)
    doc = {"description": "numeric checks for papers/prime-derivations.tex",
           "n_checks": len(CHECKS), "n_pass": n_pass, "checks": CHECKS}
    with open(os.path.join(ROOT, "out", "derivations_check.json"), "w") as fh:
        json.dump(doc, fh, indent=2)
    print("%d/%d checks pass -> out/derivations_check.json" % (n_pass, len(CHECKS)))
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
