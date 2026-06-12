# The dimension redirect and the cosmology boundary — a synthesis

**Written 2026-06-03.** This document captures one connected line of reasoning that
ran across two apparently separate questions:

1. *Do the three "baby-RH" geometries we built (honeycomb H⁴, E10/H⁹, E10 slice),
   when compared, point a way forward to the missing RH object?*
2. *Does the VFD closure geometry reach into cosmology — dark matter, the CMB?*

Both questions converge on the **same lesson**, stated at the end. Scope tags used
throughout: **[VERIFIED]** computed/checked here or a cited theorem; **[NULL]** a
controlled negative result; **[OPEN]** the genuine frontier; **[INTERPRETIVE]** a
pattern held below the line, not load-bearing.

---

## Part I — The three baby-RH geometries, compared

We had built three objects on which a finite self-adjoint operator produces "zeros on
a line" (a *baby* Riemann Hypothesis):

| setup | dim d | field | critical line (d−1)/2 | spectrum = Riemann zeros? |
|---|---|---|---|---|
| {3,3,5,3} honeycomb | 4 | ℚ(√5) | 1.5 | no (its own zeros) |
| E10 lattice / H⁹ | 9 | ℤ | 4.0 | no (its own zeros) |
| E10 2D slice | ~2* | ℤ | 0.5 | no (sparse/trivial) |

\*the slice is a PCA projection, not a genuine H² arithmetic surface.

### What they share — and why that is a *negative* result

All three run on **one generic mechanism**: a self-adjoint operator (real spectrum)
composed with the Selberg spectral map `λ = s(d−1−s)`. Real eigenvalues then land
automatically on the line `Re(s) = (d−1)/2`. **[VERIFIED]** This fires on *any*
self-adjoint operator on *any* hyperbolic-type space.

Its universality is precisely the problem: **"self-adjoint ⟹ zeros on a line" is
free.** It cannot be the thing that singles out the Riemann object, because every
geometry has it. Building more such objects can never identify the right one — this
is why the geometric baby-RH program is **exhausted**.

### What *differs* — the one constructive signal

The critical line is **geometry-set** at `(d−1)/2`: 1.5 for the honeycomb (d=4), 4.0
for E10 (d=9). The Riemann line is `Re(s) = 1/2`, which forces

```
(d − 1)/2 = 1/2   ⟹   d = 2   exactly.
```

