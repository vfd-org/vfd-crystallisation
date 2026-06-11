# Derivation: Caspar–Klug T-numbers from a Face-Level Cascade Operator

**WO:** WO-BIOLOGY-RUNG-001-CAPSID
**Date opened:** 2026-04-23
**Status:** Round 1 post-codex-review, revised

This document establishes, at the **face level** of the icosahedral
substrate: *the full Caspar–Klug T-number sequence is the spectrum
of a single operator `𝒯_casc` on the Eisenstein lattice `ℤ[ω]`,
uniquely picked out up to positive scale by the hexagonal lattice's
own 6-fold rotation symmetry.* The accompanying `A_5` action
permutes the 20 icosahedral faces but does not by itself fix the
face-level operator; the two symmetries are kept distinct.

The derivation resolves the T=5 ambiguity in `cascade-bio.md §B3`,
replaces the current partial "small-T ↔ A_5 irrep dims" match with
a structurally honest statement, and identifies the principal open
question of the programme — whether `𝒯_casc` is the face-level
residue of a cell-level Paper XXXII closure construction — as
explicit open problem [C.2].

Every new mathematical object introduced here is catalogued in
`math-catalogue.md` with prefix D/L/T/C/R/N. Cross-references of the
form `[D.1]` etc. resolve to entries there.

---

## §1. Preliminaries

### 1.1 Caspar–Klug recap

The Caspar–Klug (1962) classification assigns each icosahedral viral
capsid a triangulation number `T = h² + hk + k²` with `h, k` non-
negative integers, not both zero. A capsid with triangulation number
`T` has `20T` triangular facets arranged with icosahedral symmetry,
obtained by subdividing each face of the underlying icosahedron along
an Eisenstein-lattice vector `h + kω` where `ω = e^{iπ/3}` is a
**primitive sixth root of unity** (so `ω² = ω − 1`, and `N(h + kω) =
(h + kω)(h + kω̄) = h² + hk + k²` as stated). This is the convention
used **internally throughout this document**.

**Notation note vs. upstream.** `cascade-bio.md §B3.1` writes
`ω = e^{2πi/3}` (primitive *third* root of unity), and records the
norm formula as `T(h, k) = h² + hk + k²`. With the third-root
convention, the literal Eisenstein norm is `h² − hk + k²`, so
equating it to `h² + hk + k²` requires the basis change `k ↦ −k`
(equivalently, using the alternative generator `ρ := 1 + ω = −ω̄`,
which is itself a primitive sixth root). The two conventions attain
the same Loeschian set of values. To avoid the mismatch between the
stated generator and the stated formula, this document adopts the
sixth-root convention directly; `cascade-bio.md §B3.1` should be
normalised separately (downstream edit on the bio doc, not in scope
for this WO).

The values attained by the form `N(h, k) = h² + hk + k²` over
`(h, k) ∈ ℤ² \ {(0, 0)}` are the **Loeschian numbers** (OEIS A003136):

> 1, 3, 4, 7, 9, 12, 13, 16, 19, 21, 25, 27, 28, 31, 36, 37, …

These are exactly the integers `n ≥ 1` such that every prime `p ≡ 2
(mod 3)` appearing in the factorisation of `n` does so with even
exponent. In particular `2, 5, 6, 8, 10, 11, …` are **not** Loeschian,
so no capsid has `T = 2` or `T = 5`.

### 1.2 The icosahedral rotation group

`I ≅ A_5` acts on the 20 faces of the icosahedron with stabiliser
`C_3` (3-fold rotation through each face center). The character of
this permutation representation on the class table of `A_5` is

  `χ_perm(e)   = 20`
  `χ_perm(3A)  = 2`     (each 3-cycle fixes the two faces on its axis)
  `χ_perm(5A)  = 0`
  `χ_perm(5B)  = 0`
  `χ_perm(2A)  = 0`

which decomposes as

  `π_20 = 𝟏 ⊕ 𝟑 ⊕ 𝟑' ⊕ 𝟒^{⊕2} ⊕ 𝟓`

with multiplicities `(1, 1, 1, 2, 1)` on the irreducibles of
dimensions `(1, 3, 3, 4, 5)`. Total dimension `1 + 3 + 3 + 8 + 5 = 20`.

This decomposition is logged as [L.0].

### 1.3 The cascade substrate

Per `cascade-bio.md §3.1`, biology sits at the **cell (3-volume)
level** of the 600-cell: 600 tetrahedral cells. The upstream doc
*conjectures* a 15-fibre Hopf cell-fibration with 40 cells per
fibre (`cascade-bio.md §3.2`, `40 = 8 · 5`); this is labelled as a
"conjectured" structure / "structural candidate" there, not a
proved partition, and we mirror that status here.

