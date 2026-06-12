# Post draft: Derive Hardy–Littlewood by playing: the prime wheels

segment: visual-math | status: verified

## BLOCKED — do these before posting
- [ ] No figure attached yet (figure_idea: fig_wheels.png (the four-wheel derivation figure) or a short screen capture of the wheel lab verifying a user-typed pattern.)

## Lead post (figure attached: TODO)

```
Why are prime pairs at gap 6 exactly twice as common as twin primes? Three cells on a wheel answer it — and this page lets you derive the whole Hardy–Littlewood law yourself, verified by a live sieve in your browser.

twins predicted to 0.16% in-browser; every preset within Poisson noise vs live sieve counts, computed in the visitor's own browser — nothing pre-recorded; the page computes everything on load.

No fitted parameters. Verify it yourself:
https://github.com/vfd-org/closure-positivity-lab
```

## Thread (one reply per block)

**2/**
```
What goes in (everything, numbered — judge for yourself):
1. Residue wheels (finite cyclic screens) — the entire local mechanism
2. One multiplication: survival ratio per wheel, product over all wheels
3. The standard density integral (log-space, documented lower limit)
4. An in-browser sieve to 2×10⁷ as the referee
```

**3/**
```
How to kill it:
Type any offsets into explorables/residue-wheels.html: a pattern whose live count departs from the wheel product beyond Poisson noise kills the law on the spot, in the visitor's own browser.
```

**4/**
```
Run it (deps: a web browser):
  cd release-bundles/closure-positivity-lab
  open explorables/residue-wheels.html  (or explorables/index.html for the 5-scene tour)
```

**5/**
```
Background / independent data: https://en.wikipedia.org/wiki/First_Hardy%E2%80%93Littlewood_conjecture
```

**6/**
```
Full write-up: papers/how-the-primes-work.pdf — Prime Patterns in Five Computed Pictures (GO)
```

## Figure
TODO — idea: fig_wheels.png (the four-wheel derivation figure) or a short screen capture of the wheel lab verifying a user-typed pattern.
