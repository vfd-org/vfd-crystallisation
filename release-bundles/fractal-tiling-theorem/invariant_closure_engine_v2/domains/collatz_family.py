"""
PRIORITY DOMAIN.  Collatz family qn+1 + admissible-braid / cycle analysis.

Two genuinely falsifiable products:

(1) FAMILY DISCRIMINATION (controlled): same capacity Q = a*ln2 - ln q per odd step
    classifies 3n+1 as closing, 5n/7n/9n+1 as escaping -- and we ALSO search for the
    longest non-closing window (worst excursion) to be honest about rare braids.

(2) CYCLE PROOF-WALL EXTRACTION (frontier): the closure condition for a k-odd-step
    cycle of the shortcut map  x -> (q*x+1)/2^a  is the EXACT Diophantine equation

        n*(2^A - q^k) = SUM_{j=0}^{k-1} q^{k-1-j} * 2^{s_j},   s_j = a_1+...+a_j, s_0=0

    A cycle is a PHASE-CLOSURE (the braid returns) and has total capacity
    Q_cycle = ln(2^A / q^k) > 0  (needs 2^A > q^k).  This lets us:
      - ELIMINATE 1-cycles exactly: n = 1/(2^a - q) integer>0 forces 2^a - q = 1.
        For q=3: 2^a=4, a=2, n=1 (only the trivial cycle).  [reproduces Steiner 1977]
      - bounded search over small k for nontrivial cycles (reproduces 'no small cycles').
    This REPRODUCES KNOWN RESULTS via the closure route; it does NOT extend them.
    The open theorem stays open: no admissible INFINITE braid keeps cumulative Q<=0.
"""
import math, json
from fractions import Fraction


# ----- (1) family capacity + worst-window braid search -------------------- #
def odd_step(n, q):
    m = q * n + 1
    a = (m & -m).bit_length() - 1
    return m >> a, a


def family_capacity(q, seeds, max_odd=3000):
    L2, Lq = math.log(2), math.log(q)
    qs, worst_window = [], 0.0
    for n0 in seeds:
        n, steps, cum, run = n0, 0, 0.0, 0
        while steps < max_odd and n != 1:
            if n % 2 == 0:
                n //= 2; continue
            n, a = odd_step(n, q)
            qi = a * L2 - Lq
            qs.append(qi)
            cum = min(0.0, cum + qi)          # track sustained non-closing excursion
            worst_window = min(worst_window, cum)
            steps += 1
            if n > 10**60:
                break
    Qbar = sum(qs) / len(qs)
    cls = "STABLE-CLOSURE" if Qbar > 1e-3 else ("ESCAPE-LEAKAGE" if Qbar < -1e-3 else "CRITICAL-BOUNDARY")
    return dict(q=q, Qbar=Qbar, closed_form_Qbar=2 * L2 - Lq,
                worst_nonclosing_window=worst_window, classify=cls)


# ----- (2) cycle Diophantine equation + elimination ------------------------ #
def one_cycle_elimination(q):
    """A 1-cycle needs n = 1/(2^a - q), positive integer -> 2^a - q = 1.
    Returns the unique solution(s); for q=3 only the trivial n=1 (a=2)."""
    sols = []
    for a in range(1, 40):
        d = 2**a - q
        if d <= 0:
            continue
        if Fraction(1, d).denominator == 1:   # 1/d integer
            n = 1 // d
            if n >= 1 and (q * n + 1) % (2**a) == 0 and (q * n + 1) >> a == n:
                sols.append(dict(a=a, n=n, trivial=(n == 1)))
    return sols


def cycle_equation_n(q, a_list):
    """Given valuations a_1..a_k, return the rational n forced by cycle closure
    (or None if 2^A = q^k).  Cycle exists only if n is a positive ODD integer
    AND iterating actually reproduces a_list."""
    k = len(a_list)
    A = sum(a_list)
    denom = 2**A - q**k
    if denom == 0:
        return None
    s = 0; num = 0
    for j in range(k):
        num += q**(k - 1 - j) * (2**s)
        s += a_list[j]
    val = Fraction(num, denom)
    return val


def small_cycle_search(q, kmax=6, amax=4):
    """Search compositions a_1..a_k (1<=a_i<=amax) with 2^A>q^k for genuine cycles.
    Reports any NONTRIVIAL cycle found.  Reproduces 'no small nontrivial cycles'."""
    from itertools import product
    found_nontrivial = []
    checked = 0
    for k in range(1, kmax + 1):
        for a in product(range(1, amax + 1), repeat=k):
            A = sum(a)
            if 2**A <= q**k:
                continue                      # need positivity 2^A>q^k
            checked += 1
            val = cycle_equation_n(q, list(a))
            if val is None or val.denominator != 1:
                continue
            n = int(val)
            if n < 1 or n % 2 == 0:
                continue
            # verify the orbit really closes with exactly these valuations
            m, ok = n, True
            for ai in a:
                nxt, av = odd_step(m, q)
                if av != ai:
                    ok = False; break
                m = nxt
            if ok and m == n:
                if not (q == 3 and n == 1):
                    found_nontrivial.append(dict(q=q, k=k, a=list(a), n=n))
    return dict(q=q, kmax=kmax, amax=amax, compositions_checked=checked,
                nontrivial_cycles=found_nontrivial)


def run():
    seeds = list(range(3, 6000, 2))
    fam = {q: family_capacity(q, seeds) for q in [3, 5, 7, 9]}
    control_ok = (fam[3]["classify"] == "STABLE-CLOSURE"
                  and all(fam[q]["classify"] == "ESCAPE-LEAKAGE" for q in [5, 7, 9]))
    one_cyc = {q: one_cycle_elimination(q) for q in [3, 5, 7]}
    small = {q: small_cycle_search(q, kmax=6, amax=4) for q in [3]}
    # narrowing: did we eliminate the 1-cycle class for 3n+1 (only trivial survives)?
    elim_1cycle_3 = (len(one_cyc[3]) == 1 and one_cyc[3][0]["trivial"])
    no_small_cycles_3 = (len(small[3]["nontrivial_cycles"]) == 0)
    return dict(family=fam, control_discriminates=control_ok,
                one_cycle=one_cyc, small_cycle_search=small,
                narrowing=dict(eliminated_1cycle_class_3nplus1=elim_1cycle_3,
                               no_small_nontrivial_cycles_3nplus1=no_small_cycles_3,
                               reproduces="Steiner 1977 (no nontrivial 1-cycle) + no small cycles, via closure route"),
                closure_mode="ISOMETRIC (a cycle is a phase-return braid) with capacity Q_cycle=ln(2^A/q^k)>0",
                open_wall="no admissible INFINITE braid keeps cumulative Q<=0 forever (= Collatz)")


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, default=str))