Separately and solidly: the binary icosahedral group `2I`, of order
120, acts as the vertex set of the 600-cell, and its quotient `I =
2I / {±1} ≅ A_5`, of order 60, is the rotation group acting on the
antipodal pairs of vertices. This part is proved in `cascade-bio.md
§2.1–2.3`.

The face-level derivation below does **not** depend on the
conjectured Hopf fibration; the 600-cell → face-level reduction
required for open problem [C.2] would, and this dependency is
flagged there.

---

## §2. The Face-Level Icosahedral Eisenstein Substrate

### Definition [D.1] — Face-level Eisenstein substrate

The **face-level icosahedral Eisenstein substrate** is the pair

  `𝕊 := (ℤ[ω], A_5 ↷ 𝓕₂₀)`

where `ℤ[ω]` is the ring of Eisenstein integers viewed as the
hexagonal lattice on a single icosahedral face (basis `{1, ω}`,
`ω = e^{iπ/3}`; see §5 for the choice of primitive-sixth-root
convention that makes `N(h + kω) = h² + hk + k²`), and `𝓕₂₀` is the
20-element set of icosahedral faces carrying the `A_5` permutation
action `π_20` from §1.2.

A Caspar–Klug subdivision is a single choice of Eisenstein vector
`v = h + kω ∈ ℤ[ω] \ {0}` replicated coherently across all 20 faces
— i.e. the same `(h, k)` per face, up to the local unit-ambiguity
on each face. (A formal `A_5`-equivariance statement would require
a target action on an oriented subdivision bundle; we do not
construct that here, and it is not needed for the face-level
results below.) Two subdivisions are equivalent if they differ by
a unit of `ℤ[ω]` (the six units `{1, ω, ω², −1, −ω, −ω²}` form
`C_6` under multiplication and realise the six-fold rotation
symmetry of the hexagonal lattice at each face center).

**The two symmetries in play, kept distinct.** Two separate symmetry
groups act on `𝕊`; this derivation treats them as independent inputs
and does **not** claim either is a subgroup of the other:

1. The **icosahedral group** `I ≅ A_5` acts on `𝓕₂₀` by permuting
   faces. The stabiliser of a single face under `I` is `C_3`
   (3-fold rotation about the face-center axis); the full
   face-stabiliser under the extended icosahedral symmetry group
   `I_h = I × {±1}` of order 120 is `D_3` (dihedral of order 6).
   Neither is `C_6`.

2. The **hexagonal-lattice rotation group** `C_6` acts on `ℤ[ω]`
   by multiplication by Eisenstein units. This is an intrinsic
   symmetry of the hexagonal lattice, **independent of** the
   icosahedral group action. The `C_6` arises because the
   hexagonal lattice has 6-fold rotational symmetry as a planar
   lattice in its own right, not because any face stabiliser has
   order 6.

The face-level operator introduced in §3 uses (2) for its
uniqueness statement. The icosahedral (1) is present only to
explain why the same operator applies coherently across all 20
faces. Any statement linking `𝒯_casc` to the full 600-cell closure
machinery is held to §6 [C.2] and is not asserted at this substrate
level.

**Provenance.** Extends `cascade-bio.md §B1`/§3.1 (cell-level
biology) by naming the face-level Eisenstein structure explicitly
and attaching the `A_5` permutation rep `π_20`. The hexagonal-
lattice-on-faces picture is classical Caspar–Klug; the cascade-
specific content in this document is the uniqueness result in [L.3]
and the honest relation between the face-level and cell-level scopes
([T.1] vs. [C.2]).

### Lemma [L.0] — Decomposition of the A_5 face representation

`π_20 = 𝟏 ⊕ 𝟑 ⊕ 𝟑' ⊕ 𝟒^{⊕2} ⊕ 𝟓`, with irreps labelled by dimension
and (for the two 3-dim irreps) by the Galois pair `(3, 3')` that swap
under `φ ↔ 1 - φ`.

**Proof.** From §1.2 the permutation character is `χ_perm = (20, 2,
0, 0, 0)` on the conjugacy classes `(e, 3A, 5A, 5B, 2A)` with sizes
`(1, 20, 12, 12, 15)`. Using the standard `A_5` character table (see
e.g. ATLAS of Finite Groups) and the inner-product formula
`⟨χ_perm, χ_ρ⟩ = (1/|G|) Σ_c |c| χ_perm(c) χ_ρ(c)`, direct
computation gives multiplicities `(1, 1, 1, 2, 1)` on the irreps
of dimensions `(1, 3, 3, 4, 5)`; total dimension `1 + 3 + 3 + 8 +
5 = 20` confirms completeness of the decomposition. □

### Remark [R.0] — 2I versus A_5

The cell-level substrate admits two natural symmetry groups:

- `2I ⊂ SU(2)`, order 120, with irreps including the spin-½ rep (not
  seen by a single face but relevant to chirality across paired
  antipodal faces).
