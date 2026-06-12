# Post draft: Ten prime phenomena, one instrument, one command

segment: number-theorists | status: verified

## BLOCKED — do these before posting
- [ ] No figure attached yet (figure_idea: The ledger as a scorecard graphic: ten rows, verdict column all PASS, the three theorem anchors and the boundary row visually distinguished.)

## Lead post (figure attached: TODO)

```
We ran ten famous prime phenomena through one instrument with pre-registered gates: 10/10 pass in ten seconds — including Leech's 26,861 and the maximal gap 220 reproduced exactly — and the one place the method fails is marked as a row, not hidden.

10/10 rows PASS (pre-registered gates) vs classical results + literature constants (Leech 1957, maximal-gap records, ST moments) — 0.003%–0.65% on statistical rows; deterministic anchors exact.

No fitted parameters. Verify it yourself:
https://github.com/vfd-org/closure-positivity-lab
```

## Thread (one reply per block)

**2/**
```
What goes in (everything, numbered — judge for yourself):
1. A prime sieve to 5×10⁷ and 1,983 PARI-computed zeta zeros — nothing else
2. Per-place admissibility counting (the local layer of every row)
3. Three theorem-grade anchor rows (Dirichlet, Chebotarev, Sato–Tate) calibrating the instrument
4. Gates set before the data were inspected; one boundary row (Mersenne) marking where the method fails
```

**3/**
```
How to kill it:
python3 -m lab.prime_ledger re-runs everything; any row drifting from its gate at larger sieve bounds kills that row, and a phenomenon that cannot be factored as (local product) × (zero-distribution statement) breaks the organising thesis — by the ledger's rules it would be published as a counterexample row.
```

**4/**
```
Run it (deps: numpy (PARI/GP only to regenerate the zeros)):
  cd release-bundles/closure-positivity-lab
  python3 -m lab.prime_ledger
```

**5/**
```
Background / independent data: https://en.wikipedia.org/wiki/Twin_prime
```

**6/**
```
Full write-up: papers/prime-phenomena-ledger.pdf (review-hardened, GO)
```

## Figure
TODO — idea: The ledger as a scorecard graphic: ten rows, verdict column all PASS, the three theorem anchors and the boundary row visually distinguished.
