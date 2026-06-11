# Biology-Rung Math Catalogue

**Purpose:** Every new mathematical object introduced in this
programme (definition, lemma, theorem, conjecture, computational
result) is logged here with provenance and status, so the eventual
paper write-ups have a single source to harvest from.

**Convention:**

- `D.n` — definition
- `L.n` — lemma
- `T.n` — theorem
- `C.n` — conjecture
- `R.n` — remark
- `N.n` — numerical/computational result

Each entry lists:

| field | meaning |
|---|---|
| **Name** | Short handle used in derivations |
| **Statement** | The mathematical content (one to three lines) |
| **Provenance** | Which existing framework piece it extends or restricts from (cite `file:line` or paper/section) |
| **Status** | `proved` / `conjectured` / `computational` / `open` |
| **Used in** | Which derivation file consumes it |
| **Planned paper** | Which eventual paper carries it into print |

New entries go at the bottom of the relevant WO section. Never edit
an entry in place without also bumping its status line — the ledger
is append-only for audit reasons.

---

## WO-1 — Capsid T-number operator

### D.1 — Face-level Eisenstein substrate [REVISED after round 0]

**Statement.** The pair `𝕊 := (ℤ[ω], A_5 ↷ 𝓕₂₀)`, where `ℤ[ω]` is
the Eisenstein integers (hexagonal lattice on one icosahedral face
with basis `{1, ω}`, `ω = e^{iπ/3}` the primitive sixth root — see
D.3 notation block) and `𝓕₂₀` is the 20-face set carrying the `A_5`
permutation representation `π_20`. Two symmetry groups act, kept
distinct: `A_5` permutes faces (with face-stabiliser `C_3`
rotationally, `D_3` under `I_h`); the six Eisenstein units form a
`C_6` acting on `ℤ[ω]` by multiplication, which is an intrinsic
rotational symmetry of the hexagonal lattice, **not** a face
stabiliser in the icosahedral group.

**Revision note.** Initial draft claimed "`C_6` is the face
stabiliser in `I_h`" — codex round-0 review correctly flagged this
as wrong (the face stabiliser is `C_3` / `D_3`, not `C_6`). The
`C_6` in question is the hexagonal-lattice automorphism, separate
from the icosahedral group. Scope tightened from "cell-level" to
"face-level" throughout; the cell-level extension is open problem
[C.2].

**Provenance.** Extends `cascade-bio.md §B1` / §3.1 (cell-level
biology, which identifies the biological scale but does not specify
the face-level Eisenstein structure) by naming the face-level
Eisenstein substrate and the two-group-action structure explicitly.

**Status.** Proved (construction).

**Used in.** `derivation-capsid.md §2`.

**Planned paper.** Capsid T-number paper (biology-rung paper 1).

---

### D.2 — Cascade T-operator (face-level) [REVISED after round 0]

**Statement.** `𝒯_casc : ℤ[ω] → ℤ_{≥0}`, `𝒯_casc(z) := z · z̄ =
|z|²`. For `z = h + kω` (with `ω` the primitive sixth root),
`𝒯_casc(z) = h² + hk + k²`. `𝒯_casc` is invariant under the `C_6`
action of multiplication by the six Eisenstein units. It is
scalar-valued and therefore transforms trivially under any group
action on its domain.

**Revision note.** Earlier draft claimed "`A_5`-equivariant"
equivariance; codex round-0 flagged this as vacuous (scalar-valued
map) and confusing (no A_5 action defined on `ℤ[ω]` itself). Claim
removed.

**Provenance.** `z ↦ |z|²` is the classical Eisenstein norm.
Cascade-specific content is [L.3] (uniqueness under hexagonal-
lattice `C_6` symmetry), which picks out `𝒯_casc` as **the**
face-level operator up to positive scale without arbitrary choice.

**Status.** Proved (construction).

**Used in.** `derivation-capsid.md §3, §4, §6`.

**Planned paper.** Capsid T-number paper.

---

### D.3 — Orbit multiplicity μ(T) [REVISED 2026-04-23: D_6 → C_6]

**Statement.** Let `ω = e^{iπ/3}` (primitive sixth root of unity;
chosen here so that `N(h + kω) = h² + hk + k²` literally — see
derivation-capsid.md §1.1 for the notation reconciliation with
`cascade-bio.md §B3.1`, which writes `e^{2πi/3}`). For Loeschian
`T`, `μ(T) := #{ C_6-orbits of (h, k) ∈ ℤ² \ {0} with h² + hk + k²
= T }`, where `C_6` acts on `ℤ[ω]` by the six Eisenstein units (no
reflection — `2I` and `A_5` are proper rotation groups).

An individual orbit contributes `μ = 1` when its canonical wedge
representative lies on a hexagonal-lattice reflection axis —
either `k = 0` or `h = k` — so the orbit coincides with its
mirror (achiral). It contributes `μ = 2` when `h, k > 0` are
nonzero and distinct, giving a laevo/dextro chiral pair.
Summed across independent norm factorisations, `μ(T) ≥ 3`
occurs at Loeschian `T` with multiple distinct norm
factorisations (e.g. `T = 49`, `T = 91`).

**Provenance.** New to this WO. `μ` is elementary combinatorics on
`ℤ[ω]`; named and catalogued here because [C.3] assigns it biological
meaning (chirality splitting).

