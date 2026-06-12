"""
PRIORITY DOMAIN.  Prime trace vs fake-prime controls.

Question (the honest RH bridge prerequisite): does a closure diagnostic distinguish
TRUE arithmetic structure from density-matched fakes?  If fakes look identical, we do
not yet have an RH key.

Two layers, reported separately and honestly:

  LAYER 1 (trivial).  Triad/residue phase tau(n)=n mod 3 (and last digit mod 10).
    Primes>3 NEVER hit 0 mod 3; a naive density-matched random control does (~1/3).
    -> trivial separation, but it is just coprimality, not deep closure.  We say so.

  LAYER 2 (subtle, the real test).  Consecutive last-digit TRANSITION matrix mod 10
    on {1,3,7,9}.  Real primes carry the Lemke-Oliver--Soundararajan correlation
    (consecutive primes avoid repeating their last digit).  CONTROL = the SAME primes
    SHUFFLED (identical marginals, correlation destroyed) and a SIEVE-MATCHED memoryless
    model (independent coprime residues).  Closure residual = chi-square distance of the
    joint transition law from the independent product of marginals.

    Real primes -> LARGE residual (real correlation); shuffled/independent -> ~0.
    This is a KNOWN statistical bias (LO-S 2016), DETECTED by the engine as a
    closure-correlation signature.  It does NOT touch the Weil-positivity / RH wall.
"""
import numpy as np


def primes_upto(N):
    s = np.ones(N + 1, bool); s[:2] = False
    for i in range(2, int(N**0.5) + 1):
        if s[i]:
            s[i*i::i] = False
    return np.nonzero(s)[0]


def last_digit_transition(seq_digits, alphabet=(1, 3, 7, 9)):
    idx = {d: i for i, d in enumerate(alphabet)}
    K = len(alphabet)
    M = np.zeros((K, K))
    for a, b in zip(seq_digits[:-1], seq_digits[1:]):
        if a in idx and b in idx:
            M[idx[a], idx[b]] += 1
    row = M.sum(1, keepdims=True)
    T = M / np.maximum(row, 1)             # conditional transition probs
    marg = M.sum(0) / M.sum()              # next-digit marginal
    indep = np.repeat(marg[None, :], K, axis=0)
    # chi-square-like closure residual: joint vs product-of-marginals
    joint = M / M.sum()
    pm = (M.sum(1) / M.sum())
    prod = np.outer(pm, marg)
    resid = float(np.sum((joint - prod) ** 2 / np.maximum(prod, 1e-12)))
    return dict(T=T, residual=resid, marginal=marg)


def run(N=3_000_000, seed=0):
    P = primes_upto(N)
    P = P[P > 5]
    rng = np.random.default_rng(seed)

    # --- LAYER 1: residue mod 3 (triad leg) ---
    def mod3_hist(arr):
        h = np.bincount(arr % 3, minlength=3) / len(arr)
        return h
    prime_mod3 = mod3_hist(P)
    # naive density-matched random integers (Cramer-like inclusion) over same range
    x = np.arange(7, N)
    keep = rng.random(len(x)) < 1.0 / np.log(x)
    naive = x[keep]
    naive_mod3 = mod3_hist(naive)
    layer1_separates = bool(prime_mod3[0] < 1e-6 and naive_mod3[0] > 0.2)

    # --- LAYER 2: last-digit transition correlation (LO-S) ---
    pd = (P % 10)
    real = last_digit_transition(pd)
    # control A: shuffle primes -> same marginals, kill correlation
    shuf = pd.copy(); rng.shuffle(shuf)
    shuffled = last_digit_transition(shuf)
    # control B: sieve-matched independent coprime-to-10 draws with prime marginals
    indep_draw = rng.choice([1, 3, 7, 9], size=len(pd), p=real["marginal"])
    indep = last_digit_transition(indep_draw)

    sep_ratio = real["residual"] / max(shuffled["residual"], 1e-9)
    layer2_separates = bool(real["residual"] > 10 * max(shuffled["residual"], indep["residual"]))

    return dict(
        n_primes=int(len(P)),
        layer1_residue=dict(prime_mod3=[float(v) for v in prime_mod3],
                            naive_random_mod3=[float(v) for v in naive_mod3],
                            separates=layer1_separates,
                            note="trivial: primes>3 coprime to 3; naive control is not. Coprimality, not deep closure."),
        layer2_transition=dict(real_residual=real["residual"],
                              shuffled_residual=shuffled["residual"],
                              independent_residual=indep["residual"],
                              separation_ratio=sep_ratio,
                              real_transition=[[round(float(v),4) for v in r] for r in real["T"]],
                              separates=layer2_separates,
                              note="Lemke-Oliver--Soundararajan consecutive-digit avoidance: real correlation "
                                   "absent in shuffled/independent controls. KNOWN bias; detected as closure residual; "
                                   "does NOT touch Weil positivity / RH."),
        verdict=("SEPARATES from controls (layer1 trivial + layer2 real LO-S correlation)"
                 if (layer1_separates and layer2_separates) else "CONTROL_FAIL"),
        rh_relevance="NONE for the positivity wall: distinguishing primes from fakes via correlation "
                     "is necessary hygiene but is not the missing Weil-positivity invariant.")


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2, default=str))