- `A_5 = I = 2I / {±1}`, order 60, the actual face-permutation group.

Throughout this derivation we work with `A_5` as the acting group on
`𝓕₂₀`. The `2I` double-cover becomes relevant in §6 (chirality
weighting).

---

## §3. The Cascade T-Operator

### Definition [D.2] — Cascade T-operator (face-level)

The **face-level cascade T-operator** is the map

  `𝒯_casc : ℤ[ω] → ℤ_{≥0}`,  `𝒯_casc(z) := z · z̄ = |z|²`

sending an Eisenstein integer `z = h + kω` to its norm
`N(z) = h² + hk + k²`.

The domain `ℤ[ω]` is the hexagonal lattice on a single icosahedral
face (see [D.1]). `𝒯_casc` is invariant under multiplication by the
six Eisenstein units (the lattice-level `C_6` action); it is
scalar-valued and therefore transforms trivially under any group
action, including `A_5`. No further equivariance claim is made.

**Provenance.** The map `z ↦ |z|²` is the Eisenstein norm, classical.
The cascade-specific content is the uniqueness claim in [L.3] below
— that `𝒯_casc` is, up to positive scale, **the** positive-definite
`C_6`-invariant quadratic form on `ℤ[ω]` — which picks it out among
candidate face-level quadratic operators by the hexagonal-lattice's
own rotational symmetry.

### Lemma [L.1] — Spectrum = Loeschian numbers

  `spec(𝒯_casc) := 𝒯_casc(ℤ[ω] \ {0}) = {Loeschian numbers}`.

**Proof.** By definition, `𝒯_casc(h + kω) = h² + hk + k²` with
`(h, k) ∈ ℤ² \ {(0, 0)}`. The set of such values is the image of
the integer norm form on `ℤ[ω]`, which is the classical Loeschian
set (OEIS A003136). □

### Lemma [L.3] — Uniqueness of 𝒯_casc under C_6 symmetry

Let `Q : ℤ[ω] → ℝ_{≥0}` be any positive-definite quadratic form on
`ℤ[ω]` that extends to a `C_6`-invariant quadratic form on
`ℝ² ≅ ℂ`, where `C_6` acts by multiplication by the six Eisenstein
units. Then `Q = c · 𝒯_casc` for some `c > 0`.

**Proof.** A positive-definite quadratic form on `ℝ²` is given by
`Q(x) = x^⊤ M x` for a symmetric positive-definite `2 × 2` matrix
`M`. `C_6`-invariance requires `R^⊤ M R = M` for every rotation
`R ∈ C_6`; it is enough that this holds for a generator, say
`R = R_{π/3}` (rotation by `π/3`).

A standard calculation: write `M = (a, b; b, c)`. Imposing
`R_{π/3}^⊤ M R_{π/3} = M` for `R_{π/3} = (1/2, -√3/2; √3/2, 1/2)`
and comparing entries yields

  `a = c`  and  `b = 0`.

(Equivalently: extend `M` to a complex-linear operator on `ℂ`; then
`R_{π/3}` has eigenvalues `e^{±iπ/3}` which are not real, so the
centraliser of `R_{π/3}` in `Sym²(ℝ²)` is one-dimensional and
consists of scalar multiples of the identity quadratic form.)

Hence `M = a · I₂` and `Q(x) = a |x|²`. Restricting to `z ∈ ℤ[ω]`
gives `Q(z) = a · (z · z̄) = a · 𝒯_casc(z)`. Setting `c := a > 0`
completes the proof. □

**Significance.** [L.3] is the cascade-specific content at the
face level. It says: *any positive-definite quadratic closure form
on the hexagonal face-lattice that respects the lattice's own 6-fold
rotational symmetry is a positive scalar multiple of the Eisenstein
norm*. This pins down the face-level operator without arbitrary
choices; the corresponding statement at the full cell-level 600-cell
remains open and is stated as [C.2].

### Theorem [T.1] — Face-level T-number sequence from one operator

There exists a face-level operator `𝒯_casc` on the Eisenstein
substrate `ℤ[ω]` (per [D.1]/[D.2]), uniquely determined up to
positive scale by local hexagonal-lattice `C_6` symmetry ([L.3]),
whose spectrum is exactly the sequence of Caspar–Klug T-numbers
([L.1]).

**Proof.** Take `𝒯_casc` as in [D.2]; apply [L.1] (spectrum =
Loeschians) and [L.3] (uniqueness up to scale under the stated
symmetry). □

**Scope and what remains open.** [T.1] is a **face-level** statement:
the Caspar–Klug T-number set is realised as the spectrum of a single
quadratic form on the hexagonal face-lattice, and that form is
uniquely determined up to scale by its own local rotational
symmetry. Whether `𝒯_casc` is the correct face-level residue of a
600-cell closure functional — i.e. whether the face-level operator
is actually induced from the cascade-level Paper XXXII machinery
via a principled projection — is the content of [C.2] and is **not
claimed here**.