So **scaling the polytope/lattice *up* (E8 → E10 → E12 …) moves *away* from Riemann**,
onto ever-higher wrong lines. Riemann's line lives at the **bottom** of the dimension
ladder, d = 2 — not the top. This explains, in retrospect, why the E8→E10→E12 route
*felt* productive (each object passes baby-RH) but never closed (wrong dimension for
Riemann's line). **[VERIFIED — the dimension arithmetic]**

### Where d=2 + over-ℚ + ζ actually meet

The 2-dimensional hyperbolic object that is **arithmetic over ℚ** is the **modular
surface H²/SL(2,ℤ)**. Its Eisenstein/scattering theory has constant term

```
φ(s) = ξ(2s − 1) / ξ(2s),        ξ(s) = π^(−s/2) Γ(s/2) ζ(s)
```

which **literally contains the Riemann zeta**. The zeros of ζ sit in the surface's
**continuous (scattering) spectrum**. Numerically: φ(0.7) = −2.29, φ(1.3) = 4.03,
each built straight from ζ. **[VERIFIED]** Connes' adele-class space is the *adelic
completion* of exactly this surface.

### Verdict of Part I — redirect, not reveal

The comparison does **not** hand us the missing object, but it **redirects** the
search with two clean signals:

- the shared mechanism is generic → **more geometry won't help** **[VERIFIED/NULL]**;
- the dimension law + over-ℚ requirement says the Riemann object is the **d=2
  arithmetic surface SL(2,ℤ)\H² → Connes**, not bigger polytopes.

**But** the zeros are in the *continuous* spectrum, and proving them on the line is
still **Connes/Weil positivity = RH**. The three baby setups point *through* the
modular surface to the **same positivity wall** — now reached by the shortest, most
arithmetic road. **[OPEN]**

---

## Part II — Why "filter the primes to find the object" cannot work

A natural follow-on: if the primes look random but hide structure, can we *filter*
the noise to reveal the object?

- **Filtering reveals the ZEROS.** **[VERIFIED]** The sum `Σ_p (log p/√p) cos(t log p)`
  peaks at the imaginary parts of the zeros — we recovered 6 of the first 8
  (14.13, 21.02, 25.01, 30.42, 32.94, 43.33). This is the explicit-formula duality.
  But the zeros are *already known*; this is not the missing piece.
- **Filtering CANNOT reveal the OPERATOR.** **[VERIFIED]** Two structural reasons:
  1. *Circularity* — building `diag(γ₁, γ₂, …)` from the filtered zeros is self-
     adjoint with the right spectrum, but you fed in the zeros *as real numbers*,
     assuming the very thing RH asserts. Proves nothing.
  2. *Spectrum ≠ operator* — "you can't hear the shape of a drum" (Kac). Infinitely
     many operators (`U diag(γ) U†` for every unitary U) share any spectrum, so the
     filtered spectrum does not single out *the* object.

There is **no filter level** at which the operator emerges: the operator-vs-spectrum
gap is *structural*, not a matter of resolution. Filtering *is* the explicit formula —
it reaches the positivity wall, it does not cross it. **[OPEN]**

---

## Part III — The cosmology boundary (where the geometry does and doesn't reach)

A parallel excursion tested whether the VFD closure geometry reaches cosmology. The
discipline throughout: a **defined prediction + a null test**, never a metaphor.

### Dark energy — inside; dark matter — outside

- **Dark energy** is the programme's existing contact point (the Λ-dipole /
  hypersphere-cosmology, Ω_Λ and H₀ within ~0.5% of Planck). Legitimately owned.
