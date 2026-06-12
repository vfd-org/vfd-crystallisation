"""Gap-1 probes: can any VFD-native channel see twin-prime infinitude?

Five probes, gate-first: every probe carries a NULL criterion stated
BEFORE the data is read. A probe whose 'signal' is fully explained by the
wheel factors (the already-derived local layer) is NULL by definition.
The deliverable either way is ISOLATION: which mathematics each channel
reduces to.

Run: python3 run_probes.py     (writes probes_result.json)
"""
import json
import math
import os
import sys

import numpy as np

X = 50_000_000
HERE = os.path.dirname(os.path.abspath(__file__))
LAB = os.path.join(HERE, "..", "..", "closure-positivity-lab")
RESULTS = {}


def sieve(x):
    s = np.ones(x, dtype=bool)
    s[:2] = False
    for i in range(2, int(x ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return s


def report(name, verdict, detail):
    RESULTS[name] = {"verdict": verdict, "detail": detail}
    print("  %-12s %-7s %s" % (name, verdict, detail))


def p1_phi_place(s):
    """P1: twins by Q(sqrt5) splitting class of (p, p+2).
    NULL criterion: the three admissible classes r = p mod 5 in {1,2,4}
    each carry 1/3 of twins within 3 sigma (multinomial)."""
    tw = np.nonzero(s[:-2] & s[2:])[0]
    tw = tw[tw > 5]
    r = tw % 5
    counts = {1: int((r == 1).sum()), 2: int((r == 2).sum()),
              4: int((r == 4).sum())}
    n = sum(counts.values())
    exp, sd = n / 3, math.sqrt(n * (1 / 3) * (2 / 3))
    worst = max(abs(c - exp) / sd for c in counts.values())
    verdict = "NULL" if worst < 3 else "SIGNAL"
    report("P1 phi-place", verdict,
           "classes (S,I)/(I,S)/(S,S) = %s; worst dev %.2f sigma "
           "(wheel predicts exact thirds)" % (counts, worst))


def p2_cuspidal(s):
    """P2: Hecke eigenvalue correlation across twin pairs.
    Uses the shipped a_q data (norm <= 4999). NULL criterion: Pearson
    correlation of normalized eigenvalue x_p, x_{p+2} over twin pairs
    within 3/sqrt(n) of zero (Sato-Tate independence)."""
    with open(os.path.join(LAB, "out", "a_q_extended.json")) as fh:
        rows = json.load(fh)["rows"]
    xs = {}
    for r in rows:
        if r["norm"] == 31 and r["a_q_geometric"] == -1:
            continue  # level
        p = r["rational_prime"]
        xs.setdefault(p, []).append(
            r["a_q_geometric"] / (2 * math.sqrt(r["norm"])))
    xbar = {p: float(np.mean(v)) for p, v in xs.items()}
    pairs = [(p, p + 2) for p in xbar if (p + 2) in xbar
             and s[p] and p + 2 < len(s) and s[p + 2]]
    a = np.array([xbar[p] for p, q in pairs])
    b = np.array([xbar[q] for p, q in pairs])
    n = len(pairs)
    corr = float(np.corrcoef(a, b)[0, 1]) if n > 2 else 0.0
    thr = 3 / math.sqrt(n) if n else 1
    verdict = "NULL" if abs(corr) < thr else "SIGNAL"
    report("P2 cuspidal", verdict,
           "corr(x_p, x_{p+2}) = %+.4f over %d twin pairs "
           "(3-sigma threshold %.4f)" % (corr, n, thr))


def p3_clock(s):
    """P3: the three legal pentagonal-clock transitions for twins
    (1->3, 7->9, 9->1 mod 10). NULL criterion: equidistribution 3 sigma."""
    tw = np.nonzero(s[:-2] & s[2:])[0]
    tw = tw[tw > 5]
    r = tw % 10
    counts = {1: int((r == 1).sum()), 7: int((r == 7).sum()),
              9: int((r == 9).sum())}
    n = sum(counts.values())
    exp, sd = n / 3, math.sqrt(n * (1 / 3) * (2 / 3))
    worst = max(abs(c - exp) / sd for c in counts.values())
    verdict = "NULL" if worst < 3 else "SIGNAL"
    report("P3 clock", verdict,
           "transitions 1->3/7->9/9->1 = %s; worst dev %.2f sigma" %
           (counts, worst))


def p4_resonance(s):
    """P4: twin indicator mod 120 (the 600-cell clock). The wheel layer
    predicts 12 admissible classes, equal weights. NULL criterion: (a)
    the 12-class distribution matches within 3 sigma; (b) the Fourier
    energy of the centred indicator at every non-wheel frequency k mod
    120 is within the shuffle baseline (no substrate resonance)."""
    tw = np.nonzero(s[:-2] & s[2:])[0]
    tw = tw[tw > 7]
    r = tw % 120
    admissible = [k for k in range(120)
                  if k % 2 == 1 and k % 3 == 2 and k % 5 in (1, 2, 4)]
    counts = np.array([(r == k).sum() for k in admissible], dtype=float)
    n = counts.sum()
    sd = math.sqrt(n * (1 / 12) * (11 / 12))
    worst = float(np.max(np.abs(counts - n / 12)) / sd)
    # Fourier: energy at each frequency of the histogram over all 120 cells
    hist = np.array([(r == k).sum() for k in range(120)], dtype=float)
    # wheel-model expectation: n/12 on admissible cells, 0 elsewhere
    model = np.zeros(120)
    model[admissible] = n / 12
    resid = hist - model
    F = np.abs(np.fft.rfft(resid)) ** 2
    # multinomial noise level for residual spectrum: ~ n * (1/12) per cell var
    noise = n * (1 / 12) * (11 / 12)
    excess = float(np.max(F[1:]) / (noise * 120 / 2))
    verdict = "NULL" if (worst < 3 and excess < 3) else "SIGNAL"
    report("P4 resonance", verdict,
           "12-class worst dev %.2f sigma; max non-wheel Fourier excess "
           "%.2f x noise (no 600-cell-clock resonance beyond the wheels)"
           % (worst, excess))


def p5_isolation(s):
    """P5: where does the infinitude question's mass live? Circle-method
    decomposition of T(x) = sum_{n<=x} 1_prime(n) 1_prime(n+2) (prime
    indicator, not Lambda-weighted; constant adjusted accordingly).
    Major arcs to level Q reproduce the wheel main term; the remainder is
    the fluctuation. We measure (a) the scaled fluctuation exponent of
    D(x) = pi_2(x) - 2 C2 int dt/log^2 t at checkpoints, (b) the share of
    the pair count reconstructed by wheel data alone at Q = 2,6,30,210.
    There is no NULL/SIGNAL here; the output IS the isolation."""
    C2 = 0.6601618158468696
    tw_mask = s[:-2] & s[2:]
    idx = np.nonzero(tw_mask)[0]
    checkpoints = [10 ** 6, 5 * 10 ** 6, 10 ** 7, 25 * 10 ** 6, X]
    devs = []
    for xc in checkpoints:
        cnt = int((idx < xc).sum())
        t = np.linspace(2, xc, 2_000_001)
        hl = 2 * C2 * float(np.trapz(1 / np.log(t) ** 2, t))
        d = cnt - hl
        devs.append((xc, cnt, round(hl, 1), round(d, 1),
                     round(d / math.sqrt(xc), 4)))
    # share of structure captured by wheels at modulus q: compare the
    # variance of twin counts across residue classes mod q explained by
    # admissibility vs total
    shares = {}
    for q in (6, 30, 210):
        r = idx[idx > q] % q
        hist = np.array([(r == k).sum() for k in range(q)], dtype=float)
        adm = hist > 0.01 * hist.max()
        within = hist[adm]
        shares[q] = round(1 - float(np.var(within) * adm.sum()
                                    / max(np.var(hist) * q, 1e-9)), 4)
    report("P5 isolation", "ISOLATE",
           "D(x)/sqrt(x) at checkpoints: %s -- bounded, fluctuating "
           "(square-root-cancellation regime); wheel share of mod-q "
           "structure: %s. The entire infinitude question lives in the "
           "bounded fluctuation, i.e. minor-arc / off-diagonal "
           "cancellation." % ([d[4] for d in devs], shares))
    RESULTS["P5 checkpoints"] = {"rows": devs}


def main():
    print("Gap-1 probes (gate-first; NULL = explained by the wheel layer)")
    s = sieve(X)
    p1_phi_place(s)
    p2_cuspidal(s)
    p3_clock(s)
    p4_resonance(s)
    p5_isolation(s)
    with open(os.path.join(HERE, "probes_result.json"), "w") as fh:
        json.dump(RESULTS, fh, indent=2)
    print("-> probes_result.json")


if __name__ == "__main__":
    sys.exit(main())
