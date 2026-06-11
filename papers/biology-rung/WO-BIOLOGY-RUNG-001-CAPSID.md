# WO-BIOLOGY-RUNG-001-CAPSID: Caspar–Klug T-numbers from a Single Cascade Operator

**Status:** Active, derivation in progress
**Date opened:** 2026-04-23
**Classification:** Biology-rung cascade extension + falsifiable capsid prediction
**Priority:** High — foundation WO, closes an existing open gap in `cascade-bio.md §B3`

---

## 1. Executive Summary

`cascade-bio.md §B3` establishes that the four smallest viral capsid
T-numbers match the dimensions of the four non-trivial irreducible
representations of `A_5`, and that `T = 2` (not a Loeschian number)
is absent exactly because `A_5` has no two-dimensional irreducible
representation. But §B3 itself flags two open items:

1. **"Full derivation of all T-numbers from one cascade operator"** —
   listed as `✗ open` (line 320). Current status: small T from
   `A_5` irreps, higher T ceded to classical Eisenstein arithmetic.
2. **`T = 5` is listed as a valid T-number** matched to the 5-dim
   `A_5` irrep (line 283), but `5` is **not** a Loeschian number
   (no integers `h, k` satisfy `h² + hk + k² = 5`). Either the
   match is off by one / misaligned, or the cascade is implicitly
   *predicting* `T = 5` capsids despite classical forbiddenness.

This WO closes both. We construct a single **face-level** cascade
operator `𝒯_casc` on the Eisenstein lattice `ℤ[ω]` whose spectrum
is exactly the Caspar–Klug Loeschian sequence, give a principled
reading of the small-T / A_5-irrep match, and settle the T=5
question. The open question of whether `𝒯_casc` descends from a
cell-level Paper XXXII construction is flagged as an explicit open
problem. The sim then compares the predicted T-number distribution
against VIPERdb (~1000+ solved capsids, public).

---

## 2. Goals

### 2.1 Primary (must)

1. **Define** a cascade closure operator `𝒯_casc` at the
   **face level** on the Eisenstein lattice `ℤ[ω]`, such that
   `spec(𝒯_casc) = Loeschian numbers` (= Caspar–Klug T-numbers).
2. **Prove uniqueness** of `𝒯_casc` up to positive scale under
   the hexagonal-lattice `C_6` invariance local to each face.
3. **State** the cell-level extension (whether `𝒯_casc` descends
   from a 600-cell Paper XXXII closure construction) explicitly
   as an open problem, with a concrete plan of attack rather than
   an implicit conjecture.
4. **Resolve the small-T / A_5-irrep question**: show either (a)
   it reduces correctly to `{1, 3, 4}` with `T=5` excluded, or
   (b) give a cascade reason for T=5 to appear despite Loeschian
   forbiddenness. No hand-waving.
5. **Rank / weight** predicted T-numbers by a closure-preference
   measure (not all spec elements equally likely).
6. **Run the sim**: enumerate (h,k), compute T, compute closure
   weight, emit prediction artefact in `data/`.
7. **Compare** against VIPERdb empirical capsid T-distribution.
   Report hit/partial/miss with effect size (χ² vs. uniform-over-
   Loeschian baseline and vs. Goldberg-Coxeter permitted baseline).

### 2.2 Secondary (should)

8. **Chirality**: Caspar–Klug has laevo/dextro pairs at T=7, 13,
   19, … (when `h ≠ k` and both nonzero). Predict whether 2I
   handedness biases the observed laevo/dextro ratio in VIPERdb.
9. **Explicit comparison** of `𝒯_casc` against the existing
   600-cell closure functional `F` of Paper XXXII. State whether
   `𝒯_casc` is a face-level residue of `F` (or of the field-level
   form from `cascade-foundations.md §F2`) or a genuinely new
   construction. This is the open problem of goal 3.

### 2.3 Non-goals

- Dynamical capsid assembly — we predict the discrete T-set, not
  assembly kinetics.
- Non-icosahedral capsids (T=1 prolate, helical rod viruses) — out of
  scope; the framework is about icosahedral closure.

---

## 3. Existing Framework We Extend

