# Post draft: α⁻¹ = 137 + π/87 from 600-cell eigenvalue structure

segment: physicists | status: verified

## BLOCKED — do these before posting
- [ ] No figure attached yet (figure_idea: The formula built visually from the spectrum (9+12+14+15 = 50 stacking into the expression), with a ppm-scale error bar vs CODATA.)

## Lead post (figure attached: TODO)

```
α⁻¹ = 137 + π/87, within 0.81 ppm — every ingredient an exact integer from one graph spectrum, zero fitted parameters.

137.03611 vs 137.035999 (CODATA) — 0.81 ppm.

No fitted parameters. Verify it yourself:
https://github.com/vfd-org/vfd-crystallisation
```

## Thread (one reply per block)

**2/**
```
What goes in (everything, numbered — judge for yourself):
1. The 600-cell graph Laplacian spectrum {0, 9, 12, 14, 15} (exact, verifiable)
2. 50 = sum of the non-zero eigenvalues (forced)
3. 87 from eigenvalue/multiplicity structure (derivation in script + Paper XXII)
4. No continuous parameters anywhere in the expression
```

**3/**
```
How to kill it:
The expression is rigid: if the derivation of 87 or 50 requires any choice not forced by the spectrum, or a future CODATA value moves by more than ~1 ppm, the claim dies. The derivation chain is enumerated step-by-step in the script.
```

**4/**
```
Run it (deps: numpy):
  cd papers/paper-xxii/scripts
  python3 run_alpha_derivation.py
```

**5/**
```
Background / independent data: https://vibrationalfielddynamics.org/articles/
```

**6/**
```
Full write-up: Paper XXII (Standard Model from 600-cell closure geometry)
```

## Figure
TODO — idea: The formula built visually from the spectrum (9+12+14+15 = 50 stacking into the expression), with a ppm-scale error bar vs CODATA.
