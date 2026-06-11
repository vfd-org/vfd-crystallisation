# V_600 Programme — Master Narrative

**Scope of this document:** the *set* of papers that ship the V_600 + Dic_5 + τ_σ results, the order they appear in, the dependencies between them, and what each one claims and explicitly does not claim.

**Strategic principle (per credibility-bar lesson):** start with the smallest undismissable claim, build outward only as each prior paper lands. The arc must stand even if any single paper is read in isolation.

---

## The arc

```
        ┌──────────────────────────────────────────────────────┐
        │  Paper 1.  Bekenstein 1/4 from V_600 incidence       │
        │  (LEAD: pure finite-group identity, no physics)      │
        └──────────────────────────────────────────────────────┘
                              │
                              │ establishes V_600 + Dic_5 + V₂₄ as
                              │ a legitimate object of study
                              ▼
        ┌──────────────────────────────────────────────────────┐
        │  Paper 2.  Discrete Hawking quantum on V_600         │
        │  (single-line σ-pair spectrum, PBH prediction)       │
        └──────────────────────────────────────────────────────┘
                              │
                              │ shifts from static incidence to
                              │ dynamical σ-pair excitation
                              ▼
        ┌──────────────────────────────────────────────────────┐
        │  Paper 3.  The τ_σ involution and Dic_5-coset duality│
        │  (pure construction paper, no physics claim)         │
        └──────────────────────────────────────────────────────┘
                              │
                              │ provides the involution Papers 4-5 need
                              ▼
        ┌──────────────────────────────────────────────────────┐
        │  Paper 4.  Operator-trace ratios 13/12 and 11/12     │
        │  on the V_600 K-saturated diagonal projector algebra │
        │  (Layer 1 trace identities + admissibility theorem;  │
        │   Layer 2 H_0 / S_8 numerical observation;           │
        │   Layer 3 cycle-mode coupling hypothesis Γ — NOT     │
        │   a theorem)                                          │
        └──────────────────────────────────────────────────────┘
                              │
                              │ structural-spine factorisation
                              │ (Paper 4 Layer 1 only)
                              ▼
        ┌──────────────────────────────────────────────────────┐
        │  Paper 5.  Unified V_600 scaffolding                 │
        │  (synthesis: four theorem imports factor through     │
        │   Σ_{V_600}; CMB-bulk projection, cosmic dipole      │
        │   audit, prediction manifests are out-of-scope       │
        │   future builds)                                      │
        └──────────────────────────────────────────────────────┘
```

Five papers. The dependency arrows are one-way; each paper cites the prior ones but can be read alone.

---

## Why five (not one, not ten)

**Why not one big paper.** Bundling H_0 + σ_8 + BH + Hawking + CMB triggers credibility-bar rejection at the abstract. Five Nobel-tier claims in one document gets dismissed regardless of math. (This is the lesson from `feedback_credibility_bar.md`.)

**Why not ten papers.** The σ_8 result is the same machinery as H_0 — splitting them is artificial bulk. The CMB mapping is qualitative and only earns its keep as the synthesis chapter of the unified paper. Five is the minimum that makes each paper undismissable.

**Why this order.** Each paper's prerequisites are strictly the prior papers'. Paper 1 needs only group theory. Paper 2 adds σ-pair structure. Paper 3 adds the involution. Paper 4 needs Paper 3. Paper 5 cites all four.

---

## Per-paper one-liner

