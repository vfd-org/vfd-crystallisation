# TASK: Write the aria-chess publication-ready paper

**Date:** 2026-04-30.
**Bar:** Hostile-review-ready, no overclaim. Strong, confident paper backed by lots of empirical evidence. Per `feedback_credibility_bar.md`: "complete + undismissable" not "honest + conditional."
**Pair-programmer pattern:** codex_derive (this WO) → Claude implements → review_paper.sh hostile audit → iterate until codex says "Publication ready: yes."

---

## 1. Substrate (existing material to lift from)

**Empirical / methods content (paper-grade, ready to lift):**
- `docs/brain_mapping/MANUSCRIPT_V2.md` — 1245 lines, 11 sections, complete draft with abstract through conclusion. Already structurally close to publication; needs tex conversion and tightening.
- `docs/brain_mapping/PAPER_BASIS_2026-04-29.md` — 37 KB, paper-ready abstract + intro + methods + results
- `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md` — 6/6 v4 signature table, full per-signature documentation
- `docs/brain_mapping/P4_SYNERGY_FINDING.md` — N=20 deep-dive narrative + per-seed values + bootstrap
- `docs/brain_mapping/CROSS_DOMAIN_RESULTS.md` — chess + conversation + HCP results
- `docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md` — 18/18 prereg tally with thresholds
- `docs/brain_mapping/PREREG_H4_FINGERPRINT.md`, `PREREG_RUNG_OBSERVABLES.md` — frozen 2026-04-24 predictions
- `docs/brain_mapping/EMERGENCE_AUDIT.md` — what's hardcoded vs derived
- `docs/brain_mapping/REPRODUCIBILITY.md` — pipeline documentation

**Headline numbers (deterministic, regenerable from seed=42, seed range 32000-32019):**

| Result | Value | Source script | Wallclock |
|--------|-------|---------------|-----------|
| 6/6 v4 EEG signature table | 4 conditions × 6 signatures all pass | `demo_drug_sleep_v4.py` | ~30s |
| P4 C×P synergy (N=20) | +0.190 [+0.143, +0.239]; P(≤0)=0.0000 | `demo_p4_cxp_deep_dive.py` | ~28 min |
| 18/18 preregistered tally | All P1-P18 pass | `run_preregistered_validation.py` | ~18 min |
| HCP categorical separation | Degree-std 11.58σ, PR 79.78σ (n=1003) | Cascade pipeline | (deterministic) |
| Sleep-EDFx spindle α | 2.513 (real) ∈ ARIA CI | Sleep-EDFx public data + `run_baseline_for_eeg.py` | (cached) |
| Cascade-α three-way overlap | WAKE [1.82,2.86] ∩ EEG [2.50,2.86] ∩ ARIA prior [2.73,3.25] | Combined | (cached) |

**Validation persistence:** `~/.aria/preregistered_validation/results_1777466957.json` (Apr 29 13:49) is the 18/18 record.

**Theoretical anchors:**
- `BANOMALY-001/vfd-b-anomaly/paper/main.tex` — structural template (10 sections: intro, method, derivation, results, stress_tests, cross_dataset, cross_channel, discussion, limitations, conclusion).
- `vfd-crystalisation-paper/papers/adaptive-closure-transport/adaptive-closure-transport.tex` — ACT theory paper. The aria-chess paper is the **active-regime empirical companion** to ACT; ACT names ARIA as the candidate instantiation of the 4-tuple (Remark 7.1 / sec:aria).
- `vfd-crystalisation-paper/docs/aria-closure-kernel.md` — kernel-spine doc; aria-chess witnesses the active regime alongside b-anomaly's passive-regime witness.

---

## 2. Framing decision (load-bearing)

**Adopt the substrate-witness framing, NOT the ACT-selection-theorem-witness framing.**

The substrate-witness framing claims:
- A deterministic geometric substrate (600-cell under H₄ symmetry) reproduces 18 preregistered neuroscience predictions across multiple paradigms with NO fitted shape parameters.
- The claim is **not** that the substrate explains consciousness or that it's the unique solution.
- The claim is **not** that ACT's selection-theorem (Hypothesis 4.3) is empirically witnessed.
- The claim is: this geometry, with one parameter set, produces a specific quantitative correspondence with cortex.

