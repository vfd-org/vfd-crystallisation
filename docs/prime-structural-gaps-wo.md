# WO-VFD-PRIME-GAPS-001 — the unnamed structural gaps, and how to derive them
(2026-06-12)

Audit of the full prime narrative (lab + realization + pullback + witness +
derivations companion) for structural gaps NOT on the site's six-gap list,
plus a derivation path for every gap, named or unnamed. Two kinds:

- **Type D (derivable):** closable by finite computation or self-contained
  argument — these become new D-numbers or short theorems.
- **Type O (open mathematics):** "derive" honestly means *reduce, sharpen,
  or certify the boundary* — never close.

## A. The six MISSING gaps (none currently named anywhere on the site)

### M1 — τ at the operator level  [Type D, decidable finite question]
Finding 5 (pullback) gives only a bookkeeping split. The precise open
question is finite and decidable: does there exist a vertex permutation
(or signed-permutation / orthogonal map) τ on R^120 with
**τ C_φ τ⁻¹ = σ(C_φ)** — the Galois-conjugated operator? (An intertwiner,
not a commutant: it must swap the Galois-paired eigenspaces, which forces
conjugation onto σ(C_φ).) Since C_φ and σ(C_φ) share a spectrum, an
orthogonal intertwiner exists abstractly; the content is whether a
*combinatorial* one exists.
**Derivation path:** build C_φ exactly (closure-prime-statistics-probe /
v600 lib); enumerate candidate τ in the normalizer structure (graph
automorphisms of the 600-cell composed with the σ-twin map of pullback
Finding 4: V₆₀₀ ∪ σV₆₀₀ = even ∪ odd permutation copies — τ should factor
through the 240-vertex double); decide by exact linear algebra. Either
answer is a publishable finite theorem: existence constructs τ;
nonexistence proves the split is *spectral-only*, upgrading Finding 5's
honesty into a theorem.

### M2 — the identification theorem  [Type D]
The 664/664 and 44/44 provenance MATCHES the geometric construction
against point counts; nowhere is it *proven* that the icosian P¹-action
Brandt module IS the standard Eichler/Pizer/Dembélé Brandt module as a
Hecke module. **Derivation path:** both are built from the class set of
the same maximal order with the same level structure; exhibit the
isomorphism explicitly (class-number-1 case: the P¹ orbits ARE the right
ideal classes at level P — a two-page argument from the local splitting),
then the agreement stops being evidence and becomes a theorem with the
point counts as confirmation. Converts the anchor's strongest empirical
claim into its strongest structural claim.

### M3 — K=4 completeness for Eichler–Brandt  [Type D, small]
Pullback Finding 2 says K=4 is "plausibly complete because √p < 5".
**Derivation path:** for an icosian q with N_H(q) = p, each coordinate of
q satisfies |x_i| ≤ √p in every real embedding (positive-definite norm
form); hence integer coordinates (a,b) of x = (a+bφ)/2 are bounded by an
explicit constant < 2K for p ≤ 23. One lemma; removes the word
"plausibly" from a published finding.

### M4 — the spectrum itself  [Type D, derivable in full → D16]
The numbers 94+13+13 descend from the A₁ eigenvalues
{12, 3, 0, −2, −3, 6φ, 6−6φ, 4φ, 4−4φ} with their multiplicities — used
everywhere, derived nowhere on the prime pages. **Derivation path:**
Cayley-graph spectral theory on 2I: eigenvalues of the class-sum operator
are χ(g)|C|/χ(1) over the nine irreducible characters of 2I; the
character table of 2I is classical (entries in Z[φ]); the multiplicities
are χ(1)². One section, fully derivable, and it explains *why* exactly
two Galois-paired eigenvalue pairs exist (the two 2-dimensional and the
two... — the irrationality pattern of the character table). Candidate
D16 for the derivations companion.