**Revision note.** Initial draft used `D_6` (rotations + reflection),
which would collapse chirality pairs. Corrected to `C_6` (rotations
only) before round-0 codex review concluded; the example values given
in the derivation (μ(7) = 2 etc.) were always C_6 values.

**Status.** Proved (definition).

**Used in.** `derivation-capsid.md §5`.

**Planned paper.** Capsid T-number paper; possibly cited in
amyloid / chirality paper (WO-2).

---

### L.0 — Decomposition of π_20

**Statement.** The `A_5` permutation representation on the 20
icosahedral faces decomposes as

  `π_20 = 𝟏 ⊕ 𝟑 ⊕ 𝟑' ⊕ 𝟒^{⊕2} ⊕ 𝟓`

with multiplicities `(1, 1, 1, 2, 1)` on the irreducibles of
dimensions `(1, 3, 3, 4, 5)`. Total dimension `20`.

**Provenance.** Standard character-theoretic calculation; cited here
because the existing `cascade-bio.md §B3.2` small-T match is
re-interpreted in terms of this decomposition.

**Status.** Proved (standard).

**Used in.** `derivation-capsid.md §1.2, §4`.

**Planned paper.** Capsid T-number paper.

---

### L.1 — Spectrum of 𝒯_casc equals Loeschian numbers

**Statement.** `spec(𝒯_casc) := 𝒯_casc(ℤ[ω] \ {0}) = {Loeschian
numbers}` = OEIS A003136 = `{1, 3, 4, 7, 9, 12, 13, 16, 19, 21, …}`
= Caspar–Klug T-number sequence.

**Provenance.** Elementary consequence of `𝒯_casc = N_Eisenstein`
and the characterisation of Loeschian numbers as norms on `ℤ[ω]`.

**Status.** Proved.

**Used in.** `derivation-capsid.md §3`.

**Planned paper.** Capsid T-number paper.

---

### L.2 — Honest small-T / A_5 match [REVISED after round 0]

**Statement.** `A_5` has five irreducible representations with
**four** distinct dimensions: `1`, `3`, `4`, `5`; the dimension `3`
occurs twice as a Galois-conjugate pair. The Loeschian numbers
`≤ 5` are `{1, 3, 4}`. Hence

  `{distinct A_5 irrep dims} ∩ {Loeschians ≤ 5} = {1, 3, 4}`.

Three of the four distinct `A_5` irrep dimensions coincide with
small Loeschian numbers. The dimension `5` is not Loeschian; the
duplicate-dimension `3'` carries the same value as `3` and so
contributes no new T-value.

**Revision note.** Earlier draft said "three of the five distinct
A_5 irrep dimensions"; codex round-0 flagged that A_5 has four
distinct dimensions (not five — dimension 3 appears twice).
Corrected.

**Provenance.** Corrects the implicit T=5 claim in `cascade-bio.md
§B3.2` table (line 283).

**Status.** Proved.

**Used in.** `derivation-capsid.md §4`.

**Planned paper.** Capsid T-number paper (replaces the existing
partial small-T match).

---

### L.3 — Uniqueness of 𝒯_casc under C_6 symmetry [REVISED after round 0]

**Statement.** Any positive-definite quadratic form `Q : ℤ[ω] →
ℝ_{≥0}` that extends to a `C_6`-invariant quadratic form on
`ℝ² ≅ ℂ` (where `C_6` acts by multiplication by Eisenstein units)
satisfies `Q = c · 𝒯_casc` for some `c > 0`.

**Proof.** Matrix argument: write `Q(x) = x^⊤ M x` with `M` a
symmetric positive-definite `2 × 2` matrix. `C_6`-invariance forces
`R_{π/3}^⊤ M R_{π/3} = M`, which (by direct calculation or Schur's
lemma via the fact that `R_{π/3}` has non-real eigenvalues
`e^{±iπ/3}`) implies `M = a · I₂`, hence `Q(x) = a |x|² = a ·
𝒯_casc(z)` on `ℤ[ω]`.

**Revision note.** Earlier draft had only a sketch; codex round-0
flagged that the matrix/centraliser argument was not written out.
The full proof is now in `derivation-capsid.md §3`. Interpretation
also sharpened: the `C_6` symmetry is the hexagonal lattice's own
rotational symmetry, **not** a face-stabiliser in the icosahedral
group.

**Provenance.** Cascade-specific content at the face level.

**Status.** Proved.

**Used in.** `derivation-capsid.md §3`; cited in open problem [C.2]
as step 4 of the plan of attack.

**Planned paper.** Capsid T-number paper.

---

### T.1 — Face-level T-number sequence from one operator [REVISED after round 0]

**Statement.** There exists a face-level operator `𝒯_casc` on the
Eisenstein substrate `ℤ[ω]` (per [D.1]/[D.2]), uniquely determined
up to positive scale by local hexagonal-lattice `C_6` symmetry
([L.3]), whose spectrum is exactly the sequence of Caspar–Klug
T-numbers ([L.1]).

**Revision note.** Earlier draft claimed a cell-level / 600-cell
substrate result. Codex round-0 correctly flagged that what is
actually shown is a face-level result; the cell-level / 600-cell
version requires the open problem [C.2]. Scope tightened
accordingly: this theorem is now explicitly face-level.

