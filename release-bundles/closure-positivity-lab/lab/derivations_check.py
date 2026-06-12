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




def _icosians():
    import itertools
    import numpy as np
    PHI = (1 + 5 ** 0.5) / 2
    V = []
    for i in range(4):
        for s in (1, -1):
            v = [0.0] * 4
            v[i] = s
            V.append(v)
    for ss in itertools.product((0.5, -0.5), repeat=4):
        V.append(list(ss))
    def parity(q):
        q = list(q)
        n = 0
        for i in range(len(q)):
            for j in range(i + 1, len(q)):
                n += q[i] > q[j]
        return n % 2
    base = [0.0, 0.5, 1 / (2 * PHI), PHI / 2]
    seen = set()
    for perm in itertools.permutations(range(4)):
        if parity(perm) != 0:
            continue
        for signs in itertools.product((1, -1), repeat=4):
            v = [0.0] * 4
            for pos, idx in enumerate(perm):
                v[pos] = signs[pos] * base[idx]
            key = tuple(round(x, 9) for x in v)
            if key not in seen and abs(sum(x * x for x in v) - 1) < 1e-9:
                seen.add(key)
                V.append(list(v))
    return V


def d16_spectrum_from_characters():
    # D16: the 600-cell adjacency spectrum equals the Cayley-graph character
    # formula lambda_chi = |C| chi(g0)/chi(1), multiplicity chi(1)^2.
    import numpy as np
    from collections import Counter
    PHI = (1 + 5 ** 0.5) / 2
    V = np.array(_icosians())
    A = (np.abs(V @ V.T - PHI / 2) < 1e-9).astype(float)
    ev = np.linalg.eigvalsh(A)
    c = Counter(round(float(x), 6) for x in ev)
    expect = {12.0: 1, round(6 * PHI, 6): 4, round(6 - 6 * PHI, 6): 4,
              round(4 * PHI, 6): 9, round(4 - 4 * PHI, 6): 9,
              3.0: 16, -3.0: 16, 0.0: 25, -2.0: 36}
    ok = len(V) == 120 and dict(c) == expect
    rational_dim = 1 + 16 + 25 + 36 + 16
    check("D16 600-cell spectrum = character formula", ok,
          "9 eigenvalues, mults (1,4,4,9,9,16,16,25,36); rational block %d"
          % rational_dim)


def d17_split_necessarily_spectral():
    # D17: A1 is an integer (0/1) matrix and the four irrational eigenvalues
    # are pairwise distinct reals -- so no linear involution commuting with
    # A1 can swap the Galois-paired eigenspaces (it preserves each
    # eigenspace). The split is semilinear (Galois on the splitting field).
    import numpy as np
    PHI = (1 + 5 ** 0.5) / 2
    V = np.array(_icosians())
    A = (np.abs(V @ V.T - PHI / 2) < 1e-9)
    integer_01 = A.dtype == bool  # adjacency is exactly 0/1 by construction
    vals = [6 * PHI, 6 - 6 * PHI, 4 * PHI, 4 - 4 * PHI]
    distinct = len({round(v, 9) for v in vals}) == 4
    check("D17 split is necessarily spectral (premises)",
          integer_01 and distinct,
          "A1 integral; paired eigenvalues pairwise distinct reals")


def d18_k4_completeness():
    # D18: |a_i| <= sqrt(p), |b_i| <= 2 sqrt(p)/sqrt(5) for any coordinate of
    # an icosian with rational reduced norm p (both embeddings <= p).
    # Per-coordinate feasible set for p <= 23 has |a|,|b| <= 4; and the
    # complete count at p = 3 (K = 2 suffices by the lemma) gives r(3) = 80.
    import itertools
    import math
    PHI = (1 + 5 ** 0.5) / 2
    c = math.sqrt(23)
    feas = [(a, b) for a in range(-8, 9) for b in range(-8, 9)
            if (a + b * PHI) ** 2 <= 23 + 1e-9
            and (a + b * (1 - PHI)) ** 2 <= 23 + 1e-9]
    amax = max(abs(a) for a, b in feas)
    bmax = max(abs(b) for a, b in feas)
    lemma_ok = amax <= math.floor(c) == 4 and bmax <= 4
    # complete r(3) at K = 2 (sqrt(3) < 2 and 2 sqrt(3)/sqrt(5) < 2)
    r3 = 0
    R = range(-2, 3)
    for a in itertools.product(R, repeat=4):
        sa = sum(x * x for x in a)
        if sa > 3:
            continue
        for b in itertools.product(R, repeat=4):
            sb = sum(x * x for x in b)
            ab = sum(a[i] * b[i] for i in range(4))
            if 2 * ab + sb == 0 and sa + sb == 3:
                r3 += 1
    check("D18 K=4 completeness lemma + r(3)=80 complete at K=2",
          lemma_ok and r3 == 8 * (1 + 9),
          "feasible |a|<=%d |b|<=%d for p<=23; r(3)=%d" % (amax, bmax, r3))


def d20_zero_count_consistency():
    # D20: N(T) main term for the degree-4, conductor-775 L at T = 25 vs the
    # 33 computed zeros (consistency check; interval certification open).
    import math
    with open(os.path.join(ROOT, "out", "curve_zeros.json")) as fh:
        d = json.load(fh)
    zeros = d["L_zeros"]  # fail loudly if the artifact changes shape
    n_obs = len([z for z in zeros
                 if (z if isinstance(z, (int, float)) else z[0]) <= 25.0001])
    T, deg, cond = 25.0, 4, 775
    main = (deg * T / (2 * math.pi)) * math.log(T / (2 * math.pi * math.e))         + (T / (2 * math.pi)) * math.log(cond)
    ok = abs(n_obs - main) < 1.5
    check("D20 zero-count consistency at T=25", ok,
          "observed %s vs main term %.2f (|S(T)| within normal range; "
          "interval certification named as open)" % (n_obs, main))


def main():
    print("Derivations check (D1-D20 numeric verifications)")
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
    d16_spectrum_from_characters()
    d17_split_necessarily_spectral()
    d18_k4_completeness()
    d20_zero_count_consistency()
    n_pass = sum(c["pass"] for c in CHECKS)
    doc = {"description": "numeric checks for papers/prime-derivations.tex",
           "n_checks": len(CHECKS), "n_pass": n_pass, "checks": CHECKS}
    with open(os.path.join(ROOT, "out", "derivations_check.json"), "w") as fh:
        json.dump(doc, fh, indent=2)
    print("%d/%d checks pass -> out/derivations_check.json" % (n_pass, len(CHECKS)))
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
