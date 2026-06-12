# Control Results

Every controlled/frontier domain ran against explicit controls; a result is accepted only if the true system separates.

## Collatz family (controls = 5n+1, 7n+1, 9n+1)
- 3n+1 Q̄=0.272 STABLE; worst non-closing window -6.38
- 5n+1 Q̄=-0.177 ESCAPE-LEAKAGE
- 7n+1 Q̄=-0.560 ESCAPE-LEAKAGE
- 9n+1 Q̄=-0.810 ESCAPE-LEAKAGE
- **Separates: True**

## Primes (controls = shuffled primes, independent sieve-matched, naive random)
- Layer 1 (residue mod 3): primes [0.0, 0.499688671804735, 0.500311328195265] vs naive [0.3340252790847864, 0.3330611680044285, 0.3329135529107851] — trivial coprimality
- Layer 2 (LO-S transition): real residual 7.287e-02 vs shuffled 6.049e-05 vs independent 5.366e-05
- separation ratio 1205× — **SEPARATES from controls (layer1 trivial + layer2 real LO-S correlation)**
- HONEST: known Lemke-Oliver–Soundararajan bias; necessary hygiene, NOT the RH positivity invariant.

## RH/Weil (controls = no-arch, fake Γ(s/3), shuffled primes)
- no_arch (P-R): min eig -5.0303 (indefinite→rejected)
- fake_Gamma(s/3): min eig -0.1082 (indefinite→rejected)
- shuffled_primes: min eig +0.0668 (stays PSD — NOT rejected by positivity)
- HONEST: positivity rejects wrong *completions* but is insensitive to prime *shuffling* (caught by the explicit-formula balance instead). Different nulls fail different tests.