**Provenance.** Provides a face-level resolution of the open item
in `cascade-bio.md §B3.4` line 320 ("Full derivation of all
T-numbers from one cascade operator"). The full cell-level
resolution is left to [C.2].

**Status.** Proved (combining [L.1] and [L.3]) at face-level scope
only.

**Used in.** `derivation-capsid.md §3`.

**Planned paper.** Capsid T-number paper (headline face-level
result; the unresolved cell-level question is a companion open
problem).

---

### R.0 — 2I versus A_5 on the substrate

**Statement.** The cell-level substrate admits both `2I ⊂ SU(2)`
(order 120, double cover, with spin-½ reps relevant to antipodal-
face chirality) and `A_5 = 2I / {±1}` (order 60, acting on 𝓕₂₀).
This derivation works with `A_5` for face-level statements; `2I`
appears in §6 (chirality).

**Provenance.** `cascade-bio.md §2.1–2.3`.

**Status.** Remark.

---

### R.1 — The T=5 entry in cascade-bio.md §B3.2 is misleading [REVISED after round 1]

**Statement.** The table entry "T=5 ↔ A_5 5-dim irrep" at line 283
of `cascade-bio.md` is misleading on **purely mathematical** grounds:
`5` is not a Loeschian number (no `(h, k) ∈ ℤ²` satisfies `h² + hk
+ k² = 5`, as `5` is inert in `ℤ[ω]` with odd exponent), and hence
`5 ∉ spec(𝒯_casc)` by [L.1]. The `A_5` 5-dim irrep is a component
of the permutation representation `π_20` (see [L.0]); it is a
representation-theoretic invariant, not an Eisenstein norm value,
and it does not predict a `T=5` capsid.

Whether the Loeschian mathematical prohibition is further reinforced
by an *empirical* absence of `T=5` capsids is a separate question,
deferred to [N.2] (VIPERdb comparison). No empirical claim is made
here.

**Revision note.** Earlier draft included the unsourced claim "no
`T=5` capsids are observed". Codex round-1 flagged this as
unsourced; claim removed. The mathematical argument stands on its
own and does not require the empirical claim.

**Provenance.** Audit of `cascade-bio.md §B3.2` table.

**Status.** Remark (downstream edit pending on `cascade-bio.md`).

**Used in.** `derivation-capsid.md §4`.

---

### R.2 — 3' Galois pair as open prediction [REVISED after round 0]

**Statement.** The Galois-conjugate 3' irrep of `A_5` has the same
dimension as the 3 irrep and so contributes no new T-value; but
the two are character-theoretically distinguishable, swapped under
`φ ↔ 1 − φ`. Its possible structural meaning is captured by [C.4].

**Provenance.** Standard `A_5` character theory (e.g. ATLAS of
Finite Groups), imported into this document. Codex round-0
flagged — correctly — that `cascade-bio.md §B3.2` does **not**
itself discuss a 3/3' pair; only one 3-dim irrep appears in the
upstream table. So the provenance is representation-theoretic
(external), not internal to `cascade-bio.md`.

**Status.** Remark pointing at [C.4].

---

### C.1 — Closure-preference weighting [REVISED round 2: untested]

**Statement.** `Z(T) ∝ μ(T) · exp(-β · c(T))` where `μ(T)` is the
orbit multiplicity [D.3] and `c(T)` is a monotone non-decreasing
assembly-cost function, `β` an order-unity cascade constant.

**Provenance.** New conjecture. `μ(T)` factor is forced by [D.3];
the exponential assembly-cost ansatz is a modelling choice to be
tested when [N.2] lands.

**Status.** Conjectured. **Not tested yet** — the earlier status
line "tested against VIPERdb" was inaccurate; `wo1_compare.py`
does not yet exist, and no VIPERdb comparison has been run. The
test is planned; the planned hypothesis stack (H₀/H₁/H₂) is in
`derivation-capsid.md §7`.

**Used in.** `derivation-capsid.md §5, §7`.

**Planned paper.** Capsid T-number paper.

---

### C.2 — Does 𝒯_casc descend from a cell-level Paper XXXII / F2 construction? [REVISED round 1: refined interpretation split + four-step plan]

**Statement.** *Open problem.* Split into two interpretations:

- **(C.2-a)** point-wise form: is there a principled `2I`-
  invariant restriction of the point-wise Paper XXXII closure
  functional `F_ε^V : S³ → ℝ` (§4 Theorem F) to a face-level
  operator on `ℤ[ω]`? As stated this is ill-posed — a point-
  wise function on `S³` does not naturally give a quadratic form
  on the face-lattice — so (C.2-a) reduces in practice to
  (C.2-b) after a field-theoretic lift.

- **(C.2-b)** field/density form: does the density-level closure
  functional `F[Φ] = ∫ (α R + β E − γ Q) dV` from
  `cascade-derivation/cascade-foundations.md §F2`, restricted to
  `2I`-invariant fields and face-level-averaged via the Hopf
  cell-fibre structure, reduce on each face to `λ · 𝒯_casc` for
  some `λ > 0`?

The four-step plan of attack is in `derivation-capsid.md §6`:
(1) identify the `2I`-invariant subspace of F2 field
configurations; (2) construct a principled face-level projection;
(3) show `F[Φ]` restricts along it to a positive-definite
quadratic form on `ℤ[ω]`; (4) apply [L.3].

**Provenance + upstream citation history.** Earlier drafts
conflated two separate theorems in Paper XXXII and mis-pathed
foundations.tex. Round 1 correction:

- `papers/paper-xxxii/paper-xxxii.tex §3` Theorem `thm:600cell`
  (~line 237): under `(H1)–(H4)`, `G = 2I`.
- `papers/paper-xxxii/paper-xxxii.tex §4` Theorem F (~line 363):
  within the soft-min class, axioms A1–A3 force the log-sum-exp
  form of the point-wise closure functional `F_ε^V : M → ℝ`.
- `papers/cascade-derivation/cascade-foundations.md §F2`
  (~line 91): density form `F[Φ] = ∫ (α R + β E − γ Q) dV` under
  (i) locality, (ii) W(E₈)/σ/translation invariance, (iii) order
  ≤ 2, (iv) scalar-valued.

Round 1 also tightened: Paper XXXII's `F` is **point-wise on the
manifold** not a field functional; the field-theoretic object is
cascade-foundations §F2. Earlier framing that treated them as one
object was an attribution overreach.

**Status.** Open problem. Four-step plan of attack (not three; the
earlier "three-step" phrasing was an off-by-one) for
interpretation (C.2-b); interpretation (C.2-a) reduces to (C.2-b)
after a lift.

**Used in.** `derivation-capsid.md §6`.

**Planned paper.** Capsid T-number paper (as principal open
problem with four-step plan); resolution deferred to a follow-up
WO.

---

### C.3 — Chirality asymmetry from 2I handedness

**Statement.** For chiral T-numbers (μ(T)=2), the cascade predicts
a nonzero empirical asymmetry `(N_laevo - N_dextro) / (N_laevo +
N_dextro) ≠ 0`, with sign set by the ambient biological chirality
(L-amino-acid world). Magnitude not yet derived from first
principles.

**Provenance.** Extends `cascade-bio.md §2.7` + B5 (2I handedness
→ L-amino-acid preference) from amino-acid scale to capsid scale.

**Status.** Conjecture (qualitative direction only).

**Used in.** `derivation-capsid.md §5, §7`.

**Planned paper.** Capsid T-number paper.

---

### C.4 — Galois-conjugate structural dimorphism at T=3

**Statement.** The 3/3' Galois pair in [L.0] may manifest as a
discrete structural feature of T=3 capsids: coat-protein orientation
dimorphism, φ vs. 1-φ radius bistability, or near-degenerate
conformations separated by the Galois symmetry.

**Provenance.** Speculative extension of [L.0] / [L.2].

**Status.** Open conjecture; no concrete experimental handle
proposed yet.

**Used in.** `derivation-capsid.md §4, §6`.

**Planned paper.** Flagged in capsid paper as a "prediction to
watch for"; substantive development deferred.

---

### N.1 — Predicted ranked T-list [REVISED round 1: sim now present]

**Statement.** `scripts/wo1_capsid_predict.py` (present) emits the
predicted ranked list of `(T, μ(T))` for `T ≤ 100` to
`data/wo1_prediction.csv` (present). 36 Loeschian T ≤ 100,
61 distinct `C_6` orbits. Spot-check assertions all pass for
`T ∈ {1, 3, 4, 7, 9, 12, 13, 16, 19, 21, 25, 27, 28, 31, 37, 39,
49, 91}` and forbidden `T ∈ {2, 5, 6, 8, 10, 11, 14, 15, 17, 18,
20}`. Novel emergent result: `μ(91) = 4` (first Loeschian T with
four `C_6` orbits, arising from `91 = 7 × 13`, each a chiral
Loeschian prime).

**Revision note.** Earlier status was "pending sim run"; sim is
now present and has run successfully. Round-2 fix removed the
contradictory "pending sim run" status line.

**Status.** Computational; complete. 18 μ-value spot-checks +
11 forbidden-T spot-checks all pass (see `scripts/wo1_capsid_predict.py`
summary output).

**Used in.** `derivation-capsid.md §7`.

---

### N.2 — VIPERdb comparison [REVISED round 2: not-yet-built]

**Statement (planned).** A future `scripts/wo1_compare.py` will
emit χ², KL-divergence, and laevo/dextro chirality-asymmetry
results against an observed VIPERdb T-histogram; planned output
at `data/wo1_comparison.md`.

**Status.** **Not implemented.** Neither `scripts/wo1_compare.py`
nor the observed-T dataset exists in-repo. The fetch script
`scripts/wo1_viperdb_fetch.py` exists but current candidate
endpoints return 404 (VIPERdb API has evolved; candidate URLs need
refreshing against current VIPERdb documentation).

**Used in.** Referenced by `derivation-capsid.md §7` (planned
hypothesis stack) and [C.1]'s eventual empirical test.

---

## WO-2 — Amyloid fibril twist

### D.1 (WO-2) — Helical closure orbit

**Statement.** Given a 5-fold axis `A` of the 600-cell with
direction `ẑ`, a helical closure orbit of pitch `(α, h)` is the
orbit of a base point under `⟨R_α · T_h⟩`, where `R_α ∈ 2I` is a
rotation about `A` by angle `α` and `T_h` is axial translation by
`h`. Closure-compatible iff `α` is a rational multiple of `2π`.

**Provenance.** Extends B2's decagram helical orbit
(`cascade-bio.md §5.1`) from the single fast pitch to the full
class.

**Status.** Definition.

**Used in.** `derivation-amyloid.md §2`.

**Planned paper.** Amyloid paper (biology-rung paper 3).

---

### L.1 (WO-2) — Admissible angle set on 5-fold axis [REVISED proof]

**Statement.** The preimage in 2I (double cover of I ≅ A_5) of a
5-fold stabiliser C_5 in I is cyclic of order 10: the central
extension `1 → {±1} → 2I → I → 1` restricted to this stabiliser
splits as `C_10 = C_5 × C_2` (since `|C_5| · |C_2| = 10` is
squarefree). The SU(2) rotation angles of the 10 elements are
10th roots of unity on SU(2) about the axis:
`Stab_2I(A) = {2πk/10 : k = 0, …, 9}`. Smallest nonzero is 36°.

**Revision note.** Earlier draft's proof appealed loosely to
``conjugacy classes of 2I on a fixed axis''. Replaced with the
explicit central-extension / splitting argument.

**Status.** Proved.

**Used in.** `derivation-amyloid.md §2`.

---

### R.1 (WO-2) — Small-angle amyloid-twist constraint

**Statement.** Empirical amyloid twists (1°–5°) are below the
36° minimum of L.1, so they cannot arise as single 2I-element
rotations about the 5-fold axis. They must emerge from
commensurable compound rotations, cell-level orbits, or subgroup
orbits.

**Provenance.** Follows immediately from L.1.

**Status.** Remark.

---

### D.2 (WO-2) — Commensurable twist family [REVISED: N is parameter, not minimal]

**Statement.** For `α ∈ Stab_2I(A)\{0}`, integer `N ≥ 1`, and
integers `(p, q)` with `gcd(p, q, N) = 1`, the commensurable
twist at `(α; p, q, N)` is `θ(α; p, q, N) = (p α − q · 2π)/N`
reduced mod `2π`. N is an explicit parameter of the definition.
The commensurable twist set with resolution `N_max` is
`Θ_adm(A; N_max) = {θ(α; p, q, N) : … , 1 ≤ N ≤ N_max}`.

For α = 36°, θ = 36°(p − 10q)/N, so attainable twists are integer
multiples of 36°/N and do not depend on the specific α choice
(all α in Stab_2I(A) are multiples of 36°).

**Revision note.** Earlier draft made N minimal, creating a
circular definition. Corrected: N is now an explicit parameter.

**Status.** Definition.

**Used in.** `derivation-amyloid.md §2`.

---

### L.2 (WO-2) — Discreteness of Θ_adm

**Statement.** `Θ_adm(A)` is countable, and for each
`α ∈ Stab_2I(A) \ {0}` there is an infinite sequence `(p_n, q_n)`
(best rational approximants to `α/2π`) with `θ → 0`.

**Status.** Proved (continued-fraction argument).

---

### D.3 (WO-2) — Amyloid-scale compatibility [REVISED: corrected window]

**Statement.** A twist θ is amyloid-scale compatible if
`M θ = 360°` (exact) and `M · 4.7 Å ∈ [100 Å, 500 Å]`, giving
`22 ≤ M ≤ 106` and `θ ∈ [3.3962°, 16.3636°]`.

**Revision note.** Earlier draft had upper bound `17.1°` for
`M = 21`, but `21 · 4.7 = 98.7 Å` < `100 Å`, so `M = 21` fails
the crossover lower bound; corrected to `M = 22`, upper bound
`θ_max = 360/22 ≈ 16.36°`.

**Status.** Definition.

---

### L.3 (WO-2) — Enumeration of admissible twists [REVISED]

**Statement.** The commensurable twists
`θ = 36°(p − 10q)/N ∈ [3.3962°, 16.3636°]` for `N ≤ 20` form a
finite discrete set; `36°/N` representatives include
`N = 3, …, 10`, i.e.
`{12.0°, 9.0°, 7.2°, 6.0°, 5.14°, 4.5°, 4.0°, 3.6°}`. Note:
`36°/11 ≈ 3.27°` is BELOW the corrected lower bound 3.4° and so
NOT admissible. All admissible twists are in the `36°/N · ℤ`
ladder; α ∈ {72°, 108°, 144°, 180°} gives no new angles.

**Status.** Computational (sim run at
`scripts/wo2_helical_orbits.py`; 24 distinct θ values, all N=3..10
spot-checks pass).

---

### C.1 (WO-2) — Amyloid twist selection rule

**Statement.** Observed cross-β amyloid per-strand twists cluster
on the enumeration `Θ_adm(A) ∩ [3.4°, 17.1°]` rather than
distributing uniformly.

**Status.** Conjecture; empirical test pending
(`scripts/wo2_compare.py`, same WAITING_FOR_DATA design as WO-1).

---

### R.2 (WO-2) — Ultra-slow-twist polymorphs

**Statement.** Some tau / α-synuclein polymorphs show twists
< 3.4° (crossover > 1500 Å). Three candidate explanations:
(i) higher-denominator `N > 106` regime; (ii) different axis /
orbit class (3-fold or cell-level); (iii) loose lower bound.

**Status.** Remark / open question.

---

### C.2 (WO-2) — Cascade chirality bias for fibrils

**Statement.** Cross-β fibrils should show a handedness bias
consistent with the L-amino-acid world, inherited from the 2I
god-prime chirality
(`cascade-bio.md §B5`).

**Status.** Qualitative conjecture.

---

### C.3 (WO-2) — Protofilament count from 2I subgroups

**Statement.** Admissible protofilament bundle symmetries
correspond to non-trivial cyclic and binary-dihedral subgroups
of 2I (`C_1, C_2, C_3, C_5, D_2, …`). Testable against cryo-EM
protofilament-count statistics.

**Status.** Conjecture; enumerable.

---

### C.4 (WO-2) — Cell-level orbit supplement

**Statement.** Sub-3.4° amyloid twists may require cell-level
orbits on the 600 tetrahedral cells rather than vertex orbits.
Depends on resolving the conjectural Hopf cell-fibration
(`cascade-bio.md §2.6`).

**Status.** Open.

---

### C.5 (WO-2) — Axis selection

**Statement.** Different amyloid polymorphs could correspond to
different axis choices (5-fold vs. 3-fold vs. 2-fold) on the
600-cell.

**Status.** Open.

---

### C.6 (WO-2) — Unified closure operator with WO-1

**Statement.** Open question: can the amyloid twist selection
rule be framed as a closure-operator spectrum analogue to WO-1's
`𝒯_casc`?

**Status.** Open.

---

### N.1 (WO-2) — Enumeration output

**Statement.** `scripts/wo2_helical_orbits.py` will emit the
discrete admissible-twist set to
`data/wo2_prediction.csv` (columns
`α, p, q, N, θ, M, crossover`).

**Status.** Pending.

---

## WO-3 — Tubulin and taxane binding

### D.1 (WO-3) — 13-adjacency chamber

**Statement.** A physical lattice Λ with cyclic symmetry `C_n`
and a ℂ-linear action on an internal 13-dim state space `V` such
that each of the 13 adjacency directions from upstream T_PH_1 is
realised as a distinct `C_n`-eigenmode and no two directions
share a character. The microtubule protofilament lattice is the
empirical candidate.

**Provenance.** New; built on upstream T_PH_1
(`cascade-photon-microtubule-alpha-programme.md §2`).

**Status.** Definition.

**Used in.** `biology-rung-tubulin.tex §3`.

**Planned paper.** Tubulin paper (biology-rung paper 4).

---

### T.1 (WO-3) — Primality forces n = 13 (T_MT_1 + T_MT_2 unified)

**Statement.** For a 13-adjacency chamber (D.1), `n = 13`
uniquely; `C_13` has 13 distinct characters, all non-trivial ones
generating the full group (primality), giving an indecomposable
selector.

**Provenance.** Upgrades upstream T_MT_1 and T_MT_2
(`cascade-photon-microtubule-alpha-programme.md §2`) from Tier-2
conjectures to Tier-1 theorem under the T_PH_1 hypothesis.

**Status.** Proved (conditional on T_PH_1).

**Used in.** `biology-rung-tubulin.tex §3`.

---

### T.2 (WO-3) — Non-13 counts degenerate (T_MT_3)

**Statement.** For `n ∈ {11, 12, 14, 15, 16} \ {13}`: either
address count mismatch (n ≠ 13) or reducibility through
non-trivial subgroups (12, 14, 15, 16 composite), or both.
`C_13` is unique in `[2, 16]` implementing D.1.

**Provenance.** Upgrades upstream T_MT_3 from Tier-2 to Tier-1.

**Status.** Proved.

**Used in.** `biology-rung-tubulin.tex §3`.

---

### R.1 (WO-3) — Conditional on T_PH_1

**Statement.** T.1 and T.2 are conditional on the 13-adjacency
hypothesis T_PH_1 (upstream Tier-2). Mathematically the theorems
stand independently; biological applicability depends on T_PH_1.

**Status.** Remark.

---

### R.2 (WO-3) — In-vitro polymorphs

**Statement.** Non-13 protofilament counts observed in non-
physiological tubulin assembly conditions are compatible with the
theorem: the cascade selector applies in cellular environments
where T_PH_1 is operative, not in arbitrary in-vitro conditions.

**Status.** Remark.

---

### C.1 (WO-3) — Taxane binding pocket preserves C_13

**Statement.** Therapeutically effective taxanes bind in a
configuration preserving `C_13` modal indecomposability;
resistance-conferring mutations shift pocket geometry so the
bound drug breaks `C_13` indecomposability.

**Provenance.** New conjecture with direct cancer-chemotherapy
relevance.

**Status.** Conjecture; empirical test planned.

**Used in.** `biology-rung-tubulin.tex §4`.

---

### C.2 (WO-3) — Helical pitch from H_4 Coxeter geometry (T_MT_4)

**Statement.** 13-protofilament B-lattice helical pitch fixed
by `H_4` Coxeter angle `π/5` or φ-multiple, via shared
φ-helical-closure-orbit machinery with WO-2.

**Provenance.** Imports upstream T_MT_4
(`cascade-photon-microtubule-alpha-programme.md §2`).

**Status.** Conjecture.

---

### C.3 (WO-3) — Anesthetic mode disabling (T_MT_5)

**Statement.** Different anesthetic classes disable different
subsets of the 13 `C_13` modes.

**Provenance.** Imports upstream T_MT_5.

**Status.** Speculative.

---

### N.1 (WO-3) — B_hnb: 600-cell vertex graph is 12-regular

**Statement.** Every vertex of the 600-cell has exactly 12
nearest neighbours; consequently `|N[v]| = 13` for every vertex
`v`. Nearest-neighbour squared distance is
`2 − (1 + √5)/2 ≈ 0.381966 = 1/φ²` (which is also `λ_1` of the
cell-graph Laplacian — see WO-4 N.2 for the connection).

**Provenance.** Sim-verified by direct enumeration in
`scripts/wo3_sim_close_microtubule.py`: all 120 vertices tested,
degree distribution `{12: 120}`, no variance.

**Status.** Sim-verified (Route K foundation established).

**Used in.** `biology-rung-tubulin.tex §2.1`.

---

### N.2 (WO-3) — B_pfcount_exclusion: 13 is unique at H_4

**Statement.** Vertex-graph degree comparison across candidate
four-polytope substrates:
- 600-cell (H_4): degree 12, |N[v]| = 13 ← match
- 120-cell (H_4 dual): degree 4, |N[v]| = 5
- 24-cell (F_4): degree 8, |N[v]| = 9
- 16-cell (D_4): degree 6, |N[v]| = 7
- 8-cell / tesseract (B_4): degree 4, |N[v]| = 5

The 600-cell is the **unique** H_4-adjacent four-polytope
providing a 13-element closed neighborhood. Under (H-MT), the
13-protofilament count is forced by substrate choice.

**Status.** Sim-verified (candidate-by-candidate enumeration).

**Used in.** `biology-rung-tubulin.tex §2.1`.

---

### N.3 (WO-3) — B_3start: 13 prime ⇒ all starts equidistribute

**Statement.** For a cylinder with `n_pf = 13` protofilaments, every
`k`-start helix (k ∈ {1, …, 12}) equidistributes (visits all 13
positions before returning), because `gcd(k, 13) = 1` for every
non-trivial `k`. For composite `n_pf = 12` only 4 starts
equidistribute (k ∈ {1, 5, 7, 11}); the other 7 fail. This is the
direct geometric reason 13-protofilament lattices host a cleaner
helical addressing structure than 12-protofilament lattices.

**Status.** Sim-verified (gcd enumeration).

**Used in.** `biology-rung-tubulin.tex §2.1`; supports T.2
Theorem on non-13 counts geometrically.

---

### N.4 (WO-3, partial) — B_lattice_pitch: partial

**Statement.** A naive model (3-start helix on 13 protofilaments
at fixed axial rise 9.2 Å and tube radius 125 Å) computes pitch
angle 2.9° from vertical; observed microtubule B-lattice pitch
is ~10°. The mismatch indicates the naive cylinder-helix model
does not capture the B-lattice's true geometry (which involves
lateral protofilament offset, not a pure axial-azimuthal helix).
Full derivation of the B-lattice pitch from cascade geometry
remains open.