**Relation to open item in `cascade-bio.md §B3`.** The last row of
§B3.4 (line 320) lists "Full derivation of all T-numbers from one
cascade operator" as `✗ open`. [T.1] provides a face-level
resolution of this item: the full CK T-number sequence is the
spectrum of a single face-level cascade operator. The stronger
version — that this operator is the restriction of a Paper XXXII
600-cell closure functional — is held open as [C.2].

---

## §4. Settling the T = 5 Question

### Remark [R.1] — Why the current doc's T=5 entry is misleading

`cascade-bio.md §B3.2` (table at line 283) lists

  | T | Classical | Cascade identification |
  |---|---|---|
  | 5 | (100-facet) | A_5 5-dim irrep ✓ |

This entry is **not** supported by either of the following two
mathematical facts (empirical capsid-count claims are held to the
VIPERdb comparison [N.2] and not asserted here):

1. The classical Caspar–Klug sequence. `5` is not a Loeschian
   number: no `(h, k) ∈ ℤ²` satisfies `h² + hk + k² = 5`, because
   `5` is inert in `ℤ[ω]` (equivalently, `5 ≡ 2 (mod 3)` with odd
   exponent in the factorisation of 5).
2. The Eisenstein-norm spectrum of [D.2]. By [L.1], `5 ∉
   spec(𝒯_casc)`.

What the `A_5` 5-dim irrep *is* is the five-dimensional summand of
the permutation rep `π_20` from [L.0]. That summand has dimension 5
because `A_5` has a 5-dim irrep; it is **not** an Eisenstein norm
value and does not predict a `T = 5` capsid. Whether empirical
capsid counts reinforce this — i.e. that no observed capsid has
`T = 5` — is a separate question, deferred to [N.2] (the
comparison artefact has not been produced yet; the claim here
rests on the mathematical argument alone).

### Lemma [L.2] — The honest small-T / A_5 match

`A_5` has **five irreducible representations** with **four distinct
dimensions** — `1`, `3`, `4`, `5`; the dimension `3` occurs twice,
for a Galois-conjugate pair usually written `3` and `3'` (swapped
under `φ ↔ 1 − φ`). The Loeschian numbers less than or equal to
`5` are `{1, 3, 4}`. The overlap is

  `{distinct A_5 irrep dims} ∩ {Loeschians ≤ 5} = {1, 3, 4}`.

This is the precise content of the "small-T ↔ A_5 irrep dim" match:
**three of the four distinct `A_5` irrep dimensions coincide with
small Loeschian numbers** (namely `1`, `3`, `4`). The fourth
distinct dimension, `5`, is not a Loeschian value; and the
additional `3'` irrep in the representation count carries the same
dimension as `3` and so contributes no new T-value. These non-
Loeschian labels are representation-theoretic and do not predict
`T = 5` or a second `T = 3` capsid.

**Fix to existing doc.** `cascade-bio.md §B3.2`'s table should be
amended per [R.1]/[L.2] when the cascade-bio.md is next revised
(not rewritten here; noted for the downstream editor).

### Remark [R.2] — The 3' Galois conjugate as an open prediction

`A_5`'s two 3-dimensional irreducibles form a Galois-conjugate pair
swapped under `φ ↔ 1 − φ` (standard character-theoretic fact; see
the standard `A_5` character table, e.g. the ATLAS of Finite
Groups). The `3'` irrep has the same dimension as `3` (and so
predicts no new T-value), but it carries different character values
on the two 5-cycle classes. A speculative conjecture [C.4] below
asks whether this Galois pairing manifests as a secondary structural
feature of `T = 3` capsids (e.g. a discrete bistability of coat-
protein orientation related to the two representation choices). No
claim is made here that `cascade-bio.md §B3.2` itself flags this
pair: the Galois structure is standard `A_5` character theory,
imported into this document, not quoted from the upstream bio doc.

---

## §5. Closure Weighting and Chirality

### Definition [D.3] — Orbit multiplicity at T

**Notation.** Throughout this section `ω` denotes the primitive
sixth root of unity `ω = e^{iπ/3}`, following the Caspar–Klug /
`cascade-bio.md §B3.1` convention under which `N(h + kω) = h² + hk +
k²`. `ω` satisfies `ω² = ω - 1`, so `ω` acts on `ℤ² ≅ ℤ[ω]` by
`(h, k) ↦ (-k, h + k)`. The six units of `ℤ[ω]` are
`{1, ω, ω², -1, -ω, -ω²}` and they form a cyclic group `C_6` under
multiplication. (This is the intrinsic 6-fold rotational symmetry
of the face lattice itself — not the icosahedral face stabiliser,
which is only 3-fold — and it does **not** include a reflection,
because the ambient icosahedral rotation group `I ≅ A_5` is a
proper rotation group with no mirror.)

