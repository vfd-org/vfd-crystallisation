# Post draft: Icosian Brandt eigenvalues match elliptic-curve point counts over Q(√5)

segment: number-theorists | status: verified

## BLOCKED — do these before posting
- [ ] No figure attached yet (figure_idea: Table/strip plot of Brandt eigenvalue vs point-counted a_P per prime, in-sample vs out-of-sample shaded, all residuals zero.)

## Lead post (figure attached: TODO)

```
Quaternion arithmetic predicting point counts on an elliptic curve: 664 consecutive prime ideals, exact integers, zero fitting.

664/664 prime ideals matched, to norm 4999 (0 mismatches) vs Point counts for curve 31.1-a1 / Q(√5) (LMFDB-identified) — exact integer agreement.

No fitted parameters. Verify it yourself:
https://github.com/vfd-org/closure-positivity-lab
```

## Thread (one reply per block)

**2/**
```
What goes in (everything, numbered — judge for yourself):
1. The icosian order in the Hamilton quaternions over Q(√5) (a classical object)
2. The norm-31 prime of Z[φ] as the level
3. Brandt matrix construction via native Z[φ] lattice arithmetic (no Magma/SAGE)
4. Eichler mass formula and class number h=2 as structural gates
```

**3/**
```
How to kill it:
Any prime ideal (not dividing 31) where the cuspidal Brandt eigenvalue differs from the point-count a_P kills the claim. 664 ideals to norm 4999 are certified in out/provenance_664.json; extend the bound and re-run to stress it further.
```

**4/**
```
Run it (deps: numpy):
  cd release-bundles/closure-positivity-lab
  python3 run_lab.py   # provenance artifact: out/provenance_664.json
```

**5/**
```
Background / independent data: https://www.lmfdb.org/EllipticCurve/2.2.5.1/31.1/a/1
```

**6/**
```
Full write-up: papers/closure-diffraction-rh.pdf (reviewed, 2x GO)
```

## Figure
TODO — idea: Table/strip plot of Brandt eigenvalue vs point-counted a_P per prime, in-sample vs out-of-sample shaded, all residuals zero.