- **Dark matter is real and outside the geometry.** **[VERIFIED/NULL]** It is
  non-baryonic (BBN + CMB peaks: Ω_b ≈ 0.049 vs Ω_dm ≈ 0.266 — baryons fall ~5.4×
  short), pressureless, cold, collisionless (Bullet Cluster). A σ-paired-rung
  hypothesis yields a **forced O(1) ratio but no forced mass** — the anchor is free,
  so the predicted mass spans 10⁶–10²⁸ eV (fittable to anything = the same "free
  anchor" failure seen elsewhere). Its structure (NFW halos, cosmic web) is
  gravitational and particle-agnostic — no E8-rung lock. Black holes are ~10⁻⁵ of the
  dark mass (cannot *be* it; early-SMBH seeding is a real but *separate* puzzle).

### The CMB acoustic peaks are *sound*, and *not* a quasicrystal

- **Sound, not free EM.** **[VERIFIED]** The peak position is a speedometer: light
  (c) would put the first peak at ℓ₁ ≈ 127; sound in a photon fluid (c/√3) puts it at
  220 — and 220 is observed. The early universe was a dense ionized plasma (not a
  vacuum); the "sound" is a pressure/density wave restored by photon pressure. The
  source is the inflationary perturbation spectrum (n_s = 0.965, ≠ 1 at >8σ).
- **Gaussian random field, not a quasicrystal.** **[VERIFIED/NULL]** The acoustic
  peaks live in the *power spectrum* (variance vs scale); the sky pattern has *random
  phases*. A quasicrystal has *sharp Bragg peaks in its diffraction*. A peaked power
  spectrum from a Gaussian field is the opposite of a quasicrystal — no Bragg peaks,
  no 5-fold order (Planck confirms Gaussianity + isotropy).

### 600-cell vs the CMB acoustic peaks — null

A direct correlation test of the 600-cell spectrum against the peaks
(220, 537, 810, 1120, 1444): **[NULL]**

- best 5-subset affine fit ≈ 4% vs a *fair* best-of-subset null — but
  **operator-dependent** (adjacency 60%, Laplacian 4%), and the fit has a **free
  scale + offset** while the peak positions are set by the cosmological sound horizon.
- the marginal ~4% is a generic "regular spectra are smooth (near-arithmetic)"
  artifact, not an acoustic lock — and it is the same fitted-anchor failure as the
  dark-matter mass. Simple rungs (16-cell, tesseract, 24-cell) have fewer than 5
  distinct modes — they cannot even produce a 5-peak structure. And the peaks are a
  *single-epoch snapshot* (frozen at recombination), not a ladder of geometries.

### The category resolution — relational precision ≠ spatial imprint

The honest answer to "the VFD math is precise, so why is the geometry invisible in the
CMB?": **[VERIFIED — principle]**

- The framework's precision lives in **relations** — ratios, constants, level
  structure (the proton radius, α, the cosmological ratios are *all* dimensionless
  relations, none a spatial pattern).
- A precise geometry is **invisible in a disordered (fluid) arrangement** — exactly
  as icosahedral symmetry is exact in a buckyball yet absent from a *gas* of
  buckyballs. Visibility depends on **arrangement** (ordered vs disordered), not on
  the precision of the geometry.
- The early universe was a **fluid** → disordered arrangement → Gaussian snapshot.
  This is *expected*, not "missing structure." The substrate is the **timeless
  algebra** governing relations; the matter pattern froze *random* at recombination.

The discipline that comes with it: **"it's hidden at small scale" cannot also count
as confirmation.** Either the geometry predicts a *specific* CMB signature (tested —
not there) or it predicts none (the CMB is *neutral*). Treating the absence as support
is the one move that would make the claim unfalsifiable.

---

## The through-line (Parts I–III converge here)

Across every angle — the baby-RH geometries, the primes, the CMB, the 600-cell —
**structure lives in the SPECTRUM; randomness lives in the ARRANGEMENT.**

| object | arrangement (looks random) | spectrum (the hidden structure) |
|---|---|---|
| CMB | random phases on the sky | acoustic peaks in the power spectrum |
| 600-cell in a fluid | featureless spatial map | exact Laplacian eigenvalues |
| primes | erratic prime gaps (the "voids") | the Riemann zeros |

This is the genuine "full circle" back to primes and the void: the void (the
random-arrangement face — cosmic voids, prime gaps) and the structure (the spectral
face) are **two faces of one object**, not opposites. **[VERIFIED — the shared
statistical signature]**

The boundary, held firmly: a shared *signature* is **not** a shared *object*. The CMB
power spectrum comes from fluid acoustics + inflation; the prime spectrum comes from
the ζ zeros. They belong to the same statistical family ("structure-in-spectrum") —
the rigorous bridge being random-matrix/GUE universality on the prime side — but they
are **distinct systems with distinct mechanisms**. Claiming one *generates* the other
is unfalsifiable over-reach. The unification is the **[INTERPRETIVE]** human seat; the
load-bearing math stays separate and intact.

---

## One-paragraph summary

The three baby-RH geometries share a *generic* self-adjoint→on-line mechanism (a
negative result: it can't single out the Riemann object), but comparing them yields a
constructive **dimension redirect**: Riemann's critical line `Re(s)=1/2` corresponds to
`d=2`, so the object is the **arithmetic modular surface SL(2,ℤ)\H² → Connes adele-class
space**, not bigger polytopes — and the open step there is **Weil positivity = RH**.
Filtering the primes recovers the zeros (explicit formula) but never the operator
(circularity + spectrum≠operator). In cosmology, the geometry owns dark **energy** but
not dark **matter** (real, non-baryonic, fittable-not-forced under VFD), the CMB peaks
are genuine **sound** (c/√3) in a Gaussian field (not a quasicrystal), and the 600-cell
shows **no** non-trivial correlation with them. The resolution of "precise math,
invisible geometry" is that precision lives in **relations**, which are spatially
**invisible in a fluid** — so the Gaussian CMB is *expected*, not missing structure.
The through-line across all of it: **structure is in the spectrum, randomness in the
arrangement** — the honest "full circle" to the primes and the void, held as pattern,
not as a claim that one *is* the other.