| Piece | Where | What we use |
|---|---|---|
| 2I / A_5 substrate on 600-cell | `cascade-bio.md §2.1–2.3` | verified A_5 irrep table (dims 1,3,3',4,5; Σdim² = 60) |
| Cell-level biology claim | `cascade-bio.md §3.1` | "biology lives at the cell (3-volume) level" |
| Closure functional F (soft-min uniqueness) | `paper-xxxii/paper-xxxii.tex §4`, Theorem F (~L363) | log-sum-exp closure functional from axioms A1–A3 |
| 600-cell selection | `paper-xxxii/paper-xxxii.tex §3`, Theorem `thm:600cell` (~L237) | `(H1)–(H4)` → `G = 2I`, 120-vertex 600-cell |
| F2 closure functional form | `cascade-derivation/cascade-foundations.md §F2` (~L91) | `F = αR + βE − γQ` density under locality / invariance / order-≤2 / scalar axioms |
| Eisenstein norm form T | `cascade-bio.md §B3.1` | `T = |h + kω|²`, ω = e^(2πi/3) |
| A_5 irrep dimensions match | `cascade-bio.md §B3.2` | current partial result: T ∈ {1,3,4,?5} ↔ irrep dims |

New mathematical objects required (to catalogue):

- **D.1** Icosahedral-invariant Eisenstein sublattice `Λ_2I ⊂ Z[ω]`
  on the cell-level substrate
- **D.2** Cascade T-operator `𝒯_casc : Λ_2I → ℕ`
- **L.1** Spectrum identity: `spec(𝒯_casc) = Loeschian numbers`
- **L.2** Small-T resolution: what the A_5-irrep match is actually
  saying, stated without the T=5 ambiguity
- **C.1** Closure-preference weighting: predicted empirical T
  distribution as `w(T) ∝ <something from 2I orbit structure>`
- **N.1** Computational verification of L.1 up to T ≤ N (some
  specific cutoff)
- **N.2** VIPERdb χ² and KL results

---

## 4. Open Items / Risks

| # | Issue | Resolution plan |
|---|---|---|
| O1 | Is `𝒯_casc` a restriction of `F` (Paper XXXII) or a new object? | Answer in §2.2 of derivation explicitly; if new, give a "no-hidden-duplication" argument. |
| O2 | T=5 forbidden classically but matched to A_5 5-dim irrep — which is right? | Derivation must produce one of: (a) small-T match is `{1, 3, 4}` only, (b) T=5 is a cascade-predicted excess, (c) the "5" in the match refers to a different invariant than the Eisenstein norm. |
| O3 | 2I vs A_5 — both appear; is the cell-level operator 2I-equivariant (double cover) or A_5-equivariant? | Specify explicitly and justify from `cascade-bio.md §2.2`. |
| O4 | Laevo/dextro chirality weighting | May be a 2I vs A_5 feature; secondary goal. |
| O5 | VIPERdb coverage bias — some T's are over-represented due to database curation, not biology | Report both raw VIPERdb and a de-biased version if we can obtain a species-weighted count. |

---

## 5. Deliverables

- `derivation-capsid.md` — mathematical derivation, reviewable by
  codex as a standalone doc.
- `math-catalogue.md` updates — all new D/L/T/C/N entries for WO-1.
- `scripts/wo1_capsid_predict.py` — enumerate (h,k), compute
  `𝒯_casc` and closure weight, emit `data/wo1_prediction.csv`.
- `scripts/wo1_viperdb_fetch.py` — pull T-number distribution from
  VIPERdb, emit `data/wo1_viperdb_observed.csv`.
- `scripts/wo1_compare.py` — χ² and KL against predicted
  distribution, emit `data/wo1_comparison.md`.
- `docs/reviews/biology-rung-capsid-<ts>.md` — codex review
  reports (one per round).

---

## 6. Acceptance Criteria

1. `derivation-capsid.md` passes codex review: "Publication ready:
   yes" on substantive-math/attribution scope.
2. `math-catalogue.md` lists every D/L/T/C/N introduced, each with
   provenance and status filled in.
3. Sim runs end-to-end: prediction → VIPERdb fetch → comparison.
4. Comparison result is recorded honestly — we will take either a
   hit, a partial (some T's match, some don't), or a miss as a valid
   outcome. A miss means the framework's current B3 partial was
   over-reaching and we report accordingly.
5. T=5 question is settled explicitly.

---

## 7. Codex Review Invocation

```
bash scripts/review_wo.sh papers/biology-rung/WO-BIOLOGY-RUNG-001-CAPSID.md \
  --derivation papers/biology-rung/derivation-capsid.md \
  --focus "Round N: verify (a) D.1 and D.2 are well-defined, (b) spec(𝒯_casc) = Loeschian numbers proof is complete, (c) T=5 question is settled, (d) attributions to cascade-bio.md / paper-xxxii / foundations.tex match the cited sources. Publication ready? yes/no on substantive math."
```

---

## 8. Status Log

- 2026-04-23: WO opened. Derivation started.
