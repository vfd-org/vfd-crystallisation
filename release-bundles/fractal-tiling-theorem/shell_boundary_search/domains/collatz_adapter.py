"""
CENTREPIECE.  Collatz shell-rung geometry and the admissibility automaton.

Shell index:   h(n) = floor(log2 n)        (magnitude shell)
Transformation T-map:  n -> n/2 (even) | (3n+1)/2 (odd)
Rung:          the parity bit p_i = (n_i mod 2) at step i. p=1 expansion rung
               (x ~3/2), p=0 compression rung (x ~1/2).
Rung capacity per step (log-drift):
               q = ln(3/2)  if p=1   (+0.405, expansion)
                 = ln(1/2)  if p=0   (-0.693, compression)
A parity word escapes (grows) iff its fraction of ones exceeds ln2/ln3 ~ 0.6309.

KNOWN THEOREM (Terras 1976; Lagarias survey): the parity vector of length k is a
BIJECTION  Z/2^k  ->  {0,1}^k.  I.e. the rung grammar is the FULL one-sided shift:
EVERY finite parity word is admissible and realised by a residue class of integers.

We verify this bijection directly, then draw the certificate-class conclusion:

  >> Because the rung grammar is the full shift, every finite 'escape word'
     (fraction of ones > 0.6309) is admissible. Therefore NO finite-state automaton
     on rung-words can be a Collatz closure certificate: there is no forbidden finite
     pattern to exclude. Any certificate must be GLOBAL (control cumulative drift over
     the realised 2-adic measure) -- which is the open conjecture.

This RULES OUT an entire class of attempted certificates (finite rung automata). It is
an honest, sharp localisation of the proof wall, NOT a proof of Collatz.
"""
import math, json
import numpy as np

LN32, LN12 = math.log(1.5), math.log(0.5)
THRESH = math.log(2) / math.log(3)   # 0.63093...


def parity_vector(n, k):
    """T-map parity vector of length k starting from n."""
    p = []
    for _ in range(k):
        b = n & 1
        p.append(b)
        n = (3 * n + 1) // 2 if b else n // 2
    return tuple(p)


def verify_terras_bijection(kmax=12):
    """For each k<=kmax, enumerate n in [0,2^k) and confirm the parity vectors are all
    2^k distinct (the bijection Z/2^k -> {0,1}^k). Returns per-k result."""
    out = {}
    for k in range(1, kmax + 1):
        seen = set()
        for n in range(2 ** k):
            seen.add(parity_vector(n, k))
        out[k] = dict(distinct=len(seen), expected=2 ** k, bijection=(len(seen) == 2 ** k))
    return out


def word_capacity(word):
    """Cumulative log-drift of a parity word; >0 grows (escape), <0 decays (closure)."""
    ones = sum(word)
    return ones * LN32 + (len(word) - ones) * LN12


def escape_words_realised(k=10, sample_n=2 ** 20):
    """Confirm that escape words (fraction of ones > threshold) are realised by actual
    integers, and that their realising integers do NOT sustain escape (the excess is
    'paid back' by later compression) -- consistent with the conjecture, and showing the
    escape is not forbidden at any finite length."""
    # all-ones word of length k: maximally escaping; realised by some residue (bijection)
    # find smallest n>1 whose first-k parity vector is all ones
    target = tuple([1] * k)
    found = None
    for n in range(1, sample_n, 2):
        if parity_vector(n, k) == target:
            found = n; break
    # its longer behaviour: does it keep escaping?
    longer = parity_vector(found, 3 * k) if found else None
    later_ones_frac = (sum(longer) / len(longer)) if longer else None
    return dict(k=k, all_ones_word=target, capacity=word_capacity(target),
                realised_by_smallest_n=found,
                longer_parity_fraction_ones=later_ones_frac,
                note="all-ones (max-escape) word realised by a positive integer; its longer "
                     "trajectory's ones-fraction drops back toward/below threshold -- escape not sustained, "
                     "but NOT forbidden at finite length")


def run():
    bij = verify_terras_bijection(kmax=12)
    full_shift = all(v["bijection"] for v in bij.values())
    esc = escape_words_realised(k=10)
    # count of admissible escape words of length k (fraction ones > threshold)
    from math import comb
    k = 12
    n_escape = sum(comb(k, j) for j in range(k + 1) if j / k > THRESH)
    return dict(
        domain="collatz",
        shell="h(n)=floor(log2 n); rung = parity bit; q=ln(3/2) or ln(1/2)",
        terras_bijection=bij,
        rung_grammar_is_full_shift=full_shift,
        escape_threshold_ones_fraction=THRESH,
        admissible_escape_words_len12=int(n_escape),
        escape_realisation=esc,
        certificate_class_conclusion=(
            "Rung grammar = full one-sided shift (Terras bijection, verified). Every finite "
            "escape word is admissible & realised. => NO finite rung-word automaton can certify "
            "Collatz closure (nothing to forbid). Any certificate must be GLOBAL over the realised "
            "2-adic measure = the open conjecture."),
        mode="DISSIPATIVE-ON-AVERAGE (mean drift = ln(3/2)*0.5+ln(1/2)*0.5 < 0 over the uniform "
             "2-adic measure where ones-fraction->1/2 < threshold), but NOT certifiable by a finite automaton",
        status="MEDIUM PASS: recovers Terras 1976 + draws the certificate-class exclusion (NEW framing); "
               "no new theorem about Collatz; wall localised, not removed",
        no_proof_claim=True)


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, default=str))