| # | Title | Single claim | Pages | Risk |
|---|---|---|---|---|
| 1 | *Bekenstein 1/4 as exact incidence on the 600-cell* | 4 σ-fixed / 16 σ-mobile per Dic_5-coset = 1/4 | 12 | Low — pure arithmetic |
| 2 | *A discrete Hawking quantum from σ-pair excitations on V_600* | All σ-mobile vertices have identical |v−σ(v)|² ⇒ single-line spectrum E_q = 5/2 | 10 | Low–Medium — interpretation contested |
| 3 | *The τ_σ involution: a canonical Galois-coset duality on the binary icosahedral group* | Explicit construction; involution; fixes Dic_5; swaps K=52 ↔ K=20 within each non-bulk right coset; Z_2^5 = 32 phase ambiguity | 14 | Low — construction paper |
| 4 | *Two operator-trace ratios from V_600 K-class structure: 13/12 and 11/12, and their match to the H_0 and S_8 benchmarks* | Layer 1: tr(I_C + P_72)/12 = 13/12 and tr(I_C − P_0)/12 = 11/12 + K-saturated admissibility theorem. Layer 2: numerical match to SH0ES and KiDS S_8. Layer 3: cycle-mode coupling hypothesis Γ (NOT a theorem). | 14 | Medium — Layer-3 hypothesis is explicit |
| 5 | *A unified V_600 scaffolding for the four foundation theorems* | Synthesis: structural-spine tuple Σ_{V_600}; the four imported theorems (Paper 4 restricted to Layer 1) all factor through it. CMB-bulk projection / cosmic dipole / prediction manifest are out-of-scope future builds. | 14 | Medium — math-scaffolding only, no new physics claim |

Total: ~74 pages of paper, derived from one 120-vertex group.

---

## Per-paper SCOPE structure

Each paper gets its own `SCOPE.md` at `papers/<name>/SCOPE.md`, with this template:

1. **Working title + one-sentence pitch**
2. **Why this paper, why now** (placement in the arc)
3. **What's IN scope** (numbered, ≤ 7 items)
4. **What's explicitly OUT of scope** (numbered, ≤ 7 items)
5. **Section structure** (target page count per section)
6. **The undismissable spine** (one-paragraph summary of the abstract-level claim)
7. **Risk register** (table: hook → mitigation)
8. **Files inherited** from prior work
9. **Open scoping questions** before drafting

Each scope doc is < 5 pages. It is the first thing to land for that paper, and the last thing reviewed before LaTeX begins.

---

## Narrative through-line

A reviewer reading the five-paper set in order should perceive this arc:

> *Paper 1.* Here is a finite-group identity — 4/16 = 1/4 — that exactly reproduces the Bekenstein–Hawking entropy coefficient. We don't claim to have derived black-hole physics; we report a structural ratio.
>
> *Paper 2.* Within the same group structure, the σ-Galois pair-excitation spectrum is a single delta function. This is unusual. It suggests the discrete cascade limit of Hawking radiation is monochromatic, with a falsifiable PBH evaporation cutoff.
>
> *Paper 3.* The same group admits a canonical involution τ_σ that exchanges the two K-classes in each non-bulk coset. This is a construction, not a physics claim — but it gives the structure additional symmetry that's needed for downstream work.
>
> *Paper 4.* On the K-saturated diagonal projector algebra of V_600's 12-dimensional cycle space, the rank-1 corrections to the identity P_72 and P_0 yield the exact rational trace ratios 13/12 and 11/12 (Layer 1 theorem). Numerically these match the SH0ES/Planck H_0 ratio to ≈0.06σ and the KiDS-1000 multi-probe / Planck S_8 ratio at ≈0.24σ directional residual (Layer 2 observation). The cycle-mode coupling rule that would upgrade the match to a derivation is stated as an explicit Layer-3 hypothesis, NOT a theorem.
>
> *Paper 5.* The four foundation theorems all factor through one finite tuple Σ_{V_600}. We record this as a structural observation, not as a unified physical theory. CMB-bulk projection, cosmic dipole audits, and pre-registered prediction manifests are explicitly named out-of-scope future builds.

By Paper 5, a hostile reader has already accepted Papers 1–4. The synthesis claim is bounded by what those papers establish.

---

## Cross-cutting concerns

### Scope language

Every paper must contain a marked, load-bearing **§Scope** section that states:

- What the paper claims is *exact and unconditional*.
- What requires interpretive choices (and what those choices are).
- What is explicitly Tier-2 / future work.

This is the credibility-bar discipline. Conditional claims must be marked as such.

