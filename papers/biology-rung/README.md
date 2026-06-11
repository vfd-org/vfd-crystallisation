# Biology-Rung Programme

**Status:** Active, WO-1 in derivation
**Date opened:** 2026-04-22
**Classification:** Cascade Life-rung consolidation → falsifiable biology predictions
**Priority:** High — first biology-rung work orders, opens a whole new prediction surface

---

## 1. Why This Programme Exists

The cascade `E8 → ... → Life (icos 40) → ...` identifies the Life
rung with the binary icosahedral group `2I` acting on the 600-cell
cell-level substrate (see `papers/cascade-derivation/cascade-bio.md`).
The rung is real: `2I` is verified as the 600-cell vertex set,
`I ≅ A_5` is the quotient, and the 40 = 8 × 5 arithmetic of Hopf
cell-fibres is established (B1, complete).

**But the downstream predictions are mostly open.** The B2–B6 sub-
phases (helical orbits, Caspar–Klug T-numbers beyond the A_5 match,
DNA pitch, chirality quantitation, phyllotaxis ↔ α) are listed as
"Pending" or "honest partial." No biology-rung paper exists.

This programme closes that gap by running three work orders, each
producing a concrete, quickly-falsifiable biology prediction from the
existing cascade machinery, with every new definition/lemma/
conjecture logged in `math-catalogue.md` so the eventual papers are
traceable.

---

## 2. Scope

Six work orders (five derivation + one cross-reference), one umbrella
directory, one ledger, five eventual papers:

| WO | Target | Disease relevance | First-order falsifier |
|---|---|---|---|
| **WO-1** | Caspar–Klug T-number spectrum from a single cascade operator | none (foundation) | VIPERdb capsid histogram |
| **WO-2** | Cross-β amyloid fibril twist from φ-helical 2I orbits | type 2 diabetes (IAPP), Alzheimer's (Aβ, tau), Parkinson's (α-syn), cancer (p53 aggregation) | Amyloid Atlas / cryo-EM fibril twist database |
| **WO-3** | Tubulin 13-protofilament + taxane binding from C₁₃ irrep (incl. PDB / EMDB empirical comparison) | cancer chemotherapy | PDB tubulin-taxane complexes, cryo-EM dimer spacings |
| **WO-4** | Planarian bioelectric prepattern eigenmodes on the 2I-orbit cell graph | tissue regeneration, wound healing, axolotl limb regrowth; speculatively cancer (bioelectric disruption) | Levin group regeneration data (planarians, Xenopus "electric face") |
| **WO-5** | Fibonacci phyllotaxis angles from φ-helical closure orbits; relation to α⁻¹ = 137 + π/87 | none (foundation / plant morphogenesis) | Measured divergence angles in sunflowers, pinecones, Romanesco |
| **WO-6** | Cross-reference to aria-chess brain-mapping programme | DMN / EEG / cortical dynamics live there, not here | Housekeeping WO, no derivation |

Scope note: DMN / EEG / cortical-dynamics empirical work lives in
the sibling **aria-chess** programme (15/18 preregistered hits,
manuscript ready). WO-6 is the explicit pointer so biology-rung
readers know where adult-brain empirical neuroscience sits; see
`WO-BIOLOGY-RUNG-006-DMN-BRIDGE.md`.

WO-1 is the foundation: it settles an existing open item (B3 "full T
from one operator") and fixes a subtle issue in the current partial
derivation (T=5 is listed as an A_5-irrep-matched T-number but is not
Loeschian). WO-2 is the public-facing prediction with the most
disease-relevance. WO-3 is stretch.

---

## 3. How We Work

### 3.1 Work-order cycle

Each WO follows the same loop:

1. **Spec** — `WO-BIOLOGY-RUNG-NNN-<slug>.md` states goal,
   acceptance criteria, open items, deliverables.
2. **Derivation** — mathematical extension of the existing cascade
   machinery, drafted as `derivation-<slug>.md` (becomes a paper
   skeleton later).
3. **Catalogue** — every new definition, lemma, theorem, conjecture
   added to `math-catalogue.md` with provenance and status.
4. **Sim** — Python implementation under `scripts/`, data under
   `data/`.
5. **Codex review** — `bash scripts/review_wo.sh <wo-path> --focus
   "..." < /dev/null` lands a report in
   `docs/reviews/biology-rung-<slug>-<ts>.md`.
6. **Iterate** until codex returns *publication ready* on the
   substantive-math/attribution scope. Then move to next WO.

### 3.2 Voice

Per `docs/revision-protocol.md`: Recovery Manifest voice, surgical
edits, no wholesale rewrites once converged.

### 3.3 Acceptance

A WO is done when:

- Derivation is codex-clean on claim-audit and external-consistency.
- Sim runs, produces a prediction artifact under `data/`.
- The prediction has been compared against a public dataset and the
  result is recorded (hit, partial, miss — all are valid outcomes as
  long as the comparison is honest).
- `math-catalogue.md` lists every new entry the WO introduced.

### 3.4 Eventual paper layout

Each WO becomes a standalone paper on the programme index. The
umbrella is NOT a single paper — keeping them separate maximises
citation surface and lets each result stand or fall on its own.
Planned targets (numbering TBD when written):

- **Paper on capsid T-numbers** — extends `cascade-bio.md §B3`
- **Paper on amyloid twist from 2I orbits** — closes `cascade-bio.md §B2`
- **Paper on microtubule C₁₃ and taxane binding** — extends
  `papers/cascade-derivation/cascade-photon-microtubule-alpha-programme.md`

---

## 4. Files

| File | Purpose |
|---|---|
| `README.md` | This file |
| `math-catalogue.md` | Ledger of new definitions/lemmas/theorems/conjectures with provenance |
| `WO-BIOLOGY-RUNG-001-CAPSID.md` | WO-1 spec |
| `WO-BIOLOGY-RUNG-002-AMYLOID.md` | WO-2 spec (stub until WO-1 lands) |
| `WO-BIOLOGY-RUNG-003-TUBULIN.md` | WO-3 spec (stretch, stub) |
| `WO-BIOLOGY-RUNG-004-BIOELECTRIC.md` | WO-4 spec (Levin planarian, stub) |
| `WO-BIOLOGY-RUNG-005-PHYLLOTAXIS.md` | WO-5 spec (Fibonacci angles + α⁻¹ bridge, stub) |
| `WO-BIOLOGY-RUNG-006-DMN-BRIDGE.md` | WO-6 cross-reference to aria-chess (permanent pointer) |
| `derivation-capsid.md` | WO-1 derivation (in progress) |
| `scripts/` | Python sims per WO |
| `data/` | Prediction artifacts + fetched comparison datasets |

---

## 5. Cross-References

Upstream cascade machinery this programme depends on:

- `papers/cascade-derivation/cascade-bio.md` (Life-rung substrate, B1–B6 plan)
- `papers/cascade-derivation/cascade-foundations.md` (F2 closure functional)
- `papers/paper-xxxii/paper-xxxii.tex` (600-cell closure + coherence
  spectrum, the existing worked example of a closure operator on this
  substrate)
- `papers/cascade-derivation/cascade-genetic-code.md` (sister biology
  thread, gene code ↔ icosahedral faces)
- `papers/cascade-derivation/cascade-photon-microtubule-alpha-programme.md` (WO-3 prerequisite)