### M5 — zero certification  [Type D-ish, implementable]
The 33 zeros are computed (lfunzeros + functional-equation consistency),
not *certified*: no rigorous zero count via the argument principle, no
Turing-method bound showing none were missed below height 25.
**Derivation path:** implement N(T) by lfun-based argument-principle
integration with interval control (PARI), or the Turing bound for
degree-4 L-functions; output "certified: exactly 33 zeros to height 25,
all simple, all located". Upgrades "computed" to "certified" — the word
a hostile analyst looks for.

### M6 — lift existence  [Type D for the toy; Type O for the real thing]
Witness-resonance defines the substrate lift but constructs none.
**Derivation path (toy):** ℋ₊ = V₊ ⊗ ℓ²(N) with closure-flow extended
diagonally and Hecke extended through the modular tower; verify the
constraint list is satisfiable *except* the spectrum condition. Upgrades
Definition → Existence-of-the-frame, isolating the spectrum condition as
the entire remaining content (sharper than the current statement).

## B. The six NAMED gaps — what "derive" honestly buys

| gap | type | the derivable move |
|---|---|---|
| 1 infinitude | O | nothing derivable closes it; the ledger already states the frontier (≤246). Say so and stop. |
| 2 the wall | O | derivable sharpening: **certified Li coefficients** λ₁…λ_m for the icosian L from certified zeros (needs M5) with explicit truncation bounds — converts "finite-positive" into "certified-positive to order m". |
| 3 margin rate | O→D | derive the *conditional* rate law: under effective Sato–Tate, the expected Weil-margin decay; then measure √n·D_n on the 664 (and frontier-extended) data against it. One datum becomes a conditional law + a measured curve. |
| 4 curve-as-input | D programme | the flagship: (a) derive conductor + eigenvalue rationality from Brandt data alone [short]; (b) modularity existence theorem (defined with source: Freitas–Le Hung–Siksek for real quadratic fields) ⇒ a curve with these a_P exists; (c) derive a **Faltings–Serre criterion** for Q(√5), conductor p₃₁: an explicit finite set S of primes such that agreement of a_P on S determines the isogeny class; (d) bounded search + certificate ⇒ **the curve is reconstructed, not input**, with the 44-ideal agreement as confirmation. Every step is known technology; nobody has assembled it for this case. The next anchor-grade paper. |
| 5 the family | D compute | extend multilevel dimensions + eigensystems past norm 100; inert and composite levels (Eichler orders); cross-check vs LMFDB HMF tables. Scripts mostly exist; outputs feed the realization as new data tables. |
| 6 open halves | O + one D | GUE and Dyson's classification stay open. The derivable piece: **D13′ — the uniform peak asymptotic of the Riesz-tapered spectrum** (smoothed explicit formula; peak height/width laws in X and k). Genuine analysis but self-contained; would move D13 from "gap" to "derived". |

## C. Priority order (effort × narrative value)

1. **M3** (a lemma — hours) and **M4** (a section — a day): pure wins,
   both become D-numbers.
2. **M1** (finite computation + short argument): either outcome is a
   theorem; directly upgrades the pullback paper.
3. **M2** (the identification theorem): converts the anchor's core from
   evidence to theorem.
4. **M5** (certification): one script + one paragraph; arms gap-2's
   Li-coefficient move.
5. **Gap-4 programme** (a)–(d): the next flagship paper, "The curve as
   output". Steps (a),(c),(d) are derivations; (b) is a citation.
6. **D13′** and the **gap-3 conditional law**: medium analysis projects.

Rule unchanged: each result lands as a derivation with a numeric check in
`lab/derivations_check.py`, hostile-review loop before push, site
references by D/M-number.

## D. The missing structures for gaps 1, 2 and 6 (what would let us dig)

These three are Type O. "Digging in" means building the structure each one
is missing — and naming the barrier that the structure must overcome.