Under this framing:
- Lyapunov V(W) is **not required** as a deliverable (would be required for ACT-selection-witness).
- 2I-equivariance check is **not required** (would be required for cascade-selection-witness).
- G-ablation is **nice-to-have** but the recovery-reversibility result already witnesses learning-rule idempotency.

The ACT bridge appears as a non-load-bearing closing subsection in §8, mapping ARIA to ACT's 4-tuple as a programme-positioned correspondence (per `feedback_mathematical_framing_discipline.md` rule).

---

## 3. Output structure

Mirror BANOMALY-001/vfd-b-anomaly/paper/ exactly:

```
aria-chess/
└── paper/
    ├── main.tex              # frontmatter + \include all sections + bibliography
    ├── README.md             # paper README mirroring b-anomaly README.md (headline result, table, statistical caveat, repro recipe)
    ├── references.bib        # bibtex entries
    ├── sections/
    │   ├── 01_introduction.tex
    │   ├── 02_method.tex
    │   ├── 03_substrate.tex          # the 600-cell + cascade decomposition + Green response
    │   ├── 04_consciousness_chain.tex # 4-layer chain
    │   ├── 05_results.tex            # 6/6 v4 + 18/18 + cascade-α match
    │   ├── 06_stress_tests.tex       # P4 N=20 + bootstrap + ablation matrix
    │   ├── 07_cross_domain.tex       # chess + conversation + HCP
    │   ├── 08_discussion.tex
    │   ├── 09_limitations.tex
    │   └── 10_conclusion.tex
    └── figures/                # placeholder for any figures (likely none in v1)
```

---

## 4. Section content blueprint

### §1 Introduction (target: 100-130 lines)
- The problem: consciousness theories typically fit (predictive coding, IIT, GNW). What if a substrate were group-theoretically forced and non-fittable?
- The geometry: H₄ Coxeter / 600-cell — biological motivation (icosahedral hippocampus, theta-gamma 11:1 ratio, etc.) but NOT a-priori derivation.
- What this paper tests (verbatim "what is tested / what is not claimed" pattern, mirror b-anomaly §1).
- Programme position: passive-regime witness for $C_\varphi$ in b-anomaly is the companion (one substrate, two empirical layers).

### §2 Method (target: 150-190 lines)
- Datasets: Sleep-EDFx (n=30/24), OpenNeuro ds005620 propofol (n=20), Zenodo ds003992359 DMT (n=29), ds004902 SD (n=35), HCP-YA S1200 (n=1003) — all public, cite DOIs.
- Substrate construction summary (full derivation in §3): 600-cell, H₄ acting transitively, 9 H₃-shells, 12-degree.
- Cascade event detection method.
- Power-law fit + bootstrap CI.
- Stimulus models for v4 (WAKE, SLEEP_N3, PROPOFOL, RECOVERY).
- Preregistration protocol (frozen 2026-04-18 / 2026-04-24, what was peeked / what was not — be honest about ordering).
- Reproducibility ledger (versions, seeds, deterministic).
- State-reset protocol — the homeostatic_reset(level=1.0) call, why mandatory, how P13 changed from -3pp to +40.6pp.

### §3 Substrate construction (target: 80-120 lines)
- 600-cell vertex set V_600, 720 edges, 12-regular, 9 H₃-shells {1,12,20,12,30,12,20,12,1}.
- H₄ Coxeter symmetry, transitivity, eigenvalue spectrum (12 mult 1; 6φ mult 4; 4φ mult 9; 3 mult 16; ...).
- Cascade rung decomposition E₈→H₄→40→D₄→16→8→0 (briefly, with reference to cascade-derivation programme).
- Green response operator $C_\varphi = L + \varphi^{-2} I$, programme-level definition (NOT load-bearing for the empirical claims; cite docs/aria-closure-kernel.md).
- Reference: ACT theory paper for the 4-tuple (M, L_M, W, R_hom) framing; aria's instantiation flagged as candidate per ACT Remark 7.1.