For each Loeschian integer `T`, define

  `μ(T) := #{ C_6-orbits of (h, k) ∈ ℤ² \ {0} with h² + hk + k² = T }`

where `C_6` acts on `ℤ[ω]` by multiplication by the six Eisenstein
units.

Small values (verified by direct enumeration; sim output catalogued
as [N.1]):

  `μ(1) = μ(3) = μ(4) = μ(9) = μ(12) = μ(16) = μ(25) = μ(27) = 1`
  `μ(7) = μ(13) = μ(19) = μ(21) = μ(28) = μ(31) = μ(37) = μ(39) = 2`
  `μ(49) = 3`    (representatives `(7, 0)`, `(5, 3)`, `(3, 5)`)
  `μ(91) = 4`    (representatives `(1, 9), (5, 6), (6, 5), (9, 1)`;
                  emerges from `91 = 7 × 13`, both chiral primes)

General structure (heuristic / explanatory, not a proved
classification theorem; the rigorous classification of `μ(T)` is
Eisenstein-arithmetic and standard, with the sim authoritative
for specific values): `μ(T)` counts the distinct `C_6`-orbits at
`T`. An individual norm-factorisation contributes:

- **+1 orbit** when the canonical wedge representative lies on a
  hexagonal-lattice reflection axis — either the real axis
  (`k = 0`) or the `h = k` diagonal. Examples: `(1, 0)` for
  `T = 1`, `(2, 0)` for `T = 4`, `(1, 1)` for `T = 3`, `(2, 2)`
  for `T = 12`, `(3, 3)` for `T = 27`. Such an orbit is its own
  mirror image under the `h ↔ k` reflection, so laevo and dextro
  coincide — *achiral*.
- **+2 orbits** when the canonical representative `(h, k)` has
  `h, k > 0` and `h ≠ k` — a chiral pair: `(h, k)` contributes
  its own `C_6`-orbit plus the distinct mirror orbit containing
  `(k, h)`, since `(k, h)` is **not** in the `C_6`-orbit of
  `(h, k)` when reflections are excluded. Examples: `T = 7` with
  `{(1, 2), (2, 1)}`, `T = 13` with `{(1, 3), (3, 1)}`.