### Empirical anchors

Each paper that touches an observable must state:

- The observable + its measured value with σ.
- The cascade prediction.
- The post-correction tension.
- A pre-registered falsification window if one applies.

Pre-registration is the key trust signal. We have it for SPHEREx / LSST / SKA / DESI-quasar / Euclid / eROSITA-DE (in `cosmological-folding-rate/dynamics/preregister_k.py`).

### Frame discipline

Per `feedback_mathematical_framing_discipline.md`:
- Math sections are mathematical only.
- Interpretive framing goes in a clearly-marked closing subsection.
- The math doesn't lean on the interpretation.

### Dependency tracking

The five papers cite each other in strict dependency order:
- Papers 2, 3, 4, 5 cite Paper 1.
- Papers 4, 5 cite Paper 3.
- Paper 5 cites Papers 2, 4.

No back-citation. Nothing in Paper 1 depends on later work. This is enforceable: if we ever need to reorder, it forces a real rewrite, not just a citation patch.

---

## Release strategy

Three options:

**A. Sequential.** Ship Paper 1, wait 4–8 weeks, ship Paper 2, etc.
- Pro: maximally cautious; each paper earns the next.
- Con: 6+ months total; loses momentum.

**B. Bundled-pair.** Ship Papers 1 + 2 together (BH + Hawking, both narrow), then Papers 3 + 4 (construction + cosmology), then Paper 5.
- Pro: faster; pairings are natural.
- Con: a pair is a small bundle but still bigger than one paper.

**C. Big-bang.** Post all five to arXiv on the same day, with Paper 5 as the entry point.
- Pro: maximally cohesive narrative; one citation for the whole programme.
- Con: hostile readers still see "five Nobel-tier claims" as one thing.

**Recommendation: A (sequential).** The credibility-bar lesson is the operating constraint. Paper 1 has to land before anything else is plausible. Once Paper 1 is cited or accepted somewhere, Paper 2 becomes much easier to read fairly.

---

## Open programme-level questions

1. **Author block.** Same as paper-xxxiii, or a narrower author line for Paper 1 specifically? (Narrower may help Paper 1 stand alone.)
2. **arXiv categories.** Paper 1 = math.GR + gr-qc; Paper 2 = gr-qc + hep-th; Papers 3 = math.GR; Paper 4 = astro-ph.CO; Paper 5 = astro-ph.CO + gr-qc.
3. **Shared notation file.** Ship a single `NOTATION.tex` that all five papers `\input`, so the V_600 / Dic_5 / σ / τ_σ symbols are identical across the set.
4. **Computational appendix.** Each paper has its own verification script. Should those scripts share a `vfd_v600` Python package? (Probably yes — DRY across five papers.)
5. **Pre-registration timing.** Paper 4 is the natural place to formalise the SPHEREx/LSST predictions. Should pre-registration be an arXiv-deposited timestamp before Paper 4 ships?

---

## What lands first

Three artifacts before any LaTeX is written:

1. **This document** (`papers/v600-programme/NARRATIVE.md`) — done.
2. **Per-paper SCOPE.md** for each of Papers 1–5 (Paper 1 already has one).
3. **A shared notation appendix** (`papers/v600-programme/NOTATION.tex`) defining the symbols used across the set.

Once those three are agreed, drafting begins with Paper 1.

---

## Files

- `papers/v600-programme/NARRATIVE.md` — this document.
- `papers/bekenstein-incidence/SCOPE.md` — Paper 1 scope (drafted).
- `papers/v600-hawking-quantum/SCOPE.md` — Paper 2 scope (TBD).
- `papers/tau-sigma-construction/SCOPE.md` — Paper 3 scope (TBD).
- `papers/v600-cosmic-tensions/SCOPE.md` — Paper 4 scope (TBD).
- `papers/v600-unified/SCOPE.md` — Paper 5 scope (TBD).
- `papers/v600-programme/NOTATION.tex` — shared symbols (TBD).