### Gap 1 (infinitude): the missing structure is OFF-DIAGONAL control
The wheels control single-pattern densities. Infinitude requires control
of prime PAIR correlations — by the explicit formula, equivalently control
of ZERO pair correlations. The precise missing object is Montgomery's form
factor **F(α) for α ≥ 1** (proven only for α < 1); Goldston's equivalences
make this exact: averaged twin-type asymptotics ⟺ F-behaviour beyond the
proven range. The named barrier is the **parity problem** of sieve theory:
linear sieve information cannot distinguish integers with an even vs odd
number of prime factors, which is exactly why Maynard-type machinery
proves "some gap ≤ 246 recurs" but cannot fix WHICH gap. Breaking it needs
bilinear/Type-II information for the pattern — the one ingredient nobody
has.
**Diggable now:** (i) build the pair-correlation instrument — compute
F(α, T) from our 1,983 zeros and display Montgomery's wedge (the
instrument for the wall's second floor; ledger row 10 is its first
floor); (ii) a Goldston-equivalence dashboard (which F-statement buys
which prime-pair statement); (iii) exhibit the parity barrier concretely
(Selberg's ±λ(n) example fooling a linear sieve) — make the barrier
itself a derived, visualised object on the site.

### Gap 2 (the wall): the missing structure is a COHOMOLOGICAL HOME
Why the wall sits exactly where it does, structurally: the definite
icosian order's geometric object is ZERO-dimensional (a finite class set).
Dimension 0 has no H¹, no intersection pairing, no Frobenius-on-cohomology
— so the definite side can only ever produce coefficients, never zeros.
The function-field proof of RH (Weil) runs through exactly the structures
we lack: a cohomology carrying the eigenform, an intersection pairing, and
a positivity statement (Hodge index). For number fields at large this is
the Connes/Deninger programme (open). For OUR L-function specifically, the
missing structure has a name: the **Jacquet–Langlands partner** — the
indefinite quaternion algebra over Q(√5) (ramified at p₃₁ and one
infinite place) whose Shimura CURVE has an H¹ that carries the same
eigenform, and where arithmetic intersection theory (heights, Arakelov)
actually lives.
**Diggable now:** (i) state and source the JL transfer for our form;
assemble the Shimura-curve data (level, genus, CM points) — the wall-side
geometry made concrete; (ii) the near-term certified moves already in
§B: M5 certification → certified Li coefficients λ₁…λ_m; (iii) write the
"why the wall is exactly here" remark (dim-0 has no H¹) as a derivable
addition — it upgrades the wall page from location to *explanation*.

### Gap 6 (open halves): one shared object + one classification
**6a (GUE beyond Montgomery's range)** is the SAME missing object as
gap 1: F(α) for α ≥ 1. One structure, two famous costumes — worth saying
on the site.
**6b (Dyson's classification)**: the missing structure is a
classification of Fourier quasicrystals BEYOND the cut-and-project class
— and recent mathematics locates the frontier precisely: Lev–Olevskii
showed the rigid class (positive, uniformly discrete support and
spectrum) is essentially lattice combinations, and Kurasov–Sarnak
constructed genuinely new one-dimensional Fourier quasicrystals from
stable (Lee–Yang) polynomials. Derivable proposition (D21 candidate):
the zeta zeros have average gap 2π/log T → 0 and the prime-power
frequencies log p^m accumulate, so under RH the zero quasicrystal has
NON-uniformly-discrete support and spectrum — it provably lies OUTSIDE
the lattice and cut-and-project classes (including our Fibonacci chain).
So the site's crystal page can sharpen honestly: Fibonacci is the charted
territory; the zeros, even under RH, live in the wider Kurasov–Sarnak
wilderness; the missing structure is the classification of that
wilderness, and the modern question is whether the zero measure is a
limit of Lee–Yang-type constructions.
**Diggable now:** write D21 (the outside-the-charted-class proposition,
elementary from zero-density + log-prime accumulation); add the taxonomy
(lattice / model set / stable-polynomial FQ / zeros' conjectural
position) to the crystal page with sources.