### §4 Consciousness chain (target: 80-120 lines)
- Recurrent loop: Cascade event detection feeding cascade-pressure ρ.
- Bounded-top-K (k=12) thresholding (matches degree).
- IIT integrated-information layer (Φ trajectory).
- Stream continuity layer.
- Phenomenal-field binding.
- All four layers derived from substrate; no fitted parameters.

### §5 Results (target: 200-280 lines)

**§5.1 Six v4 EEG signatures across 4 brain states**

Verbatim from MANUSCRIPT_V2 lines 661-677. Per-condition table:

| Cond | n_evt | α | 95% CI | R² | I_var | Φ_traj | cont |
| WAKE | 58 | 2.252 | [1.82, 2.86] | 0.956 | 2.18e-05 | 0.0008 | 0.943 |
| SLEEP_N3 | 111 | 3.250 | [2.44, 4.14] | 0.886 | 1.01e-05 | 0.0055 | 0.980 |
| PROPOFOL | 246 | 2.758 | [2.52, 3.09] | 0.931 | 5.37e-06 | 0.0003 | 0.877 |
| RECOVERY | 58 | 2.252 | [1.82, 2.86] | 0.956 | 2.18e-05 | 0.0008 | 0.943 |

Per-signature pass with explicit threshold + falsification gate.

**§5.2 18/18 preregistered validation tally**

Full table P1-P18 with threshold + result + dataset + verdict.

**§5.3 Cascade-α three-way overlap**

WAKE α [1.82, 2.86] ∩ real EEG α [2.50, 2.86] (Sleep-EDFx n=30) ∩ ARIA prior α [2.73, 3.25].

### §6 Stress tests (target: 120-180 lines)

**§6.1 P4 C×P deep-dive (the headline stress test)**

N=3→5→10→20 trend with per-seed values (19/20 positive); bootstrap CI [+0.143, +0.239]; P(≤0)=0.0000.

Architectural reading: C and P are STRONGLY coupled, not nearly-orthogonal as the original prereg implicitly assumed. Original "fail" was Type II underpower + seed-range bias.

**§6.2 16-condition 2⁴ ablation matrix**

Main effects + pairwise interactions.

**§6.3 Non-equilibrium homeostatic reset finding**

Conditions A/B/C/D (no homeostasis / periodic only / wake-decay only / dual). Both required.

### §7 Cross-domain (target: 120-160 lines)

**§7.1 Chess** — 5-fold CV 83.1%, LOO lift +40.6pp with reset, goldilocks peak n=25.
**§7.2 Conversation** — 87.5% raw, |lift| < 10pp (selective amplifier).
**§7.3 HCP categorical separation** — n=1003, degree-std 11.58σ, PR 79.78σ.

### §8 Discussion (target: 120-180 lines)

**§8.1 What's new** — substrate witness, no fitted parameters, 18/18 prereg, 4-state cross-paradigm.
**§8.2 Comparison to existing theories** — IIT, GNW, predictive coding (substrate ≠ alternative theory; substrate is what *any* theory needs).
**§8.3 Strong C×P coupling for biology** — implications.
**§8.4 Substrate as null reference** — HCP separation reading.
**§8.5 Programme position: ACT bridge (non-load-bearing)** — map to 4-tuple as candidate instantiation; explicitly defer Lyapunov / 2I-equivariance / edge-space lift to ACT open items.

### §9 Limitations (target: 120-180 lines)

Brutal honest scope. Apply b-anomaly §9 5-move template:

**Move 1 (regime clarity):** State that this is a substrate-witness paper; ACT-selection-theorem witness is NOT delivered.

**Move 2 (post-hoc structure verification):** P4 retest at N=20 was data-second (we saw N=3 fail first). Acknowledge ordering.

**Move 3 (interpretation alternatives):** Three readings — (a) substrate is real-physics, (b) H₄ is structurally right, (c) data is rank-1 in any group-theoretic substrate. Adopt (c) as conservative.

**Move 4 (test vs claim boundary):** Universality + cross-paradigm consistency PASS; ACT-active-regime selection-theorem witness NOT claimed.

**Move 5 (substrate state-drift acknowledged):** Polytope state-drift (P13 fail mode without reset) explicitly disclosed; reset protocol mandatory in repro pipeline.