**Status.** Partial / open; documents the specific mismatch for
future closure (build B_lattice_pitch_v2).

---

## WO-5 — Phyllotaxis and the integer-137 coincidence

### D.1 (WO-5) — Phyllotaxis divergence angle

**Statement.** The phyllotaxis divergence angle
`θ_phyllo ∈ [0°, 360°]` is the angular spacing between successive
primordia in a Fibonacci-type phyllotactic arrangement, as observed
empirically across several hundred plant species.

**Provenance.** Classical phyllotaxis (Airy 1873, Schwendener 1878,
Jean 1994 survey); import into this programme as the cell-level
complement to WO-1's face-level T-number operator.

**Status.** Definition.

**Used in.** `papers/biology-rung-phyllotaxis/biology-rung-phyllotaxis.tex §3`.

**Planned paper.** Phyllotaxis paper (biology-rung paper 2).

---

### Prop (WO-5) — Three-distance theorem / optimal aperiodic pitch

**Statement.** Among aperiodic rotations `θ ∈ (0°, 360°)`, the
``most irrational'' pitch (with continued-fraction expansion all
1's) is `θ = 360°·(φ − 1) = 360°/φ² = 360°·(1 − 1/φ)`.

**Provenance.** Classical (Coxeter 1953; Vogel 1979; Sós 1958;
Świerczkowski 1958).

**Status.** Proved (classical).

**Used in.** `biology-rung-phyllotaxis.tex §3`.

---

### T.1 (WO-5) — Cascade golden-angle theorem

**Statement.** On the 600-cell 5-fold axial decagram substrate
(`cascade-bio.md §5.1`, B2 result), the per-primordium axial
rotation compatible with Fibonacci-parastichy closure across
iterated 2I actions is uniquely `θ_phyllo = 360°/φ² ≈ 137.5077640°`.

**Provenance.** VFD-specific re-derivation of the classical
Coxeter–Vogel result; cascade-specific content is that φ enters
structurally via axiom F1 rather than as a post-hoc fit, and the
decagram orbit provides the axial substrate.

**Status.** Proved (by combining cascade B2 result with classical
three-distance / continued-fraction selection).

**Used in.** `biology-rung-phyllotaxis.tex §3`.

**Planned paper.** Phyllotaxis paper.

---

### R.1 (WO-5) — Integer-137 shared, fractional parts not

**Statement.** `⌊α⁻¹⌋ = ⌊θ_phyllo⌋ = 137` is a structurally shared
cascade signature: both quantities extract a value near 137 from
φ-driven 600-cell geometry at different rungs (vertex spectrum for
α⁻¹; cell-level spherical packing for θ_phyllo). The fractional
parts (0.036 via π/87 vs. 0.508 via 360/φ² − 137) are **not**
related by any clean cascade-only formula; candidate expressions
(ln φ, small multiples of π/87, 1/φ^k, π-times-small-numbers) all
fail to match Δ ≈ 0.4717 to better than ~5%.

**Provenance.** Upstream `cascade-bio.md §B6.1–B6.2`, consolidated
into this paper.

**Status.** Remark / consolidated finding.

**Used in.** `biology-rung-phyllotaxis.tex §4`.

---

### N.1 (WO-5) — Numerical table of Δ candidates

**Statement.** `scripts/phyllotaxis_alpha_check.py` (upstream at
`papers/cascade-derivation/scripts/`) tabulates candidate cascade
expressions for `Δ = θ_phyllo − α⁻¹ ≈ 0.4716538`. None match to
better than ~5%. Closest structural candidate is `13·π/87 ≈
0.469433` (at 0.5% distance), with 13 a Fibonacci number — flagged
as suggestive but not quantitatively decisive.

**Status.** Computational (present).

**Used in.** `biology-rung-phyllotaxis.tex §4 Table 1`.

---

## WO-4 — Bioelectric morphogenetic attractors (Levin)

### D.1 (WO-4) — Cell graph $\mathcal{G}$

**Statement.** `𝒢 = (V, E)` with `V` = the 600 tetrahedral cells
of the 600-cell, `E` = face-sharing adjacencies (two cells share
exactly 3 vertices). Graph is 4-regular, 1200 edges.

**Status.** Proved (construction + verification in
`scripts/wo4_sim_close_laplacian.py`).

**Used in.** `biology-rung-bioelectric.tex §2, §3`.

**Planned paper.** Bioelectric paper (biology-rung paper 4).

---

### N.1 (WO-4) — B_orbits: 2I acts freely on cells

**Statement.** The action of the binary icosahedral group 2I on
the 600 cells of `𝒢` by left quaternion multiplication is FREE:
every non-identity element fixes no cell. Orbit count is exactly
5, orbit sizes are all 120 (`600 = 5 × 120`).

**Provenance.** Sim-verified by direct enumeration in
`scripts/wo4_sim_close_orbits.py`. No counting-argument shortcut
— all 120 × 600 = 72 000 actions computed via quaternion
multiplication + vertex-matching, then orbit BFS.

**Status.** Sim-verified (computational certificate).

**Used in.** `biology-rung-bioelectric.tex §2`.

---

### N.2 (WO-4) — B_laplacian: cell-graph Laplacian spectrum

**Statement.** The 600-cell cell-graph Laplacian `L = D − A` on
`𝒢` has 27 distinct eigenvalues. The first six eigenvalue
multiplicities are `(1, 4, 9, 16, 25, 36) = (1², 2², 3², 4², 5², 6²)`,
exactly the squared dimensions of the first six 2I irreps
`{1, 2, 3, 4, 5, 6}`. Per-eigenspace `χ(−e)` values alternate
`+1, −4, +9, −16, +25, −36`, matching integer-spin / half-integer-
spin parity of the first 6 irreps.

**Provenance.** `scripts/wo4_sim_close_laplacian.py`: full
600 × 600 Laplacian diagonalisation via numpy; 2I perm-rep
characters via direct trace over eigenspaces.

**Status.** Sim-verified (multiplicity + character-parity
structure). Full per-eigenspace decomposition into specific
(labelled) 2I irreps is pending independent character-projection
audit.

**Used in.** `biology-rung-bioelectric.tex §3, §4`.

---

### C.1 (WO-4) — Morphogenetic attractors at 2I-irrep level

**Statement.** Morphologically admissible bioelectric prepatterns
are low-lying eigenmodes of the cascade closure-Laplacian on the
2I cell-graph, classified by 2I (NOT A_5) irrep content — the
central element `−e` acts non-trivially on cells
(B_orbits verified free action), so there is no descent to A_5.
Attractor count is bounded by the 9 distinct 2I irreps, not 5.

**Status.** Conjecture with sim-verified spectral support
(N.1, N.2).

---

### C.2 (WO-4) — Specific low-mode phenotype assignments

**Statement.** The first six low-lying Laplacian modes, in the
pattern `(dim 1, 2, 3, 4, 5, 6)`, are conjectured to correspond
to specific morphological attractor families. Concrete assignments
(double-head, electric face, etc.) require the full per-eigenspace
2I-irrep labelling, which is deferred to a follow-up sim-audit.

**Status.** Conjecture, pending build B_modes_full per codex-5.5
gap report.

---

### C.3 (WO-4) — Forbidden-pattern falsifier

**Statement.** Bioelectric prepatterns whose 2I-irrep content
does not overlap any low-lying Laplacian eigenspace should fail
to produce a viable morphological outcome when induced
experimentally.

**Status.** Conjecture; testable against Levin-group protocols.

---

## Cross-WO / shared machinery

*(empty — entries shared across WOs land here if/when they arise)*
