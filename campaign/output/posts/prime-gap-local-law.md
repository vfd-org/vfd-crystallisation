# Post draft: Prime-gap abundances from an all-places product (and twins to 0.003%)

segment: number-theorists | status: verified

## BLOCKED — do these before posting
- [ ] No figure attached yet (figure_idea: Bar chart: measured abundance ratio per gap (2..210) with the local-product prediction overlaid as markers — eight bars, eight bullseyes. Inset: twin count vs HL curve converging (1.0038 → 1.0017 → 0.99997).)

## Lead post (figure attached: TODO)

```
Did you know prime pairs at gap 6 are exactly twice as common as twin primes? One product over the primes dividing the gap predicts every ratio — verified to 0.25% across eight gaps, and the twin count itself to 0.003%.

239,101 twins counted vs 239,107 predicted; every gap ratio within 0.25% vs Hardy–Littlewood singular series (1923) — 0.003% (twins); ≤0.25% (gap ratios incl. 210 → 3.1994 vs 16/5).

No fitted parameters. Verify it yourself:
https://github.com/vfd-org/closure-positivity-lab
```

## Thread (one reply per block)

**2/**
```
What goes in (everything, numbered — judge for yourself):
1. A prime sieve to 5×10⁷ (nothing else — no fitting surface exists)
2. Per-place admissibility counting: each odd prime p dividing the gap contributes (p−1)/(p−2)
3. Hardy–Littlewood constant C2 as the convergent all-places product
4. Theorem anchors run alongside: Dirichlet equidistribution + Q(√5) splitting, both PASS
```

**3/**
```
How to kill it:
Run python3 -m lab.prime_ledger with a larger X: any gap whose abundance drifts from its local product, or a twin count diverging from the HL integral, kills the row. Every gate and artifact is in out/prime_ledger.json.
```

**4/**
```
Run it (deps: numpy):
  cd release-bundles/closure-positivity-lab
  python3 -m lab.prime_ledger
```

**5/**
```
Background / independent data: https://en.wikipedia.org/wiki/Twin_prime#First_Hardy%E2%80%93Littlewood_conjecture
```

**6/**
```
Full write-up: Prime Phenomena Ledger (WO-VFD-PRIME-LEDGER-001, paper in Phase C)
```

## Figure
TODO — idea: Bar chart: measured abundance ratio per gap (2..210) with the local-product prediction overlaid as markers — eight bars, eight bullseyes. Inset: twin count vs HL curve converging (1.0038 → 1.0017 → 0.99997).