Plus enumerated per-section limits:
- 8.1 Substrate-level (600-cell only tested; no comparison to 24-cell, 120-cell)
- 8.2 Consciousness chain (single-seed determinism, stylised stimuli)
- 8.3 Cross-domain (small test sets, single parcellation)
- 8.4 Preregistered validation (single seed range for N=20 P4; freeze date 2026-04-18 vs 2026-04-24 ambiguity)
- 8.5 Theoretical (post-hoc 600-cell choice; cascade decomposition non-unique; φ⁻² floor design-level not derived)

### §10 Conclusion (target: 80-120 lines)

- Headline results recap.
- Falsification programme: 4 explicit kill-switches.
- What this is / is not (b-anomaly Move 5).
- Reproducibility recap.
- Connection to b-anomaly + ACT (one cascade infrastructure, two empirical witnesses).

---

## 5. Acceptance criteria

**AC1.** Every numerical claim is verbatim from the deterministic scripts. The 18/18 table, the 6/6 signature table, the P4 N=20 result, the HCP separation — exact numbers reproducible from `demo_drug_sleep_v4.py`, `demo_p4_cxp_deep_dive.py`, `run_preregistered_validation.py`.

**AC2.** No claim is stronger than what the substrate-witness framing supports. In particular:
- DO NOT claim ACT-selection-theorem witness (Hypothesis 4.3) is delivered.
- DO NOT claim 2I-equivariance is checked.
- DO NOT claim Lyapunov V(W) exists.
- DO NOT claim consciousness is "explained."
- DO NOT claim the substrate is the unique solution.

**AC3.** The five b-anomaly honest-scope moves have explicit equivalents in §9 (regime, post-hoc, interpretation, test/claim, state-drift).

**AC4.** φ⁻² floor is explicitly disclosed as design-level (consciousness_tensor.py:348, pending first-principles calibration).

**AC5.** Polytope state-drift is explicitly disclosed; the homeostatic_reset(level=1.0) protocol is mandatory in the repro pipeline.

**AC6.** ACT bridge (§8.5) is non-load-bearing per `feedback_mathematical_framing_discipline.md`.

**AC7.** Citations to b-anomaly + adaptive-closure-transport are correct, with proper bibtex.

**AC8.** Preregistration date ambiguity (2026-04-18 frozen predictions vs 2026-04-24 frozen H4-fingerprint) is explicitly clarified.

**AC9.** Hostile-review-ready: every paragraph survives a referee asking "is this what the data actually shows, or what you wish it showed?"

---

## 6. Out of scope

- Aria-chess `paper/figures/` content (placeholder OK; figures can be added in revision).
- Code-freeze tag (separate task; user controls).
- Edits to MANUSCRIPT_V2.md or other supporting docs (those are the source; the tex paper is the deliverable).
- Lyapunov V derivation (deferred to ACT companion paper or future work).
- 2I-equivariance audit (deferred).
- G-ablation (nice-to-have; not blocking).

---

## 7. Codex derive prompt

Read this TASK file plus all referenced source documents. For the paper-writing project, produce:

**SECTION A.** Inventory of paper-ready content vs writing-from-scratch content. For each of the 10 sections, state: which existing material can be lifted directly (cite file:line), what needs writing from scratch.

**SECTION B.** Numbered build list (B1, B2, ..., Bn) with:
- target file (e.g. `aria-chess/paper/sections/05_results.tex`)
- content blueprint (what goes in this section)
- source attribution (cite file:line for every claim)
- cross-references to other sections / papers
- what AC# it discharges

**SECTION C.** Citation requirements: which papers need bibtex entries (b-anomaly, ACT, foundation papers, EEG literature). Cite with file paths.

**SECTION D.** Hostile-review risk register: top 5 places a referee will attack, and how to guard against each. Specifically:
- φ⁻² floor not derived
- preregistration date ambiguity
- single-seed determinism for v4
- post-hoc N=20 P4 retest
- 600-cell as post-hoc choice

**SECTION E.** Missing-content check: anything from MANUSCRIPT_V2 that's WORKING-NOTES quality and needs actual writing for paper-grade prose.

**SECTION F.** Top-3 build priorities with file:line anchors.

Hostile-review framing throughout. Do not propose to add content beyond what the substrate-witness framing supports.