For `T` with multiple independent norm-factorisations, each
factorisation contributes its own orbit structure, summing to
`μ(T) ≥ 3`. Examples: `T = 49 = 7²` yields `μ = 3` (one axis
orbit from `(7, 0)` plus one chiral pair from `7 × 7`); `T = 91
= 7 × 13` yields `μ = 4` (two chiral pairs, one from each prime
factor's contribution). The general rule is not "μ = 2 whenever
`h, k > 0` distinct" — that statement overstates the pattern and
misses the multi-factorisation cases. The sim enumeration at
`data/wo1_prediction.csv` is authoritative for specific `T`
values.

**Why C_6 and not D_6.** The full hexagonal-lattice automorphism
group is `D_6` (twelve elements = six rotations + six
reflections). Under `D_6`, the reflection `(h, k) ↦ (k, h)` glues
laevo and dextro into a single orbit, so `μ_{D_6}(7) = 1`. But `2I`
and `A_5` are **proper** rotation groups — they contain no
reflections. The physically meaningful group for biology is `C_6`
(rotations only), and chirality is therefore preserved as distinct
`C_6`-orbit content.

**Provenance.** New to this WO. `μ` is elementary combinatorics on
`ℤ[ω]`; named and catalogued here because [C.3] assigns it
biological meaning (chirality asymmetry).

### Conjecture [C.1] — Closure-preference weighting

Let `Z(T)` denote the closure-preference weight the cascade assigns
to a T-number capsid at equilibrium. Then

  `Z(T) ∝ μ(T) · exp( -β · c(T) )`

where `c(T)` is a cascade-level assembly cost (monotonic non-
decreasing in `T`, reflecting that larger capsids require more
protein subunits) and `β` is an inverse-temperature / selection
constant of order unity in natural cascade units.

**Status.** Conjectural. The multiplicity factor `μ(T)` is forced
by [D.3]; the exponential assembly-cost factor is a modelling
assumption motivated by biological capsid-economy arguments and
will be tested as part of [N.2] (VIPERdb comparison). If the
exponential ansatz fails empirically, `c(T)` will be left as an
open function to be fitted.

### Conjecture [C.3] — Chirality asymmetry from 2I handedness

For chiral T-numbers (those with `μ(T) = 2`, e.g. `T ∈ {7, 13, 19,
21, 28, …}`), the cascade predicts a small but nonzero empirical
asymmetry between laevo and dextro capsids:

  `(N_laevo - N_dextro) / (N_laevo + N_dextro) ≠ 0`,

with sign determined by the handedness of the ambient biological
chirality regime (L-amino-acid world). The cascade does not predict
the magnitude of this asymmetry from first principles yet; the
qualitative prediction is *nonzero* with *sign from ambient
chirality*.

**Provenance.** Extends `cascade-bio.md §2.7` (2I intrinsic
handedness → L-amino-acid preference, listed as pending B5) from the
amino-acid scale to the capsid scale.

**Empirical content.** If a VIPERdb-style dataset tagging capsids
by chirality can be assembled (not yet obtained — see §7 planned
hypothesis stack), the 50/50 null is decisively falsifiable with
moderate sample size. This repo does not currently hold such a
dataset; extracting chirality from VIPERdb entries is part of the
open work under [N.2]. The present document makes no empirical
claim.

---

## §6. Relation to the Paper XXXII Closure Functional

### Open problem [C.2] — Does 𝒯_casc descend from the Paper XXXII closure functional?

This section frankly identifies what would be needed to upgrade the
face-level result of §3 into a genuine cell-level statement. It is
**not** a worked conjecture — several of the objects used below are
not yet defined in this document, and the correct upstream citation
is only established here in outline form.

**Upstream citations (corrected).** Paper XXXII contains two
distinct uniqueness theorems, which this derivation previously
conflated:

- `papers/paper-xxxii/paper-xxxii.tex §3` (Section "The 600-Cell
  from the ADE Classification", Theorem `thm:600cell` around line
  237): under structural assumptions `(H1)` configuration space
  `S³ ≅ SU(2)`, `(H2)` closure symmetry a finite subgroup `G ≤
  SU(2)`, `(H3)` nearest-neighbour angular separation `π/5`, and
  `(H4)` `G` maximal among such subgroups, the unique choice is
  `G = 2I`, whose 120 elements form the 600-cell vertex set.

- `papers/paper-xxxii/paper-xxxii.tex §4` (Section "The Closure
  Functional: Uniqueness", Theorem F around line 363): within the
  class `𝒞` of continuous regularised soft-min functionals
  `F_ε^V(x) = opt_p [ Σᵢ pᵢ |x − vᵢ|² / 2 + ε² R(p) ]` (with
  permutation-symmetric `R` as part of the class definition),
  axioms **A1 continuity, A2 sharp limit, A3 extensivity** under
  independent composition force `F(x) = −ε² log Σᵢ exp(−|x − vᵢ|² /
  (2 ε²))`, i.e. the log-sum-exp form with Gibbs minimiser.

These are the two upstream theorems. The face-level operator
`𝒯_casc` introduced here is **not** derived from either in this
document.

**Important clarification about Paper XXXII's F.** Paper XXXII's
closure functional is **point-wise on the manifold**:
`F_ε^V : M → ℝ` takes `x ∈ S³` and returns a real closure distance;
axioms A1–A3 fix it as the log-sum-exp form (§4 Theorem F). It is
**not** a field-theoretic functional on `C^∞(S³, 𝒜)` for any
target bundle `𝒜`. The field-theoretic / density-level closure
form `F[Φ] = ∫ (α R + β E − γ Q) dV` lives separately in
`cascade-derivation/cascade-foundations.md §F2`. Earlier drafts of
this document conflated the two.

The open problem below therefore splits into two sub-problems
depending on which upstream object one is trying to face-level-
restrict: **(C.2-a)** the point-wise `F_ε^V : S³ → ℝ` from Paper
XXXII §4; or **(C.2-b)** the density-level `F[Φ] = ∫ L dV` from
cascade-foundations §F2. The two are related but not identical,
and the face-level-restriction argument is different for each.

**What the open problem asks.** Fix interpretation (C.2-b), the
field-level F2 density, as the more natural candidate (since
quadratic-on-slice only makes sense for a field-theoretic object,
not a point-wise real-valued function on S³). The four steps of
the plan are:

1. Identify a **subspace of 2I-invariant configurations** — a
   `2I`-fixed-point subspace of cascade-foundations.md §F2's field
   configuration space on which `F[Φ]` restricts coherently. The
   existence and a precise description of this subspace require a
   re-read of the F2 setup and are not shown here.

2. Construct a **face-level projection** from this `2I`-invariant
   subspace to `ℤ[ω]`-valued face data: intuitively, each of the
   20 icosahedral faces inherits an `(h, k)`-subdivision parameter,
   and the projection records this parameter per face. A natural
   candidate averaging is the **conjectured** Hopf cell-fibre
   partition (`cascade-bio.md §3.2`, labelled conjectural there;
   15 candidate fibres × 40 cells). Because that partition is
   itself not proved in the upstream document, any face-level
   projection built on it inherits conjectural status until the
   fibration is established. Alternative averaging schemes may
   exist — the 15-fibre Hopf structure is one candidate, not the
   only one.

3. Show that `F[Φ]` restricted along this projection descends to
   a positive-definite quadratic form on `ℤ[ω]`. F2 gives
   `F[Φ] = ∫ (α R + β E − γ Q) dV`, a quadratic density on field
   components; but quadratic density does not automatically yield
   quadratic-on-slice after averaging. This step is the real
   technical obstacle.

4. Apply [L.3] to identify the projected form with `c · 𝒯_casc`
   for some `c > 0`. This is the only step this document
   establishes; it is contingent on 1–3.

The interpretation (C.2-a) with the point-wise F of Paper XXXII §4
is more subtle: a point-wise function `S³ → ℝ` cannot directly
define a quadratic form on `ℤ[ω]`, so (C.2-a) would first need a
field-theoretic lift of Paper XXXII's F — at which point it becomes
essentially (C.2-b).

**What is claimed at present.** Nothing beyond steps 1–4 being the
remaining work under interpretation (C.2-b), and (C.2-a) reducing
to (C.2-b) after a lift. This is an *open problem*, not a
conjecture in the strong sense.

**Status.** Open problem with a four-step plan of attack under
interpretation (C.2-b). Demoted from the earlier "Conjecture"
status on codex-round-0 feedback, with the Paper XXXII attribution
tightened on round 1.

**Additional argument context (for completeness, now labelled as what it is):**

1. The `2I`-invariant subspace of 600-cell fields is spanned (by
   Frobenius reciprocity) by the irreducible components of the
   regular representation of `2I` fixed under the `2I`-diagonal.
   Restricted to a single cell-fibre, these span the face-level
   Eisenstein data. **Caveat:** this uses a Frobenius / induction
   formalism appropriate to finite-dimensional representations of
   `2I`; the application to continuous `C^∞(S³, 𝒜)` data requires
   identifying the correct `𝒜` and checking that `2I`-invariance
   is compatible with the soft-min extensivity axiom A3 of Paper
   XXXII Theorem F. Not shown here.
2. Step 2 previously read "`F` is positive-definite and quadratic
   on its free parameters (Paper XXXII F2)". This attribution was
   incorrect in the earlier draft: `F2` in the cascade programme
   is the closure-functional-form theorem `F = α R + β E − γ Q`
   of `papers/cascade-derivation/cascade-foundations.md §F2`,
   which gives a specific *density* decomposition; it is **not**
   a direct guarantee that Paper XXXII's `F` is quadratic on an
   arbitrary face-level slice. The quadratic-on-slice property
   has to be proved, not quoted.
3. If 1–2 yield a positive-definite quadratic form on `ℤ[ω]`,
   and if that form is `C_6`-invariant (which requires the
   hexagonal-lattice rotation symmetry to survive the projection),
   [L.3] then identifies it as `c · 𝒯_casc`.

The earlier draft advertised this as a conjecture with a near-
complete sketch; round-0 review correctly identified it as too
loosely posed. Until steps 1–3 are concretely worked out (probably
a separate round's worth of WO), [C.2] stands as an *open problem*,
not a conjecture.

### Conjecture [C.4] — Galois-conjugate prediction

The 3' irrep of `A_5` in [L.0] is Galois-conjugate to the 3 irrep
under `φ ↔ 1 - φ`. If the cascade reading is correct, a `T = 3`
capsid should exhibit a discrete structural feature whose two states
correspond to the 3 / 3' pair — candidates include:

- A dimorphism in coat-protein orientation at each facet
- A Golden-ratio / silver-ratio bistability in capsid radius
- A pair of near-degenerate coat-protein conformations separated
  by the Galois symmetry

**Status.** Speculative and preliminary. No experimental handle
proposed yet. Flagged here only to mark the expected form of a
future prediction, not to claim one now.

---

## §7. Empirical Predictions and Null Hypotheses (Planned)

The sim in `scripts/wo1_capsid_predict.py` produces the ranked list
of Loeschian T-numbers with their `μ(T)` values out to a cutoff
(default `T ≤ 100`); this script exists and runs.

A companion comparison script `scripts/wo1_compare.py` is **planned
but not yet written**; when implemented it will test three null
hypotheses against an observed VIPERdb T-histogram (also not yet
obtained — see [O.5] below and WO §4). The planned hypothesis
structure is:

| H | Statement | Falsifier (when sim + data land) |
|---|---|---|
| H₀ | Capsid T's are uniformly distributed over all positive integers | Observed T's are confined to Loeschian numbers (classical CK + [L.1]) — expected to be strongly falsified. |
| H₁ | Capsid T's are uniformly distributed over Loeschian numbers | Observed T's show structure beyond bare Loeschian admissibility. |
| H₂ | Capsid T's follow [C.1] with `μ(T)` multiplicity weighting and a monotone assembly-cost `c(T)` | Observed T's do not match the μ-weighted structure; chirality asymmetry [C.3] is zero. |

This table is a **plan**, not a result. No comparison has been run;
no hypothesis has been tested in this repo; [C.1] has not been
empirically fit. The "expected outcome" guesses below are
researcher priors, not evidence.

Researcher priors (for the log, not claims): H₀ expected strongly
falsified (a classical CK-level result), H₁ expected weakly
falsified (small-T heavily over-represented in nature), H₂ unknown
and the interesting question. Each failure mode would tell us
something specific about which cascade ingredient is doing work —
if and when the comparison is actually run.

### Numerical result [N.1] — sim output (present)

Predicted ranked list of `(T, μ(T))` for `T ≤ 100` produced by
`scripts/wo1_capsid_predict.py`; output at
`data/wo1_prediction.csv`. 36 Loeschian T-values ≤ 100, 61 distinct
`C_6` orbits. Novel emergent result confirmed: `μ(91) = 4` (four
distinct orbits: `(1,9), (5,6), (6,5), (9,1)`), consistent with
`91 = 7 · 13` where each factor is a chiral Loeschian prime.

### Numerical result [N.2] — pending (VIPERdb comparison)

VIPERdb observed-T histogram vs. predicted `Z(T)`. χ², KL-
divergence, and chirality-asymmetry test results to be emitted to
`data/wo1_comparison.md` by `scripts/wo1_compare.py`. Script and
data not yet present. Held until the face-level derivation is
codex-clean on substantive content (round 2+).

---

## §8. Open Items Carried Forward

| # | Item | Status | Carries to |
|---|---|---|---|
| 1 | [C.2] face-level residue of Paper XXXII / F2 machinery | Open problem, four-step plan under interpretation (C.2-b) | Future WO or follow-up round after cascade-foundations §F2 re-read |
| 2 | [C.3] chirality asymmetry magnitude | Qualitative conjecture only | Future WO; may connect to the genetic-code chirality work (`cascade-genetic-code.md`) |
| 3 | [C.4] Galois-conjugate structural dimorphism at T=3 | Speculative | Held as "prediction to watch for" — no sim yet |
| 4 | `cascade-bio.md §B3.2` table fix per [R.1] | Edit pending on upstream doc | Downstream bio-md revision, not this WO |
| 5 | Honest form of `c(T)` in [C.1] | Ansatz, to be tested | [N.2] sim will fit or falsify |
| 6 | `wo1_compare.py` and VIPERdb observed-T fetch | Script not yet written; fetch endpoints 404 | Addressed as [N.2] lands |

---

## §9. Summary after Round 1+2 Revision

This revised draft establishes:

- **[T.1] (face-level scope)**: the full CK T-number sequence is
  the spectrum of a single face-level cascade operator `𝒯_casc`,
  uniquely determined up to positive scale by local hexagonal-
  lattice `C_6` symmetry ([L.3]). This provides a face-level
  resolution of the open item in `cascade-bio.md §B3.4`. The
  stronger cell-level version (that `𝒯_casc` descends from the
  Paper XXXII 600-cell closure functional) is **not** claimed here
  and is held as open problem [C.2].
- **[L.3] (now with proper proof)**: any positive-definite
  `C_6`-invariant quadratic form on `ℤ[ω] ⊂ ℝ²` is a positive
  scalar multiple of the Eisenstein norm. Proof via direct matrix
  calculation / Schur's lemma; no sketch remains.
- **[R.1] + [L.2]**: the `T = 5` entry in `cascade-bio.md §B3.2`
  is mathematically unsupported; the honest small-T match is
  `{distinct A_5 irrep dims} ∩ {Loeschians ≤ 5} = {1, 3, 4}`,
  three of the **four** distinct dimensions.
- **[D.3] + [C.1] + [C.3]**: closure-weight and chirality
  conjectures for the VIPERdb test, using the corrected `C_6`-
  orbit multiplicity (the earlier D_6-orbit version was an error;
  see the catalogue revision note on D.3).
- **[C.2]**: open problem linking `𝒯_casc` to the Paper XXXII
  closure functional; previously stated as a conjecture with a
  proof sketch, now honestly framed as an open problem with a
  **four-step** plan of attack under interpretation (C.2-b),
  splitting off from the point-wise (C.2-a) interpretation.
  Paper XXXII citations are corrected to distinguish the 600-cell
  selection theorem (§3, Theorem `thm:600cell`) from the point-
  wise closure-functional uniqueness theorem (§4, Theorem F),
  while the field-theoretic density `F[Φ] = ∫(αR+βE−γQ)dV` lives
  separately at `cascade-derivation/cascade-foundations.md §F2`.

Round 1 codex review is expected to pressure-test: (a) whether
[L.3]'s rewritten proof is now tight; (b) whether the scope
narrowing in [T.1] is faithful to what's actually proved; (c)
whether the sim artefacts now in the repo correctly implement
[L.1] and [D.3]; (d) whether [C.2] is now posed clearly enough
to be either worked out or deferred without ambiguity.
