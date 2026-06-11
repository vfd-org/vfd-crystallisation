# Post draft: 33 zeros of a degree-4 L-function built from the icosian order

segment: number-theorists | status: verified

## BLOCKED — do these before posting
- [ ] No figure attached yet (figure_idea: The diffraction figure from the paper (fig_diffraction.png): prime-wave interference intensity with the 33 independently-computed zeros overlaid on the fringes. The bundle also has anim_diffraction.mp4 for a video post.)

## Lead post (figure attached: TODO)

```
We built an L-function out of quaternion geometry, computed 33 of its zeros, then rebuilt its critical line from prime waves alone — the zeros landed on the fringes.

33 zeros to height 25; t₁ = 3.679; lfuncheckfeq ≈ −126 (log₂) vs functional-equation self-consistency + Sato–Tate (2nd moment 0.2515 vs 0.25) — two independent review passes, both GO; reviewer re-ran all numbers live.

No fitted parameters. Verify it yourself:
https://github.com/vfd-org/closure-positivity-lab
```

## Thread (one reply per block)

**2/**
```
What goes in (everything, numbered — judge for yourself):
1. The icosian (binary-icosahedral) maximal order over Q(√5) — a classical object
2. Brandt eigenvalues certified by two independent algorithms at 664/664 prime ideals to norm 4999
3. Modularity identification with elliptic curve 31.1-a1/Q(√5) (the licence, certified above)
4. PARI/GP lfun machinery for the zero computation (standard, reproducible)
```

**3/**
```
How to kill it:
Recompute in PARI/GP (out/_curve_zeros.gp) and find a zero off the critical line within the certified height, break the functional-equation self-consistency, or find one Brandt/point-count mismatch among the 664 certified prime ideals.
```

**4/**
```
Run it (deps: PARI/GP (zeros), numpy (lab)):
  cd release-bundles/closure-positivity-lab
  gp -q out/_curve_zeros.gp   # zeros; python3 run_lab.py for the lab table
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
TODO — idea: The diffraction figure from the paper (fig_diffraction.png): prime-wave interference intensity with the 33 independently-computed zeros overlaid on the fringes. The bundle also has anim_diffraction.mp4 for a video post.
