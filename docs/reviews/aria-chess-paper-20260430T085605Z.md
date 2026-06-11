Reading additional input from stdin...
2026-04-30T08:56:12.274395Z ERROR codex_models_manager::manager: failed to refresh available models: timeout waiting for child process to exit
OpenAI Codex v0.124.0 (research preview)
--------
workdir: /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
model: gpt-5.5
provider: openai
approval: never
sandbox: read-only
reasoning effort: xhigh
reasoning summaries: none
session id: 019ddd9a-54f2-7dd0-bc29-071630daada1
--------
user
You are reviewing a physics/neuroscience preprint in LaTeX. Treat this like a careful
journal-referee pass, not a code review.

Paper path (absolute, outside this repo):
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex

Section files (read all 10):
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex

Bibliography:
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/references.bib

Source documents the paper lifts from (verify numbers verbatim):
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/MANUSCRIPT_V2.md
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/P4_SYNERGY_FINDING.md
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/CROSS_DOMAIN_RESULTS.md
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/PAPER_PREDICTIONS.md
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md

WO context (read first):
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-chess-paper/TASK-aria-paper-completion.md
  /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/codex-derive/TASK-aria-paper-completion-20260430T081822Z.md

This paper is a SUBSTRATE WITNESS, not a selection theorem. The hard discipline:
- never claim the substrate IS consciousness
- never claim the 600-cell is unique among regular 4-polytopes
- never claim a Lyapunov function on the reduced flow has been delivered
- never claim ACT delivers a selection theorem here
- 18/18 preregistered MUST be reported with methodology refinement disclosure (NOT threshold change)
- chess +40.6pp lift at n=25 with reset (NOT +27.2pp at n=15)
- C×P bootstrap should report 0/2000 resamples at or below zero (NOT P=0)
- propofol switching ratio 1.83x (NOT 2.96x — the latter is the empirical reference)
- HCP n=1003 is descriptive on top of preregistered n=100; not the preregistered N

Read the file in full, then produce a structured review with the following
sections:

1. **Claim audit** For every non-trivial claim (theorem, proposition,
   numerical result, headline statement), say whether the stated argument
   actually establishes the stated claim. Flag over-claims, hidden assumptions,
   missing hypotheses, or cases where the prose needs softening. Quote the
   specific claim and cite the file:line.

2. **Internal consistency** Identify any place where definitions,
   assumptions, or notation conflict across sections. Check that the abstract
   matches the headline tally (18/18 with N=20 deep-dive, 17/18 standard);
   that thresholds in §5 match the preregistration document; that bootstrap
   wording is "0/2000 resamples at or below zero, reported as 0.0000" not "P=0".

3. **External consistency / numerics** For each headline numeric verify against
   the source document by reading it locally:
   - 6/6 v4 signatures (CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md)
   - 18/18 preregistered (VALIDATION_RESULTS_2026-04-29.md)
   - C×P 0.190 / [+0.143, +0.239] / 0/2000 (P4_SYNERGY_FINDING.md)
   - Chess +40.6pp at n=25 with reset (CROSS_DOMAIN_RESULTS.md)
   - HCP -11.58σ / +79.78σ / +6.80σ (CROSS_DOMAIN_RESULTS.md)
   If you find any disagreement, flag with file:line in both source and paper.

4. **Substrate-witness scope discipline** Identify any sentence that strays
   into selection-theorem territory or uniqueness territory. The paper must
   stay strictly inside substrate-witness scope.

5. **Tightness** Identify passages where the tone is stronger than the
   evidence supports, or weaker. Suggest one-line edits.

6. **Surface issues** Typos, undefined macros, broken LaTeX, inconsistent
   capitalisation. The paper defines \Ph, \Lop, \Cph, \Rsixhundred as macros
   in main.tex preamble; check usage is consistent.

7. **Top three fixes** Your ranked list of the most important issues to
   address before this paper is publication-ready. Be specific; cite file:line.

8. **Verdict** "Publication ready: yes" or "Publication ready: no — must-fix
   list above". Be direct. Over-claiming is worse than under-claiming.

PRIOR ROUND VERDICT was 'Publication ready: no'. The author addressed:
- P13 estimator: now disclosed as 5-fold CV preregistered, LOO refinement (table footnote ddagger).
- Six-signature framing: explicitly stated as not part of P1-P18 prereg, published-reference thresholds, v4 stimulus redesign disclosed.
- Abstract: now states '17/18 standard; 18/18 with N=20 deep-dive'.
- Bootstrap wording: removed P-notation, only '0/2000 reported as 0.0000' now.
- C×P monotone trend: replaced with 'remains small at N=3/5; rises at N=10/20'.
- Type II false negative: softened to 'consistent with an underpowered interaction estimate'.
- Sleep-EDFx CI: standardised to [2.50, 2.53] consistently.
- Cross-domain 'amplifies only when': softened to 'in these two tasks'.
- HCP preprocessing-noise claim: replaced with 'large on ICA-50 pipeline; cross-parcellation open'.
- Participation-ratio comparability: now disclosed (120 vs 50 nodes).
- Novelty claim: softened to 'we are not aware of'.
- Citations: Baars 1988, Dehaene 2014, Friston 2010, Clark 2013 added for GWT and PP.
- Brodbeck: now disclosed as wake/NREM lineage, not propofol-specific.

Verify each prior must-fix is closed; flag any new must-fix items; give verdict.
warning: Codex could not find bubblewrap on PATH. Install bubblewrap with your OS package manager. See the sandbox prerequisites: https://developers.openai.com/codex/concepts/sandboxing#prerequisites. Codex will use the vendored bubblewrap in the meantime.
2026-04-30T08:56:33.702391Z ERROR rmcp::transport::worker: worker quit with fatal: Client error: HTTP request failed: http/request failed: error sending request for url (https://chatgpt.com/backend-api/wham/apps), when send initialized notification
codex
I’ll treat this as a referee audit, reading the WO context first, then the LaTeX and source documents with line numbers.
  → Read WO context and paper
  • Verify source numerics
  • Audit claims and scope
  • Compile referee verdict
exec
/bin/bash -lc "printf '--- WO1 ---\\n'; nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/aria-chess-paper/TASK-aria-paper-completion.md' | sed -n '1,220p'; printf '\\n--- WO2 ---\\n'; nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/codex-derive/TASK-aria-paper-completion-20260430T081822Z.md' | sed -n '1,260p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 233ms:
/bin/bash: line 0: printf: --: invalid option
printf: usage: printf [-v var] format [arguments]
     1	# TASK: Write the aria-chess publication-ready paper
     2	
     3	**Date:** 2026-04-30.
     4	**Bar:** Hostile-review-ready, no overclaim. Strong, confident paper backed by lots of empirical evidence. Per `feedback_credibility_bar.md`: "complete + undismissable" not "honest + conditional."
     5	**Pair-programmer pattern:** codex_derive (this WO) → Claude implements → review_paper.sh hostile audit → iterate until codex says "Publication ready: yes."
     6	
     7	---
     8	
     9	## 1. Substrate (existing material to lift from)
    10	
    11	**Empirical / methods content (paper-grade, ready to lift):**
    12	- `docs/brain_mapping/MANUSCRIPT_V2.md` — 1245 lines, 11 sections, complete draft with abstract through conclusion. Already structurally close to publication; needs tex conversion and tightening.
    13	- `docs/brain_mapping/PAPER_BASIS_2026-04-29.md` — 37 KB, paper-ready abstract + intro + methods + results
    14	- `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md` — 6/6 v4 signature table, full per-signature documentation
    15	- `docs/brain_mapping/P4_SYNERGY_FINDING.md` — N=20 deep-dive narrative + per-seed values + bootstrap
    16	- `docs/brain_mapping/CROSS_DOMAIN_RESULTS.md` — chess + conversation + HCP results
    17	- `docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md` — 18/18 prereg tally with thresholds
    18	- `docs/brain_mapping/PREREG_H4_FINGERPRINT.md`, `PREREG_RUNG_OBSERVABLES.md` — frozen 2026-04-24 predictions
    19	- `docs/brain_mapping/EMERGENCE_AUDIT.md` — what's hardcoded vs derived
    20	- `docs/brain_mapping/REPRODUCIBILITY.md` — pipeline documentation
    21	
    22	**Headline numbers (deterministic, regenerable from seed=42, seed range 32000-32019):**
    23	
    24	| Result | Value | Source script | Wallclock |
    25	|--------|-------|---------------|-----------|
    26	| 6/6 v4 EEG signature table | 4 conditions × 6 signatures all pass | `demo_drug_sleep_v4.py` | ~30s |
    27	| P4 C×P synergy (N=20) | +0.190 [+0.143, +0.239]; P(≤0)=0.0000 | `demo_p4_cxp_deep_dive.py` | ~28 min |
    28	| 18/18 preregistered tally | All P1-P18 pass | `run_preregistered_validation.py` | ~18 min |
    29	| HCP categorical separation | Degree-std 11.58σ, PR 79.78σ (n=1003) | Cascade pipeline | (deterministic) |
    30	| Sleep-EDFx spindle α | 2.513 (real) ∈ ARIA CI | Sleep-EDFx public data + `run_baseline_for_eeg.py` | (cached) |
    31	| Cascade-α three-way overlap | WAKE [1.82,2.86] ∩ EEG [2.50,2.86] ∩ ARIA prior [2.73,3.25] | Combined | (cached) |
    32	
    33	**Validation persistence:** `~/.aria/preregistered_validation/results_1777466957.json` (Apr 29 13:49) is the 18/18 record.
    34	
    35	**Theoretical anchors:**
    36	- `BANOMALY-001/vfd-b-anomaly/paper/main.tex` — structural template (10 sections: intro, method, derivation, results, stress_tests, cross_dataset, cross_channel, discussion, limitations, conclusion).
    37	- `vfd-crystalisation-paper/papers/adaptive-closure-transport/adaptive-closure-transport.tex` — ACT theory paper. The aria-chess paper is the **active-regime empirical companion** to ACT; ACT names ARIA as the candidate instantiation of the 4-tuple (Remark 7.1 / sec:aria).
    38	- `vfd-crystalisation-paper/docs/aria-closure-kernel.md` — kernel-spine doc; aria-chess witnesses the active regime alongside b-anomaly's passive-regime witness.
    39	
    40	---
    41	
    42	## 2. Framing decision (load-bearing)
    43	
    44	**Adopt the substrate-witness framing, NOT the ACT-selection-theorem-witness framing.**
    45	
    46	The substrate-witness framing claims:
    47	- A deterministic geometric substrate (600-cell under H₄ symmetry) reproduces 18 preregistered neuroscience predictions across multiple paradigms with NO fitted shape parameters.
    48	- The claim is **not** that the substrate explains consciousness or that it's the unique solution.
    49	- The claim is **not** that ACT's selection-theorem (Hypothesis 4.3) is empirically witnessed.
    50	- The claim is: this geometry, with one parameter set, produces a specific quantitative correspondence with cortex.
    51	
    52	Under this framing:
    53	- Lyapunov V(W) is **not required** as a deliverable (would be required for ACT-selection-witness).
    54	- 2I-equivariance check is **not required** (would be required for cascade-selection-witness).
    55	- G-ablation is **nice-to-have** but the recovery-reversibility result already witnesses learning-rule idempotency.
    56	
    57	The ACT bridge appears as a non-load-bearing closing subsection in §8, mapping ARIA to ACT's 4-tuple as a programme-positioned correspondence (per `feedback_mathematical_framing_discipline.md` rule).
    58	
    59	---
    60	
    61	## 3. Output structure
    62	
    63	Mirror BANOMALY-001/vfd-b-anomaly/paper/ exactly:
    64	
    65	```
    66	aria-chess/
    67	└── paper/
    68	    ├── main.tex              # frontmatter + \include all sections + bibliography
    69	    ├── README.md             # paper README mirroring b-anomaly README.md (headline result, table, statistical caveat, repro recipe)
    70	    ├── references.bib        # bibtex entries
    71	    ├── sections/
    72	    │   ├── 01_introduction.tex
    73	    │   ├── 02_method.tex
    74	    │   ├── 03_substrate.tex          # the 600-cell + cascade decomposition + Green response
    75	    │   ├── 04_consciousness_chain.tex # 4-layer chain
    76	    │   ├── 05_results.tex            # 6/6 v4 + 18/18 + cascade-α match
    77	    │   ├── 06_stress_tests.tex       # P4 N=20 + bootstrap + ablation matrix
    78	    │   ├── 07_cross_domain.tex       # chess + conversation + HCP
    79	    │   ├── 08_discussion.tex
    80	    │   ├── 09_limitations.tex
    81	    │   └── 10_conclusion.tex
    82	    └── figures/                # placeholder for any figures (likely none in v1)
    83	```
    84	
    85	---
    86	
    87	## 4. Section content blueprint
    88	
    89	### §1 Introduction (target: 100-130 lines)
    90	- The problem: consciousness theories typically fit (predictive coding, IIT, GNW). What if a substrate were group-theoretically forced and non-fittable?
    91	- The geometry: H₄ Coxeter / 600-cell — biological motivation (icosahedral hippocampus, theta-gamma 11:1 ratio, etc.) but NOT a-priori derivation.
    92	- What this paper tests (verbatim "what is tested / what is not claimed" pattern, mirror b-anomaly §1).
    93	- Programme position: passive-regime witness for $C_\varphi$ in b-anomaly is the companion (one substrate, two empirical layers).
    94	
    95	### §2 Method (target: 150-190 lines)
    96	- Datasets: Sleep-EDFx (n=30/24), OpenNeuro ds005620 propofol (n=20), Zenodo ds003992359 DMT (n=29), ds004902 SD (n=35), HCP-YA S1200 (n=1003) — all public, cite DOIs.
    97	- Substrate construction summary (full derivation in §3): 600-cell, H₄ acting transitively, 9 H₃-shells, 12-degree.
    98	- Cascade event detection method.
    99	- Power-law fit + bootstrap CI.
   100	- Stimulus models for v4 (WAKE, SLEEP_N3, PROPOFOL, RECOVERY).
   101	- Preregistration protocol (frozen 2026-04-18 / 2026-04-24, what was peeked / what was not — be honest about ordering).
   102	- Reproducibility ledger (versions, seeds, deterministic).
   103	- State-reset protocol — the homeostatic_reset(level=1.0) call, why mandatory, how P13 changed from -3pp to +40.6pp.
   104	
   105	### §3 Substrate construction (target: 80-120 lines)
   106	- 600-cell vertex set V_600, 720 edges, 12-regular, 9 H₃-shells {1,12,20,12,30,12,20,12,1}.
   107	- H₄ Coxeter symmetry, transitivity, eigenvalue spectrum (12 mult 1; 6φ mult 4; 4φ mult 9; 3 mult 16; ...).
   108	- Cascade rung decomposition E₈→H₄→40→D₄→16→8→0 (briefly, with reference to cascade-derivation programme).
   109	- Green response operator $C_\varphi = L + \varphi^{-2} I$, programme-level definition (NOT load-bearing for the empirical claims; cite docs/aria-closure-kernel.md).
   110	- Reference: ACT theory paper for the 4-tuple (M, L_M, W, R_hom) framing; aria's instantiation flagged as candidate per ACT Remark 7.1.
   111	
   112	### §4 Consciousness chain (target: 80-120 lines)
   113	- Recurrent loop: Cascade event detection feeding cascade-pressure ρ.
   114	- Bounded-top-K (k=12) thresholding (matches degree).
   115	- IIT integrated-information layer (Φ trajectory).
   116	- Stream continuity layer.
   117	- Phenomenal-field binding.
   118	- All four layers derived from substrate; no fitted parameters.
   119	
   120	### §5 Results (target: 200-280 lines)
   121	
   122	**§5.1 Six v4 EEG signatures across 4 brain states**
   123	
   124	Verbatim from MANUSCRIPT_V2 lines 661-677. Per-condition table:
   125	
   126	| Cond | n_evt | α | 95% CI | R² | I_var | Φ_traj | cont |
   127	| WAKE | 58 | 2.252 | [1.82, 2.86] | 0.956 | 2.18e-05 | 0.0008 | 0.943 |
   128	| SLEEP_N3 | 111 | 3.250 | [2.44, 4.14] | 0.886 | 1.01e-05 | 0.0055 | 0.980 |
   129	| PROPOFOL | 246 | 2.758 | [2.52, 3.09] | 0.931 | 5.37e-06 | 0.0003 | 0.877 |
   130	| RECOVERY | 58 | 2.252 | [1.82, 2.86] | 0.956 | 2.18e-05 | 0.0008 | 0.943 |
   131	
   132	Per-signature pass with explicit threshold + falsification gate.
   133	
   134	**§5.2 18/18 preregistered validation tally**
   135	
   136	Full table P1-P18 with threshold + result + dataset + verdict.
   137	
   138	**§5.3 Cascade-α three-way overlap**
   139	
   140	WAKE α [1.82, 2.86] ∩ real EEG α [2.50, 2.86] (Sleep-EDFx n=30) ∩ ARIA prior α [2.73, 3.25].
   141	
   142	### §6 Stress tests (target: 120-180 lines)
   143	
   144	**§6.1 P4 C×P deep-dive (the headline stress test)**
   145	
   146	N=3→5→10→20 trend with per-seed values (19/20 positive); bootstrap CI [+0.143, +0.239]; P(≤0)=0.0000.
   147	
   148	Architectural reading: C and P are STRONGLY coupled, not nearly-orthogonal as the original prereg implicitly assumed. Original "fail" was Type II underpower + seed-range bias.
   149	
   150	**§6.2 16-condition 2⁴ ablation matrix**
   151	
   152	Main effects + pairwise interactions.
   153	
   154	**§6.3 Non-equilibrium homeostatic reset finding**
   155	
   156	Conditions A/B/C/D (no homeostasis / periodic only / wake-decay only / dual). Both required.
   157	
   158	### §7 Cross-domain (target: 120-160 lines)
   159	
   160	**§7.1 Chess** — 5-fold CV 83.1%, LOO lift +40.6pp with reset, goldilocks peak n=25.
   161	**§7.2 Conversation** — 87.5% raw, |lift| < 10pp (selective amplifier).
   162	**§7.3 HCP categorical separation** — n=1003, degree-std 11.58σ, PR 79.78σ.
   163	
   164	### §8 Discussion (target: 120-180 lines)
   165	
   166	**§8.1 What's new** — substrate witness, no fitted parameters, 18/18 prereg, 4-state cross-paradigm.
   167	**§8.2 Comparison to existing theories** — IIT, GNW, predictive coding (substrate ≠ alternative theory; substrate is what *any* theory needs).
   168	**§8.3 Strong C×P coupling for biology** — implications.
   169	**§8.4 Substrate as null reference** — HCP separation reading.
   170	**§8.5 Programme position: ACT bridge (non-load-bearing)** — map to 4-tuple as candidate instantiation; explicitly defer Lyapunov / 2I-equivariance / edge-space lift to ACT open items.
   171	
   172	### §9 Limitations (target: 120-180 lines)
   173	
   174	Brutal honest scope. Apply b-anomaly §9 5-move template:
   175	
   176	**Move 1 (regime clarity):** State that this is a substrate-witness paper; ACT-selection-theorem witness is NOT delivered.
   177	
   178	**Move 2 (post-hoc structure verification):** P4 retest at N=20 was data-second (we saw N=3 fail first). Acknowledge ordering.
   179	
   180	**Move 3 (interpretation alternatives):** Three readings — (a) substrate is real-physics, (b) H₄ is structurally right, (c) data is rank-1 in any group-theoretic substrate. Adopt (c) as conservative.
   181	
   182	**Move 4 (test vs claim boundary):** Universality + cross-paradigm consistency PASS; ACT-active-regime selection-theorem witness NOT claimed.
   183	
   184	**Move 5 (substrate state-drift acknowledged):** Polytope state-drift (P13 fail mode without reset) explicitly disclosed; reset protocol mandatory in repro pipeline.
   185	
   186	Plus enumerated per-section limits:
   187	- 8.1 Substrate-level (600-cell only tested; no comparison to 24-cell, 120-cell)
   188	- 8.2 Consciousness chain (single-seed determinism, stylised stimuli)
   189	- 8.3 Cross-domain (small test sets, single parcellation)
   190	- 8.4 Preregistered validation (single seed range for N=20 P4; freeze date 2026-04-18 vs 2026-04-24 ambiguity)
   191	- 8.5 Theoretical (post-hoc 600-cell choice; cascade decomposition non-unique; φ⁻² floor design-level not derived)
   192	
   193	### §10 Conclusion (target: 80-120 lines)
   194	
   195	- Headline results recap.
   196	- Falsification programme: 4 explicit kill-switches.
   197	- What this is / is not (b-anomaly Move 5).
   198	- Reproducibility recap.
   199	- Connection to b-anomaly + ACT (one cascade infrastructure, two empirical witnesses).
   200	
   201	---
   202	
   203	## 5. Acceptance criteria
   204	
   205	**AC1.** Every numerical claim is verbatim from the deterministic scripts. The 18/18 table, the 6/6 signature table, the P4 N=20 result, the HCP separation — exact numbers reproducible from `demo_drug_sleep_v4.py`, `demo_p4_cxp_deep_dive.py`, `run_preregistered_validation.py`.
   206	
   207	**AC2.** No claim is stronger than what the substrate-witness framing supports. In particular:
   208	- DO NOT claim ACT-selection-theorem witness (Hypothesis 4.3) is delivered.
   209	- DO NOT claim 2I-equivariance is checked.
   210	- DO NOT claim Lyapunov V(W) exists.
   211	- DO NOT claim consciousness is "explained."
   212	- DO NOT claim the substrate is the unique solution.
   213	
   214	**AC3.** The five b-anomaly honest-scope moves have explicit equivalents in §9 (regime, post-hoc, interpretation, test/claim, state-drift).
   215	
   216	**AC4.** φ⁻² floor is explicitly disclosed as design-level (consciousness_tensor.py:348, pending first-principles calibration).
   217	
   218	**AC5.** Polytope state-drift is explicitly disclosed; the homeostatic_reset(level=1.0) protocol is mandatory in the repro pipeline.
   219	
   220	**AC6.** ACT bridge (§8.5) is non-load-bearing per `feedback_mathematical_framing_discipline.md`.

--- WO2 ---
     1	Read-only audit completed. I did not edit or commit anything.
     2	
     3	**SECTION A. Insight / External Relevance**
     4	
     5	**Already in cascade / companion papers**
     6	- Substrate-witness framing is explicit in `TASK-aria-paper-completion.md:42-57`: use substrate witness, not ACT selection witness; no Lyapunov \(V(W)\), no \(2I\)-equivariance check as deliverables.
     7	- Fixed response kernel is already defined in `docs/aria-closure-kernel.md:11-23`, with 600-cell facts at `:49-60`.
     8	- b-anomaly is the passive-regime companion witness: fixed \(C_\varphi\)-derived kernel, no shape retuning, one amplitude per dataset, at `docs/aria-closure-kernel.md:76-90`, with caveats at `:127-143`.
     9	- ACT supplies only the non-load-bearing 4-tuple bridge: selection is conditional on Lyapunov/timescale hypotheses in `adaptive-closure-transport.tex:222-228`; ARIA dictionary is proposed, not proved, at `:303-328`; programme bridge is explicitly non-load-bearing at `:394-449`.
    10	
    11	**Only in `insight.md`, not suitable as load-bearing ARIA paper content**
    12	- Fine-structure / two-600-cell material: `insight.md:47-64`, `:176-234`. Interesting programme background, but not relevant to ARIA neuroscience claims.
    13	- Crystallisation triplet / \(\alpha\) as selection coupling: `insight.md:361-407`, `:410-450`. Do not import into ARIA except as future programme language.
    14	- RH, god-prime, QMS-3, prime-locus material: `insight.md:601-717`, `:724-827`. Not relevant to this paper.
    15	- Pentagonal holonomy connection: `insight.md:830-892`. Potential future route for selection dynamics, but outside substrate-witness scope.
    16	
    17	**External literature directly needed**
    18	- 600-cell/H4 facts: Coxeter/MathWorld 600-cell reference.
    19	- EEG/SOC: Beggs & Plenz 2003.
    20	- Dataset citations: Sleep-EDFx/PhysioNet, OpenNeuro `ds005620`, OpenNeuro `ds004902`, Zenodo DMT `10.5281/zenodo.3992359`, HCP S1200.
    21	- Consciousness theory comparison: Tononi/IIT, Balduzzi & Tononi, Global Workspace, predictive processing.
    22	- Microstates: Brodbeck et al. 2012 for wake/NREM; propofol microstate/anesthesia papers for drug-state support.
    23	
    24	**SECTION B. Priority Gaps / Build List**
    25	
    26	B1. `01_introduction.tex`: claim-boundary definition  
    27	Object: \(q:\mathcal R_{\rm numeric}\to\mathcal C_{\rm admissible}\), prose map from results to allowed claims.  
    28	Bridges: strong manuscript claims to substrate-witness scope.  
    29	Route: new writing from task discipline.  
    30	First step: “What is tested / not claimed” box.  
    31	Sources: `TASK:44-57`, `TASK:203-226`, `MANUSCRIPT_V2.md:75-87`, `:1086-1091`. AC2, AC9.
    32	
    33	B2. `02_method.tex`: provenance ledger  
    34	Object: \(\Pi:\{P1..P18,S1..S6\}\to\)(script, seed, dataset, threshold, result).  
    35	Bridges: preregistration, deterministic scripts, hostile reproducibility.  
    36	Route: lift from validation docs.  
    37	First step: one table for dates, seeds, scripts, wallclock.  
    38	Sources: `TASK:22-33`, `MANUSCRIPT_V2.md:554-609`, `PAPER_PREDICTIONS.md:1-14`, `VALIDATION_RESULTS_2026-04-29.md:19-75`. AC1, AC8.
    39	
    40	B3. `03_substrate.tex`: 600-cell response substrate  
    41	Object: \(V_{600}=(V,E)\), \(L:\mathbb R^{120}\to\mathbb R^{120}\), \(C_\varphi=L+\varphi^{-2}I\).  
    42	Bridges: classical geometry to empirical substrate.  
    43	Route: classical literature plus local kernel doc.  
    44	First step: lemma stating 120 vertices, 720 edges, degree 12, H4 transitivity, 9 shells, shifted Green response.  
    45	Sources: `MANUSCRIPT_V2.md:158-224`, `aria-closure-kernel.md:11-60`. AC4.
    46	
    47	B4. `04_consciousness_chain.tex`: recurrent substrate observables  
    48	Object: \(T_\eta:\mathbb R^{120}\times F_t\to\mathbb R^{120}\); observables \(O(\tau)=(\alpha,I_{\rm var},\Phi,{\rm cont})\).  
    49	Bridges: substrate response to six EEG signatures.  
    50	Route: lift implementation narrative, rewrite as method not metaphysics.  
    51	First step: define `bounded_topk(k=12)`, \(\Phi\) proxy, continuity score.  
    52	Sources: `CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:51-102`, `:195-288`; `consciousness_tensor.py:340-359` for \(\varphi^{-2}\) floor caveat. AC4.
    53	
    54	B5. `05_results.tex`: exact empirical tables  
    55	Object: result map \(R:\) condition/test id \(\to\) scalar plus threshold verdict.  
    56	Bridges: source numerics to paper claims.  
    57	Route: verbatim lift, no recomputation.  
    58	First step: tables for 6/6 v4, 18/18, three-way \(\alpha\) overlap.  
    59	Sources: `CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:30-42`, `:197-288`; `VALIDATION_RESULTS_2026-04-29.md:78-99`, `:262-295`. AC1.
    60	
    61	B6. `06_stress_tests.tex`: C×P interaction proof block  
    62	Object: \(\Delta_{CP}=((\alpha_{CP}+\alpha_0)-(\alpha_C+\alpha_P))/2\).  
    63	Bridges: original P4 fail to strong-coupling result without threshold change.  
    64	Route: existing N=20 derivation plus bootstrap.  
    65	First step: include N=3/5/10/20 trend, finite-bootstrap wording.  
    66	Sources: `P4_SYNERGY_FINDING.md:102-173`, `:175-193`, `:197-229`, `:375-398`. AC1, AC9.
    67	
    68	B7. `07_cross_domain.tex`: selective amplifier and HCP null  
    69	Object: \(A_d={\rm Acc}_{sub,d}-{\rm Acc}_{raw,d}\); \(Z_m=(m_{\rm ARIA}-\mu_{\rm HCP})/\sigma_{\rm HCP}\).  
    70	Bridges: chess/conversation/HCP into one substrate-witness result.  
    71	Route: lift latest cross-domain report, not older Paper Basis numbers.  
    72	First step: use +40.6pp, n=25, 93.8% as authoritative.  
    73	Sources: `CROSS_DOMAIN_RESULTS.md:52-216`, `:234-303`, `:307-424`. AC1, AC5.
    74	
    75	B8. `08_discussion.tex`: non-load-bearing ACT bridge  
    76	Object: dictionary \(D_{\rm ACT}:(M,L_M,W,R_{\rm hom})\to\) ARIA components.  
    77	Bridges: empirical ARIA to ACT without claiming selection theorem.  
    78	Route: alternative route K, explicitly non-load-bearing.  
    79	First step: one closing subsection mapping the 4-tuple and deferring Lyapunov, edge-space lift, \(2I\)-equivariance.  
    80	Sources: `TASK:44-57`, `ACT:303-328`, `ACT:394-449`, `aria-closure-kernel.md:216-257`. AC2, AC6, AC7.
    81	
    82	B9. `09_limitations.tex`: hostile-review guard matrix  
    83	Object: \(G:{\rm risk}\to({\rm disclosure},{\rm evidence},{\rm build})\).  
    84	Bridges: evidence to credible scope.  
    85	Route: b-anomaly five-move template.  
    86	First step: regime, post-hoc, interpretation, test/claim, state-drift moves.  
    87	Sources: `TASK:172-191`, `MANUSCRIPT_V2.md:1012-1098`, `CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:354-379`, `NON_EQUILIBRIUM_FINDING.md:11-21`, `:97-105`. AC3, AC5.
    88	
    89	B10. `main.tex`, `README.md`, `references.bib`: paper shell  
    90	Object: deliverable graph \(D=(sections,bib,repro)\).  
    91	Bridges: source docs to BANOMALY-style paper.  
    92	Route: mirror template.  
    93	First step: scaffold exact 10-section structure.  
    94	Sources: `TASK:61-83`, `b-anomaly/paper/main.tex:136-171`, `MANUSCRIPT_V2.md:1101-1159`. AC7.
    95	
    96	**SECTION C. Reversals / Corrections**
    97	
    98	Apply these when lifting prose:
    99	
   100	- at `PAPER_BASIS_2026-04-29.md:48` replace `chess pattern recognition (84.4% LOO with reset; 83.1% 5-fold CV)` with `chess pattern recognition (93.8% LOO with reset at n=25; 83.1% 5-fold CV)`.
   101	- at `PAPER_BASIS_2026-04-29.md:550` replace `Chess goldilocks peak:                   n=15` with `Chess goldilocks peak:                   n=25`.
   102	- at `PAPER_BASIS_2026-04-29.md:551` replace `Chess substrate lift on LOO (with reset): +27.2pp` with `Chess substrate lift on LOO (with reset): +40.6pp`.
   103	- at `PAPER_BASIS_2026-04-29.md:562` replace `substrate **lifts chess by +27pp**` with `substrate **lifts chess by +40.6pp on LOO at n=25**`.
   104	- at `PAPER_BASIS_2026-04-29.md:602` replace `| P12 | Goldilocks peak ∈ {15, 25, 40, 60} | ✅ | 15 |` with `| P12 | Goldilocks peak ∈ {15, 25, 40, 60} | ✅ | 25 |`.
   105	- at `PAPER_BASIS_2026-04-29.md:603` replace `| P13 | Chess LOO lift ≥ +15pp (with reset) | ✅ | +27.2pp |` with `| P13 | Chess LOO lift ≥ +15pp (with reset) | ✅ | +40.6pp |`.
   106	- at `MANUSCRIPT_V2.md:17` replace `The substrate is fully derivable from group theory:` with `Once the 600-cell substrate is chosen, its graph structure is fixed by group theory:`.
   107	- at `PAPER_BASIS_2026-04-29.md:27` replace `The substrate is fully derivable from group theory;` with `Once the 600-cell substrate is chosen, its graph structure is fixed by group theory;`.
   108	- at `MANUSCRIPT_V2.md:795` replace `**HCP result (n=1003 subjects, ICA-50):**` with `**HCP result (preregistered n=100 ICA-50 plus full-cohort n=1003 descriptive statistics):**`.
   109	- in any new paper text replace `P(synergy ≤ 0) = 0` with `0/2000 bootstrap resamples were at or below zero, reported as 0.0000`.
   110	
   111	**SECTION D. Route Discipline / Citation Audit**
   112	
   113	Route S, load-bearing: substrate-witness paper. It needs exact numerics, prereg provenance, substrate construction, limitations.
   114	
   115	Route K, non-load-bearing only: ACT-selection witness. It would require Lyapunov \(V(W)\), edge-space decomposition, \(2I\)-equivariance, and full reduced-flow convergence. Do not present this as delivered.
   116	
   117	Required bibtex groups:
   118	- Geometry: Coxeter / 600-cell reference, e.g. MathWorld 600-cell.
   119	- EEG avalanche: Beggs & Plenz 2003, DOI `10.1523/JNEUROSCI.23-35-11167.2003`.
   120	- Datasets: Sleep-EDFx/PhysioNet; OpenNeuro `ds005620` DOI `10.18112/openneuro.ds005620.v1.0.0`; OpenNeuro `ds004902` DOI `10.18112/openneuro.ds004902.v1.0.8`; DMT Zenodo `10.5281/zenodo.3992359`; HCP S1200 plus Van Essen 2013 DOI `10.1016/j.neuroimage.2013.05.041`.
   121	- Consciousness theory: Tononi 2008, Balduzzi & Tononi 2008, Global Workspace, predictive processing.
   122	- Microstates/anesthesia: Brodbeck et al. 2012 DOI `10.1016/j.neuroimage.2012.05.060`; add a propofol-specific microstate citation if claiming anesthesia fragmentation.
   123	
   124	**SECTION E. Top-5 Risk Register**
   125	
   126	1. \(\varphi^{-2}\) floor not derived. Guard: disclose as design-level stability clamp, not theorem. Anchor: `consciousness_tensor.py:348-359`.
   127	2. Preregistration date ambiguity. Guard: separate Apr 18 P1-P18 from Apr 24 H4/rung batteries. Anchors: `PAPER_PREDICTIONS.md:1-14`, `PREREG_H4_FINGERPRINT.md:1-11`, `PREREG_RUNG_OBSERVABLES.md:1-7`.
   128	3. v4 single-seed chain. Guard: state deterministic seed 42 and event bootstrap; name cross-seed replication as strengthening build. Anchor: `CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:195-203`, `:371-376`.
   129	4. P4 N=20 was data-second after N=3 fail. Guard: report ordering, original fail, same threshold, high-variance rationale. Anchors: `P4_SYNERGY_FINDING.md:68-95`, `:102-123`, `VALIDATION_RESULTS_2026-04-29.md:267-280`.
   130	5. 600-cell chosen post-hoc. Guard: substrate-witness framing, no uniqueness claim, future ablation against 24-cell/120-cell. Anchors: `TASK:46-50`, `MANUSCRIPT_V2.md:1086-1091`.
   131	
   132	Missing-content check: `MANUSCRIPT_V2` is paper-shaped, but §1 and abstract need overclaim tightening; §5 needs exact dataset DOIs; §6 needs finite-bootstrap wording; §8 limits must become target §9 five-move limitations.
   133	
   134	**SECTION F. Top 3 Next Builds**
   135	
   136	1. Build `paper/sections/05_results.tex`: insert exact 6/6, 18/18, and \(\alpha\)-overlap tables. Anchors: `CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:197-288`, `VALIDATION_RESULTS_2026-04-29.md:78-99`, `CROSS_DOMAIN_RESULTS.md:184-196`.
   137	
   138	2. Build `paper/sections/03_substrate.tex` plus limitation hooks: define \(V_{600}\), \(L\), \(C_\varphi\), shells, and \(\varphi^{-2}\) disclosure. Anchors: `aria-closure-kernel.md:11-60`, `MANUSCRIPT_V2.md:158-224`, `consciousness_tensor.py:348-359`.
   139	
   140	3. Build `paper/sections/06_stress_tests.tex` and `07_cross_domain.tex`: P4 factorial derivation, reset protocol, +40.6pp chess lift, HCP null. Anchors: `P4_SYNERGY_FINDING.md:125-173`, `VALIDATION_RESULTS_2026-04-29.md:163-194`, `CROSS_DOMAIN_RESULTS.md:175-216`, `:307-424`.
   141	
   142	External sources used: MathWorld 600-cell, PhysioNet Sleep-EDFx, EEGDash/OpenNeuro DS005620 and DS004902, Zenodo DMT record 3992359, PubMed/PMC entries for Beggs & Plenz, Tononi, Balduzzi & Tononi, Brodbeck, and Van Essen/HCP.

codex
WO framing is clear: strict substrate-witness, exact numerics, no selection theorem. Now I’ll inspect the paper and source evidence line-numbered.
  → Read WO context and paper
  • Verify source numerics
  • Audit claims and scope
  • Compile referee verdict
exec
/bin/bash -lc "for f in \\
'/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' \\
'/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex' \\
'/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex' \\
'/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex' \\
'/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex' \\
'/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex' \\
'/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex' \\
'/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex' \\
'/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex' \\
'/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex' \\
'/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex'; do echo \"===== "'$f ====="; nl -ba "$f"; done' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 375ms:
===== /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex =====
     1	\documentclass[11pt]{article}
     2	
     3	\usepackage[a4paper, margin=2.5cm]{geometry}
     4	\usepackage{amsmath, amssymb, amsthm}
     5	\usepackage{booktabs}
     6	\usepackage{enumitem}
     7	\usepackage{graphicx}
     8	\usepackage{natbib}
     9	\usepackage[colorlinks=true, linkcolor=blue, citecolor=blue, urlcolor=blue]{hyperref}
    10	\usepackage{xcolor}
    11	
    12	\graphicspath{{figures/}}
    13	
    14	\newcommand{\Ph}{\varphi}
    15	\newcommand{\Lop}{L_{V_{600}}}
    16	\newcommand{\Cph}{C_{\Ph}}
    17	\newcommand{\Rsixhundred}{V_{600}}
    18	
    19	\title{A geometry-fixed substrate witness for cortical signatures:\\
    20	       eighteen preregistered correspondences and six drug/sleep EEG\\
    21	       signatures from the 600-cell under H$_4$ Coxeter symmetry}
    22	
    23	\author{%
    24	  Lee Smart\\[2pt]
    25	  \textit{Institute of Vibrational Field Dynamics}\\[2pt]
    26	  \texttt{contact@vibrationalfielddynamics.org}\\[2pt]
    27	  \texttt{@vfd\_org}%
    28	}
    29	
    30	\date{April 2026}
    31	
    32	\begin{document}
    33	
    34	\maketitle
    35	
    36	\noindent\textbf{Status:} Preprint, not peer-reviewed.
    37	
    38	\noindent\emph{Headline.}
    39	Once the 600-cell substrate is chosen, its graph structure is fixed by
    40	group theory: $120$ vertices of uniform degree $12$, Laplacian
    41	eigenvalues $\{0, 3, 4\Ph, 6\Ph, 12\!-\!4\Ph, 12\!-\!6\Ph, 12\!-\!3, 12\}$
    42	in their H$_4$-irrep multiplicities, with $\Ph=(1+\sqrt 5)/2$. Treated
    43	as an architectural-level substrate with a fixed shifted-Laplacian
    44	response $\Cph = \Lop + \Ph^{-2} I$ and a small dynamical layer above
    45	it, this single deterministic structure is consistent with eighteen
    46	quantitative correspondences with neuroscience data — preregistered
    47	on 2026-04-18 before any validation run — plus six drug/sleep EEG
    48	signatures of conscious vs unconscious states tested against
    49	published-reference thresholds on a single deterministic substrate
    50	trajectory at seed~$42$. No shape parameter is tuned to any neural
    51	dataset. The recurrent layer above the substrate adds one
    52	substrate-pinned nonlinearity $\mathrm{bounded\_topk}(\cdot, k\!=\!12)$
    53	at the graph's average degree and one condition-dependent self-injection
    54	coupling $\eta\!\in\!\{0, 0.05, 0.20\}$; condition-specific stimulus
    55	models (\S\ref{sec:chain}) are biologically-motivated design choices,
    56	not measurement-fits.
    57	
    58	\noindent\emph{Scope.}
    59	This paper presents an empirical \emph{substrate witness}: it shows
    60	that a geometry-fixed substrate, with no shape parameters tuned to any
    61	neural dataset, is consistent with eighteen preregistered correspondences
    62	and six EEG signatures. It is not a derivation of consciousness, nor a
    63	selection theorem, nor a uniqueness claim for the 600-cell among regular
    64	4-polytopes. The companion adaptive-closure-transport
    65	preprint~\citep{SmartAdaptiveClosureTransport2026} provides the
    66	4-tuple bridge $(M, L_M, W, R_{\mathrm{hom}})$ in which this substrate
    67	sits as the $L_M$ instance; the selection of the 600-cell as the active
    68	$M$ is treated as conjectural and is not load-bearing here.
    69	
    70	\begin{abstract}
    71	We test whether a geometry-fixed substrate — the 600-cell regular
    72	4-polytope $\Rsixhundred$ under H$_4$ Coxeter symmetry, with the
    73	shifted graph Laplacian $\Cph = \Lop + \Ph^{-2} I$ as its response
    74	operator — is consistent with cortical signatures across five
    75	neuroscience domains. Eighteen quantitative predictions were
    76	preregistered on 2026-04-18 (\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md})
    77	before any validation run; each has a falsifiable threshold. The
    78	preregistered tally is $17/18$ at standard validation methodology
    79	($5$-seed cascade block plus state-reset protocol), and $18/18$ after
    80	a documented $N\!=\!20$ deep-dive on the residual high-variance
    81	interaction (P4); no preregistered threshold has been modified. We
    82	additionally report six drug/sleep EEG signatures tested on a recurrent
    83	self-model layer above the substrate, on a single deterministic
    84	trajectory at seed~$42$. The six signatures are not part of the
    85	P1--P18 preregistration; they are tested against published-reference
    86	thresholds (Sleep-EDFx, OpenNeuro, Brodbeck, Tononi) and were obtained
    87	under condition-specific stimulus models redesigned at v4 to be
    88	biologically realistic (\S\ref{sec:chain}).
    89	
    90	\noindent\emph{(i) Cortical avalanches.}
    91	Wake cascade-event power-law exponent $\alpha = 2.252$,
    92	$95\%$ CI $[1.82, 2.86]$ ($R^{2}=0.956$, $n_{\mathrm{events}}=58$).
    93	This 95\% CI overlaps simultaneously real Sleep-EDFx EEG ($n=30$
    94	subjects, $\alpha=2.51$, CI $[2.50, 2.53]$) and ARIA's prior cascade
    95	pipeline ($\alpha=2.85$, CI $[2.73, 3.25]$) — three-way confidence
    96	overlap.
    97	
    98	\noindent\emph{(ii) Drug/sleep state transitions.}
    99	NREM-N3 phenomenal-intensity variance ratio $0.463\!\times$ wake
   100	(predicted $\sim 0.365$, threshold $<\!0.70$); propofol modality-switching
   101	ratio $1.83\!\times$ wake (threshold $\in[1.5, 5.0]$, empirical
   102	reference $2.96\!\times$ from OpenNeuro \texttt{ds005620}, $n=8$);
   103	propofol continuity drop $+0.066$ (threshold $>\!0.020$); propofol
   104	integrated-information $\Phi$ collapse to $0.33\!\times$ wake (IIT
   105	direction confirmed); recovery deterministically identical to wake.
   106	All six signatures pass against their published-reference thresholds
   107	on the single deterministic substrate trajectory.
   108	
   109	\noindent\emph{(iii) Causal mechanism isolation.}
   110	Two of four cascade mechanisms — context rotation $C$ and partial
   111	emission $P$ — are causally significant, and the original
   112	preregistered C$\times$P synergy prediction $\geq +0.10$ closes
   113	decisively at adequate replication: $N\!=\!20$ fresh seeds give a
   114	bootstrap point estimate of $+0.190$ with $95\%$ CI $[+0.143, +0.239]$
   115	(threshold $\geq +0.10$); $0/2000$ bootstrap resamples were at or
   116	below zero, reported as $0.0000$. We document the original $N\!=\!3$
   117	underestimate ($+0.044$) as consistent with an underpowered interaction
   118	estimate at $N\!=\!3$ and contribute the $N\!\geq\!20$ minimum as a
   119	preregistration-practice recommendation for high-variance interaction
   120	terms.
   121	
   122	\noindent\emph{(iv) Cross-domain selectivity.}
   123	The substrate exhibits domain-invariant selective amplification on
   124	the two tasks tested: chess 4-category position classification on
   125	8-dimensional V2 features lifts $+40.6$ percentage points on
   126	leave-one-out at canonical depth $n\!=\!25$ ticks (raw $53.1\%$
   127	$\to$ substrate-routed $93.8\%$, with state reset; the
   128	preregistered estimator P13 was $5$-fold CV with threshold
   129	$\geq\!+15$pp; the LOO finding above is a stronger validation-protocol
   130	refinement at the same threshold), while conversation utterance
   131	classification at raw $87.5\%$ yields a substrate lift of $-4.4$pp
   132	(threshold $|\cdot| < 10$pp), consistent with selective amplification
   133	only where raw features are ambiguous. On HCP brain functional connectivity
   134	(preregistered $n\!=\!100$ ICA-50 plus full-cohort $n\!=\!1003$
   135	descriptive statistics), the H$_4$-transitive substrate is a
   136	maximum-symmetry deterministic null reference: ARIA degree std
   137	$=\!0$ by transitivity; HCP $3.28\!\pm\!0.28$; ARIA at $-11.58\sigma$
   138	on degree homogeneity, $+79.78\sigma$ on participation ratio, and
   139	$+6.80\sigma$ on clustering coefficient.
   140	
   141	\noindent\emph{What we do not claim.}
   142	We do not claim the 600-cell is the unique substrate consistent with
   143	these signatures, nor that other regular 4-polytopes (24-cell, 120-cell)
   144	have been ruled out. We do not derive the $\Ph^{-2}$ floor from
   145	first principles; it is a design-level stability clamp on the
   146	shifted-Laplacian response. The recurrent layer above the substrate
   147	is reported on a single deterministic trajectory; cross-seed CIs on
   148	the per-condition signatures are an explicit strengthening build.
   149	The structural scope of this paper is: \emph{a geometry-fixed
   150	substrate, with no shape parameters tuned to any neural dataset,
   151	is consistent with eighteen preregistered neuroscience
   152	correspondences and six drug/sleep EEG signatures, with all gaps in
   153	the original preregistration closed by methodology refinement and
   154	without modifying any preregistered threshold.}
   155	\end{abstract}
   156	
   157	% =====================================================================
   158	\input{sections/01_introduction.tex}
   159	\input{sections/02_method.tex}
   160	\input{sections/03_substrate.tex}
   161	\input{sections/04_consciousness_chain.tex}
   162	\input{sections/05_results.tex}
   163	\input{sections/06_stress_tests.tex}
   164	\input{sections/07_cross_domain.tex}
   165	\input{sections/08_discussion.tex}
   166	\input{sections/09_limitations.tex}
   167	\input{sections/10_conclusion.tex}
   168	% =====================================================================
   169	
   170	\section*{Acknowledgements}
   171	We thank the Sleep-EDFx (PhysioNet)~\citep{PhysioNet2000,SleepEDFx},
   172	OpenNeuro propofol cohort \texttt{ds005620}~\citep{OpenNeuroDS005620},
   173	the OpenNeuro DMT cohort \texttt{ds004902}~\citep{OpenNeuroDS004902},
   174	the Zenodo DMT EEG release~\citep{ZenodoDMT3992359}, and the WU-Minn
   175	HCP Consortium~\citep{VanEssen2013HCP} for releasing the public
   176	datasets that made these comparisons possible. Cortical avalanche
   177	methodology follows~\citep{BeggsPlenz2003}; the integrated-information
   178	$\Phi$ proxy is in the IIT family~\citep{Tononi2008,BalduzziTononi2008};
   179	the propofol microstate comparison uses Brodbeck et
   180	al.~\citep{Brodbeck2012Microstates}. The 600-cell construction
   181	follows~\citep{CoxeterRegularPolytopes,Weisstein600Cell}. All code
   182	and processed data are released under MIT licence at the project
   183	repository~\citep{ariaChessRepo}.
   184	
   185	\section*{Reproducibility}
   186	The complete pipeline (substrate construction, six-signature
   187	consciousness chain, $N\!=\!20$ C$\times$P deep-dive, eighteen-prediction
   188	preregistered validation, figure regeneration, this paper) is reproducible
   189	from the project repository~\citep{ariaChessRepo} via the included
   190	\texttt{reproduce\_paper\_claims.sh} script. All scripts are
   191	deterministic given seeds; the substrate's spectral decomposition is
   192	cached at module level. Wallclocks: drug/sleep v4 $\sim 30$\,s;
   193	$N\!=\!20$ deep-dive $\sim 28$\,min; preregistered validation
   194	$\sim 18$\,min.
   195	
   196	\bibliographystyle{plainnat}
   197	\bibliography{references}
   198	
   199	\end{document}
===== /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/01_introduction.tex =====
     1	% =====================================================================
     2	\section{Introduction}\label{sec:intro}
     3	% =====================================================================
     4	
     5	Theories of consciousness divide into mechanism-driven proposals
     6	(Integrated Information Theory~\citep{Tononi2008,BalduzziTononi2008},
     7	Global Workspace Theory~\citep{Baars1988GWT,Dehaene2014ConsciousAndBrain},
     8	predictive processing~\citep{FristonFreeEnergy2010,ClarkPP2013}) and
     9	structure-driven proposals (geometric or topological substrates,
    10	neural-population dynamics). The mechanism-driven proposals offer compelling axiomatic
    11	stories but have not yielded preregistered quantitative signatures
    12	that survive on real EEG data. The structure-driven proposals produce
    13	numbers but typically introduce fitted parameters, learned weights,
    14	or domain-specific tuning.
    15	
    16	This paper takes a deliberately constrained third path. Once a
    17	substrate is chosen, we ask which neuroscience phenomena it is
    18	consistent with under \emph{no} shape parameter tuning, no learned
    19	weights, and no domain-specific calibration. The substrate is the
    20	600-cell regular 4-polytope $\Rsixhundred$, treated as a graph with
    21	H$_4$ Coxeter symmetry. It has been studied in pure mathematics for
    22	over a century~\citep{CoxeterRegularPolytopes,Weisstein600Cell}; to
    23	our knowledge it has not been proposed before as an empirical
    24	consciousness substrate. We construct $\Rsixhundred$, fix its response
    25	operator $\Cph = \Lop + \Ph^{-2} I$ where $\Ph=(1+\sqrt 5)/2$, add a
    26	single condition-dependent self-injection coupling $\eta$ and a
    27	single graph-pinned nonlinearity, and test the resulting witness
    28	against eighteen preregistered correspondences plus six independent
    29	drug/sleep EEG signatures.
    30	
    31	\subsection*{What this paper claims}
    32	
    33	We claim a single \emph{substrate witness}: that a geometry-fixed
    34	substrate, with no shape parameters tuned to any neural dataset, is
    35	consistent with eighteen preregistered correspondences (frozen
    36	2026-04-18) and six independent drug/sleep EEG signatures of
    37	conscious vs unconscious states.
    38	
    39	\begin{enumerate}\itemsep=2pt
    40	\item \textbf{Substrate is fixed by group theory once chosen.} Once
    41	  $\Rsixhundred$ is selected, $120$ vertices of uniform degree $12$
    42	  are forced by H$_4$ transitivity, the Laplacian eigenvalues
    43	  $\{0, 3, 4\Ph, 6\Ph, 12\!-\!4\Ph, 12\!-\!6\Ph, 12\!-\!3, 12\}$ in
    44	  their irrep multiplicities are forced by character theory, and
    45	  the response operator $\Cph$ is fully fixed up to the single
    46	  parameter $\Ph^{-2}$ (a stability shift for the inverse map).
    47	\item \textbf{Cortical avalanches.} Wake cascade-event power-law
    48	  exponent $\alpha = 2.252$, $95\%$ CI $[1.82, 2.86]$ ($R^{2}=0.956$),
    49	  three-way overlapping the Sleep-EDFx EEG CI $[2.50, 2.53]$
    50	  (n$=$30 subjects) and ARIA's prior cascade-pipeline CI
    51	  $[2.73, 3.25]$.
    52	\item \textbf{Six drug/sleep signatures.} On a single deterministic
    53	  trajectory at seed $42$: NREM-N3 phenomenal-intensity variance
    54	  collapse to $0.463\!\times$ wake; propofol modality-switching
    55	  $1.83\!\times$ wake; propofol continuity drop $+0.066$; propofol
    56	  $\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
    57	  recovery deterministically identical to wake; wake cascade-$\alpha$
    58	  in the SOC band.
    59	\item \textbf{Eighteen preregistered correspondences pass.}
    60	  $17/18$ at standard methodology; $18/18$ after a documented
    61	  $N\!=\!20$ deep-dive on the residual high-variance interaction
    62	  test; \emph{no preregistered threshold has been modified}.
    63	\item \textbf{Cross-domain selectivity.} The substrate functions as
    64	  a domain-invariant selective amplifier (chess $+40.6$pp leave-one-out
    65	  lift at depth $n\!=\!25$ ticks; conversation $-4.4$pp lift, within
    66	  preregistered neutrality bounds) and a maximum-symmetry deterministic
    67	  null reference for cortical functional connectivity (HCP $n\!=\!1003$:
    68	  ARIA at $-11.58\sigma$ on degree homogeneity; $+79.78\sigma$ on
    69	  participation ratio).
    70	\end{enumerate}
    71	
    72	\subsection*{What this paper does \emph{not} claim}
    73	
    74	\begin{itemize}\itemsep=2pt
    75	\item \emph{Not a uniqueness claim.} We do not claim the 600-cell is
    76	  the unique substrate consistent with these signatures. Other regular
    77	  4-polytopes (the 24-cell, the 120-cell) are an explicit ablation
    78	  build, not a discharged comparison. The 600-cell choice is post-hoc
    79	  motivated by the H$_4$ Coxeter cascade structure and biological
    80	  observables; it is not an a-priori derivation from first principles.
    81	\item \emph{Not a derivation of consciousness.} The substrate witness
    82	  shows quantitative agreement with cortical signatures; it does not
    83	  establish that the substrate \emph{is} consciousness, nor that
    84	  its dynamics implement specific phenomenal content.
    85	\item \emph{Not a selection theorem.} The companion adaptive-closure-
    86	  transport preprint~\citep{SmartAdaptiveClosureTransport2026}
    87	  proposes a 4-tuple bridge $(M, L_M, W, R_{\mathrm{hom}})$ in which
    88	  this substrate fills the $L_M$ slot. The selection of the 600-cell
    89	  as the active $M$ is conjectural in that paper and is treated as
    90	  non-load-bearing here. We do not deliver a Lyapunov function on the
    91	  reduced flow, nor a $2I$-equivariance audit of the closure operator,
    92	  nor a formal edge-space decomposition. These are listed as open
    93	  builds in~\S\ref{sec:limitations}.
    94	\item \emph{Not a circuit-level model.} The substrate is at the
    95	  architectural-algorithmic level. We do not identify which neural
    96	  populations implement context rotation or partial emission, only
    97	  that some such mechanisms appear in the substrate's preregistered
    98	  ablation matrix and exhibit strong inter-mechanism coupling.
    99	\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shifted-
   100	  Laplacian floor $\Ph^{-2} \approx 0.382$ is a design-level
   101	  stability clamp (it makes $\Cph$ strictly positive definite and
   102	  bounds the Green response). It is not derived as a theorem from a
   103	  closure functional. The companion kernel
   104	  document~\citep{SmartAriaClosureKernel2026} discusses its role.
   105	\end{itemize}
   106	
   107	\subsection*{Mapping from numerical results to admissible claims}
   108	
   109	To keep this paper inside the substrate-witness scope, we use the
   110	following claim-boundary discipline. Numerical results
   111	$\mathcal R_{\mathrm{numeric}}$ are mapped to admissible claims
   112	$\mathcal C_{\mathrm{admissible}}$ by the rule
   113	\[
   114	q\colon \mathcal R_{\mathrm{numeric}} \longrightarrow \mathcal C_{\mathrm{admissible}},
   115	\qquad
   116	\mathcal C_{\mathrm{admissible}}
   117	\;=\;\{\text{`consistent with', `inside threshold', `direction confirmed'}\}.
   118	\]
   119	We never write `the substrate \emph{is} cortex' or `derives consciousness'.
   120	A result that lands inside its preregistered threshold licenses a
   121	`consistent with' claim. A result that exceeds the preregistered
   122	threshold by an order of magnitude (e.g.\ chess $+40.6$pp vs the
   123	$+15$pp floor) licenses `decisively above prereg', not `proves'. A
   124	$\sigma$-distance result against an external null
   125	(e.g.\ $-11.58\sigma$ on HCP degree homogeneity) licenses `outside
   126	the biological distribution', not `cortex has drifted from an ideal
   127	polytope'. The claim-boundary rule is summarised in the box below
   128	and applied throughout~\S\ref{sec:results}.
   129	
   130	\medskip
   131	\begin{center}
   132	\fbox{\parbox{0.92\linewidth}{\small
   133	\textbf{What is tested / what is not claimed.}\par
   134	\emph{Tested:} 18 preregistered correspondences plus 6 drug/sleep EEG
   135	signatures, on a geometry-fixed substrate with one condition-dependent
   136	parameter $\eta$ and one graph-pinned nonlinearity, against published
   137	biological observables.\par
   138	\emph{Not claimed:} substrate uniqueness; derivation of consciousness;
   139	selection theorem on the 4-tuple bridge; circuit-level mechanistic
   140	identification; first-principles derivation of $\Ph^{-2}$ shift;
   141	that cortex \emph{is} the 600-cell.
   142	}}
   143	\end{center}
   144	
   145	\subsection*{Layout}
   146	
   147	\S\ref{sec:method} gives the provenance ledger (preregistration date,
   148	seeds, scripts, datasets, thresholds). \S\ref{sec:substrate}
   149	constructs $\Rsixhundred$ and the response operator $\Cph$, with the
   150	$\Ph^{-2}$ shift disclosed as a design-level stability clamp.
   151	\S\ref{sec:chain} adds the recurrent self-model layer above the
   152	substrate (single nonlinearity, single self-injection coupling).
   153	\S\ref{sec:results} reports the empirical tables: six drug/sleep
   154	signatures, eighteen preregistered correspondences, three-way
   155	$\alpha$-overlap. \S\ref{sec:stress} presents the C$\times$P
   156	synergy stress test ($N\!=\!3, 5, 10, 20$ trend with bootstrap
   157	$95\%$ CI). \S\ref{sec:cross_domain} reports cross-domain
   158	selectivity (chess, conversation, HCP). \S\ref{sec:discussion}
   159	discusses the substrate witness and proposes a non-load-bearing
   160	ACT bridge (without claiming a selection theorem).
   161	\S\ref{sec:limitations} enumerates limitations and the
   162	hostile-review guard matrix. \S\ref{sec:conclusion} concludes.
===== /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex =====
     1	% =====================================================================
     2	\section{Methods and provenance}\label{sec:method}
     3	% =====================================================================
     4	
     5	This section is a provenance ledger. It records, for each empirical
     6	claim downstream, the dataset, the preregistration date and document,
     7	the validation script, the seed range, the threshold, and the
     8	wallclock — the minimal information a hostile reviewer needs to
     9	reproduce or refute the claim.
    10	
    11	\subsection{Preregistration discipline}
    12	
    13	\textbf{Frozen 2026-04-18.} Eighteen quantitative predictions
    14	(P1--P18) were locked on 2026-04-18 in
    15	\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md} before any validation
    16	run. Each prediction has (i) a specific numerical claim, (ii) a
    17	falsifiable threshold, (iii) the validation test (script + seed range),
    18	and (iv) a rationale identifying what would falsify it.
    19	
    20	\textbf{Frozen 2026-04-24.} Two later batteries — H$_4$ fingerprint
    21	predictions and rung observables — were preregistered on 2026-04-24
    22	in \texttt{docs/brain\_mapping/PREREG\_H4\_FINGERPRINT.md} and
    23	\texttt{docs/brain\_mapping/PREREG\_RUNG\_OBSERVABLES.md}. \emph{We do
    24	not include those batteries in the headline 18/18 tally.} They are
    25	listed as future strengthening builds in~\S\ref{sec:limitations}.
    26	
    27	\textbf{Six EEG signatures (set B).} The drug/sleep signatures on the
    28	recurrent layer (\texttt{demo\_drug\_sleep\_v4.py}) test six
    29	independent published biological signatures (NREM-N3 variance ratio,
    30	propofol switching ratio, propofol continuity drop, propofol $\Phi$
    31	collapse, recovery reversibility, wake cascade-$\alpha$). They are
    32	not part of the P1--P18 preregistration; they are reported as a
    33	companion validation set on the recurrent layer.
    34	
    35	\textbf{No threshold has been modified post-hoc.} Where the original
    36	2026-04-20 validation reported failures (P3, P4, P13), the documented
    37	methodological refinements were
    38	(a)~increasing $N$ from $3$ to $5$ for cascade interaction terms,
    39	(b)~adding a $N\!=\!20$ deep-dive for the highest-variance interaction
    40	(P4, C$\times$P), and
    41	(c)~wiring \texttt{homeostatic\_reset(level=1.0)} between depth-sweep
    42	measurements for the chess LOO test (P13). None of these touched a
    43	preregistered threshold.
    44	
    45	\subsection{Provenance ledger}
    46	
    47	We write the provenance map as $\Pi\colon\{\text{claim id}\}
    48	\to (\text{script}, \text{seed range}, \text{dataset/source},
    49	\text{threshold}, \text{result})$.
    50	
    51	\begin{table}[ht]
    52	\centering
    53	\small
    54	\caption{Provenance ledger for the headline empirical claims.}
    55	\label{tab:provenance}
    56	\begin{tabular}{l l l l l}
    57	\toprule
    58	Claim & Script & Seed range & Dataset / source & Threshold \\
    59	\midrule
    60	P1 ($\alpha$ SOC band) & \texttt{run\_preregistered\_validation.py} & 30000--30004 & this paper & $\alpha\in[2.5, 3.5]$ \\
    61	P2 ($C$ main) & same & 30010--30014 & this paper & $\geq +0.30$ \\
    62	P3 ($|D{\times}C|$) & same & 30020--30024 & this paper & $|\cdot| < 0.20$ \\
    63	\textbf{P4 ($C{\times}P$)} & \texttt{demo\_p4\_cxp\_deep\_dive.py} & 32000--32019 & this paper & $\geq +0.10$ \\
    64	P5 ($|E|$) & \texttt{run\_preregistered\_validation.py} & 30030--30034 & this paper & $|\cdot| < 0.15$ \\
    65	P6 (real EEG $\alpha$) & same & 30100 & Sleep-EDFx~\citep{SleepEDFx} & $\alpha\in[2.0, 3.0]$ \\
    66	P7 ($W{\to}N3$ var) & same & deterministic & Sleep-EDFx ($n=24$) & $<0.70$ \\
    67	P8 ($W{\to}N3$ switch) & same & deterministic & Sleep-EDFx ($n=24$) & $<0.50$ \\
    68	P9 (chess 5-fold) & same & 30200--30204 & 32 positions, 4 cat. & $\geq 70\%$ \\
    69	P10 (chess null) & \texttt{run\_chess\_robustness.py} & 30210 & same & $\geq 50\%$ \\
    70	P11 (chess random-label) & same & 30210+ & same & $\in [15\%, 35\%]$ \\
    71	P12 (goldilocks) & \texttt{run\_preregistered\_validation.py} & with reset & same & $n\in\{15,25,40,60\}$ \\
    72	\textbf{P13 (chess sub.\ lift)} & same & with reset & same (LOO refinement) & $\geq +15$pp \\
    73	P14 (conv 5-fold) & same & 30220--30224 & 64 utt., 8 cat. & $\geq 75\%$ \\
    74	P15 ($|$conv lift$|$) & same & same & same & $|\cdot| < 10$pp \\
    75	P16 (conv null) & \texttt{run\_conversation\_robustness.py} & 30210 & same & $\geq 50\%$ \\
    76	P17 (ARIA deg std) & substrate construction & deterministic & H$_4$ theorem & $=0$ \\
    77	P18 (HCP deg std) & \texttt{run\_hcp\_validation.py} & deterministic & HCP S1200~\citep{VanEssen2013HCP} & $> 2.0$ \\
    78	\midrule
    79	Sig 1--6 (drug/sleep) & \texttt{demo\_drug\_sleep\_v4.py} & seed 42 & published biological & per-signature \\
    80	\bottomrule
    81	\end{tabular}
    82	\end{table}
    83	
    84	\subsection{Datasets and DOIs}
    85	
    86	\textbf{Sleep-EDFx (PhysioNet).} Public polysomnography
    87	recordings~\citep{SleepEDFx,PhysioNet2000}; $n=30$ subjects used for
    88	the cortical-avalanche $\alpha$ baseline; $n=24$ subjects used for
    89	the wake$\to$N3 variance and switching ratios. Cortical-avalanche
    90	fitting follows the Beggs--Plenz log-CCDF
    91	methodology~\citep{BeggsPlenz2003}.
    92	
    93	\textbf{OpenNeuro \texttt{ds005620}.} Propofol-induced loss of
    94	consciousness EEG, $n=8$~\citep{OpenNeuroDS005620},
    95	DOI \texttt{10.18112/openneuro.ds005620.v1.0.0}. Used as the
    96	empirical reference for the propofol switching ratio
    97	($2.96\!\times$ wake) in Sig~2.
    98	
    99	\textbf{OpenNeuro \texttt{ds004902}.} DMT-induced altered states
   100	EEG~\citep{OpenNeuroDS004902},
   101	DOI \texttt{10.18112/openneuro.ds004902.v1.0.8}. Background
   102	psychedelic-state reference; not load-bearing for the headline tally.
   103	
   104	\textbf{Zenodo \texttt{3992359}.} DMT EEG public
   105	release~\citep{ZenodoDMT3992359},
   106	DOI \texttt{10.5281/zenodo.3992359}. Same status as above.
   107	
   108	\textbf{HCP S1200.} Human Connectome Project
   109	S1200~\citep{VanEssen2013HCP}, ICA-50 group-averaged connectivity
   110	matrix. The preregistered test (P18) was on $n=100$ subjects for
   111	computational tractability; full-cohort $n=1003$ statistics
   112	(degree std, participation ratio, clustering coefficient $\sigma$-
   113	distances) are reported as descriptive statistics on top of the
   114	preregistered test.
   115	
   116	\textbf{Microstate baseline (qualifier).} The continuity-drop
   117	signature (Sig~3) follows the EEG microstate methodology lineage of
   118	Brodbeck et al.~\citep{Brodbeck2012Microstates} on wake/NREM
   119	microstates. Brodbeck et al.\ is not a propofol-specific paper; we
   120	use it for the underlying microstate-fragmentation methodology, not
   121	as a propofol reference. A propofol-specific microstate citation
   122	would tighten this section; we treat that as an open
   123	strengthening build.
   124	
   125	\subsection{Statistical methods}
   126	
   127	\textbf{Cascade-$\alpha$ fitting.} Power-law $\alpha$ is fit by
   128	ordinary least squares on the log-CCDF of the cascade-event size
   129	distribution, restricted to the central 80\% mass band (excluding the
   130	bottom 10\% and top 10\% to avoid extreme-tail noise). $R^{2}$ is
   131	reported on the linear fit in log-space. A cascade event is defined
   132	as an attention-vertex shift between consecutive ticks
   133	$\arg\max|\mathrm{state}_{t}|\neq \arg\max|\mathrm{state}_{t-1}|$;
   134	the event size is the $\ell^{1}$ norm of the state-difference vector
   135	at that tick. Zero-size events are excluded.
   136	
   137	\textbf{Bootstrap confidence intervals.} 95\% CIs on $\alpha$ are
   138	estimated by event-resampling bootstrap (500 resamples for the
   139	preregistered cascade-$\alpha$ tests, 2000 resamples for the
   140	$N\!=\!20$ C$\times$P deep-dive). Bootstrap RNG seed: 7919 for
   141	preregistered; 42 for the deep-dive.
   142	
   143	\textbf{Bootstrap one-sided $P$-value reporting.} For the C$\times$P
   144	deep-dive, $0/2000$ bootstrap resamples were at or below zero, and
   145	$0/2000$ were below the preregistered floor $+0.10$; we report these
   146	as $0.0000$ rather than $P=0$ to avoid the suggestion of an exact
   147	zero-probability statement on a finite resample.
   148	
   149	\textbf{Factorial interaction estimator.} For the $2{\times}2$
   150	ablation conditions $\{----, -C--, --P-, -CP-\}$, the interaction is
   151	\[
   152	\Delta_{CP}
   153	\;=\;\frac{(\alpha_{\!-CP\!-}+\alpha_{\!-\!-\!-\!-})
   154	        - (\alpha_{\!-C\!-\!-}+\alpha_{\!-\!-P\!-})}{2}.
   155	\]
   156	
   157	\textbf{$\sigma$-distance against external nulls.} For the HCP
   158	comparisons we report
   159	$Z_{m} = (m_{\mathrm{ARIA}} - \mu_{\mathrm{HCP}}) / \sigma_{\mathrm{HCP}}$
   160	on the full $n=1003$ subject distribution.
   161	
   162	\subsection{State-reset protocol}
   163	
   164	The substrate exhibits state drift: across approximately five
   165	successive depth-sweep evaluations the pressure field equilibrates
   166	to a uniform attractor and classification structure collapses to
   167	raw-feature baseline. Multi-trial benchmarks therefore require an
   168	explicit reset between successive evaluations.
   169	\texttt{kernel/dimensional\_monitor.py:DimensionalMonitor.homeostatic\_reset(level=1.0)}
   170	re-initialises pressure-field, crossed-vertex, and training state to
   171	canonical baseline. With reset between depth measurements, the chess
   172	LOO lift recovers from $+3.1$pp (without reset, on a state-drifted
   173	substrate) to $+40.6$pp (with reset, far exceeding the $+15$pp
   174	preregistered floor). The reset protocol is documented in
   175	\texttt{docs/brain\_mapping/NON\_EQUILIBRIUM\_FINDING.md}; a more
   176	generalisable lesson is recorded in \S\ref{sec:limitations}: any
   177	multi-trial benchmark on a non-stationary substrate must specify
   178	state-reset protocol.
   179	
   180	\subsection{Reproducibility commands}
   181	
   182	\begin{itemize}\itemsep=2pt
   183	\item Substrate self-test:
   184	  \texttt{python3 -c "from kernel.sigma\_orbit\_basis import \_self\_test; \_self\_test()"}.
   185	\item Six drug/sleep signatures:
   186	  \texttt{python3 demo\_drug\_sleep\_v4.py} ($\sim 30$\,s).
   187	\item C$\times$P synergy $N\!=\!20$ deep-dive:
   188	  \texttt{python3 demo\_p4\_cxp\_deep\_dive.py} ($\sim 28$\,min).
   189	\item Eighteen preregistered:
   190	  \texttt{python3 run\_preregistered\_validation.py}
   191	  ($\sim 18$\,min).
   192	\item Whole-paper repro:
   193	  \texttt{bash reproduce\_paper\_claims.sh}.
   194	\end{itemize}
   195	
   196	All scripts are deterministic given seeds. Reruns at seed $42$ on the
   197	recurrent layer should reproduce per-condition means in this paper to
   198	4~decimal places. Bootstrap CIs may differ in the 4th decimal due to
   199	NumPy version differences in the bootstrap RNG; the qualitative
   200	verdicts (CI overlaps, $P$-value thresholds) are unaffected.
===== /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex =====
     1	% =====================================================================
     2	\section{The 600-cell response substrate}\label{sec:substrate}
     3	% =====================================================================
     4	
     5	This section constructs the substrate. \S\ref{ssec:vertices}
     6	gives the vertex set. \S\ref{ssec:graph} gives the graph and its
     7	H$_4$-symmetry-forced spectrum. \S\ref{ssec:cphi} gives the response
     8	operator $\Cph$ and the $\Ph^{-2}$ stability clamp.
     9	\S\ref{ssec:shells} gives the 9-shell decomposition used for source
    10	projection. \S\ref{ssec:cascade} sketches the seven-rung cascade
    11	descent referenced by the recurrent layer in~\S\ref{sec:chain}. None
    12	of these objects depend on neural data.
    13	
    14	\subsection{Vertex construction}\label{ssec:vertices}
    15	
    16	The 600-cell $\Rsixhundred$ has $120$ vertices in
    17	$\mathbb{R}^{4}$~\citep{CoxeterRegularPolytopes,Weisstein600Cell}.
    18	With $\Ph = (1+\sqrt 5)/2$ the canonical vertex set is
    19	\begin{itemize}\itemsep=1pt
    20	\item $8$ vertices: all permutations of $(\pm 1, 0, 0, 0)$;
    21	\item $16$ vertices: all sign combinations of
    22	  $(\pm 1, \pm 1, \pm 1, \pm 1)/2$;
    23	\item $96$ vertices: all even permutations of
    24	  $(\pm \Ph, \pm 1, \pm 1/\Ph, 0)/2$.
    25	\end{itemize}
    26	All $120$ vertices lie on the unit $3$-sphere $S^{3}$. The H$_4$
    27	Coxeter group acts transitively on the vertex set; in particular,
    28	every vertex has identical local structure. Implementation:
    29	\texttt{kernel/vfd\_closure\_kernel.py:build\_600cell\_vertices}.
    30	
    31	\subsection{Graph and Laplacian spectrum}\label{ssec:graph}
    32	
    33	The substrate graph $G_{V_{600}} = (V, E)$ is built by connecting each
    34	vertex to its nearest neighbours under the Euclidean metric on $S^{3}$.
    35	H$_4$ acts transitively on the vertex set, forcing uniformity of the
    36	local structure; the eigenvalue multiplicities follow from H$_4$
    37	character theory on the regular representation. The construction and
    38	spectrum are standard~\citep{CoxeterRegularPolytopes,Weisstein600Cell}.
    39	\begin{lemma}[600-cell graph facts]\label{lem:600cell}
    40	The graph $G_{V_{600}}$ has $|V|=120$ vertices, $|E|=720$ edges, every
    41	vertex has degree exactly $12$, and the unweighted graph Laplacian
    42	$\Lop = D - A$ has spectrum
    43	\[
    44	\sigma(\Lop) \;=\;
    45	\bigl\{0^{1}, 3^{4}, 4\Ph^{9}, 6\Ph^{16}, (12\!-\!4\Ph)^{9},
    46	       (12\!-\!6\Ph)^{16}, 9^{4}, 12^{1}\bigr\},
    47	\]
    48	where the exponent denotes multiplicity. The decomposition into H$_4$
    49	irreducible representations is exact at machine precision; the
    50	$\sigma$-orbit projector basis (\texttt{kernel/sigma\_orbit\_basis.py})
    51	realises it block-by-block with cross-block norm $<10^{-15}$.
    52	\end{lemma}
    53	
    54	The non-trivial eigenmodes partition into Coxeter exponent classes.
    55	For H$_4$ proper, the exponents are $\{1, 11, 19, 29\}$; for the
    56	Galois twin $\sigma(\mathrm{H}_4)$ under the $\sigma$-automorphism of
    57	$\mathbb{Z}[\Ph]$, the exponents become $\{7, 13, 17, 23\}$. We label
    58	the eigenspaces $K_{1}, K_{11}, K_{19}, K_{29}$ for H$_4$-proper modes
    59	and $K_{7}, K_{13}, K_{17}, K_{23}$ for $\sigma$-twin modes. The
    60	multiplicities follow from character theory and are reproduced in
    61	the implementation
    62	(\texttt{kernel/sigma\_orbit\_basis.py:\_self\_test}). The
    63	$K_{7}$-modes will be the dominant phenomenal-binding profile in
    64	\S\ref{sec:chain}.
    65	
    66	\subsection{The shifted-Laplacian response \texorpdfstring{$\Cph$}{C\_phi}}\label{ssec:cphi}
    67	
    68	The substrate's linear response to an external source $f \in \mathbb{R}^{120}$
    69	is the discrete Green's function of the shifted Laplacian:
    70	\begin{equation}\label{eq:cphi}
    71	\Cph \;=\; \Lop + \Ph^{-2} I,
    72	\qquad
    73	\psi \;=\; \Cph^{-1} f.
    74	\end{equation}
    75	The shift $\Ph^{-2} \approx 0.382$ is a design-level stability
    76	clamp: it makes $\Cph$ strictly positive definite (smallest eigenvalue
    77	$\Ph^{-2}$, since the trivial Laplacian eigenvalue is $0$), so that the
    78	inverse is bounded with operator norm $\Ph^{2}\approx 2.618$. This is
    79	\emph{not} a derived theorem; it is a stability choice. The companion
    80	kernel document~\citep{SmartAriaClosureKernel2026} discusses the same
    81	$\Cph$ as the basis for an independent passive-regime witness in
    82	flavour physics~\citep{SmartBAnomaly2026}, where the same operator
    83	form (without retuning the shift) describes the
    84	$B\to K^{*}\mu^{+}\mu^{-}$ angular anomaly across five public datasets.
    85	This paper imports $\Cph$ from that line; we do not re-derive it.
    86	
    87	The response $\psi = \Cph^{-1} f$ is smooth in $f$. By itself it does
    88	not produce critical-state cascade statistics; the recurrent layer
    89	in~\S\ref{sec:chain} adds a graph-pinned nonlinearity
    90	$\mathrm{bounded\_topk}(\psi, k\!=\!12)$ to obtain self-organised-critical
    91	event distributions. The choice $k\!=\!12$ is the average degree of
    92	$G_{V_{600}}$ (Lemma~\ref{lem:600cell}), pinned by the substrate, not
    93	fitted to any dataset.
    94	
    95	\paragraph{Disclosure (substrate-witness scope).}
    96	The $\Ph^{-2}$ floor is a stability shift, not a derived parameter.
    97	The bounded-top-$K$ nonlinearity uses $k\!=\!12$ pinned to the graph's
    98	average degree, not a fitted threshold. No other shape parameter
    99	enters. The condition-dependent self-injection coupling
   100	$\eta\in\{0, 0.05, 0.20\}$ is the only architectural parameter that
   101	varies between conditions in~\S\ref{sec:chain}; it is reported
   102	explicitly per condition.
   103	
   104	\subsection{Shell decomposition}\label{ssec:shells}
   105	
   106	Under the H$_3$ subgroup, the $120$ vertices partition into $9$
   107	spherical shells indexed by Euclidean inner product with a chosen pole:
   108	\[
   109	\bigl(|S_0|,\ldots,|S_8|\bigr) \;=\; (1, 12, 20, 12, 30, 12, 20, 12, 1).
   110	\]
   111	The middle shell $S_{4}$ has $30$ vertices on the equatorial plane
   112	(the icosidodecahedral ring). When projecting onto a continuum kernel
   113	in companion preprints~\citep{SmartAriaClosureKernel2026}, the
   114	shell-mean projection of the equatorial-source response,
   115	$\kappa(x) = \mathrm{shell\text{-}mean}[\Cph^{-1} f_{\mathrm{equat}}](x)$,
   116	collapses on the continuum exponential $\frac{\Ph}{2}\,e^{-|x|/\Ph}$.
   117	This paper does not use that continuum projection; we work with the
   118	discrete operator throughout.
   119	
   120	\subsection{Cascade descent (sketch)}\label{ssec:cascade}
   121	
   122	The recurrent layer in~\S\ref{sec:chain} references a cascade
   123	decomposition $E_{8}\to H_{4}\to H_{3}\to D_{4}\to \mathrm{Cl}(1,3)
   124	\to S^{7}\to 0$, implemented in
   125	\texttt{kernel/cascade\_descent.py:descend\_operator\_e8\_to\_h4\_clean}.
   126	An arbitrary operator on the $E_{8}$ root system descends to the
   127	4-D H$_4$ subspace through a sequence of orthogonal projections, each
   128	preserving the Frobenius norm to within $10^{-15}$. The
   129	$\sigma$-orbit projector basis from
   130	\texttt{kernel/sigma\_orbit\_basis.py} gives the K-class block
   131	decomposition at machine precision.
   132	
   133	The descent provides numerical stability for the cascade ablations:
   134	when one ablates a specific K-class contribution (e.g.\ $K_{7}$), the
   135	remaining operator structure is exactly preserved. We do not claim
   136	the cascade itself is forced by physics on a pre-substrate level; the
   137	cascade is a decomposition of operators on $\Rsixhundred$, and the
   138	choice of $\Rsixhundred$ as the active substrate is post-hoc justified
   139	by the empirical correspondences in~\S\ref{sec:results}.
   140	
   141	\subsection{What the substrate is fixed-by, and what it is not}
   142	
   143	\begin{itemize}\itemsep=2pt
   144	\item Fixed by group theory once $\Rsixhundred$ is chosen: $|V|=120$,
   145	  uniform degree $12$, Laplacian spectrum, $9$-shell partition, K-class
   146	  irrep block structure, average degree $k\!=\!12$, $\sigma$-twin pairing.
   147	\item Fixed by stability choice: the $\Ph^{-2}$ shift in $\Cph$. This
   148	  is not a derivation; it is a design-level clamp that bounds the
   149	  response inverse.
   150	\item Not fixed by this paper: the choice of $\Rsixhundred$ over the
   151	  $24$-cell or $120$-cell. The choice is post-hoc motivated by the H$_4$
   152	  cascade structure and the empirical correspondences. A formal
   153	  ablation against alternative regular 4-polytopes is an open build
   154	  (\S\ref{sec:limitations}).
   155	\end{itemize}
===== /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex =====
     1	% =====================================================================
     2	\section{The recurrent layer}\label{sec:chain}
     3	% =====================================================================
     4	
     5	The cascade-pipeline substrate (\S\ref{sec:substrate}) reproduces
     6	cortical-avalanche statistics matching real EEG (\S\ref{sec:results}).
     7	To test high-level signatures — NREM-N3 variance collapse, propofol
     8	regime-switching, propofol $\Phi$ collapse — we add a recurrent
     9	self-model layer above the substrate. The layer adds one
    10	graph-pinned nonlinearity, one condition-dependent self-injection
    11	coupling $\eta$, and four trajectory observables. No shape parameter
    12	is fit to any neural dataset.
    13	
    14	This section is method, not metaphysics. We do not claim the
    15	recurrent layer ``is'' consciousness; we report which numerical
    16	observables on the layer's trajectory match published biological
    17	signatures in~\S\ref{sec:results}.
    18	
    19	\subsection{The recurrent loop}
    20	
    21	Implementation: \texttt{kernel/self\_model\_stream.py:SelfModelLoop}.
    22	At each tick $t$ the substrate state evolves as
    23	\begin{align}
    24	f_{\mathrm{total}}(t) &= f_{\mathrm{ext}}(t) + \eta\cdot f_{\mathrm{self}}(\mathrm{snap}_{t-1}, \psi_{t-1}), \\
    25	\psi_{t} &= \Cph^{-1}\, f_{\mathrm{total}}(t), \\
    26	\psi^{\mathrm{thr}}_{t} &= \mathrm{bounded\_topk}(\psi_{t}, k=12), \\
    27	\mathrm{state}_{t} &= \mathrm{decay}\cdot\mathrm{state}_{t-1} + (1-\mathrm{decay})\cdot \psi^{\mathrm{thr}}_{t}, \\
    28	\mathrm{snap}_{t} &= \mathrm{bind\_phenomenal\_field}(\psi_{t}, \texttt{profile=K\_7\_only}),
    29	\end{align}
    30	with $\mathrm{decay}=0.95$ (state EMA factor) and $\eta$ the only
    31	condition-dependent architectural parameter. $f_{\mathrm{self}}$ maps
    32	the prior phenomenal snapshot to a directional source weighted by
    33	ignition $\times$ intensity (cosine direction alignment with the
    34	prior snapshot). The substrate response operator $\Cph$ is unchanged
    35	across all conditions.
    36	
    37	Conditions:
    38	\begin{itemize}\itemsep=2pt
    39	\item $\eta = 0.20$ for WAKE and RECOVERY (active recurrent self-loop);
    40	\item $\eta = 0.05$ for SLEEP\_N3 (attenuated self-loop);
    41	\item $\eta = 0.00$ for PROPOFOL (broken recurrence; residual cortex
    42	  preserved as background drive).
    43	\end{itemize}
    44	
    45	\subsection{The graph-pinned nonlinearity}
    46	
    47	\textbf{$\mathrm{bounded\_topk}(\psi, k=12)$.} This is the load-bearing
    48	nonlinearity, implemented in
    49	\texttt{kernel/lyapunov\_selector.py:bounded\_topk}: zero all but the
    50	top-$12$ vertex amplitudes (by absolute value), and rescale the rest
    51	to a small fraction of their baseline. Linear Green response alone
    52	gives smooth dynamics with cascade $\alpha\approx 1.09$ — no
    53	avalanches. Adding bounded-top-$K$ at $k=12$ drives $\alpha$ into the
    54	SOC band $(2.0, 3.5)$ with $R^{2}>0.85$.
    55	
    56	\textbf{Why $k=12$.} The choice $k=12$ is the average degree of
    57	$G_{V_{600}}$ (Lemma~\ref{lem:600cell}), pinned by the substrate
    58	geometry, not by neural data. Smaller $k$ (e.g.\ $k=6$) gives $\alpha$
    59	at the band edge with poorer fit; larger $k$ ($24, 48$) gives $\alpha$
    60	above band or with degraded fit. We do not search $k$ over a fitted
    61	window; $k$ is determined by the graph.
    62	
    63	\subsection{The integrated-information proxy
    64	            \texorpdfstring{$\Phi$}{Phi}}
    65	
    66	Implementation:
    67	\texttt{kernel/consciousness\_binding.py:phi\_iit\_trajectory}.
    68	Given the state history matrix $S\in\mathbb{R}^{T\times 120}$, write
    69	$A = S\cdot V$ for the H$_4$-eigenvector matrix $V$ (mode amplitudes
    70	$A\in\mathbb{R}^{T\times 120}$). Define $c_{\mathrm{full}}$ as the
    71	lag-$1$ auto-correlation of the full system, and $c_{k}$ as the
    72	lag-$1$ auto-correlation within the K-class irrep block $k$. Then
    73	\[
    74	\Phi \;=\; \max\!\bigl(0,\; |c_{\mathrm{full}}| - \mathrm{mean}_{k}\,|c_{k}|\bigr).
    75	\]
    76	By construction $\Phi\to 0$ under H$_{4}$-equivariant dynamics, since
    77	group symmetry forbids information transport across irrep classes;
    78	$\Phi > 0$ only when the dynamics break symmetry and transport
    79	information across class boundaries. This is a port of the published
    80	\texttt{integrated\_information\_phi\_irrep} proxy from the cascade
    81	pipeline, adapted to take amplitude trajectories from any source.
    82	
    83	We position $\Phi$ as an IIT-style direction-of-effect proxy, not as
    84	a full implementation of IIT. ARIA does not implement cause-effect
    85	repertoires, exclusion postulate, or integration-over-partitions
    86	machinery~\citep{Tononi2008,BalduzziTononi2008}. The propofol $\Phi$
    87	collapse in~\S\ref{sec:results} is consistent with the IIT direction
    88	of effect on the propofol-vs-wake state contrast; it is not a
    89	discharge of the IIT axioms.
    90	
    91	\subsection{The continuity composite}
    92	
    93	Implementation:
    94	\texttt{kernel/self\_model\_stream.py:StreamContinuityScorer}.
    95	A composite first-person continuity score over a 64-tick rolling
    96	window:
    97	\begin{align*}
    98	b_{\mathrm{cont}} &= \mathrm{mean\ cos\text{-}sim\ of\ consecutive}\ (I, L, P)\,\mathrm{vectors},\\
    99	v_{\mathrm{cont}} &= 1/(1 + 4\cdot \mathrm{var}(\mathrm{valence})),\\
   100	m_{\mathrm{pers}} &= \mathrm{frac.\ of\ consecutive\ same\text{-}modality\ ticks},\\
   101	i_{\mathrm{smooth}} &= 1/(1 + 4\cdot \mathrm{TV}(\mathrm{intensity})),\\
   102	\mathrm{composite} &= 0.35\cdot b_{\mathrm{cont}} + 0.25\cdot v_{\mathrm{cont}} + 0.20\cdot m_{\mathrm{pers}} + 0.20\cdot i_{\mathrm{smooth}}.
   103	\end{align*}
   104	This composite produces the propofol continuity-drop signature
   105	(WAKE composite $0.943$; PROPOFOL composite $0.877$;
   106	drop $+0.066$).
   107	
   108	\subsection{The phenomenal-field binding}
   109	
   110	Implementation:
   111	\texttt{kernel/consciousness\_binding.py:bind\_phenomenal\_field}.
   112	The substrate state $\psi_{t}$ is mapped to a phenomenal snapshot
   113	with channels (intensity $I$, self-luminosity $L$, presence $P$,
   114	valence, modality\_label). The modality\_label is determined by which
   115	H$_4$ K-class dominates the isotypic compression of $\psi_{t}$ under
   116	the $\sigma$-orbit projector basis. The default profile
   117	\texttt{K\_7\_only} restricts to $\sigma$-twin K-classes for modality
   118	labelling; H$_4$-proper classes contribute amplitude bias.
   119	
   120	\subsection{Stimulus models}
   121	
   122	Implementation: \texttt{demo\_drug\_sleep\_v4.py}. Four conditions
   123	$\times$ $800$ ticks each at seed $42$:
   124	
   125	\textbf{WAKE.} AR(1) cortical noise ($\beta=0.90$), tonic equator-shell
   126	coherence (small always-on bias), and attention episodes (20--50
   127	ticks at amplitude $0.8$, anchored to the largest shell with $15\%$
   128	within-shell rotation per tick). The AR(1) gives temporal correlation
   129	that lets the $\eta=0.20$ self-loop integrate; tonic coherence anchors
   130	modality; attention episodes mimic biological visual fixation
   131	(200--400~ms dwell time analogue); within-shell rotation generates
   132	cascade events without changing modality.
   133	
   134	\textbf{SLEEP\_N3.} Slow oscillation ($\sim 1$\,Hz analogue,
   135	amplitude $1.0$) on a coherent shell, plus spindle bursts ($12$ ticks
   136	every $100$ at amplitude $0.4$ fast modulation), plus K-complexes
   137	($4\%$ of ticks at amplitude $0.8$).
   138	
   139	\textbf{PROPOFOL.} Low-amplitude tonic noise (amplitude $0.05$);
   140	$\eta = 0.00$ (broken recurrence). Residual cortex preserved as
   141	background drive.
   142	
   143	\textbf{RECOVERY.} Identical to WAKE — verifies determinism and
   144	reversibility.
   145	
   146	The stimulus models are deliberately structural rather than
   147	measurement-fitted: amplitudes and durations match published
   148	biological time scales but are not tuned to specific signatures.
   149	The full stimulus code is \texttt{demo\_drug\_sleep\_v4.py}. We
   150	disclose stimulus-shape choice as a methodological design move,
   151	not a derived theorem.
   152	
   153	\subsection{Cascade-mechanism ablation matrix}
   154	
   155	The cascade dynamics on the substrate use four mechanisms acting on
   156	the pressure field, each ablatable independently. The $2^{4}$
   157	ablation grid is the basis for the preregistered tests P1--P5 and
   158	the C$\times$P stress test in~\S\ref{sec:stress}.
   159	
   160	\textbf{$D$ — D$_{4}$ orbit coupling.} The H$_4$ root system contains
   161	five disjoint 24-cells (D$_4$ orbits). $D$ adds a small
   162	(coupling $0.05$) cross-orbit pressure averaging that prevents
   163	cascades from localising to one orbit.
   164	Implementation: \texttt{kernel/dimensional\_monitor.py:300-305}.
   165	
   166	\textbf{$C$ — Context rotation (S$^{7}$ observer frames).} The active
   167	observer frame on the S$^{7}$ rung rotates periodically based on
   168	which uncrossed vertices have accumulated pressure aligning with
   169	each frame's preferences. This creates churn in \emph{which}
   170	vertices are uncrossed at any tick.
   171	Implementation: \texttt{kernel/dimensional\_monitor.py:316-318, 823-827}.
   172	
   173	\textbf{$P$ — Partial emission.} High-pressure uncrossed vertices
   174	(above threshold but not yet crossed) emit pressure at $30\%$ scale,
   175	saturating at pressure $3.0$. Without this mechanism, only fully-
   176	crossed vertices emit.
   177	Implementation: \texttt{kernel/dimensional\_monitor.py:842-855}.
   178	
   179	\textbf{$E$ — Equator compensation.} The H$_3$ shell-4 equator is a
   180	30-vertex icosidodecahedral ring with split degree distribution.
   181	$E$ scales pressure gain by $(\bar d / d_{v})$ so sparse commissural
   182	vertices overcome their connectivity deficit.
   183	Implementation: \texttt{kernel/dimensional\_monitor.py:320-360}.
   184	
   185	The four mechanisms are pinned to the substrate's geometry (D$_4$
   186	orbits, S$^{7}$ rung, equatorial shell) — they are not free dynamical
   187	choices. Their causal effects are reported in~\S\ref{sec:stress}.
===== /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex =====
     1	% =====================================================================
     2	\section{Results}\label{sec:results}
     3	% =====================================================================
     4	
     5	This section is the empirical core. \S\ref{ssec:six_signatures}
     6	gives the six drug/sleep EEG signatures on the recurrent layer
     7	(set B). \S\ref{ssec:eighteen_prereg} gives the eighteen
     8	preregistered correspondences (set A). \S\ref{ssec:alpha_overlap}
     9	gives the three-way $\alpha$ overlap. We lift the result map
    10	$R\colon (\text{condition / test id}) \to \text{(scalar, threshold,
    11	verdict)}$ verbatim from the validation outputs without
    12	recomputation; sources are
    13	\texttt{docs/brain\_mapping/CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}
    14	and \texttt{docs/brain\_mapping/VALIDATION\_RESULTS\_2026-04-29.md}.
    15	
    16	\subsection{Six drug/sleep EEG signatures}\label{ssec:six_signatures}
    17	
    18	\textbf{Setup.} Four conditions $\times$ $800$ ticks at seed $42$,
    19	$k_{\mathrm{thr}}=12$, single deterministic substrate
    20	(\S\ref{sec:chain}). Per-condition trajectory observables are
    21	$(n_{\mathrm{evt}}, \alpha, \mathrm{CI}_{95}, R^{2}, I_{\mathrm{var}},
    22	\Phi_{\mathrm{traj}}, \mathrm{cont})$.
    23	
    24	\begin{table}[ht]
    25	\centering
    26	\small
    27	\caption{Per-condition trajectory observables (\texttt{demo\_drug\_sleep\_v4.py},
    28	seed 42).}
    29	\label{tab:per_condition}
    30	\begin{tabular}{l r r l r r r r}
    31	\toprule
    32	condition & $n_{\mathrm{evt}}$ & $\alpha$ & 95\% CI & $R^{2}$ & $I_{\mathrm{var}}$ & $\Phi_{\mathrm{traj}}$ & cont \\
    33	\midrule
    34	WAKE      & $58$  & $2.252$ & $[1.82, 2.86]$ & $0.956$ & $2.18\!\times\!10^{-5}$ & $0.0008$ & $0.943$ \\
    35	SLEEP\_N3 & $111$ & $3.250$ & $[2.44, 4.14]$ & $0.886$ & $1.01\!\times\!10^{-5}$ & $0.0055$ & $0.980$ \\
    36	PROPOFOL  & $246$ & $2.758$ & $[2.52, 3.09]$ & $0.931$ & $5.37\!\times\!10^{-6}$ & $0.0003$ & $0.877$ \\
    37	RECOVERY  & $58$  & $2.252$ & $[1.82, 2.86]$ & $0.956$ & $2.18\!\times\!10^{-5}$ & $0.0008$ & $0.943$ \\
    38	\bottomrule
    39	\end{tabular}
    40	\end{table}
    41	
    42	\begin{table}[ht]
    43	\centering
    44	\small
    45	\caption{Six drug/sleep signatures with published references.}
    46	\label{tab:six_signatures}
    47	\begin{tabular}{c l l c c l}
    48	\toprule
    49	\# & Signature & Reference & Predicted & Observed & Verdict \\
    50	\midrule
    51	1 & NREM-N3 var ratio (vs Wake) &
    52	   Sleep-EDFx W$\to$N3 ($n=24$)~\citep{SleepEDFx} &
    53	   $\approx 0.365$ & $0.463$ & $\checkmark$ \\
    54	2 & Propofol switching ratio &
    55	   OpenNeuro \texttt{ds005620} ($n=8$, $2.96{\times}$)~\citep{OpenNeuroDS005620} &
    56	   $\in[1.5, 5.0]$ & $1.83\times$ & $\checkmark$ \\
    57	3 & Propofol continuity drop &
    58	   EEG microstate~\citep{Brodbeck2012Microstates} &
    59	   $> 0.020$ & $+0.066$ & $\checkmark$ \\
    60	4 & Propofol $\Phi$ collapse (IIT) &
    61	   Tononi 2008~\citep{Tononi2008} &
    62	   ratio $< 0.50$ & $0.33\times$ & $\checkmark$ \\
    63	5 & Recovery reversibility &
    64	   clinical anaesthesia &
    65	   identical to wake & $0$ diff & $\checkmark$ \\
    66	6 & Wake cortical-avalanche $\alpha$ &
    67	   Sleep-EDFx $n=30$ CI~$[2.50, 2.53]$~\citep{BeggsPlenz2003,SleepEDFx} &
    68	   $\alpha\!\in\![1.5, 3.5]$, $R^{2}\!>\!0.85$ &
    69	   $2.252$ $[1.82, 2.86]$ $R^{2}\!=\!0.956$ &
    70	   $\checkmark$ \\
    71	\bottomrule
    72	\end{tabular}
    73	\end{table}
    74	
    75	All six signatures pass against their published-reference thresholds
    76	on the same deterministic substrate trajectory. The six signatures
    77	are not part of the dated 2026-04-18 P1--P18 preregistration; they
    78	were tested on a recurrent-layer architecture redesigned at v4 with
    79	biologically-motivated condition-specific stimulus models
    80	(\S\ref{sec:chain}; \texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}
    81	documents the v3$\to$v4 stimulus redesign). The mechanistic readings
    82	in \texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md} are not
    83	load-bearing for the headline claim. Single-seed disclosure:
    84	\S\ref{sec:limitations}~\ref{ssec:regime}.
    85	
    86	\subsection{Eighteen preregistered correspondences}\label{ssec:eighteen_prereg}
    87	
    88	\textbf{Tally.} $17/18$ at standard validation
    89	(\texttt{run\_preregistered\_validation.py}, $5$-seed cascade block
    90	plus state-reset protocol); $18/18$ after the $N\!=\!20$ deep-dive
    91	on the residual P4 (\texttt{demo\_p4\_cxp\_deep\_dive.py}, seed range
    92	$32000$--$32019$). \emph{No preregistered threshold has been modified.}
    93	
    94	\begin{table}[ht]
    95	\centering
    96	\small
    97	\caption{All eighteen preregistered correspondences, frozen 2026-04-18.}
    98	\label{tab:eighteen_prereg}
    99	\begin{tabular}{l l l l l}
   100	\toprule
   101	ID & Test & Threshold & Observed (2026-04-29) & Verdict \\
   102	\midrule
   103	P1  & Cascade $\alpha$ SOC range            & $\in [2.5, 3.5]$ & $2.958$ & $\checkmark$ \\
   104	P2  & $C$ main effect                        & $\geq +0.30$     & $+0.621$ & $\checkmark$ \\
   105	P3  & $|D{\times}C|$ (independence)          & $|\cdot| < 0.20$ & $-0.183$ ($N\!=\!5$) & $\checkmark$ \\
   106	\textbf{P4} & $C{\times}P$ synergy           & $\geq +0.10$     &
   107	   $+0.190$ \, CI $[+0.143, +0.239]$ ($N\!=\!20$) & $\checkmark$ \\
   108	P5  & $|E|$ main effect (null)               & $|\cdot| < 0.15$ & $+0.046$ & $\checkmark$ \\
   109	P6  & Real EEG $\alpha$                      & $\in [2.0, 3.0]$ & $2.513$ & $\checkmark$ \\
   110	P7  & W$\!\to\!$N3 variance ratio            & $< 0.70$         & $0.365$ & $\checkmark$ \\
   111	P8  & W$\!\to\!$N3 switching ratio           & $< 0.50$         & $0.058$ & $\checkmark$ \\
   112	P9  & Chess 5-fold CV                        & $\geq 70\%$      & $83.1\%$ & $\checkmark$ \\
   113	P10 & Chess null mapping                     & $\geq 50\%$      & $65.4\%$ & $\checkmark$ \\
   114	P11 & Chess random-label                     & $\in [15\%, 35\%]$ & $23.4\%$ & $\checkmark$ \\
   115	P12 & Chess goldilocks peak                  & $\in \{15, 25, 40, 60\}$ & $n=25$ & $\checkmark$ \\
   116	\textbf{P13} & Chess substrate lift (5-fold CV preregistered; LOO refinement, with reset) & $\geq +15$pp & $+40.6$pp (LOO) & $\checkmark$ \\
   117	P14 & Conv raw 5-fold CV                     & $\geq 75\%$      & $87.5\%$ & $\checkmark$ \\
   118	P15 & $|$conv lift$|$                        & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
   119	P16 & Conv null mapping                      & $\geq 50\%$      & $70.6\%$ & $\checkmark$ \\
   120	P17 & ARIA degree std (theorem)              & $= 0$            & $0.0000$ & $\checkmark$ \\
   121	P18 & HCP degree std                         & $> 2.0$          & $3.388$ & $\checkmark$ \\
   122	\bottomrule
   123	\end{tabular}
   124	\end{table}
   125	
   126	\textbf{Three predictions that flipped to PASS, with documented
   127	methodology refinement (no threshold change).}
   128	\begin{itemize}\itemsep=2pt
   129	\item P3 (D$\times$C interaction independence) was outside the band
   130	  at $N\!=\!3$ ($-0.231$) and inside the band at $N\!=\!5$ ($-0.183$).
   131	  Reading: consistent with an underpowered interaction estimate at
   132	  $N\!=\!3$ on a high-per-seed-variance interaction term.
   133	\item P4 (C$\times$P synergy) was below threshold at $N\!=\!3$
   134	  ($+0.044$) and at $N\!=\!5$ ($+0.039$); the $N\!=\!20$ deep-dive
   135	  (\S\ref{sec:stress}) gives $+0.190$ with $95\%$ CI
   136	  $[+0.143, +0.239]$, decisively above the $\geq +0.10$ floor.
   137	\item P13 (chess substrate lift): the 2026-04-18 preregistration
   138	  (\texttt{PAPER\_PREDICTIONS.md:115-120}) specified the estimator as
   139	  $5$-fold CV with threshold $\geq +15$pp at $n=25$. The 2026-04-29
   140	  validation strengthened the estimator to LOO with state reset, a
   141	  stricter test at the same threshold; the LOO lift was $+3.1$pp
   142	  without state reset on a state-drifted substrate, and $+40.6$pp
   143	  with \texttt{homeostatic\_reset(level=1.0)} between depth measurements
   144	  (\S\ref{sec:method}; \texttt{NON\_EQUILIBRIUM\_FINDING.md}). We
   145	  report this as a \emph{validation-protocol refinement on the
   146	  preregistered estimator}, not as preregistration revision.
   147	\end{itemize}
   148	
   149	\textbf{Headline verdict.} Eighteen preregistered correspondences
   150	all pass at preregistered thresholds, with two interaction tests
   151	requiring $N\!\geq\!5$ and one requiring $N\!=\!20$ for reliable
   152	detection of high-variance interaction terms, and one test
   153	requiring the documented state-reset protocol. The original $15/18$
   154	result was a methodology-limited tally, not a content failure.
   155	
   156	\subsection{Three-way \texorpdfstring{$\alpha$}{alpha} overlap}\label{ssec:alpha_overlap}
   157	
   158	The substrate's wake cascade-$\alpha$ confidence interval overlaps
   159	\emph{three independent reference ranges} simultaneously:
   160	
   161	\begin{table}[ht]
   162	\centering
   163	\small
   164	\caption{Three-way $\alpha$ overlap on the wake cascade-event power
   165	law.}
   166	\label{tab:alpha_overlap}
   167	\begin{tabular}{l c l c}
   168	\toprule
   169	Source & $\alpha$ & 95\% CI & $n$ \\
   170	\midrule
   171	ARIA cascade-pipeline baseline ($N=5$) & $2.958$  & inside $[2.5, 3.5]$ & 5 seeds \\
   172	Real EEG (Sleep-EDFx, $n=30$ subjects)~\citep{SleepEDFx} & $2.51$ & $[2.50, 2.53]$ & 30 \\
   173	ARIA prior cascade pipeline ($n=4$ subjects) & $2.85$ & $[2.73, 3.25]$ & per-subject \\
   174	\textbf{v4 WAKE consciousness chain} & $\mathbf{2.252}$ & $[\mathbf{1.82, 2.86}]$ & 58 events \\
   175	\bottomrule
   176	\end{tabular}
   177	\end{table}
   178	
   179	The v4 WAKE 95\% CI $[1.82, 2.86]$ contains the upper arm of the
   180	real Sleep-EDFx EEG CI $[2.50, 2.53]$, overlaps the ARIA prior
   181	cascade pipeline CI $[2.73, 3.25]$ on the interval $[2.73, 2.86]$,
   182	and lies inside the cortical-avalanche band
   183	$\alpha\!\in\![1.5, 3.5]$~\citep{BeggsPlenz2003}. The pairwise
   184	intersections (WAKE $\cap$ Sleep-EDFx, WAKE $\cap$ prior pipeline,
   185	WAKE $\cap$ cortical-avalanche band) are non-empty across three
   186	independent reference ranges.
   187	
   188	\textbf{Reading.} The substrate produces self-organised-critical
   189	cascade statistics matching the cortical-avalanche literature with
   190	no fitted parameter on neural data. The bounded-top-$K$ at
   191	$k=12$ is pinned to the substrate's average degree
   192	(Lemma~\ref{lem:600cell}); the $\Ph^{-2}$ shift in $\Cph$ is a
   193	stability clamp (\S\ref{ssec:cphi}); the AR(1) WAKE input has
   194	biological time-scale parameters but is not measurement-fitted to
   195	any specific subject (\S\ref{sec:chain}). Three-way overlap on the
   196	power-law exponent is the strongest single empirical anchor in the
   197	paper.
===== /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex =====
     1	% =====================================================================
     2	\section{Stress test: the C\texorpdfstring{$\times$}{x}P synergy at adequate
     3	         replication}\label{sec:stress}
     4	% =====================================================================
     5	
     6	This section is the C$\times$P interaction stress test. The original
     7	preregistered prediction was P4: $C\times P$ interaction
     8	$\Delta_{CP} \geq +0.10$ on cascade-$\alpha$. The 2026-04-20
     9	$N\!=\!3$ validation gave $+0.044$ — below the threshold — and the
    10	architectural claim ``C and P synergise on cascade-state stability''
    11	was walked back. Closing this gap without modifying the preregistered
    12	threshold required (a) re-evaluating the $N\!=\!3$ point estimate as
    13	consistent with an underpowered interaction estimate, (b) tracking
    14	the estimate's behaviour across $N$, and (c) bootstrapping a
    15	confidence interval on a fresh-seed $N\!=\!20$ sample. We did all
    16	three.
    17	
    18	\subsection{The factorial estimator}
    19	
    20	For the four ablation conditions $\{----, -C--, --P-, -CP-\}$
    21	(\S\ref{sec:chain}), the $C\times P$ interaction estimate is the
    22	standard $2\times 2$ factorial difference:
    23	\[
    24	\Delta_{CP}
    25	\;=\;\frac{(\alpha_{\!-CP\!-}+\alpha_{\!-\!-\!-\!-})
    26	        - (\alpha_{\!-C\!-\!-}+\alpha_{\!-\!-P\!-})}{2}.
    27	\]
    28	Per-seed paired estimates use the same formula on a single seed's
    29	four conditions.
    30	
    31	\subsection{The trend across \texorpdfstring{$N$}{N}}
    32	
    33	\begin{table}[ht]
    34	\centering
    35	\small
    36	\caption{$C\times P$ interaction estimate as a function of $N$.}
    37	\label{tab:cxp_trend}
    38	\begin{tabular}{r l r l l}
    39	\toprule
    40	$N$ & Seeds & Estimate $\Delta_{CP}$ & 95\% CI & Verdict vs $\geq +0.10$ \\
    41	\midrule
    42	$3$  & $30040$--$30042$ & $+0.044$ & --- & $\times$ original prereg \\
    43	$5$  & $30040$--$30044$ & $+0.039$ & --- & $\times$ this session re-run \\
    44	$10$ & $31000$--$31009$ & $+0.088$ & $[-0.002, +0.174]$ & borderline \\
    45	$\mathbf{20}$ & $\mathbf{32000\text{--}32019}$ & $\mathbf{+0.190}$
    46	       & $\mathbf{[+0.143, +0.239]}$ & $\checkmark$ decisively above \\
    47	\bottomrule
    48	\end{tabular}
    49	\end{table}
    50	
    51	The estimate remains small at $N\!=\!3$ and $N\!=\!5$
    52	($+0.044, +0.039$) and rises at $N\!=\!10$ and $N\!=\!20$
    53	($+0.088, +0.190$). Per-seed std at $N\!=\!10$ was $0.159$; at
    54	$N\!=\!20$ it dropped to $0.089$ — the $N\!=\!10$ sample landed on
    55	outliers; the $N\!=\!20$ sample reveals a clean narrow positive
    56	distribution.
    57	
    58	\subsection{The \texorpdfstring{$N\!=\!20$}{N=20} fresh-seed estimate}
    59	
    60	\textbf{Setup.} $4$ conditions $\times$ $20$ fresh seeds (range
    61	$32000$--$32019$, non-overlapping with original validation seeds in
    62	the $30000$s), $150$ epochs per run. All other ablation flags off
    63	($D, E$ held on). Bootstrap $n_{\mathrm{resamples}}\!=\!2000$,
    64	seed $42$. Wallclock $1706$\,s on a single CPU
    65	(\texttt{demo\_p4\_cxp\_deep\_dive.py}).
    66	
    67	\textbf{Per-condition means at \texorpdfstring{$N\!=\!20$}{N=20}.}
    68	
    69	\begin{table}[ht]
    70	\centering
    71	\small
    72	\caption{Per-condition mean $\alpha$ at $N=20$ fresh seeds.}
    73	\label{tab:cxp_means}
    74	\begin{tabular}{l r r r}
    75	\toprule
    76	condition & mean $\alpha$ & std & sem \\
    77	\midrule
    78	$----$ baseline    & $3.008$ & $0.090$ & $0.020$ \\
    79	$-C--$ (C off)     & $3.464$ & $0.097$ & $0.022$ \\
    80	$--P-$ (P off)     & $2.790$ & $0.086$ & $0.019$ \\
    81	$-CP-$ (both off)  & $3.628$ & $0.161$ & $0.036$ \\
    82	\bottomrule
    83	\end{tabular}
    84	\end{table}
    85	
    86	\textbf{Main effects at \texorpdfstring{$N\!=\!20$}{N=20}.}
    87	$C$ main effect $= +0.456$ (turning $C$ off raises $\alpha$);
    88	$P$ main effect $= -0.218$ (turning $P$ off lowers $\alpha$).
    89	
    90	\textbf{Interaction estimate.} Direct calculation from means:
    91	\[
    92	\Delta_{CP} \;=\; \frac{(3.628 + 3.008) - (3.464 + 2.790)}{2}
    93	            \;=\; +0.191.
    94	\]
    95	Bootstrap on the 20-seed sample (2000 resamples):
    96	\begin{itemize}\itemsep=1pt
    97	\item bootstrap mean $\Delta_{CP} = +0.190$;
    98	\item 95\% bootstrap CI $[+0.143, +0.239]$;
    99	\item $0/2000$ bootstrap resamples were at or below zero, reported as
   100	      $0.0000$;
   101	\item $0/2000$ bootstrap resamples were below the preregistered
   102	      $+0.10$ floor, reported as $0.0000$.
   103	\end{itemize}
   104	
   105	\textbf{Per-seed paired distribution.}
   106	$19/20$ seeds give a positive paired-interaction estimate (range
   107	$+0.055$ to $+0.322$); a single seed gives $-0.009$. No seed gives a
   108	strongly negative interaction.
   109	
   110	\subsection{Reading and disclosure}
   111	
   112	\textbf{The 95\% CI is entirely above the preregistered $+0.10$
   113	threshold} on a fresh-seed sample. $0/2000$ bootstrap resamples were
   114	at or below zero, reported as $0.0000$; $0/2000$ bootstrap resamples
   115	were below the preregistered $+0.10$ floor, reported as $0.0000$.
   116	
   117	\textbf{Architectural reading (substrate witness).} $C$ creates churn
   118	in \emph{which} vertices are uncrossed (frame rotation churns the
   119	uncrossed pool). $P$ promotes the high-pressure subset of the
   120	uncrossed pool to mini-emitters. The product is a non-additive
   121	novel-event-generation pathway: with both on, the uncrossed pool
   122	churns and $P$ amplifies new vertices entering the high-pressure
   123	region; with either off, the pathway collapses. The interaction
   124	$+0.19$ is comparable in magnitude to the $P$ main effect $-0.22$,
   125	so $C$ and $P$ are \emph{strongly coupled} cascade-state stabilisers
   126	on this substrate, not nearly-orthogonal ones. This reverses an
   127	architectural claim from the original 3-seed validation that held $C$
   128	and $P$ approximately orthogonal.
   129	
   130	\textbf{Disclosure: $N\!=\!20$ ordering.} The $N\!=\!20$ deep-dive
   131	was conducted \emph{after} the original $N\!=\!3$ failure
   132	(2026-04-29 vs 2026-04-20). The seed range $32000$--$32019$ was
   133	selected to be non-overlapping with the original $30000$s seeds.
   134	Two strengthening builds we have not delivered:
   135	(i) a second independent $N\!=\!20$ run at a different seed range
   136	(e.g.\ $33000$--$33019$), and
   137	(ii) an $N\!=\!50$ characterisation of the per-seed sample
   138	distribution. Both are recorded as open builds in
   139	\S\ref{sec:limitations}.
   140	
   141	\textbf{What this stress test does \emph{not} establish.}
   142	\begin{itemize}\itemsep=2pt
   143	\item It does not establish a Lyapunov function on the reduced flow.
   144	\item It does not establish that the substrate is uniquely selected by
   145	  $C\times P$ coupling among regular 4-polytopes.
   146	\item It does not establish an $\eta$-trajectory derivation; $\eta$
   147	  is treated as a condition-dependent constant in this paper.
   148	\end{itemize}
   149	The stress test is what its name says: a high-replication factorial
   150	test of one preregistered interaction prediction, on a fresh-seed
   151	sample, with bootstrap confidence intervals. The architectural reading
   152	is a \emph{description} of what $C$ and $P$ do on the substrate, not a
   153	theorem about why they do it.
   154	
   155	\subsection{Methodological contribution}
   156	
   157	We document, as a methodological contribution to preregistration
   158	practice, that interaction terms in cascade ablation matrices require
   159	$N\!\geq\!20$ fresh seeds for reliable detection when the
   160	interaction-to-main-effect ratio is below $0.5$. The original 3-seed
   161	preregistered validation gave estimates consistent with underpowered
   162	detection on both interaction tests (P3 and P4); both close at higher
   163	$N$ without threshold modification. For preregistration design more broadly:
   164	when preregistering an interaction effect on a system with unknown
   165	per-seed variance, allocate the seed count from a power-analysis
   166	assumption that the per-seed std could be as large as the interaction
   167	effect itself. Under that assumption, $N\!\geq\!20$ is the conservative
   168	minimum.
===== /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex =====
     1	% =====================================================================
     2	\section{Cross-domain selectivity}\label{sec:cross_domain}
     3	% =====================================================================
     4	
     5	This section reports three cross-domain witnesses. \S\ref{ssec:chess}
     6	gives the chess pattern-recognition lift. \S\ref{ssec:conv} gives the
     7	conversation neutrality result that confirms the lift is selective.
     8	\S\ref{ssec:hcp} gives the HCP brain-graph maximum-symmetry null.
     9	For each domain we report
    10	$A_{d} = \mathrm{Acc}_{\mathrm{sub}, d} - \mathrm{Acc}_{\mathrm{raw}, d}$
    11	or, in the HCP case,
    12	$Z_{m} = (m_{\mathrm{ARIA}} - \mu_{\mathrm{HCP}})/\sigma_{\mathrm{HCP}}$.
    13	Numbers are lifted verbatim from
    14	\texttt{docs/brain\_mapping/CROSS\_DOMAIN\_RESULTS.md}.
    15	
    16	\subsection{Chess pattern recognition (P9--P13)}\label{ssec:chess}
    17	
    18	\textbf{Setup.} $32$ chess positions across $4$ categories (tactical,
    19	positional, endgame, opening). Per-position $8$-dimensional V2
    20	features (material balance, king safety, pawn structure, centre
    21	control, piece activity, mobility, threat density, defensive
    22	structure), normalised by per-feature $L^{2}$ norms. Substrate
    23	routing: features injected as pressure into the $S^{7}$ observer
    24	frames; substrate run forward by $n_{\mathrm{ticks}}$; resulting
    25	vertex pattern used as classifier feature vector. Classifier:
    26	1-nearest-neighbour on cosine similarity, validated by $5$-fold CV
    27	or leave-one-out (LOO).
    28	
    29	\textbf{Critical methodological detail.} Between successive depth
    30	measurements the substrate is reset to canonical state via
    31	\texttt{mon.homeostatic\_reset(level=1.0)}. Without this, pressure-
    32	field state drifts toward equilibrium across $\sim 5$ evaluations
    33	and classification structure collapses to raw-feature baseline.
    34	
    35	\begin{table}[ht]
    36	\centering
    37	\small
    38	\caption{Chess substrate-routed depth sweep with state reset between
    39	measurements.}
    40	\label{tab:chess_depth}
    41	\begin{tabular}{r r}
    42	\toprule
    43	$n_{\mathrm{ticks}}$ & accuracy \\
    44	\midrule
    45	$5$    & $53.1\%$ \\
    46	$15$   & $65.6\%$ \\
    47	$\mathbf{25}$  & $\mathbf{93.8\%}$ ($\leftarrow$ peak) \\
    48	$40$   & $84.4\%$ \\
    49	$60$   & $84.4\%$ \\
    50	$100$  & $78.1\%$ \\
    51	\bottomrule
    52	\end{tabular}
    53	\end{table}
    54	
    55	\begin{table}[ht]
    56	\centering
    57	\small
    58	\caption{Chess preregistered tests (with reset, $n=25$ canonical
    59	depth).}
    60	\label{tab:chess_prereg}
    61	\begin{tabular}{l l l l l}
    62	\toprule
    63	ID & Test & Threshold & Observed & Verdict \\
    64	\midrule
    65	P9  & 5-fold CV (seeds 30200--30204)        & $\geq 70\%$ & $83.1\%$ & $\checkmark$ \\
    66	P10 & null perm. mapping (chess, 15 perms)$^{\dagger}$  & $\geq 50\%$ & $65.4\%$ & $\checkmark$ \\
    67	P11 & random-label baseline (20 trials)     & $\in[15\%, 35\%]$ & $23.4\%$ & $\checkmark$ \\
    68	P12 & goldilocks peak depth                 & $\in\{15,25,40,60\}$ & $n=25$ & $\checkmark$ \\
    69	\textbf{P13} & substrate lift, LOO refinement (with reset)$^{\ddagger}$ & $\geq +15$pp & $\mathbf{+40.6}$pp (LOO) & $\checkmark$ \\
    70	\bottomrule
    71	\end{tabular}
    72	\end{table}
    73	
    74	$^{\dagger}$ The 2026-04-18 preregistration P16 specified the null
    75	permutation test as ``$\geq 50\%$ on \emph{both} chess and
    76	conversation''; we present the chess and conversation null mappings
    77	separately as P10 (chess) and P16 (conversation) for table clarity.
    78	Both pass.
    79	
    80	$^{\ddagger}$ The 2026-04-18 preregistration P13 specified the chess
    81	substrate-lift estimator as $5$-fold CV at threshold $\geq +15$pp.
    82	The 2026-04-29 validation tightened the estimator to LOO with state
    83	reset; we report the LOO finding ($+40.6$pp) above as a stricter
    84	validation-protocol refinement at the unchanged $+15$pp threshold,
    85	not a preregistration revision.
    86	
    87	\textbf{Reading.} Substrate routing amplifies chess-position
    88	4-category classification from raw $53.1\%$ (just above $25\%$
    89	chance) to substrate-routed $93.8\%$ at canonical depth $n=25$.
    90	This is a $+40.6$pp lift on the LOO refinement; on the preregistered
    91	$5$-fold CV estimator the substrate-routed accuracy is $83.1\%$
    92	(P9), itself well above any reasonable raw-features baseline.
    93	The original 2026-04-20 validation reported the LOO lift at
    94	$+3.1$pp, a state-drift artefact closed by the reset protocol
    95	(\S\ref{sec:method}).
    96	
    97	\textbf{Permutation null decomposition.} The null permutation
    98	mapping (P10) randomises the feature$\to$frame assignment, so each
    99	feature is routed to a different $S^{7}$ frame than canonical. The
   100	substrate retains $65.4\%$ classification accuracy under random
   101	permutation — well above the $25\%$ chance level for $4$ categories.
   102	We read this as a substrate-witness decomposition:
   103	$\sim 65$pp of classification power is \emph{architectural} (it
   104	persists when feature$\to$frame assignment is randomised; it is the
   105	H$_4$-symmetric amplifier acting on whatever input lands in the
   106	frames), and the remaining $\sim 17$pp is the semantic-alignment
   107	bonus. We do not claim this decomposition is unique; it is a
   108	description of the observed accuracy stack.
   109	
   110	\subsection{Conversation neutrality (P14--P16)}\label{ssec:conv}
   111	
   112	\textbf{Setup.} $64$ utterances across $8$ dialogue-act categories.
   113	$8$-dimensional injection-row features per utterance. Identical
   114	substrate routing pipeline to chess.
   115	
   116	\begin{table}[ht]
   117	\centering
   118	\small
   119	\caption{Conversation preregistered tests.}
   120	\label{tab:conv_prereg}
   121	\begin{tabular}{l l l l l}
   122	\toprule
   123	ID & Test & Threshold & Observed & Verdict \\
   124	\midrule
   125	P14 & raw 5-fold CV (seeds 30220--30224)    & $\geq 75\%$ & $87.5\%$ & $\checkmark$ \\
   126	P15 & substrate lift                         & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
   127	P16 & null perm. mapping (15 perms)         & $\geq 50\%$ & $70.6\%$ & $\checkmark$ \\
   128	\bottomrule
   129	\end{tabular}
   130	\end{table}
   131	
   132	\textbf{Reading.} Conversation raw features at $87.5\%$ are already
   133	strongly discriminative (cf.\ chess raw $\sim 53\%$); the substrate
   134	lift is $-4.4$pp, well within the preregistered neutrality band
   135	$|\cdot|\!<\!10$pp. The substrate is correctly null on conversation.
   136	
   137	\textbf{Selective amplifier signature.} The pair (chess
   138	$+40.6$pp lift; conversation $-4.4$pp lift) is consistent with the
   139	selective-amplifier behaviour preregistered in 2026-04-18: in these
   140	two tasks, the architecture amplifies when raw features are ambiguous
   141	(chess raw $\sim 53\%$) and is approximately neutral when raw features
   142	are already saturated (conversation raw $87.5\%$). We do not claim
   143	this generalises to all classification tasks; cross-domain transfer
   144	to additional ambiguous-feature benchmarks is an open build
   145	(\S\ref{sec:limitations}).
   146	
   147	\subsection{HCP brain-graph maximum-symmetry null
   148	            (P17--P18)}\label{ssec:hcp}
   149	
   150	\textbf{Setup.} Reference cohort: Human Connectome Project (HCP)
   151	$n=1003$ subjects~\citep{VanEssen2013HCP}; preregistered tests on
   152	$n=100$ subjects for computational tractability, with full-cohort
   153	$n=1003$ descriptive statistics also reported. ICA-50 group-averaged
   154	connectivity matrix; thresholded at the same density as ARIA's
   155	vertex graph ($\rho=0.101$). Compare degree distribution and
   156	higher-order graph statistics. ARIA reference: $G_{V_{600}}$ with
   157	$\Lop$. By H$_4$ transitivity (Lemma~\ref{lem:600cell}) every vertex
   158	has identical local structure $\Rightarrow$ uniform degree $12$
   159	$\Rightarrow$ degree std $= 0$ as a theorem.
   160	
   161	\begin{table}[ht]
   162	\centering
   163	\small
   164	\caption{HCP comparison: preregistered $n=100$ test plus full-cohort
   165	$n=1003$ descriptive statistics.}
   166	\label{tab:hcp}
   167	\begin{tabular}{l r r r}
   168	\toprule
   169	Metric & ARIA & HCP $n=1003$ mean (sd) & $\sigma$ from HCP \\
   170	\midrule
   171	Degree std (preregistered, $n=100$ subset) & $0.000$ & $3.388$ ($> 2.0$) & --- \\
   172	Degree std (descriptive, $n=1003$)         & $0.000$ & $3.28\pm 0.28$ & $-11.58\sigma$ \\
   173	Participation ratio (descriptive)          & $68.54$ & $19.72\pm 0.61$ & $+79.78\sigma$ \\
   174	Clustering coefficient (descriptive)       & $0.455$ & $0.220$ & $+6.80\sigma$ \\
   175	\bottomrule
   176	\end{tabular}
   177	\end{table}
   178	
   179	\begin{itemize}\itemsep=2pt
   180	\item P17 (ARIA degree std, theorem): predicted $=0$, observed
   181	  $0.0000$, $\checkmark$.
   182	\item P18 (HCP ICA-50 degree std, $n=100$ density-matched):
   183	  predicted $> 2.0$, observed $3.388$, $\checkmark$. Zero of $1003$
   184	  HCP subjects have degree std below $2.0$.
   185	\end{itemize}
   186	
   187	\textbf{Reading (substrate witness).} ARIA's H$_4$-transitive
   188	structure is a deterministic group-theoretic null reference for
   189	cortical functional connectivity. Real cortex breaks the symmetry
   190	through hub-spoke functional specialisation; the $\sigma$-distances
   191	quantify the magnitude of biological symmetry-breaking with no
   192	fitted parameters. The $\sigma$-distances ($-11.58\sigma$ on degree
   193	homogeneity, $+79.78\sigma$ on participation ratio, $+6.80\sigma$ on
   194	clustering coefficient) are large on the ICA-50 pipeline at the
   195	density-matched threshold $\rho = 0.101$; cross-parcellation
   196	replication (Schaefer, Glasser) remains an open build.
   197	
   198	\textbf{Participation-ratio comparability.} ARIA's vertex graph has
   199	$120$ nodes; the HCP ICA-50 connectivity matrix has $50$ nodes. The
   200	participation-ratio statistic
   201	$\mathrm{PR}(G) = (\sum_{i} d_{i})^{2} / \sum_{i} d_{i}^{2}$ is
   202	node-count-dependent — its theoretical maximum is the node count of
   203	the graph. We report the raw $\mathrm{PR}$ values
   204	($\mathrm{ARIA}=68.54$ on a 120-node graph; $\mathrm{HCP}=19.72$ on a
   205	50-node graph) and the $\sigma$-distance against the HCP
   206	across-subject distribution, but the $+79.78\sigma$ value reflects
   207	both the architectural difference and the differing node counts. A
   208	node-count-normalised statistic
   209	$\mathrm{PR}/|V|$ gives $\mathrm{ARIA}=0.571$ vs $\mathrm{HCP}=0.394$,
   210	a smaller absolute gap; we keep the raw-PR comparison as headline
   211	because the HCP subject distribution and the across-subject
   212	$\sigma$ are computed in the same units, but flag the node-count
   213	caveat here.
   214	
   215	\textbf{What we do not claim.}
   216	\begin{itemize}\itemsep=2pt
   217	\item We do not claim cortex has ``drifted from an ideal polytope'';
   218	  the substrate is a useful a-priori null whose deviation from real
   219	  cortex is precisely measurable.
   220	\item We do not claim parcellation invariance: the $\sigma$-distances
   221	  are reported on ICA-50; alternative parcellations (Schaefer,
   222	  Glasser) would give different per-metric numbers but, on the
   223	  basis of the qualitative pattern that cortex is hub-concentrated
   224	  relative to ARIA's transitive null, we expect them to preserve the
   225	  signs. Verification across parcellations is an open build
   226	  (\S\ref{sec:limitations}).
   227	\end{itemize}
   228	
   229	\subsection{Cross-domain summary as a selective amplifier
   230	            \texorpdfstring{$+$}{+} maximum-symmetry null}
   231	
   232	\begin{table}[ht]
   233	\centering
   234	\small
   235	\caption{Cross-domain summary on a single substrate.}
   236	\label{tab:cross_domain_summary}
   237	\begin{tabular}{l r r r r r}
   238	\toprule
   239	Task & Raw & Substrate & Null perm. & Geom.\ floor & Sem.\ alignment \\
   240	\midrule
   241	Chess (LOO, $n=25$, w/ reset) & $53.1\%$ & $93.8\%$ & --- & --- & $+40.6$pp lift \\
   242	Chess (5-fold CV)             & ---      & $83.1\%$ & $65.4\%$ & $65.4\%$ & $+17.7$pp \\
   243	Conversation (5-fold CV)      & $87.5\%$ & $83.1\%$ & $70.6\%$ & $70.6\%$ & $+12.5$pp (raw vs null) \\
   244	\bottomrule
   245	\end{tabular}
   246	\end{table}
   247	
   248	The geometric content ($\approx 65$--$71\%$ across the two domains)
   249	is the architecture-invariant null floor. The semantic content
   250	($12$--$18$pp) is the domain-specific contribution. On HCP,
   251	$\sigma$-distances against the biological cohort are
   252	$(-11.58, +79.78, +6.80)$ on (degree std, participation ratio,
   253	clustering coefficient).
   254	
   255	\textbf{Headline cross-domain reading.} The substrate is
   256	\emph{selectively} amplifying (not unconditionally), and it is a
   257	maximum-symmetry deterministic null on connectivity (not a fitted
   258	model). Both readings sit inside the substrate-witness scope.
===== /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex =====
     1	% =====================================================================
     2	\section{Discussion}\label{sec:discussion}
     3	% =====================================================================
     4	
     5	This section reads the substrate-witness result against existing
     6	theories of consciousness, identifies what is novel here that is not
     7	a re-statement of an earlier theory, and proposes a non-load-bearing
     8	ACT bridge to the companion adaptive-closure-transport
     9	preprint~\citep{SmartAdaptiveClosureTransport2026}. We do not claim a
    10	selection theorem, we do not claim a Lyapunov derivation, and we do
    11	not claim the recurrent layer ``is'' consciousness.
    12	
    13	\subsection{What is novel in this work}
    14	
    15	Three things are claimed novel as a substrate witness:
    16	\begin{enumerate}\itemsep=2pt
    17	\item \textbf{A geometry-fixed substrate that is consistent with
    18	  real-cortex EEG signatures without fitted shape parameters on neural
    19	  data.} The 600-cell + H$_4$ symmetry is fixed by group theory once
    20	  the substrate is chosen; cascade-$\alpha$ matches Sleep-EDFx within
    21	  preregistered tolerance with pairwise CI overlap on three reference
    22	  ranges; six drug/sleep signatures pass at published-reference
    23	  thresholds on a single deterministic substrate. We are not aware of
    24	  a prior geometric substrate that has been tested against this many
    25	  preregistered cortical correspondences from a graph fixed by group
    26	  theory; we cannot rule out that such a model exists.
    27	\item \textbf{The strong-coupling architectural finding.} $C$ and $P$
    28	  are strongly coupled cascade-state stabilisers, not
    29	  nearly-orthogonal ones. The $C\!\times\!P$ interaction
    30	  ($+0.190$, $95\%$ CI $[+0.143, +0.239]$ at $N\!=\!20$) is comparable
    31	  in magnitude to the $P$ main effect ($-0.218$). This was hidden by
    32	  underpowered ablation and emerged only at $N\!\geq\!20$ — a
    33	  substantive correction to the architectural reading from the
    34	  original 3-seed validation.
    35	\item \textbf{The 18/18 preregistered correspondences with no
    36	  threshold modification.} Every prediction in the preregistered set
    37	  passes at the preregistered thresholds. The two interaction tests
    38	  (P3, P4) required $N\!\geq\!5$ and $N\!\geq\!20$ respectively, and
    39	  one test (P13) required the documented state-reset protocol. We
    40	  report this transparently as methodology refinement, not as
    41	  threshold change.
    42	\end{enumerate}
    43	
    44	\subsection{Comparison to existing theories of consciousness}
    45	
    46	\textbf{vs IIT.}~\citep{Tononi2008,BalduzziTononi2008} ARIA produces
    47	IIT-direction-correct $\Phi$ collapse on propofol ($0.33\!\times$
    48	wake). The H$_4$-equivariance argument
    49	(\S\ref{sec:chain}) makes $\Phi\to 0$ when dynamics are
    50	group-symmetric, and $\Phi > 0$ only when dynamics break symmetry.
    51	ARIA does not implement the full IIT axioms (cause-effect repertoires,
    52	exclusion postulate, integration-over-partitions); it reproduces the
    53	observable consequence on the propofol--wake state contrast. This is
    54	a consistency-of-direction result, not a discharge of IIT.
    55	
    56	\textbf{vs Global Workspace Theory.}~\citep{Baars1988GWT,Dehaene2014ConsciousAndBrain}
    57	The $S^{7}$ context-rotation mechanism (\S\ref{sec:chain}) is
    58	functionally analogous to a workspace with rotating attentional
    59	selection; the active observer frame plays the role of a temporary
    60	in-workspace subset of features. ARIA does not commit to the GWT
    61	broadcast/access distinction at the architectural level; the
    62	analogy is descriptive.
    63	
    64	\textbf{vs Predictive Processing.}~\citep{FristonFreeEnergy2010,ClarkPP2013}
    65	ARIA does not implement prediction-error minimisation or hierarchical
    66	generative models.
    67	The recurrent self-model layer ($\eta\!=\!0.20$) provides top-down
    68	modulation of the substrate response by cosine direction alignment
    69	with the prior phenomenal snapshot, not by learned prediction errors.
    70	Predictive-processing-style refinements (e.g.\ $\eta$ as an adaptive
    71	learning rate over a prediction-error norm) are an open build, not
    72	delivered here.
    73	
    74	\textbf{vs neural mass models.} ARIA operates at the
    75	architectural-algorithmic level; it does not specify which neural
    76	circuits implement context rotation or partial emission. The 600-cell
    77	substrate is proposed as an abstract description of the criticality-
    78	maintaining structure of cortex, not as a circuit model.
    79	
    80	\subsection{The non-load-bearing ACT bridge}\label{ssec:act_bridge}
    81	
    82	The companion adaptive-closure-transport
    83	preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
    84	4-tuple bridge
    85	$(M, L_{M}, W, R_{\mathrm{hom}})$ — substrate $M$, response operator
    86	$L_{M}$, learnable Hebbian-like field $W$, and a homeostatic
    87	regulariser $R_{\mathrm{hom}}$. We propose the dictionary
    88	$D_{\mathrm{ACT}}$:
    89	\[
    90	D_{\mathrm{ACT}}\colon (M, L_{M}, W, R_{\mathrm{hom}})
    91	\;\longmapsto\;
    92	(\Rsixhundred,\ \Cph,\ \text{cascade pressure field}\ W_{\mathrm{p}},
    93	   \ \texttt{homeostatic\_reset}).
    94	\]
    95	\textbf{This bridge is non-load-bearing for the present paper.} It is
    96	included as a route-K (alternative-route) reading; the substrate-
    97	witness claims (six signatures, $18/18$, chess $+40.6$pp,
    98	HCP $\sigma$-distances) do not require any of the ACT theorems.
    99	
   100	\textbf{What ACT would have to deliver to make this load-bearing.}
   101	The companion preprint identifies four open builds, each of which is
   102	deferred:
   103	\begin{itemize}\itemsep=2pt
   104	\item A Lyapunov function $V(W)$ on the reduced flow whose
   105	  monotonicity proves selection — not delivered.
   106	\item An edge-space decomposition of $\mathbb{R}^{E_{M}}$ under the
   107	  Hodge edge Laplacian $L_{\mathrm{edge}} = \delta_{2}\delta_{2}^{\mathsf T} +
   108	  \delta_{1}^{\mathsf T}\delta_{1}$ — not delivered.
   109	\item A formal $2I$-equivariance audit of the closure operator
   110	  family — not delivered.
   111	\item A full reduced-flow convergence theorem on
   112	  $W$-trajectories — not delivered.
   113	\end{itemize}
   114	Until these are delivered, ARIA is positioned as the empirical
   115	\emph{substrate witness} for the family that ACT names; ACT is not the
   116	selection-theorem witness for ARIA. The companion kernel
   117	document~\citep{SmartAriaClosureKernel2026} discusses the same $\Cph$
   118	in a passive-regime witness via the $B\to K^{*}\mu^{+}\mu^{-}$ flavour
   119	anomaly~\citep{SmartBAnomaly2026}; that line shares operator-level
   120	infrastructure with this paper, but does not transfer empirical
   121	support for ARIA.
   122	
   123	\subsection{The strong-coupling reading for cortical architecture}
   124	
   125	Real cortical criticality is maintained by multiple parallel
   126	mechanisms: E/I balance, neuromodulation (acetylcholine, noradrenaline),
   127	homeostatic plasticity, gain control. The naive expectation — and the
   128	one we held until the $N\!=\!20$ deep-dive — is that these are mostly
   129	orthogonal, so losing one removes only its own main effect. The
   130	$N\!=\!20$ result reverses this on the substrate: $C$ and $P$ are
   131	strongly coupled. Disabling one cascades into losing the synergistic
   132	contribution of the other.
   133	
   134	This matches clinical observations: anaesthesia (which targets
   135	GABAergic transmission) and seizure (which targets E/I balance)
   136	produce widespread network-level dysfunction beyond their direct
   137	targets — exactly what strong synergy predicts. We position this as
   138	\emph{a hypothesis the substrate witness raises}, not as a proof.
   139	The bridge from cascade-mechanism interaction on $\Rsixhundred$ to
   140	real-cortex pharmacological coupling is a step we do not take in
   141	this paper.
   142	
   143	\subsection{Methodological contributions}
   144	
   145	Two methodological items are worth recording outside the headline:
   146	\begin{enumerate}\itemsep=2pt
   147	\item \textbf{$N\!\geq\!20$ for high-variance interaction terms.}
   148	  Allocation discipline for preregistration: when preregistering an
   149	  interaction effect on a system with unknown per-seed variance,
   150	  budget for $N\!\geq\!20$ from the start. The original 3-seed plan
   151	  was the source of two underpowered-interaction estimates in this work.
   152	\item \textbf{State-reset protocol on non-stationary substrates.}
   153	  ARIA's substrate is a non-stationary dynamical system; the
   154	  pressure field equilibrates within $\sim 5$ successive evaluations.
   155	  Any multi-trial benchmark must specify a state-reset protocol or
   156	  document the drift. Generalisable lesson: \emph{published
   157	  cross-domain benchmarks on non-stationary substrates should report
   158	  an explicit reset/equilibration discipline}, not just seed.
   159	\end{enumerate}
   160	
   161	\subsection{The substrate as a maximum-symmetry connectivity null}
   162	
   163	The HCP comparison (\S\ref{ssec:hcp}) places ARIA as a principled
   164	deterministic null reference for cortical functional connectivity.
   165	Real cortex breaks the symmetry through hub-spoke functional
   166	specialisation; the $\sigma$-distances from ARIA quantify the
   167	magnitude of biological symmetry-breaking with no fitted parameters.
   168	
   169	This is a methodological contribution to comparative connectomics.
   170	Stochastic nulls (Erd\H{o}s--R\'enyi, configuration model,
   171	edge-randomised graphs) compare cortex to a random graph with matched
   172	density. ARIA is a different kind of null: a deterministic
   173	group-theoretic graph with theorem-level statements of structure
   174	(degree std $=\!0$ by transitivity, eigenvalue spectrum
   175	$\{0, 3, 4\Ph, 6\Ph, 12{-}4\Ph, 12{-}6\Ph, 9, 12\}$ by character
   176	theory). Both null kinds are useful; ARIA gives a specific,
   177	reproducible, group-theoretic baseline that cortex deviates from in
   178	quantifiable $\sigma$-units.
   179	
   180	\subsection{Open questions raised by the substrate witness}
   181	
   182	\begin{itemize}\itemsep=2pt
   183	\item Do the six drug/sleep signatures replicate across $10$--$20$
   184	  cross-seed runs of the recurrent layer? (Single-seed disclosure;
   185	  see \S\ref{sec:limitations}.)
   186	\item Do alternative regular 4-polytopes ($24$-cell, $120$-cell)
   187	  reproduce comparable signature sets, or is the $600$-cell
   188	  distinguished?
   189	\item Does the strong-coupling reading ($C\!\times\!P$) survive an
   190	  independent fresh-seed $N\!=\!20$ replication at a different seed
   191	  range?
   192	\item Does the substrate's amplifier behaviour transfer to other
   193	  ambiguous-feature classification tasks beyond chess (e.g.\ visual
   194	  pattern, audio classification)?
   195	\item Does the Sleep-EDFx three-way CI overlap survive on a different
   196	  EEG cohort (TUH, NHM)?
   197	\end{itemize}
   198	We list these as open questions raised by the witness, not as gaps
   199	in the witness itself.
===== /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex =====
     1	% =====================================================================
     2	\section{Limitations and hostile-review guard matrix}\label{sec:limitations}
     3	% =====================================================================
     4	
     5	This section enumerates limitations transparently, organised as a
     6	five-move guard matrix following the b-anomaly preprint
     7	template~\citep{SmartBAnomaly2026}: regime, post-hoc, interpretation,
     8	test/claim, state-drift. For each guard we record
     9	$G\colon \mathrm{risk} \to (\mathrm{disclosure}, \mathrm{evidence},
    10	\mathrm{strengthening\ build})$.
    11	
    12	\subsection{Regime}\label{ssec:regime}
    13	
    14	\textbf{Single substrate (the 600-cell).} We have not tested whether
    15	other regular 4-polytopes ($24$-cell, $120$-cell) would produce
    16	comparable correspondences. The 600-cell was chosen because its
    17	H$_4$ Coxeter cascade structure aligns with the empirical signatures
    18	that motivated this paper, not from an a-priori derivation.
    19	\emph{Disclosure:} substrate-witness scope, no uniqueness claim
    20	(\S\ref{sec:intro}). \emph{Evidence:} empirical correspondences hold
    21	on $\Rsixhundred$. \emph{Strengthening build:} formal ablation against
    22	$\{24\text{-cell}, 120\text{-cell}\}$ on the same six-signature
    23	battery and the eighteen preregistered tests, with thresholds
    24	preserved.
    25	
    26	\textbf{Single-seed determinism on the recurrent layer.} The v4
    27	six-signature results in~\S\ref{ssec:six_signatures} are reported on
    28	a single deterministic trajectory at seed $42$. Empirical CIs across
    29	$10$--$20$ cross-seed runs would strengthen the per-signature claims
    30	beyond the single-trajectory bootstrap of $58$ events that gives the
    31	WAKE 95\% CI $[1.82, 2.86]$. \emph{Disclosure:} explicitly single-seed
    32	in~\S\ref{sec:method} and~\S\ref{ssec:six_signatures}.
    33	\emph{Evidence:} bootstrap CI on the wake 58 events, plus three-way
    34	overlap with two independent reference $\alpha$ ranges.
    35	\emph{Strengthening build:} 10--20 cross-seed runs of
    36	\texttt{demo\_drug\_sleep\_v4.py}, with per-signature bootstrap CIs.
    37	
    38	\textbf{Stylised stimulus models on the recurrent layer.} The v4
    39	stimulus models for WAKE (AR(1) noise + tonic shell + attention
    40	episodes), SLEEP\_N3 (slow oscillation + spindles + K-complexes),
    41	and PROPOFOL (low-amplitude tonic noise) are biologically motivated
    42	but abstract: a single shell anchor for tonic coherence, fixed
    43	$40$-tick period for slow-wave drive, etc. Real spatial structure of
    44	cortical input is much richer. \emph{Disclosure:}~\S\ref{sec:chain}
    45	``deliberately structural rather than measurement-fitted''.
    46	\emph{Evidence:} models match published biological time scales but
    47	are not tuned to specific signatures. \emph{Strengthening build:}
    48	replication on stimulus models derived from anatomically-grounded
    49	input statistics (e.g.\ retinotopic, tonotopic).
    50	
    51	\subsection{Post-hoc}\label{ssec:posthoc}
    52	
    53	\textbf{The 600-cell choice is post-hoc justified by empirical
    54	observables.} While the construction of $\Rsixhundred$ is theorem-
    55	level rigorous (H$_4$ Coxeter group theory), the choice of \emph{this}
    56	polytope as the consciousness-substrate instance is motivated by the
    57	correspondences observed, not by an a-priori biological argument.
    58	\emph{Disclosure:}~\S\ref{sec:intro}, ``substrate witness, not
    59	derivation; not a uniqueness claim''. \emph{Evidence:} the eighteen
    60	preregistered correspondences plus six signatures; the H$_4$
    61	transitivity theorem ($P17$). \emph{Strengthening build:} comparison
    62	with the $24$-cell and $120$-cell on the same signatures; formal
    63	ACT-selection-theorem witness via the bridge of~\S\ref{ssec:act_bridge}
    64	(deferred).
    65	
    66	\textbf{Cascade decomposition is one of several possible
    67	decompositions of H$_4$.} We use the $\sigma$-orbit projector basis
    68	because it is machine-precise and biologically informative, but other
    69	bases (character-theoretic, Galois-twin) give the same physical
    70	predictions through different intermediate variables. \emph{Disclosure:}
    71	\S\ref{ssec:cascade} acknowledges non-uniqueness of decomposition.
    72	\emph{Evidence:} block-diagonalisation at $<10^{-15}$ cross-block
    73	norm. \emph{Strengthening build:} catalogue and equivalence-prove the
    74	admissible decompositions.
    75	
    76	\textbf{$\Ph^{-2}$ floor not derived.} The shifted-Laplacian floor
    77	$\Ph^{-2}\!\approx\!0.382$ is a stability clamp making $\Cph$
    78	strictly positive definite (\S\ref{ssec:cphi}); it is not derived
    79	from a closure functional or symmetry argument. \emph{Disclosure:}
    80	\S\ref{ssec:cphi} marks this as a design-level choice; the companion
    81	kernel doc~\citep{SmartAriaClosureKernel2026} explicitly does not
    82	derive it. \emph{Evidence:} the same operator (with the same shift)
    83	serves as the basis for the b-anomaly passive-regime
    84	witness~\citep{SmartBAnomaly2026}. \emph{Strengthening build:}
    85	derive the $\Ph^{-2}$ shift as the unique stability clamp under a
    86	named regularity criterion.
    87	
    88	\subsection{Interpretation}\label{ssec:interpretation}
    89	
    90	\textbf{The recurrent layer is a method, not a metaphysics claim.}
    91	We do not claim the recurrent self-model layer ``is'' consciousness;
    92	we claim quantitative consistency with six published biological
    93	signatures on a deterministic trajectory. \emph{Disclosure:}
    94	\S\ref{sec:intro}, \S\ref{sec:chain} (``method, not metaphysics'').
    95	\emph{Evidence:} six signatures vs published thresholds.
    96	\emph{Strengthening build:} cross-seed CIs (\S\ref{ssec:regime}); a
    97	formal account of which substrate observables map to which phenomenal
    98	contents (the bind\_phenomenal\_field channels) is not delivered.
    99	
   100	\textbf{$\Phi$ is an IIT-style direction-of-effect proxy, not a full
   101	IIT discharge.} \emph{Disclosure:}~\S\ref{sec:chain} explicitly.
   102	\emph{Evidence:} propofol $\Phi$ collapse to $0.33\!\times$ wake
   103	matches IIT direction. \emph{Strengthening build:} a
   104	\texttt{phi\_iit\_full} implementation following Balduzzi--Tononi
   105	2008~\citep{BalduzziTononi2008} on the substrate; not delivered.
   106	
   107	\textbf{HCP $\sigma$-distances are descriptive, not normative.} We
   108	do not claim ``cortex has drifted from an ideal polytope''; we
   109	quantify the distance between cortex and the deterministic H$_4$ null.
   110	\emph{Disclosure:}~\S\ref{ssec:hcp} explicitly. \emph{Evidence:}
   111	$\sigma$-distances on three independent metrics. \emph{Strengthening
   112	build:} cross-parcellation replication (Schaefer, Glasser).
   113	
   114	\subsection{Test/claim}\label{ssec:testclaim}
   115	
   116	\textbf{Two preregistered interaction tests required higher $N$
   117	than originally allocated.} P3 closes at $N\!=\!5$; P4 closes only at
   118	$N\!=\!20$. We document this transparently as a Type II
   119	methodology issue, not a threshold change. \emph{Disclosure:}
   120	\S\ref{sec:method}, \S\ref{sec:results}, \S\ref{sec:stress}.
   121	\emph{Evidence:} bootstrap CI fully above the $+0.10$ floor; per-seed
   122	distribution narrow at $N\!=\!20$ ($\mathrm{std}=0.089$);
   123	$19/20$ seeds positive. \emph{Strengthening build:} a second
   124	$N\!=\!20$ run at a different seed range (e.g.\ $33000$--$33019$);
   125	an $N\!=\!50$ characterisation of the per-seed distribution.
   126	
   127	\textbf{The original 2026-04-20 walks-back are reversed without
   128	threshold modification.} The reversals (P3, P4, P13) are documented
   129	in
   130	\texttt{docs/brain\_mapping/VALIDATION\_RESULTS\_2026-04-29.md} with
   131	the original failure values, the methodology refinement, and the
   132	post-refinement values. \emph{Disclosure:} this paper carries those
   133	disclosures verbatim. \emph{Evidence:} 2026-04-20 vs 2026-04-29 side-
   134	by-side results table. \emph{Strengthening build:} the strengthening
   135	builds for P3/P4/P13 above; no further claim is needed.
   136	
   137	\textbf{Bayesian and full-IIT inference not performed.} All intervals
   138	are frequentist (bootstrap CIs); $\Phi$ is the direction-of-effect
   139	proxy, not the Balduzzi--Tononi 2008 algorithm. \emph{Disclosure:}
   140	this section. \emph{Strengthening build:} Bayesian posterior on
   141	$\Delta_{CP}$; full-IIT computation on the $S^{4}\!\to\!2^{4}$
   142	substrate state space. The latter is computationally heavy and is
   143	deferred.
   144	
   145	\subsection{State-drift / out-of-scope}\label{ssec:scope}
   146	
   147	\textbf{Single condition-dependent parameter $\eta$ is not derived
   148	as a learned variable.} $\eta\in\{0, 0.05, 0.20\}$ across PROPOFOL,
   149	SLEEP\_N3, and WAKE/RECOVERY is a condition-dependent constant in
   150	this paper, not a learned trajectory. A predictive-processing
   151	extension where $\eta$ adapts on an error norm is an open build.
   152	
   153	\textbf{No deuteron / hadron / RH / capstone material is loaded into
   154	this paper.} The companion programme (cascade-derivation, capstone
   155	coalgebra, RH formal) shares operator-level infrastructure but is not
   156	load-bearing here. Deliberately out of scope.
   157	
   158	\textbf{Out-of-scope items NOT delivered (correctly).}
   159	\begin{itemize}\itemsep=2pt
   160	\item Aria-chess active-regime companion analysis on chess move-by-move
   161	  trajectories (this paper covers static positions only).
   162	\item Edge-space decomposition of $\mathbb{R}^{E_{M}}$ under
   163	  $2I$-equivariance — open build of the ACT companion paper.
   164	\item Lyapunov derivation $V(W)$ from a closure functional
   165	  $\mathcal{F}$ — open build of the ACT companion paper.
   166	\item Selection theorem for $\Rsixhundred$ over alternative regular
   167	  4-polytopes — see~\S\ref{ssec:regime}.
   168	\item Cross-cohort EEG (TUH, NHM, OpenNeuro non-propofol) replication
   169	  of the six signatures.
   170	\item Cross-parcellation replication of the HCP $\sigma$-distances
   171	  (Schaefer, Glasser, etc.).
   172	\item Bayesian posterior on the C$\times$P interaction.
   173	\end{itemize}
   174	
   175	\subsection{The honest verdict}
   176	
   177	The result is a substrate witness: a geometry-fixed substrate, with
   178	no shape parameters tuned to any neural dataset, is consistent with
   179	eighteen preregistered correspondences and six independent drug/sleep
   180	EEG signatures, with all original gaps closed by methodology
   181	refinement and without modifying any preregistered threshold. We do
   182	not claim the substrate \emph{is} consciousness. We do not claim a
   183	selection theorem on the ACT bridge. We do not claim uniqueness for
   184	$\Rsixhundred$ among regular 4-polytopes. The strengthening builds
   185	for these stronger claims are listed above and remain open.
===== /mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/10_conclusion.tex =====
     1	% =====================================================================
     2	\section{Conclusion}\label{sec:conclusion}
     3	% =====================================================================
     4	
     5	The 600-cell regular 4-polytope $\Rsixhundred$ under H$_4$ Coxeter
     6	symmetry, with the shifted-Laplacian response operator
     7	$\Cph = \Lop + \Ph^{-2} I$ ($\Ph=(1+\sqrt 5)/2$), is a
     8	geometry-fixed substrate that is consistent with eighteen
     9	preregistered neuroscience correspondences plus six independent
    10	drug/sleep EEG signatures of conscious vs unconscious states. Once
    11	the substrate is chosen, its graph structure
    12	($120$ vertices, uniform degree $12$, Laplacian spectrum
    13	$\{0, 3, 4\Ph, 6\Ph, 12{-}4\Ph, 12{-}6\Ph, 9, 12\}$) is fixed by
    14	group theory; only one condition-dependent self-injection coupling
    15	$\eta\in\{0, 0.05, 0.20\}$ and one substrate-pinned nonlinearity
    16	$\mathrm{bounded\_topk}(\cdot, k\!=\!12)$ at the graph's average
    17	degree enter the recurrent layer above the substrate. No shape
    18	parameter is tuned to any neural dataset.
    19	
    20	\textbf{Headline tally.} On a single deterministic trajectory, six
    21	drug/sleep EEG signatures pass at preregistered thresholds:
    22	NREM-N3 phenomenal-intensity variance ratio $0.463\!\times$ wake;
    23	propofol modality-switching $1.83\!\times$ wake; propofol continuity
    24	drop $+0.066$; propofol integrated-information $\Phi$ collapse to
    25	$0.33\!\times$ wake (IIT direction confirmed); recovery
    26	deterministically identical to wake; wake cortical-avalanche power
    27	law $\alpha\!=\!2.252$, $95\%$ CI $[1.82, 2.86]$, $R^{2}\!=\!0.956$.
    28	The wake $95\%$ CI overlaps simultaneously the real Sleep-EDFx EEG
    29	$95\%$ CI ($n\!=\!30$ subjects, $\alpha\!=\!2.51$,
    30	CI $[2.50, 2.53]$) and ARIA's prior cascade pipeline CI
    31	$[2.73, 3.25]$.
    32	
    33	\textbf{Eighteen preregistered correspondences.} All eighteen pass at
    34	preregistered thresholds, with two interaction tests requiring
    35	$N\!\geq\!5$ and $N\!=\!20$ respectively for reliable detection of
    36	high-variance interaction terms, and one cross-domain test requiring
    37	the documented \texttt{homeostatic\_reset} state-reset protocol. No
    38	preregistered threshold has been modified. The original 2026-04-20
    39	$15/18$ tally was a methodology-limited reading, not a content
    40	failure; the closure of the three gaps (P3, P4, P13) is documented
    41	transparently in
    42	\texttt{docs/brain\_mapping/VALIDATION\_RESULTS\_2026-04-29.md}.
    43	
    44	\textbf{Strong-coupling architectural finding.} Two cascade
    45	mechanisms — context rotation $C$ and partial emission $P$ — are
    46	causally identifiable and \emph{strongly synergistic}: their
    47	interaction $\Delta_{CP}\!=\!+0.190$ at $N\!=\!20$
    48	($95\%$ bootstrap CI $[+0.143, +0.239]$, $0/2000$ resamples at or
    49	below zero, reported as $0.0000$) is comparable in magnitude to the
    50	$P$ main effect $-0.218$. The original 3-seed estimate ($+0.044$)
    51	is consistent with an underpowered interaction estimate on a
    52	high-per-seed-variance term ($\mathrm{std}=0.089$ at $N\!=\!20$); we
    53	contribute the $N\!\geq\!20$ minimum as a preregistration-practice
    54	recommendation.
    55	
    56	\textbf{Cross-domain selectivity.} The substrate exhibits selective
    57	amplification on the two tasks tested: chess 4-category position
    58	classification on 8-D V2 features lifts $+40.6$pp on leave-one-out at
    59	canonical depth $n\!=\!25$ ticks (raw $53.1\%$ $\to$ substrate-routed
    60	$93.8\%$, with state reset; preregistered threshold $\geq +15$pp on
    61	$5$-fold CV — the LOO finding above is a stricter validation-protocol
    62	refinement at the same threshold), while
    63	conversation utterance classification at raw $87.5\%$ lifts $-4.4$pp
    64	(threshold $|\cdot|\!<\!10$pp) — and as a maximum-symmetry
    65	deterministic null reference for cortical functional connectivity:
    66	on HCP $n\!=\!1003$, ARIA's H$_4$-transitive structure is at
    67	$-11.58\sigma$ on degree homogeneity, $+79.78\sigma$ on participation
    68	ratio, and $+6.80\sigma$ on clustering coefficient.
    69	
    70	\textbf{Substrate-witness scope.} This is a substrate witness, not a
    71	derivation of consciousness, not a selection theorem on the
    72	companion adaptive-closure-transport
    73	4-tuple~\citep{SmartAdaptiveClosureTransport2026}, and not a
    74	uniqueness claim for the 600-cell among regular 4-polytopes. The
    75	strengthening builds — cross-seed CIs on the recurrent-layer
    76	signatures, alternative-polytope ablations, an independent $N\!=\!20$
    77	C$\times$P replication at a different seed range, cross-parcellation
    78	HCP replication, a Lyapunov function on the reduced flow,
    79	$2I$-equivariance audit of the closure operator family — are
    80	explicitly listed in~\S\ref{sec:limitations} and remain open.
    81	
    82	We are not aware of a prior deterministic geometric architecture
    83	tested against this many preregistered cortical correspondences from
    84	a graph fixed by group theory with no shape parameters tuned to
    85	neural data; we cannot rule out that such prior work exists. The empirical material
    86	gathered here is the substrate witness; the broader programme to
    87	turn the witness into a selection-theorem-grade claim — including the
    88	independent passive-regime witness via the $B\to K^{*}\mu^{+}\mu^{-}$
    89	flavour anomaly~\citep{SmartBAnomaly2026} on the same response
    90	operator $\Cph$ — is sketched in the companion preprints and remains
    91	the natural next step.

codex
I found one likely scope/wording issue in the conclusion; now I’m narrowing all headline and theorem-like claims against source lines.
exec
/bin/bash -lc "cd '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess' && rg -n \"(preregister|18/18|17/18|six|6/6|P4|C\\\\\\\\times|0/2000|P=0|P\\\\(|40\\.6|27\\.2|n=15|n\\\\"'!='"\\\\"'!15|n=25|1'"\\.83|2\\.96|1003|n=100|selection theorem|unique|uniqueness|Lyapunov|ACT|adaptive|consciousness|is consciousness|derivation of consciousness|threshold|modified|refinement|methodology|LOO|5-fold|reset|propofol|Sleep-EDFx|2\\.50|2\\.53|amplif|only when|not aware|Brodbeck|2I|regular 4-polytopes|Phi|\\\\\\\\Phi|Coxeter|600-cell|shape parameter|fitted|causally|theorem|proposition|Lemma|Corollary)\" paper/main.tex paper/sections/*.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 396ms:
paper/sections/06_stress_tests.tex:7:preregistered prediction was P4: $C\times P$ interaction
paper/sections/06_stress_tests.tex:9:$N\!=\!3$ validation gave $+0.044$ — below the threshold — and the
paper/sections/06_stress_tests.tex:11:was walked back. Closing this gap without modifying the preregistered
paper/sections/06_stress_tests.tex:12:threshold required (a) re-evaluating the $N\!=\!3$ point estimate as
paper/sections/06_stress_tests.tex:21:(\S\ref{sec:chain}), the $C\times P$ interaction estimate is the
paper/sections/06_stress_tests.tex:36:\caption{$C\times P$ interaction estimate as a function of $N$.}
paper/sections/06_stress_tests.tex:99:\item $0/2000$ bootstrap resamples were at or below zero, reported as
paper/sections/06_stress_tests.tex:101:\item $0/2000$ bootstrap resamples were below the preregistered
paper/sections/06_stress_tests.tex:112:\textbf{The 95\% CI is entirely above the preregistered $+0.10$
paper/sections/06_stress_tests.tex:113:threshold} on a fresh-seed sample. $0/2000$ bootstrap resamples were
paper/sections/06_stress_tests.tex:114:at or below zero, reported as $0.0000$; $0/2000$ bootstrap resamples
paper/sections/06_stress_tests.tex:115:were below the preregistered $+0.10$ floor, reported as $0.0000$.
paper/sections/06_stress_tests.tex:122:churns and $P$ amplifies new vertices entering the high-pressure
paper/sections/06_stress_tests.tex:143:\item It does not establish a Lyapunov function on the reduced flow.
paper/sections/06_stress_tests.tex:144:\item It does not establish that the substrate is uniquely selected by
paper/sections/06_stress_tests.tex:145:  $C\times P$ coupling among regular 4-polytopes.
paper/sections/06_stress_tests.tex:150:test of one preregistered interaction prediction, on a fresh-seed
paper/sections/06_stress_tests.tex:153:theorem about why they do it.
paper/sections/06_stress_tests.tex:161:preregistered validation gave estimates consistent with underpowered
paper/sections/06_stress_tests.tex:162:detection on both interaction tests (P3 and P4); both close at higher
paper/sections/06_stress_tests.tex:163:$N$ without threshold modification. For preregistration design more broadly:
paper/sections/06_stress_tests.tex:164:when preregistering an interaction effect on a system with unknown
paper/sections/08_discussion.tex:6:theories of consciousness, identifies what is novel here that is not
paper/sections/08_discussion.tex:8:ACT bridge to the companion adaptive-closure-transport
paper/sections/08_discussion.tex:10:selection theorem, we do not claim a Lyapunov derivation, and we do
paper/sections/08_discussion.tex:11:not claim the recurrent layer ``is'' consciousness.
paper/sections/08_discussion.tex:18:  real-cortex EEG signatures without fitted shape parameters on neural
paper/sections/08_discussion.tex:19:  data.} The 600-cell + H$_4$ symmetry is fixed by group theory once
paper/sections/08_discussion.tex:20:  the substrate is chosen; cascade-$\alpha$ matches Sleep-EDFx within
paper/sections/08_discussion.tex:21:  preregistered tolerance with pairwise CI overlap on three reference
paper/sections/08_discussion.tex:22:  ranges; six drug/sleep signatures pass at published-reference
paper/sections/08_discussion.tex:23:  thresholds on a single deterministic substrate. We are not aware of
paper/sections/08_discussion.tex:25:  preregistered cortical correspondences from a graph fixed by group
paper/sections/08_discussion.tex:35:\item \textbf{The 18/18 preregistered correspondences with no
paper/sections/08_discussion.tex:36:  threshold modification.} Every prediction in the preregistered set
paper/sections/08_discussion.tex:37:  passes at the preregistered thresholds. The two interaction tests
paper/sections/08_discussion.tex:38:  (P3, P4) required $N\!\geq\!5$ and $N\!\geq\!20$ respectively, and
paper/sections/08_discussion.tex:39:  one test (P13) required the documented state-reset protocol. We
paper/sections/08_discussion.tex:40:  report this transparently as methodology refinement, not as
paper/sections/08_discussion.tex:41:  threshold change.
paper/sections/08_discussion.tex:44:\subsection{Comparison to existing theories of consciousness}
paper/sections/08_discussion.tex:47:IIT-direction-correct $\Phi$ collapse on propofol ($0.33\!\times$
paper/sections/08_discussion.tex:49:(\S\ref{sec:chain}) makes $\Phi\to 0$ when dynamics are
paper/sections/08_discussion.tex:50:group-symmetric, and $\Phi > 0$ only when dynamics break symmetry.
paper/sections/08_discussion.tex:53:observable consequence on the propofol--wake state contrast. This is
paper/sections/08_discussion.tex:70:Predictive-processing-style refinements (e.g.\ $\eta$ as an adaptive
paper/sections/08_discussion.tex:76:circuits implement context rotation or partial emission. The 600-cell
paper/sections/08_discussion.tex:80:\subsection{The non-load-bearing ACT bridge}\label{ssec:act_bridge}
paper/sections/08_discussion.tex:82:The companion adaptive-closure-transport
paper/sections/08_discussion.tex:88:$D_{\mathrm{ACT}}$:
paper/sections/08_discussion.tex:90:D_{\mathrm{ACT}}\colon (M, L_{M}, W, R_{\mathrm{hom}})
paper/sections/08_discussion.tex:92:(\Rsixhundred,\ \Cph,\ \text{cascade pressure field}\ W_{\mathrm{p}},
paper/sections/08_discussion.tex:93:   \ \texttt{homeostatic\_reset}).
paper/sections/08_discussion.tex:97:witness claims (six signatures, $18/18$, chess $+40.6$pp,
paper/sections/08_discussion.tex:98:HCP $\sigma$-distances) do not require any of the ACT theorems.
paper/sections/08_discussion.tex:100:\textbf{What ACT would have to deliver to make this load-bearing.}
paper/sections/08_discussion.tex:104:\item A Lyapunov function $V(W)$ on the reduced flow whose
paper/sections/08_discussion.tex:109:\item A formal $2I$-equivariance audit of the closure operator
paper/sections/08_discussion.tex:111:\item A full reduced-flow convergence theorem on
paper/sections/08_discussion.tex:115:\emph{substrate witness} for the family that ACT names; ACT is not the
paper/sections/08_discussion.tex:116:selection-theorem witness for ARIA. The companion kernel
paper/sections/08_discussion.tex:139:The bridge from cascade-mechanism interaction on $\Rsixhundred$ to
paper/sections/08_discussion.tex:148:  Allocation discipline for preregistration: when preregistering an
paper/sections/08_discussion.tex:152:\item \textbf{State-reset protocol on non-stationary substrates.}
paper/sections/08_discussion.tex:155:  Any multi-trial benchmark must specify a state-reset protocol or
paper/sections/08_discussion.tex:158:  an explicit reset/equilibration discipline}, not just seed.
paper/sections/08_discussion.tex:167:magnitude of biological symmetry-breaking with no fitted parameters.
paper/sections/08_discussion.tex:173:group-theoretic graph with theorem-level statements of structure
paper/sections/08_discussion.tex:183:\item Do the six drug/sleep signatures replicate across $10$--$20$
paper/sections/08_discussion.tex:186:\item Do alternative regular 4-polytopes ($24$-cell, $120$-cell)
paper/sections/08_discussion.tex:192:\item Does the substrate's amplifier behaviour transfer to other
paper/sections/08_discussion.tex:195:\item Does the Sleep-EDFx three-way CI overlap survive on a different
paper/sections/09_limitations.tex:14:\textbf{Single substrate (the 600-cell).} We have not tested whether
paper/sections/09_limitations.tex:15:other regular 4-polytopes ($24$-cell, $120$-cell) would produce
paper/sections/09_limitations.tex:16:comparable correspondences. The 600-cell was chosen because its
paper/sections/09_limitations.tex:17:H$_4$ Coxeter cascade structure aligns with the empirical signatures
paper/sections/09_limitations.tex:19:\emph{Disclosure:} substrate-witness scope, no uniqueness claim
paper/sections/09_limitations.tex:21:on $\Rsixhundred$. \emph{Strengthening build:} formal ablation against
paper/sections/09_limitations.tex:22:$\{24\text{-cell}, 120\text{-cell}\}$ on the same six-signature
paper/sections/09_limitations.tex:23:battery and the eighteen preregistered tests, with thresholds
paper/sections/09_limitations.tex:27:six-signature results in~\S\ref{ssec:six_signatures} are reported on
paper/sections/09_limitations.tex:32:in~\S\ref{sec:method} and~\S\ref{ssec:six_signatures}.
paper/sections/09_limitations.tex:45:``deliberately structural rather than measurement-fitted''.
paper/sections/09_limitations.tex:53:\textbf{The 600-cell choice is post-hoc justified by empirical
paper/sections/09_limitations.tex:54:observables.} While the construction of $\Rsixhundred$ is theorem-
paper/sections/09_limitations.tex:55:level rigorous (H$_4$ Coxeter group theory), the choice of \emph{this}
paper/sections/09_limitations.tex:56:polytope as the consciousness-substrate instance is motivated by the
paper/sections/09_limitations.tex:59:derivation; not a uniqueness claim''. \emph{Evidence:} the eighteen
paper/sections/09_limitations.tex:60:preregistered correspondences plus six signatures; the H$_4$
paper/sections/09_limitations.tex:61:transitivity theorem ($P17$). \emph{Strengthening build:} comparison
paper/sections/09_limitations.tex:63:ACT-selection-theorem witness via the bridge of~\S\ref{ssec:act_bridge}
paper/sections/09_limitations.tex:71:\S\ref{ssec:cascade} acknowledges non-uniqueness of decomposition.
paper/sections/09_limitations.tex:85:derive the $\Ph^{-2}$ shift as the unique stability clamp under a
paper/sections/09_limitations.tex:91:We do not claim the recurrent self-model layer ``is'' consciousness;
paper/sections/09_limitations.tex:92:we claim quantitative consistency with six published biological
paper/sections/09_limitations.tex:95:\emph{Evidence:} six signatures vs published thresholds.
paper/sections/09_limitations.tex:100:\textbf{$\Phi$ is an IIT-style direction-of-effect proxy, not a full
paper/sections/09_limitations.tex:102:\emph{Evidence:} propofol $\Phi$ collapse to $0.33\!\times$ wake
paper/sections/09_limitations.tex:116:\textbf{Two preregistered interaction tests required higher $N$
paper/sections/09_limitations.tex:117:than originally allocated.} P3 closes at $N\!=\!5$; P4 closes only at
paper/sections/09_limitations.tex:119:methodology issue, not a threshold change. \emph{Disclosure:}
paper/sections/09_limitations.tex:128:threshold modification.} The reversals (P3, P4, P13) are documented
paper/sections/09_limitations.tex:131:the original failure values, the methodology refinement, and the
paper/sections/09_limitations.tex:132:post-refinement values. \emph{Disclosure:} this paper carries those
paper/sections/09_limitations.tex:135:builds for P3/P4/P13 above; no further claim is needed.
paper/sections/09_limitations.tex:138:are frequentist (bootstrap CIs); $\Phi$ is the direction-of-effect
paper/sections/09_limitations.tex:163:  $2I$-equivariance — open build of the ACT companion paper.
paper/sections/09_limitations.tex:164:\item Lyapunov derivation $V(W)$ from a closure functional
paper/sections/09_limitations.tex:165:  $\mathcal{F}$ — open build of the ACT companion paper.
paper/sections/09_limitations.tex:166:\item Selection theorem for $\Rsixhundred$ over alternative regular
paper/sections/09_limitations.tex:168:\item Cross-cohort EEG (TUH, NHM, OpenNeuro non-propofol) replication
paper/sections/09_limitations.tex:169:  of the six signatures.
paper/sections/09_limitations.tex:178:no shape parameters tuned to any neural dataset, is consistent with
paper/sections/09_limitations.tex:179:eighteen preregistered correspondences and six independent drug/sleep
paper/sections/09_limitations.tex:180:EEG signatures, with all original gaps closed by methodology
paper/sections/09_limitations.tex:181:refinement and without modifying any preregistered threshold. We do
paper/sections/09_limitations.tex:182:not claim the substrate \emph{is} consciousness. We do not claim a
paper/sections/09_limitations.tex:183:selection theorem on the ACT bridge. We do not claim uniqueness for
paper/sections/09_limitations.tex:184:$\Rsixhundred$ among regular 4-polytopes. The strengthening builds
paper/sections/10_conclusion.tex:5:The 600-cell regular 4-polytope $\Rsixhundred$ under H$_4$ Coxeter
paper/sections/10_conclusion.tex:9:preregistered neuroscience correspondences plus six independent
paper/sections/10_conclusion.tex:20:\textbf{Headline tally.} On a single deterministic trajectory, six
paper/sections/10_conclusion.tex:21:drug/sleep EEG signatures pass at preregistered thresholds:
paper/sections/10_conclusion.tex:23:propofol modality-switching $1.83\!\times$ wake; propofol continuity
paper/sections/10_conclusion.tex:24:drop $+0.066$; propofol integrated-information $\Phi$ collapse to
paper/sections/10_conclusion.tex:28:The wake $95\%$ CI overlaps simultaneously the real Sleep-EDFx EEG
paper/sections/10_conclusion.tex:30:CI $[2.50, 2.53]$) and ARIA's prior cascade pipeline CI
paper/sections/10_conclusion.tex:33:\textbf{Eighteen preregistered correspondences.} All eighteen pass at
paper/sections/10_conclusion.tex:34:preregistered thresholds, with two interaction tests requiring
paper/sections/10_conclusion.tex:37:the documented \texttt{homeostatic\_reset} state-reset protocol. No
paper/sections/10_conclusion.tex:38:preregistered threshold has been modified. The original 2026-04-20
paper/sections/10_conclusion.tex:39:$15/18$ tally was a methodology-limited reading, not a content
paper/sections/10_conclusion.tex:40:failure; the closure of the three gaps (P3, P4, P13) is documented
paper/sections/10_conclusion.tex:46:causally identifiable and \emph{strongly synergistic}: their
paper/sections/10_conclusion.tex:48:($95\%$ bootstrap CI $[+0.143, +0.239]$, $0/2000$ resamples at or
paper/sections/10_conclusion.tex:57:amplification on the two tasks tested: chess 4-category position
paper/sections/10_conclusion.tex:58:classification on 8-D V2 features lifts $+40.6$pp on leave-one-out at
paper/sections/10_conclusion.tex:60:$93.8\%$, with state reset; preregistered threshold $\geq +15$pp on
paper/sections/10_conclusion.tex:61:$5$-fold CV — the LOO finding above is a stricter validation-protocol
paper/sections/10_conclusion.tex:62:refinement at the same threshold), while
paper/sections/10_conclusion.tex:64:(threshold $|\cdot|\!<\!10$pp) — and as a maximum-symmetry
paper/sections/10_conclusion.tex:66:on HCP $n\!=\!1003$, ARIA's H$_4$-transitive structure is at
paper/sections/10_conclusion.tex:71:derivation of consciousness, not a selection theorem on the
paper/sections/10_conclusion.tex:72:companion adaptive-closure-transport
paper/sections/10_conclusion.tex:74:uniqueness claim for the 600-cell among regular 4-polytopes. The
paper/sections/10_conclusion.tex:78:HCP replication, a Lyapunov function on the reduced flow,
paper/sections/10_conclusion.tex:79:$2I$-equivariance audit of the closure operator family — are
paper/sections/10_conclusion.tex:82:We are not aware of a prior deterministic geometric architecture
paper/sections/10_conclusion.tex:83:tested against this many preregistered cortical correspondences from
paper/sections/10_conclusion.tex:84:a graph fixed by group theory with no shape parameters tuned to
paper/sections/10_conclusion.tex:87:turn the witness into a selection-theorem-grade claim — including the
paper/sections/05_results.tex:5:This section is the empirical core. \S\ref{ssec:six_signatures}
paper/sections/05_results.tex:6:gives the six drug/sleep EEG signatures on the recurrent layer
paper/sections/05_results.tex:8:preregistered correspondences (set A). \S\ref{ssec:alpha_overlap}
paper/sections/05_results.tex:10:$R\colon (\text{condition / test id}) \to \text{(scalar, threshold,
paper/sections/05_results.tex:16:\subsection{Six drug/sleep EEG signatures}\label{ssec:six_signatures}
paper/sections/05_results.tex:22:\Phi_{\mathrm{traj}}, \mathrm{cont})$.
paper/sections/05_results.tex:32:condition & $n_{\mathrm{evt}}$ & $\alpha$ & 95\% CI & $R^{2}$ & $I_{\mathrm{var}}$ & $\Phi_{\mathrm{traj}}$ & cont \\
paper/sections/05_results.tex:46:\label{tab:six_signatures}
paper/sections/05_results.tex:52:   Sleep-EDFx W$\to$N3 ($n=24$)~\citep{SleepEDFx} &
paper/sections/05_results.tex:55:   OpenNeuro \texttt{ds005620} ($n=8$, $2.96{\times}$)~\citep{OpenNeuroDS005620} &
paper/sections/05_results.tex:56:   $\in[1.5, 5.0]$ & $1.83\times$ & $\checkmark$ \\
paper/sections/05_results.tex:58:   EEG microstate~\citep{Brodbeck2012Microstates} &
paper/sections/05_results.tex:60:4 & Propofol $\Phi$ collapse (IIT) &
paper/sections/05_results.tex:67:   Sleep-EDFx $n=30$ CI~$[2.50, 2.53]$~\citep{BeggsPlenz2003,SleepEDFx} &
paper/sections/05_results.tex:75:All six signatures pass against their published-reference thresholds
paper/sections/05_results.tex:76:on the same deterministic substrate trajectory. The six signatures
paper/sections/05_results.tex:86:\subsection{Eighteen preregistered correspondences}\label{ssec:eighteen_prereg}
paper/sections/05_results.tex:88:\textbf{Tally.} $17/18$ at standard validation
paper/sections/05_results.tex:89:(\texttt{run\_preregistered\_validation.py}, $5$-seed cascade block
paper/sections/05_results.tex:90:plus state-reset protocol); $18/18$ after the $N\!=\!20$ deep-dive
paper/sections/05_results.tex:91:on the residual P4 (\texttt{demo\_p4\_cxp\_deep\_dive.py}, seed range
paper/sections/05_results.tex:92:$32000$--$32019$). \emph{No preregistered threshold has been modified.}
paper/sections/05_results.tex:97:\caption{All eighteen preregistered correspondences, frozen 2026-04-18.}
paper/sections/05_results.tex:106:\textbf{P4} & $C{\times}P$ synergy           & $\geq +0.10$     &
paper/sections/05_results.tex:112:P9  & Chess 5-fold CV                        & $\geq 70\%$      & $83.1\%$ & $\checkmark$ \\
paper/sections/05_results.tex:115:P12 & Chess goldilocks peak                  & $\in \{15, 25, 40, 60\}$ & $n=25$ & $\checkmark$ \\
paper/sections/05_results.tex:116:\textbf{P13} & Chess substrate lift (5-fold CV preregistered; LOO refinement, with reset) & $\geq +15$pp & $+40.6$pp (LOO) & $\checkmark$ \\
paper/sections/05_results.tex:117:P14 & Conv raw 5-fold CV                     & $\geq 75\%$      & $87.5\%$ & $\checkmark$ \\
paper/sections/05_results.tex:120:P17 & ARIA degree std (theorem)              & $= 0$            & $0.0000$ & $\checkmark$ \\
paper/sections/05_results.tex:127:methodology refinement (no threshold change).}
paper/sections/05_results.tex:133:\item P4 (C$\times$P synergy) was below threshold at $N\!=\!3$
paper/sections/05_results.tex:139:  $5$-fold CV with threshold $\geq +15$pp at $n=25$. The 2026-04-29
paper/sections/05_results.tex:140:  validation strengthened the estimator to LOO with state reset, a
paper/sections/05_results.tex:141:  stricter test at the same threshold; the LOO lift was $+3.1$pp
paper/sections/05_results.tex:142:  without state reset on a state-drifted substrate, and $+40.6$pp
paper/sections/05_results.tex:143:  with \texttt{homeostatic\_reset(level=1.0)} between depth measurements
paper/sections/05_results.tex:145:  report this as a \emph{validation-protocol refinement on the
paper/sections/05_results.tex:146:  preregistered estimator}, not as preregistration revision.
paper/sections/05_results.tex:149:\textbf{Headline verdict.} Eighteen preregistered correspondences
paper/sections/05_results.tex:150:all pass at preregistered thresholds, with two interaction tests
paper/sections/05_results.tex:153:requiring the documented state-reset protocol. The original $15/18$
paper/sections/05_results.tex:154:result was a methodology-limited tally, not a content failure.
paper/sections/05_results.tex:172:Real EEG (Sleep-EDFx, $n=30$ subjects)~\citep{SleepEDFx} & $2.51$ & $[2.50, 2.53]$ & 30 \\
paper/sections/05_results.tex:174:\textbf{v4 WAKE consciousness chain} & $\mathbf{2.252}$ & $[\mathbf{1.82, 2.86}]$ & 58 events \\
paper/sections/05_results.tex:180:real Sleep-EDFx EEG CI $[2.50, 2.53]$, overlaps the ARIA prior
paper/sections/05_results.tex:184:intersections (WAKE $\cap$ Sleep-EDFx, WAKE $\cap$ prior pipeline,
paper/sections/05_results.tex:190:no fitted parameter on neural data. The bounded-top-$K$ at
paper/sections/05_results.tex:192:(Lemma~\ref{lem:600cell}); the $\Ph^{-2}$ shift in $\Cph$ is a
paper/sections/05_results.tex:194:biological time-scale parameters but is not measurement-fitted to
paper/sections/03_substrate.tex:2:\section{The 600-cell response substrate}\label{sec:substrate}
paper/sections/03_substrate.tex:16:The 600-cell $\Rsixhundred$ has $120$ vertices in
paper/sections/03_substrate.tex:17:$\mathbb{R}^{4}$~\citep{CoxeterRegularPolytopes,Weisstein600Cell}.
paper/sections/03_substrate.tex:27:Coxeter group acts transitively on the vertex set; in particular,
paper/sections/03_substrate.tex:38:spectrum are standard~\citep{CoxeterRegularPolytopes,Weisstein600Cell}.
paper/sections/03_substrate.tex:39:\begin{lemma}[600-cell graph facts]\label{lem:600cell}
paper/sections/03_substrate.tex:54:The non-trivial eigenmodes partition into Coxeter exponent classes.
paper/sections/03_substrate.tex:79:\emph{not} a derived theorem; it is a stability choice. The companion
paper/sections/03_substrate.tex:92:$G_{V_{600}}$ (Lemma~\ref{lem:600cell}), pinned by the substrate, not
paper/sections/03_substrate.tex:93:fitted to any dataset.
paper/sections/03_substrate.tex:98:average degree, not a fitted threshold. No other shape parameter
paper/sections/03_substrate.tex:137:cascade is a decomposition of operators on $\Rsixhundred$, and the
paper/sections/03_substrate.tex:138:choice of $\Rsixhundred$ as the active substrate is post-hoc justified
paper/sections/03_substrate.tex:144:\item Fixed by group theory once $\Rsixhundred$ is chosen: $|V|=120$,
paper/sections/03_substrate.tex:150:\item Not fixed by this paper: the choice of $\Rsixhundred$ over the
paper/sections/03_substrate.tex:153:  ablation against alternative regular 4-polytopes is an open build
paper/sections/04_consciousness_chain.tex:7:To test high-level signatures — NREM-N3 variance collapse, propofol
paper/sections/04_consciousness_chain.tex:8:regime-switching, propofol $\Phi$ collapse — we add a recurrent
paper/sections/04_consciousness_chain.tex:11:coupling $\eta$, and four trajectory observables. No shape parameter
paper/sections/04_consciousness_chain.tex:15:recurrent layer ``is'' consciousness; we report which numerical
paper/sections/04_consciousness_chain.tex:57:$G_{V_{600}}$ (Lemma~\ref{lem:600cell}), pinned by the substrate
paper/sections/04_consciousness_chain.tex:60:above band or with degraded fit. We do not search $k$ over a fitted
paper/sections/04_consciousness_chain.tex:64:            \texorpdfstring{$\Phi$}{Phi}}
paper/sections/04_consciousness_chain.tex:67:\texttt{kernel/consciousness\_binding.py:phi\_iit\_trajectory}.
paper/sections/04_consciousness_chain.tex:74:\Phi \;=\; \max\!\bigl(0,\; |c_{\mathrm{full}}| - \mathrm{mean}_{k}\,|c_{k}|\bigr).
paper/sections/04_consciousness_chain.tex:76:By construction $\Phi\to 0$ under H$_{4}$-equivariant dynamics, since
paper/sections/04_consciousness_chain.tex:78:$\Phi > 0$ only when the dynamics break symmetry and transport
paper/sections/04_consciousness_chain.tex:83:We position $\Phi$ as an IIT-style direction-of-effect proxy, not as
paper/sections/04_consciousness_chain.tex:86:machinery~\citep{Tononi2008,BalduzziTononi2008}. The propofol $\Phi$
paper/sections/04_consciousness_chain.tex:88:of effect on the propofol-vs-wake state contrast; it is not a
paper/sections/04_consciousness_chain.tex:104:This composite produces the propofol continuity-drop signature
paper/sections/04_consciousness_chain.tex:111:\texttt{kernel/consciousness\_binding.py:bind\_phenomenal\_field}.
paper/sections/04_consciousness_chain.tex:147:measurement-fitted: amplitudes and durations match published
paper/sections/04_consciousness_chain.tex:151:not a derived theorem.
paper/sections/04_consciousness_chain.tex:157:ablation grid is the basis for the preregistered tests P1--P5 and
paper/sections/04_consciousness_chain.tex:174:(above threshold but not yet crossed) emit pressure at $30\%$ scale,
paper/sections/07_cross_domain.tex:27:or leave-one-out (LOO).
paper/sections/07_cross_domain.tex:30:measurements the substrate is reset to canonical state via
paper/sections/07_cross_domain.tex:31:\texttt{mon.homeostatic\_reset(level=1.0)}. Without this, pressure-
paper/sections/07_cross_domain.tex:38:\caption{Chess substrate-routed depth sweep with state reset between
paper/sections/07_cross_domain.tex:58:\caption{Chess preregistered tests (with reset, $n=25$ canonical
paper/sections/07_cross_domain.tex:65:P9  & 5-fold CV (seeds 30200--30204)        & $\geq 70\%$ & $83.1\%$ & $\checkmark$ \\
paper/sections/07_cross_domain.tex:68:P12 & goldilocks peak depth                 & $\in\{15,25,40,60\}$ & $n=25$ & $\checkmark$ \\
paper/sections/07_cross_domain.tex:69:\textbf{P13} & substrate lift, LOO refinement (with reset)$^{\ddagger}$ & $\geq +15$pp & $\mathbf{+40.6}$pp (LOO) & $\checkmark$ \\
paper/sections/07_cross_domain.tex:81:substrate-lift estimator as $5$-fold CV at threshold $\geq +15$pp.
paper/sections/07_cross_domain.tex:82:The 2026-04-29 validation tightened the estimator to LOO with state
paper/sections/07_cross_domain.tex:83:reset; we report the LOO finding ($+40.6$pp) above as a stricter
paper/sections/07_cross_domain.tex:84:validation-protocol refinement at the unchanged $+15$pp threshold,
paper/sections/07_cross_domain.tex:87:\textbf{Reading.} Substrate routing amplifies chess-position
paper/sections/07_cross_domain.tex:89:chance) to substrate-routed $93.8\%$ at canonical depth $n=25$.
paper/sections/07_cross_domain.tex:90:This is a $+40.6$pp lift on the LOO refinement; on the preregistered
paper/sections/07_cross_domain.tex:93:The original 2026-04-20 validation reported the LOO lift at
paper/sections/07_cross_domain.tex:94:$+3.1$pp, a state-drift artefact closed by the reset protocol
paper/sections/07_cross_domain.tex:105:H$_4$-symmetric amplifier acting on whatever input lands in the
paper/sections/07_cross_domain.tex:107:bonus. We do not claim this decomposition is unique; it is a
paper/sections/07_cross_domain.tex:119:\caption{Conversation preregistered tests.}
paper/sections/07_cross_domain.tex:125:P14 & raw 5-fold CV (seeds 30220--30224)    & $\geq 75\%$ & $87.5\%$ & $\checkmark$ \\
paper/sections/07_cross_domain.tex:134:lift is $-4.4$pp, well within the preregistered neutrality band
paper/sections/07_cross_domain.tex:137:\textbf{Selective amplifier signature.} The pair (chess
paper/sections/07_cross_domain.tex:138:$+40.6$pp lift; conversation $-4.4$pp lift) is consistent with the
paper/sections/07_cross_domain.tex:139:selective-amplifier behaviour preregistered in 2026-04-18: in these
paper/sections/07_cross_domain.tex:140:two tasks, the architecture amplifies when raw features are ambiguous
paper/sections/07_cross_domain.tex:151:$n=1003$ subjects~\citep{VanEssen2013HCP}; preregistered tests on
paper/sections/07_cross_domain.tex:152:$n=100$ subjects for computational tractability, with full-cohort
paper/sections/07_cross_domain.tex:153:$n=1003$ descriptive statistics also reported. ICA-50 group-averaged
paper/sections/07_cross_domain.tex:154:connectivity matrix; thresholded at the same density as ARIA's
paper/sections/07_cross_domain.tex:157:$\Lop$. By H$_4$ transitivity (Lemma~\ref{lem:600cell}) every vertex
paper/sections/07_cross_domain.tex:159:$\Rightarrow$ degree std $= 0$ as a theorem.
paper/sections/07_cross_domain.tex:164:\caption{HCP comparison: preregistered $n=100$ test plus full-cohort
paper/sections/07_cross_domain.tex:165:$n=1003$ descriptive statistics.}
paper/sections/07_cross_domain.tex:169:Metric & ARIA & HCP $n=1003$ mean (sd) & $\sigma$ from HCP \\
paper/sections/07_cross_domain.tex:171:Degree std (preregistered, $n=100$ subset) & $0.000$ & $3.388$ ($> 2.0$) & --- \\
paper/sections/07_cross_domain.tex:172:Degree std (descriptive, $n=1003$)         & $0.000$ & $3.28\pm 0.28$ & $-11.58\sigma$ \\
paper/sections/07_cross_domain.tex:180:\item P17 (ARIA degree std, theorem): predicted $=0$, observed
paper/sections/07_cross_domain.tex:182:\item P18 (HCP ICA-50 degree std, $n=100$ density-matched):
paper/sections/07_cross_domain.tex:183:  predicted $> 2.0$, observed $3.388$, $\checkmark$. Zero of $1003$
paper/sections/07_cross_domain.tex:192:fitted parameters. The $\sigma$-distances ($-11.58\sigma$ on degree
paper/sections/07_cross_domain.tex:195:density-matched threshold $\rho = 0.101$; cross-parcellation
paper/sections/07_cross_domain.tex:229:\subsection{Cross-domain summary as a selective amplifier
paper/sections/07_cross_domain.tex:241:Chess (LOO, $n=25$, w/ reset) & $53.1\%$ & $93.8\%$ & --- & --- & $+40.6$pp lift \\
paper/sections/07_cross_domain.tex:242:Chess (5-fold CV)             & ---      & $83.1\%$ & $65.4\%$ & $65.4\%$ & $+17.7$pp \\
paper/sections/07_cross_domain.tex:243:Conversation (5-fold CV)      & $87.5\%$ & $83.1\%$ & $70.6\%$ & $70.6\%$ & $+12.5$pp (raw vs null) \\
paper/sections/07_cross_domain.tex:256:\emph{selectively} amplifying (not unconditionally), and it is a
paper/sections/07_cross_domain.tex:257:maximum-symmetry deterministic null on connectivity (not a fitted
paper/sections/02_method.tex:7:the validation script, the seed range, the threshold, and the
paper/sections/02_method.tex:17:falsifiable threshold, (iii) the validation test (script + seed range),
paper/sections/02_method.tex:21:predictions and rung observables — were preregistered on 2026-04-24
paper/sections/02_method.tex:24:not include those batteries in the headline 18/18 tally.} They are
paper/sections/02_method.tex:28:recurrent layer (\texttt{demo\_drug\_sleep\_v4.py}) test six
paper/sections/02_method.tex:30:propofol switching ratio, propofol continuity drop, propofol $\Phi$
paper/sections/02_method.tex:35:\textbf{No threshold has been modified post-hoc.} Where the original
paper/sections/02_method.tex:36:2026-04-20 validation reported failures (P3, P4, P13), the documented
paper/sections/02_method.tex:37:methodological refinements were
paper/sections/02_method.tex:40:(P4, C$\times$P), and
paper/sections/02_method.tex:41:(c)~wiring \texttt{homeostatic\_reset(level=1.0)} between depth-sweep
paper/sections/02_method.tex:42:measurements for the chess LOO test (P13). None of these touched a
paper/sections/02_method.tex:43:preregistered threshold.
paper/sections/02_method.tex:49:\text{threshold}, \text{result})$.
paper/sections/02_method.tex:60:P1 ($\alpha$ SOC band) & \texttt{run\_preregistered\_validation.py} & 30000--30004 & this paper & $\alpha\in[2.5, 3.5]$ \\
paper/sections/02_method.tex:63:\textbf{P4 ($C{\times}P$)} & \texttt{demo\_p4\_cxp\_deep\_dive.py} & 32000--32019 & this paper & $\geq +0.10$ \\
paper/sections/02_method.tex:64:P5 ($|E|$) & \texttt{run\_preregistered\_validation.py} & 30030--30034 & this paper & $|\cdot| < 0.15$ \\
paper/sections/02_method.tex:65:P6 (real EEG $\alpha$) & same & 30100 & Sleep-EDFx~\citep{SleepEDFx} & $\alpha\in[2.0, 3.0]$ \\
paper/sections/02_method.tex:66:P7 ($W{\to}N3$ var) & same & deterministic & Sleep-EDFx ($n=24$) & $<0.70$ \\
paper/sections/02_method.tex:67:P8 ($W{\to}N3$ switch) & same & deterministic & Sleep-EDFx ($n=24$) & $<0.50$ \\
paper/sections/02_method.tex:68:P9 (chess 5-fold) & same & 30200--30204 & 32 positions, 4 cat. & $\geq 70\%$ \\
paper/sections/02_method.tex:71:P12 (goldilocks) & \texttt{run\_preregistered\_validation.py} & with reset & same & $n\in\{15,25,40,60\}$ \\
paper/sections/02_method.tex:72:\textbf{P13 (chess sub.\ lift)} & same & with reset & same (LOO refinement) & $\geq +15$pp \\
paper/sections/02_method.tex:73:P14 (conv 5-fold) & same & 30220--30224 & 64 utt., 8 cat. & $\geq 75\%$ \\
paper/sections/02_method.tex:76:P17 (ARIA deg std) & substrate construction & deterministic & H$_4$ theorem & $=0$ \\
paper/sections/02_method.tex:86:\textbf{Sleep-EDFx (PhysioNet).} Public polysomnography
paper/sections/02_method.tex:91:methodology~\citep{BeggsPlenz2003}.
paper/sections/02_method.tex:94:consciousness EEG, $n=8$~\citep{OpenNeuroDS005620},
paper/sections/02_method.tex:96:empirical reference for the propofol switching ratio
paper/sections/02_method.tex:97:($2.96\!\times$ wake) in Sig~2.
paper/sections/02_method.tex:110:matrix. The preregistered test (P18) was on $n=100$ subjects for
paper/sections/02_method.tex:111:computational tractability; full-cohort $n=1003$ statistics
paper/sections/02_method.tex:114:preregistered test.
paper/sections/02_method.tex:117:signature (Sig~3) follows the EEG microstate methodology lineage of
paper/sections/02_method.tex:118:Brodbeck et al.~\citep{Brodbeck2012Microstates} on wake/NREM
paper/sections/02_method.tex:119:microstates. Brodbeck et al.\ is not a propofol-specific paper; we
paper/sections/02_method.tex:120:use it for the underlying microstate-fragmentation methodology, not
paper/sections/02_method.tex:121:as a propofol reference. A propofol-specific microstate citation
paper/sections/02_method.tex:139:preregistered cascade-$\alpha$ tests, 2000 resamples for the
paper/sections/02_method.tex:141:preregistered; 42 for the deep-dive.
paper/sections/02_method.tex:144:deep-dive, $0/2000$ bootstrap resamples were at or below zero, and
paper/sections/02_method.tex:145:$0/2000$ were below the preregistered floor $+0.10$; we report these
paper/sections/02_method.tex:146:as $0.0000$ rather than $P=0$ to avoid the suggestion of an exact
paper/sections/02_method.tex:160:on the full $n=1003$ subject distribution.
paper/sections/02_method.tex:162:\subsection{State-reset protocol}
paper/sections/02_method.tex:168:explicit reset between successive evaluations.
paper/sections/02_method.tex:169:\texttt{kernel/dimensional\_monitor.py:DimensionalMonitor.homeostatic\_reset(level=1.0)}
paper/sections/02_method.tex:171:canonical baseline. With reset between depth measurements, the chess
paper/sections/02_method.tex:172:LOO lift recovers from $+3.1$pp (without reset, on a state-drifted
paper/sections/02_method.tex:173:substrate) to $+40.6$pp (with reset, far exceeding the $+15$pp
paper/sections/02_method.tex:174:preregistered floor). The reset protocol is documented in
paper/sections/02_method.tex:178:state-reset protocol.
paper/sections/02_method.tex:189:\item Eighteen preregistered:
paper/sections/02_method.tex:190:  \texttt{python3 run\_preregistered\_validation.py}
paper/sections/02_method.tex:200:verdicts (CI overlaps, $P$-value thresholds) are unaffected.
paper/main.tex:17:\newcommand{\Rsixhundred}{V_{600}}
paper/main.tex:20:       eighteen preregistered correspondences and six drug/sleep EEG\\
paper/main.tex:21:       signatures from the 600-cell under H$_4$ Coxeter symmetry}
paper/main.tex:39:Once the 600-cell substrate is chosen, its graph structure is fixed by
paper/main.tex:46:quantitative correspondences with neuroscience data — preregistered
paper/main.tex:47:on 2026-04-18 before any validation run — plus six drug/sleep EEG
paper/main.tex:49:published-reference thresholds on a single deterministic substrate
paper/main.tex:50:trajectory at seed~$42$. No shape parameter is tuned to any neural
paper/main.tex:60:that a geometry-fixed substrate, with no shape parameters tuned to any
paper/main.tex:61:neural dataset, is consistent with eighteen preregistered correspondences
paper/main.tex:62:and six EEG signatures. It is not a derivation of consciousness, nor a
paper/main.tex:63:selection theorem, nor a uniqueness claim for the 600-cell among regular
paper/main.tex:64:4-polytopes. The companion adaptive-closure-transport
paper/main.tex:67:sits as the $L_M$ instance; the selection of the 600-cell as the active
paper/main.tex:71:We test whether a geometry-fixed substrate — the 600-cell regular
paper/main.tex:72:4-polytope $\Rsixhundred$ under H$_4$ Coxeter symmetry, with the
paper/main.tex:76:preregistered on 2026-04-18 (\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md})
paper/main.tex:77:before any validation run; each has a falsifiable threshold. The
paper/main.tex:78:preregistered tally is $17/18$ at standard validation methodology
paper/main.tex:79:($5$-seed cascade block plus state-reset protocol), and $18/18$ after
paper/main.tex:81:interaction (P4); no preregistered threshold has been modified. We
paper/main.tex:82:additionally report six drug/sleep EEG signatures tested on a recurrent
paper/main.tex:84:trajectory at seed~$42$. The six signatures are not part of the
paper/main.tex:86:thresholds (Sleep-EDFx, OpenNeuro, Brodbeck, Tononi) and were obtained
paper/main.tex:93:This 95\% CI overlaps simultaneously real Sleep-EDFx EEG ($n=30$
paper/main.tex:94:subjects, $\alpha=2.51$, CI $[2.50, 2.53]$) and ARIA's prior cascade
paper/main.tex:100:(predicted $\sim 0.365$, threshold $<\!0.70$); propofol modality-switching
paper/main.tex:101:ratio $1.83\!\times$ wake (threshold $\in[1.5, 5.0]$, empirical
paper/main.tex:102:reference $2.96\!\times$ from OpenNeuro \texttt{ds005620}, $n=8$);
paper/main.tex:103:propofol continuity drop $+0.066$ (threshold $>\!0.020$); propofol
paper/main.tex:104:integrated-information $\Phi$ collapse to $0.33\!\times$ wake (IIT
paper/main.tex:106:All six signatures pass against their published-reference thresholds
paper/main.tex:111:emission $P$ — are causally significant, and the original
paper/main.tex:112:preregistered C$\times$P synergy prediction $\geq +0.10$ closes
paper/main.tex:115:(threshold $\geq +0.10$); $0/2000$ bootstrap resamples were at or
paper/main.tex:123:The substrate exhibits domain-invariant selective amplification on
paper/main.tex:125:8-dimensional V2 features lifts $+40.6$ percentage points on
paper/main.tex:127:$\to$ substrate-routed $93.8\%$, with state reset; the
paper/main.tex:128:preregistered estimator P13 was $5$-fold CV with threshold
paper/main.tex:129:$\geq\!+15$pp; the LOO finding above is a stronger validation-protocol
paper/main.tex:130:refinement at the same threshold), while conversation utterance
paper/main.tex:132:(threshold $|\cdot| < 10$pp), consistent with selective amplification
paper/main.tex:134:(preregistered $n\!=\!100$ ICA-50 plus full-cohort $n\!=\!1003$
paper/main.tex:142:We do not claim the 600-cell is the unique substrate consistent with
paper/main.tex:143:these signatures, nor that other regular 4-polytopes (24-cell, 120-cell)
paper/main.tex:150:substrate, with no shape parameters tuned to any neural dataset,
paper/main.tex:151:is consistent with eighteen preregistered neuroscience
paper/main.tex:152:correspondences and six drug/sleep EEG signatures, with all gaps in
paper/main.tex:153:the original preregistration closed by methodology refinement and
paper/main.tex:154:without modifying any preregistered threshold.}
paper/main.tex:161:\input{sections/04_consciousness_chain.tex}
paper/main.tex:171:We thank the Sleep-EDFx (PhysioNet)~\citep{PhysioNet2000,SleepEDFx},
paper/main.tex:172:OpenNeuro propofol cohort \texttt{ds005620}~\citep{OpenNeuroDS005620},
paper/main.tex:177:methodology follows~\citep{BeggsPlenz2003}; the integrated-information
paper/main.tex:178:$\Phi$ proxy is in the IIT family~\citep{Tononi2008,BalduzziTononi2008};
paper/main.tex:179:the propofol microstate comparison uses Brodbeck et
paper/main.tex:180:al.~\citep{Brodbeck2012Microstates}. The 600-cell construction
paper/main.tex:181:follows~\citep{CoxeterRegularPolytopes,Weisstein600Cell}. All code
paper/main.tex:186:The complete pipeline (substrate construction, six-signature
paper/main.tex:187:consciousness chain, $N\!=\!20$ C$\times$P deep-dive, eighteen-prediction
paper/main.tex:188:preregistered validation, figure regeneration, this paper) is reproducible
paper/main.tex:193:$N\!=\!20$ deep-dive $\sim 28$\,min; preregistered validation
paper/sections/01_introduction.tex:5:Theories of consciousness divide into mechanism-driven proposals
paper/sections/01_introduction.tex:11:stories but have not yielded preregistered quantitative signatures
paper/sections/01_introduction.tex:13:numbers but typically introduce fitted parameters, learned weights,
paper/sections/01_introduction.tex:18:consistent with under \emph{no} shape parameter tuning, no learned
paper/sections/01_introduction.tex:20:600-cell regular 4-polytope $\Rsixhundred$, treated as a graph with
paper/sections/01_introduction.tex:21:H$_4$ Coxeter symmetry. It has been studied in pure mathematics for
paper/sections/01_introduction.tex:22:over a century~\citep{CoxeterRegularPolytopes,Weisstein600Cell}; to
paper/sections/01_introduction.tex:24:consciousness substrate. We construct $\Rsixhundred$, fix its response
paper/sections/01_introduction.tex:28:against eighteen preregistered correspondences plus six independent
paper/sections/01_introduction.tex:34:substrate, with no shape parameters tuned to any neural dataset, is
paper/sections/01_introduction.tex:35:consistent with eighteen preregistered correspondences (frozen
paper/sections/01_introduction.tex:36:2026-04-18) and six independent drug/sleep EEG signatures of
paper/sections/01_introduction.tex:41:  $\Rsixhundred$ is selected, $120$ vertices of uniform degree $12$
paper/sections/01_introduction.tex:49:  three-way overlapping the Sleep-EDFx EEG CI $[2.50, 2.53]$
paper/sections/01_introduction.tex:54:  collapse to $0.463\!\times$ wake; propofol modality-switching
paper/sections/01_introduction.tex:55:  $1.83\!\times$ wake; propofol continuity drop $+0.066$; propofol
paper/sections/01_introduction.tex:56:  $\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
paper/sections/01_introduction.tex:59:\item \textbf{Eighteen preregistered correspondences pass.}
paper/sections/01_introduction.tex:60:  $17/18$ at standard methodology; $18/18$ after a documented
paper/sections/01_introduction.tex:62:  test; \emph{no preregistered threshold has been modified}.
paper/sections/01_introduction.tex:64:  a domain-invariant selective amplifier (chess $+40.6$pp leave-one-out
paper/sections/01_introduction.tex:66:  preregistered neutrality bounds) and a maximum-symmetry deterministic
paper/sections/01_introduction.tex:67:  null reference for cortical functional connectivity (HCP $n\!=\!1003$:
paper/sections/01_introduction.tex:75:\item \emph{Not a uniqueness claim.} We do not claim the 600-cell is
paper/sections/01_introduction.tex:76:  the unique substrate consistent with these signatures. Other regular
paper/sections/01_introduction.tex:78:  build, not a discharged comparison. The 600-cell choice is post-hoc
paper/sections/01_introduction.tex:79:  motivated by the H$_4$ Coxeter cascade structure and biological
paper/sections/01_introduction.tex:81:\item \emph{Not a derivation of consciousness.} The substrate witness
paper/sections/01_introduction.tex:83:  establish that the substrate \emph{is} consciousness, nor that
paper/sections/01_introduction.tex:85:\item \emph{Not a selection theorem.} The companion adaptive-closure-
paper/sections/01_introduction.tex:88:  this substrate fills the $L_M$ slot. The selection of the 600-cell
paper/sections/01_introduction.tex:90:  non-load-bearing here. We do not deliver a Lyapunov function on the
paper/sections/01_introduction.tex:91:  reduced flow, nor a $2I$-equivariance audit of the closure operator,
paper/sections/01_introduction.tex:97:  that some such mechanisms appear in the substrate's preregistered
paper/sections/01_introduction.tex:102:  bounds the Green response). It is not derived as a theorem from a
paper/sections/01_introduction.tex:117:\;=\;\{\text{`consistent with', `inside threshold', `direction confirmed'}\}.
paper/sections/01_introduction.tex:119:We never write `the substrate \emph{is} cortex' or `derives consciousness'.
paper/sections/01_introduction.tex:120:A result that lands inside its preregistered threshold licenses a
paper/sections/01_introduction.tex:121:`consistent with' claim. A result that exceeds the preregistered
paper/sections/01_introduction.tex:122:threshold by an order of magnitude (e.g.\ chess $+40.6$pp vs the
paper/sections/01_introduction.tex:134:\emph{Tested:} 18 preregistered correspondences plus 6 drug/sleep EEG
paper/sections/01_introduction.tex:138:\emph{Not claimed:} substrate uniqueness; derivation of consciousness;
paper/sections/01_introduction.tex:139:selection theorem on the 4-tuple bridge; circuit-level mechanistic
paper/sections/01_introduction.tex:141:that cortex \emph{is} the 600-cell.
paper/sections/01_introduction.tex:148:seeds, scripts, datasets, thresholds). \S\ref{sec:substrate}
paper/sections/01_introduction.tex:149:constructs $\Rsixhundred$ and the response operator $\Cph$, with the
paper/sections/01_introduction.tex:153:\S\ref{sec:results} reports the empirical tables: six drug/sleep
paper/sections/01_introduction.tex:154:signatures, eighteen preregistered correspondences, three-way
paper/sections/01_introduction.tex:160:ACT bridge (without claiming a selection theorem).

exec
/bin/bash -lc 'for f in 01_introduction 02_method 03_substrate 04_consciousness_chain 05_results 06_stress_tests 07_cross_domain 08_discussion 09_limitations; do echo =====$f=====; nl -ba "/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/${f}.tex" | sed -n '"'1,240p'; done" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 329ms:
=====01_introduction=====
     1	% =====================================================================
     2	\section{Introduction}\label{sec:intro}
     3	% =====================================================================
     4	
     5	Theories of consciousness divide into mechanism-driven proposals
     6	(Integrated Information Theory~\citep{Tononi2008,BalduzziTononi2008},
     7	Global Workspace Theory~\citep{Baars1988GWT,Dehaene2014ConsciousAndBrain},
     8	predictive processing~\citep{FristonFreeEnergy2010,ClarkPP2013}) and
     9	structure-driven proposals (geometric or topological substrates,
    10	neural-population dynamics). The mechanism-driven proposals offer compelling axiomatic
    11	stories but have not yielded preregistered quantitative signatures
    12	that survive on real EEG data. The structure-driven proposals produce
    13	numbers but typically introduce fitted parameters, learned weights,
    14	or domain-specific tuning.
    15	
    16	This paper takes a deliberately constrained third path. Once a
    17	substrate is chosen, we ask which neuroscience phenomena it is
    18	consistent with under \emph{no} shape parameter tuning, no learned
    19	weights, and no domain-specific calibration. The substrate is the
    20	600-cell regular 4-polytope $\Rsixhundred$, treated as a graph with
    21	H$_4$ Coxeter symmetry. It has been studied in pure mathematics for
    22	over a century~\citep{CoxeterRegularPolytopes,Weisstein600Cell}; to
    23	our knowledge it has not been proposed before as an empirical
    24	consciousness substrate. We construct $\Rsixhundred$, fix its response
    25	operator $\Cph = \Lop + \Ph^{-2} I$ where $\Ph=(1+\sqrt 5)/2$, add a
    26	single condition-dependent self-injection coupling $\eta$ and a
    27	single graph-pinned nonlinearity, and test the resulting witness
    28	against eighteen preregistered correspondences plus six independent
    29	drug/sleep EEG signatures.
    30	
    31	\subsection*{What this paper claims}
    32	
    33	We claim a single \emph{substrate witness}: that a geometry-fixed
    34	substrate, with no shape parameters tuned to any neural dataset, is
    35	consistent with eighteen preregistered correspondences (frozen
    36	2026-04-18) and six independent drug/sleep EEG signatures of
    37	conscious vs unconscious states.
    38	
    39	\begin{enumerate}\itemsep=2pt
    40	\item \textbf{Substrate is fixed by group theory once chosen.} Once
    41	  $\Rsixhundred$ is selected, $120$ vertices of uniform degree $12$
    42	  are forced by H$_4$ transitivity, the Laplacian eigenvalues
    43	  $\{0, 3, 4\Ph, 6\Ph, 12\!-\!4\Ph, 12\!-\!6\Ph, 12\!-\!3, 12\}$ in
    44	  their irrep multiplicities are forced by character theory, and
    45	  the response operator $\Cph$ is fully fixed up to the single
    46	  parameter $\Ph^{-2}$ (a stability shift for the inverse map).
    47	\item \textbf{Cortical avalanches.} Wake cascade-event power-law
    48	  exponent $\alpha = 2.252$, $95\%$ CI $[1.82, 2.86]$ ($R^{2}=0.956$),
    49	  three-way overlapping the Sleep-EDFx EEG CI $[2.50, 2.53]$
    50	  (n$=$30 subjects) and ARIA's prior cascade-pipeline CI
    51	  $[2.73, 3.25]$.
    52	\item \textbf{Six drug/sleep signatures.} On a single deterministic
    53	  trajectory at seed $42$: NREM-N3 phenomenal-intensity variance
    54	  collapse to $0.463\!\times$ wake; propofol modality-switching
    55	  $1.83\!\times$ wake; propofol continuity drop $+0.066$; propofol
    56	  $\Phi$ collapse to $0.33\!\times$ wake (IIT direction confirmed);
    57	  recovery deterministically identical to wake; wake cascade-$\alpha$
    58	  in the SOC band.
    59	\item \textbf{Eighteen preregistered correspondences pass.}
    60	  $17/18$ at standard methodology; $18/18$ after a documented
    61	  $N\!=\!20$ deep-dive on the residual high-variance interaction
    62	  test; \emph{no preregistered threshold has been modified}.
    63	\item \textbf{Cross-domain selectivity.} The substrate functions as
    64	  a domain-invariant selective amplifier (chess $+40.6$pp leave-one-out
    65	  lift at depth $n\!=\!25$ ticks; conversation $-4.4$pp lift, within
    66	  preregistered neutrality bounds) and a maximum-symmetry deterministic
    67	  null reference for cortical functional connectivity (HCP $n\!=\!1003$:
    68	  ARIA at $-11.58\sigma$ on degree homogeneity; $+79.78\sigma$ on
    69	  participation ratio).
    70	\end{enumerate}
    71	
    72	\subsection*{What this paper does \emph{not} claim}
    73	
    74	\begin{itemize}\itemsep=2pt
    75	\item \emph{Not a uniqueness claim.} We do not claim the 600-cell is
    76	  the unique substrate consistent with these signatures. Other regular
    77	  4-polytopes (the 24-cell, the 120-cell) are an explicit ablation
    78	  build, not a discharged comparison. The 600-cell choice is post-hoc
    79	  motivated by the H$_4$ Coxeter cascade structure and biological
    80	  observables; it is not an a-priori derivation from first principles.
    81	\item \emph{Not a derivation of consciousness.} The substrate witness
    82	  shows quantitative agreement with cortical signatures; it does not
    83	  establish that the substrate \emph{is} consciousness, nor that
    84	  its dynamics implement specific phenomenal content.
    85	\item \emph{Not a selection theorem.} The companion adaptive-closure-
    86	  transport preprint~\citep{SmartAdaptiveClosureTransport2026}
    87	  proposes a 4-tuple bridge $(M, L_M, W, R_{\mathrm{hom}})$ in which
    88	  this substrate fills the $L_M$ slot. The selection of the 600-cell
    89	  as the active $M$ is conjectural in that paper and is treated as
    90	  non-load-bearing here. We do not deliver a Lyapunov function on the
    91	  reduced flow, nor a $2I$-equivariance audit of the closure operator,
    92	  nor a formal edge-space decomposition. These are listed as open
    93	  builds in~\S\ref{sec:limitations}.
    94	\item \emph{Not a circuit-level model.} The substrate is at the
    95	  architectural-algorithmic level. We do not identify which neural
    96	  populations implement context rotation or partial emission, only
    97	  that some such mechanisms appear in the substrate's preregistered
    98	  ablation matrix and exhibit strong inter-mechanism coupling.
    99	\item \emph{Not a derivation of the $\Ph^{-2}$ floor.} The shifted-
   100	  Laplacian floor $\Ph^{-2} \approx 0.382$ is a design-level
   101	  stability clamp (it makes $\Cph$ strictly positive definite and
   102	  bounds the Green response). It is not derived as a theorem from a
   103	  closure functional. The companion kernel
   104	  document~\citep{SmartAriaClosureKernel2026} discusses its role.
   105	\end{itemize}
   106	
   107	\subsection*{Mapping from numerical results to admissible claims}
   108	
   109	To keep this paper inside the substrate-witness scope, we use the
   110	following claim-boundary discipline. Numerical results
   111	$\mathcal R_{\mathrm{numeric}}$ are mapped to admissible claims
   112	$\mathcal C_{\mathrm{admissible}}$ by the rule
   113	\[
   114	q\colon \mathcal R_{\mathrm{numeric}} \longrightarrow \mathcal C_{\mathrm{admissible}},
   115	\qquad
   116	\mathcal C_{\mathrm{admissible}}
   117	\;=\;\{\text{`consistent with', `inside threshold', `direction confirmed'}\}.
   118	\]
   119	We never write `the substrate \emph{is} cortex' or `derives consciousness'.
   120	A result that lands inside its preregistered threshold licenses a
   121	`consistent with' claim. A result that exceeds the preregistered
   122	threshold by an order of magnitude (e.g.\ chess $+40.6$pp vs the
   123	$+15$pp floor) licenses `decisively above prereg', not `proves'. A
   124	$\sigma$-distance result against an external null
   125	(e.g.\ $-11.58\sigma$ on HCP degree homogeneity) licenses `outside
   126	the biological distribution', not `cortex has drifted from an ideal
   127	polytope'. The claim-boundary rule is summarised in the box below
   128	and applied throughout~\S\ref{sec:results}.
   129	
   130	\medskip
   131	\begin{center}
   132	\fbox{\parbox{0.92\linewidth}{\small
   133	\textbf{What is tested / what is not claimed.}\par
   134	\emph{Tested:} 18 preregistered correspondences plus 6 drug/sleep EEG
   135	signatures, on a geometry-fixed substrate with one condition-dependent
   136	parameter $\eta$ and one graph-pinned nonlinearity, against published
   137	biological observables.\par
   138	\emph{Not claimed:} substrate uniqueness; derivation of consciousness;
   139	selection theorem on the 4-tuple bridge; circuit-level mechanistic
   140	identification; first-principles derivation of $\Ph^{-2}$ shift;
   141	that cortex \emph{is} the 600-cell.
   142	}}
   143	\end{center}
   144	
   145	\subsection*{Layout}
   146	
   147	\S\ref{sec:method} gives the provenance ledger (preregistration date,
   148	seeds, scripts, datasets, thresholds). \S\ref{sec:substrate}
   149	constructs $\Rsixhundred$ and the response operator $\Cph$, with the
   150	$\Ph^{-2}$ shift disclosed as a design-level stability clamp.
   151	\S\ref{sec:chain} adds the recurrent self-model layer above the
   152	substrate (single nonlinearity, single self-injection coupling).
   153	\S\ref{sec:results} reports the empirical tables: six drug/sleep
   154	signatures, eighteen preregistered correspondences, three-way
   155	$\alpha$-overlap. \S\ref{sec:stress} presents the C$\times$P
   156	synergy stress test ($N\!=\!3, 5, 10, 20$ trend with bootstrap
   157	$95\%$ CI). \S\ref{sec:cross_domain} reports cross-domain
   158	selectivity (chess, conversation, HCP). \S\ref{sec:discussion}
   159	discusses the substrate witness and proposes a non-load-bearing
   160	ACT bridge (without claiming a selection theorem).
   161	\S\ref{sec:limitations} enumerates limitations and the
   162	hostile-review guard matrix. \S\ref{sec:conclusion} concludes.
=====02_method=====
     1	% =====================================================================
     2	\section{Methods and provenance}\label{sec:method}
     3	% =====================================================================
     4	
     5	This section is a provenance ledger. It records, for each empirical
     6	claim downstream, the dataset, the preregistration date and document,
     7	the validation script, the seed range, the threshold, and the
     8	wallclock — the minimal information a hostile reviewer needs to
     9	reproduce or refute the claim.
    10	
    11	\subsection{Preregistration discipline}
    12	
    13	\textbf{Frozen 2026-04-18.} Eighteen quantitative predictions
    14	(P1--P18) were locked on 2026-04-18 in
    15	\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md} before any validation
    16	run. Each prediction has (i) a specific numerical claim, (ii) a
    17	falsifiable threshold, (iii) the validation test (script + seed range),
    18	and (iv) a rationale identifying what would falsify it.
    19	
    20	\textbf{Frozen 2026-04-24.} Two later batteries — H$_4$ fingerprint
    21	predictions and rung observables — were preregistered on 2026-04-24
    22	in \texttt{docs/brain\_mapping/PREREG\_H4\_FINGERPRINT.md} and
    23	\texttt{docs/brain\_mapping/PREREG\_RUNG\_OBSERVABLES.md}. \emph{We do
    24	not include those batteries in the headline 18/18 tally.} They are
    25	listed as future strengthening builds in~\S\ref{sec:limitations}.
    26	
    27	\textbf{Six EEG signatures (set B).} The drug/sleep signatures on the
    28	recurrent layer (\texttt{demo\_drug\_sleep\_v4.py}) test six
    29	independent published biological signatures (NREM-N3 variance ratio,
    30	propofol switching ratio, propofol continuity drop, propofol $\Phi$
    31	collapse, recovery reversibility, wake cascade-$\alpha$). They are
    32	not part of the P1--P18 preregistration; they are reported as a
    33	companion validation set on the recurrent layer.
    34	
    35	\textbf{No threshold has been modified post-hoc.} Where the original
    36	2026-04-20 validation reported failures (P3, P4, P13), the documented
    37	methodological refinements were
    38	(a)~increasing $N$ from $3$ to $5$ for cascade interaction terms,
    39	(b)~adding a $N\!=\!20$ deep-dive for the highest-variance interaction
    40	(P4, C$\times$P), and
    41	(c)~wiring \texttt{homeostatic\_reset(level=1.0)} between depth-sweep
    42	measurements for the chess LOO test (P13). None of these touched a
    43	preregistered threshold.
    44	
    45	\subsection{Provenance ledger}
    46	
    47	We write the provenance map as $\Pi\colon\{\text{claim id}\}
    48	\to (\text{script}, \text{seed range}, \text{dataset/source},
    49	\text{threshold}, \text{result})$.
    50	
    51	\begin{table}[ht]
    52	\centering
    53	\small
    54	\caption{Provenance ledger for the headline empirical claims.}
    55	\label{tab:provenance}
    56	\begin{tabular}{l l l l l}
    57	\toprule
    58	Claim & Script & Seed range & Dataset / source & Threshold \\
    59	\midrule
    60	P1 ($\alpha$ SOC band) & \texttt{run\_preregistered\_validation.py} & 30000--30004 & this paper & $\alpha\in[2.5, 3.5]$ \\
    61	P2 ($C$ main) & same & 30010--30014 & this paper & $\geq +0.30$ \\
    62	P3 ($|D{\times}C|$) & same & 30020--30024 & this paper & $|\cdot| < 0.20$ \\
    63	\textbf{P4 ($C{\times}P$)} & \texttt{demo\_p4\_cxp\_deep\_dive.py} & 32000--32019 & this paper & $\geq +0.10$ \\
    64	P5 ($|E|$) & \texttt{run\_preregistered\_validation.py} & 30030--30034 & this paper & $|\cdot| < 0.15$ \\
    65	P6 (real EEG $\alpha$) & same & 30100 & Sleep-EDFx~\citep{SleepEDFx} & $\alpha\in[2.0, 3.0]$ \\
    66	P7 ($W{\to}N3$ var) & same & deterministic & Sleep-EDFx ($n=24$) & $<0.70$ \\
    67	P8 ($W{\to}N3$ switch) & same & deterministic & Sleep-EDFx ($n=24$) & $<0.50$ \\
    68	P9 (chess 5-fold) & same & 30200--30204 & 32 positions, 4 cat. & $\geq 70\%$ \\
    69	P10 (chess null) & \texttt{run\_chess\_robustness.py} & 30210 & same & $\geq 50\%$ \\
    70	P11 (chess random-label) & same & 30210+ & same & $\in [15\%, 35\%]$ \\
    71	P12 (goldilocks) & \texttt{run\_preregistered\_validation.py} & with reset & same & $n\in\{15,25,40,60\}$ \\
    72	\textbf{P13 (chess sub.\ lift)} & same & with reset & same (LOO refinement) & $\geq +15$pp \\
    73	P14 (conv 5-fold) & same & 30220--30224 & 64 utt., 8 cat. & $\geq 75\%$ \\
    74	P15 ($|$conv lift$|$) & same & same & same & $|\cdot| < 10$pp \\
    75	P16 (conv null) & \texttt{run\_conversation\_robustness.py} & 30210 & same & $\geq 50\%$ \\
    76	P17 (ARIA deg std) & substrate construction & deterministic & H$_4$ theorem & $=0$ \\
    77	P18 (HCP deg std) & \texttt{run\_hcp\_validation.py} & deterministic & HCP S1200~\citep{VanEssen2013HCP} & $> 2.0$ \\
    78	\midrule
    79	Sig 1--6 (drug/sleep) & \texttt{demo\_drug\_sleep\_v4.py} & seed 42 & published biological & per-signature \\
    80	\bottomrule
    81	\end{tabular}
    82	\end{table}
    83	
    84	\subsection{Datasets and DOIs}
    85	
    86	\textbf{Sleep-EDFx (PhysioNet).} Public polysomnography
    87	recordings~\citep{SleepEDFx,PhysioNet2000}; $n=30$ subjects used for
    88	the cortical-avalanche $\alpha$ baseline; $n=24$ subjects used for
    89	the wake$\to$N3 variance and switching ratios. Cortical-avalanche
    90	fitting follows the Beggs--Plenz log-CCDF
    91	methodology~\citep{BeggsPlenz2003}.
    92	
    93	\textbf{OpenNeuro \texttt{ds005620}.} Propofol-induced loss of
    94	consciousness EEG, $n=8$~\citep{OpenNeuroDS005620},
    95	DOI \texttt{10.18112/openneuro.ds005620.v1.0.0}. Used as the
    96	empirical reference for the propofol switching ratio
    97	($2.96\!\times$ wake) in Sig~2.
    98	
    99	\textbf{OpenNeuro \texttt{ds004902}.} DMT-induced altered states
   100	EEG~\citep{OpenNeuroDS004902},
   101	DOI \texttt{10.18112/openneuro.ds004902.v1.0.8}. Background
   102	psychedelic-state reference; not load-bearing for the headline tally.
   103	
   104	\textbf{Zenodo \texttt{3992359}.} DMT EEG public
   105	release~\citep{ZenodoDMT3992359},
   106	DOI \texttt{10.5281/zenodo.3992359}. Same status as above.
   107	
   108	\textbf{HCP S1200.} Human Connectome Project
   109	S1200~\citep{VanEssen2013HCP}, ICA-50 group-averaged connectivity
   110	matrix. The preregistered test (P18) was on $n=100$ subjects for
   111	computational tractability; full-cohort $n=1003$ statistics
   112	(degree std, participation ratio, clustering coefficient $\sigma$-
   113	distances) are reported as descriptive statistics on top of the
   114	preregistered test.
   115	
   116	\textbf{Microstate baseline (qualifier).} The continuity-drop
   117	signature (Sig~3) follows the EEG microstate methodology lineage of
   118	Brodbeck et al.~\citep{Brodbeck2012Microstates} on wake/NREM
   119	microstates. Brodbeck et al.\ is not a propofol-specific paper; we
   120	use it for the underlying microstate-fragmentation methodology, not
   121	as a propofol reference. A propofol-specific microstate citation
   122	would tighten this section; we treat that as an open
   123	strengthening build.
   124	
   125	\subsection{Statistical methods}
   126	
   127	\textbf{Cascade-$\alpha$ fitting.} Power-law $\alpha$ is fit by
   128	ordinary least squares on the log-CCDF of the cascade-event size
   129	distribution, restricted to the central 80\% mass band (excluding the
   130	bottom 10\% and top 10\% to avoid extreme-tail noise). $R^{2}$ is
   131	reported on the linear fit in log-space. A cascade event is defined
   132	as an attention-vertex shift between consecutive ticks
   133	$\arg\max|\mathrm{state}_{t}|\neq \arg\max|\mathrm{state}_{t-1}|$;
   134	the event size is the $\ell^{1}$ norm of the state-difference vector
   135	at that tick. Zero-size events are excluded.
   136	
   137	\textbf{Bootstrap confidence intervals.} 95\% CIs on $\alpha$ are
   138	estimated by event-resampling bootstrap (500 resamples for the
   139	preregistered cascade-$\alpha$ tests, 2000 resamples for the
   140	$N\!=\!20$ C$\times$P deep-dive). Bootstrap RNG seed: 7919 for
   141	preregistered; 42 for the deep-dive.
   142	
   143	\textbf{Bootstrap one-sided $P$-value reporting.} For the C$\times$P
   144	deep-dive, $0/2000$ bootstrap resamples were at or below zero, and
   145	$0/2000$ were below the preregistered floor $+0.10$; we report these
   146	as $0.0000$ rather than $P=0$ to avoid the suggestion of an exact
   147	zero-probability statement on a finite resample.
   148	
   149	\textbf{Factorial interaction estimator.} For the $2{\times}2$
   150	ablation conditions $\{----, -C--, --P-, -CP-\}$, the interaction is
   151	\[
   152	\Delta_{CP}
   153	\;=\;\frac{(\alpha_{\!-CP\!-}+\alpha_{\!-\!-\!-\!-})
   154	        - (\alpha_{\!-C\!-\!-}+\alpha_{\!-\!-P\!-})}{2}.
   155	\]
   156	
   157	\textbf{$\sigma$-distance against external nulls.} For the HCP
   158	comparisons we report
   159	$Z_{m} = (m_{\mathrm{ARIA}} - \mu_{\mathrm{HCP}}) / \sigma_{\mathrm{HCP}}$
   160	on the full $n=1003$ subject distribution.
   161	
   162	\subsection{State-reset protocol}
   163	
   164	The substrate exhibits state drift: across approximately five
   165	successive depth-sweep evaluations the pressure field equilibrates
   166	to a uniform attractor and classification structure collapses to
   167	raw-feature baseline. Multi-trial benchmarks therefore require an
   168	explicit reset between successive evaluations.
   169	\texttt{kernel/dimensional\_monitor.py:DimensionalMonitor.homeostatic\_reset(level=1.0)}
   170	re-initialises pressure-field, crossed-vertex, and training state to
   171	canonical baseline. With reset between depth measurements, the chess
   172	LOO lift recovers from $+3.1$pp (without reset, on a state-drifted
   173	substrate) to $+40.6$pp (with reset, far exceeding the $+15$pp
   174	preregistered floor). The reset protocol is documented in
   175	\texttt{docs/brain\_mapping/NON\_EQUILIBRIUM\_FINDING.md}; a more
   176	generalisable lesson is recorded in \S\ref{sec:limitations}: any
   177	multi-trial benchmark on a non-stationary substrate must specify
   178	state-reset protocol.
   179	
   180	\subsection{Reproducibility commands}
   181	
   182	\begin{itemize}\itemsep=2pt
   183	\item Substrate self-test:
   184	  \texttt{python3 -c "from kernel.sigma\_orbit\_basis import \_self\_test; \_self\_test()"}.
   185	\item Six drug/sleep signatures:
   186	  \texttt{python3 demo\_drug\_sleep\_v4.py} ($\sim 30$\,s).
   187	\item C$\times$P synergy $N\!=\!20$ deep-dive:
   188	  \texttt{python3 demo\_p4\_cxp\_deep\_dive.py} ($\sim 28$\,min).
   189	\item Eighteen preregistered:
   190	  \texttt{python3 run\_preregistered\_validation.py}
   191	  ($\sim 18$\,min).
   192	\item Whole-paper repro:
   193	  \texttt{bash reproduce\_paper\_claims.sh}.
   194	\end{itemize}
   195	
   196	All scripts are deterministic given seeds. Reruns at seed $42$ on the
   197	recurrent layer should reproduce per-condition means in this paper to
   198	4~decimal places. Bootstrap CIs may differ in the 4th decimal due to
   199	NumPy version differences in the bootstrap RNG; the qualitative
   200	verdicts (CI overlaps, $P$-value thresholds) are unaffected.
=====03_substrate=====
     1	% =====================================================================
     2	\section{The 600-cell response substrate}\label{sec:substrate}
     3	% =====================================================================
     4	
     5	This section constructs the substrate. \S\ref{ssec:vertices}
     6	gives the vertex set. \S\ref{ssec:graph} gives the graph and its
     7	H$_4$-symmetry-forced spectrum. \S\ref{ssec:cphi} gives the response
     8	operator $\Cph$ and the $\Ph^{-2}$ stability clamp.
     9	\S\ref{ssec:shells} gives the 9-shell decomposition used for source
    10	projection. \S\ref{ssec:cascade} sketches the seven-rung cascade
    11	descent referenced by the recurrent layer in~\S\ref{sec:chain}. None
    12	of these objects depend on neural data.
    13	
    14	\subsection{Vertex construction}\label{ssec:vertices}
    15	
    16	The 600-cell $\Rsixhundred$ has $120$ vertices in
    17	$\mathbb{R}^{4}$~\citep{CoxeterRegularPolytopes,Weisstein600Cell}.
    18	With $\Ph = (1+\sqrt 5)/2$ the canonical vertex set is
    19	\begin{itemize}\itemsep=1pt
    20	\item $8$ vertices: all permutations of $(\pm 1, 0, 0, 0)$;
    21	\item $16$ vertices: all sign combinations of
    22	  $(\pm 1, \pm 1, \pm 1, \pm 1)/2$;
    23	\item $96$ vertices: all even permutations of
    24	  $(\pm \Ph, \pm 1, \pm 1/\Ph, 0)/2$.
    25	\end{itemize}
    26	All $120$ vertices lie on the unit $3$-sphere $S^{3}$. The H$_4$
    27	Coxeter group acts transitively on the vertex set; in particular,
    28	every vertex has identical local structure. Implementation:
    29	\texttt{kernel/vfd\_closure\_kernel.py:build\_600cell\_vertices}.
    30	
    31	\subsection{Graph and Laplacian spectrum}\label{ssec:graph}
    32	
    33	The substrate graph $G_{V_{600}} = (V, E)$ is built by connecting each
    34	vertex to its nearest neighbours under the Euclidean metric on $S^{3}$.
    35	H$_4$ acts transitively on the vertex set, forcing uniformity of the
    36	local structure; the eigenvalue multiplicities follow from H$_4$
    37	character theory on the regular representation. The construction and
    38	spectrum are standard~\citep{CoxeterRegularPolytopes,Weisstein600Cell}.
    39	\begin{lemma}[600-cell graph facts]\label{lem:600cell}
    40	The graph $G_{V_{600}}$ has $|V|=120$ vertices, $|E|=720$ edges, every
    41	vertex has degree exactly $12$, and the unweighted graph Laplacian
    42	$\Lop = D - A$ has spectrum
    43	\[
    44	\sigma(\Lop) \;=\;
    45	\bigl\{0^{1}, 3^{4}, 4\Ph^{9}, 6\Ph^{16}, (12\!-\!4\Ph)^{9},
    46	       (12\!-\!6\Ph)^{16}, 9^{4}, 12^{1}\bigr\},
    47	\]
    48	where the exponent denotes multiplicity. The decomposition into H$_4$
    49	irreducible representations is exact at machine precision; the
    50	$\sigma$-orbit projector basis (\texttt{kernel/sigma\_orbit\_basis.py})
    51	realises it block-by-block with cross-block norm $<10^{-15}$.
    52	\end{lemma}
    53	
    54	The non-trivial eigenmodes partition into Coxeter exponent classes.
    55	For H$_4$ proper, the exponents are $\{1, 11, 19, 29\}$; for the
    56	Galois twin $\sigma(\mathrm{H}_4)$ under the $\sigma$-automorphism of
    57	$\mathbb{Z}[\Ph]$, the exponents become $\{7, 13, 17, 23\}$. We label
    58	the eigenspaces $K_{1}, K_{11}, K_{19}, K_{29}$ for H$_4$-proper modes
    59	and $K_{7}, K_{13}, K_{17}, K_{23}$ for $\sigma$-twin modes. The
    60	multiplicities follow from character theory and are reproduced in
    61	the implementation
    62	(\texttt{kernel/sigma\_orbit\_basis.py:\_self\_test}). The
    63	$K_{7}$-modes will be the dominant phenomenal-binding profile in
    64	\S\ref{sec:chain}.
    65	
    66	\subsection{The shifted-Laplacian response \texorpdfstring{$\Cph$}{C\_phi}}\label{ssec:cphi}
    67	
    68	The substrate's linear response to an external source $f \in \mathbb{R}^{120}$
    69	is the discrete Green's function of the shifted Laplacian:
    70	\begin{equation}\label{eq:cphi}
    71	\Cph \;=\; \Lop + \Ph^{-2} I,
    72	\qquad
    73	\psi \;=\; \Cph^{-1} f.
    74	\end{equation}
    75	The shift $\Ph^{-2} \approx 0.382$ is a design-level stability
    76	clamp: it makes $\Cph$ strictly positive definite (smallest eigenvalue
    77	$\Ph^{-2}$, since the trivial Laplacian eigenvalue is $0$), so that the
    78	inverse is bounded with operator norm $\Ph^{2}\approx 2.618$. This is
    79	\emph{not} a derived theorem; it is a stability choice. The companion
    80	kernel document~\citep{SmartAriaClosureKernel2026} discusses the same
    81	$\Cph$ as the basis for an independent passive-regime witness in
    82	flavour physics~\citep{SmartBAnomaly2026}, where the same operator
    83	form (without retuning the shift) describes the
    84	$B\to K^{*}\mu^{+}\mu^{-}$ angular anomaly across five public datasets.
    85	This paper imports $\Cph$ from that line; we do not re-derive it.
    86	
    87	The response $\psi = \Cph^{-1} f$ is smooth in $f$. By itself it does
    88	not produce critical-state cascade statistics; the recurrent layer
    89	in~\S\ref{sec:chain} adds a graph-pinned nonlinearity
    90	$\mathrm{bounded\_topk}(\psi, k\!=\!12)$ to obtain self-organised-critical
    91	event distributions. The choice $k\!=\!12$ is the average degree of
    92	$G_{V_{600}}$ (Lemma~\ref{lem:600cell}), pinned by the substrate, not
    93	fitted to any dataset.
    94	
    95	\paragraph{Disclosure (substrate-witness scope).}
    96	The $\Ph^{-2}$ floor is a stability shift, not a derived parameter.
    97	The bounded-top-$K$ nonlinearity uses $k\!=\!12$ pinned to the graph's
    98	average degree, not a fitted threshold. No other shape parameter
    99	enters. The condition-dependent self-injection coupling
   100	$\eta\in\{0, 0.05, 0.20\}$ is the only architectural parameter that
   101	varies between conditions in~\S\ref{sec:chain}; it is reported
   102	explicitly per condition.
   103	
   104	\subsection{Shell decomposition}\label{ssec:shells}
   105	
   106	Under the H$_3$ subgroup, the $120$ vertices partition into $9$
   107	spherical shells indexed by Euclidean inner product with a chosen pole:
   108	\[
   109	\bigl(|S_0|,\ldots,|S_8|\bigr) \;=\; (1, 12, 20, 12, 30, 12, 20, 12, 1).
   110	\]
   111	The middle shell $S_{4}$ has $30$ vertices on the equatorial plane
   112	(the icosidodecahedral ring). When projecting onto a continuum kernel
   113	in companion preprints~\citep{SmartAriaClosureKernel2026}, the
   114	shell-mean projection of the equatorial-source response,
   115	$\kappa(x) = \mathrm{shell\text{-}mean}[\Cph^{-1} f_{\mathrm{equat}}](x)$,
   116	collapses on the continuum exponential $\frac{\Ph}{2}\,e^{-|x|/\Ph}$.
   117	This paper does not use that continuum projection; we work with the
   118	discrete operator throughout.
   119	
   120	\subsection{Cascade descent (sketch)}\label{ssec:cascade}
   121	
   122	The recurrent layer in~\S\ref{sec:chain} references a cascade
   123	decomposition $E_{8}\to H_{4}\to H_{3}\to D_{4}\to \mathrm{Cl}(1,3)
   124	\to S^{7}\to 0$, implemented in
   125	\texttt{kernel/cascade\_descent.py:descend\_operator\_e8\_to\_h4\_clean}.
   126	An arbitrary operator on the $E_{8}$ root system descends to the
   127	4-D H$_4$ subspace through a sequence of orthogonal projections, each
   128	preserving the Frobenius norm to within $10^{-15}$. The
   129	$\sigma$-orbit projector basis from
   130	\texttt{kernel/sigma\_orbit\_basis.py} gives the K-class block
   131	decomposition at machine precision.
   132	
   133	The descent provides numerical stability for the cascade ablations:
   134	when one ablates a specific K-class contribution (e.g.\ $K_{7}$), the
   135	remaining operator structure is exactly preserved. We do not claim
   136	the cascade itself is forced by physics on a pre-substrate level; the
   137	cascade is a decomposition of operators on $\Rsixhundred$, and the
   138	choice of $\Rsixhundred$ as the active substrate is post-hoc justified
   139	by the empirical correspondences in~\S\ref{sec:results}.
   140	
   141	\subsection{What the substrate is fixed-by, and what it is not}
   142	
   143	\begin{itemize}\itemsep=2pt
   144	\item Fixed by group theory once $\Rsixhundred$ is chosen: $|V|=120$,
   145	  uniform degree $12$, Laplacian spectrum, $9$-shell partition, K-class
   146	  irrep block structure, average degree $k\!=\!12$, $\sigma$-twin pairing.
   147	\item Fixed by stability choice: the $\Ph^{-2}$ shift in $\Cph$. This
   148	  is not a derivation; it is a design-level clamp that bounds the
   149	  response inverse.
   150	\item Not fixed by this paper: the choice of $\Rsixhundred$ over the
   151	  $24$-cell or $120$-cell. The choice is post-hoc motivated by the H$_4$
   152	  cascade structure and the empirical correspondences. A formal
   153	  ablation against alternative regular 4-polytopes is an open build
   154	  (\S\ref{sec:limitations}).
   155	\end{itemize}
=====04_consciousness_chain=====
     1	% =====================================================================
     2	\section{The recurrent layer}\label{sec:chain}
     3	% =====================================================================
     4	
     5	The cascade-pipeline substrate (\S\ref{sec:substrate}) reproduces
     6	cortical-avalanche statistics matching real EEG (\S\ref{sec:results}).
     7	To test high-level signatures — NREM-N3 variance collapse, propofol
     8	regime-switching, propofol $\Phi$ collapse — we add a recurrent
     9	self-model layer above the substrate. The layer adds one
    10	graph-pinned nonlinearity, one condition-dependent self-injection
    11	coupling $\eta$, and four trajectory observables. No shape parameter
    12	is fit to any neural dataset.
    13	
    14	This section is method, not metaphysics. We do not claim the
    15	recurrent layer ``is'' consciousness; we report which numerical
    16	observables on the layer's trajectory match published biological
    17	signatures in~\S\ref{sec:results}.
    18	
    19	\subsection{The recurrent loop}
    20	
    21	Implementation: \texttt{kernel/self\_model\_stream.py:SelfModelLoop}.
    22	At each tick $t$ the substrate state evolves as
    23	\begin{align}
    24	f_{\mathrm{total}}(t) &= f_{\mathrm{ext}}(t) + \eta\cdot f_{\mathrm{self}}(\mathrm{snap}_{t-1}, \psi_{t-1}), \\
    25	\psi_{t} &= \Cph^{-1}\, f_{\mathrm{total}}(t), \\
    26	\psi^{\mathrm{thr}}_{t} &= \mathrm{bounded\_topk}(\psi_{t}, k=12), \\
    27	\mathrm{state}_{t} &= \mathrm{decay}\cdot\mathrm{state}_{t-1} + (1-\mathrm{decay})\cdot \psi^{\mathrm{thr}}_{t}, \\
    28	\mathrm{snap}_{t} &= \mathrm{bind\_phenomenal\_field}(\psi_{t}, \texttt{profile=K\_7\_only}),
    29	\end{align}
    30	with $\mathrm{decay}=0.95$ (state EMA factor) and $\eta$ the only
    31	condition-dependent architectural parameter. $f_{\mathrm{self}}$ maps
    32	the prior phenomenal snapshot to a directional source weighted by
    33	ignition $\times$ intensity (cosine direction alignment with the
    34	prior snapshot). The substrate response operator $\Cph$ is unchanged
    35	across all conditions.
    36	
    37	Conditions:
    38	\begin{itemize}\itemsep=2pt
    39	\item $\eta = 0.20$ for WAKE and RECOVERY (active recurrent self-loop);
    40	\item $\eta = 0.05$ for SLEEP\_N3 (attenuated self-loop);
    41	\item $\eta = 0.00$ for PROPOFOL (broken recurrence; residual cortex
    42	  preserved as background drive).
    43	\end{itemize}
    44	
    45	\subsection{The graph-pinned nonlinearity}
    46	
    47	\textbf{$\mathrm{bounded\_topk}(\psi, k=12)$.} This is the load-bearing
    48	nonlinearity, implemented in
    49	\texttt{kernel/lyapunov\_selector.py:bounded\_topk}: zero all but the
    50	top-$12$ vertex amplitudes (by absolute value), and rescale the rest
    51	to a small fraction of their baseline. Linear Green response alone
    52	gives smooth dynamics with cascade $\alpha\approx 1.09$ — no
    53	avalanches. Adding bounded-top-$K$ at $k=12$ drives $\alpha$ into the
    54	SOC band $(2.0, 3.5)$ with $R^{2}>0.85$.
    55	
    56	\textbf{Why $k=12$.} The choice $k=12$ is the average degree of
    57	$G_{V_{600}}$ (Lemma~\ref{lem:600cell}), pinned by the substrate
    58	geometry, not by neural data. Smaller $k$ (e.g.\ $k=6$) gives $\alpha$
    59	at the band edge with poorer fit; larger $k$ ($24, 48$) gives $\alpha$
    60	above band or with degraded fit. We do not search $k$ over a fitted
    61	window; $k$ is determined by the graph.
    62	
    63	\subsection{The integrated-information proxy
    64	            \texorpdfstring{$\Phi$}{Phi}}
    65	
    66	Implementation:
    67	\texttt{kernel/consciousness\_binding.py:phi\_iit\_trajectory}.
    68	Given the state history matrix $S\in\mathbb{R}^{T\times 120}$, write
    69	$A = S\cdot V$ for the H$_4$-eigenvector matrix $V$ (mode amplitudes
    70	$A\in\mathbb{R}^{T\times 120}$). Define $c_{\mathrm{full}}$ as the
    71	lag-$1$ auto-correlation of the full system, and $c_{k}$ as the
    72	lag-$1$ auto-correlation within the K-class irrep block $k$. Then
    73	\[
    74	\Phi \;=\; \max\!\bigl(0,\; |c_{\mathrm{full}}| - \mathrm{mean}_{k}\,|c_{k}|\bigr).
    75	\]
    76	By construction $\Phi\to 0$ under H$_{4}$-equivariant dynamics, since
    77	group symmetry forbids information transport across irrep classes;
    78	$\Phi > 0$ only when the dynamics break symmetry and transport
    79	information across class boundaries. This is a port of the published
    80	\texttt{integrated\_information\_phi\_irrep} proxy from the cascade
    81	pipeline, adapted to take amplitude trajectories from any source.
    82	
    83	We position $\Phi$ as an IIT-style direction-of-effect proxy, not as
    84	a full implementation of IIT. ARIA does not implement cause-effect
    85	repertoires, exclusion postulate, or integration-over-partitions
    86	machinery~\citep{Tononi2008,BalduzziTononi2008}. The propofol $\Phi$
    87	collapse in~\S\ref{sec:results} is consistent with the IIT direction
    88	of effect on the propofol-vs-wake state contrast; it is not a
    89	discharge of the IIT axioms.
    90	
    91	\subsection{The continuity composite}
    92	
    93	Implementation:
    94	\texttt{kernel/self\_model\_stream.py:StreamContinuityScorer}.
    95	A composite first-person continuity score over a 64-tick rolling
    96	window:
    97	\begin{align*}
    98	b_{\mathrm{cont}} &= \mathrm{mean\ cos\text{-}sim\ of\ consecutive}\ (I, L, P)\,\mathrm{vectors},\\
    99	v_{\mathrm{cont}} &= 1/(1 + 4\cdot \mathrm{var}(\mathrm{valence})),\\
   100	m_{\mathrm{pers}} &= \mathrm{frac.\ of\ consecutive\ same\text{-}modality\ ticks},\\
   101	i_{\mathrm{smooth}} &= 1/(1 + 4\cdot \mathrm{TV}(\mathrm{intensity})),\\
   102	\mathrm{composite} &= 0.35\cdot b_{\mathrm{cont}} + 0.25\cdot v_{\mathrm{cont}} + 0.20\cdot m_{\mathrm{pers}} + 0.20\cdot i_{\mathrm{smooth}}.
   103	\end{align*}
   104	This composite produces the propofol continuity-drop signature
   105	(WAKE composite $0.943$; PROPOFOL composite $0.877$;
   106	drop $+0.066$).
   107	
   108	\subsection{The phenomenal-field binding}
   109	
   110	Implementation:
   111	\texttt{kernel/consciousness\_binding.py:bind\_phenomenal\_field}.
   112	The substrate state $\psi_{t}$ is mapped to a phenomenal snapshot
   113	with channels (intensity $I$, self-luminosity $L$, presence $P$,
   114	valence, modality\_label). The modality\_label is determined by which
   115	H$_4$ K-class dominates the isotypic compression of $\psi_{t}$ under
   116	the $\sigma$-orbit projector basis. The default profile
   117	\texttt{K\_7\_only} restricts to $\sigma$-twin K-classes for modality
   118	labelling; H$_4$-proper classes contribute amplitude bias.
   119	
   120	\subsection{Stimulus models}
   121	
   122	Implementation: \texttt{demo\_drug\_sleep\_v4.py}. Four conditions
   123	$\times$ $800$ ticks each at seed $42$:
   124	
   125	\textbf{WAKE.} AR(1) cortical noise ($\beta=0.90$), tonic equator-shell
   126	coherence (small always-on bias), and attention episodes (20--50
   127	ticks at amplitude $0.8$, anchored to the largest shell with $15\%$
   128	within-shell rotation per tick). The AR(1) gives temporal correlation
   129	that lets the $\eta=0.20$ self-loop integrate; tonic coherence anchors
   130	modality; attention episodes mimic biological visual fixation
   131	(200--400~ms dwell time analogue); within-shell rotation generates
   132	cascade events without changing modality.
   133	
   134	\textbf{SLEEP\_N3.} Slow oscillation ($\sim 1$\,Hz analogue,
   135	amplitude $1.0$) on a coherent shell, plus spindle bursts ($12$ ticks
   136	every $100$ at amplitude $0.4$ fast modulation), plus K-complexes
   137	($4\%$ of ticks at amplitude $0.8$).
   138	
   139	\textbf{PROPOFOL.} Low-amplitude tonic noise (amplitude $0.05$);
   140	$\eta = 0.00$ (broken recurrence). Residual cortex preserved as
   141	background drive.
   142	
   143	\textbf{RECOVERY.} Identical to WAKE — verifies determinism and
   144	reversibility.
   145	
   146	The stimulus models are deliberately structural rather than
   147	measurement-fitted: amplitudes and durations match published
   148	biological time scales but are not tuned to specific signatures.
   149	The full stimulus code is \texttt{demo\_drug\_sleep\_v4.py}. We
   150	disclose stimulus-shape choice as a methodological design move,
   151	not a derived theorem.
   152	
   153	\subsection{Cascade-mechanism ablation matrix}
   154	
   155	The cascade dynamics on the substrate use four mechanisms acting on
   156	the pressure field, each ablatable independently. The $2^{4}$
   157	ablation grid is the basis for the preregistered tests P1--P5 and
   158	the C$\times$P stress test in~\S\ref{sec:stress}.
   159	
   160	\textbf{$D$ — D$_{4}$ orbit coupling.} The H$_4$ root system contains
   161	five disjoint 24-cells (D$_4$ orbits). $D$ adds a small
   162	(coupling $0.05$) cross-orbit pressure averaging that prevents
   163	cascades from localising to one orbit.
   164	Implementation: \texttt{kernel/dimensional\_monitor.py:300-305}.
   165	
   166	\textbf{$C$ — Context rotation (S$^{7}$ observer frames).} The active
   167	observer frame on the S$^{7}$ rung rotates periodically based on
   168	which uncrossed vertices have accumulated pressure aligning with
   169	each frame's preferences. This creates churn in \emph{which}
   170	vertices are uncrossed at any tick.
   171	Implementation: \texttt{kernel/dimensional\_monitor.py:316-318, 823-827}.
   172	
   173	\textbf{$P$ — Partial emission.} High-pressure uncrossed vertices
   174	(above threshold but not yet crossed) emit pressure at $30\%$ scale,
   175	saturating at pressure $3.0$. Without this mechanism, only fully-
   176	crossed vertices emit.
   177	Implementation: \texttt{kernel/dimensional\_monitor.py:842-855}.
   178	
   179	\textbf{$E$ — Equator compensation.} The H$_3$ shell-4 equator is a
   180	30-vertex icosidodecahedral ring with split degree distribution.
   181	$E$ scales pressure gain by $(\bar d / d_{v})$ so sparse commissural
   182	vertices overcome their connectivity deficit.
   183	Implementation: \texttt{kernel/dimensional\_monitor.py:320-360}.
   184	
   185	The four mechanisms are pinned to the substrate's geometry (D$_4$
   186	orbits, S$^{7}$ rung, equatorial shell) — they are not free dynamical
   187	choices. Their causal effects are reported in~\S\ref{sec:stress}.
=====05_results=====
     1	% =====================================================================
     2	\section{Results}\label{sec:results}
     3	% =====================================================================
     4	
     5	This section is the empirical core. \S\ref{ssec:six_signatures}
     6	gives the six drug/sleep EEG signatures on the recurrent layer
     7	(set B). \S\ref{ssec:eighteen_prereg} gives the eighteen
     8	preregistered correspondences (set A). \S\ref{ssec:alpha_overlap}
     9	gives the three-way $\alpha$ overlap. We lift the result map
    10	$R\colon (\text{condition / test id}) \to \text{(scalar, threshold,
    11	verdict)}$ verbatim from the validation outputs without
    12	recomputation; sources are
    13	\texttt{docs/brain\_mapping/CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}
    14	and \texttt{docs/brain\_mapping/VALIDATION\_RESULTS\_2026-04-29.md}.
    15	
    16	\subsection{Six drug/sleep EEG signatures}\label{ssec:six_signatures}
    17	
    18	\textbf{Setup.} Four conditions $\times$ $800$ ticks at seed $42$,
    19	$k_{\mathrm{thr}}=12$, single deterministic substrate
    20	(\S\ref{sec:chain}). Per-condition trajectory observables are
    21	$(n_{\mathrm{evt}}, \alpha, \mathrm{CI}_{95}, R^{2}, I_{\mathrm{var}},
    22	\Phi_{\mathrm{traj}}, \mathrm{cont})$.
    23	
    24	\begin{table}[ht]
    25	\centering
    26	\small
    27	\caption{Per-condition trajectory observables (\texttt{demo\_drug\_sleep\_v4.py},
    28	seed 42).}
    29	\label{tab:per_condition}
    30	\begin{tabular}{l r r l r r r r}
    31	\toprule
    32	condition & $n_{\mathrm{evt}}$ & $\alpha$ & 95\% CI & $R^{2}$ & $I_{\mathrm{var}}$ & $\Phi_{\mathrm{traj}}$ & cont \\
    33	\midrule
    34	WAKE      & $58$  & $2.252$ & $[1.82, 2.86]$ & $0.956$ & $2.18\!\times\!10^{-5}$ & $0.0008$ & $0.943$ \\
    35	SLEEP\_N3 & $111$ & $3.250$ & $[2.44, 4.14]$ & $0.886$ & $1.01\!\times\!10^{-5}$ & $0.0055$ & $0.980$ \\
    36	PROPOFOL  & $246$ & $2.758$ & $[2.52, 3.09]$ & $0.931$ & $5.37\!\times\!10^{-6}$ & $0.0003$ & $0.877$ \\
    37	RECOVERY  & $58$  & $2.252$ & $[1.82, 2.86]$ & $0.956$ & $2.18\!\times\!10^{-5}$ & $0.0008$ & $0.943$ \\
    38	\bottomrule
    39	\end{tabular}
    40	\end{table}
    41	
    42	\begin{table}[ht]
    43	\centering
    44	\small
    45	\caption{Six drug/sleep signatures with published references.}
    46	\label{tab:six_signatures}
    47	\begin{tabular}{c l l c c l}
    48	\toprule
    49	\# & Signature & Reference & Predicted & Observed & Verdict \\
    50	\midrule
    51	1 & NREM-N3 var ratio (vs Wake) &
    52	   Sleep-EDFx W$\to$N3 ($n=24$)~\citep{SleepEDFx} &
    53	   $\approx 0.365$ & $0.463$ & $\checkmark$ \\
    54	2 & Propofol switching ratio &
    55	   OpenNeuro \texttt{ds005620} ($n=8$, $2.96{\times}$)~\citep{OpenNeuroDS005620} &
    56	   $\in[1.5, 5.0]$ & $1.83\times$ & $\checkmark$ \\
    57	3 & Propofol continuity drop &
    58	   EEG microstate~\citep{Brodbeck2012Microstates} &
    59	   $> 0.020$ & $+0.066$ & $\checkmark$ \\
    60	4 & Propofol $\Phi$ collapse (IIT) &
    61	   Tononi 2008~\citep{Tononi2008} &
    62	   ratio $< 0.50$ & $0.33\times$ & $\checkmark$ \\
    63	5 & Recovery reversibility &
    64	   clinical anaesthesia &
    65	   identical to wake & $0$ diff & $\checkmark$ \\
    66	6 & Wake cortical-avalanche $\alpha$ &
    67	   Sleep-EDFx $n=30$ CI~$[2.50, 2.53]$~\citep{BeggsPlenz2003,SleepEDFx} &
    68	   $\alpha\!\in\![1.5, 3.5]$, $R^{2}\!>\!0.85$ &
    69	   $2.252$ $[1.82, 2.86]$ $R^{2}\!=\!0.956$ &
    70	   $\checkmark$ \\
    71	\bottomrule
    72	\end{tabular}
    73	\end{table}
    74	
    75	All six signatures pass against their published-reference thresholds
    76	on the same deterministic substrate trajectory. The six signatures
    77	are not part of the dated 2026-04-18 P1--P18 preregistration; they
    78	were tested on a recurrent-layer architecture redesigned at v4 with
    79	biologically-motivated condition-specific stimulus models
    80	(\S\ref{sec:chain}; \texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}
    81	documents the v3$\to$v4 stimulus redesign). The mechanistic readings
    82	in \texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md} are not
    83	load-bearing for the headline claim. Single-seed disclosure:
    84	\S\ref{sec:limitations}~\ref{ssec:regime}.
    85	
    86	\subsection{Eighteen preregistered correspondences}\label{ssec:eighteen_prereg}
    87	
    88	\textbf{Tally.} $17/18$ at standard validation
    89	(\texttt{run\_preregistered\_validation.py}, $5$-seed cascade block
    90	plus state-reset protocol); $18/18$ after the $N\!=\!20$ deep-dive
    91	on the residual P4 (\texttt{demo\_p4\_cxp\_deep\_dive.py}, seed range
    92	$32000$--$32019$). \emph{No preregistered threshold has been modified.}
    93	
    94	\begin{table}[ht]
    95	\centering
    96	\small
    97	\caption{All eighteen preregistered correspondences, frozen 2026-04-18.}
    98	\label{tab:eighteen_prereg}
    99	\begin{tabular}{l l l l l}
   100	\toprule
   101	ID & Test & Threshold & Observed (2026-04-29) & Verdict \\
   102	\midrule
   103	P1  & Cascade $\alpha$ SOC range            & $\in [2.5, 3.5]$ & $2.958$ & $\checkmark$ \\
   104	P2  & $C$ main effect                        & $\geq +0.30$     & $+0.621$ & $\checkmark$ \\
   105	P3  & $|D{\times}C|$ (independence)          & $|\cdot| < 0.20$ & $-0.183$ ($N\!=\!5$) & $\checkmark$ \\
   106	\textbf{P4} & $C{\times}P$ synergy           & $\geq +0.10$     &
   107	   $+0.190$ \, CI $[+0.143, +0.239]$ ($N\!=\!20$) & $\checkmark$ \\
   108	P5  & $|E|$ main effect (null)               & $|\cdot| < 0.15$ & $+0.046$ & $\checkmark$ \\
   109	P6  & Real EEG $\alpha$                      & $\in [2.0, 3.0]$ & $2.513$ & $\checkmark$ \\
   110	P7  & W$\!\to\!$N3 variance ratio            & $< 0.70$         & $0.365$ & $\checkmark$ \\
   111	P8  & W$\!\to\!$N3 switching ratio           & $< 0.50$         & $0.058$ & $\checkmark$ \\
   112	P9  & Chess 5-fold CV                        & $\geq 70\%$      & $83.1\%$ & $\checkmark$ \\
   113	P10 & Chess null mapping                     & $\geq 50\%$      & $65.4\%$ & $\checkmark$ \\
   114	P11 & Chess random-label                     & $\in [15\%, 35\%]$ & $23.4\%$ & $\checkmark$ \\
   115	P12 & Chess goldilocks peak                  & $\in \{15, 25, 40, 60\}$ & $n=25$ & $\checkmark$ \\
   116	\textbf{P13} & Chess substrate lift (5-fold CV preregistered; LOO refinement, with reset) & $\geq +15$pp & $+40.6$pp (LOO) & $\checkmark$ \\
   117	P14 & Conv raw 5-fold CV                     & $\geq 75\%$      & $87.5\%$ & $\checkmark$ \\
   118	P15 & $|$conv lift$|$                        & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
   119	P16 & Conv null mapping                      & $\geq 50\%$      & $70.6\%$ & $\checkmark$ \\
   120	P17 & ARIA degree std (theorem)              & $= 0$            & $0.0000$ & $\checkmark$ \\
   121	P18 & HCP degree std                         & $> 2.0$          & $3.388$ & $\checkmark$ \\
   122	\bottomrule
   123	\end{tabular}
   124	\end{table}
   125	
   126	\textbf{Three predictions that flipped to PASS, with documented
   127	methodology refinement (no threshold change).}
   128	\begin{itemize}\itemsep=2pt
   129	\item P3 (D$\times$C interaction independence) was outside the band
   130	  at $N\!=\!3$ ($-0.231$) and inside the band at $N\!=\!5$ ($-0.183$).
   131	  Reading: consistent with an underpowered interaction estimate at
   132	  $N\!=\!3$ on a high-per-seed-variance interaction term.
   133	\item P4 (C$\times$P synergy) was below threshold at $N\!=\!3$
   134	  ($+0.044$) and at $N\!=\!5$ ($+0.039$); the $N\!=\!20$ deep-dive
   135	  (\S\ref{sec:stress}) gives $+0.190$ with $95\%$ CI
   136	  $[+0.143, +0.239]$, decisively above the $\geq +0.10$ floor.
   137	\item P13 (chess substrate lift): the 2026-04-18 preregistration
   138	  (\texttt{PAPER\_PREDICTIONS.md:115-120}) specified the estimator as
   139	  $5$-fold CV with threshold $\geq +15$pp at $n=25$. The 2026-04-29
   140	  validation strengthened the estimator to LOO with state reset, a
   141	  stricter test at the same threshold; the LOO lift was $+3.1$pp
   142	  without state reset on a state-drifted substrate, and $+40.6$pp
   143	  with \texttt{homeostatic\_reset(level=1.0)} between depth measurements
   144	  (\S\ref{sec:method}; \texttt{NON\_EQUILIBRIUM\_FINDING.md}). We
   145	  report this as a \emph{validation-protocol refinement on the
   146	  preregistered estimator}, not as preregistration revision.
   147	\end{itemize}
   148	
   149	\textbf{Headline verdict.} Eighteen preregistered correspondences
   150	all pass at preregistered thresholds, with two interaction tests
   151	requiring $N\!\geq\!5$ and one requiring $N\!=\!20$ for reliable
   152	detection of high-variance interaction terms, and one test
   153	requiring the documented state-reset protocol. The original $15/18$
   154	result was a methodology-limited tally, not a content failure.
   155	
   156	\subsection{Three-way \texorpdfstring{$\alpha$}{alpha} overlap}\label{ssec:alpha_overlap}
   157	
   158	The substrate's wake cascade-$\alpha$ confidence interval overlaps
   159	\emph{three independent reference ranges} simultaneously:
   160	
   161	\begin{table}[ht]
   162	\centering
   163	\small
   164	\caption{Three-way $\alpha$ overlap on the wake cascade-event power
   165	law.}
   166	\label{tab:alpha_overlap}
   167	\begin{tabular}{l c l c}
   168	\toprule
   169	Source & $\alpha$ & 95\% CI & $n$ \\
   170	\midrule
   171	ARIA cascade-pipeline baseline ($N=5$) & $2.958$  & inside $[2.5, 3.5]$ & 5 seeds \\
   172	Real EEG (Sleep-EDFx, $n=30$ subjects)~\citep{SleepEDFx} & $2.51$ & $[2.50, 2.53]$ & 30 \\
   173	ARIA prior cascade pipeline ($n=4$ subjects) & $2.85$ & $[2.73, 3.25]$ & per-subject \\
   174	\textbf{v4 WAKE consciousness chain} & $\mathbf{2.252}$ & $[\mathbf{1.82, 2.86}]$ & 58 events \\
   175	\bottomrule
   176	\end{tabular}
   177	\end{table}
   178	
   179	The v4 WAKE 95\% CI $[1.82, 2.86]$ contains the upper arm of the
   180	real Sleep-EDFx EEG CI $[2.50, 2.53]$, overlaps the ARIA prior
   181	cascade pipeline CI $[2.73, 3.25]$ on the interval $[2.73, 2.86]$,
   182	and lies inside the cortical-avalanche band
   183	$\alpha\!\in\![1.5, 3.5]$~\citep{BeggsPlenz2003}. The pairwise
   184	intersections (WAKE $\cap$ Sleep-EDFx, WAKE $\cap$ prior pipeline,
   185	WAKE $\cap$ cortical-avalanche band) are non-empty across three
   186	independent reference ranges.
   187	
   188	\textbf{Reading.} The substrate produces self-organised-critical
   189	cascade statistics matching the cortical-avalanche literature with
   190	no fitted parameter on neural data. The bounded-top-$K$ at
   191	$k=12$ is pinned to the substrate's average degree
   192	(Lemma~\ref{lem:600cell}); the $\Ph^{-2}$ shift in $\Cph$ is a
   193	stability clamp (\S\ref{ssec:cphi}); the AR(1) WAKE input has
   194	biological time-scale parameters but is not measurement-fitted to
   195	any specific subject (\S\ref{sec:chain}). Three-way overlap on the
   196	power-law exponent is the strongest single empirical anchor in the
   197	paper.
=====06_stress_tests=====
     1	% =====================================================================
     2	\section{Stress test: the C\texorpdfstring{$\times$}{x}P synergy at adequate
     3	         replication}\label{sec:stress}
     4	% =====================================================================
     5	
     6	This section is the C$\times$P interaction stress test. The original
     7	preregistered prediction was P4: $C\times P$ interaction
     8	$\Delta_{CP} \geq +0.10$ on cascade-$\alpha$. The 2026-04-20
     9	$N\!=\!3$ validation gave $+0.044$ — below the threshold — and the
    10	architectural claim ``C and P synergise on cascade-state stability''
    11	was walked back. Closing this gap without modifying the preregistered
    12	threshold required (a) re-evaluating the $N\!=\!3$ point estimate as
    13	consistent with an underpowered interaction estimate, (b) tracking
    14	the estimate's behaviour across $N$, and (c) bootstrapping a
    15	confidence interval on a fresh-seed $N\!=\!20$ sample. We did all
    16	three.
    17	
    18	\subsection{The factorial estimator}
    19	
    20	For the four ablation conditions $\{----, -C--, --P-, -CP-\}$
    21	(\S\ref{sec:chain}), the $C\times P$ interaction estimate is the
    22	standard $2\times 2$ factorial difference:
    23	\[
    24	\Delta_{CP}
    25	\;=\;\frac{(\alpha_{\!-CP\!-}+\alpha_{\!-\!-\!-\!-})
    26	        - (\alpha_{\!-C\!-\!-}+\alpha_{\!-\!-P\!-})}{2}.
    27	\]
    28	Per-seed paired estimates use the same formula on a single seed's
    29	four conditions.
    30	
    31	\subsection{The trend across \texorpdfstring{$N$}{N}}
    32	
    33	\begin{table}[ht]
    34	\centering
    35	\small
    36	\caption{$C\times P$ interaction estimate as a function of $N$.}
    37	\label{tab:cxp_trend}
    38	\begin{tabular}{r l r l l}
    39	\toprule
    40	$N$ & Seeds & Estimate $\Delta_{CP}$ & 95\% CI & Verdict vs $\geq +0.10$ \\
    41	\midrule
    42	$3$  & $30040$--$30042$ & $+0.044$ & --- & $\times$ original prereg \\
    43	$5$  & $30040$--$30044$ & $+0.039$ & --- & $\times$ this session re-run \\
    44	$10$ & $31000$--$31009$ & $+0.088$ & $[-0.002, +0.174]$ & borderline \\
    45	$\mathbf{20}$ & $\mathbf{32000\text{--}32019}$ & $\mathbf{+0.190}$
    46	       & $\mathbf{[+0.143, +0.239]}$ & $\checkmark$ decisively above \\
    47	\bottomrule
    48	\end{tabular}
    49	\end{table}
    50	
    51	The estimate remains small at $N\!=\!3$ and $N\!=\!5$
    52	($+0.044, +0.039$) and rises at $N\!=\!10$ and $N\!=\!20$
    53	($+0.088, +0.190$). Per-seed std at $N\!=\!10$ was $0.159$; at
    54	$N\!=\!20$ it dropped to $0.089$ — the $N\!=\!10$ sample landed on
    55	outliers; the $N\!=\!20$ sample reveals a clean narrow positive
    56	distribution.
    57	
    58	\subsection{The \texorpdfstring{$N\!=\!20$}{N=20} fresh-seed estimate}
    59	
    60	\textbf{Setup.} $4$ conditions $\times$ $20$ fresh seeds (range
    61	$32000$--$32019$, non-overlapping with original validation seeds in
    62	the $30000$s), $150$ epochs per run. All other ablation flags off
    63	($D, E$ held on). Bootstrap $n_{\mathrm{resamples}}\!=\!2000$,
    64	seed $42$. Wallclock $1706$\,s on a single CPU
    65	(\texttt{demo\_p4\_cxp\_deep\_dive.py}).
    66	
    67	\textbf{Per-condition means at \texorpdfstring{$N\!=\!20$}{N=20}.}
    68	
    69	\begin{table}[ht]
    70	\centering
    71	\small
    72	\caption{Per-condition mean $\alpha$ at $N=20$ fresh seeds.}
    73	\label{tab:cxp_means}
    74	\begin{tabular}{l r r r}
    75	\toprule
    76	condition & mean $\alpha$ & std & sem \\
    77	\midrule
    78	$----$ baseline    & $3.008$ & $0.090$ & $0.020$ \\
    79	$-C--$ (C off)     & $3.464$ & $0.097$ & $0.022$ \\
    80	$--P-$ (P off)     & $2.790$ & $0.086$ & $0.019$ \\
    81	$-CP-$ (both off)  & $3.628$ & $0.161$ & $0.036$ \\
    82	\bottomrule
    83	\end{tabular}
    84	\end{table}
    85	
    86	\textbf{Main effects at \texorpdfstring{$N\!=\!20$}{N=20}.}
    87	$C$ main effect $= +0.456$ (turning $C$ off raises $\alpha$);
    88	$P$ main effect $= -0.218$ (turning $P$ off lowers $\alpha$).
    89	
    90	\textbf{Interaction estimate.} Direct calculation from means:
    91	\[
    92	\Delta_{CP} \;=\; \frac{(3.628 + 3.008) - (3.464 + 2.790)}{2}
    93	            \;=\; +0.191.
    94	\]
    95	Bootstrap on the 20-seed sample (2000 resamples):
    96	\begin{itemize}\itemsep=1pt
    97	\item bootstrap mean $\Delta_{CP} = +0.190$;
    98	\item 95\% bootstrap CI $[+0.143, +0.239]$;
    99	\item $0/2000$ bootstrap resamples were at or below zero, reported as
   100	      $0.0000$;
   101	\item $0/2000$ bootstrap resamples were below the preregistered
   102	      $+0.10$ floor, reported as $0.0000$.
   103	\end{itemize}
   104	
   105	\textbf{Per-seed paired distribution.}
   106	$19/20$ seeds give a positive paired-interaction estimate (range
   107	$+0.055$ to $+0.322$); a single seed gives $-0.009$. No seed gives a
   108	strongly negative interaction.
   109	
   110	\subsection{Reading and disclosure}
   111	
   112	\textbf{The 95\% CI is entirely above the preregistered $+0.10$
   113	threshold} on a fresh-seed sample. $0/2000$ bootstrap resamples were
   114	at or below zero, reported as $0.0000$; $0/2000$ bootstrap resamples
   115	were below the preregistered $+0.10$ floor, reported as $0.0000$.
   116	
   117	\textbf{Architectural reading (substrate witness).} $C$ creates churn
   118	in \emph{which} vertices are uncrossed (frame rotation churns the
   119	uncrossed pool). $P$ promotes the high-pressure subset of the
   120	uncrossed pool to mini-emitters. The product is a non-additive
   121	novel-event-generation pathway: with both on, the uncrossed pool
   122	churns and $P$ amplifies new vertices entering the high-pressure
   123	region; with either off, the pathway collapses. The interaction
   124	$+0.19$ is comparable in magnitude to the $P$ main effect $-0.22$,
   125	so $C$ and $P$ are \emph{strongly coupled} cascade-state stabilisers
   126	on this substrate, not nearly-orthogonal ones. This reverses an
   127	architectural claim from the original 3-seed validation that held $C$
   128	and $P$ approximately orthogonal.
   129	
   130	\textbf{Disclosure: $N\!=\!20$ ordering.} The $N\!=\!20$ deep-dive
   131	was conducted \emph{after} the original $N\!=\!3$ failure
   132	(2026-04-29 vs 2026-04-20). The seed range $32000$--$32019$ was
   133	selected to be non-overlapping with the original $30000$s seeds.
   134	Two strengthening builds we have not delivered:
   135	(i) a second independent $N\!=\!20$ run at a different seed range
   136	(e.g.\ $33000$--$33019$), and
   137	(ii) an $N\!=\!50$ characterisation of the per-seed sample
   138	distribution. Both are recorded as open builds in
   139	\S\ref{sec:limitations}.
   140	
   141	\textbf{What this stress test does \emph{not} establish.}
   142	\begin{itemize}\itemsep=2pt
   143	\item It does not establish a Lyapunov function on the reduced flow.
   144	\item It does not establish that the substrate is uniquely selected by
   145	  $C\times P$ coupling among regular 4-polytopes.
   146	\item It does not establish an $\eta$-trajectory derivation; $\eta$
   147	  is treated as a condition-dependent constant in this paper.
   148	\end{itemize}
   149	The stress test is what its name says: a high-replication factorial
   150	test of one preregistered interaction prediction, on a fresh-seed
   151	sample, with bootstrap confidence intervals. The architectural reading
   152	is a \emph{description} of what $C$ and $P$ do on the substrate, not a
   153	theorem about why they do it.
   154	
   155	\subsection{Methodological contribution}
   156	
   157	We document, as a methodological contribution to preregistration
   158	practice, that interaction terms in cascade ablation matrices require
   159	$N\!\geq\!20$ fresh seeds for reliable detection when the
   160	interaction-to-main-effect ratio is below $0.5$. The original 3-seed
   161	preregistered validation gave estimates consistent with underpowered
   162	detection on both interaction tests (P3 and P4); both close at higher
   163	$N$ without threshold modification. For preregistration design more broadly:
   164	when preregistering an interaction effect on a system with unknown
   165	per-seed variance, allocate the seed count from a power-analysis
   166	assumption that the per-seed std could be as large as the interaction
   167	effect itself. Under that assumption, $N\!\geq\!20$ is the conservative
   168	minimum.
=====07_cross_domain=====
     1	% =====================================================================
     2	\section{Cross-domain selectivity}\label{sec:cross_domain}
     3	% =====================================================================
     4	
     5	This section reports three cross-domain witnesses. \S\ref{ssec:chess}
     6	gives the chess pattern-recognition lift. \S\ref{ssec:conv} gives the
     7	conversation neutrality result that confirms the lift is selective.
     8	\S\ref{ssec:hcp} gives the HCP brain-graph maximum-symmetry null.
     9	For each domain we report
    10	$A_{d} = \mathrm{Acc}_{\mathrm{sub}, d} - \mathrm{Acc}_{\mathrm{raw}, d}$
    11	or, in the HCP case,
    12	$Z_{m} = (m_{\mathrm{ARIA}} - \mu_{\mathrm{HCP}})/\sigma_{\mathrm{HCP}}$.
    13	Numbers are lifted verbatim from
    14	\texttt{docs/brain\_mapping/CROSS\_DOMAIN\_RESULTS.md}.
    15	
    16	\subsection{Chess pattern recognition (P9--P13)}\label{ssec:chess}
    17	
    18	\textbf{Setup.} $32$ chess positions across $4$ categories (tactical,
    19	positional, endgame, opening). Per-position $8$-dimensional V2
    20	features (material balance, king safety, pawn structure, centre
    21	control, piece activity, mobility, threat density, defensive
    22	structure), normalised by per-feature $L^{2}$ norms. Substrate
    23	routing: features injected as pressure into the $S^{7}$ observer
    24	frames; substrate run forward by $n_{\mathrm{ticks}}$; resulting
    25	vertex pattern used as classifier feature vector. Classifier:
    26	1-nearest-neighbour on cosine similarity, validated by $5$-fold CV
    27	or leave-one-out (LOO).
    28	
    29	\textbf{Critical methodological detail.} Between successive depth
    30	measurements the substrate is reset to canonical state via
    31	\texttt{mon.homeostatic\_reset(level=1.0)}. Without this, pressure-
    32	field state drifts toward equilibrium across $\sim 5$ evaluations
    33	and classification structure collapses to raw-feature baseline.
    34	
    35	\begin{table}[ht]
    36	\centering
    37	\small
    38	\caption{Chess substrate-routed depth sweep with state reset between
    39	measurements.}
    40	\label{tab:chess_depth}
    41	\begin{tabular}{r r}
    42	\toprule
    43	$n_{\mathrm{ticks}}$ & accuracy \\
    44	\midrule
    45	$5$    & $53.1\%$ \\
    46	$15$   & $65.6\%$ \\
    47	$\mathbf{25}$  & $\mathbf{93.8\%}$ ($\leftarrow$ peak) \\
    48	$40$   & $84.4\%$ \\
    49	$60$   & $84.4\%$ \\
    50	$100$  & $78.1\%$ \\
    51	\bottomrule
    52	\end{tabular}
    53	\end{table}
    54	
    55	\begin{table}[ht]
    56	\centering
    57	\small
    58	\caption{Chess preregistered tests (with reset, $n=25$ canonical
    59	depth).}
    60	\label{tab:chess_prereg}
    61	\begin{tabular}{l l l l l}
    62	\toprule
    63	ID & Test & Threshold & Observed & Verdict \\
    64	\midrule
    65	P9  & 5-fold CV (seeds 30200--30204)        & $\geq 70\%$ & $83.1\%$ & $\checkmark$ \\
    66	P10 & null perm. mapping (chess, 15 perms)$^{\dagger}$  & $\geq 50\%$ & $65.4\%$ & $\checkmark$ \\
    67	P11 & random-label baseline (20 trials)     & $\in[15\%, 35\%]$ & $23.4\%$ & $\checkmark$ \\
    68	P12 & goldilocks peak depth                 & $\in\{15,25,40,60\}$ & $n=25$ & $\checkmark$ \\
    69	\textbf{P13} & substrate lift, LOO refinement (with reset)$^{\ddagger}$ & $\geq +15$pp & $\mathbf{+40.6}$pp (LOO) & $\checkmark$ \\
    70	\bottomrule
    71	\end{tabular}
    72	\end{table}
    73	
    74	$^{\dagger}$ The 2026-04-18 preregistration P16 specified the null
    75	permutation test as ``$\geq 50\%$ on \emph{both} chess and
    76	conversation''; we present the chess and conversation null mappings
    77	separately as P10 (chess) and P16 (conversation) for table clarity.
    78	Both pass.
    79	
    80	$^{\ddagger}$ The 2026-04-18 preregistration P13 specified the chess
    81	substrate-lift estimator as $5$-fold CV at threshold $\geq +15$pp.
    82	The 2026-04-29 validation tightened the estimator to LOO with state
    83	reset; we report the LOO finding ($+40.6$pp) above as a stricter
    84	validation-protocol refinement at the unchanged $+15$pp threshold,
    85	not a preregistration revision.
    86	
    87	\textbf{Reading.} Substrate routing amplifies chess-position
    88	4-category classification from raw $53.1\%$ (just above $25\%$
    89	chance) to substrate-routed $93.8\%$ at canonical depth $n=25$.
    90	This is a $+40.6$pp lift on the LOO refinement; on the preregistered
    91	$5$-fold CV estimator the substrate-routed accuracy is $83.1\%$
    92	(P9), itself well above any reasonable raw-features baseline.
    93	The original 2026-04-20 validation reported the LOO lift at
    94	$+3.1$pp, a state-drift artefact closed by the reset protocol
    95	(\S\ref{sec:method}).
    96	
    97	\textbf{Permutation null decomposition.} The null permutation
    98	mapping (P10) randomises the feature$\to$frame assignment, so each
    99	feature is routed to a different $S^{7}$ frame than canonical. The
   100	substrate retains $65.4\%$ classification accuracy under random
   101	permutation — well above the $25\%$ chance level for $4$ categories.
   102	We read this as a substrate-witness decomposition:
   103	$\sim 65$pp of classification power is \emph{architectural} (it
   104	persists when feature$\to$frame assignment is randomised; it is the
   105	H$_4$-symmetric amplifier acting on whatever input lands in the
   106	frames), and the remaining $\sim 17$pp is the semantic-alignment
   107	bonus. We do not claim this decomposition is unique; it is a
   108	description of the observed accuracy stack.
   109	
   110	\subsection{Conversation neutrality (P14--P16)}\label{ssec:conv}
   111	
   112	\textbf{Setup.} $64$ utterances across $8$ dialogue-act categories.
   113	$8$-dimensional injection-row features per utterance. Identical
   114	substrate routing pipeline to chess.
   115	
   116	\begin{table}[ht]
   117	\centering
   118	\small
   119	\caption{Conversation preregistered tests.}
   120	\label{tab:conv_prereg}
   121	\begin{tabular}{l l l l l}
   122	\toprule
   123	ID & Test & Threshold & Observed & Verdict \\
   124	\midrule
   125	P14 & raw 5-fold CV (seeds 30220--30224)    & $\geq 75\%$ & $87.5\%$ & $\checkmark$ \\
   126	P15 & substrate lift                         & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
   127	P16 & null perm. mapping (15 perms)         & $\geq 50\%$ & $70.6\%$ & $\checkmark$ \\
   128	\bottomrule
   129	\end{tabular}
   130	\end{table}
   131	
   132	\textbf{Reading.} Conversation raw features at $87.5\%$ are already
   133	strongly discriminative (cf.\ chess raw $\sim 53\%$); the substrate
   134	lift is $-4.4$pp, well within the preregistered neutrality band
   135	$|\cdot|\!<\!10$pp. The substrate is correctly null on conversation.
   136	
   137	\textbf{Selective amplifier signature.} The pair (chess
   138	$+40.6$pp lift; conversation $-4.4$pp lift) is consistent with the
   139	selective-amplifier behaviour preregistered in 2026-04-18: in these
   140	two tasks, the architecture amplifies when raw features are ambiguous
   141	(chess raw $\sim 53\%$) and is approximately neutral when raw features
   142	are already saturated (conversation raw $87.5\%$). We do not claim
   143	this generalises to all classification tasks; cross-domain transfer
   144	to additional ambiguous-feature benchmarks is an open build
   145	(\S\ref{sec:limitations}).
   146	
   147	\subsection{HCP brain-graph maximum-symmetry null
   148	            (P17--P18)}\label{ssec:hcp}
   149	
   150	\textbf{Setup.} Reference cohort: Human Connectome Project (HCP)
   151	$n=1003$ subjects~\citep{VanEssen2013HCP}; preregistered tests on
   152	$n=100$ subjects for computational tractability, with full-cohort
   153	$n=1003$ descriptive statistics also reported. ICA-50 group-averaged
   154	connectivity matrix; thresholded at the same density as ARIA's
   155	vertex graph ($\rho=0.101$). Compare degree distribution and
   156	higher-order graph statistics. ARIA reference: $G_{V_{600}}$ with
   157	$\Lop$. By H$_4$ transitivity (Lemma~\ref{lem:600cell}) every vertex
   158	has identical local structure $\Rightarrow$ uniform degree $12$
   159	$\Rightarrow$ degree std $= 0$ as a theorem.
   160	
   161	\begin{table}[ht]
   162	\centering
   163	\small
   164	\caption{HCP comparison: preregistered $n=100$ test plus full-cohort
   165	$n=1003$ descriptive statistics.}
   166	\label{tab:hcp}
   167	\begin{tabular}{l r r r}
   168	\toprule
   169	Metric & ARIA & HCP $n=1003$ mean (sd) & $\sigma$ from HCP \\
   170	\midrule
   171	Degree std (preregistered, $n=100$ subset) & $0.000$ & $3.388$ ($> 2.0$) & --- \\
   172	Degree std (descriptive, $n=1003$)         & $0.000$ & $3.28\pm 0.28$ & $-11.58\sigma$ \\
   173	Participation ratio (descriptive)          & $68.54$ & $19.72\pm 0.61$ & $+79.78\sigma$ \\
   174	Clustering coefficient (descriptive)       & $0.455$ & $0.220$ & $+6.80\sigma$ \\
   175	\bottomrule
   176	\end{tabular}
   177	\end{table}
   178	
   179	\begin{itemize}\itemsep=2pt
   180	\item P17 (ARIA degree std, theorem): predicted $=0$, observed
   181	  $0.0000$, $\checkmark$.
   182	\item P18 (HCP ICA-50 degree std, $n=100$ density-matched):
   183	  predicted $> 2.0$, observed $3.388$, $\checkmark$. Zero of $1003$
   184	  HCP subjects have degree std below $2.0$.
   185	\end{itemize}
   186	
   187	\textbf{Reading (substrate witness).} ARIA's H$_4$-transitive
   188	structure is a deterministic group-theoretic null reference for
   189	cortical functional connectivity. Real cortex breaks the symmetry
   190	through hub-spoke functional specialisation; the $\sigma$-distances
   191	quantify the magnitude of biological symmetry-breaking with no
   192	fitted parameters. The $\sigma$-distances ($-11.58\sigma$ on degree
   193	homogeneity, $+79.78\sigma$ on participation ratio, $+6.80\sigma$ on
   194	clustering coefficient) are large on the ICA-50 pipeline at the
   195	density-matched threshold $\rho = 0.101$; cross-parcellation
   196	replication (Schaefer, Glasser) remains an open build.
   197	
   198	\textbf{Participation-ratio comparability.} ARIA's vertex graph has
   199	$120$ nodes; the HCP ICA-50 connectivity matrix has $50$ nodes. The
   200	participation-ratio statistic
   201	$\mathrm{PR}(G) = (\sum_{i} d_{i})^{2} / \sum_{i} d_{i}^{2}$ is
   202	node-count-dependent — its theoretical maximum is the node count of
   203	the graph. We report the raw $\mathrm{PR}$ values
   204	($\mathrm{ARIA}=68.54$ on a 120-node graph; $\mathrm{HCP}=19.72$ on a
   205	50-node graph) and the $\sigma$-distance against the HCP
   206	across-subject distribution, but the $+79.78\sigma$ value reflects
   207	both the architectural difference and the differing node counts. A
   208	node-count-normalised statistic
   209	$\mathrm{PR}/|V|$ gives $\mathrm{ARIA}=0.571$ vs $\mathrm{HCP}=0.394$,
   210	a smaller absolute gap; we keep the raw-PR comparison as headline
   211	because the HCP subject distribution and the across-subject
   212	$\sigma$ are computed in the same units, but flag the node-count
   213	caveat here.
   214	
   215	\textbf{What we do not claim.}
   216	\begin{itemize}\itemsep=2pt
   217	\item We do not claim cortex has ``drifted from an ideal polytope'';
   218	  the substrate is a useful a-priori null whose deviation from real
   219	  cortex is precisely measurable.
   220	\item We do not claim parcellation invariance: the $\sigma$-distances
   221	  are reported on ICA-50; alternative parcellations (Schaefer,
   222	  Glasser) would give different per-metric numbers but, on the
   223	  basis of the qualitative pattern that cortex is hub-concentrated
   224	  relative to ARIA's transitive null, we expect them to preserve the
   225	  signs. Verification across parcellations is an open build
   226	  (\S\ref{sec:limitations}).
   227	\end{itemize}
   228	
   229	\subsection{Cross-domain summary as a selective amplifier
   230	            \texorpdfstring{$+$}{+} maximum-symmetry null}
   231	
   232	\begin{table}[ht]
   233	\centering
   234	\small
   235	\caption{Cross-domain summary on a single substrate.}
   236	\label{tab:cross_domain_summary}
   237	\begin{tabular}{l r r r r r}
   238	\toprule
   239	Task & Raw & Substrate & Null perm. & Geom.\ floor & Sem.\ alignment \\
   240	\midrule
=====08_discussion=====
     1	% =====================================================================
     2	\section{Discussion}\label{sec:discussion}
     3	% =====================================================================
     4	
     5	This section reads the substrate-witness result against existing
     6	theories of consciousness, identifies what is novel here that is not
     7	a re-statement of an earlier theory, and proposes a non-load-bearing
     8	ACT bridge to the companion adaptive-closure-transport
     9	preprint~\citep{SmartAdaptiveClosureTransport2026}. We do not claim a
    10	selection theorem, we do not claim a Lyapunov derivation, and we do
    11	not claim the recurrent layer ``is'' consciousness.
    12	
    13	\subsection{What is novel in this work}
    14	
    15	Three things are claimed novel as a substrate witness:
    16	\begin{enumerate}\itemsep=2pt
    17	\item \textbf{A geometry-fixed substrate that is consistent with
    18	  real-cortex EEG signatures without fitted shape parameters on neural
    19	  data.} The 600-cell + H$_4$ symmetry is fixed by group theory once
    20	  the substrate is chosen; cascade-$\alpha$ matches Sleep-EDFx within
    21	  preregistered tolerance with pairwise CI overlap on three reference
    22	  ranges; six drug/sleep signatures pass at published-reference
    23	  thresholds on a single deterministic substrate. We are not aware of
    24	  a prior geometric substrate that has been tested against this many
    25	  preregistered cortical correspondences from a graph fixed by group
    26	  theory; we cannot rule out that such a model exists.
    27	\item \textbf{The strong-coupling architectural finding.} $C$ and $P$
    28	  are strongly coupled cascade-state stabilisers, not
    29	  nearly-orthogonal ones. The $C\!\times\!P$ interaction
    30	  ($+0.190$, $95\%$ CI $[+0.143, +0.239]$ at $N\!=\!20$) is comparable
    31	  in magnitude to the $P$ main effect ($-0.218$). This was hidden by
    32	  underpowered ablation and emerged only at $N\!\geq\!20$ — a
    33	  substantive correction to the architectural reading from the
    34	  original 3-seed validation.
    35	\item \textbf{The 18/18 preregistered correspondences with no
    36	  threshold modification.} Every prediction in the preregistered set
    37	  passes at the preregistered thresholds. The two interaction tests
    38	  (P3, P4) required $N\!\geq\!5$ and $N\!\geq\!20$ respectively, and
    39	  one test (P13) required the documented state-reset protocol. We
    40	  report this transparently as methodology refinement, not as
    41	  threshold change.
    42	\end{enumerate}
    43	
    44	\subsection{Comparison to existing theories of consciousness}
    45	
    46	\textbf{vs IIT.}~\citep{Tononi2008,BalduzziTononi2008} ARIA produces
    47	IIT-direction-correct $\Phi$ collapse on propofol ($0.33\!\times$
    48	wake). The H$_4$-equivariance argument
    49	(\S\ref{sec:chain}) makes $\Phi\to 0$ when dynamics are
    50	group-symmetric, and $\Phi > 0$ only when dynamics break symmetry.
    51	ARIA does not implement the full IIT axioms (cause-effect repertoires,
    52	exclusion postulate, integration-over-partitions); it reproduces the
    53	observable consequence on the propofol--wake state contrast. This is
    54	a consistency-of-direction result, not a discharge of IIT.
    55	
    56	\textbf{vs Global Workspace Theory.}~\citep{Baars1988GWT,Dehaene2014ConsciousAndBrain}
    57	The $S^{7}$ context-rotation mechanism (\S\ref{sec:chain}) is
    58	functionally analogous to a workspace with rotating attentional
    59	selection; the active observer frame plays the role of a temporary
    60	in-workspace subset of features. ARIA does not commit to the GWT
    61	broadcast/access distinction at the architectural level; the
    62	analogy is descriptive.
    63	
    64	\textbf{vs Predictive Processing.}~\citep{FristonFreeEnergy2010,ClarkPP2013}
    65	ARIA does not implement prediction-error minimisation or hierarchical
    66	generative models.
    67	The recurrent self-model layer ($\eta\!=\!0.20$) provides top-down
    68	modulation of the substrate response by cosine direction alignment
    69	with the prior phenomenal snapshot, not by learned prediction errors.
    70	Predictive-processing-style refinements (e.g.\ $\eta$ as an adaptive
    71	learning rate over a prediction-error norm) are an open build, not
    72	delivered here.
    73	
    74	\textbf{vs neural mass models.} ARIA operates at the
    75	architectural-algorithmic level; it does not specify which neural
    76	circuits implement context rotation or partial emission. The 600-cell
    77	substrate is proposed as an abstract description of the criticality-
    78	maintaining structure of cortex, not as a circuit model.
    79	
    80	\subsection{The non-load-bearing ACT bridge}\label{ssec:act_bridge}
    81	
    82	The companion adaptive-closure-transport
    83	preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
    84	4-tuple bridge
    85	$(M, L_{M}, W, R_{\mathrm{hom}})$ — substrate $M$, response operator
    86	$L_{M}$, learnable Hebbian-like field $W$, and a homeostatic
    87	regulariser $R_{\mathrm{hom}}$. We propose the dictionary
    88	$D_{\mathrm{ACT}}$:
    89	\[
    90	D_{\mathrm{ACT}}\colon (M, L_{M}, W, R_{\mathrm{hom}})
    91	\;\longmapsto\;
    92	(\Rsixhundred,\ \Cph,\ \text{cascade pressure field}\ W_{\mathrm{p}},
    93	   \ \texttt{homeostatic\_reset}).
    94	\]
    95	\textbf{This bridge is non-load-bearing for the present paper.} It is
    96	included as a route-K (alternative-route) reading; the substrate-
    97	witness claims (six signatures, $18/18$, chess $+40.6$pp,
    98	HCP $\sigma$-distances) do not require any of the ACT theorems.
    99	
   100	\textbf{What ACT would have to deliver to make this load-bearing.}
   101	The companion preprint identifies four open builds, each of which is
   102	deferred:
   103	\begin{itemize}\itemsep=2pt
   104	\item A Lyapunov function $V(W)$ on the reduced flow whose
   105	  monotonicity proves selection — not delivered.
   106	\item An edge-space decomposition of $\mathbb{R}^{E_{M}}$ under the
   107	  Hodge edge Laplacian $L_{\mathrm{edge}} = \delta_{2}\delta_{2}^{\mathsf T} +
   108	  \delta_{1}^{\mathsf T}\delta_{1}$ — not delivered.
   109	\item A formal $2I$-equivariance audit of the closure operator
   110	  family — not delivered.
   111	\item A full reduced-flow convergence theorem on
   112	  $W$-trajectories — not delivered.
   113	\end{itemize}
   114	Until these are delivered, ARIA is positioned as the empirical
   115	\emph{substrate witness} for the family that ACT names; ACT is not the
   116	selection-theorem witness for ARIA. The companion kernel
   117	document~\citep{SmartAriaClosureKernel2026} discusses the same $\Cph$
   118	in a passive-regime witness via the $B\to K^{*}\mu^{+}\mu^{-}$ flavour
   119	anomaly~\citep{SmartBAnomaly2026}; that line shares operator-level
   120	infrastructure with this paper, but does not transfer empirical
   121	support for ARIA.
   122	
   123	\subsection{The strong-coupling reading for cortical architecture}
   124	
   125	Real cortical criticality is maintained by multiple parallel
   126	mechanisms: E/I balance, neuromodulation (acetylcholine, noradrenaline),
   127	homeostatic plasticity, gain control. The naive expectation — and the
   128	one we held until the $N\!=\!20$ deep-dive — is that these are mostly
   129	orthogonal, so losing one removes only its own main effect. The
   130	$N\!=\!20$ result reverses this on the substrate: $C$ and $P$ are
   131	strongly coupled. Disabling one cascades into losing the synergistic
   132	contribution of the other.
   133	
   134	This matches clinical observations: anaesthesia (which targets
   135	GABAergic transmission) and seizure (which targets E/I balance)
   136	produce widespread network-level dysfunction beyond their direct
   137	targets — exactly what strong synergy predicts. We position this as
   138	\emph{a hypothesis the substrate witness raises}, not as a proof.
   139	The bridge from cascade-mechanism interaction on $\Rsixhundred$ to
   140	real-cortex pharmacological coupling is a step we do not take in
   141	this paper.
   142	
   143	\subsection{Methodological contributions}
   144	
   145	Two methodological items are worth recording outside the headline:
   146	\begin{enumerate}\itemsep=2pt
   147	\item \textbf{$N\!\geq\!20$ for high-variance interaction terms.}
   148	  Allocation discipline for preregistration: when preregistering an
   149	  interaction effect on a system with unknown per-seed variance,
   150	  budget for $N\!\geq\!20$ from the start. The original 3-seed plan
   151	  was the source of two underpowered-interaction estimates in this work.
   152	\item \textbf{State-reset protocol on non-stationary substrates.}
   153	  ARIA's substrate is a non-stationary dynamical system; the
   154	  pressure field equilibrates within $\sim 5$ successive evaluations.
   155	  Any multi-trial benchmark must specify a state-reset protocol or
   156	  document the drift. Generalisable lesson: \emph{published
   157	  cross-domain benchmarks on non-stationary substrates should report
   158	  an explicit reset/equilibration discipline}, not just seed.
   159	\end{enumerate}
   160	
   161	\subsection{The substrate as a maximum-symmetry connectivity null}
   162	
   163	The HCP comparison (\S\ref{ssec:hcp}) places ARIA as a principled
   164	deterministic null reference for cortical functional connectivity.
   165	Real cortex breaks the symmetry through hub-spoke functional
   166	specialisation; the $\sigma$-distances from ARIA quantify the
   167	magnitude of biological symmetry-breaking with no fitted parameters.
   168	
   169	This is a methodological contribution to comparative connectomics.
   170	Stochastic nulls (Erd\H{o}s--R\'enyi, configuration model,
   171	edge-randomised graphs) compare cortex to a random graph with matched
   172	density. ARIA is a different kind of null: a deterministic
   173	group-theoretic graph with theorem-level statements of structure
   174	(degree std $=\!0$ by transitivity, eigenvalue spectrum
   175	$\{0, 3, 4\Ph, 6\Ph, 12{-}4\Ph, 12{-}6\Ph, 9, 12\}$ by character
   176	theory). Both null kinds are useful; ARIA gives a specific,
   177	reproducible, group-theoretic baseline that cortex deviates from in
   178	quantifiable $\sigma$-units.
   179	
   180	\subsection{Open questions raised by the substrate witness}
   181	
   182	\begin{itemize}\itemsep=2pt
   183	\item Do the six drug/sleep signatures replicate across $10$--$20$
   184	  cross-seed runs of the recurrent layer? (Single-seed disclosure;
   185	  see \S\ref{sec:limitations}.)
   186	\item Do alternative regular 4-polytopes ($24$-cell, $120$-cell)
   187	  reproduce comparable signature sets, or is the $600$-cell
   188	  distinguished?
   189	\item Does the strong-coupling reading ($C\!\times\!P$) survive an
   190	  independent fresh-seed $N\!=\!20$ replication at a different seed
   191	  range?
   192	\item Does the substrate's amplifier behaviour transfer to other
   193	  ambiguous-feature classification tasks beyond chess (e.g.\ visual
   194	  pattern, audio classification)?
   195	\item Does the Sleep-EDFx three-way CI overlap survive on a different
   196	  EEG cohort (TUH, NHM)?
   197	\end{itemize}
   198	We list these as open questions raised by the witness, not as gaps
   199	in the witness itself.
=====09_limitations=====
     1	% =====================================================================
     2	\section{Limitations and hostile-review guard matrix}\label{sec:limitations}
     3	% =====================================================================
     4	
     5	This section enumerates limitations transparently, organised as a
     6	five-move guard matrix following the b-anomaly preprint
     7	template~\citep{SmartBAnomaly2026}: regime, post-hoc, interpretation,
     8	test/claim, state-drift. For each guard we record
     9	$G\colon \mathrm{risk} \to (\mathrm{disclosure}, \mathrm{evidence},
    10	\mathrm{strengthening\ build})$.
    11	
    12	\subsection{Regime}\label{ssec:regime}
    13	
    14	\textbf{Single substrate (the 600-cell).} We have not tested whether
    15	other regular 4-polytopes ($24$-cell, $120$-cell) would produce
    16	comparable correspondences. The 600-cell was chosen because its
    17	H$_4$ Coxeter cascade structure aligns with the empirical signatures
    18	that motivated this paper, not from an a-priori derivation.
    19	\emph{Disclosure:} substrate-witness scope, no uniqueness claim
    20	(\S\ref{sec:intro}). \emph{Evidence:} empirical correspondences hold
    21	on $\Rsixhundred$. \emph{Strengthening build:} formal ablation against
    22	$\{24\text{-cell}, 120\text{-cell}\}$ on the same six-signature
    23	battery and the eighteen preregistered tests, with thresholds
    24	preserved.
    25	
    26	\textbf{Single-seed determinism on the recurrent layer.} The v4
    27	six-signature results in~\S\ref{ssec:six_signatures} are reported on
    28	a single deterministic trajectory at seed $42$. Empirical CIs across
    29	$10$--$20$ cross-seed runs would strengthen the per-signature claims
    30	beyond the single-trajectory bootstrap of $58$ events that gives the
    31	WAKE 95\% CI $[1.82, 2.86]$. \emph{Disclosure:} explicitly single-seed
    32	in~\S\ref{sec:method} and~\S\ref{ssec:six_signatures}.
    33	\emph{Evidence:} bootstrap CI on the wake 58 events, plus three-way
    34	overlap with two independent reference $\alpha$ ranges.
    35	\emph{Strengthening build:} 10--20 cross-seed runs of
    36	\texttt{demo\_drug\_sleep\_v4.py}, with per-signature bootstrap CIs.
    37	
    38	\textbf{Stylised stimulus models on the recurrent layer.} The v4
    39	stimulus models for WAKE (AR(1) noise + tonic shell + attention
    40	episodes), SLEEP\_N3 (slow oscillation + spindles + K-complexes),
    41	and PROPOFOL (low-amplitude tonic noise) are biologically motivated
    42	but abstract: a single shell anchor for tonic coherence, fixed
    43	$40$-tick period for slow-wave drive, etc. Real spatial structure of
    44	cortical input is much richer. \emph{Disclosure:}~\S\ref{sec:chain}
    45	``deliberately structural rather than measurement-fitted''.
    46	\emph{Evidence:} models match published biological time scales but
    47	are not tuned to specific signatures. \emph{Strengthening build:}
    48	replication on stimulus models derived from anatomically-grounded
    49	input statistics (e.g.\ retinotopic, tonotopic).
    50	
    51	\subsection{Post-hoc}\label{ssec:posthoc}
    52	
    53	\textbf{The 600-cell choice is post-hoc justified by empirical
    54	observables.} While the construction of $\Rsixhundred$ is theorem-
    55	level rigorous (H$_4$ Coxeter group theory), the choice of \emph{this}
    56	polytope as the consciousness-substrate instance is motivated by the
    57	correspondences observed, not by an a-priori biological argument.
    58	\emph{Disclosure:}~\S\ref{sec:intro}, ``substrate witness, not
    59	derivation; not a uniqueness claim''. \emph{Evidence:} the eighteen
    60	preregistered correspondences plus six signatures; the H$_4$
    61	transitivity theorem ($P17$). \emph{Strengthening build:} comparison
    62	with the $24$-cell and $120$-cell on the same signatures; formal
    63	ACT-selection-theorem witness via the bridge of~\S\ref{ssec:act_bridge}
    64	(deferred).
    65	
    66	\textbf{Cascade decomposition is one of several possible
    67	decompositions of H$_4$.} We use the $\sigma$-orbit projector basis
    68	because it is machine-precise and biologically informative, but other
    69	bases (character-theoretic, Galois-twin) give the same physical
    70	predictions through different intermediate variables. \emph{Disclosure:}
    71	\S\ref{ssec:cascade} acknowledges non-uniqueness of decomposition.
    72	\emph{Evidence:} block-diagonalisation at $<10^{-15}$ cross-block
    73	norm. \emph{Strengthening build:} catalogue and equivalence-prove the
    74	admissible decompositions.
    75	
    76	\textbf{$\Ph^{-2}$ floor not derived.} The shifted-Laplacian floor
    77	$\Ph^{-2}\!\approx\!0.382$ is a stability clamp making $\Cph$
    78	strictly positive definite (\S\ref{ssec:cphi}); it is not derived
    79	from a closure functional or symmetry argument. \emph{Disclosure:}
    80	\S\ref{ssec:cphi} marks this as a design-level choice; the companion
    81	kernel doc~\citep{SmartAriaClosureKernel2026} explicitly does not
    82	derive it. \emph{Evidence:} the same operator (with the same shift)
    83	serves as the basis for the b-anomaly passive-regime
    84	witness~\citep{SmartBAnomaly2026}. \emph{Strengthening build:}
    85	derive the $\Ph^{-2}$ shift as the unique stability clamp under a
    86	named regularity criterion.
    87	
    88	\subsection{Interpretation}\label{ssec:interpretation}
    89	
    90	\textbf{The recurrent layer is a method, not a metaphysics claim.}
    91	We do not claim the recurrent self-model layer ``is'' consciousness;
    92	we claim quantitative consistency with six published biological
    93	signatures on a deterministic trajectory. \emph{Disclosure:}
    94	\S\ref{sec:intro}, \S\ref{sec:chain} (``method, not metaphysics'').
    95	\emph{Evidence:} six signatures vs published thresholds.
    96	\emph{Strengthening build:} cross-seed CIs (\S\ref{ssec:regime}); a
    97	formal account of which substrate observables map to which phenomenal
    98	contents (the bind\_phenomenal\_field channels) is not delivered.
    99	
   100	\textbf{$\Phi$ is an IIT-style direction-of-effect proxy, not a full
   101	IIT discharge.} \emph{Disclosure:}~\S\ref{sec:chain} explicitly.
   102	\emph{Evidence:} propofol $\Phi$ collapse to $0.33\!\times$ wake
   103	matches IIT direction. \emph{Strengthening build:} a
   104	\texttt{phi\_iit\_full} implementation following Balduzzi--Tononi
   105	2008~\citep{BalduzziTononi2008} on the substrate; not delivered.
   106	
   107	\textbf{HCP $\sigma$-distances are descriptive, not normative.} We
   108	do not claim ``cortex has drifted from an ideal polytope''; we
   109	quantify the distance between cortex and the deterministic H$_4$ null.
   110	\emph{Disclosure:}~\S\ref{ssec:hcp} explicitly. \emph{Evidence:}
   111	$\sigma$-distances on three independent metrics. \emph{Strengthening
   112	build:} cross-parcellation replication (Schaefer, Glasser).
   113	
   114	\subsection{Test/claim}\label{ssec:testclaim}
   115	
   116	\textbf{Two preregistered interaction tests required higher $N$
   117	than originally allocated.} P3 closes at $N\!=\!5$; P4 closes only at
   118	$N\!=\!20$. We document this transparently as a Type II
   119	methodology issue, not a threshold change. \emph{Disclosure:}
   120	\S\ref{sec:method}, \S\ref{sec:results}, \S\ref{sec:stress}.
   121	\emph{Evidence:} bootstrap CI fully above the $+0.10$ floor; per-seed
   122	distribution narrow at $N\!=\!20$ ($\mathrm{std}=0.089$);
   123	$19/20$ seeds positive. \emph{Strengthening build:} a second
   124	$N\!=\!20$ run at a different seed range (e.g.\ $33000$--$33019$);
   125	an $N\!=\!50$ characterisation of the per-seed distribution.
   126	
   127	\textbf{The original 2026-04-20 walks-back are reversed without
   128	threshold modification.} The reversals (P3, P4, P13) are documented
   129	in
   130	\texttt{docs/brain\_mapping/VALIDATION\_RESULTS\_2026-04-29.md} with
   131	the original failure values, the methodology refinement, and the
   132	post-refinement values. \emph{Disclosure:} this paper carries those
   133	disclosures verbatim. \emph{Evidence:} 2026-04-20 vs 2026-04-29 side-
   134	by-side results table. \emph{Strengthening build:} the strengthening
   135	builds for P3/P4/P13 above; no further claim is needed.
   136	
   137	\textbf{Bayesian and full-IIT inference not performed.} All intervals
   138	are frequentist (bootstrap CIs); $\Phi$ is the direction-of-effect
   139	proxy, not the Balduzzi--Tononi 2008 algorithm. \emph{Disclosure:}
   140	this section. \emph{Strengthening build:} Bayesian posterior on
   141	$\Delta_{CP}$; full-IIT computation on the $S^{4}\!\to\!2^{4}$
   142	substrate state space. The latter is computationally heavy and is
   143	deferred.
   144	
   145	\subsection{State-drift / out-of-scope}\label{ssec:scope}
   146	
   147	\textbf{Single condition-dependent parameter $\eta$ is not derived
   148	as a learned variable.} $\eta\in\{0, 0.05, 0.20\}$ across PROPOFOL,
   149	SLEEP\_N3, and WAKE/RECOVERY is a condition-dependent constant in
   150	this paper, not a learned trajectory. A predictive-processing
   151	extension where $\eta$ adapts on an error norm is an open build.
   152	
   153	\textbf{No deuteron / hadron / RH / capstone material is loaded into
   154	this paper.} The companion programme (cascade-derivation, capstone
   155	coalgebra, RH formal) shares operator-level infrastructure but is not
   156	load-bearing here. Deliberately out of scope.
   157	
   158	\textbf{Out-of-scope items NOT delivered (correctly).}
   159	\begin{itemize}\itemsep=2pt
   160	\item Aria-chess active-regime companion analysis on chess move-by-move
   161	  trajectories (this paper covers static positions only).
   162	\item Edge-space decomposition of $\mathbb{R}^{E_{M}}$ under
   163	  $2I$-equivariance — open build of the ACT companion paper.
   164	\item Lyapunov derivation $V(W)$ from a closure functional
   165	  $\mathcal{F}$ — open build of the ACT companion paper.
   166	\item Selection theorem for $\Rsixhundred$ over alternative regular
   167	  4-polytopes — see~\S\ref{ssec:regime}.
   168	\item Cross-cohort EEG (TUH, NHM, OpenNeuro non-propofol) replication
   169	  of the six signatures.
   170	\item Cross-parcellation replication of the HCP $\sigma$-distances
   171	  (Schaefer, Glasser, etc.).
   172	\item Bayesian posterior on the C$\times$P interaction.
   173	\end{itemize}
   174	
   175	\subsection{The honest verdict}
   176	
   177	The result is a substrate witness: a geometry-fixed substrate, with
   178	no shape parameters tuned to any neural dataset, is consistent with
   179	eighteen preregistered correspondences and six independent drug/sleep
   180	EEG signatures, with all original gaps closed by methodology
   181	refinement and without modifying any preregistered threshold. We do
   182	not claim the substrate \emph{is} consciousness. We do not claim a
   183	selection theorem on the ACT bridge. We do not claim uniqueness for
   184	$\Rsixhundred$ among regular 4-polytopes. The strengthening builds
   185	for these stronger claims are listed above and remain open.

exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex' | sed -n '1,260p'
printf '\\n---03---\\n'
nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex' | sed -n '1,260p'
printf '\\n---04---\\n'
nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex' | sed -n '1,260p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 305ms:
     1	% =====================================================================
     2	\section{Methods and provenance}\label{sec:method}
     3	% =====================================================================
     4	
     5	This section is a provenance ledger. It records, for each empirical
     6	claim downstream, the dataset, the preregistration date and document,
     7	the validation script, the seed range, the threshold, and the
     8	wallclock — the minimal information a hostile reviewer needs to
     9	reproduce or refute the claim.
    10	
    11	\subsection{Preregistration discipline}
    12	
    13	\textbf{Frozen 2026-04-18.} Eighteen quantitative predictions
    14	(P1--P18) were locked on 2026-04-18 in
    15	\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md} before any validation
    16	run. Each prediction has (i) a specific numerical claim, (ii) a
    17	falsifiable threshold, (iii) the validation test (script + seed range),
    18	and (iv) a rationale identifying what would falsify it.
    19	
    20	\textbf{Frozen 2026-04-24.} Two later batteries — H$_4$ fingerprint
    21	predictions and rung observables — were preregistered on 2026-04-24
    22	in \texttt{docs/brain\_mapping/PREREG\_H4\_FINGERPRINT.md} and
    23	\texttt{docs/brain\_mapping/PREREG\_RUNG\_OBSERVABLES.md}. \emph{We do
    24	not include those batteries in the headline 18/18 tally.} They are
    25	listed as future strengthening builds in~\S\ref{sec:limitations}.
    26	
    27	\textbf{Six EEG signatures (set B).} The drug/sleep signatures on the
    28	recurrent layer (\texttt{demo\_drug\_sleep\_v4.py}) test six
    29	independent published biological signatures (NREM-N3 variance ratio,
    30	propofol switching ratio, propofol continuity drop, propofol $\Phi$
    31	collapse, recovery reversibility, wake cascade-$\alpha$). They are
    32	not part of the P1--P18 preregistration; they are reported as a
    33	companion validation set on the recurrent layer.
    34	
    35	\textbf{No threshold has been modified post-hoc.} Where the original
    36	2026-04-20 validation reported failures (P3, P4, P13), the documented
    37	methodological refinements were
    38	(a)~increasing $N$ from $3$ to $5$ for cascade interaction terms,
    39	(b)~adding a $N\!=\!20$ deep-dive for the highest-variance interaction
    40	(P4, C$\times$P), and
    41	(c)~wiring \texttt{homeostatic\_reset(level=1.0)} between depth-sweep
    42	measurements for the chess LOO test (P13). None of these touched a
    43	preregistered threshold.
    44	
    45	\subsection{Provenance ledger}
    46	
    47	We write the provenance map as $\Pi\colon\{\text{claim id}\}
    48	\to (\text{script}, \text{seed range}, \text{dataset/source},
    49	\text{threshold}, \text{result})$.
    50	
    51	\begin{table}[ht]
    52	\centering
    53	\small
    54	\caption{Provenance ledger for the headline empirical claims.}
    55	\label{tab:provenance}
    56	\begin{tabular}{l l l l l}
    57	\toprule
    58	Claim & Script & Seed range & Dataset / source & Threshold \\
    59	\midrule
    60	P1 ($\alpha$ SOC band) & \texttt{run\_preregistered\_validation.py} & 30000--30004 & this paper & $\alpha\in[2.5, 3.5]$ \\
    61	P2 ($C$ main) & same & 30010--30014 & this paper & $\geq +0.30$ \\
    62	P3 ($|D{\times}C|$) & same & 30020--30024 & this paper & $|\cdot| < 0.20$ \\
    63	\textbf{P4 ($C{\times}P$)} & \texttt{demo\_p4\_cxp\_deep\_dive.py} & 32000--32019 & this paper & $\geq +0.10$ \\
    64	P5 ($|E|$) & \texttt{run\_preregistered\_validation.py} & 30030--30034 & this paper & $|\cdot| < 0.15$ \\
    65	P6 (real EEG $\alpha$) & same & 30100 & Sleep-EDFx~\citep{SleepEDFx} & $\alpha\in[2.0, 3.0]$ \\
    66	P7 ($W{\to}N3$ var) & same & deterministic & Sleep-EDFx ($n=24$) & $<0.70$ \\
    67	P8 ($W{\to}N3$ switch) & same & deterministic & Sleep-EDFx ($n=24$) & $<0.50$ \\
    68	P9 (chess 5-fold) & same & 30200--30204 & 32 positions, 4 cat. & $\geq 70\%$ \\
    69	P10 (chess null) & \texttt{run\_chess\_robustness.py} & 30210 & same & $\geq 50\%$ \\
    70	P11 (chess random-label) & same & 30210+ & same & $\in [15\%, 35\%]$ \\
    71	P12 (goldilocks) & \texttt{run\_preregistered\_validation.py} & with reset & same & $n\in\{15,25,40,60\}$ \\
    72	\textbf{P13 (chess sub.\ lift)} & same & with reset & same (LOO refinement) & $\geq +15$pp \\
    73	P14 (conv 5-fold) & same & 30220--30224 & 64 utt., 8 cat. & $\geq 75\%$ \\
    74	P15 ($|$conv lift$|$) & same & same & same & $|\cdot| < 10$pp \\
    75	P16 (conv null) & \texttt{run\_conversation\_robustness.py} & 30210 & same & $\geq 50\%$ \\
    76	P17 (ARIA deg std) & substrate construction & deterministic & H$_4$ theorem & $=0$ \\
    77	P18 (HCP deg std) & \texttt{run\_hcp\_validation.py} & deterministic & HCP S1200~\citep{VanEssen2013HCP} & $> 2.0$ \\
    78	\midrule
    79	Sig 1--6 (drug/sleep) & \texttt{demo\_drug\_sleep\_v4.py} & seed 42 & published biological & per-signature \\
    80	\bottomrule
    81	\end{tabular}
    82	\end{table}
    83	
    84	\subsection{Datasets and DOIs}
    85	
    86	\textbf{Sleep-EDFx (PhysioNet).} Public polysomnography
    87	recordings~\citep{SleepEDFx,PhysioNet2000}; $n=30$ subjects used for
    88	the cortical-avalanche $\alpha$ baseline; $n=24$ subjects used for
    89	the wake$\to$N3 variance and switching ratios. Cortical-avalanche
    90	fitting follows the Beggs--Plenz log-CCDF
    91	methodology~\citep{BeggsPlenz2003}.
    92	
    93	\textbf{OpenNeuro \texttt{ds005620}.} Propofol-induced loss of
    94	consciousness EEG, $n=8$~\citep{OpenNeuroDS005620},
    95	DOI \texttt{10.18112/openneuro.ds005620.v1.0.0}. Used as the
    96	empirical reference for the propofol switching ratio
    97	($2.96\!\times$ wake) in Sig~2.
    98	
    99	\textbf{OpenNeuro \texttt{ds004902}.} DMT-induced altered states
   100	EEG~\citep{OpenNeuroDS004902},
   101	DOI \texttt{10.18112/openneuro.ds004902.v1.0.8}. Background
   102	psychedelic-state reference; not load-bearing for the headline tally.
   103	
   104	\textbf{Zenodo \texttt{3992359}.} DMT EEG public
   105	release~\citep{ZenodoDMT3992359},
   106	DOI \texttt{10.5281/zenodo.3992359}. Same status as above.
   107	
   108	\textbf{HCP S1200.} Human Connectome Project
   109	S1200~\citep{VanEssen2013HCP}, ICA-50 group-averaged connectivity
   110	matrix. The preregistered test (P18) was on $n=100$ subjects for
   111	computational tractability; full-cohort $n=1003$ statistics
   112	(degree std, participation ratio, clustering coefficient $\sigma$-
   113	distances) are reported as descriptive statistics on top of the
   114	preregistered test.
   115	
   116	\textbf{Microstate baseline (qualifier).} The continuity-drop
   117	signature (Sig~3) follows the EEG microstate methodology lineage of
   118	Brodbeck et al.~\citep{Brodbeck2012Microstates} on wake/NREM
   119	microstates. Brodbeck et al.\ is not a propofol-specific paper; we
   120	use it for the underlying microstate-fragmentation methodology, not
   121	as a propofol reference. A propofol-specific microstate citation
   122	would tighten this section; we treat that as an open
   123	strengthening build.
   124	
   125	\subsection{Statistical methods}
   126	
   127	\textbf{Cascade-$\alpha$ fitting.} Power-law $\alpha$ is fit by
   128	ordinary least squares on the log-CCDF of the cascade-event size
   129	distribution, restricted to the central 80\% mass band (excluding the
   130	bottom 10\% and top 10\% to avoid extreme-tail noise). $R^{2}$ is
   131	reported on the linear fit in log-space. A cascade event is defined
   132	as an attention-vertex shift between consecutive ticks
   133	$\arg\max|\mathrm{state}_{t}|\neq \arg\max|\mathrm{state}_{t-1}|$;
   134	the event size is the $\ell^{1}$ norm of the state-difference vector
   135	at that tick. Zero-size events are excluded.
   136	
   137	\textbf{Bootstrap confidence intervals.} 95\% CIs on $\alpha$ are
   138	estimated by event-resampling bootstrap (500 resamples for the
   139	preregistered cascade-$\alpha$ tests, 2000 resamples for the
   140	$N\!=\!20$ C$\times$P deep-dive). Bootstrap RNG seed: 7919 for
   141	preregistered; 42 for the deep-dive.
   142	
   143	\textbf{Bootstrap one-sided $P$-value reporting.} For the C$\times$P
   144	deep-dive, $0/2000$ bootstrap resamples were at or below zero, and
   145	$0/2000$ were below the preregistered floor $+0.10$; we report these
   146	as $0.0000$ rather than $P=0$ to avoid the suggestion of an exact
   147	zero-probability statement on a finite resample.
   148	
   149	\textbf{Factorial interaction estimator.} For the $2{\times}2$
   150	ablation conditions $\{----, -C--, --P-, -CP-\}$, the interaction is
   151	\[
   152	\Delta_{CP}
   153	\;=\;\frac{(\alpha_{\!-CP\!-}+\alpha_{\!-\!-\!-\!-})
   154	        - (\alpha_{\!-C\!-\!-}+\alpha_{\!-\!-P\!-})}{2}.
   155	\]
   156	
   157	\textbf{$\sigma$-distance against external nulls.} For the HCP
   158	comparisons we report
   159	$Z_{m} = (m_{\mathrm{ARIA}} - \mu_{\mathrm{HCP}}) / \sigma_{\mathrm{HCP}}$
   160	on the full $n=1003$ subject distribution.
   161	
   162	\subsection{State-reset protocol}
   163	
   164	The substrate exhibits state drift: across approximately five
   165	successive depth-sweep evaluations the pressure field equilibrates
   166	to a uniform attractor and classification structure collapses to
   167	raw-feature baseline. Multi-trial benchmarks therefore require an
   168	explicit reset between successive evaluations.
   169	\texttt{kernel/dimensional\_monitor.py:DimensionalMonitor.homeostatic\_reset(level=1.0)}
   170	re-initialises pressure-field, crossed-vertex, and training state to
   171	canonical baseline. With reset between depth measurements, the chess
   172	LOO lift recovers from $+3.1$pp (without reset, on a state-drifted
   173	substrate) to $+40.6$pp (with reset, far exceeding the $+15$pp
   174	preregistered floor). The reset protocol is documented in
   175	\texttt{docs/brain\_mapping/NON\_EQUILIBRIUM\_FINDING.md}; a more
   176	generalisable lesson is recorded in \S\ref{sec:limitations}: any
   177	multi-trial benchmark on a non-stationary substrate must specify
   178	state-reset protocol.
   179	
   180	\subsection{Reproducibility commands}
   181	
   182	\begin{itemize}\itemsep=2pt
   183	\item Substrate self-test:
   184	  \texttt{python3 -c "from kernel.sigma\_orbit\_basis import \_self\_test; \_self\_test()"}.
   185	\item Six drug/sleep signatures:
   186	  \texttt{python3 demo\_drug\_sleep\_v4.py} ($\sim 30$\,s).
   187	\item C$\times$P synergy $N\!=\!20$ deep-dive:
   188	  \texttt{python3 demo\_p4\_cxp\_deep\_dive.py} ($\sim 28$\,min).
   189	\item Eighteen preregistered:
   190	  \texttt{python3 run\_preregistered\_validation.py}
   191	  ($\sim 18$\,min).
   192	\item Whole-paper repro:
   193	  \texttt{bash reproduce\_paper\_claims.sh}.
   194	\end{itemize}
   195	
   196	All scripts are deterministic given seeds. Reruns at seed $42$ on the
   197	recurrent layer should reproduce per-condition means in this paper to
   198	4~decimal places. Bootstrap CIs may differ in the 4th decimal due to
   199	NumPy version differences in the bootstrap RNG; the qualitative
   200	verdicts (CI overlaps, $P$-value thresholds) are unaffected.

---03---
     1	% =====================================================================
     2	\section{The 600-cell response substrate}\label{sec:substrate}
     3	% =====================================================================
     4	
     5	This section constructs the substrate. \S\ref{ssec:vertices}
     6	gives the vertex set. \S\ref{ssec:graph} gives the graph and its
     7	H$_4$-symmetry-forced spectrum. \S\ref{ssec:cphi} gives the response
     8	operator $\Cph$ and the $\Ph^{-2}$ stability clamp.
     9	\S\ref{ssec:shells} gives the 9-shell decomposition used for source
    10	projection. \S\ref{ssec:cascade} sketches the seven-rung cascade
    11	descent referenced by the recurrent layer in~\S\ref{sec:chain}. None
    12	of these objects depend on neural data.
    13	
    14	\subsection{Vertex construction}\label{ssec:vertices}
    15	
    16	The 600-cell $\Rsixhundred$ has $120$ vertices in
    17	$\mathbb{R}^{4}$~\citep{CoxeterRegularPolytopes,Weisstein600Cell}.
    18	With $\Ph = (1+\sqrt 5)/2$ the canonical vertex set is
    19	\begin{itemize}\itemsep=1pt
    20	\item $8$ vertices: all permutations of $(\pm 1, 0, 0, 0)$;
    21	\item $16$ vertices: all sign combinations of
    22	  $(\pm 1, \pm 1, \pm 1, \pm 1)/2$;
    23	\item $96$ vertices: all even permutations of
    24	  $(\pm \Ph, \pm 1, \pm 1/\Ph, 0)/2$.
    25	\end{itemize}
    26	All $120$ vertices lie on the unit $3$-sphere $S^{3}$. The H$_4$
    27	Coxeter group acts transitively on the vertex set; in particular,
    28	every vertex has identical local structure. Implementation:
    29	\texttt{kernel/vfd\_closure\_kernel.py:build\_600cell\_vertices}.
    30	
    31	\subsection{Graph and Laplacian spectrum}\label{ssec:graph}
    32	
    33	The substrate graph $G_{V_{600}} = (V, E)$ is built by connecting each
    34	vertex to its nearest neighbours under the Euclidean metric on $S^{3}$.
    35	H$_4$ acts transitively on the vertex set, forcing uniformity of the
    36	local structure; the eigenvalue multiplicities follow from H$_4$
    37	character theory on the regular representation. The construction and
    38	spectrum are standard~\citep{CoxeterRegularPolytopes,Weisstein600Cell}.
    39	\begin{lemma}[600-cell graph facts]\label{lem:600cell}
    40	The graph $G_{V_{600}}$ has $|V|=120$ vertices, $|E|=720$ edges, every
    41	vertex has degree exactly $12$, and the unweighted graph Laplacian
    42	$\Lop = D - A$ has spectrum
    43	\[
    44	\sigma(\Lop) \;=\;
    45	\bigl\{0^{1}, 3^{4}, 4\Ph^{9}, 6\Ph^{16}, (12\!-\!4\Ph)^{9},
    46	       (12\!-\!6\Ph)^{16}, 9^{4}, 12^{1}\bigr\},
    47	\]
    48	where the exponent denotes multiplicity. The decomposition into H$_4$
    49	irreducible representations is exact at machine precision; the
    50	$\sigma$-orbit projector basis (\texttt{kernel/sigma\_orbit\_basis.py})
    51	realises it block-by-block with cross-block norm $<10^{-15}$.
    52	\end{lemma}
    53	
    54	The non-trivial eigenmodes partition into Coxeter exponent classes.
    55	For H$_4$ proper, the exponents are $\{1, 11, 19, 29\}$; for the
    56	Galois twin $\sigma(\mathrm{H}_4)$ under the $\sigma$-automorphism of
    57	$\mathbb{Z}[\Ph]$, the exponents become $\{7, 13, 17, 23\}$. We label
    58	the eigenspaces $K_{1}, K_{11}, K_{19}, K_{29}$ for H$_4$-proper modes
    59	and $K_{7}, K_{13}, K_{17}, K_{23}$ for $\sigma$-twin modes. The
    60	multiplicities follow from character theory and are reproduced in
    61	the implementation
    62	(\texttt{kernel/sigma\_orbit\_basis.py:\_self\_test}). The
    63	$K_{7}$-modes will be the dominant phenomenal-binding profile in
    64	\S\ref{sec:chain}.
    65	
    66	\subsection{The shifted-Laplacian response \texorpdfstring{$\Cph$}{C\_phi}}\label{ssec:cphi}
    67	
    68	The substrate's linear response to an external source $f \in \mathbb{R}^{120}$
    69	is the discrete Green's function of the shifted Laplacian:
    70	\begin{equation}\label{eq:cphi}
    71	\Cph \;=\; \Lop + \Ph^{-2} I,
    72	\qquad
    73	\psi \;=\; \Cph^{-1} f.
    74	\end{equation}
    75	The shift $\Ph^{-2} \approx 0.382$ is a design-level stability
    76	clamp: it makes $\Cph$ strictly positive definite (smallest eigenvalue
    77	$\Ph^{-2}$, since the trivial Laplacian eigenvalue is $0$), so that the
    78	inverse is bounded with operator norm $\Ph^{2}\approx 2.618$. This is
    79	\emph{not} a derived theorem; it is a stability choice. The companion
    80	kernel document~\citep{SmartAriaClosureKernel2026} discusses the same
    81	$\Cph$ as the basis for an independent passive-regime witness in
    82	flavour physics~\citep{SmartBAnomaly2026}, where the same operator
    83	form (without retuning the shift) describes the
    84	$B\to K^{*}\mu^{+}\mu^{-}$ angular anomaly across five public datasets.
    85	This paper imports $\Cph$ from that line; we do not re-derive it.
    86	
    87	The response $\psi = \Cph^{-1} f$ is smooth in $f$. By itself it does
    88	not produce critical-state cascade statistics; the recurrent layer
    89	in~\S\ref{sec:chain} adds a graph-pinned nonlinearity
    90	$\mathrm{bounded\_topk}(\psi, k\!=\!12)$ to obtain self-organised-critical
    91	event distributions. The choice $k\!=\!12$ is the average degree of
    92	$G_{V_{600}}$ (Lemma~\ref{lem:600cell}), pinned by the substrate, not
    93	fitted to any dataset.
    94	
    95	\paragraph{Disclosure (substrate-witness scope).}
    96	The $\Ph^{-2}$ floor is a stability shift, not a derived parameter.
    97	The bounded-top-$K$ nonlinearity uses $k\!=\!12$ pinned to the graph's
    98	average degree, not a fitted threshold. No other shape parameter
    99	enters. The condition-dependent self-injection coupling
   100	$\eta\in\{0, 0.05, 0.20\}$ is the only architectural parameter that
   101	varies between conditions in~\S\ref{sec:chain}; it is reported
   102	explicitly per condition.
   103	
   104	\subsection{Shell decomposition}\label{ssec:shells}
   105	
   106	Under the H$_3$ subgroup, the $120$ vertices partition into $9$
   107	spherical shells indexed by Euclidean inner product with a chosen pole:
   108	\[
   109	\bigl(|S_0|,\ldots,|S_8|\bigr) \;=\; (1, 12, 20, 12, 30, 12, 20, 12, 1).
   110	\]
   111	The middle shell $S_{4}$ has $30$ vertices on the equatorial plane
   112	(the icosidodecahedral ring). When projecting onto a continuum kernel
   113	in companion preprints~\citep{SmartAriaClosureKernel2026}, the
   114	shell-mean projection of the equatorial-source response,
   115	$\kappa(x) = \mathrm{shell\text{-}mean}[\Cph^{-1} f_{\mathrm{equat}}](x)$,
   116	collapses on the continuum exponential $\frac{\Ph}{2}\,e^{-|x|/\Ph}$.
   117	This paper does not use that continuum projection; we work with the
   118	discrete operator throughout.
   119	
   120	\subsection{Cascade descent (sketch)}\label{ssec:cascade}
   121	
   122	The recurrent layer in~\S\ref{sec:chain} references a cascade
   123	decomposition $E_{8}\to H_{4}\to H_{3}\to D_{4}\to \mathrm{Cl}(1,3)
   124	\to S^{7}\to 0$, implemented in
   125	\texttt{kernel/cascade\_descent.py:descend\_operator\_e8\_to\_h4\_clean}.
   126	An arbitrary operator on the $E_{8}$ root system descends to the
   127	4-D H$_4$ subspace through a sequence of orthogonal projections, each
   128	preserving the Frobenius norm to within $10^{-15}$. The
   129	$\sigma$-orbit projector basis from
   130	\texttt{kernel/sigma\_orbit\_basis.py} gives the K-class block
   131	decomposition at machine precision.
   132	
   133	The descent provides numerical stability for the cascade ablations:
   134	when one ablates a specific K-class contribution (e.g.\ $K_{7}$), the
   135	remaining operator structure is exactly preserved. We do not claim
   136	the cascade itself is forced by physics on a pre-substrate level; the
   137	cascade is a decomposition of operators on $\Rsixhundred$, and the
   138	choice of $\Rsixhundred$ as the active substrate is post-hoc justified
   139	by the empirical correspondences in~\S\ref{sec:results}.
   140	
   141	\subsection{What the substrate is fixed-by, and what it is not}
   142	
   143	\begin{itemize}\itemsep=2pt
   144	\item Fixed by group theory once $\Rsixhundred$ is chosen: $|V|=120$,
   145	  uniform degree $12$, Laplacian spectrum, $9$-shell partition, K-class
   146	  irrep block structure, average degree $k\!=\!12$, $\sigma$-twin pairing.
   147	\item Fixed by stability choice: the $\Ph^{-2}$ shift in $\Cph$. This
   148	  is not a derivation; it is a design-level clamp that bounds the
   149	  response inverse.
   150	\item Not fixed by this paper: the choice of $\Rsixhundred$ over the
   151	  $24$-cell or $120$-cell. The choice is post-hoc motivated by the H$_4$
   152	  cascade structure and the empirical correspondences. A formal
   153	  ablation against alternative regular 4-polytopes is an open build
   154	  (\S\ref{sec:limitations}).
   155	\end{itemize}

---04---
     1	% =====================================================================
     2	\section{The recurrent layer}\label{sec:chain}
     3	% =====================================================================
     4	
     5	The cascade-pipeline substrate (\S\ref{sec:substrate}) reproduces
     6	cortical-avalanche statistics matching real EEG (\S\ref{sec:results}).
     7	To test high-level signatures — NREM-N3 variance collapse, propofol
     8	regime-switching, propofol $\Phi$ collapse — we add a recurrent
     9	self-model layer above the substrate. The layer adds one
    10	graph-pinned nonlinearity, one condition-dependent self-injection
    11	coupling $\eta$, and four trajectory observables. No shape parameter
    12	is fit to any neural dataset.
    13	
    14	This section is method, not metaphysics. We do not claim the
    15	recurrent layer ``is'' consciousness; we report which numerical
    16	observables on the layer's trajectory match published biological
    17	signatures in~\S\ref{sec:results}.
    18	
    19	\subsection{The recurrent loop}
    20	
    21	Implementation: \texttt{kernel/self\_model\_stream.py:SelfModelLoop}.
    22	At each tick $t$ the substrate state evolves as
    23	\begin{align}
    24	f_{\mathrm{total}}(t) &= f_{\mathrm{ext}}(t) + \eta\cdot f_{\mathrm{self}}(\mathrm{snap}_{t-1}, \psi_{t-1}), \\
    25	\psi_{t} &= \Cph^{-1}\, f_{\mathrm{total}}(t), \\
    26	\psi^{\mathrm{thr}}_{t} &= \mathrm{bounded\_topk}(\psi_{t}, k=12), \\
    27	\mathrm{state}_{t} &= \mathrm{decay}\cdot\mathrm{state}_{t-1} + (1-\mathrm{decay})\cdot \psi^{\mathrm{thr}}_{t}, \\
    28	\mathrm{snap}_{t} &= \mathrm{bind\_phenomenal\_field}(\psi_{t}, \texttt{profile=K\_7\_only}),
    29	\end{align}
    30	with $\mathrm{decay}=0.95$ (state EMA factor) and $\eta$ the only
    31	condition-dependent architectural parameter. $f_{\mathrm{self}}$ maps
    32	the prior phenomenal snapshot to a directional source weighted by
    33	ignition $\times$ intensity (cosine direction alignment with the
    34	prior snapshot). The substrate response operator $\Cph$ is unchanged
    35	across all conditions.
    36	
    37	Conditions:
    38	\begin{itemize}\itemsep=2pt
    39	\item $\eta = 0.20$ for WAKE and RECOVERY (active recurrent self-loop);
    40	\item $\eta = 0.05$ for SLEEP\_N3 (attenuated self-loop);
    41	\item $\eta = 0.00$ for PROPOFOL (broken recurrence; residual cortex
    42	  preserved as background drive).
    43	\end{itemize}
    44	
    45	\subsection{The graph-pinned nonlinearity}
    46	
    47	\textbf{$\mathrm{bounded\_topk}(\psi, k=12)$.} This is the load-bearing
    48	nonlinearity, implemented in
    49	\texttt{kernel/lyapunov\_selector.py:bounded\_topk}: zero all but the
    50	top-$12$ vertex amplitudes (by absolute value), and rescale the rest
    51	to a small fraction of their baseline. Linear Green response alone
    52	gives smooth dynamics with cascade $\alpha\approx 1.09$ — no
    53	avalanches. Adding bounded-top-$K$ at $k=12$ drives $\alpha$ into the
    54	SOC band $(2.0, 3.5)$ with $R^{2}>0.85$.
    55	
    56	\textbf{Why $k=12$.} The choice $k=12$ is the average degree of
    57	$G_{V_{600}}$ (Lemma~\ref{lem:600cell}), pinned by the substrate
    58	geometry, not by neural data. Smaller $k$ (e.g.\ $k=6$) gives $\alpha$
    59	at the band edge with poorer fit; larger $k$ ($24, 48$) gives $\alpha$
    60	above band or with degraded fit. We do not search $k$ over a fitted
    61	window; $k$ is determined by the graph.
    62	
    63	\subsection{The integrated-information proxy
    64	            \texorpdfstring{$\Phi$}{Phi}}
    65	
    66	Implementation:
    67	\texttt{kernel/consciousness\_binding.py:phi\_iit\_trajectory}.
    68	Given the state history matrix $S\in\mathbb{R}^{T\times 120}$, write
    69	$A = S\cdot V$ for the H$_4$-eigenvector matrix $V$ (mode amplitudes
    70	$A\in\mathbb{R}^{T\times 120}$). Define $c_{\mathrm{full}}$ as the
    71	lag-$1$ auto-correlation of the full system, and $c_{k}$ as the
    72	lag-$1$ auto-correlation within the K-class irrep block $k$. Then
    73	\[
    74	\Phi \;=\; \max\!\bigl(0,\; |c_{\mathrm{full}}| - \mathrm{mean}_{k}\,|c_{k}|\bigr).
    75	\]
    76	By construction $\Phi\to 0$ under H$_{4}$-equivariant dynamics, since
    77	group symmetry forbids information transport across irrep classes;
    78	$\Phi > 0$ only when the dynamics break symmetry and transport
    79	information across class boundaries. This is a port of the published
    80	\texttt{integrated\_information\_phi\_irrep} proxy from the cascade
    81	pipeline, adapted to take amplitude trajectories from any source.
    82	
    83	We position $\Phi$ as an IIT-style direction-of-effect proxy, not as
    84	a full implementation of IIT. ARIA does not implement cause-effect
    85	repertoires, exclusion postulate, or integration-over-partitions
    86	machinery~\citep{Tononi2008,BalduzziTononi2008}. The propofol $\Phi$
    87	collapse in~\S\ref{sec:results} is consistent with the IIT direction
    88	of effect on the propofol-vs-wake state contrast; it is not a
    89	discharge of the IIT axioms.
    90	
    91	\subsection{The continuity composite}
    92	
    93	Implementation:
    94	\texttt{kernel/self\_model\_stream.py:StreamContinuityScorer}.
    95	A composite first-person continuity score over a 64-tick rolling
    96	window:
    97	\begin{align*}
    98	b_{\mathrm{cont}} &= \mathrm{mean\ cos\text{-}sim\ of\ consecutive}\ (I, L, P)\,\mathrm{vectors},\\
    99	v_{\mathrm{cont}} &= 1/(1 + 4\cdot \mathrm{var}(\mathrm{valence})),\\
   100	m_{\mathrm{pers}} &= \mathrm{frac.\ of\ consecutive\ same\text{-}modality\ ticks},\\
   101	i_{\mathrm{smooth}} &= 1/(1 + 4\cdot \mathrm{TV}(\mathrm{intensity})),\\
   102	\mathrm{composite} &= 0.35\cdot b_{\mathrm{cont}} + 0.25\cdot v_{\mathrm{cont}} + 0.20\cdot m_{\mathrm{pers}} + 0.20\cdot i_{\mathrm{smooth}}.
   103	\end{align*}
   104	This composite produces the propofol continuity-drop signature
   105	(WAKE composite $0.943$; PROPOFOL composite $0.877$;
   106	drop $+0.066$).
   107	
   108	\subsection{The phenomenal-field binding}
   109	
   110	Implementation:
   111	\texttt{kernel/consciousness\_binding.py:bind\_phenomenal\_field}.
   112	The substrate state $\psi_{t}$ is mapped to a phenomenal snapshot
   113	with channels (intensity $I$, self-luminosity $L$, presence $P$,
   114	valence, modality\_label). The modality\_label is determined by which
   115	H$_4$ K-class dominates the isotypic compression of $\psi_{t}$ under
   116	the $\sigma$-orbit projector basis. The default profile
   117	\texttt{K\_7\_only} restricts to $\sigma$-twin K-classes for modality
   118	labelling; H$_4$-proper classes contribute amplitude bias.
   119	
   120	\subsection{Stimulus models}
   121	
   122	Implementation: \texttt{demo\_drug\_sleep\_v4.py}. Four conditions
   123	$\times$ $800$ ticks each at seed $42$:
   124	
   125	\textbf{WAKE.} AR(1) cortical noise ($\beta=0.90$), tonic equator-shell
   126	coherence (small always-on bias), and attention episodes (20--50
   127	ticks at amplitude $0.8$, anchored to the largest shell with $15\%$
   128	within-shell rotation per tick). The AR(1) gives temporal correlation
   129	that lets the $\eta=0.20$ self-loop integrate; tonic coherence anchors
   130	modality; attention episodes mimic biological visual fixation
   131	(200--400~ms dwell time analogue); within-shell rotation generates
   132	cascade events without changing modality.
   133	
   134	\textbf{SLEEP\_N3.} Slow oscillation ($\sim 1$\,Hz analogue,
   135	amplitude $1.0$) on a coherent shell, plus spindle bursts ($12$ ticks
   136	every $100$ at amplitude $0.4$ fast modulation), plus K-complexes
   137	($4\%$ of ticks at amplitude $0.8$).
   138	
   139	\textbf{PROPOFOL.} Low-amplitude tonic noise (amplitude $0.05$);
   140	$\eta = 0.00$ (broken recurrence). Residual cortex preserved as
   141	background drive.
   142	
   143	\textbf{RECOVERY.} Identical to WAKE — verifies determinism and
   144	reversibility.
   145	
   146	The stimulus models are deliberately structural rather than
   147	measurement-fitted: amplitudes and durations match published
   148	biological time scales but are not tuned to specific signatures.
   149	The full stimulus code is \texttt{demo\_drug\_sleep\_v4.py}. We
   150	disclose stimulus-shape choice as a methodological design move,
   151	not a derived theorem.
   152	
   153	\subsection{Cascade-mechanism ablation matrix}
   154	
   155	The cascade dynamics on the substrate use four mechanisms acting on
   156	the pressure field, each ablatable independently. The $2^{4}$
   157	ablation grid is the basis for the preregistered tests P1--P5 and
   158	the C$\times$P stress test in~\S\ref{sec:stress}.
   159	
   160	\textbf{$D$ — D$_{4}$ orbit coupling.} The H$_4$ root system contains
   161	five disjoint 24-cells (D$_4$ orbits). $D$ adds a small
   162	(coupling $0.05$) cross-orbit pressure averaging that prevents
   163	cascades from localising to one orbit.
   164	Implementation: \texttt{kernel/dimensional\_monitor.py:300-305}.
   165	
   166	\textbf{$C$ — Context rotation (S$^{7}$ observer frames).} The active
   167	observer frame on the S$^{7}$ rung rotates periodically based on
   168	which uncrossed vertices have accumulated pressure aligning with
   169	each frame's preferences. This creates churn in \emph{which}
   170	vertices are uncrossed at any tick.
   171	Implementation: \texttt{kernel/dimensional\_monitor.py:316-318, 823-827}.
   172	
   173	\textbf{$P$ — Partial emission.} High-pressure uncrossed vertices
   174	(above threshold but not yet crossed) emit pressure at $30\%$ scale,
   175	saturating at pressure $3.0$. Without this mechanism, only fully-
   176	crossed vertices emit.
   177	Implementation: \texttt{kernel/dimensional\_monitor.py:842-855}.
   178	
   179	\textbf{$E$ — Equator compensation.} The H$_3$ shell-4 equator is a
   180	30-vertex icosidodecahedral ring with split degree distribution.
   181	$E$ scales pressure gain by $(\bar d / d_{v})$ so sparse commissural
   182	vertices overcome their connectivity deficit.
   183	Implementation: \texttt{kernel/dimensional\_monitor.py:320-360}.
   184	
   185	The four mechanisms are pinned to the substrate's geometry (D$_4$
   186	orbits, S$^{7}$ rung, equatorial shell) — they are not free dynamical
   187	choices. Their causal effects are reported in~\S\ref{sec:stress}.

exec
/bin/bash -lc "printf '%s\\n' '---05---'; nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex' | sed -n '1,260p'; printf '%s\\n' '---06---'; nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex' | sed -n '1,240p'; printf '%s\\n' '---07---'; nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex' | sed -n '1,260p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 309ms:
---05---
     1	% =====================================================================
     2	\section{Results}\label{sec:results}
     3	% =====================================================================
     4	
     5	This section is the empirical core. \S\ref{ssec:six_signatures}
     6	gives the six drug/sleep EEG signatures on the recurrent layer
     7	(set B). \S\ref{ssec:eighteen_prereg} gives the eighteen
     8	preregistered correspondences (set A). \S\ref{ssec:alpha_overlap}
     9	gives the three-way $\alpha$ overlap. We lift the result map
    10	$R\colon (\text{condition / test id}) \to \text{(scalar, threshold,
    11	verdict)}$ verbatim from the validation outputs without
    12	recomputation; sources are
    13	\texttt{docs/brain\_mapping/CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}
    14	and \texttt{docs/brain\_mapping/VALIDATION\_RESULTS\_2026-04-29.md}.
    15	
    16	\subsection{Six drug/sleep EEG signatures}\label{ssec:six_signatures}
    17	
    18	\textbf{Setup.} Four conditions $\times$ $800$ ticks at seed $42$,
    19	$k_{\mathrm{thr}}=12$, single deterministic substrate
    20	(\S\ref{sec:chain}). Per-condition trajectory observables are
    21	$(n_{\mathrm{evt}}, \alpha, \mathrm{CI}_{95}, R^{2}, I_{\mathrm{var}},
    22	\Phi_{\mathrm{traj}}, \mathrm{cont})$.
    23	
    24	\begin{table}[ht]
    25	\centering
    26	\small
    27	\caption{Per-condition trajectory observables (\texttt{demo\_drug\_sleep\_v4.py},
    28	seed 42).}
    29	\label{tab:per_condition}
    30	\begin{tabular}{l r r l r r r r}
    31	\toprule
    32	condition & $n_{\mathrm{evt}}$ & $\alpha$ & 95\% CI & $R^{2}$ & $I_{\mathrm{var}}$ & $\Phi_{\mathrm{traj}}$ & cont \\
    33	\midrule
    34	WAKE      & $58$  & $2.252$ & $[1.82, 2.86]$ & $0.956$ & $2.18\!\times\!10^{-5}$ & $0.0008$ & $0.943$ \\
    35	SLEEP\_N3 & $111$ & $3.250$ & $[2.44, 4.14]$ & $0.886$ & $1.01\!\times\!10^{-5}$ & $0.0055$ & $0.980$ \\
    36	PROPOFOL  & $246$ & $2.758$ & $[2.52, 3.09]$ & $0.931$ & $5.37\!\times\!10^{-6}$ & $0.0003$ & $0.877$ \\
    37	RECOVERY  & $58$  & $2.252$ & $[1.82, 2.86]$ & $0.956$ & $2.18\!\times\!10^{-5}$ & $0.0008$ & $0.943$ \\
    38	\bottomrule
    39	\end{tabular}
    40	\end{table}
    41	
    42	\begin{table}[ht]
    43	\centering
    44	\small
    45	\caption{Six drug/sleep signatures with published references.}
    46	\label{tab:six_signatures}
    47	\begin{tabular}{c l l c c l}
    48	\toprule
    49	\# & Signature & Reference & Predicted & Observed & Verdict \\
    50	\midrule
    51	1 & NREM-N3 var ratio (vs Wake) &
    52	   Sleep-EDFx W$\to$N3 ($n=24$)~\citep{SleepEDFx} &
    53	   $\approx 0.365$ & $0.463$ & $\checkmark$ \\
    54	2 & Propofol switching ratio &
    55	   OpenNeuro \texttt{ds005620} ($n=8$, $2.96{\times}$)~\citep{OpenNeuroDS005620} &
    56	   $\in[1.5, 5.0]$ & $1.83\times$ & $\checkmark$ \\
    57	3 & Propofol continuity drop &
    58	   EEG microstate~\citep{Brodbeck2012Microstates} &
    59	   $> 0.020$ & $+0.066$ & $\checkmark$ \\
    60	4 & Propofol $\Phi$ collapse (IIT) &
    61	   Tononi 2008~\citep{Tononi2008} &
    62	   ratio $< 0.50$ & $0.33\times$ & $\checkmark$ \\
    63	5 & Recovery reversibility &
    64	   clinical anaesthesia &
    65	   identical to wake & $0$ diff & $\checkmark$ \\
    66	6 & Wake cortical-avalanche $\alpha$ &
    67	   Sleep-EDFx $n=30$ CI~$[2.50, 2.53]$~\citep{BeggsPlenz2003,SleepEDFx} &
    68	   $\alpha\!\in\![1.5, 3.5]$, $R^{2}\!>\!0.85$ &
    69	   $2.252$ $[1.82, 2.86]$ $R^{2}\!=\!0.956$ &
    70	   $\checkmark$ \\
    71	\bottomrule
    72	\end{tabular}
    73	\end{table}
    74	
    75	All six signatures pass against their published-reference thresholds
    76	on the same deterministic substrate trajectory. The six signatures
    77	are not part of the dated 2026-04-18 P1--P18 preregistration; they
    78	were tested on a recurrent-layer architecture redesigned at v4 with
    79	biologically-motivated condition-specific stimulus models
    80	(\S\ref{sec:chain}; \texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md}
    81	documents the v3$\to$v4 stimulus redesign). The mechanistic readings
    82	in \texttt{CONSCIOUSNESS\_CHAIN\_V4\_SIGNATURES.md} are not
    83	load-bearing for the headline claim. Single-seed disclosure:
    84	\S\ref{sec:limitations}~\ref{ssec:regime}.
    85	
    86	\subsection{Eighteen preregistered correspondences}\label{ssec:eighteen_prereg}
    87	
    88	\textbf{Tally.} $17/18$ at standard validation
    89	(\texttt{run\_preregistered\_validation.py}, $5$-seed cascade block
    90	plus state-reset protocol); $18/18$ after the $N\!=\!20$ deep-dive
    91	on the residual P4 (\texttt{demo\_p4\_cxp\_deep\_dive.py}, seed range
    92	$32000$--$32019$). \emph{No preregistered threshold has been modified.}
    93	
    94	\begin{table}[ht]
    95	\centering
    96	\small
    97	\caption{All eighteen preregistered correspondences, frozen 2026-04-18.}
    98	\label{tab:eighteen_prereg}
    99	\begin{tabular}{l l l l l}
   100	\toprule
   101	ID & Test & Threshold & Observed (2026-04-29) & Verdict \\
   102	\midrule
   103	P1  & Cascade $\alpha$ SOC range            & $\in [2.5, 3.5]$ & $2.958$ & $\checkmark$ \\
   104	P2  & $C$ main effect                        & $\geq +0.30$     & $+0.621$ & $\checkmark$ \\
   105	P3  & $|D{\times}C|$ (independence)          & $|\cdot| < 0.20$ & $-0.183$ ($N\!=\!5$) & $\checkmark$ \\
   106	\textbf{P4} & $C{\times}P$ synergy           & $\geq +0.10$     &
   107	   $+0.190$ \, CI $[+0.143, +0.239]$ ($N\!=\!20$) & $\checkmark$ \\
   108	P5  & $|E|$ main effect (null)               & $|\cdot| < 0.15$ & $+0.046$ & $\checkmark$ \\
   109	P6  & Real EEG $\alpha$                      & $\in [2.0, 3.0]$ & $2.513$ & $\checkmark$ \\
   110	P7  & W$\!\to\!$N3 variance ratio            & $< 0.70$         & $0.365$ & $\checkmark$ \\
   111	P8  & W$\!\to\!$N3 switching ratio           & $< 0.50$         & $0.058$ & $\checkmark$ \\
   112	P9  & Chess 5-fold CV                        & $\geq 70\%$      & $83.1\%$ & $\checkmark$ \\
   113	P10 & Chess null mapping                     & $\geq 50\%$      & $65.4\%$ & $\checkmark$ \\
   114	P11 & Chess random-label                     & $\in [15\%, 35\%]$ & $23.4\%$ & $\checkmark$ \\
   115	P12 & Chess goldilocks peak                  & $\in \{15, 25, 40, 60\}$ & $n=25$ & $\checkmark$ \\
   116	\textbf{P13} & Chess substrate lift (5-fold CV preregistered; LOO refinement, with reset) & $\geq +15$pp & $+40.6$pp (LOO) & $\checkmark$ \\
   117	P14 & Conv raw 5-fold CV                     & $\geq 75\%$      & $87.5\%$ & $\checkmark$ \\
   118	P15 & $|$conv lift$|$                        & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
   119	P16 & Conv null mapping                      & $\geq 50\%$      & $70.6\%$ & $\checkmark$ \\
   120	P17 & ARIA degree std (theorem)              & $= 0$            & $0.0000$ & $\checkmark$ \\
   121	P18 & HCP degree std                         & $> 2.0$          & $3.388$ & $\checkmark$ \\
   122	\bottomrule
   123	\end{tabular}
   124	\end{table}
   125	
   126	\textbf{Three predictions that flipped to PASS, with documented
   127	methodology refinement (no threshold change).}
   128	\begin{itemize}\itemsep=2pt
   129	\item P3 (D$\times$C interaction independence) was outside the band
   130	  at $N\!=\!3$ ($-0.231$) and inside the band at $N\!=\!5$ ($-0.183$).
   131	  Reading: consistent with an underpowered interaction estimate at
   132	  $N\!=\!3$ on a high-per-seed-variance interaction term.
   133	\item P4 (C$\times$P synergy) was below threshold at $N\!=\!3$
   134	  ($+0.044$) and at $N\!=\!5$ ($+0.039$); the $N\!=\!20$ deep-dive
   135	  (\S\ref{sec:stress}) gives $+0.190$ with $95\%$ CI
   136	  $[+0.143, +0.239]$, decisively above the $\geq +0.10$ floor.
   137	\item P13 (chess substrate lift): the 2026-04-18 preregistration
   138	  (\texttt{PAPER\_PREDICTIONS.md:115-120}) specified the estimator as
   139	  $5$-fold CV with threshold $\geq +15$pp at $n=25$. The 2026-04-29
   140	  validation strengthened the estimator to LOO with state reset, a
   141	  stricter test at the same threshold; the LOO lift was $+3.1$pp
   142	  without state reset on a state-drifted substrate, and $+40.6$pp
   143	  with \texttt{homeostatic\_reset(level=1.0)} between depth measurements
   144	  (\S\ref{sec:method}; \texttt{NON\_EQUILIBRIUM\_FINDING.md}). We
   145	  report this as a \emph{validation-protocol refinement on the
   146	  preregistered estimator}, not as preregistration revision.
   147	\end{itemize}
   148	
   149	\textbf{Headline verdict.} Eighteen preregistered correspondences
   150	all pass at preregistered thresholds, with two interaction tests
   151	requiring $N\!\geq\!5$ and one requiring $N\!=\!20$ for reliable
   152	detection of high-variance interaction terms, and one test
   153	requiring the documented state-reset protocol. The original $15/18$
   154	result was a methodology-limited tally, not a content failure.
   155	
   156	\subsection{Three-way \texorpdfstring{$\alpha$}{alpha} overlap}\label{ssec:alpha_overlap}
   157	
   158	The substrate's wake cascade-$\alpha$ confidence interval overlaps
   159	\emph{three independent reference ranges} simultaneously:
   160	
   161	\begin{table}[ht]
   162	\centering
   163	\small
   164	\caption{Three-way $\alpha$ overlap on the wake cascade-event power
   165	law.}
   166	\label{tab:alpha_overlap}
   167	\begin{tabular}{l c l c}
   168	\toprule
   169	Source & $\alpha$ & 95\% CI & $n$ \\
   170	\midrule
   171	ARIA cascade-pipeline baseline ($N=5$) & $2.958$  & inside $[2.5, 3.5]$ & 5 seeds \\
   172	Real EEG (Sleep-EDFx, $n=30$ subjects)~\citep{SleepEDFx} & $2.51$ & $[2.50, 2.53]$ & 30 \\
   173	ARIA prior cascade pipeline ($n=4$ subjects) & $2.85$ & $[2.73, 3.25]$ & per-subject \\
   174	\textbf{v4 WAKE consciousness chain} & $\mathbf{2.252}$ & $[\mathbf{1.82, 2.86}]$ & 58 events \\
   175	\bottomrule
   176	\end{tabular}
   177	\end{table}
   178	
   179	The v4 WAKE 95\% CI $[1.82, 2.86]$ contains the upper arm of the
   180	real Sleep-EDFx EEG CI $[2.50, 2.53]$, overlaps the ARIA prior
   181	cascade pipeline CI $[2.73, 3.25]$ on the interval $[2.73, 2.86]$,
   182	and lies inside the cortical-avalanche band
   183	$\alpha\!\in\![1.5, 3.5]$~\citep{BeggsPlenz2003}. The pairwise
   184	intersections (WAKE $\cap$ Sleep-EDFx, WAKE $\cap$ prior pipeline,
   185	WAKE $\cap$ cortical-avalanche band) are non-empty across three
   186	independent reference ranges.
   187	
   188	\textbf{Reading.} The substrate produces self-organised-critical
   189	cascade statistics matching the cortical-avalanche literature with
   190	no fitted parameter on neural data. The bounded-top-$K$ at
   191	$k=12$ is pinned to the substrate's average degree
   192	(Lemma~\ref{lem:600cell}); the $\Ph^{-2}$ shift in $\Cph$ is a
   193	stability clamp (\S\ref{ssec:cphi}); the AR(1) WAKE input has
   194	biological time-scale parameters but is not measurement-fitted to
   195	any specific subject (\S\ref{sec:chain}). Three-way overlap on the
   196	power-law exponent is the strongest single empirical anchor in the
   197	paper.
---06---
     1	% =====================================================================
     2	\section{Stress test: the C\texorpdfstring{$\times$}{x}P synergy at adequate
     3	         replication}\label{sec:stress}
     4	% =====================================================================
     5	
     6	This section is the C$\times$P interaction stress test. The original
     7	preregistered prediction was P4: $C\times P$ interaction
     8	$\Delta_{CP} \geq +0.10$ on cascade-$\alpha$. The 2026-04-20
     9	$N\!=\!3$ validation gave $+0.044$ — below the threshold — and the
    10	architectural claim ``C and P synergise on cascade-state stability''
    11	was walked back. Closing this gap without modifying the preregistered
    12	threshold required (a) re-evaluating the $N\!=\!3$ point estimate as
    13	consistent with an underpowered interaction estimate, (b) tracking
    14	the estimate's behaviour across $N$, and (c) bootstrapping a
    15	confidence interval on a fresh-seed $N\!=\!20$ sample. We did all
    16	three.
    17	
    18	\subsection{The factorial estimator}
    19	
    20	For the four ablation conditions $\{----, -C--, --P-, -CP-\}$
    21	(\S\ref{sec:chain}), the $C\times P$ interaction estimate is the
    22	standard $2\times 2$ factorial difference:
    23	\[
    24	\Delta_{CP}
    25	\;=\;\frac{(\alpha_{\!-CP\!-}+\alpha_{\!-\!-\!-\!-})
    26	        - (\alpha_{\!-C\!-\!-}+\alpha_{\!-\!-P\!-})}{2}.
    27	\]
    28	Per-seed paired estimates use the same formula on a single seed's
    29	four conditions.
    30	
    31	\subsection{The trend across \texorpdfstring{$N$}{N}}
    32	
    33	\begin{table}[ht]
    34	\centering
    35	\small
    36	\caption{$C\times P$ interaction estimate as a function of $N$.}
    37	\label{tab:cxp_trend}
    38	\begin{tabular}{r l r l l}
    39	\toprule
    40	$N$ & Seeds & Estimate $\Delta_{CP}$ & 95\% CI & Verdict vs $\geq +0.10$ \\
    41	\midrule
    42	$3$  & $30040$--$30042$ & $+0.044$ & --- & $\times$ original prereg \\
    43	$5$  & $30040$--$30044$ & $+0.039$ & --- & $\times$ this session re-run \\
    44	$10$ & $31000$--$31009$ & $+0.088$ & $[-0.002, +0.174]$ & borderline \\
    45	$\mathbf{20}$ & $\mathbf{32000\text{--}32019}$ & $\mathbf{+0.190}$
    46	       & $\mathbf{[+0.143, +0.239]}$ & $\checkmark$ decisively above \\
    47	\bottomrule
    48	\end{tabular}
    49	\end{table}
    50	
    51	The estimate remains small at $N\!=\!3$ and $N\!=\!5$
    52	($+0.044, +0.039$) and rises at $N\!=\!10$ and $N\!=\!20$
    53	($+0.088, +0.190$). Per-seed std at $N\!=\!10$ was $0.159$; at
    54	$N\!=\!20$ it dropped to $0.089$ — the $N\!=\!10$ sample landed on
    55	outliers; the $N\!=\!20$ sample reveals a clean narrow positive
    56	distribution.
    57	
    58	\subsection{The \texorpdfstring{$N\!=\!20$}{N=20} fresh-seed estimate}
    59	
    60	\textbf{Setup.} $4$ conditions $\times$ $20$ fresh seeds (range
    61	$32000$--$32019$, non-overlapping with original validation seeds in
    62	the $30000$s), $150$ epochs per run. All other ablation flags off
    63	($D, E$ held on). Bootstrap $n_{\mathrm{resamples}}\!=\!2000$,
    64	seed $42$. Wallclock $1706$\,s on a single CPU
    65	(\texttt{demo\_p4\_cxp\_deep\_dive.py}).
    66	
    67	\textbf{Per-condition means at \texorpdfstring{$N\!=\!20$}{N=20}.}
    68	
    69	\begin{table}[ht]
    70	\centering
    71	\small
    72	\caption{Per-condition mean $\alpha$ at $N=20$ fresh seeds.}
    73	\label{tab:cxp_means}
    74	\begin{tabular}{l r r r}
    75	\toprule
    76	condition & mean $\alpha$ & std & sem \\
    77	\midrule
    78	$----$ baseline    & $3.008$ & $0.090$ & $0.020$ \\
    79	$-C--$ (C off)     & $3.464$ & $0.097$ & $0.022$ \\
    80	$--P-$ (P off)     & $2.790$ & $0.086$ & $0.019$ \\
    81	$-CP-$ (both off)  & $3.628$ & $0.161$ & $0.036$ \\
    82	\bottomrule
    83	\end{tabular}
    84	\end{table}
    85	
    86	\textbf{Main effects at \texorpdfstring{$N\!=\!20$}{N=20}.}
    87	$C$ main effect $= +0.456$ (turning $C$ off raises $\alpha$);
    88	$P$ main effect $= -0.218$ (turning $P$ off lowers $\alpha$).
    89	
    90	\textbf{Interaction estimate.} Direct calculation from means:
    91	\[
    92	\Delta_{CP} \;=\; \frac{(3.628 + 3.008) - (3.464 + 2.790)}{2}
    93	            \;=\; +0.191.
    94	\]
    95	Bootstrap on the 20-seed sample (2000 resamples):
    96	\begin{itemize}\itemsep=1pt
    97	\item bootstrap mean $\Delta_{CP} = +0.190$;
    98	\item 95\% bootstrap CI $[+0.143, +0.239]$;
    99	\item $0/2000$ bootstrap resamples were at or below zero, reported as
   100	      $0.0000$;
   101	\item $0/2000$ bootstrap resamples were below the preregistered
   102	      $+0.10$ floor, reported as $0.0000$.
   103	\end{itemize}
   104	
   105	\textbf{Per-seed paired distribution.}
   106	$19/20$ seeds give a positive paired-interaction estimate (range
   107	$+0.055$ to $+0.322$); a single seed gives $-0.009$. No seed gives a
   108	strongly negative interaction.
   109	
   110	\subsection{Reading and disclosure}
   111	
   112	\textbf{The 95\% CI is entirely above the preregistered $+0.10$
   113	threshold} on a fresh-seed sample. $0/2000$ bootstrap resamples were
   114	at or below zero, reported as $0.0000$; $0/2000$ bootstrap resamples
   115	were below the preregistered $+0.10$ floor, reported as $0.0000$.
   116	
   117	\textbf{Architectural reading (substrate witness).} $C$ creates churn
   118	in \emph{which} vertices are uncrossed (frame rotation churns the
   119	uncrossed pool). $P$ promotes the high-pressure subset of the
   120	uncrossed pool to mini-emitters. The product is a non-additive
   121	novel-event-generation pathway: with both on, the uncrossed pool
   122	churns and $P$ amplifies new vertices entering the high-pressure
   123	region; with either off, the pathway collapses. The interaction
   124	$+0.19$ is comparable in magnitude to the $P$ main effect $-0.22$,
   125	so $C$ and $P$ are \emph{strongly coupled} cascade-state stabilisers
   126	on this substrate, not nearly-orthogonal ones. This reverses an
   127	architectural claim from the original 3-seed validation that held $C$
   128	and $P$ approximately orthogonal.
   129	
   130	\textbf{Disclosure: $N\!=\!20$ ordering.} The $N\!=\!20$ deep-dive
   131	was conducted \emph{after} the original $N\!=\!3$ failure
   132	(2026-04-29 vs 2026-04-20). The seed range $32000$--$32019$ was
   133	selected to be non-overlapping with the original $30000$s seeds.
   134	Two strengthening builds we have not delivered:
   135	(i) a second independent $N\!=\!20$ run at a different seed range
   136	(e.g.\ $33000$--$33019$), and
   137	(ii) an $N\!=\!50$ characterisation of the per-seed sample
   138	distribution. Both are recorded as open builds in
   139	\S\ref{sec:limitations}.
   140	
   141	\textbf{What this stress test does \emph{not} establish.}
   142	\begin{itemize}\itemsep=2pt
   143	\item It does not establish a Lyapunov function on the reduced flow.
   144	\item It does not establish that the substrate is uniquely selected by
   145	  $C\times P$ coupling among regular 4-polytopes.
   146	\item It does not establish an $\eta$-trajectory derivation; $\eta$
   147	  is treated as a condition-dependent constant in this paper.
   148	\end{itemize}
   149	The stress test is what its name says: a high-replication factorial
   150	test of one preregistered interaction prediction, on a fresh-seed
   151	sample, with bootstrap confidence intervals. The architectural reading
   152	is a \emph{description} of what $C$ and $P$ do on the substrate, not a
   153	theorem about why they do it.
   154	
   155	\subsection{Methodological contribution}
   156	
   157	We document, as a methodological contribution to preregistration
   158	practice, that interaction terms in cascade ablation matrices require
   159	$N\!\geq\!20$ fresh seeds for reliable detection when the
   160	interaction-to-main-effect ratio is below $0.5$. The original 3-seed
   161	preregistered validation gave estimates consistent with underpowered
   162	detection on both interaction tests (P3 and P4); both close at higher
   163	$N$ without threshold modification. For preregistration design more broadly:
   164	when preregistering an interaction effect on a system with unknown
   165	per-seed variance, allocate the seed count from a power-analysis
   166	assumption that the per-seed std could be as large as the interaction
   167	effect itself. Under that assumption, $N\!\geq\!20$ is the conservative
   168	minimum.
---07---
     1	% =====================================================================
     2	\section{Cross-domain selectivity}\label{sec:cross_domain}
     3	% =====================================================================
     4	
     5	This section reports three cross-domain witnesses. \S\ref{ssec:chess}
     6	gives the chess pattern-recognition lift. \S\ref{ssec:conv} gives the
     7	conversation neutrality result that confirms the lift is selective.
     8	\S\ref{ssec:hcp} gives the HCP brain-graph maximum-symmetry null.
     9	For each domain we report
    10	$A_{d} = \mathrm{Acc}_{\mathrm{sub}, d} - \mathrm{Acc}_{\mathrm{raw}, d}$
    11	or, in the HCP case,
    12	$Z_{m} = (m_{\mathrm{ARIA}} - \mu_{\mathrm{HCP}})/\sigma_{\mathrm{HCP}}$.
    13	Numbers are lifted verbatim from
    14	\texttt{docs/brain\_mapping/CROSS\_DOMAIN\_RESULTS.md}.
    15	
    16	\subsection{Chess pattern recognition (P9--P13)}\label{ssec:chess}
    17	
    18	\textbf{Setup.} $32$ chess positions across $4$ categories (tactical,
    19	positional, endgame, opening). Per-position $8$-dimensional V2
    20	features (material balance, king safety, pawn structure, centre
    21	control, piece activity, mobility, threat density, defensive
    22	structure), normalised by per-feature $L^{2}$ norms. Substrate
    23	routing: features injected as pressure into the $S^{7}$ observer
    24	frames; substrate run forward by $n_{\mathrm{ticks}}$; resulting
    25	vertex pattern used as classifier feature vector. Classifier:
    26	1-nearest-neighbour on cosine similarity, validated by $5$-fold CV
    27	or leave-one-out (LOO).
    28	
    29	\textbf{Critical methodological detail.} Between successive depth
    30	measurements the substrate is reset to canonical state via
    31	\texttt{mon.homeostatic\_reset(level=1.0)}. Without this, pressure-
    32	field state drifts toward equilibrium across $\sim 5$ evaluations
    33	and classification structure collapses to raw-feature baseline.
    34	
    35	\begin{table}[ht]
    36	\centering
    37	\small
    38	\caption{Chess substrate-routed depth sweep with state reset between
    39	measurements.}
    40	\label{tab:chess_depth}
    41	\begin{tabular}{r r}
    42	\toprule
    43	$n_{\mathrm{ticks}}$ & accuracy \\
    44	\midrule
    45	$5$    & $53.1\%$ \\
    46	$15$   & $65.6\%$ \\
    47	$\mathbf{25}$  & $\mathbf{93.8\%}$ ($\leftarrow$ peak) \\
    48	$40$   & $84.4\%$ \\
    49	$60$   & $84.4\%$ \\
    50	$100$  & $78.1\%$ \\
    51	\bottomrule
    52	\end{tabular}
    53	\end{table}
    54	
    55	\begin{table}[ht]
    56	\centering
    57	\small
    58	\caption{Chess preregistered tests (with reset, $n=25$ canonical
    59	depth).}
    60	\label{tab:chess_prereg}
    61	\begin{tabular}{l l l l l}
    62	\toprule
    63	ID & Test & Threshold & Observed & Verdict \\
    64	\midrule
    65	P9  & 5-fold CV (seeds 30200--30204)        & $\geq 70\%$ & $83.1\%$ & $\checkmark$ \\
    66	P10 & null perm. mapping (chess, 15 perms)$^{\dagger}$  & $\geq 50\%$ & $65.4\%$ & $\checkmark$ \\
    67	P11 & random-label baseline (20 trials)     & $\in[15\%, 35\%]$ & $23.4\%$ & $\checkmark$ \\
    68	P12 & goldilocks peak depth                 & $\in\{15,25,40,60\}$ & $n=25$ & $\checkmark$ \\
    69	\textbf{P13} & substrate lift, LOO refinement (with reset)$^{\ddagger}$ & $\geq +15$pp & $\mathbf{+40.6}$pp (LOO) & $\checkmark$ \\
    70	\bottomrule
    71	\end{tabular}
    72	\end{table}
    73	
    74	$^{\dagger}$ The 2026-04-18 preregistration P16 specified the null
    75	permutation test as ``$\geq 50\%$ on \emph{both} chess and
    76	conversation''; we present the chess and conversation null mappings
    77	separately as P10 (chess) and P16 (conversation) for table clarity.
    78	Both pass.
    79	
    80	$^{\ddagger}$ The 2026-04-18 preregistration P13 specified the chess
    81	substrate-lift estimator as $5$-fold CV at threshold $\geq +15$pp.
    82	The 2026-04-29 validation tightened the estimator to LOO with state
    83	reset; we report the LOO finding ($+40.6$pp) above as a stricter
    84	validation-protocol refinement at the unchanged $+15$pp threshold,
    85	not a preregistration revision.
    86	
    87	\textbf{Reading.} Substrate routing amplifies chess-position
    88	4-category classification from raw $53.1\%$ (just above $25\%$
    89	chance) to substrate-routed $93.8\%$ at canonical depth $n=25$.
    90	This is a $+40.6$pp lift on the LOO refinement; on the preregistered
    91	$5$-fold CV estimator the substrate-routed accuracy is $83.1\%$
    92	(P9), itself well above any reasonable raw-features baseline.
    93	The original 2026-04-20 validation reported the LOO lift at
    94	$+3.1$pp, a state-drift artefact closed by the reset protocol
    95	(\S\ref{sec:method}).
    96	
    97	\textbf{Permutation null decomposition.} The null permutation
    98	mapping (P10) randomises the feature$\to$frame assignment, so each
    99	feature is routed to a different $S^{7}$ frame than canonical. The
   100	substrate retains $65.4\%$ classification accuracy under random
   101	permutation — well above the $25\%$ chance level for $4$ categories.
   102	We read this as a substrate-witness decomposition:
   103	$\sim 65$pp of classification power is \emph{architectural} (it
   104	persists when feature$\to$frame assignment is randomised; it is the
   105	H$_4$-symmetric amplifier acting on whatever input lands in the
   106	frames), and the remaining $\sim 17$pp is the semantic-alignment
   107	bonus. We do not claim this decomposition is unique; it is a
   108	description of the observed accuracy stack.
   109	
   110	\subsection{Conversation neutrality (P14--P16)}\label{ssec:conv}
   111	
   112	\textbf{Setup.} $64$ utterances across $8$ dialogue-act categories.
   113	$8$-dimensional injection-row features per utterance. Identical
   114	substrate routing pipeline to chess.
   115	
   116	\begin{table}[ht]
   117	\centering
   118	\small
   119	\caption{Conversation preregistered tests.}
   120	\label{tab:conv_prereg}
   121	\begin{tabular}{l l l l l}
   122	\toprule
   123	ID & Test & Threshold & Observed & Verdict \\
   124	\midrule
   125	P14 & raw 5-fold CV (seeds 30220--30224)    & $\geq 75\%$ & $87.5\%$ & $\checkmark$ \\
   126	P15 & substrate lift                         & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
   127	P16 & null perm. mapping (15 perms)         & $\geq 50\%$ & $70.6\%$ & $\checkmark$ \\
   128	\bottomrule
   129	\end{tabular}
   130	\end{table}
   131	
   132	\textbf{Reading.} Conversation raw features at $87.5\%$ are already
   133	strongly discriminative (cf.\ chess raw $\sim 53\%$); the substrate
   134	lift is $-4.4$pp, well within the preregistered neutrality band
   135	$|\cdot|\!<\!10$pp. The substrate is correctly null on conversation.
   136	
   137	\textbf{Selective amplifier signature.} The pair (chess
   138	$+40.6$pp lift; conversation $-4.4$pp lift) is consistent with the
   139	selective-amplifier behaviour preregistered in 2026-04-18: in these
   140	two tasks, the architecture amplifies when raw features are ambiguous
   141	(chess raw $\sim 53\%$) and is approximately neutral when raw features
   142	are already saturated (conversation raw $87.5\%$). We do not claim
   143	this generalises to all classification tasks; cross-domain transfer
   144	to additional ambiguous-feature benchmarks is an open build
   145	(\S\ref{sec:limitations}).
   146	
   147	\subsection{HCP brain-graph maximum-symmetry null
   148	            (P17--P18)}\label{ssec:hcp}
   149	
   150	\textbf{Setup.} Reference cohort: Human Connectome Project (HCP)
   151	$n=1003$ subjects~\citep{VanEssen2013HCP}; preregistered tests on
   152	$n=100$ subjects for computational tractability, with full-cohort
   153	$n=1003$ descriptive statistics also reported. ICA-50 group-averaged
   154	connectivity matrix; thresholded at the same density as ARIA's
   155	vertex graph ($\rho=0.101$). Compare degree distribution and
   156	higher-order graph statistics. ARIA reference: $G_{V_{600}}$ with
   157	$\Lop$. By H$_4$ transitivity (Lemma~\ref{lem:600cell}) every vertex
   158	has identical local structure $\Rightarrow$ uniform degree $12$
   159	$\Rightarrow$ degree std $= 0$ as a theorem.
   160	
   161	\begin{table}[ht]
   162	\centering
   163	\small
   164	\caption{HCP comparison: preregistered $n=100$ test plus full-cohort
   165	$n=1003$ descriptive statistics.}
   166	\label{tab:hcp}
   167	\begin{tabular}{l r r r}
   168	\toprule
   169	Metric & ARIA & HCP $n=1003$ mean (sd) & $\sigma$ from HCP \\
   170	\midrule
   171	Degree std (preregistered, $n=100$ subset) & $0.000$ & $3.388$ ($> 2.0$) & --- \\
   172	Degree std (descriptive, $n=1003$)         & $0.000$ & $3.28\pm 0.28$ & $-11.58\sigma$ \\
   173	Participation ratio (descriptive)          & $68.54$ & $19.72\pm 0.61$ & $+79.78\sigma$ \\
   174	Clustering coefficient (descriptive)       & $0.455$ & $0.220$ & $+6.80\sigma$ \\
   175	\bottomrule
   176	\end{tabular}
   177	\end{table}
   178	
   179	\begin{itemize}\itemsep=2pt
   180	\item P17 (ARIA degree std, theorem): predicted $=0$, observed
   181	  $0.0000$, $\checkmark$.
   182	\item P18 (HCP ICA-50 degree std, $n=100$ density-matched):
   183	  predicted $> 2.0$, observed $3.388$, $\checkmark$. Zero of $1003$
   184	  HCP subjects have degree std below $2.0$.
   185	\end{itemize}
   186	
   187	\textbf{Reading (substrate witness).} ARIA's H$_4$-transitive
   188	structure is a deterministic group-theoretic null reference for
   189	cortical functional connectivity. Real cortex breaks the symmetry
   190	through hub-spoke functional specialisation; the $\sigma$-distances
   191	quantify the magnitude of biological symmetry-breaking with no
   192	fitted parameters. The $\sigma$-distances ($-11.58\sigma$ on degree
   193	homogeneity, $+79.78\sigma$ on participation ratio, $+6.80\sigma$ on
   194	clustering coefficient) are large on the ICA-50 pipeline at the
   195	density-matched threshold $\rho = 0.101$; cross-parcellation
   196	replication (Schaefer, Glasser) remains an open build.
   197	
   198	\textbf{Participation-ratio comparability.} ARIA's vertex graph has
   199	$120$ nodes; the HCP ICA-50 connectivity matrix has $50$ nodes. The
   200	participation-ratio statistic
   201	$\mathrm{PR}(G) = (\sum_{i} d_{i})^{2} / \sum_{i} d_{i}^{2}$ is
   202	node-count-dependent — its theoretical maximum is the node count of
   203	the graph. We report the raw $\mathrm{PR}$ values
   204	($\mathrm{ARIA}=68.54$ on a 120-node graph; $\mathrm{HCP}=19.72$ on a
   205	50-node graph) and the $\sigma$-distance against the HCP
   206	across-subject distribution, but the $+79.78\sigma$ value reflects
   207	both the architectural difference and the differing node counts. A
   208	node-count-normalised statistic
   209	$\mathrm{PR}/|V|$ gives $\mathrm{ARIA}=0.571$ vs $\mathrm{HCP}=0.394$,
   210	a smaller absolute gap; we keep the raw-PR comparison as headline
   211	because the HCP subject distribution and the across-subject
   212	$\sigma$ are computed in the same units, but flag the node-count
   213	caveat here.
   214	
   215	\textbf{What we do not claim.}
   216	\begin{itemize}\itemsep=2pt
   217	\item We do not claim cortex has ``drifted from an ideal polytope'';
   218	  the substrate is a useful a-priori null whose deviation from real
   219	  cortex is precisely measurable.
   220	\item We do not claim parcellation invariance: the $\sigma$-distances
   221	  are reported on ICA-50; alternative parcellations (Schaefer,
   222	  Glasser) would give different per-metric numbers but, on the
   223	  basis of the qualitative pattern that cortex is hub-concentrated
   224	  relative to ARIA's transitive null, we expect them to preserve the
   225	  signs. Verification across parcellations is an open build
   226	  (\S\ref{sec:limitations}).
   227	\end{itemize}
   228	
   229	\subsection{Cross-domain summary as a selective amplifier
   230	            \texorpdfstring{$+$}{+} maximum-symmetry null}
   231	
   232	\begin{table}[ht]
   233	\centering
   234	\small
   235	\caption{Cross-domain summary on a single substrate.}
   236	\label{tab:cross_domain_summary}
   237	\begin{tabular}{l r r r r r}
   238	\toprule
   239	Task & Raw & Substrate & Null perm. & Geom.\ floor & Sem.\ alignment \\
   240	\midrule
   241	Chess (LOO, $n=25$, w/ reset) & $53.1\%$ & $93.8\%$ & --- & --- & $+40.6$pp lift \\
   242	Chess (5-fold CV)             & ---      & $83.1\%$ & $65.4\%$ & $65.4\%$ & $+17.7$pp \\
   243	Conversation (5-fold CV)      & $87.5\%$ & $83.1\%$ & $70.6\%$ & $70.6\%$ & $+12.5$pp (raw vs null) \\
   244	\bottomrule
   245	\end{tabular}
   246	\end{table}
   247	
   248	The geometric content ($\approx 65$--$71\%$ across the two domains)
   249	is the architecture-invariant null floor. The semantic content
   250	($12$--$18$pp) is the domain-specific contribution. On HCP,
   251	$\sigma$-distances against the biological cohort are
   252	$(-11.58, +79.78, +6.80)$ on (degree std, participation ratio,
   253	clustering coefficient).
   254	
   255	\textbf{Headline cross-domain reading.} The substrate is
   256	\emph{selectively} amplifying (not unconditionally), and it is a
   257	maximum-symmetry deterministic null on connectivity (not a fitted
   258	model). Both readings sit inside the substrate-witness scope.

exec
/bin/bash -lc "printf '%s\\n' '---05 86-180---'; nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex' | sed -n '86,180p'; printf '%s\\n' '---07 1-146---'; nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex' | sed -n '1,146p'; printf '%s\\n' '---08---'; nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex' | sed -n '1,180p'; printf '%s\\n' '---09---'; nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/09_limitations.tex' | sed -n '1,220p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 260ms:
---05 86-180---
    86	\subsection{Eighteen preregistered correspondences}\label{ssec:eighteen_prereg}
    87	
    88	\textbf{Tally.} $17/18$ at standard validation
    89	(\texttt{run\_preregistered\_validation.py}, $5$-seed cascade block
    90	plus state-reset protocol); $18/18$ after the $N\!=\!20$ deep-dive
    91	on the residual P4 (\texttt{demo\_p4\_cxp\_deep\_dive.py}, seed range
    92	$32000$--$32019$). \emph{No preregistered threshold has been modified.}
    93	
    94	\begin{table}[ht]
    95	\centering
    96	\small
    97	\caption{All eighteen preregistered correspondences, frozen 2026-04-18.}
    98	\label{tab:eighteen_prereg}
    99	\begin{tabular}{l l l l l}
   100	\toprule
   101	ID & Test & Threshold & Observed (2026-04-29) & Verdict \\
   102	\midrule
   103	P1  & Cascade $\alpha$ SOC range            & $\in [2.5, 3.5]$ & $2.958$ & $\checkmark$ \\
   104	P2  & $C$ main effect                        & $\geq +0.30$     & $+0.621$ & $\checkmark$ \\
   105	P3  & $|D{\times}C|$ (independence)          & $|\cdot| < 0.20$ & $-0.183$ ($N\!=\!5$) & $\checkmark$ \\
   106	\textbf{P4} & $C{\times}P$ synergy           & $\geq +0.10$     &
   107	   $+0.190$ \, CI $[+0.143, +0.239]$ ($N\!=\!20$) & $\checkmark$ \\
   108	P5  & $|E|$ main effect (null)               & $|\cdot| < 0.15$ & $+0.046$ & $\checkmark$ \\
   109	P6  & Real EEG $\alpha$                      & $\in [2.0, 3.0]$ & $2.513$ & $\checkmark$ \\
   110	P7  & W$\!\to\!$N3 variance ratio            & $< 0.70$         & $0.365$ & $\checkmark$ \\
   111	P8  & W$\!\to\!$N3 switching ratio           & $< 0.50$         & $0.058$ & $\checkmark$ \\
   112	P9  & Chess 5-fold CV                        & $\geq 70\%$      & $83.1\%$ & $\checkmark$ \\
   113	P10 & Chess null mapping                     & $\geq 50\%$      & $65.4\%$ & $\checkmark$ \\
   114	P11 & Chess random-label                     & $\in [15\%, 35\%]$ & $23.4\%$ & $\checkmark$ \\
   115	P12 & Chess goldilocks peak                  & $\in \{15, 25, 40, 60\}$ & $n=25$ & $\checkmark$ \\
   116	\textbf{P13} & Chess substrate lift (5-fold CV preregistered; LOO refinement, with reset) & $\geq +15$pp & $+40.6$pp (LOO) & $\checkmark$ \\
   117	P14 & Conv raw 5-fold CV                     & $\geq 75\%$      & $87.5\%$ & $\checkmark$ \\
   118	P15 & $|$conv lift$|$                        & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
   119	P16 & Conv null mapping                      & $\geq 50\%$      & $70.6\%$ & $\checkmark$ \\
   120	P17 & ARIA degree std (theorem)              & $= 0$            & $0.0000$ & $\checkmark$ \\
   121	P18 & HCP degree std                         & $> 2.0$          & $3.388$ & $\checkmark$ \\
   122	\bottomrule
   123	\end{tabular}
   124	\end{table}
   125	
   126	\textbf{Three predictions that flipped to PASS, with documented
   127	methodology refinement (no threshold change).}
   128	\begin{itemize}\itemsep=2pt
   129	\item P3 (D$\times$C interaction independence) was outside the band
   130	  at $N\!=\!3$ ($-0.231$) and inside the band at $N\!=\!5$ ($-0.183$).
   131	  Reading: consistent with an underpowered interaction estimate at
   132	  $N\!=\!3$ on a high-per-seed-variance interaction term.
   133	\item P4 (C$\times$P synergy) was below threshold at $N\!=\!3$
   134	  ($+0.044$) and at $N\!=\!5$ ($+0.039$); the $N\!=\!20$ deep-dive
   135	  (\S\ref{sec:stress}) gives $+0.190$ with $95\%$ CI
   136	  $[+0.143, +0.239]$, decisively above the $\geq +0.10$ floor.
   137	\item P13 (chess substrate lift): the 2026-04-18 preregistration
   138	  (\texttt{PAPER\_PREDICTIONS.md:115-120}) specified the estimator as
   139	  $5$-fold CV with threshold $\geq +15$pp at $n=25$. The 2026-04-29
   140	  validation strengthened the estimator to LOO with state reset, a
   141	  stricter test at the same threshold; the LOO lift was $+3.1$pp
   142	  without state reset on a state-drifted substrate, and $+40.6$pp
   143	  with \texttt{homeostatic\_reset(level=1.0)} between depth measurements
   144	  (\S\ref{sec:method}; \texttt{NON\_EQUILIBRIUM\_FINDING.md}). We
   145	  report this as a \emph{validation-protocol refinement on the
   146	  preregistered estimator}, not as preregistration revision.
   147	\end{itemize}
   148	
   149	\textbf{Headline verdict.} Eighteen preregistered correspondences
   150	all pass at preregistered thresholds, with two interaction tests
   151	requiring $N\!\geq\!5$ and one requiring $N\!=\!20$ for reliable
   152	detection of high-variance interaction terms, and one test
   153	requiring the documented state-reset protocol. The original $15/18$
   154	result was a methodology-limited tally, not a content failure.
   155	
   156	\subsection{Three-way \texorpdfstring{$\alpha$}{alpha} overlap}\label{ssec:alpha_overlap}
   157	
   158	The substrate's wake cascade-$\alpha$ confidence interval overlaps
   159	\emph{three independent reference ranges} simultaneously:
   160	
   161	\begin{table}[ht]
   162	\centering
   163	\small
   164	\caption{Three-way $\alpha$ overlap on the wake cascade-event power
   165	law.}
   166	\label{tab:alpha_overlap}
   167	\begin{tabular}{l c l c}
   168	\toprule
   169	Source & $\alpha$ & 95\% CI & $n$ \\
   170	\midrule
   171	ARIA cascade-pipeline baseline ($N=5$) & $2.958$  & inside $[2.5, 3.5]$ & 5 seeds \\
   172	Real EEG (Sleep-EDFx, $n=30$ subjects)~\citep{SleepEDFx} & $2.51$ & $[2.50, 2.53]$ & 30 \\
   173	ARIA prior cascade pipeline ($n=4$ subjects) & $2.85$ & $[2.73, 3.25]$ & per-subject \\
   174	\textbf{v4 WAKE consciousness chain} & $\mathbf{2.252}$ & $[\mathbf{1.82, 2.86}]$ & 58 events \\
   175	\bottomrule
   176	\end{tabular}
   177	\end{table}
   178	
   179	The v4 WAKE 95\% CI $[1.82, 2.86]$ contains the upper arm of the
   180	real Sleep-EDFx EEG CI $[2.50, 2.53]$, overlaps the ARIA prior
---07 1-146---
     1	% =====================================================================
     2	\section{Cross-domain selectivity}\label{sec:cross_domain}
     3	% =====================================================================
     4	
     5	This section reports three cross-domain witnesses. \S\ref{ssec:chess}
     6	gives the chess pattern-recognition lift. \S\ref{ssec:conv} gives the
     7	conversation neutrality result that confirms the lift is selective.
     8	\S\ref{ssec:hcp} gives the HCP brain-graph maximum-symmetry null.
     9	For each domain we report
    10	$A_{d} = \mathrm{Acc}_{\mathrm{sub}, d} - \mathrm{Acc}_{\mathrm{raw}, d}$
    11	or, in the HCP case,
    12	$Z_{m} = (m_{\mathrm{ARIA}} - \mu_{\mathrm{HCP}})/\sigma_{\mathrm{HCP}}$.
    13	Numbers are lifted verbatim from
    14	\texttt{docs/brain\_mapping/CROSS\_DOMAIN\_RESULTS.md}.
    15	
    16	\subsection{Chess pattern recognition (P9--P13)}\label{ssec:chess}
    17	
    18	\textbf{Setup.} $32$ chess positions across $4$ categories (tactical,
    19	positional, endgame, opening). Per-position $8$-dimensional V2
    20	features (material balance, king safety, pawn structure, centre
    21	control, piece activity, mobility, threat density, defensive
    22	structure), normalised by per-feature $L^{2}$ norms. Substrate
    23	routing: features injected as pressure into the $S^{7}$ observer
    24	frames; substrate run forward by $n_{\mathrm{ticks}}$; resulting
    25	vertex pattern used as classifier feature vector. Classifier:
    26	1-nearest-neighbour on cosine similarity, validated by $5$-fold CV
    27	or leave-one-out (LOO).
    28	
    29	\textbf{Critical methodological detail.} Between successive depth
    30	measurements the substrate is reset to canonical state via
    31	\texttt{mon.homeostatic\_reset(level=1.0)}. Without this, pressure-
    32	field state drifts toward equilibrium across $\sim 5$ evaluations
    33	and classification structure collapses to raw-feature baseline.
    34	
    35	\begin{table}[ht]
    36	\centering
    37	\small
    38	\caption{Chess substrate-routed depth sweep with state reset between
    39	measurements.}
    40	\label{tab:chess_depth}
    41	\begin{tabular}{r r}
    42	\toprule
    43	$n_{\mathrm{ticks}}$ & accuracy \\
    44	\midrule
    45	$5$    & $53.1\%$ \\
    46	$15$   & $65.6\%$ \\
    47	$\mathbf{25}$  & $\mathbf{93.8\%}$ ($\leftarrow$ peak) \\
    48	$40$   & $84.4\%$ \\
    49	$60$   & $84.4\%$ \\
    50	$100$  & $78.1\%$ \\
    51	\bottomrule
    52	\end{tabular}
    53	\end{table}
    54	
    55	\begin{table}[ht]
    56	\centering
    57	\small
    58	\caption{Chess preregistered tests (with reset, $n=25$ canonical
    59	depth).}
    60	\label{tab:chess_prereg}
    61	\begin{tabular}{l l l l l}
    62	\toprule
    63	ID & Test & Threshold & Observed & Verdict \\
    64	\midrule
    65	P9  & 5-fold CV (seeds 30200--30204)        & $\geq 70\%$ & $83.1\%$ & $\checkmark$ \\
    66	P10 & null perm. mapping (chess, 15 perms)$^{\dagger}$  & $\geq 50\%$ & $65.4\%$ & $\checkmark$ \\
    67	P11 & random-label baseline (20 trials)     & $\in[15\%, 35\%]$ & $23.4\%$ & $\checkmark$ \\
    68	P12 & goldilocks peak depth                 & $\in\{15,25,40,60\}$ & $n=25$ & $\checkmark$ \\
    69	\textbf{P13} & substrate lift, LOO refinement (with reset)$^{\ddagger}$ & $\geq +15$pp & $\mathbf{+40.6}$pp (LOO) & $\checkmark$ \\
    70	\bottomrule
    71	\end{tabular}
    72	\end{table}
    73	
    74	$^{\dagger}$ The 2026-04-18 preregistration P16 specified the null
    75	permutation test as ``$\geq 50\%$ on \emph{both} chess and
    76	conversation''; we present the chess and conversation null mappings
    77	separately as P10 (chess) and P16 (conversation) for table clarity.
    78	Both pass.
    79	
    80	$^{\ddagger}$ The 2026-04-18 preregistration P13 specified the chess
    81	substrate-lift estimator as $5$-fold CV at threshold $\geq +15$pp.
    82	The 2026-04-29 validation tightened the estimator to LOO with state
    83	reset; we report the LOO finding ($+40.6$pp) above as a stricter
    84	validation-protocol refinement at the unchanged $+15$pp threshold,
    85	not a preregistration revision.
    86	
    87	\textbf{Reading.} Substrate routing amplifies chess-position
    88	4-category classification from raw $53.1\%$ (just above $25\%$
    89	chance) to substrate-routed $93.8\%$ at canonical depth $n=25$.
    90	This is a $+40.6$pp lift on the LOO refinement; on the preregistered
    91	$5$-fold CV estimator the substrate-routed accuracy is $83.1\%$
    92	(P9), itself well above any reasonable raw-features baseline.
    93	The original 2026-04-20 validation reported the LOO lift at
    94	$+3.1$pp, a state-drift artefact closed by the reset protocol
    95	(\S\ref{sec:method}).
    96	
    97	\textbf{Permutation null decomposition.} The null permutation
    98	mapping (P10) randomises the feature$\to$frame assignment, so each
    99	feature is routed to a different $S^{7}$ frame than canonical. The
   100	substrate retains $65.4\%$ classification accuracy under random
   101	permutation — well above the $25\%$ chance level for $4$ categories.
   102	We read this as a substrate-witness decomposition:
   103	$\sim 65$pp of classification power is \emph{architectural} (it
   104	persists when feature$\to$frame assignment is randomised; it is the
   105	H$_4$-symmetric amplifier acting on whatever input lands in the
   106	frames), and the remaining $\sim 17$pp is the semantic-alignment
   107	bonus. We do not claim this decomposition is unique; it is a
   108	description of the observed accuracy stack.
   109	
   110	\subsection{Conversation neutrality (P14--P16)}\label{ssec:conv}
   111	
   112	\textbf{Setup.} $64$ utterances across $8$ dialogue-act categories.
   113	$8$-dimensional injection-row features per utterance. Identical
   114	substrate routing pipeline to chess.
   115	
   116	\begin{table}[ht]
   117	\centering
   118	\small
   119	\caption{Conversation preregistered tests.}
   120	\label{tab:conv_prereg}
   121	\begin{tabular}{l l l l l}
   122	\toprule
   123	ID & Test & Threshold & Observed & Verdict \\
   124	\midrule
   125	P14 & raw 5-fold CV (seeds 30220--30224)    & $\geq 75\%$ & $87.5\%$ & $\checkmark$ \\
   126	P15 & substrate lift                         & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
   127	P16 & null perm. mapping (15 perms)         & $\geq 50\%$ & $70.6\%$ & $\checkmark$ \\
   128	\bottomrule
   129	\end{tabular}
   130	\end{table}
   131	
   132	\textbf{Reading.} Conversation raw features at $87.5\%$ are already
   133	strongly discriminative (cf.\ chess raw $\sim 53\%$); the substrate
   134	lift is $-4.4$pp, well within the preregistered neutrality band
   135	$|\cdot|\!<\!10$pp. The substrate is correctly null on conversation.
   136	
   137	\textbf{Selective amplifier signature.} The pair (chess
   138	$+40.6$pp lift; conversation $-4.4$pp lift) is consistent with the
   139	selective-amplifier behaviour preregistered in 2026-04-18: in these
   140	two tasks, the architecture amplifies when raw features are ambiguous
   141	(chess raw $\sim 53\%$) and is approximately neutral when raw features
   142	are already saturated (conversation raw $87.5\%$). We do not claim
   143	this generalises to all classification tasks; cross-domain transfer
   144	to additional ambiguous-feature benchmarks is an open build
   145	(\S\ref{sec:limitations}).
   146	
---08---
     1	% =====================================================================
     2	\section{Discussion}\label{sec:discussion}
     3	% =====================================================================
     4	
     5	This section reads the substrate-witness result against existing
     6	theories of consciousness, identifies what is novel here that is not
     7	a re-statement of an earlier theory, and proposes a non-load-bearing
     8	ACT bridge to the companion adaptive-closure-transport
     9	preprint~\citep{SmartAdaptiveClosureTransport2026}. We do not claim a
    10	selection theorem, we do not claim a Lyapunov derivation, and we do
    11	not claim the recurrent layer ``is'' consciousness.
    12	
    13	\subsection{What is novel in this work}
    14	
    15	Three things are claimed novel as a substrate witness:
    16	\begin{enumerate}\itemsep=2pt
    17	\item \textbf{A geometry-fixed substrate that is consistent with
    18	  real-cortex EEG signatures without fitted shape parameters on neural
    19	  data.} The 600-cell + H$_4$ symmetry is fixed by group theory once
    20	  the substrate is chosen; cascade-$\alpha$ matches Sleep-EDFx within
    21	  preregistered tolerance with pairwise CI overlap on three reference
    22	  ranges; six drug/sleep signatures pass at published-reference
    23	  thresholds on a single deterministic substrate. We are not aware of
    24	  a prior geometric substrate that has been tested against this many
    25	  preregistered cortical correspondences from a graph fixed by group
    26	  theory; we cannot rule out that such a model exists.
    27	\item \textbf{The strong-coupling architectural finding.} $C$ and $P$
    28	  are strongly coupled cascade-state stabilisers, not
    29	  nearly-orthogonal ones. The $C\!\times\!P$ interaction
    30	  ($+0.190$, $95\%$ CI $[+0.143, +0.239]$ at $N\!=\!20$) is comparable
    31	  in magnitude to the $P$ main effect ($-0.218$). This was hidden by
    32	  underpowered ablation and emerged only at $N\!\geq\!20$ — a
    33	  substantive correction to the architectural reading from the
    34	  original 3-seed validation.
    35	\item \textbf{The 18/18 preregistered correspondences with no
    36	  threshold modification.} Every prediction in the preregistered set
    37	  passes at the preregistered thresholds. The two interaction tests
    38	  (P3, P4) required $N\!\geq\!5$ and $N\!\geq\!20$ respectively, and
    39	  one test (P13) required the documented state-reset protocol. We
    40	  report this transparently as methodology refinement, not as
    41	  threshold change.
    42	\end{enumerate}
    43	
    44	\subsection{Comparison to existing theories of consciousness}
    45	
    46	\textbf{vs IIT.}~\citep{Tononi2008,BalduzziTononi2008} ARIA produces
    47	IIT-direction-correct $\Phi$ collapse on propofol ($0.33\!\times$
    48	wake). The H$_4$-equivariance argument
    49	(\S\ref{sec:chain}) makes $\Phi\to 0$ when dynamics are
    50	group-symmetric, and $\Phi > 0$ only when dynamics break symmetry.
    51	ARIA does not implement the full IIT axioms (cause-effect repertoires,
    52	exclusion postulate, integration-over-partitions); it reproduces the
    53	observable consequence on the propofol--wake state contrast. This is
    54	a consistency-of-direction result, not a discharge of IIT.
    55	
    56	\textbf{vs Global Workspace Theory.}~\citep{Baars1988GWT,Dehaene2014ConsciousAndBrain}
    57	The $S^{7}$ context-rotation mechanism (\S\ref{sec:chain}) is
    58	functionally analogous to a workspace with rotating attentional
    59	selection; the active observer frame plays the role of a temporary
    60	in-workspace subset of features. ARIA does not commit to the GWT
    61	broadcast/access distinction at the architectural level; the
    62	analogy is descriptive.
    63	
    64	\textbf{vs Predictive Processing.}~\citep{FristonFreeEnergy2010,ClarkPP2013}
    65	ARIA does not implement prediction-error minimisation or hierarchical
    66	generative models.
    67	The recurrent self-model layer ($\eta\!=\!0.20$) provides top-down
    68	modulation of the substrate response by cosine direction alignment
    69	with the prior phenomenal snapshot, not by learned prediction errors.
    70	Predictive-processing-style refinements (e.g.\ $\eta$ as an adaptive
    71	learning rate over a prediction-error norm) are an open build, not
    72	delivered here.
    73	
    74	\textbf{vs neural mass models.} ARIA operates at the
    75	architectural-algorithmic level; it does not specify which neural
    76	circuits implement context rotation or partial emission. The 600-cell
    77	substrate is proposed as an abstract description of the criticality-
    78	maintaining structure of cortex, not as a circuit model.
    79	
    80	\subsection{The non-load-bearing ACT bridge}\label{ssec:act_bridge}
    81	
    82	The companion adaptive-closure-transport
    83	preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
    84	4-tuple bridge
    85	$(M, L_{M}, W, R_{\mathrm{hom}})$ — substrate $M$, response operator
    86	$L_{M}$, learnable Hebbian-like field $W$, and a homeostatic
    87	regulariser $R_{\mathrm{hom}}$. We propose the dictionary
    88	$D_{\mathrm{ACT}}$:
    89	\[
    90	D_{\mathrm{ACT}}\colon (M, L_{M}, W, R_{\mathrm{hom}})
    91	\;\longmapsto\;
    92	(\Rsixhundred,\ \Cph,\ \text{cascade pressure field}\ W_{\mathrm{p}},
    93	   \ \texttt{homeostatic\_reset}).
    94	\]
    95	\textbf{This bridge is non-load-bearing for the present paper.} It is
    96	included as a route-K (alternative-route) reading; the substrate-
    97	witness claims (six signatures, $18/18$, chess $+40.6$pp,
    98	HCP $\sigma$-distances) do not require any of the ACT theorems.
    99	
   100	\textbf{What ACT would have to deliver to make this load-bearing.}
   101	The companion preprint identifies four open builds, each of which is
   102	deferred:
   103	\begin{itemize}\itemsep=2pt
   104	\item A Lyapunov function $V(W)$ on the reduced flow whose
   105	  monotonicity proves selection — not delivered.
   106	\item An edge-space decomposition of $\mathbb{R}^{E_{M}}$ under the
   107	  Hodge edge Laplacian $L_{\mathrm{edge}} = \delta_{2}\delta_{2}^{\mathsf T} +
   108	  \delta_{1}^{\mathsf T}\delta_{1}$ — not delivered.
   109	\item A formal $2I$-equivariance audit of the closure operator
   110	  family — not delivered.
   111	\item A full reduced-flow convergence theorem on
   112	  $W$-trajectories — not delivered.
   113	\end{itemize}
   114	Until these are delivered, ARIA is positioned as the empirical
   115	\emph{substrate witness} for the family that ACT names; ACT is not the
   116	selection-theorem witness for ARIA. The companion kernel
   117	document~\citep{SmartAriaClosureKernel2026} discusses the same $\Cph$
   118	in a passive-regime witness via the $B\to K^{*}\mu^{+}\mu^{-}$ flavour
   119	anomaly~\citep{SmartBAnomaly2026}; that line shares operator-level
   120	infrastructure with this paper, but does not transfer empirical
   121	support for ARIA.
   122	
   123	\subsection{The strong-coupling reading for cortical architecture}
   124	
   125	Real cortical criticality is maintained by multiple parallel
   126	mechanisms: E/I balance, neuromodulation (acetylcholine, noradrenaline),
   127	homeostatic plasticity, gain control. The naive expectation — and the
   128	one we held until the $N\!=\!20$ deep-dive — is that these are mostly
   129	orthogonal, so losing one removes only its own main effect. The
   130	$N\!=\!20$ result reverses this on the substrate: $C$ and $P$ are
   131	strongly coupled. Disabling one cascades into losing the synergistic
   132	contribution of the other.
   133	
   134	This matches clinical observations: anaesthesia (which targets
   135	GABAergic transmission) and seizure (which targets E/I balance)
   136	produce widespread network-level dysfunction beyond their direct
   137	targets — exactly what strong synergy predicts. We position this as
   138	\emph{a hypothesis the substrate witness raises}, not as a proof.
   139	The bridge from cascade-mechanism interaction on $\Rsixhundred$ to
   140	real-cortex pharmacological coupling is a step we do not take in
   141	this paper.
   142	
   143	\subsection{Methodological contributions}
   144	
   145	Two methodological items are worth recording outside the headline:
   146	\begin{enumerate}\itemsep=2pt
   147	\item \textbf{$N\!\geq\!20$ for high-variance interaction terms.}
   148	  Allocation discipline for preregistration: when preregistering an
   149	  interaction effect on a system with unknown per-seed variance,
   150	  budget for $N\!\geq\!20$ from the start. The original 3-seed plan
   151	  was the source of two underpowered-interaction estimates in this work.
   152	\item \textbf{State-reset protocol on non-stationary substrates.}
   153	  ARIA's substrate is a non-stationary dynamical system; the
   154	  pressure field equilibrates within $\sim 5$ successive evaluations.
   155	  Any multi-trial benchmark must specify a state-reset protocol or
   156	  document the drift. Generalisable lesson: \emph{published
   157	  cross-domain benchmarks on non-stationary substrates should report
   158	  an explicit reset/equilibration discipline}, not just seed.
   159	\end{enumerate}
   160	
   161	\subsection{The substrate as a maximum-symmetry connectivity null}
   162	
   163	The HCP comparison (\S\ref{ssec:hcp}) places ARIA as a principled
   164	deterministic null reference for cortical functional connectivity.
   165	Real cortex breaks the symmetry through hub-spoke functional
   166	specialisation; the $\sigma$-distances from ARIA quantify the
   167	magnitude of biological symmetry-breaking with no fitted parameters.
   168	
   169	This is a methodological contribution to comparative connectomics.
   170	Stochastic nulls (Erd\H{o}s--R\'enyi, configuration model,
   171	edge-randomised graphs) compare cortex to a random graph with matched
   172	density. ARIA is a different kind of null: a deterministic
   173	group-theoretic graph with theorem-level statements of structure
   174	(degree std $=\!0$ by transitivity, eigenvalue spectrum
   175	$\{0, 3, 4\Ph, 6\Ph, 12{-}4\Ph, 12{-}6\Ph, 9, 12\}$ by character
   176	theory). Both null kinds are useful; ARIA gives a specific,
   177	reproducible, group-theoretic baseline that cortex deviates from in
   178	quantifiable $\sigma$-units.
   179	
   180	\subsection{Open questions raised by the substrate witness}
---09---
     1	% =====================================================================
     2	\section{Limitations and hostile-review guard matrix}\label{sec:limitations}
     3	% =====================================================================
     4	
     5	This section enumerates limitations transparently, organised as a
     6	five-move guard matrix following the b-anomaly preprint
     7	template~\citep{SmartBAnomaly2026}: regime, post-hoc, interpretation,
     8	test/claim, state-drift. For each guard we record
     9	$G\colon \mathrm{risk} \to (\mathrm{disclosure}, \mathrm{evidence},
    10	\mathrm{strengthening\ build})$.
    11	
    12	\subsection{Regime}\label{ssec:regime}
    13	
    14	\textbf{Single substrate (the 600-cell).} We have not tested whether
    15	other regular 4-polytopes ($24$-cell, $120$-cell) would produce
    16	comparable correspondences. The 600-cell was chosen because its
    17	H$_4$ Coxeter cascade structure aligns with the empirical signatures
    18	that motivated this paper, not from an a-priori derivation.
    19	\emph{Disclosure:} substrate-witness scope, no uniqueness claim
    20	(\S\ref{sec:intro}). \emph{Evidence:} empirical correspondences hold
    21	on $\Rsixhundred$. \emph{Strengthening build:} formal ablation against
    22	$\{24\text{-cell}, 120\text{-cell}\}$ on the same six-signature
    23	battery and the eighteen preregistered tests, with thresholds
    24	preserved.
    25	
    26	\textbf{Single-seed determinism on the recurrent layer.} The v4
    27	six-signature results in~\S\ref{ssec:six_signatures} are reported on
    28	a single deterministic trajectory at seed $42$. Empirical CIs across
    29	$10$--$20$ cross-seed runs would strengthen the per-signature claims
    30	beyond the single-trajectory bootstrap of $58$ events that gives the
    31	WAKE 95\% CI $[1.82, 2.86]$. \emph{Disclosure:} explicitly single-seed
    32	in~\S\ref{sec:method} and~\S\ref{ssec:six_signatures}.
    33	\emph{Evidence:} bootstrap CI on the wake 58 events, plus three-way
    34	overlap with two independent reference $\alpha$ ranges.
    35	\emph{Strengthening build:} 10--20 cross-seed runs of
    36	\texttt{demo\_drug\_sleep\_v4.py}, with per-signature bootstrap CIs.
    37	
    38	\textbf{Stylised stimulus models on the recurrent layer.} The v4
    39	stimulus models for WAKE (AR(1) noise + tonic shell + attention
    40	episodes), SLEEP\_N3 (slow oscillation + spindles + K-complexes),
    41	and PROPOFOL (low-amplitude tonic noise) are biologically motivated
    42	but abstract: a single shell anchor for tonic coherence, fixed
    43	$40$-tick period for slow-wave drive, etc. Real spatial structure of
    44	cortical input is much richer. \emph{Disclosure:}~\S\ref{sec:chain}
    45	``deliberately structural rather than measurement-fitted''.
    46	\emph{Evidence:} models match published biological time scales but
    47	are not tuned to specific signatures. \emph{Strengthening build:}
    48	replication on stimulus models derived from anatomically-grounded
    49	input statistics (e.g.\ retinotopic, tonotopic).
    50	
    51	\subsection{Post-hoc}\label{ssec:posthoc}
    52	
    53	\textbf{The 600-cell choice is post-hoc justified by empirical
    54	observables.} While the construction of $\Rsixhundred$ is theorem-
    55	level rigorous (H$_4$ Coxeter group theory), the choice of \emph{this}
    56	polytope as the consciousness-substrate instance is motivated by the
    57	correspondences observed, not by an a-priori biological argument.
    58	\emph{Disclosure:}~\S\ref{sec:intro}, ``substrate witness, not
    59	derivation; not a uniqueness claim''. \emph{Evidence:} the eighteen
    60	preregistered correspondences plus six signatures; the H$_4$
    61	transitivity theorem ($P17$). \emph{Strengthening build:} comparison
    62	with the $24$-cell and $120$-cell on the same signatures; formal
    63	ACT-selection-theorem witness via the bridge of~\S\ref{ssec:act_bridge}
    64	(deferred).
    65	
    66	\textbf{Cascade decomposition is one of several possible
    67	decompositions of H$_4$.} We use the $\sigma$-orbit projector basis
    68	because it is machine-precise and biologically informative, but other
    69	bases (character-theoretic, Galois-twin) give the same physical
    70	predictions through different intermediate variables. \emph{Disclosure:}
    71	\S\ref{ssec:cascade} acknowledges non-uniqueness of decomposition.
    72	\emph{Evidence:} block-diagonalisation at $<10^{-15}$ cross-block
    73	norm. \emph{Strengthening build:} catalogue and equivalence-prove the
    74	admissible decompositions.
    75	
    76	\textbf{$\Ph^{-2}$ floor not derived.} The shifted-Laplacian floor
    77	$\Ph^{-2}\!\approx\!0.382$ is a stability clamp making $\Cph$
    78	strictly positive definite (\S\ref{ssec:cphi}); it is not derived
    79	from a closure functional or symmetry argument. \emph{Disclosure:}
    80	\S\ref{ssec:cphi} marks this as a design-level choice; the companion
    81	kernel doc~\citep{SmartAriaClosureKernel2026} explicitly does not
    82	derive it. \emph{Evidence:} the same operator (with the same shift)
    83	serves as the basis for the b-anomaly passive-regime
    84	witness~\citep{SmartBAnomaly2026}. \emph{Strengthening build:}
    85	derive the $\Ph^{-2}$ shift as the unique stability clamp under a
    86	named regularity criterion.
    87	
    88	\subsection{Interpretation}\label{ssec:interpretation}
    89	
    90	\textbf{The recurrent layer is a method, not a metaphysics claim.}
    91	We do not claim the recurrent self-model layer ``is'' consciousness;
    92	we claim quantitative consistency with six published biological
    93	signatures on a deterministic trajectory. \emph{Disclosure:}
    94	\S\ref{sec:intro}, \S\ref{sec:chain} (``method, not metaphysics'').
    95	\emph{Evidence:} six signatures vs published thresholds.
    96	\emph{Strengthening build:} cross-seed CIs (\S\ref{ssec:regime}); a
    97	formal account of which substrate observables map to which phenomenal
    98	contents (the bind\_phenomenal\_field channels) is not delivered.
    99	
   100	\textbf{$\Phi$ is an IIT-style direction-of-effect proxy, not a full
   101	IIT discharge.} \emph{Disclosure:}~\S\ref{sec:chain} explicitly.
   102	\emph{Evidence:} propofol $\Phi$ collapse to $0.33\!\times$ wake
   103	matches IIT direction. \emph{Strengthening build:} a
   104	\texttt{phi\_iit\_full} implementation following Balduzzi--Tononi
   105	2008~\citep{BalduzziTononi2008} on the substrate; not delivered.
   106	
   107	\textbf{HCP $\sigma$-distances are descriptive, not normative.} We
   108	do not claim ``cortex has drifted from an ideal polytope''; we
   109	quantify the distance between cortex and the deterministic H$_4$ null.
   110	\emph{Disclosure:}~\S\ref{ssec:hcp} explicitly. \emph{Evidence:}
   111	$\sigma$-distances on three independent metrics. \emph{Strengthening
   112	build:} cross-parcellation replication (Schaefer, Glasser).
   113	
   114	\subsection{Test/claim}\label{ssec:testclaim}
   115	
   116	\textbf{Two preregistered interaction tests required higher $N$
   117	than originally allocated.} P3 closes at $N\!=\!5$; P4 closes only at
   118	$N\!=\!20$. We document this transparently as a Type II
   119	methodology issue, not a threshold change. \emph{Disclosure:}
   120	\S\ref{sec:method}, \S\ref{sec:results}, \S\ref{sec:stress}.
   121	\emph{Evidence:} bootstrap CI fully above the $+0.10$ floor; per-seed
   122	distribution narrow at $N\!=\!20$ ($\mathrm{std}=0.089$);
   123	$19/20$ seeds positive. \emph{Strengthening build:} a second
   124	$N\!=\!20$ run at a different seed range (e.g.\ $33000$--$33019$);
   125	an $N\!=\!50$ characterisation of the per-seed distribution.
   126	
   127	\textbf{The original 2026-04-20 walks-back are reversed without
   128	threshold modification.} The reversals (P3, P4, P13) are documented
   129	in
   130	\texttt{docs/brain\_mapping/VALIDATION\_RESULTS\_2026-04-29.md} with
   131	the original failure values, the methodology refinement, and the
   132	post-refinement values. \emph{Disclosure:} this paper carries those
   133	disclosures verbatim. \emph{Evidence:} 2026-04-20 vs 2026-04-29 side-
   134	by-side results table. \emph{Strengthening build:} the strengthening
   135	builds for P3/P4/P13 above; no further claim is needed.
   136	
   137	\textbf{Bayesian and full-IIT inference not performed.} All intervals
   138	are frequentist (bootstrap CIs); $\Phi$ is the direction-of-effect
   139	proxy, not the Balduzzi--Tononi 2008 algorithm. \emph{Disclosure:}
   140	this section. \emph{Strengthening build:} Bayesian posterior on
   141	$\Delta_{CP}$; full-IIT computation on the $S^{4}\!\to\!2^{4}$
   142	substrate state space. The latter is computationally heavy and is
   143	deferred.
   144	
   145	\subsection{State-drift / out-of-scope}\label{ssec:scope}
   146	
   147	\textbf{Single condition-dependent parameter $\eta$ is not derived
   148	as a learned variable.} $\eta\in\{0, 0.05, 0.20\}$ across PROPOFOL,
   149	SLEEP\_N3, and WAKE/RECOVERY is a condition-dependent constant in
   150	this paper, not a learned trajectory. A predictive-processing
   151	extension where $\eta$ adapts on an error norm is an open build.
   152	
   153	\textbf{No deuteron / hadron / RH / capstone material is loaded into
   154	this paper.} The companion programme (cascade-derivation, capstone
   155	coalgebra, RH formal) shares operator-level infrastructure but is not
   156	load-bearing here. Deliberately out of scope.
   157	
   158	\textbf{Out-of-scope items NOT delivered (correctly).}
   159	\begin{itemize}\itemsep=2pt
   160	\item Aria-chess active-regime companion analysis on chess move-by-move
   161	  trajectories (this paper covers static positions only).
   162	\item Edge-space decomposition of $\mathbb{R}^{E_{M}}$ under
   163	  $2I$-equivariance — open build of the ACT companion paper.
   164	\item Lyapunov derivation $V(W)$ from a closure functional
   165	  $\mathcal{F}$ — open build of the ACT companion paper.
   166	\item Selection theorem for $\Rsixhundred$ over alternative regular
   167	  4-polytopes — see~\S\ref{ssec:regime}.
   168	\item Cross-cohort EEG (TUH, NHM, OpenNeuro non-propofol) replication
   169	  of the six signatures.
   170	\item Cross-parcellation replication of the HCP $\sigma$-distances
   171	  (Schaefer, Glasser, etc.).
   172	\item Bayesian posterior on the C$\times$P interaction.
   173	\end{itemize}
   174	
   175	\subsection{The honest verdict}
   176	
   177	The result is a substrate witness: a geometry-fixed substrate, with
   178	no shape parameters tuned to any neural dataset, is consistent with
   179	eighteen preregistered correspondences and six independent drug/sleep
   180	EEG signatures, with all original gaps closed by methodology
   181	refinement and without modifying any preregistered threshold. We do
   182	not claim the substrate \emph{is} consciousness. We do not claim a
   183	selection theorem on the ACT bridge. We do not claim uniqueness for
   184	$\Rsixhundred$ among regular 4-polytopes. The strengthening builds
   185	for these stronger claims are listed above and remain open.

exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/07_cross_domain.tex' | sed -n '1,180p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 377ms:
     1	% =====================================================================
     2	\section{Cross-domain selectivity}\label{sec:cross_domain}
     3	% =====================================================================
     4	
     5	This section reports three cross-domain witnesses. \S\ref{ssec:chess}
     6	gives the chess pattern-recognition lift. \S\ref{ssec:conv} gives the
     7	conversation neutrality result that confirms the lift is selective.
     8	\S\ref{ssec:hcp} gives the HCP brain-graph maximum-symmetry null.
     9	For each domain we report
    10	$A_{d} = \mathrm{Acc}_{\mathrm{sub}, d} - \mathrm{Acc}_{\mathrm{raw}, d}$
    11	or, in the HCP case,
    12	$Z_{m} = (m_{\mathrm{ARIA}} - \mu_{\mathrm{HCP}})/\sigma_{\mathrm{HCP}}$.
    13	Numbers are lifted verbatim from
    14	\texttt{docs/brain\_mapping/CROSS\_DOMAIN\_RESULTS.md}.
    15	
    16	\subsection{Chess pattern recognition (P9--P13)}\label{ssec:chess}
    17	
    18	\textbf{Setup.} $32$ chess positions across $4$ categories (tactical,
    19	positional, endgame, opening). Per-position $8$-dimensional V2
    20	features (material balance, king safety, pawn structure, centre
    21	control, piece activity, mobility, threat density, defensive
    22	structure), normalised by per-feature $L^{2}$ norms. Substrate
    23	routing: features injected as pressure into the $S^{7}$ observer
    24	frames; substrate run forward by $n_{\mathrm{ticks}}$; resulting
    25	vertex pattern used as classifier feature vector. Classifier:
    26	1-nearest-neighbour on cosine similarity, validated by $5$-fold CV
    27	or leave-one-out (LOO).
    28	
    29	\textbf{Critical methodological detail.} Between successive depth
    30	measurements the substrate is reset to canonical state via
    31	\texttt{mon.homeostatic\_reset(level=1.0)}. Without this, pressure-
    32	field state drifts toward equilibrium across $\sim 5$ evaluations
    33	and classification structure collapses to raw-feature baseline.
    34	
    35	\begin{table}[ht]
    36	\centering
    37	\small
    38	\caption{Chess substrate-routed depth sweep with state reset between
    39	measurements.}
    40	\label{tab:chess_depth}
    41	\begin{tabular}{r r}
    42	\toprule
    43	$n_{\mathrm{ticks}}$ & accuracy \\
    44	\midrule
    45	$5$    & $53.1\%$ \\
    46	$15$   & $65.6\%$ \\
    47	$\mathbf{25}$  & $\mathbf{93.8\%}$ ($\leftarrow$ peak) \\
    48	$40$   & $84.4\%$ \\
    49	$60$   & $84.4\%$ \\
    50	$100$  & $78.1\%$ \\
    51	\bottomrule
    52	\end{tabular}
    53	\end{table}
    54	
    55	\begin{table}[ht]
    56	\centering
    57	\small
    58	\caption{Chess preregistered tests (with reset, $n=25$ canonical
    59	depth).}
    60	\label{tab:chess_prereg}
    61	\begin{tabular}{l l l l l}
    62	\toprule
    63	ID & Test & Threshold & Observed & Verdict \\
    64	\midrule
    65	P9  & 5-fold CV (seeds 30200--30204)        & $\geq 70\%$ & $83.1\%$ & $\checkmark$ \\
    66	P10 & null perm. mapping (chess, 15 perms)$^{\dagger}$  & $\geq 50\%$ & $65.4\%$ & $\checkmark$ \\
    67	P11 & random-label baseline (20 trials)     & $\in[15\%, 35\%]$ & $23.4\%$ & $\checkmark$ \\
    68	P12 & goldilocks peak depth                 & $\in\{15,25,40,60\}$ & $n=25$ & $\checkmark$ \\
    69	\textbf{P13} & substrate lift, LOO refinement (with reset)$^{\ddagger}$ & $\geq +15$pp & $\mathbf{+40.6}$pp (LOO) & $\checkmark$ \\
    70	\bottomrule
    71	\end{tabular}
    72	\end{table}
    73	
    74	$^{\dagger}$ The 2026-04-18 preregistration P16 specified the null
    75	permutation test as ``$\geq 50\%$ on \emph{both} chess and
    76	conversation''; we present the chess and conversation null mappings
    77	separately as P10 (chess) and P16 (conversation) for table clarity.
    78	Both pass.
    79	
    80	$^{\ddagger}$ The 2026-04-18 preregistration P13 specified the chess
    81	substrate-lift estimator as $5$-fold CV at threshold $\geq +15$pp.
    82	The 2026-04-29 validation tightened the estimator to LOO with state
    83	reset; we report the LOO finding ($+40.6$pp) above as a stricter
    84	validation-protocol refinement at the unchanged $+15$pp threshold,
    85	not a preregistration revision.
    86	
    87	\textbf{Reading.} Substrate routing amplifies chess-position
    88	4-category classification from raw $53.1\%$ (just above $25\%$
    89	chance) to substrate-routed $93.8\%$ at canonical depth $n=25$.
    90	This is a $+40.6$pp lift on the LOO refinement; on the preregistered
    91	$5$-fold CV estimator the substrate-routed accuracy is $83.1\%$
    92	(P9), itself well above any reasonable raw-features baseline.
    93	The original 2026-04-20 validation reported the LOO lift at
    94	$+3.1$pp, a state-drift artefact closed by the reset protocol
    95	(\S\ref{sec:method}).
    96	
    97	\textbf{Permutation null decomposition.} The null permutation
    98	mapping (P10) randomises the feature$\to$frame assignment, so each
    99	feature is routed to a different $S^{7}$ frame than canonical. The
   100	substrate retains $65.4\%$ classification accuracy under random
   101	permutation — well above the $25\%$ chance level for $4$ categories.
   102	We read this as a substrate-witness decomposition:
   103	$\sim 65$pp of classification power is \emph{architectural} (it
   104	persists when feature$\to$frame assignment is randomised; it is the
   105	H$_4$-symmetric amplifier acting on whatever input lands in the
   106	frames), and the remaining $\sim 17$pp is the semantic-alignment
   107	bonus. We do not claim this decomposition is unique; it is a
   108	description of the observed accuracy stack.
   109	
   110	\subsection{Conversation neutrality (P14--P16)}\label{ssec:conv}
   111	
   112	\textbf{Setup.} $64$ utterances across $8$ dialogue-act categories.
   113	$8$-dimensional injection-row features per utterance. Identical
   114	substrate routing pipeline to chess.
   115	
   116	\begin{table}[ht]
   117	\centering
   118	\small
   119	\caption{Conversation preregistered tests.}
   120	\label{tab:conv_prereg}
   121	\begin{tabular}{l l l l l}
   122	\toprule
   123	ID & Test & Threshold & Observed & Verdict \\
   124	\midrule
   125	P14 & raw 5-fold CV (seeds 30220--30224)    & $\geq 75\%$ & $87.5\%$ & $\checkmark$ \\
   126	P15 & substrate lift                         & $|\cdot| < 10$pp & $-4.4$pp & $\checkmark$ \\
   127	P16 & null perm. mapping (15 perms)         & $\geq 50\%$ & $70.6\%$ & $\checkmark$ \\
   128	\bottomrule
   129	\end{tabular}
   130	\end{table}
   131	
   132	\textbf{Reading.} Conversation raw features at $87.5\%$ are already
   133	strongly discriminative (cf.\ chess raw $\sim 53\%$); the substrate
   134	lift is $-4.4$pp, well within the preregistered neutrality band
   135	$|\cdot|\!<\!10$pp. The substrate is correctly null on conversation.
   136	
   137	\textbf{Selective amplifier signature.} The pair (chess
   138	$+40.6$pp lift; conversation $-4.4$pp lift) is consistent with the
   139	selective-amplifier behaviour preregistered in 2026-04-18: in these
   140	two tasks, the architecture amplifies when raw features are ambiguous
   141	(chess raw $\sim 53\%$) and is approximately neutral when raw features
   142	are already saturated (conversation raw $87.5\%$). We do not claim
   143	this generalises to all classification tasks; cross-domain transfer
   144	to additional ambiguous-feature benchmarks is an open build
   145	(\S\ref{sec:limitations}).
   146	
   147	\subsection{HCP brain-graph maximum-symmetry null
   148	            (P17--P18)}\label{ssec:hcp}
   149	
   150	\textbf{Setup.} Reference cohort: Human Connectome Project (HCP)
   151	$n=1003$ subjects~\citep{VanEssen2013HCP}; preregistered tests on
   152	$n=100$ subjects for computational tractability, with full-cohort
   153	$n=1003$ descriptive statistics also reported. ICA-50 group-averaged
   154	connectivity matrix; thresholded at the same density as ARIA's
   155	vertex graph ($\rho=0.101$). Compare degree distribution and
   156	higher-order graph statistics. ARIA reference: $G_{V_{600}}$ with
   157	$\Lop$. By H$_4$ transitivity (Lemma~\ref{lem:600cell}) every vertex
   158	has identical local structure $\Rightarrow$ uniform degree $12$
   159	$\Rightarrow$ degree std $= 0$ as a theorem.
   160	
   161	\begin{table}[ht]
   162	\centering
   163	\small
   164	\caption{HCP comparison: preregistered $n=100$ test plus full-cohort
   165	$n=1003$ descriptive statistics.}
   166	\label{tab:hcp}
   167	\begin{tabular}{l r r r}
   168	\toprule
   169	Metric & ARIA & HCP $n=1003$ mean (sd) & $\sigma$ from HCP \\
   170	\midrule
   171	Degree std (preregistered, $n=100$ subset) & $0.000$ & $3.388$ ($> 2.0$) & --- \\
   172	Degree std (descriptive, $n=1003$)         & $0.000$ & $3.28\pm 0.28$ & $-11.58\sigma$ \\
   173	Participation ratio (descriptive)          & $68.54$ & $19.72\pm 0.61$ & $+79.78\sigma$ \\
   174	Clustering coefficient (descriptive)       & $0.455$ & $0.220$ & $+6.80\sigma$ \\
   175	\bottomrule
   176	\end{tabular}
   177	\end{table}
   178	
   179	\begin{itemize}\itemsep=2pt
   180	\item P17 (ARIA degree std, theorem): predicted $=0$, observed

exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex' | sed -n '1,220p'; printf '%s\\n' '---03---'; nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex' | sed -n '1,220p'; printf '%s\\n' '---04 1-160---'; nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex' | sed -n '1,160p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 304ms:
     1	% =====================================================================
     2	\section{Stress test: the C\texorpdfstring{$\times$}{x}P synergy at adequate
     3	         replication}\label{sec:stress}
     4	% =====================================================================
     5	
     6	This section is the C$\times$P interaction stress test. The original
     7	preregistered prediction was P4: $C\times P$ interaction
     8	$\Delta_{CP} \geq +0.10$ on cascade-$\alpha$. The 2026-04-20
     9	$N\!=\!3$ validation gave $+0.044$ — below the threshold — and the
    10	architectural claim ``C and P synergise on cascade-state stability''
    11	was walked back. Closing this gap without modifying the preregistered
    12	threshold required (a) re-evaluating the $N\!=\!3$ point estimate as
    13	consistent with an underpowered interaction estimate, (b) tracking
    14	the estimate's behaviour across $N$, and (c) bootstrapping a
    15	confidence interval on a fresh-seed $N\!=\!20$ sample. We did all
    16	three.
    17	
    18	\subsection{The factorial estimator}
    19	
    20	For the four ablation conditions $\{----, -C--, --P-, -CP-\}$
    21	(\S\ref{sec:chain}), the $C\times P$ interaction estimate is the
    22	standard $2\times 2$ factorial difference:
    23	\[
    24	\Delta_{CP}
    25	\;=\;\frac{(\alpha_{\!-CP\!-}+\alpha_{\!-\!-\!-\!-})
    26	        - (\alpha_{\!-C\!-\!-}+\alpha_{\!-\!-P\!-})}{2}.
    27	\]
    28	Per-seed paired estimates use the same formula on a single seed's
    29	four conditions.
    30	
    31	\subsection{The trend across \texorpdfstring{$N$}{N}}
    32	
    33	\begin{table}[ht]
    34	\centering
    35	\small
    36	\caption{$C\times P$ interaction estimate as a function of $N$.}
    37	\label{tab:cxp_trend}
    38	\begin{tabular}{r l r l l}
    39	\toprule
    40	$N$ & Seeds & Estimate $\Delta_{CP}$ & 95\% CI & Verdict vs $\geq +0.10$ \\
    41	\midrule
    42	$3$  & $30040$--$30042$ & $+0.044$ & --- & $\times$ original prereg \\
    43	$5$  & $30040$--$30044$ & $+0.039$ & --- & $\times$ this session re-run \\
    44	$10$ & $31000$--$31009$ & $+0.088$ & $[-0.002, +0.174]$ & borderline \\
    45	$\mathbf{20}$ & $\mathbf{32000\text{--}32019}$ & $\mathbf{+0.190}$
    46	       & $\mathbf{[+0.143, +0.239]}$ & $\checkmark$ decisively above \\
    47	\bottomrule
    48	\end{tabular}
    49	\end{table}
    50	
    51	The estimate remains small at $N\!=\!3$ and $N\!=\!5$
    52	($+0.044, +0.039$) and rises at $N\!=\!10$ and $N\!=\!20$
    53	($+0.088, +0.190$). Per-seed std at $N\!=\!10$ was $0.159$; at
    54	$N\!=\!20$ it dropped to $0.089$ — the $N\!=\!10$ sample landed on
    55	outliers; the $N\!=\!20$ sample reveals a clean narrow positive
    56	distribution.
    57	
    58	\subsection{The \texorpdfstring{$N\!=\!20$}{N=20} fresh-seed estimate}
    59	
    60	\textbf{Setup.} $4$ conditions $\times$ $20$ fresh seeds (range
    61	$32000$--$32019$, non-overlapping with original validation seeds in
    62	the $30000$s), $150$ epochs per run. All other ablation flags off
    63	($D, E$ held on). Bootstrap $n_{\mathrm{resamples}}\!=\!2000$,
    64	seed $42$. Wallclock $1706$\,s on a single CPU
    65	(\texttt{demo\_p4\_cxp\_deep\_dive.py}).
    66	
    67	\textbf{Per-condition means at \texorpdfstring{$N\!=\!20$}{N=20}.}
    68	
    69	\begin{table}[ht]
    70	\centering
    71	\small
    72	\caption{Per-condition mean $\alpha$ at $N=20$ fresh seeds.}
    73	\label{tab:cxp_means}
    74	\begin{tabular}{l r r r}
    75	\toprule
    76	condition & mean $\alpha$ & std & sem \\
    77	\midrule
    78	$----$ baseline    & $3.008$ & $0.090$ & $0.020$ \\
    79	$-C--$ (C off)     & $3.464$ & $0.097$ & $0.022$ \\
    80	$--P-$ (P off)     & $2.790$ & $0.086$ & $0.019$ \\
    81	$-CP-$ (both off)  & $3.628$ & $0.161$ & $0.036$ \\
    82	\bottomrule
    83	\end{tabular}
    84	\end{table}
    85	
    86	\textbf{Main effects at \texorpdfstring{$N\!=\!20$}{N=20}.}
    87	$C$ main effect $= +0.456$ (turning $C$ off raises $\alpha$);
    88	$P$ main effect $= -0.218$ (turning $P$ off lowers $\alpha$).
    89	
    90	\textbf{Interaction estimate.} Direct calculation from means:
    91	\[
    92	\Delta_{CP} \;=\; \frac{(3.628 + 3.008) - (3.464 + 2.790)}{2}
    93	            \;=\; +0.191.
    94	\]
    95	Bootstrap on the 20-seed sample (2000 resamples):
    96	\begin{itemize}\itemsep=1pt
    97	\item bootstrap mean $\Delta_{CP} = +0.190$;
    98	\item 95\% bootstrap CI $[+0.143, +0.239]$;
    99	\item $0/2000$ bootstrap resamples were at or below zero, reported as
   100	      $0.0000$;
   101	\item $0/2000$ bootstrap resamples were below the preregistered
   102	      $+0.10$ floor, reported as $0.0000$.
   103	\end{itemize}
   104	
   105	\textbf{Per-seed paired distribution.}
   106	$19/20$ seeds give a positive paired-interaction estimate (range
   107	$+0.055$ to $+0.322$); a single seed gives $-0.009$. No seed gives a
   108	strongly negative interaction.
   109	
   110	\subsection{Reading and disclosure}
   111	
   112	\textbf{The 95\% CI is entirely above the preregistered $+0.10$
   113	threshold} on a fresh-seed sample. $0/2000$ bootstrap resamples were
   114	at or below zero, reported as $0.0000$; $0/2000$ bootstrap resamples
   115	were below the preregistered $+0.10$ floor, reported as $0.0000$.
   116	
   117	\textbf{Architectural reading (substrate witness).} $C$ creates churn
   118	in \emph{which} vertices are uncrossed (frame rotation churns the
   119	uncrossed pool). $P$ promotes the high-pressure subset of the
   120	uncrossed pool to mini-emitters. The product is a non-additive
   121	novel-event-generation pathway: with both on, the uncrossed pool
   122	churns and $P$ amplifies new vertices entering the high-pressure
   123	region; with either off, the pathway collapses. The interaction
   124	$+0.19$ is comparable in magnitude to the $P$ main effect $-0.22$,
   125	so $C$ and $P$ are \emph{strongly coupled} cascade-state stabilisers
   126	on this substrate, not nearly-orthogonal ones. This reverses an
   127	architectural claim from the original 3-seed validation that held $C$
   128	and $P$ approximately orthogonal.
   129	
   130	\textbf{Disclosure: $N\!=\!20$ ordering.} The $N\!=\!20$ deep-dive
   131	was conducted \emph{after} the original $N\!=\!3$ failure
   132	(2026-04-29 vs 2026-04-20). The seed range $32000$--$32019$ was
   133	selected to be non-overlapping with the original $30000$s seeds.
   134	Two strengthening builds we have not delivered:
   135	(i) a second independent $N\!=\!20$ run at a different seed range
   136	(e.g.\ $33000$--$33019$), and
   137	(ii) an $N\!=\!50$ characterisation of the per-seed sample
   138	distribution. Both are recorded as open builds in
   139	\S\ref{sec:limitations}.
   140	
   141	\textbf{What this stress test does \emph{not} establish.}
   142	\begin{itemize}\itemsep=2pt
   143	\item It does not establish a Lyapunov function on the reduced flow.
   144	\item It does not establish that the substrate is uniquely selected by
   145	  $C\times P$ coupling among regular 4-polytopes.
   146	\item It does not establish an $\eta$-trajectory derivation; $\eta$
   147	  is treated as a condition-dependent constant in this paper.
   148	\end{itemize}
   149	The stress test is what its name says: a high-replication factorial
   150	test of one preregistered interaction prediction, on a fresh-seed
   151	sample, with bootstrap confidence intervals. The architectural reading
   152	is a \emph{description} of what $C$ and $P$ do on the substrate, not a
   153	theorem about why they do it.
   154	
   155	\subsection{Methodological contribution}
   156	
   157	We document, as a methodological contribution to preregistration
   158	practice, that interaction terms in cascade ablation matrices require
   159	$N\!\geq\!20$ fresh seeds for reliable detection when the
   160	interaction-to-main-effect ratio is below $0.5$. The original 3-seed
   161	preregistered validation gave estimates consistent with underpowered
   162	detection on both interaction tests (P3 and P4); both close at higher
   163	$N$ without threshold modification. For preregistration design more broadly:
   164	when preregistering an interaction effect on a system with unknown
   165	per-seed variance, allocate the seed count from a power-analysis
   166	assumption that the per-seed std could be as large as the interaction
   167	effect itself. Under that assumption, $N\!\geq\!20$ is the conservative
   168	minimum.
---03---
     1	% =====================================================================
     2	\section{The 600-cell response substrate}\label{sec:substrate}
     3	% =====================================================================
     4	
     5	This section constructs the substrate. \S\ref{ssec:vertices}
     6	gives the vertex set. \S\ref{ssec:graph} gives the graph and its
     7	H$_4$-symmetry-forced spectrum. \S\ref{ssec:cphi} gives the response
     8	operator $\Cph$ and the $\Ph^{-2}$ stability clamp.
     9	\S\ref{ssec:shells} gives the 9-shell decomposition used for source
    10	projection. \S\ref{ssec:cascade} sketches the seven-rung cascade
    11	descent referenced by the recurrent layer in~\S\ref{sec:chain}. None
    12	of these objects depend on neural data.
    13	
    14	\subsection{Vertex construction}\label{ssec:vertices}
    15	
    16	The 600-cell $\Rsixhundred$ has $120$ vertices in
    17	$\mathbb{R}^{4}$~\citep{CoxeterRegularPolytopes,Weisstein600Cell}.
    18	With $\Ph = (1+\sqrt 5)/2$ the canonical vertex set is
    19	\begin{itemize}\itemsep=1pt
    20	\item $8$ vertices: all permutations of $(\pm 1, 0, 0, 0)$;
    21	\item $16$ vertices: all sign combinations of
    22	  $(\pm 1, \pm 1, \pm 1, \pm 1)/2$;
    23	\item $96$ vertices: all even permutations of
    24	  $(\pm \Ph, \pm 1, \pm 1/\Ph, 0)/2$.
    25	\end{itemize}
    26	All $120$ vertices lie on the unit $3$-sphere $S^{3}$. The H$_4$
    27	Coxeter group acts transitively on the vertex set; in particular,
    28	every vertex has identical local structure. Implementation:
    29	\texttt{kernel/vfd\_closure\_kernel.py:build\_600cell\_vertices}.
    30	
    31	\subsection{Graph and Laplacian spectrum}\label{ssec:graph}
    32	
    33	The substrate graph $G_{V_{600}} = (V, E)$ is built by connecting each
    34	vertex to its nearest neighbours under the Euclidean metric on $S^{3}$.
    35	H$_4$ acts transitively on the vertex set, forcing uniformity of the
    36	local structure; the eigenvalue multiplicities follow from H$_4$
    37	character theory on the regular representation. The construction and
    38	spectrum are standard~\citep{CoxeterRegularPolytopes,Weisstein600Cell}.
    39	\begin{lemma}[600-cell graph facts]\label{lem:600cell}
    40	The graph $G_{V_{600}}$ has $|V|=120$ vertices, $|E|=720$ edges, every
    41	vertex has degree exactly $12$, and the unweighted graph Laplacian
    42	$\Lop = D - A$ has spectrum
    43	\[
    44	\sigma(\Lop) \;=\;
    45	\bigl\{0^{1}, 3^{4}, 4\Ph^{9}, 6\Ph^{16}, (12\!-\!4\Ph)^{9},
    46	       (12\!-\!6\Ph)^{16}, 9^{4}, 12^{1}\bigr\},
    47	\]
    48	where the exponent denotes multiplicity. The decomposition into H$_4$
    49	irreducible representations is exact at machine precision; the
    50	$\sigma$-orbit projector basis (\texttt{kernel/sigma\_orbit\_basis.py})
    51	realises it block-by-block with cross-block norm $<10^{-15}$.
    52	\end{lemma}
    53	
    54	The non-trivial eigenmodes partition into Coxeter exponent classes.
    55	For H$_4$ proper, the exponents are $\{1, 11, 19, 29\}$; for the
    56	Galois twin $\sigma(\mathrm{H}_4)$ under the $\sigma$-automorphism of
    57	$\mathbb{Z}[\Ph]$, the exponents become $\{7, 13, 17, 23\}$. We label
    58	the eigenspaces $K_{1}, K_{11}, K_{19}, K_{29}$ for H$_4$-proper modes
    59	and $K_{7}, K_{13}, K_{17}, K_{23}$ for $\sigma$-twin modes. The
    60	multiplicities follow from character theory and are reproduced in
    61	the implementation
    62	(\texttt{kernel/sigma\_orbit\_basis.py:\_self\_test}). The
    63	$K_{7}$-modes will be the dominant phenomenal-binding profile in
    64	\S\ref{sec:chain}.
    65	
    66	\subsection{The shifted-Laplacian response \texorpdfstring{$\Cph$}{C\_phi}}\label{ssec:cphi}
    67	
    68	The substrate's linear response to an external source $f \in \mathbb{R}^{120}$
    69	is the discrete Green's function of the shifted Laplacian:
    70	\begin{equation}\label{eq:cphi}
    71	\Cph \;=\; \Lop + \Ph^{-2} I,
    72	\qquad
    73	\psi \;=\; \Cph^{-1} f.
    74	\end{equation}
    75	The shift $\Ph^{-2} \approx 0.382$ is a design-level stability
    76	clamp: it makes $\Cph$ strictly positive definite (smallest eigenvalue
    77	$\Ph^{-2}$, since the trivial Laplacian eigenvalue is $0$), so that the
    78	inverse is bounded with operator norm $\Ph^{2}\approx 2.618$. This is
    79	\emph{not} a derived theorem; it is a stability choice. The companion
    80	kernel document~\citep{SmartAriaClosureKernel2026} discusses the same
    81	$\Cph$ as the basis for an independent passive-regime witness in
    82	flavour physics~\citep{SmartBAnomaly2026}, where the same operator
    83	form (without retuning the shift) describes the
    84	$B\to K^{*}\mu^{+}\mu^{-}$ angular anomaly across five public datasets.
    85	This paper imports $\Cph$ from that line; we do not re-derive it.
    86	
    87	The response $\psi = \Cph^{-1} f$ is smooth in $f$. By itself it does
    88	not produce critical-state cascade statistics; the recurrent layer
    89	in~\S\ref{sec:chain} adds a graph-pinned nonlinearity
    90	$\mathrm{bounded\_topk}(\psi, k\!=\!12)$ to obtain self-organised-critical
    91	event distributions. The choice $k\!=\!12$ is the average degree of
    92	$G_{V_{600}}$ (Lemma~\ref{lem:600cell}), pinned by the substrate, not
    93	fitted to any dataset.
    94	
    95	\paragraph{Disclosure (substrate-witness scope).}
    96	The $\Ph^{-2}$ floor is a stability shift, not a derived parameter.
    97	The bounded-top-$K$ nonlinearity uses $k\!=\!12$ pinned to the graph's
    98	average degree, not a fitted threshold. No other shape parameter
    99	enters. The condition-dependent self-injection coupling
   100	$\eta\in\{0, 0.05, 0.20\}$ is the only architectural parameter that
   101	varies between conditions in~\S\ref{sec:chain}; it is reported
   102	explicitly per condition.
   103	
   104	\subsection{Shell decomposition}\label{ssec:shells}
   105	
   106	Under the H$_3$ subgroup, the $120$ vertices partition into $9$
   107	spherical shells indexed by Euclidean inner product with a chosen pole:
   108	\[
   109	\bigl(|S_0|,\ldots,|S_8|\bigr) \;=\; (1, 12, 20, 12, 30, 12, 20, 12, 1).
   110	\]
   111	The middle shell $S_{4}$ has $30$ vertices on the equatorial plane
   112	(the icosidodecahedral ring). When projecting onto a continuum kernel
   113	in companion preprints~\citep{SmartAriaClosureKernel2026}, the
   114	shell-mean projection of the equatorial-source response,
   115	$\kappa(x) = \mathrm{shell\text{-}mean}[\Cph^{-1} f_{\mathrm{equat}}](x)$,
   116	collapses on the continuum exponential $\frac{\Ph}{2}\,e^{-|x|/\Ph}$.
   117	This paper does not use that continuum projection; we work with the
   118	discrete operator throughout.
   119	
   120	\subsection{Cascade descent (sketch)}\label{ssec:cascade}
   121	
   122	The recurrent layer in~\S\ref{sec:chain} references a cascade
   123	decomposition $E_{8}\to H_{4}\to H_{3}\to D_{4}\to \mathrm{Cl}(1,3)
   124	\to S^{7}\to 0$, implemented in
   125	\texttt{kernel/cascade\_descent.py:descend\_operator\_e8\_to\_h4\_clean}.
   126	An arbitrary operator on the $E_{8}$ root system descends to the
   127	4-D H$_4$ subspace through a sequence of orthogonal projections, each
   128	preserving the Frobenius norm to within $10^{-15}$. The
   129	$\sigma$-orbit projector basis from
   130	\texttt{kernel/sigma\_orbit\_basis.py} gives the K-class block
   131	decomposition at machine precision.
   132	
   133	The descent provides numerical stability for the cascade ablations:
   134	when one ablates a specific K-class contribution (e.g.\ $K_{7}$), the
   135	remaining operator structure is exactly preserved. We do not claim
   136	the cascade itself is forced by physics on a pre-substrate level; the
   137	cascade is a decomposition of operators on $\Rsixhundred$, and the
   138	choice of $\Rsixhundred$ as the active substrate is post-hoc justified
   139	by the empirical correspondences in~\S\ref{sec:results}.
   140	
   141	\subsection{What the substrate is fixed-by, and what it is not}
   142	
   143	\begin{itemize}\itemsep=2pt
   144	\item Fixed by group theory once $\Rsixhundred$ is chosen: $|V|=120$,
   145	  uniform degree $12$, Laplacian spectrum, $9$-shell partition, K-class
   146	  irrep block structure, average degree $k\!=\!12$, $\sigma$-twin pairing.
   147	\item Fixed by stability choice: the $\Ph^{-2}$ shift in $\Cph$. This
   148	  is not a derivation; it is a design-level clamp that bounds the
   149	  response inverse.
   150	\item Not fixed by this paper: the choice of $\Rsixhundred$ over the
   151	  $24$-cell or $120$-cell. The choice is post-hoc motivated by the H$_4$
   152	  cascade structure and the empirical correspondences. A formal
   153	  ablation against alternative regular 4-polytopes is an open build
   154	  (\S\ref{sec:limitations}).
   155	\end{itemize}
---04 1-160---
     1	% =====================================================================
     2	\section{The recurrent layer}\label{sec:chain}
     3	% =====================================================================
     4	
     5	The cascade-pipeline substrate (\S\ref{sec:substrate}) reproduces
     6	cortical-avalanche statistics matching real EEG (\S\ref{sec:results}).
     7	To test high-level signatures — NREM-N3 variance collapse, propofol
     8	regime-switching, propofol $\Phi$ collapse — we add a recurrent
     9	self-model layer above the substrate. The layer adds one
    10	graph-pinned nonlinearity, one condition-dependent self-injection
    11	coupling $\eta$, and four trajectory observables. No shape parameter
    12	is fit to any neural dataset.
    13	
    14	This section is method, not metaphysics. We do not claim the
    15	recurrent layer ``is'' consciousness; we report which numerical
    16	observables on the layer's trajectory match published biological
    17	signatures in~\S\ref{sec:results}.
    18	
    19	\subsection{The recurrent loop}
    20	
    21	Implementation: \texttt{kernel/self\_model\_stream.py:SelfModelLoop}.
    22	At each tick $t$ the substrate state evolves as
    23	\begin{align}
    24	f_{\mathrm{total}}(t) &= f_{\mathrm{ext}}(t) + \eta\cdot f_{\mathrm{self}}(\mathrm{snap}_{t-1}, \psi_{t-1}), \\
    25	\psi_{t} &= \Cph^{-1}\, f_{\mathrm{total}}(t), \\
    26	\psi^{\mathrm{thr}}_{t} &= \mathrm{bounded\_topk}(\psi_{t}, k=12), \\
    27	\mathrm{state}_{t} &= \mathrm{decay}\cdot\mathrm{state}_{t-1} + (1-\mathrm{decay})\cdot \psi^{\mathrm{thr}}_{t}, \\
    28	\mathrm{snap}_{t} &= \mathrm{bind\_phenomenal\_field}(\psi_{t}, \texttt{profile=K\_7\_only}),
    29	\end{align}
    30	with $\mathrm{decay}=0.95$ (state EMA factor) and $\eta$ the only
    31	condition-dependent architectural parameter. $f_{\mathrm{self}}$ maps
    32	the prior phenomenal snapshot to a directional source weighted by
    33	ignition $\times$ intensity (cosine direction alignment with the
    34	prior snapshot). The substrate response operator $\Cph$ is unchanged
    35	across all conditions.
    36	
    37	Conditions:
    38	\begin{itemize}\itemsep=2pt
    39	\item $\eta = 0.20$ for WAKE and RECOVERY (active recurrent self-loop);
    40	\item $\eta = 0.05$ for SLEEP\_N3 (attenuated self-loop);
    41	\item $\eta = 0.00$ for PROPOFOL (broken recurrence; residual cortex
    42	  preserved as background drive).
    43	\end{itemize}
    44	
    45	\subsection{The graph-pinned nonlinearity}
    46	
    47	\textbf{$\mathrm{bounded\_topk}(\psi, k=12)$.} This is the load-bearing
    48	nonlinearity, implemented in
    49	\texttt{kernel/lyapunov\_selector.py:bounded\_topk}: zero all but the
    50	top-$12$ vertex amplitudes (by absolute value), and rescale the rest
    51	to a small fraction of their baseline. Linear Green response alone
    52	gives smooth dynamics with cascade $\alpha\approx 1.09$ — no
    53	avalanches. Adding bounded-top-$K$ at $k=12$ drives $\alpha$ into the
    54	SOC band $(2.0, 3.5)$ with $R^{2}>0.85$.
    55	
    56	\textbf{Why $k=12$.} The choice $k=12$ is the average degree of
    57	$G_{V_{600}}$ (Lemma~\ref{lem:600cell}), pinned by the substrate
    58	geometry, not by neural data. Smaller $k$ (e.g.\ $k=6$) gives $\alpha$
    59	at the band edge with poorer fit; larger $k$ ($24, 48$) gives $\alpha$
    60	above band or with degraded fit. We do not search $k$ over a fitted
    61	window; $k$ is determined by the graph.
    62	
    63	\subsection{The integrated-information proxy
    64	            \texorpdfstring{$\Phi$}{Phi}}
    65	
    66	Implementation:
    67	\texttt{kernel/consciousness\_binding.py:phi\_iit\_trajectory}.
    68	Given the state history matrix $S\in\mathbb{R}^{T\times 120}$, write
    69	$A = S\cdot V$ for the H$_4$-eigenvector matrix $V$ (mode amplitudes
    70	$A\in\mathbb{R}^{T\times 120}$). Define $c_{\mathrm{full}}$ as the
    71	lag-$1$ auto-correlation of the full system, and $c_{k}$ as the
    72	lag-$1$ auto-correlation within the K-class irrep block $k$. Then
    73	\[
    74	\Phi \;=\; \max\!\bigl(0,\; |c_{\mathrm{full}}| - \mathrm{mean}_{k}\,|c_{k}|\bigr).
    75	\]
    76	By construction $\Phi\to 0$ under H$_{4}$-equivariant dynamics, since
    77	group symmetry forbids information transport across irrep classes;
    78	$\Phi > 0$ only when the dynamics break symmetry and transport
    79	information across class boundaries. This is a port of the published
    80	\texttt{integrated\_information\_phi\_irrep} proxy from the cascade
    81	pipeline, adapted to take amplitude trajectories from any source.
    82	
    83	We position $\Phi$ as an IIT-style direction-of-effect proxy, not as
    84	a full implementation of IIT. ARIA does not implement cause-effect
    85	repertoires, exclusion postulate, or integration-over-partitions
    86	machinery~\citep{Tononi2008,BalduzziTononi2008}. The propofol $\Phi$
    87	collapse in~\S\ref{sec:results} is consistent with the IIT direction
    88	of effect on the propofol-vs-wake state contrast; it is not a
    89	discharge of the IIT axioms.
    90	
    91	\subsection{The continuity composite}
    92	
    93	Implementation:
    94	\texttt{kernel/self\_model\_stream.py:StreamContinuityScorer}.
    95	A composite first-person continuity score over a 64-tick rolling
    96	window:
    97	\begin{align*}
    98	b_{\mathrm{cont}} &= \mathrm{mean\ cos\text{-}sim\ of\ consecutive}\ (I, L, P)\,\mathrm{vectors},\\
    99	v_{\mathrm{cont}} &= 1/(1 + 4\cdot \mathrm{var}(\mathrm{valence})),\\
   100	m_{\mathrm{pers}} &= \mathrm{frac.\ of\ consecutive\ same\text{-}modality\ ticks},\\
   101	i_{\mathrm{smooth}} &= 1/(1 + 4\cdot \mathrm{TV}(\mathrm{intensity})),\\
   102	\mathrm{composite} &= 0.35\cdot b_{\mathrm{cont}} + 0.25\cdot v_{\mathrm{cont}} + 0.20\cdot m_{\mathrm{pers}} + 0.20\cdot i_{\mathrm{smooth}}.
   103	\end{align*}
   104	This composite produces the propofol continuity-drop signature
   105	(WAKE composite $0.943$; PROPOFOL composite $0.877$;
   106	drop $+0.066$).
   107	
   108	\subsection{The phenomenal-field binding}
   109	
   110	Implementation:
   111	\texttt{kernel/consciousness\_binding.py:bind\_phenomenal\_field}.
   112	The substrate state $\psi_{t}$ is mapped to a phenomenal snapshot
   113	with channels (intensity $I$, self-luminosity $L$, presence $P$,
   114	valence, modality\_label). The modality\_label is determined by which
   115	H$_4$ K-class dominates the isotypic compression of $\psi_{t}$ under
   116	the $\sigma$-orbit projector basis. The default profile
   117	\texttt{K\_7\_only} restricts to $\sigma$-twin K-classes for modality
   118	labelling; H$_4$-proper classes contribute amplitude bias.
   119	
   120	\subsection{Stimulus models}
   121	
   122	Implementation: \texttt{demo\_drug\_sleep\_v4.py}. Four conditions
   123	$\times$ $800$ ticks each at seed $42$:
   124	
   125	\textbf{WAKE.} AR(1) cortical noise ($\beta=0.90$), tonic equator-shell
   126	coherence (small always-on bias), and attention episodes (20--50
   127	ticks at amplitude $0.8$, anchored to the largest shell with $15\%$
   128	within-shell rotation per tick). The AR(1) gives temporal correlation
   129	that lets the $\eta=0.20$ self-loop integrate; tonic coherence anchors
   130	modality; attention episodes mimic biological visual fixation
   131	(200--400~ms dwell time analogue); within-shell rotation generates
   132	cascade events without changing modality.
   133	
   134	\textbf{SLEEP\_N3.} Slow oscillation ($\sim 1$\,Hz analogue,
   135	amplitude $1.0$) on a coherent shell, plus spindle bursts ($12$ ticks
   136	every $100$ at amplitude $0.4$ fast modulation), plus K-complexes
   137	($4\%$ of ticks at amplitude $0.8$).
   138	
   139	\textbf{PROPOFOL.} Low-amplitude tonic noise (amplitude $0.05$);
   140	$\eta = 0.00$ (broken recurrence). Residual cortex preserved as
   141	background drive.
   142	
   143	\textbf{RECOVERY.} Identical to WAKE — verifies determinism and
   144	reversibility.
   145	
   146	The stimulus models are deliberately structural rather than
   147	measurement-fitted: amplitudes and durations match published
   148	biological time scales but are not tuned to specific signatures.
   149	The full stimulus code is \texttt{demo\_drug\_sleep\_v4.py}. We
   150	disclose stimulus-shape choice as a methodological design move,
   151	not a derived theorem.
   152	
   153	\subsection{Cascade-mechanism ablation matrix}
   154	
   155	The cascade dynamics on the substrate use four mechanisms acting on
   156	the pressure field, each ablatable independently. The $2^{4}$
   157	ablation grid is the basis for the preregistered tests P1--P5 and
   158	the C$\times$P stress test in~\S\ref{sec:stress}.
   159	
   160	\textbf{$D$ — D$_{4}$ orbit coupling.} The H$_4$ root system contains

exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/03_substrate.tex' | sed -n '1,220p'; printf '%s\\n' '---04 start---'; nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex' | sed -n '1,90p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 281ms:
     1	% =====================================================================
     2	\section{The 600-cell response substrate}\label{sec:substrate}
     3	% =====================================================================
     4	
     5	This section constructs the substrate. \S\ref{ssec:vertices}
     6	gives the vertex set. \S\ref{ssec:graph} gives the graph and its
     7	H$_4$-symmetry-forced spectrum. \S\ref{ssec:cphi} gives the response
     8	operator $\Cph$ and the $\Ph^{-2}$ stability clamp.
     9	\S\ref{ssec:shells} gives the 9-shell decomposition used for source
    10	projection. \S\ref{ssec:cascade} sketches the seven-rung cascade
    11	descent referenced by the recurrent layer in~\S\ref{sec:chain}. None
    12	of these objects depend on neural data.
    13	
    14	\subsection{Vertex construction}\label{ssec:vertices}
    15	
    16	The 600-cell $\Rsixhundred$ has $120$ vertices in
    17	$\mathbb{R}^{4}$~\citep{CoxeterRegularPolytopes,Weisstein600Cell}.
    18	With $\Ph = (1+\sqrt 5)/2$ the canonical vertex set is
    19	\begin{itemize}\itemsep=1pt
    20	\item $8$ vertices: all permutations of $(\pm 1, 0, 0, 0)$;
    21	\item $16$ vertices: all sign combinations of
    22	  $(\pm 1, \pm 1, \pm 1, \pm 1)/2$;
    23	\item $96$ vertices: all even permutations of
    24	  $(\pm \Ph, \pm 1, \pm 1/\Ph, 0)/2$.
    25	\end{itemize}
    26	All $120$ vertices lie on the unit $3$-sphere $S^{3}$. The H$_4$
    27	Coxeter group acts transitively on the vertex set; in particular,
    28	every vertex has identical local structure. Implementation:
    29	\texttt{kernel/vfd\_closure\_kernel.py:build\_600cell\_vertices}.
    30	
    31	\subsection{Graph and Laplacian spectrum}\label{ssec:graph}
    32	
    33	The substrate graph $G_{V_{600}} = (V, E)$ is built by connecting each
    34	vertex to its nearest neighbours under the Euclidean metric on $S^{3}$.
    35	H$_4$ acts transitively on the vertex set, forcing uniformity of the
    36	local structure; the eigenvalue multiplicities follow from H$_4$
    37	character theory on the regular representation. The construction and
    38	spectrum are standard~\citep{CoxeterRegularPolytopes,Weisstein600Cell}.
    39	\begin{lemma}[600-cell graph facts]\label{lem:600cell}
    40	The graph $G_{V_{600}}$ has $|V|=120$ vertices, $|E|=720$ edges, every
    41	vertex has degree exactly $12$, and the unweighted graph Laplacian
    42	$\Lop = D - A$ has spectrum
    43	\[
    44	\sigma(\Lop) \;=\;
    45	\bigl\{0^{1}, 3^{4}, 4\Ph^{9}, 6\Ph^{16}, (12\!-\!4\Ph)^{9},
    46	       (12\!-\!6\Ph)^{16}, 9^{4}, 12^{1}\bigr\},
    47	\]
    48	where the exponent denotes multiplicity. The decomposition into H$_4$
    49	irreducible representations is exact at machine precision; the
    50	$\sigma$-orbit projector basis (\texttt{kernel/sigma\_orbit\_basis.py})
    51	realises it block-by-block with cross-block norm $<10^{-15}$.
    52	\end{lemma}
    53	
    54	The non-trivial eigenmodes partition into Coxeter exponent classes.
    55	For H$_4$ proper, the exponents are $\{1, 11, 19, 29\}$; for the
    56	Galois twin $\sigma(\mathrm{H}_4)$ under the $\sigma$-automorphism of
    57	$\mathbb{Z}[\Ph]$, the exponents become $\{7, 13, 17, 23\}$. We label
    58	the eigenspaces $K_{1}, K_{11}, K_{19}, K_{29}$ for H$_4$-proper modes
    59	and $K_{7}, K_{13}, K_{17}, K_{23}$ for $\sigma$-twin modes. The
    60	multiplicities follow from character theory and are reproduced in
    61	the implementation
    62	(\texttt{kernel/sigma\_orbit\_basis.py:\_self\_test}). The
    63	$K_{7}$-modes will be the dominant phenomenal-binding profile in
    64	\S\ref{sec:chain}.
    65	
    66	\subsection{The shifted-Laplacian response \texorpdfstring{$\Cph$}{C\_phi}}\label{ssec:cphi}
    67	
    68	The substrate's linear response to an external source $f \in \mathbb{R}^{120}$
    69	is the discrete Green's function of the shifted Laplacian:
    70	\begin{equation}\label{eq:cphi}
    71	\Cph \;=\; \Lop + \Ph^{-2} I,
    72	\qquad
    73	\psi \;=\; \Cph^{-1} f.
    74	\end{equation}
    75	The shift $\Ph^{-2} \approx 0.382$ is a design-level stability
    76	clamp: it makes $\Cph$ strictly positive definite (smallest eigenvalue
    77	$\Ph^{-2}$, since the trivial Laplacian eigenvalue is $0$), so that the
    78	inverse is bounded with operator norm $\Ph^{2}\approx 2.618$. This is
    79	\emph{not} a derived theorem; it is a stability choice. The companion
    80	kernel document~\citep{SmartAriaClosureKernel2026} discusses the same
    81	$\Cph$ as the basis for an independent passive-regime witness in
    82	flavour physics~\citep{SmartBAnomaly2026}, where the same operator
    83	form (without retuning the shift) describes the
    84	$B\to K^{*}\mu^{+}\mu^{-}$ angular anomaly across five public datasets.
    85	This paper imports $\Cph$ from that line; we do not re-derive it.
    86	
    87	The response $\psi = \Cph^{-1} f$ is smooth in $f$. By itself it does
    88	not produce critical-state cascade statistics; the recurrent layer
    89	in~\S\ref{sec:chain} adds a graph-pinned nonlinearity
    90	$\mathrm{bounded\_topk}(\psi, k\!=\!12)$ to obtain self-organised-critical
    91	event distributions. The choice $k\!=\!12$ is the average degree of
    92	$G_{V_{600}}$ (Lemma~\ref{lem:600cell}), pinned by the substrate, not
    93	fitted to any dataset.
    94	
    95	\paragraph{Disclosure (substrate-witness scope).}
    96	The $\Ph^{-2}$ floor is a stability shift, not a derived parameter.
    97	The bounded-top-$K$ nonlinearity uses $k\!=\!12$ pinned to the graph's
    98	average degree, not a fitted threshold. No other shape parameter
    99	enters. The condition-dependent self-injection coupling
   100	$\eta\in\{0, 0.05, 0.20\}$ is the only architectural parameter that
   101	varies between conditions in~\S\ref{sec:chain}; it is reported
   102	explicitly per condition.
   103	
   104	\subsection{Shell decomposition}\label{ssec:shells}
   105	
   106	Under the H$_3$ subgroup, the $120$ vertices partition into $9$
   107	spherical shells indexed by Euclidean inner product with a chosen pole:
   108	\[
   109	\bigl(|S_0|,\ldots,|S_8|\bigr) \;=\; (1, 12, 20, 12, 30, 12, 20, 12, 1).
   110	\]
   111	The middle shell $S_{4}$ has $30$ vertices on the equatorial plane
   112	(the icosidodecahedral ring). When projecting onto a continuum kernel
   113	in companion preprints~\citep{SmartAriaClosureKernel2026}, the
   114	shell-mean projection of the equatorial-source response,
   115	$\kappa(x) = \mathrm{shell\text{-}mean}[\Cph^{-1} f_{\mathrm{equat}}](x)$,
   116	collapses on the continuum exponential $\frac{\Ph}{2}\,e^{-|x|/\Ph}$.
   117	This paper does not use that continuum projection; we work with the
   118	discrete operator throughout.
   119	
   120	\subsection{Cascade descent (sketch)}\label{ssec:cascade}
   121	
   122	The recurrent layer in~\S\ref{sec:chain} references a cascade
   123	decomposition $E_{8}\to H_{4}\to H_{3}\to D_{4}\to \mathrm{Cl}(1,3)
   124	\to S^{7}\to 0$, implemented in
   125	\texttt{kernel/cascade\_descent.py:descend\_operator\_e8\_to\_h4\_clean}.
   126	An arbitrary operator on the $E_{8}$ root system descends to the
   127	4-D H$_4$ subspace through a sequence of orthogonal projections, each
   128	preserving the Frobenius norm to within $10^{-15}$. The
   129	$\sigma$-orbit projector basis from
   130	\texttt{kernel/sigma\_orbit\_basis.py} gives the K-class block
   131	decomposition at machine precision.
   132	
   133	The descent provides numerical stability for the cascade ablations:
   134	when one ablates a specific K-class contribution (e.g.\ $K_{7}$), the
   135	remaining operator structure is exactly preserved. We do not claim
   136	the cascade itself is forced by physics on a pre-substrate level; the
   137	cascade is a decomposition of operators on $\Rsixhundred$, and the
   138	choice of $\Rsixhundred$ as the active substrate is post-hoc justified
   139	by the empirical correspondences in~\S\ref{sec:results}.
   140	
   141	\subsection{What the substrate is fixed-by, and what it is not}
   142	
   143	\begin{itemize}\itemsep=2pt
   144	\item Fixed by group theory once $\Rsixhundred$ is chosen: $|V|=120$,
   145	  uniform degree $12$, Laplacian spectrum, $9$-shell partition, K-class
   146	  irrep block structure, average degree $k\!=\!12$, $\sigma$-twin pairing.
   147	\item Fixed by stability choice: the $\Ph^{-2}$ shift in $\Cph$. This
   148	  is not a derivation; it is a design-level clamp that bounds the
   149	  response inverse.
   150	\item Not fixed by this paper: the choice of $\Rsixhundred$ over the
   151	  $24$-cell or $120$-cell. The choice is post-hoc motivated by the H$_4$
   152	  cascade structure and the empirical correspondences. A formal
   153	  ablation against alternative regular 4-polytopes is an open build
   154	  (\S\ref{sec:limitations}).
   155	\end{itemize}
---04 start---
     1	% =====================================================================
     2	\section{The recurrent layer}\label{sec:chain}
     3	% =====================================================================
     4	
     5	The cascade-pipeline substrate (\S\ref{sec:substrate}) reproduces
     6	cortical-avalanche statistics matching real EEG (\S\ref{sec:results}).
     7	To test high-level signatures — NREM-N3 variance collapse, propofol
     8	regime-switching, propofol $\Phi$ collapse — we add a recurrent
     9	self-model layer above the substrate. The layer adds one
    10	graph-pinned nonlinearity, one condition-dependent self-injection
    11	coupling $\eta$, and four trajectory observables. No shape parameter
    12	is fit to any neural dataset.
    13	
    14	This section is method, not metaphysics. We do not claim the
    15	recurrent layer ``is'' consciousness; we report which numerical
    16	observables on the layer's trajectory match published biological
    17	signatures in~\S\ref{sec:results}.
    18	
    19	\subsection{The recurrent loop}
    20	
    21	Implementation: \texttt{kernel/self\_model\_stream.py:SelfModelLoop}.
    22	At each tick $t$ the substrate state evolves as
    23	\begin{align}
    24	f_{\mathrm{total}}(t) &= f_{\mathrm{ext}}(t) + \eta\cdot f_{\mathrm{self}}(\mathrm{snap}_{t-1}, \psi_{t-1}), \\
    25	\psi_{t} &= \Cph^{-1}\, f_{\mathrm{total}}(t), \\
    26	\psi^{\mathrm{thr}}_{t} &= \mathrm{bounded\_topk}(\psi_{t}, k=12), \\
    27	\mathrm{state}_{t} &= \mathrm{decay}\cdot\mathrm{state}_{t-1} + (1-\mathrm{decay})\cdot \psi^{\mathrm{thr}}_{t}, \\
    28	\mathrm{snap}_{t} &= \mathrm{bind\_phenomenal\_field}(\psi_{t}, \texttt{profile=K\_7\_only}),
    29	\end{align}
    30	with $\mathrm{decay}=0.95$ (state EMA factor) and $\eta$ the only
    31	condition-dependent architectural parameter. $f_{\mathrm{self}}$ maps
    32	the prior phenomenal snapshot to a directional source weighted by
    33	ignition $\times$ intensity (cosine direction alignment with the
    34	prior snapshot). The substrate response operator $\Cph$ is unchanged
    35	across all conditions.
    36	
    37	Conditions:
    38	\begin{itemize}\itemsep=2pt
    39	\item $\eta = 0.20$ for WAKE and RECOVERY (active recurrent self-loop);
    40	\item $\eta = 0.05$ for SLEEP\_N3 (attenuated self-loop);
    41	\item $\eta = 0.00$ for PROPOFOL (broken recurrence; residual cortex
    42	  preserved as background drive).
    43	\end{itemize}
    44	
    45	\subsection{The graph-pinned nonlinearity}
    46	
    47	\textbf{$\mathrm{bounded\_topk}(\psi, k=12)$.} This is the load-bearing
    48	nonlinearity, implemented in
    49	\texttt{kernel/lyapunov\_selector.py:bounded\_topk}: zero all but the
    50	top-$12$ vertex amplitudes (by absolute value), and rescale the rest
    51	to a small fraction of their baseline. Linear Green response alone
    52	gives smooth dynamics with cascade $\alpha\approx 1.09$ — no
    53	avalanches. Adding bounded-top-$K$ at $k=12$ drives $\alpha$ into the
    54	SOC band $(2.0, 3.5)$ with $R^{2}>0.85$.
    55	
    56	\textbf{Why $k=12$.} The choice $k=12$ is the average degree of
    57	$G_{V_{600}}$ (Lemma~\ref{lem:600cell}), pinned by the substrate
    58	geometry, not by neural data. Smaller $k$ (e.g.\ $k=6$) gives $\alpha$
    59	at the band edge with poorer fit; larger $k$ ($24, 48$) gives $\alpha$
    60	above band or with degraded fit. We do not search $k$ over a fitted
    61	window; $k$ is determined by the graph.
    62	
    63	\subsection{The integrated-information proxy
    64	            \texorpdfstring{$\Phi$}{Phi}}
    65	
    66	Implementation:
    67	\texttt{kernel/consciousness\_binding.py:phi\_iit\_trajectory}.
    68	Given the state history matrix $S\in\mathbb{R}^{T\times 120}$, write
    69	$A = S\cdot V$ for the H$_4$-eigenvector matrix $V$ (mode amplitudes
    70	$A\in\mathbb{R}^{T\times 120}$). Define $c_{\mathrm{full}}$ as the
    71	lag-$1$ auto-correlation of the full system, and $c_{k}$ as the
    72	lag-$1$ auto-correlation within the K-class irrep block $k$. Then
    73	\[
    74	\Phi \;=\; \max\!\bigl(0,\; |c_{\mathrm{full}}| - \mathrm{mean}_{k}\,|c_{k}|\bigr).
    75	\]
    76	By construction $\Phi\to 0$ under H$_{4}$-equivariant dynamics, since
    77	group symmetry forbids information transport across irrep classes;
    78	$\Phi > 0$ only when the dynamics break symmetry and transport
    79	information across class boundaries. This is a port of the published
    80	\texttt{integrated\_information\_phi\_irrep} proxy from the cascade
    81	pipeline, adapted to take amplitude trajectories from any source.
    82	
    83	We position $\Phi$ as an IIT-style direction-of-effect proxy, not as
    84	a full implementation of IIT. ARIA does not implement cause-effect
    85	repertoires, exclusion postulate, or integration-over-partitions
    86	machinery~\citep{Tononi2008,BalduzziTononi2008}. The propofol $\Phi$
    87	collapse in~\S\ref{sec:results} is consistent with the IIT direction
    88	of effect on the propofol-vs-wake state contrast; it is not a
    89	discharge of the IIT axioms.
    90	

codex
The paper’s headline tables are now mapped; I’ll verify the exact numeric provenance from the local source documents.
  ✓ Read WO context and paper
  → Verify source numerics
  • Audit claims and scope
  • Compile referee verdict
exec
/bin/bash -lc "cd '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess' && for f in docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md docs/brain_mapping/P4_SYNERGY_FINDING.md docs/brain_mapping/CROSS_DOMAIN_RESULTS.md docs/brain_mapping/PAPER_PREDICTIONS.md docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md docs/brain_mapping/MANUSCRIPT_V2.md; do echo \"===== "'$f ====="; rg -n "(6/6|PASS|18/18|17/18|15/18|0/2000|0'"\\.190|0\\.143|0\\.239|\\+40\\.6|\\+27\\.2|n=25|n=15|93\\.8|83\\.1|53\\.1|1\\.83|2\\.96|11\\.58|79\\.78|6\\.80|1003|n=100|3\\.388|P13|P4|methodology|threshold|reset|LOO|5-fold|0\\.463|0\\.33|0\\.066|2\\.252|2\\.50|2\\.53|Brodbeck|propofol switching|switching ratio|preregister|refinement|0\\.0000)\" \""'$f"; done' in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 368ms:
===== docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md =====
15:recurrence on the 600-cell with bounded-top-K thresholding) plus
23:has a published reference and a falsifiable threshold; all six pass.
26:stimulus-model artefacts in `demo_wake_alpha_diagnosis.py`) to 6/6 by
32:| 1 | Sleep variance ratio | NREM-N3 EEG (Lee 2017, Jobst 2017) | ratio ≈ 0.365 | 0.463 | ✓ within 30% |
33:| 2 | Propofol switching ↑ | OpenNeuro ds005620 (n=8, 2.96×) | ratio in [1.5, 5.0] | 1.83× | ✓ |
34:| 3 | Propofol continuity ↓ | EEG microstate (Brodbeck 2012) | drop > 0.020 | +0.066 | ✓ |
35:| 4 | Propofol Φ collapse | IIT prediction (Tononi 2008) | ratio < 0.5 | 0.33× | ✓ |
37:| 6 | Cortical avalanche α | Sleep-EDFx n=30 (α=2.51 [2.50, 2.53]) | α ∈ [1.5, 3.5], R² > 0.85 | 2.252 [1.82, 2.86] R²=0.956 | ✓ |
40:**ARIA WAKE α CI [1.82, 2.86] overlaps real Sleep-EDFx EEG CI [2.50, 2.86]
63:**The bounded_topk(k=12) thresholding is the load-bearing nonlinearity.**
195:All four conditions run for 800 ticks at seed = 42, k_threshold = 12.
199:WAKE       58   2.252   [1.82, 2.86]   0.956  2.18e-05    0.0008   0.943
202:RECOVERY   58   2.252   [1.82, 2.86]   0.956  2.18e-05    0.0008   0.943
212:Ratio = 0.463. Falls within [0.255, 0.475], the 30% prediction window.
224:microstate switching ratio 2.96×).
226:**Observed:** WAKE modality_switches → PROPOFOL modality_switches ratio = 1.83×.
227:Falls within [1.5×, 5.0×] window. Below the empirical 2.96× point estimate
238:modality + smoothness). Source: Brodbeck 2012 microstate literature
242:Drop = +0.066. Falls past the +0.020 minimum.
256:Ratio PROPOFOL/WAKE = 0.33×. Below the 0.50× threshold.
283:**Observed:** WAKE α = 2.252, 95% CI [1.82, 2.86], R² = 0.956 (n_events=58).
286:- Real Sleep-EDFx EEG CI [2.50, 2.86] (n=30 subjects, prior preregistration)
293:**Mechanism:** The bounded_topk(k=12) thresholding is the critical
313:| H4: k_threshold sweep | k=12 is the sweet spot |
329:- **v4.final**: AR(1) β=0.90 + tonic shell + episodes 20-50 amp 0.8 anchored to shell + within-shell rotation → 6/6
345:- k_threshold: 12 (cortical band; bounded_topk nonlinearity)
357:- The deterministic 600-cell substrate with bounded_topk thresholding
362:- All six signatures pass under preregistered thresholds.
368:- The Sig 2 ratio (1.83×) is below the empirical point estimate (2.96×)
373:  preregistered validation methodology).
376:  "exact match" — only "within preregistered tolerance."
386:| `demo_drug_sleep_v4.py` | The 6/6 demo script — single deterministic run |
392:| `kernel/lyapunov_selector.py` | bounded_topk thresholding |
404:- `project_propofol_empirical_5.md` — empirical anchor for Sig 2 (n=8, 2.96×)
406:  (n=30 Sleep-EDFx, α=2.51 [2.50, 2.53])
413:polytope with bounded top-K thresholding (k=12) and a recurrent self-injection
415:signature is a falsifiable threshold against published data: cortical-avalanche
416:power law in the wake-state band (passes with α = 2.252, 95% CI [1.82, 2.86]
417:overlapping the real Sleep-EDFx CI [2.50, 2.86]), NREM-N3 variance collapse to
419:1.83×), propofol continuity disruption (passes at +0.066), propofol Φ collapse
420:in the IIT direction (passes at 0.33× wake), and recovery reversibility (passes
===== docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md =====
3:*This document supersedes `VALIDATION_RESULTS.md` (2026-04-20, 15/18).
4:It records the most recent run of the preregistered validation harness
5:plus the N=20 deep-dive on the residual P4 prediction.*
8:> 18 / 18 with N=20 deep-dive on the residual P4.** Original 15/18
10:> ablation interaction tests and an unspecified reset protocol for the
11:> chess LOO test. With (a) cascade block bumped from 3 to 5 seeds per
12:> condition, (b) `homeostatic_reset(level=1.0)` wired in between depth
13:> measurements for chess LOO, and (c) N=20 fresh-seed replication of
15:> set is fully validated against preregistered thresholds.
25:Each prediction has a falsifiable threshold (numerical band or
27:`run_preregistered_validation.py` — git-tracked, deterministic given
37:The original validation run on 2026-04-20 reported **15/18 passes**:
45:  - **P4** (C×P synergy): observed +0.044 at N=3, below +0.10 floor.
46:  - **P13** (Chess LOO substrate lift ≥ +15pp): observed +3.1pp,
50:- "P3, P4 walked back to 'preliminary, requires larger N'."
51:- "P13 reframed as state-dependent — substrate state drifted toward
53:  reset protocol."
59:1. **Cascade block N bumped 3 → 5** for P2, P3, P4, P5 conditions
60:   in `run_preregistered_validation.py`. The original 3 seeds was
61:   the source of high-variance failure on P3 and P4.
63:2. **`homeostatic_reset(level=1.0)`** wired into the validation script
65:   This is the reset protocol identified post-hoc as necessary to
66:   prevent pressure-field equilibration across LOO depth measurements
69:3. **N=20 deep-dive** on the residual P4 (`demo_p4_cxp_deep_dive.py`):
72:   `P4_SYNERGY_FINDING.md` for the standalone report.
80:| ID | Claim | Threshold | 2026-04-20 (3-seed) | **2026-04-29 (5-seed + reset + N=20 P4)** | Verdict |
85:| P4 | C×P synergy | ≥ +0.10 | +0.044 ❌ | **+0.190 at N=20, CI [+0.143, +0.239]** | ✅ at N=20 |
89:| P8 | W→N3 switching ratio | < 0.50 | 0.058 ✅ | **0.058** | ✅ |
90:| P9 | Chess 5-fold CV | ≥ 70% | 83.1% ✅ | **83.1%** | ✅ |
93:| P12 | Chess goldilocks peak | ∈ {15, 25, 40, 60} | n=15 ✅ | **n=25** | ✅ |
94:| P13 | Chess LOO substrate lift | ≥ +15pp (with reset) | +3.1pp ❌ | **+40.6pp** | ✅ |
95:| P14 | Conv raw 5-fold CV | ≥ 75% | 87.5% ✅ | **87.5%** | ✅ |
98:| P17 | ARIA degree std (theorem) | = 0.00 | 0.0000 ✅ | **0.0000** | ✅ |
99:| P18 | HCP ICA-50 degree std | > 2.0 | 3.388 ✅ | **3.388** | ✅ |
103:## 3. Predictions that flipped to PASS — explained
116:seeds tightens the estimate enough to land inside the threshold.
120:interaction estimate is approximately 0.06–0.10; the threshold is
125:cascade-α" is **supported** by the N=5 re-run within the preregistered
126:threshold. We do not claim point-zero independence (the estimate is
130:### 3.2 P4 — C×P synergy
133:`P4_SYNERGY_FINDING.md` for the full story.
137:**Original (N=3) failure:** +0.044. Below threshold.
139:**2026-04-29 re-run (N=5):** +0.039. Still below threshold — confirming
145:C×P bootstrap mean:           +0.190
146:C×P 95% bootstrap CI:         [+0.143, +0.239]
147:P(interaction ≤ 0):           0.0000
148:P(interaction < +0.10):       0.0000
151:The 95% CI is **entirely above the preregistered +0.10 threshold**.
161:`P4_SYNERGY_FINDING.md` for the mechanistic interpretation.
163:### 3.3 P13 — Chess LOO substrate lift
165:**Threshold:** ≥ +15pp lift (substrate vs raw on LOO at n=25 ticks).
167:**Original (N=1) failure:** +3.1pp. Far below threshold.
169:**2026-04-29 re-run (with `homeostatic_reset(level=1.0)` between depth
170:measurements):** **+40.6pp**.
173:Depth sweep (raw 53.1%, with reset between measurements):
174:  n=5:    53.1%
175:  n=15:   65.6%
176:  n=25:   93.8%   ← peak (P12 goldilocks)
179:  n=100:  78.1%
181:Lift at n=25 = 93.8% − 53.1% = +40.6pp
186:original LOO test ran six consecutive depth measurements (n=5, 15, 25,
187:40, 60, 100) without reset, so by the time it reached n=25 the substrate
189:washed out, collapsing the LOO lift to +3pp.
191:The reset protocol restores the canonical far-from-equilibrium operating
192:point before each measurement. With reset, the predicted +15pp lift is
197:dynamical system. **Any multi-trial benchmark must specify state-reset
212:  at 3 seeds). Both above the +0.30 dominance threshold.
221:- **P8**: W→N3 switching ratio = 0.058. Below 0.50 — sleep is the
225:### 4.3 Chess closed-loop (P9, P10, P11, P12, plus P13 fixed)
227:- **P9**: Chess 5-fold CV at fresh seeds (30200–30204) = 83.1%
235:- **P12**: Goldilocks peak depth = n=25 (∈ {15, 25, 40, 60}). With
236:  reset between measurements, n=25 is the global maximum at 93.8%.
237:- **P13**: LOO substrate lift at n=25 = **+40.6pp** with reset
242:- **P14**: Conv raw 5-fold CV = 87.5% (≥ 75%). Already saturated at
254:- **P17**: ARIA degree std = 0.0000. Theorem (H₄ transitivity).
255:- **P18**: HCP ICA-50 degree std = 3.388 (n=100 subjects, density-
256:  matched threshold). > 2.0 confirms small-world hub-spoke structure
258:  symmetry-breaking is +79.78σ on participation ratio against ARIA.
262:## 5. The 18/18 verdict
264:**Standard validation tally:** 17/18 (the residual P4 fails at N=5).
265:**Including the N=20 deep-dive:** 18/18 (P4 passes decisively at N=20).
267:The empirical tally is **18/18 at adequate replication**. Two of the
268:three original failures (P3, P13) close at standard methodology
269:improvements (5-seed cascade block + reset protocol). The third (P4)
275:All eighteen preregistered predictions are **supported by the data
276:within preregistered thresholds**, with the methodological caveat
277:that two interaction tests (P3, P4) require N ≥ 5 and N ≥ 20
286:> *"All eighteen preregistered predictions pass at empirical thresholds.
287:> The validation runs at standard methodology (5-seed cascade block,
288:> homeostatic reset between LOO depth measurements) give 17/18; the
289:> residual prediction (P4 — C×P synergy) requires higher-N replication
291:> interaction-term estimates. With adequate N, P4 passes decisively
292:> (+0.190, 95% bootstrap CI [+0.143, +0.239]); the synergy is in fact
293:> ~90% above the preregistered floor, indicating C and P are strongly
310:within the preregistered |·| < 0.20 band, confirmed at N=5.
313:### 6.2 Original walk-back on P4 (C×P synergy)
318:**Now reads:** C×P synergy is +0.190 [+0.143, +0.239] at N=20, ~90%
319:above preregistered. C and P are strongly coupled cascade-state
323:### 6.3 Original walk-back on P13 (chess LOO lift)
325:> *"Specify polytope reset protocol in paper. Note that substrate
331:is retracted: with the reset protocol wired into the harness, the lift
332:is +40.6pp.
338:The original validation methodology — 18 preregistered predictions
339:with falsifiable thresholds, frozen before any validation run — is
341:re-run with N improvements **did not modify any threshold or claim
343:reset. The fact that this gave 18/18 (with N=20 P4) where the
344:original gave 15/18 demonstrates that:
348:(b) The original validation methodology was insufficient — N=3 is
350:(c) A re-run with adequate methodology validates all predictions
355:adequate power. No threshold was loosened. No prediction was rewritten
364:# Standard validation (17/18, ~18 min)
366:python3 run_preregistered_validation.py
368:# P4 N=20 deep-dive (~28 min)
372:JSON results are saved to `~/.aria/preregistered_validation/results_*.json`.
385:- `docs/brain_mapping/VALIDATION_RESULTS.md` — original 15/18 result
387:- `docs/brain_mapping/P4_SYNERGY_FINDING.md` — standalone N=20 report
390:  drug/sleep EEG signatures (independent of preregistered set, on
394:- `docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md` — homeostatic-reset
396:- `run_preregistered_validation.py` — validation harness
===== docs/brain_mapping/P4_SYNERGY_FINDING.md =====
3:*Standalone publishable finding from N=20 seed deep-dive on the residual P4
4:preregistered prediction. Compiled 2026-04-29.*
9:> on cascade-α is +0.190, 95% bootstrap CI [+0.143, +0.239]** — comparable
11:> preregistered prediction of ≥+0.10. The original 3-seed preregistered
20:## 1. Background: what was preregistered, what failed at N=3
37:  threshold but not yet crossed) emit pressure at 30% scale, saturating
48:### 1.2 The preregistered predictions for D/C/P/E mechanisms
57:| **P4** | **C×P synergy ≥ +0.10** | ≥ +0.10 |
60:**P4 was the genuine architectural prediction:** because C creates variety
63:contribution to cascade-α. The preregistered floor was +0.10 — stating
87:This was below the +0.10 threshold, so P4 was reported as a **fail**
88:in the headline 15/18 result. The walk-back was:
165:C×P bootstrap mean:           +0.190
166:C×P 95% bootstrap CI:         [+0.143, +0.239]
167:P(interaction ≤ 0):           0.0000
168:P(interaction < +0.10):       0.0000
171:**The 95% CI is entirely above the preregistered +0.10 threshold.**
186:mean = +0.190,  std = 0.089,  SEM = 0.020
206:20   32000–32019      +0.190          [+0.143, +0.239]      ✅ DECISIVELY ABOVE
216:   were no other bias — already containing the threshold. But N=3 also
252:exceeded threshold. As the frame rotates, the uncrossed pool's
300:### 5.1 The corrected paper claim on P4
302:**Old framing (2026-04-20, with 15/18 result):**
304:> *"P4 (C×P synergy ≥+0.10) failed at +0.04 in 3-seed validation. We
310:> *"P4 (C×P synergy ≥+0.10) was preregistered with a +0.10 floor.
314:> gives synergy = +0.190, 95% bootstrap CI [+0.143, +0.239],
334:### 5.3 The 18/18 verdict
336:P4 was the residual gap in the 17/18 validation re-run from earlier in
338:the preregistered floor. **Effectively, all eighteen preregistered
387:   (e.g., pressure-threshold crossings) might give a slightly different
404:The C×P interaction in ARIA's cascade ablation matrix was preregistered
409:synergy = +0.190, 95% bootstrap CI [+0.143, +0.239], P(synergy ≤ 0) = 0,
420:from the preregistered prediction set, taking the empirical tally from
421:17/18 to 18/18.
430:- `run_preregistered_validation.py` — original cascade-block test
432:- `docs/brain_mapping/VALIDATION_RESULTS.md` — original 15/18 result
===== docs/brain_mapping/CROSS_DOMAIN_RESULTS.md =====
8:> when raw features are ambiguous (chess: +40.6 percentage points on
9:> leave-one-out, raw 53.1% → substrate-routed 93.8%) and is correctly
13:> transitivity); HCP n=1003 degree std = 3.28 ± 0.28; ARIA is
14:> −11.58σ on degree homogeneity and +79.78σ on participation ratio,
27:1. **Chess pattern recognition** (P9–P13 in the preregistered set):
42:   the Human Connectome Project (n=1003 subjects, ICA-50
47:preregistered tests on chess + conversation pass at fresh seeds; both
52:## 2. Chess pattern recognition (P9–P13)
76:cosine similarity, validated by k-fold CV (k=5) or leave-one-out (LOO).
79:is reset to canonical state via `mon.homeostatic_reset(level=1.0)`.
84:### 2.2 P9 — Raw 5-fold cross-validation (fresh seeds)
86:**Threshold:** Chess substrate-routed 5-fold CV ≥ 70%.
92:Mean:                 83.1%
95:**Interpretation:** Substrate-routed classification at 5-fold CV is
96:83.1% on the 32-position × 4-category task, well above the 70%
97:threshold. Per-seed variance is small (range 81.2%–87.5%).
100:the fresh-seed mean of 83.1% replicates discovery within expected
121:(83.1% − 65.4%) is the semantic alignment bonus.
143:(23.4% ≈ 25% chance). This confirms the 83.1% raw and 65.4% null are
153:depth, with `homeostatic_reset(level=1.0)` between measurements.
159:   5     53.1%
161:  25     93.8%   ← peak
168:n=25, with a roll-off both at shallower depth (insufficient
175:### 2.6 P13 — Substrate lift on LOO with reset protocol
177:**Threshold:** Substrate-routed LOO accuracy − raw-feature LOO
180:**Method:** Run LOO classification on (a) raw 8-dim V2 features and
181:(b) substrate-routed patterns at n=25, with reset between depth
187:Raw features (LOO, 1-NN cosine):       53.1%
188:Substrate-routed (n=25, with reset):   93.8%
189:Lift:                                  +40.6 percentage points
193:discrimination from chance-level on raw features (53.1% on 4 categories
194:is just above chance-25%) to near-perfect (93.8%) when routed through
195:the substrate's 600-cell graph. This is **+40.6pp of geometric
196:amplification**, far exceeding the +15pp prereg threshold.
199:failure of the reset protocol (substrate state drifted toward
201:classification structure). With the reset protocol now wired in, the
202:lift is restored to +40.6pp. See `NON_EQUILIBRIUM_FINDING.md` for the
208:- 53.1% raw → 93.8% substrate-routed at canonical depth (n=25)
210:- 83.1% 5-fold CV at fresh seeds
211:- Goldilocks optimum at n=25 ticks of substrate evolution
213:The +40.6pp lift is roughly an order of magnitude above the +15pp
214:preregistered floor. The 65.4% null mapping shows two-thirds of the
234:### 3.2 P14 — Raw 5-fold CV
236:**Threshold:** Conversation raw 5-fold CV ≥ 75%.
241:discriminative — 87.5% raw classification at 5-fold CV exceeds the
242:chess raw rate (53.1% LOO) by ~34pp. There is little headroom for
253:Raw 5-fold CV:               87.5%
254:Substrate 5-fold CV (n=25):  83.1%
262:preregistered window, and the negative sign suggests minor noise
289:| Chess (LOO) | 53.1% | 93.8% | n/a | n/a | +40.6pp lift |
290:| Chess (5-fold CV) | n/a | 83.1% | 65.4% | 65.4% | +17.7pp |
291:| Conversation (5-fold CV) | 87.5% | 83.1% | 70.6% | 70.6% | +12.5pp (raw vs null) |
301:substrate routing at 83.1% (lift −4.4pp) is within preregistered
311:**Reference cohort:** Human Connectome Project (HCP), n=1003 subjects.
312:For preregistered tests, n=100 subjects (computational tractability)
313:in ICA-50 parcellation. The full-cohort effects (n=1003) match the
314:n=100 subset within standard error.
316:**Method:** Build group-averaged ICA-50 connectivity matrix; threshold
328:**Result:** 0.0000 (exactly).
340:**Result (n=100 subjects, density 0.101):** **3.388**.
347:**ARIA is at −11.58σ** below the HCP cohort mean on this metric:
348:ARIA's degree std is 0; HCP n=1003 mean is 3.28 ± 0.28; the gap is
349:(0 − 3.28) / 0.28 = −11.7σ. **Zero of 1003 HCP subjects** have
352:### 4.4 Higher-order graph statistics (full cohort, n=1003)
358:Metric                 ARIA     HCP n=1003 mean   σ from HCP
360:Degree std             0.000    3.28 ± 0.28        −11.58σ
361:Participation ratio    68.54    19.72 ± 0.61       +79.78σ
362:Clustering coefficient 0.455    0.220              +6.80σ
371:  Real cortex is hub-concentrated; ARIA is uniform. +79.78σ.
375:  +6.80σ.
387:methodology: instead of comparing real cortex to a stochastic null
390:giving precise effect-size statements like "real cortex is +79.78σ
395:parcellation choice, density threshold, and subject inclusion
418:ARIA's degree std = 0 (theorem); HCP n=1003 degree std = 3.28 ± 0.28,
419:range [2.55, 4.16], with zero of 1003 subjects below 2.0. ARIA is
420:−11.58σ on degree homogeneity, +79.78σ on participation ratio, and
421:+6.80σ on clustering coefficient. The substrate functions as a
433:hand-features is at chance-class (53.1% raw LOO), substrate routing
434:amplifies to 93.8% LOO (+40.6pp lift) and 83.1% 5-fold CV across fresh
440:is correctly null (lift −4.4pp, well within preregistered neutrality
442:unconditional booster. On HCP brain functional connectivity (n=1003,
444:std = 0) is −11.58σ below the biological mean (3.28 ± 0.28); on
445:participation ratio ARIA at 68.54 is +79.78σ above HCP (19.72 ± 0.61),
446:and on clustering coefficient ARIA at 0.455 is +6.80σ above HCP (0.220).
459:The contrast between chess (+40.6pp lift) and conversation (−4.4pp
479:reference for biological cortex. The σ-distances (−11.58σ, +79.78σ,
480:+6.80σ) quantify the magnitude of biological symmetry-breaking, with
493:python3 run_preregistered_validation.py
502:- HCP n=100 ICA-50: deterministic from group average
509:JSON outputs land in `~/.aria/preregistered_validation/results_*.json`.
516:1. **Chess test is small (32 positions, 4 categories).** The ~93.8%
518:   chess test bench would strengthen the lift claim. The 5-fold CV
519:   at 83.1% is a more conservative readout (4-category random
520:   subsamples rather than full LOO).
551:- `run_preregistered_validation.py` — full P1–P18 harness
559:  with pressure-field dynamics; `homeostatic_reset(level=1.0)` is
560:  the reset method.
567:  preregistered tally
568:- `docs/brain_mapping/P4_SYNERGY_FINDING.md` — synergy deep-dive
573:  state-drift diagnostic; rationale for `homeostatic_reset()`
583:- `project_preregistered_validation_17_of_18.md` — re-run summary
===== docs/brain_mapping/PAPER_PREDICTIONS.md =====
10:- a **pass threshold** (interval, inequality, or categorical match)
43:### P4. C×P synergy is positive and substantial
65:  2.513 [2.504, 2.526]. A different seed's bootstrap CI should
78:- **Claim**: Mean N3/W switching ratio **< 0.50**.
88:### P9. Chess 5-fold CV ≥ chance + substantial margin
89:- **Claim**: 5-fold CV on v2 features at n=25 ticks, 5 fresh seeds
92:  < 70% would mean our 84.4% LOO number was misleadingly inflated.
93:- **Run**: `run_chess_pattern_readout.py` + 5-fold with fresh seeds.
115:### P13. Substrate lift on chess v2 is positive
116:- **Claim**: At n=25, substrate ≥ raw **+ 15pp** on 5-fold CV (fresh
127:- **Claim**: Raw conversation 5-fold CV accuracy **≥ 75%** on fresh
129:- **Rationale**: Discovery gave 87.5% LOO. If much lower, the
138:- **Run**: 5-fold CV raw vs substrate on fresh seeds.
160:  density-matched threshold.
184:## Success thresholds
192:We do not expect 18/18 — some are noisy empirical tests and statistical
===== docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md =====
20:Only a **reset mechanism** analogous to biological sleep restores
27:### E1 — Drift curve (30 consecutive classifications, no reset)
32:| 2 | 93.8% | 100 | 147.9 | 1.000 |
43:### E2 — Homeostatic reset
49:| **Full reset** | **87.5% (higher than fresh)** |
50:| Partial reset (50% decay) | 81.2% |
52:**Full reset restores AND improves on the fresh state**. Because
54:full reset clears those, leaving the substrate genuinely canonical.
99:| P13 preregistration fail | polytope drifted to equilibrium across evaluations |
121:pre-loaded "ignited" state is SOC; steady operation without reset
132:during wake. Our reset operation is a direct computational analogue.
134:synaptic downscaling — exactly what our `_homeostatic_reset` does
141:If sleep is the biological analogue of our reset operation:
149:  reset dynamics (higher or more variable, as the substrate is
203:   to test the "SWS = substrate reset" prediction
205:4. ⏳ Add homeostatic reset API to DimensionalMonitor
206:5. ⏳ Re-run preregistered validation with proper reset — convert
207:   P13 from FAIL to the PASS it deserves
229:- Sleep-like reset is the thermodynamic necessity
===== docs/brain_mapping/MANUSCRIPT_V2.md =====
23:preregistered before the validation runs (frozen 2026-04-18). We
27:α = 2.252, 95% CI [1.82, 2.86] (R² = 0.956), with three-way confidence
28:interval overlap with real Sleep-EDFx EEG (α = 2.51, CI [2.50, 2.53])
31:regime-switching elevates 1.83× wake; propofol continuity drops by
32:0.066; propofol integrated information Φ collapses to 0.33× wake (IIT
36:exhibit a strong synergistic interaction of +0.190 (95% bootstrap CI
37:[+0.143, +0.239]), comparable in magnitude to the P main effect
42:recognition by +40.6 percentage points (raw 53.1% → substrate-routed
43:93.8% on leave-one-out at canonical depth) but is correctly null on
46:HCP brain functional connectivity (n=1003 subjects), ARIA serves as a
48:(theorem); HCP degree std = 3.28 ± 0.28; ARIA is at −11.58σ on degree
49:homogeneity and +79.78σ on participation ratio. With the N=20
50:deep-dive, the empirical tally is 18/18 preregistered predictions
51:plus 6/6 drug/sleep signatures; no claim is walked back. This is the
54:preregistered tests.
57:avalanches, integrated information, drug/sleep EEG, preregistered
129:`O*` within a preregistered threshold. We report two non-overlapping
132:**Set A: Eighteen preregistered predictions** (frozen 2026-04-18 in
135:chess pattern recognition (P9–P13), conversation utterance
141:propofol switching, propofol continuity disruption, propofol Φ
146:thresholds (with the methodological caveat that two interaction
147:predictions, P3 and P4, require N ≥ 5 and N ≥ 20 respectively for
232:A vertex "crosses" once its accumulated pressure exceeds a threshold;
237:2⁴ ablation in the preregistered validation (P1–P5).
249:preregistered |·| < 0.20 independence band).
266:High-pressure uncrossed vertices (above threshold but not yet
287:the preregistered |·| < 0.15 null band. E is a structural completeness
294:estimated at +0.044 — below the preregistered +0.10 threshold —
310:  point estimate:           +0.190
311:  95% CI:                   [+0.143, +0.239]
312:  P(interaction ≤ 0):       0.0000
313:  P(interaction < +0.10):   0.0000
316:The 95% CI is **entirely above the preregistered +0.10 threshold**;
327:| **20** | **+0.190, CI [+0.143, +0.239]** | **decisively above** |
331:With adequate N, the synergy is in fact ~90% above the preregistered
393:### 4.2 The bounded-top-K thresholding
445:WAKE composite = 0.943; PROPOFOL composite = 0.877; drop = +0.066.
558:run. Each prediction has a falsifiable threshold (numerical band or
560:`run_preregistered_validation.py`; it is git-tracked, deterministic
563:**Critical: no threshold has been modified post-hoc. The original
565:methodology required improvement (cascade block N, reset protocol,
566:deep-dive N), this is documented as a methodological refinement,
567:not as a threshold change.
571:The cascade ablation block (P1–P5 + interaction tests P3, P4) tests
581:Both interaction tests in the original preregistration set (P3, P4)
583:−0.183, inside |·|<0.20 band). P4 closes only at N = 20 (C×P = +0.190,
584:CI [+0.143, +0.239]).
587:preregistering interaction terms with high per-seed variance, allocate
590:### 5.7 The non-stationarity finding and reset protocol
597:The fix is `homeostatic_reset(level=1.0)` — a method that
599:training state to canonical baseline. With reset between depth
600:measurements, chess LOO classification recovers from collapsed
601:+3.1pp lift (without reset, on a state-drifted substrate) to +40.6pp
602:lift (with reset, far exceeding the preregistered +15pp floor).
605:Implementation: `kernel/dimensional_monitor.py:DimensionalMonitor.homeostatic_reset`.
609:specify state-reset protocol**.
622:EEG within preregistered tolerance.
628:**Result (preregistered re-run 2026-04-29, 5 seeds):**
633:| Real EEG (Sleep-EDFx, n=30) | 2.51 | [2.50, 2.53] | > 0.85 | varies per subject |
635:| v4 WAKE consciousness chain | 2.252 | [1.82, 2.86] | 0.956 | 58 |
646:preregistered fits.
651:bounded top-K thresholding and IIT-style Φ, reproduces six independent
654:**Method.** Four conditions × 800 ticks at seed = 42, k_threshold = 12.
662:WAKE       58   2.252   [1.82, 2.86]   0.956  2.18e-05    0.0008   0.943
665:RECOVERY   58   2.252   [1.82, 2.86]   0.956  2.18e-05    0.0008   0.943
672:| 1 | NREM-N3 variance ratio (vs Wake) | Sleep-EDFx W→N3 (n=24) | ≈ 0.365 | **0.463** | ✓ |
673:| 2 | Propofol regime-switching ratio | OpenNeuro ds005620 (n=8, 2.96×) | ∈ [1.5, 5.0] | **1.83×** | ✓ |
674:| 3 | Propofol continuity drop | EEG microstate (Brodbeck 2012) | > 0.020 | **+0.066** | ✓ |
675:| 4 | Propofol Φ collapse (IIT) | Tononi 2008 | ratio < 0.50 | **0.33×** | ✓ |
677:| 6 | Wake cortical-avalanche α | n=30 Sleep-EDFx CI [2.50, 2.86] | α ∈ [1.5, 3.5], R²>0.85 | **2.252 [1.82, 2.86] R²=0.956** | ✓ |
679:All six signatures pass at preregistered thresholds. The wake cascade-α
686:Φ collapse on propofol (0.33× wake) is consistent with the Tononi
689:2.96× empirically); the NREM-N3 variance collapse magnitude is
694:### 6.3 Causal mechanism isolation: C and P strongly synergistic (P2, P3, P4, P5)
707:C main:  +0.621  (≥ +0.30 prereg threshold)        ✅ P2
722:| **C × P (P4)** | **20** | **+0.190** | **[+0.143, +0.239]** | **✅ strongly synergistic** |
731:| **20** | **32000–32019** | **+0.190** | **[+0.143, +0.239]** |
733:P(synergy ≤ 0) = 0.0000; P(synergy < +0.10) = 0.0000.
749:Detail: `docs/brain_mapping/P4_SYNERGY_FINDING.md`.
762:  ticks; classifier 1-NN cosine similarity with k-fold CV or LOO.
766:  order statistics to HCP n=1003 ICA-50 group-averaged connectivity
767:  (density-matched threshold = 0.101).
769:**Chess result (with `homeostatic_reset` between depth measurements):**
772:P9  — 5-fold CV (fresh seeds 30200-30204):     83.1%  ≥ 70%   ✅
775:P12 — goldilocks peak depth:                   n=25   ∈ {15,25,40,60}  ✅
776:P13 — LOO substrate lift (raw 53.1% → 93.8%):  +40.6pp ≥ +15pp  ✅
778:Depth sweep (with reset, fresh seed):
779:  n=5:    53.1%
780:  n=15:   65.6%
781:  n=25:   93.8%   ← peak
784:  n=100:  78.1%
790:P14 — raw 5-fold CV (fresh seeds 30220-30224):   87.5%  ≥ 75%  ✅
795:**HCP result (n=1003 subjects, ICA-50):**
797:| Metric | ARIA | HCP n=1003 mean | σ from HCP |
799:| Degree std | 0.000 (theorem) | 3.28 ± 0.28 | **−11.58σ** |
800:| Participation ratio | 68.54 | 19.72 ± 0.61 | **+79.78σ** |
801:| Clustering coefficient | 0.455 | 0.220 | +6.80σ |
804:P17 — ARIA degree std (theorem):              0.0000  = 0.00  ✅
805:P18 — HCP ICA-50 degree std:                  3.388   > 2.0   ✅
808:Zero of 1003 HCP subjects have degree std below 2.0; ARIA is far
813:(i) **Selective amplification.** The contrast between chess (+40.6pp
814:lift on LOO) and conversation (−4.4pp lift) demonstrates the substrate
816:53.1% is barely above chance (25% for 4 categories); the substrate
817:amplifies to 93.8% (near-perfect). Conversation raw at 87.5% is
830:symmetry-breaking. The σ-distances (−11.58σ on degree, +79.78σ on
835:### 6.5 The eighteen preregistered predictions: 17/18 standard, 18/18 with N=20 P4
837:**Method.** Run `run_preregistered_validation.py` with 5-seed cascade
838:block + `homeostatic_reset` wired in. Run `demo_p4_cxp_deep_dive.py`
839:at N=20 for the residual P4. Tally pass/fail per preregistered threshold.
848:| **P4** | **C×P synergy** | **≥ +0.10** | **+0.190 [+0.143, +0.239] (N=20)** | **✅** |
852:| P8 | W→N3 switching ratio | < 0.50 | 0.058 | ✅ |
853:| P9 | Chess 5-fold CV | ≥ 70% | 83.1% | ✅ |
856:| P12 | Chess goldilocks peak | ∈ {15, 25, 40, 60} | n=25 | ✅ |
857:| P13 | Chess LOO lift (with reset) | ≥ +15pp | +40.6pp | ✅ |
858:| P14 | Conv raw 5-fold CV | ≥ 75% | 87.5% | ✅ |
861:| P17 | ARIA degree std (theorem) | = 0 | 0.0000 | ✅ |
862:| P18 | HCP degree std | > 2.0 | 3.388 | ✅ |
864:**Tally: 17/18 at standard validation; 18/18 with N=20 deep-dive on P4.**
866:**Comparison to the original 2026-04-20 run (15/18):**
872:- **P4** (C×P synergy): +0.044 at N=3 → +0.190 at N=20. Same
874:- **P13** (chess LOO lift): +3.1pp without reset → +40.6pp with reset.
876:  resolved by `homeostatic_reset(level=1.0)` between measurements.
878:**No threshold has been modified.** The original predictions are
879:confirmed in their original form, with two methodological refinements
880:(adequate N for high-variance interactions; reset protocol for multi-
895:group theory; cascade-α matches Sleep-EDFx within preregistered
896:tolerance; six drug/sleep signatures pass at preregistered thresholds.
908:**(3) The 18/18 preregistered claim with no threshold modification.**
909:Every prediction in the preregistered set passes at empirical
910:thresholds. The two interaction tests (P3, P4) required higher N
911:than the original 3-seed protocol, and one test (P13) required the
912:documented reset protocol; we report this honestly as methodology
913:refinement, not as a post-hoc threshold change.
918:propofol (0.33× wake). The substrate's symmetry-breaking is what
972:preregistered validation hit Type II false negatives on both
973:interaction tests (P3 and P4); both close at higher N without
974:threshold modification.
976:For preregistration design more broadly: when preregistering an
995:{12, 6φ, 4φ, 3} by character theory). The σ-distances (−11.58σ on
996:degree homogeneity, +79.78σ on participation ratio) far exceed any
1044:4. **Sig 2 ratio (1.83×) is below empirical point estimate (2.96×)**
1051:   ~93.8% substrate-routed accuracy is on a small evaluation set.
1070:1. **One seed range tested at N=20** for P4. A second N=20 run at a
1072:   reproducibility of the +0.190 estimate.
1079:3. **The original predictions were preregistered in 2026-04-18**,
1113:| Eighteen preregistered (§6.5) | `python3 run_preregistered_validation.py` | ~18 min | JSON + log |
1125:- k_threshold = 12 (cortical band; bounded_topk nonlinearity)
1134:For the preregistered validation (`run_preregistered_validation.py`):
1140:- HCP: deterministic (n=100 ICA-50 group average)
1151:# Run preregistered set
1152:python3 run_preregistered_validation.py
1159:overlaps, P-value thresholds) should be unaffected.
1170:| `dimensional_monitor.py` | Pressure-field cascade dynamics; the four mechanisms (D, C, P, E); homeostatic_reset |
1186:| `run_preregistered_validation.py` | Eighteen-prediction harness (§6.5) |
1193:| `docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md` | Full preregistered tally (this work) |
1195:| `docs/brain_mapping/P4_SYNERGY_FINDING.md` | Strong-coupling architectural finding (this work) |
1211:preregistered neuroscience correspondences plus six independent
1219:(+0.190, 95% CI [+0.143, +0.239] at N=20) is comparable in magnitude
1221:preregistered validation underestimated this synergy by 5× due to
1227:top-K thresholding and an IIT-style integrated information proxy,
1229:substrate. Wake cortical-avalanche power law has α = 2.252,
1234:classification tasks (chess +40.6pp lift; conversation correctly null
1236:cortical functional connectivity (HCP n=1003: ARIA at −11.58σ on
1237:degree homogeneity, +79.78σ on participation ratio).
1241:preregistered tests with no walked-back claims. The architectural

exec
/bin/bash -lc "cd '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess' && echo '---P4---'; nl -ba docs/brain_mapping/P4_SYNERGY_FINDING.md | sed -n '1,180p'; echo '---Cross---'; nl -ba docs/brain_mapping/CROSS_DOMAIN_RESULTS.md | sed -n '1,230p'; echo '---Validation 1-150---'; nl -ba docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md | sed -n '1,150p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 258ms:
---P4---
     1	# The C×P Synergy: Strong Coupling Between Two Cascade-State Stabilisers
     2	
     3	*Standalone publishable finding from N=20 seed deep-dive on the residual P4
     4	preregistered prediction. Compiled 2026-04-29.*
     5	
     6	> **Headline.** Two of ARIA's four cascade mechanisms — **context rotation
     7	> (C)** and **partial emission (P)** — are causally significant. With
     8	> adequate replication (N ≥ 20 fresh seeds), their **interaction effect
     9	> on cascade-α is +0.190, 95% bootstrap CI [+0.143, +0.239]** — comparable
    10	> in magnitude to the **P main effect of −0.218** and ~90% above the
    11	> preregistered prediction of ≥+0.10. The original 3-seed preregistered
    12	> validation underestimated this synergy by 5×; the underestimate was a
    13	> Type II false negative compounded by seed-range sampling bias on a
    14	> high-per-seed-variance interaction term. The corrected reading reverses
    15	> the prior architectural claim: C and P are **strongly coupled critical-
    16	> state stabilisers**, not nearly-orthogonal ones.
    17	
    18	---
    19	
    20	## 1. Background: what was preregistered, what failed at N=3
    21	
    22	### 1.1 The four cascade mechanisms
    23	
    24	ARIA's substrate is the 600-cell regular 4-polytope (120 vertices,
    25	uniform degree 12, H₄ Coxeter symmetry). On top of the static graph,
    26	substrate **dynamics** are driven by a pressure-field over each vertex,
    27	with four mechanisms acting on the field:
    28	
    29	- **D — D₄ orbit coupling.** The H₄ root system contains five disjoint
    30	  24-cells (D₄ orbits). A small (0.05) cross-orbit pressure averaging
    31	  prevents cascades from localising to one orbit.
    32	- **C — Context rotation.** The active observer frame on the S⁷ rung
    33	  rotates periodically based on which uncrossed vertices have
    34	  accumulated pressure aligning with each frame's preferences.
    35	  Implementation: `kernel/dimensional_monitor.py:316-318`.
    36	- **P — Partial emission.** High-pressure uncrossed vertices (above
    37	  threshold but not yet crossed) emit pressure at 30% scale, saturating
    38	  at pressure 3.0. Without this mechanism, only fully-crossed vertices
    39	  emit. Implementation: `kernel/dimensional_monitor.py:842-855`.
    40	- **E — Equator compensation.** Sparse-degree vertices on the H₃
    41	  shell-4 equator (corpus-callosum analogue) get a degree-compensation
    42	  multiplier so they overcome their connectivity deficit.
    43	
    44	The cascade-α (the slope of the avalanche-size power-law) is the
    45	empirical readout for cortex-like criticality. Preregistration tests
    46	each mechanism's effect on cascade-α via 2⁴ ablation.
    47	
    48	### 1.2 The preregistered predictions for D/C/P/E mechanisms
    49	
    50	Predictions frozen 2026-04-18 in `docs/brain_mapping/PAPER_PREDICTIONS.md`:
    51	
    52	| ID | Prediction | Threshold |
    53	|---|---|---|
    54	| P1 | Cascade α SOC range | ∈ [2.5, 3.5] |
    55	| P2 | C main effect | ≥ +0.30 |
    56	| **P3** | **\|D×C\| < 0.20** (independence) | \|·\| < 0.20 |
    57	| **P4** | **C×P synergy ≥ +0.10** | ≥ +0.10 |
    58	| P5 | \|E main effect\| < 0.15 (null) | \|·\| < 0.15 |
    59	
    60	**P4 was the genuine architectural prediction:** because C creates variety
    61	in *which* vertices are uncrossed, and P promotes high-pressure uncrossed
    62	vertices to mini-emitters, their composition should generate a non-additive
    63	contribution to cascade-α. The preregistered floor was +0.10 — stating
    64	that the synergy must be at least 10% of the main-effect scale.
    65	
    66	### 1.3 What the original validation reported
    67	
    68	Original validation (2026-04-20, 3 seeds per condition):
    69	
    70	```
    71	Means (N=3 each):
    72	  ----  baseline:    α = 3.020
    73	  -C-- (C off):      α = 3.612
    74	  --P- (P off):      α = 2.844
    75	  -CP- (both off):   α = 3.530
    76	```
    77	
    78	Computing the C×P interaction:
    79	
    80	```
    81	C×P = ((α(CP-off) + α(baseline)) − (α(C-off) + α(P-off))) / 2
    82	    = ((3.530 + 3.020) − (3.612 + 2.844)) / 2
    83	    = (6.550 − 6.456) / 2
    84	    = +0.047
    85	```
    86	
    87	This was below the +0.10 threshold, so P4 was reported as a **fail**
    88	in the headline 15/18 result. The walk-back was:
    89	
    90	> *"Partial emission interaction with C requires larger-N replication;
    91	> report as preliminary."*
    92	
    93	We took this at face value at the time and weakened the claim. **The
    94	N=20 deep-dive presented below shows this was wrong.**
    95	
    96	---
    97	
    98	## 2. The N=20 deep-dive (2026-04-29)
    99	
   100	### 2.1 Method
   101	
   102	We ran the same 4-condition ablation (baseline, -C--, --P-, -CP-) at:
   103	
   104	- **N = 20 fresh seeds** (range 32000–32019, non-overlapping with prior
   105	  validation seeds 30000s).
   106	- **150 epochs per run** (matching original validation).
   107	- **All other ablation flags off** — the test isolates C × P with
   108	  D, E held on.
   109	
   110	We computed the C×P interaction estimate per the standard 2×2 factorial
   111	formula:
   112	
   113	```
   114	interaction = ((α_CP-off + α_baseline) − (α_C-off + α_P-off)) / 2
   115	```
   116	
   117	We then bootstrapped the interaction distribution (2000 resamples,
   118	seeded) over the 20-seed sample to get a 95% confidence interval, plus
   119	one-sided P(interaction ≤ 0) and P(interaction < +0.10).
   120	
   121	The full script is `demo_p4_cxp_deep_dive.py`. Wallclock was 1706 s
   122	(28 min) on a single CPU. The script also reports identical-N runs at
   123	N = 10 (range 31000–31009) for trend analysis.
   124	
   125	### 2.2 Per-condition means at N=20
   126	
   127	```
   128	cond     mean α   std    sem    individual seeds (n=20)
   129	----     3.008   0.090  0.020   [2.905, 3.013, 3.005, 3.087, 3.136, 3.022, 3.075, 2.879, 2.880,
   130	                                  2.999, 2.947, 3.002, 3.258, 2.946, 2.984, 2.959, 2.952, 3.079,
   131	                                  2.998, 3.033]
   132	-C--     3.464   0.097  0.022   [3.536, 3.444, 3.302, 3.613, 3.311, 3.503, 3.458, 3.540, 3.573,
   133	                                  3.421, 3.514, 3.419, 3.281, 3.617, 3.364, 3.460, 3.542, 3.414,
   134	                                  3.480, 3.492]
   135	--P-     2.790   0.086  0.019   [2.783, 2.873, 2.794, 2.749, 2.880, 2.791, 2.744, 2.845, 2.631,
   136	                                  2.850, 2.731, 2.953, 2.816, 2.761, 2.758, 2.696, 2.704, 2.830,
   137	                                  2.666, 2.949]
   138	-CP-     3.628   0.161  0.036   [3.932, 3.773, 3.557, 3.656, 3.325, 3.469, 3.617, 3.840, 3.617,
   139	                                  3.714, 3.409, 3.733, 3.480, 3.628, 3.670, 3.840, 3.531, 3.724,
   140	                                  3.649, 3.391]
   141	```
   142	
   143	### 2.3 Main-effect estimates at N=20
   144	
   145	```
   146	C main effect (turn C off, leave P/D/E on):  α(-C--) − α(----) = +0.456
   147	P main effect (turn P off, leave C/D/E on):  α(--P-) − α(----) = −0.218
   148	```
   149	
   150	C raises α by 0.46 when removed; P lowers α by 0.22 when removed.
   151	
   152	### 2.4 The interaction estimate
   153	
   154	Direct calculation from means:
   155	
   156	```
   157	C×P interaction = ((3.628 + 3.008) − (3.464 + 2.790)) / 2
   158	                = (6.636 − 6.254) / 2
   159	                = +0.191
   160	```
   161	
   162	Bootstrap (2000 resamples) on the 20-seed sample gives:
   163	
   164	```
   165	C×P bootstrap mean:           +0.190
   166	C×P 95% bootstrap CI:         [+0.143, +0.239]
   167	P(interaction ≤ 0):           0.0000
   168	P(interaction < +0.10):       0.0000
   169	```
   170	
   171	**The 95% CI is entirely above the preregistered +0.10 threshold.**
   172	The synergy is decisively positive (p = 0 against zero) and decisively
   173	above prereg (p = 0 against +0.10).
   174	
   175	### 2.5 Per-seed paired interactions
   176	
   177	For each seed (paired across the four conditions), we can compute that
   178	seed's interaction estimate:
   179	
   180	```
---Cross---
     1	# Cross-Domain Validation: Chess, Conversation, and HCP Connectivity
     2	
     3	*Standalone consolidation of ARIA's three cross-domain validation tracks.
     4	Compiled 2026-04-29. Self-contained for paper inclusion.*
     5	
     6	> **Headline.** The 600-cell substrate functions as a **selective
     7	> amplifier** on real-world classification tasks: it lifts performance
     8	> when raw features are ambiguous (chess: +40.6 percentage points on
     9	> leave-one-out, raw 53.1% → substrate-routed 93.8%) and is correctly
    10	> null when raw features already saturate (conversation: 87.5% raw,
    11	> substrate −4.4pp). On structural connectivity, ARIA is the **maximum-
    12	> symmetry null reference** for cortex: ARIA degree std = 0 (H₄
    13	> transitivity); HCP n=1003 degree std = 3.28 ± 0.28; ARIA is
    14	> −11.58σ on degree homogeneity and +79.78σ on participation ratio,
    15	> placing ARIA two orders of magnitude away from biological cortex on
    16	> functional-specialisation metrics. Symmetry-breaking is precisely
    17	> the biological content that distinguishes real cortex from the
    18	> H₄ baseline.
    19	
    20	---
    21	
    22	## 1. The cross-domain test rationale
    23	
    24	Three tracks test ARIA's substrate against domains where it has no
    25	domain-specific tuning:
    26	
    27	1. **Chess pattern recognition** (P9–P13 in the preregistered set):
    28	   classify chess positions by tactical / positional / endgame /
    29	   opening category from 8-dimensional V2 features (material balance,
    30	   king safety, pawn structure, etc.). Test whether the substrate's
    31	   geometry amplifies category structure beyond raw-feature
    32	   classification.
    33	
    34	2. **Conversation utterance categorisation** (P14–P16): classify
    35	   utterances by 8 dialogue-act categories from 8-dimensional features.
    36	   Test whether the substrate is correctly **null** on a domain where
    37	   raw features are already discriminative, validating that it is a
    38	   **selective** amplifier (not an unconditional one).
    39	
    40	3. **HCP brain connectivity** (P17–P18): compare ARIA's vertex-graph
    41	   degree distribution to real cortical functional connectivity from
    42	   the Human Connectome Project (n=1003 subjects, ICA-50
    43	   parcellation). Test whether ARIA serves as a quantifiable maximum-
    44	   symmetry null reference for cortex.
    45	
    46	All three are deterministic given seeds and substrate state. All five
    47	preregistered tests on chess + conversation pass at fresh seeds; both
    48	HCP tests pass deterministically (P17 from theorem; P18 from data).
    49	
    50	---
    51	
    52	## 2. Chess pattern recognition (P9–P13)
    53	
    54	### 2.1 Setup
    55	
    56	**Positions:** 32 chess positions from 4 categories (8 per category):
    57	tactical, positional, endgame, opening.
    58	
    59	**Features (V2):** 8 hand-engineered scalar features per position,
    60	normalised by per-feature norms `V2_NORMALISERS`:
    61	- Material balance
    62	- King safety (white + black, summed)
    63	- Pawn structure
    64	- Centre control
    65	- Piece activity
    66	- Mobility (legal moves count)
    67	- Threat density
    68	- Defensive structure
    69	
    70	Implementation: `run_chess_pattern_readout.py:extract_v2`.
    71	
    72	**Substrate routing:** features are injected as pressure into the
    73	substrate's S⁷ observer frames; the substrate is run forward by
    74	`n_ticks` (default 25); the resulting vertex pattern is used as the
    75	classification feature vector. Classifier: 1-nearest-neighbour on
    76	cosine similarity, validated by k-fold CV (k=5) or leave-one-out (LOO).
    77	
    78	Critical detail: between successive depth measurements, the substrate
    79	is reset to canonical state via `mon.homeostatic_reset(level=1.0)`.
    80	Without this, pressure-field state drifts toward equilibrium across
    81	~5 evaluations, washing out classification structure (see
    82	§2.5 and `NON_EQUILIBRIUM_FINDING.md`).
    83	
    84	### 2.2 P9 — Raw 5-fold cross-validation (fresh seeds)
    85	
    86	**Threshold:** Chess substrate-routed 5-fold CV ≥ 70%.
    87	
    88	**Result (fresh seeds 30200–30204):**
    89	
    90	```
    91	Per-seed accuracies:  81.2%, 81.2%, 84.4%, 87.5%, 81.2%
    92	Mean:                 83.1%
    93	```
    94	
    95	**Interpretation:** Substrate-routed classification at 5-fold CV is
    96	83.1% on the 32-position × 4-category task, well above the 70%
    97	threshold. Per-seed variance is small (range 81.2%–87.5%).
    98	
    99	For comparison, **discovery accuracy** on the same task was 84.4%;
   100	the fresh-seed mean of 83.1% replicates discovery within expected
   101	variance.
   102	
   103	### 2.3 P10 — Permutation null (feature → frame mapping)
   104	
   105	**Threshold:** Random permutation of feature → frame assignment
   106	preserves classification accuracy ≥ 50%.
   107	
   108	**Method:** Apply random permutation σ to the 8 V2 features, so each
   109	feature is assigned to a different S⁷ frame than canonical. Run
   110	substrate, classify. Repeat 15 times with seeded random permutations
   111	(seed 30210). Average accuracy across 15 trials.
   112	
   113	**Result:** 65.4% mean across 15 permutations.
   114	
   115	**Interpretation:** This is the most architecturally informative cross-
   116	domain finding. Even with feature → frame assignments randomised, the
   117	substrate retains 65.4% classification power — well above the 25%
   118	chance level for 4 categories. **Approximately 65pp of the
   119	classification accuracy comes from the substrate's geometric structure
   120	itself, not from semantic feature alignment.** The remaining ~17pp
   121	(83.1% − 65.4%) is the semantic alignment bonus.
   122	
   123	This decomposes substrate classification into:
   124	- **Geometric content (65%):** substrate amplifies category structure
   125	  regardless of which features map where. This is the H₄ symmetry
   126	  acting as a selective amplifier on any input — a domain-invariant
   127	  null floor.
   128	- **Semantic content (17pp):** alignment of specific features to
   129	  specific frames adds accuracy on top of the geometric floor. This
   130	  is the domain-specific contribution.
   131	
   132	### 2.4 P11 — Random-label baseline
   133	
   134	**Threshold:** Random-label classifier accuracy ∈ [15%, 35%] (chance
   135	for 4 categories ≈ 25%).
   136	
   137	**Method:** Shuffle category labels randomly, classify the substrate-
   138	routed patterns, repeat 20 times with different seeds.
   139	
   140	**Result:** 23.4% mean across 20 trials.
   141	
   142	**Interpretation:** With shuffled labels, classification drops to chance
   143	(23.4% ≈ 25% chance). This confirms the 83.1% raw and 65.4% null are
   144	not artefacts — they are real signal that disappears when category
   145	structure is destroyed.
   146	
   147	### 2.5 P12 — Goldilocks peak depth
   148	
   149	**Threshold:** Optimal substrate depth ∈ {15, 25, 40, 60} ticks.
   150	
   151	**Method:** Run the substrate at six different `n_ticks` values
   152	(5, 15, 25, 40, 60, 100) and report classification accuracy at each
   153	depth, with `homeostatic_reset(level=1.0)` between measurements.
   154	
   155	**Result (fresh seed):**
   156	
   157	```
   158	n_ticks  accuracy
   159	   5     53.1%
   160	  15     65.6%
   161	  25     93.8%   ← peak
   162	  40     84.4%
   163	  60     84.4%
   164	 100     78.1%
   165	```
   166	
   167	**Interpretation:** The substrate has a clear optimal depth around
   168	n=25, with a roll-off both at shallower depth (insufficient
   169	integration) and deeper depth (substrate equilibrates and loses
   170	specificity). The "goldilocks" structure mirrors cortical integration
   171	literature (Thorpe / Kiani): perceptual integration has an optimal
   172	time window, with shorter giving noisy classification and longer
   173	giving over-integration.
   174	
   175	### 2.6 P13 — Substrate lift on LOO with reset protocol
   176	
   177	**Threshold:** Substrate-routed LOO accuracy − raw-feature LOO
   178	accuracy ≥ +15 percentage points.
   179	
   180	**Method:** Run LOO classification on (a) raw 8-dim V2 features and
   181	(b) substrate-routed patterns at n=25, with reset between depth
   182	measurements.
   183	
   184	**Result:**
   185	
   186	```
   187	Raw features (LOO, 1-NN cosine):       53.1%
   188	Substrate-routed (n=25, with reset):   93.8%
   189	Lift:                                  +40.6 percentage points
   190	```
   191	
   192	**Interpretation:** The substrate amplifies the chess-position
   193	discrimination from chance-level on raw features (53.1% on 4 categories
   194	is just above chance-25%) to near-perfect (93.8%) when routed through
   195	the substrate's 600-cell graph. This is **+40.6pp of geometric
   196	amplification**, far exceeding the +15pp prereg threshold.
   197	
   198	The original 2026-04-20 validation reported this lift at +3.1pp — a
   199	failure of the reset protocol (substrate state drifted toward
   200	equilibrium across the prior depth-sweep measurements, collapsing the
   201	classification structure). With the reset protocol now wired in, the
   202	lift is restored to +40.6pp. See `NON_EQUILIBRIUM_FINDING.md` for the
   203	diagnostic details.
   204	
   205	### 2.7 Chess summary
   206	
   207	The substrate is a **strong geometric amplifier** on chess:
   208	- 53.1% raw → 93.8% substrate-routed at canonical depth (n=25)
   209	- 65.4% null mapping (architecture-invariant geometric floor)
   210	- 83.1% 5-fold CV at fresh seeds
   211	- Goldilocks optimum at n=25 ticks of substrate evolution
   212	
   213	The +40.6pp lift is roughly an order of magnitude above the +15pp
   214	preregistered floor. The 65.4% null mapping shows two-thirds of the
   215	amplification is from geometric structure alone, not from how features
   216	are assigned to frames.
   217	
   218	---
   219	
   220	## 3. Conversation utterance categorisation (P14–P16)
   221	
   222	### 3.1 Setup
   223	
   224	**Utterances:** 8 categories (greetings, questions, agreements,
   225	clarifications, etc.) × 8 utterances per category = 64 utterances.
   226	
   227	**Features:** 8-dimensional injection-row features per utterance.
   228	Source: `run_conversation_readout.py:_injection_row, _build_tables`.
   229	
   230	**Substrate routing:** identical to chess — features injected as
---Validation 1-150---
     1	# Preregistered Validation — Results (2026-04-29 update)
     2	
     3	*This document supersedes `VALIDATION_RESULTS.md` (2026-04-20, 15/18).
     4	It records the most recent run of the preregistered validation harness
     5	plus the N=20 deep-dive on the residual P4 prediction.*
     6	
     7	> **Headline:** **17 / 18 predictions pass at standard validation;
     8	> 18 / 18 with N=20 deep-dive on the residual P4.** Original 15/18
     9	> result reflected three honest walks-back from underpowered cascade-
    10	> ablation interaction tests and an unspecified reset protocol for the
    11	> chess LOO test. With (a) cascade block bumped from 3 to 5 seeds per
    12	> condition, (b) `homeostatic_reset(level=1.0)` wired in between depth
    13	> measurements for chess LOO, and (c) N=20 fresh-seed replication of
    14	> the C×P interaction test, all gaps close. The architecture's claim
    15	> set is fully validated against preregistered thresholds.
    16	
    17	---
    18	
    19	## 1. Provenance and protocol
    20	
    21	### 1.1 Preregistration
    22	
    23	Eighteen quantitative predictions were frozen on **2026-04-18** in
    24	`docs/brain_mapping/PAPER_PREDICTIONS.md`, before any validation run.
    25	Each prediction has a falsifiable threshold (numerical band or
    26	directional inequality). The validation harness is
    27	`run_preregistered_validation.py` — git-tracked, deterministic given
    28	seeds, produces JSON + log output.
    29	
    30	The preregistration was frozen because earlier "discovery runs" had
    31	14 correspondences with no protection against p-hacking. Without
    32	preregistration, claims are vulnerable to "you cherry-picked seeds"
    33	critiques. With it, claims survive.
    34	
    35	### 1.2 The original 2026-04-20 result
    36	
    37	The original validation run on 2026-04-20 reported **15/18 passes**:
    38	- All cascade main effects passed (P1, P2, P5).
    39	- All EEG/sleep deterministic re-runs passed (P6, P7, P8).
    40	- All cross-domain tests passed at fresh seeds (P9, P10, P11, P12,
    41	  P14, P15, P16, P17, P18).
    42	- **Three failed:**
    43	  - **P3** (D×C interaction independence): observed −0.231 at N=3,
    44	    outside |·| < 0.20 band.
    45	  - **P4** (C×P synergy): observed +0.044 at N=3, below +0.10 floor.
    46	  - **P13** (Chess LOO substrate lift ≥ +15pp): observed +3.1pp,
    47	    far below +15pp floor.
    48	
    49	The walks-back at the time were:
    50	- "P3, P4 walked back to 'preliminary, requires larger N'."
    51	- "P13 reframed as state-dependent — substrate state drifted toward
    52	  equilibrium across successive depth measurements; need to specify
    53	  reset protocol."
    54	
    55	### 1.3 What changed for the 2026-04-29 re-run
    56	
    57	Three improvements:
    58	
    59	1. **Cascade block N bumped 3 → 5** for P2, P3, P4, P5 conditions
    60	   in `run_preregistered_validation.py`. The original 3 seeds was
    61	   the source of high-variance failure on P3 and P4.
    62	
    63	2. **`homeostatic_reset(level=1.0)`** wired into the validation script
    64	   between depth-sweep measurements (lines 274–285 of the script).
    65	   This is the reset protocol identified post-hoc as necessary to
    66	   prevent pressure-field equilibration across LOO depth measurements
    67	   (`docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md`).
    68	
    69	3. **N=20 deep-dive** on the residual P4 (`demo_p4_cxp_deep_dive.py`):
    70	   ran the C×P interaction test at 20 fresh seeds (32000–32019) with
    71	   bootstrap 95% CI on the interaction estimate. See
    72	   `P4_SYNERGY_FINDING.md` for the standalone report.
    73	
    74	Wallclock for the standard re-run was 1101 s (~18 min).
    75	
    76	---
    77	
    78	## 2. Full results table — 2026-04-29 run
    79	
    80	| ID | Claim | Threshold | 2026-04-20 (3-seed) | **2026-04-29 (5-seed + reset + N=20 P4)** | Verdict |
    81	|---|---|---|---|---|---|
    82	| P1 | Cascade α ∈ [2.5, 3.5] | ∈ [2.5, 3.5] | 3.020 ✅ | **2.958** | ✅ |
    83	| P2 | Context-rotation main effect | ≥ +0.30 | +0.588 ✅ | **+0.621** | ✅ |
    84	| P3 | \|D×C interaction\| (independence) | \|·\| < 0.20 | −0.231 ❌ | **−0.183** | ✅ |
    85	| P4 | C×P synergy | ≥ +0.10 | +0.044 ❌ | **+0.190 at N=20, CI [+0.143, +0.239]** | ✅ at N=20 |
    86	| P5 | \|equator main effect\| (null) | \|·\| < 0.15 | +0.046 ✅ | **+0.046** | ✅ |
    87	| P6 | Real EEG α | ∈ [2.0, 3.0] | 2.513 ✅ | **2.513** | ✅ |
    88	| P7 | W→N3 variance ratio | < 0.70 | 0.365 ✅ | **0.365** | ✅ |
    89	| P8 | W→N3 switching ratio | < 0.50 | 0.058 ✅ | **0.058** | ✅ |
    90	| P9 | Chess 5-fold CV | ≥ 70% | 83.1% ✅ | **83.1%** | ✅ |
    91	| P10 | Chess null mapping | ≥ 50% | 65.4% ✅ | **65.4%** | ✅ |
    92	| P11 | Chess random-label | ∈ [15%, 35%] | 23.4% ✅ | **23.4%** | ✅ |
    93	| P12 | Chess goldilocks peak | ∈ {15, 25, 40, 60} | n=15 ✅ | **n=25** | ✅ |
    94	| P13 | Chess LOO substrate lift | ≥ +15pp (with reset) | +3.1pp ❌ | **+40.6pp** | ✅ |
    95	| P14 | Conv raw 5-fold CV | ≥ 75% | 87.5% ✅ | **87.5%** | ✅ |
    96	| P15 | \|conv substrate lift\| | \|·\| < 10pp | −4.4pp ✅ | **−4.4pp** | ✅ |
    97	| P16 | Conv null mapping | ≥ 50% | 70.6% ✅ | **70.6%** | ✅ |
    98	| P17 | ARIA degree std (theorem) | = 0.00 | 0.0000 ✅ | **0.0000** | ✅ |
    99	| P18 | HCP ICA-50 degree std | > 2.0 | 3.388 ✅ | **3.388** | ✅ |
   100	
   101	---
   102	
   103	## 3. Predictions that flipped to PASS — explained
   104	
   105	### 3.1 P3 — D×C interaction independence
   106	
   107	**Threshold:** \|D×C interaction\| < 0.20.
   108	
   109	**Original (N=3) failure:** −0.231. The interaction estimate fell just
   110	outside the independence band. Sign and magnitude were inconsistent with
   111	discovery (which had given +0.039).
   112	
   113	**2026-04-29 re-run (N=5):** −0.183. Now inside the independence band.
   114	The shift from −0.231 (N=3) to −0.183 (N=5) is the kind of stabilisation
   115	typical of high-variance interaction terms at small N — adding two
   116	seeds tightens the estimate enough to land inside the threshold.
   117	
   118	**Diagnosis:** classical Type II false negative on an interaction with
   119	high per-seed variance. With 3 seeds, the standard error on the
   120	interaction estimate is approximately 0.06–0.10; the threshold is
   121	±0.20; and a single bad-luck draw at N=3 can put the point estimate
   122	just outside. With 5 seeds (and clearer at 20+) the estimate stabilises.
   123	
   124	The architectural claim "D₄ and context rotation act independently on
   125	cascade-α" is **supported** by the N=5 re-run within the preregistered
   126	threshold. We do not claim point-zero independence (the estimate is
   127	slightly antagonistic, −0.183), but the magnitude is bounded inside
   128	the |·| < 0.20 band by direct measurement.
   129	
   130	### 3.2 P4 — C×P synergy
   131	
   132	This is the most consequential change. See the standalone report
   133	`P4_SYNERGY_FINDING.md` for the full story.
   134	
   135	**Threshold:** ≥ +0.10.
   136	
   137	**Original (N=3) failure:** +0.044. Below threshold.
   138	
   139	**2026-04-29 re-run (N=5):** +0.039. Still below threshold — confirming
   140	the N=3 reading at face value.
   141	
   142	**N=20 fresh-seed deep-dive (`demo_p4_cxp_deep_dive.py`, seeds 32000–32019):**
   143	
   144	```
   145	C×P bootstrap mean:           +0.190
   146	C×P 95% bootstrap CI:         [+0.143, +0.239]
   147	P(interaction ≤ 0):           0.0000
   148	P(interaction < +0.10):       0.0000
   149	```
   150	

exec
/bin/bash -lc "cd '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess' && nl -ba docs/brain_mapping/P4_SYNERGY_FINDING.md | sed -n '125,190p'; echo '--- cross relevant ---'; nl -ba docs/brain_mapping/CROSS_DOMAIN_RESULTS.md | sed -n '160,230p'; echo '--- cross hcp ---'; nl -ba docs/brain_mapping/CROSS_DOMAIN_RESULTS.md | sed -n '300,430p'; echo '--- validation 142-170 ---'; nl -ba docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md | sed -n '142,170p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 352ms:
   125	### 2.2 Per-condition means at N=20
   126	
   127	```
   128	cond     mean α   std    sem    individual seeds (n=20)
   129	----     3.008   0.090  0.020   [2.905, 3.013, 3.005, 3.087, 3.136, 3.022, 3.075, 2.879, 2.880,
   130	                                  2.999, 2.947, 3.002, 3.258, 2.946, 2.984, 2.959, 2.952, 3.079,
   131	                                  2.998, 3.033]
   132	-C--     3.464   0.097  0.022   [3.536, 3.444, 3.302, 3.613, 3.311, 3.503, 3.458, 3.540, 3.573,
   133	                                  3.421, 3.514, 3.419, 3.281, 3.617, 3.364, 3.460, 3.542, 3.414,
   134	                                  3.480, 3.492]
   135	--P-     2.790   0.086  0.019   [2.783, 2.873, 2.794, 2.749, 2.880, 2.791, 2.744, 2.845, 2.631,
   136	                                  2.850, 2.731, 2.953, 2.816, 2.761, 2.758, 2.696, 2.704, 2.830,
   137	                                  2.666, 2.949]
   138	-CP-     3.628   0.161  0.036   [3.932, 3.773, 3.557, 3.656, 3.325, 3.469, 3.617, 3.840, 3.617,
   139	                                  3.714, 3.409, 3.733, 3.480, 3.628, 3.670, 3.840, 3.531, 3.724,
   140	                                  3.649, 3.391]
   141	```
   142	
   143	### 2.3 Main-effect estimates at N=20
   144	
   145	```
   146	C main effect (turn C off, leave P/D/E on):  α(-C--) − α(----) = +0.456
   147	P main effect (turn P off, leave C/D/E on):  α(--P-) − α(----) = −0.218
   148	```
   149	
   150	C raises α by 0.46 when removed; P lowers α by 0.22 when removed.
   151	
   152	### 2.4 The interaction estimate
   153	
   154	Direct calculation from means:
   155	
   156	```
   157	C×P interaction = ((3.628 + 3.008) − (3.464 + 2.790)) / 2
   158	                = (6.636 − 6.254) / 2
   159	                = +0.191
   160	```
   161	
   162	Bootstrap (2000 resamples) on the 20-seed sample gives:
   163	
   164	```
   165	C×P bootstrap mean:           +0.190
   166	C×P 95% bootstrap CI:         [+0.143, +0.239]
   167	P(interaction ≤ 0):           0.0000
   168	P(interaction < +0.10):       0.0000
   169	```
   170	
   171	**The 95% CI is entirely above the preregistered +0.10 threshold.**
   172	The synergy is decisively positive (p = 0 against zero) and decisively
   173	above prereg (p = 0 against +0.10).
   174	
   175	### 2.5 Per-seed paired interactions
   176	
   177	For each seed (paired across the four conditions), we can compute that
   178	seed's interaction estimate:
   179	
   180	```
   181	per-seed C×P:
   182	[+0.259, +0.234, +0.233, +0.191, +0.135, +0.098, +0.245, +0.167,
   183	 +0.147, +0.221, +0.055, +0.182, +0.320, +0.098, +0.267, +0.322,
   184	 +0.118, +0.279, +0.251, −0.009]
   185	
   186	mean = +0.190,  std = 0.089,  SEM = 0.020
   187	```
   188	
   189	19 of 20 seeds give a positive interaction; one is essentially zero
   190	(−0.009). No seed gives a strongly negative interaction. The
--- cross relevant ---
   160	  15     65.6%
   161	  25     93.8%   ← peak
   162	  40     84.4%
   163	  60     84.4%
   164	 100     78.1%
   165	```
   166	
   167	**Interpretation:** The substrate has a clear optimal depth around
   168	n=25, with a roll-off both at shallower depth (insufficient
   169	integration) and deeper depth (substrate equilibrates and loses
   170	specificity). The "goldilocks" structure mirrors cortical integration
   171	literature (Thorpe / Kiani): perceptual integration has an optimal
   172	time window, with shorter giving noisy classification and longer
   173	giving over-integration.
   174	
   175	### 2.6 P13 — Substrate lift on LOO with reset protocol
   176	
   177	**Threshold:** Substrate-routed LOO accuracy − raw-feature LOO
   178	accuracy ≥ +15 percentage points.
   179	
   180	**Method:** Run LOO classification on (a) raw 8-dim V2 features and
   181	(b) substrate-routed patterns at n=25, with reset between depth
   182	measurements.
   183	
   184	**Result:**
   185	
   186	```
   187	Raw features (LOO, 1-NN cosine):       53.1%
   188	Substrate-routed (n=25, with reset):   93.8%
   189	Lift:                                  +40.6 percentage points
   190	```
   191	
   192	**Interpretation:** The substrate amplifies the chess-position
   193	discrimination from chance-level on raw features (53.1% on 4 categories
   194	is just above chance-25%) to near-perfect (93.8%) when routed through
   195	the substrate's 600-cell graph. This is **+40.6pp of geometric
   196	amplification**, far exceeding the +15pp prereg threshold.
   197	
   198	The original 2026-04-20 validation reported this lift at +3.1pp — a
   199	failure of the reset protocol (substrate state drifted toward
   200	equilibrium across the prior depth-sweep measurements, collapsing the
   201	classification structure). With the reset protocol now wired in, the
   202	lift is restored to +40.6pp. See `NON_EQUILIBRIUM_FINDING.md` for the
   203	diagnostic details.
   204	
   205	### 2.7 Chess summary
   206	
   207	The substrate is a **strong geometric amplifier** on chess:
   208	- 53.1% raw → 93.8% substrate-routed at canonical depth (n=25)
   209	- 65.4% null mapping (architecture-invariant geometric floor)
   210	- 83.1% 5-fold CV at fresh seeds
   211	- Goldilocks optimum at n=25 ticks of substrate evolution
   212	
   213	The +40.6pp lift is roughly an order of magnitude above the +15pp
   214	preregistered floor. The 65.4% null mapping shows two-thirds of the
   215	amplification is from geometric structure alone, not from how features
   216	are assigned to frames.
   217	
   218	---
   219	
   220	## 3. Conversation utterance categorisation (P14–P16)
   221	
   222	### 3.1 Setup
   223	
   224	**Utterances:** 8 categories (greetings, questions, agreements,
   225	clarifications, etc.) × 8 utterances per category = 64 utterances.
   226	
   227	**Features:** 8-dimensional injection-row features per utterance.
   228	Source: `run_conversation_readout.py:_injection_row, _build_tables`.
   229	
   230	**Substrate routing:** identical to chess — features injected as
--- cross hcp ---
   300	selective amplification. Raw features at 87.5% leave little headroom;
   301	substrate routing at 83.1% (lift −4.4pp) is within preregistered
   302	neutrality bounds. The null permutation at 70.6% confirms geometric
   303	content carries across domains.
   304	
   305	---
   306	
   307	## 4. HCP brain connectivity (P17–P18)
   308	
   309	### 4.1 Setup
   310	
   311	**Reference cohort:** Human Connectome Project (HCP), n=1003 subjects.
   312	For preregistered tests, n=100 subjects (computational tractability)
   313	in ICA-50 parcellation. The full-cohort effects (n=1003) match the
   314	n=100 subset within standard error.
   315	
   316	**Method:** Build group-averaged ICA-50 connectivity matrix; threshold
   317	at the same density as ARIA's vertex graph (0.101). Compare degree
   318	distribution and higher-order graph statistics.
   319	
   320	**ARIA reference:** 600-cell H₄ graph. By H₄ transitivity, every
   321	vertex has identical local structure → uniform degree 12 → degree
   322	std = 0 by theorem.
   323	
   324	### 4.2 P17 — ARIA degree homogeneity (theorem)
   325	
   326	**Threshold:** ARIA degree std = 0.00 (H₄ transitivity theorem).
   327	
   328	**Result:** 0.0000 (exactly).
   329	
   330	**Interpretation:** This is a theorem, not a measurement. The H₄
   331	Coxeter group acts transitively on the 600-cell vertices; every
   332	vertex is in the same orbit; every vertex has the same local
   333	neighbourhood structure; degree is uniform. The validation is
   334	included to verify the substrate construction is correct.
   335	
   336	### 4.3 P18 — HCP degree std (hub-spoke structure)
   337	
   338	**Threshold:** HCP ICA-50 degree std > 2.0.
   339	
   340	**Result (n=100 subjects, density 0.101):** **3.388**.
   341	
   342	**Interpretation:** Real cortical functional connectivity has
   343	substantial degree heterogeneity — std 3.39 means the vertex degrees
   344	range across roughly ±5 around the mean. This is the classical hub-
   345	spoke / small-world signature of cortex.
   346	
   347	**ARIA is at −11.58σ** below the HCP cohort mean on this metric:
   348	ARIA's degree std is 0; HCP n=1003 mean is 3.28 ± 0.28; the gap is
   349	(0 − 3.28) / 0.28 = −11.7σ. **Zero of 1003 HCP subjects** have
   350	degree std below 2.0. ARIA is far outside the biological distribution.
   351	
   352	### 4.4 Higher-order graph statistics (full cohort, n=1003)
   353	
   354	Three metrics computed across the full HCP cohort, with ARIA's value
   355	in parentheses:
   356	
   357	```
   358	Metric                 ARIA     HCP n=1003 mean   σ from HCP
   359	─────────────────────────────────────────────────────────────
   360	Degree std             0.000    3.28 ± 0.28        −11.58σ
   361	Participation ratio    68.54    19.72 ± 0.61       +79.78σ
   362	Clustering coefficient 0.455    0.220              +6.80σ
   363	```
   364	
   365	**Interpretation:**
   366	
   367	- **Participation ratio** measures how distributed the connectivity
   368	  is across the 50-region parcellation (high = uniform spread; low =
   369	  hub-concentrated). ARIA at 68.54 vs HCP at 19.72 — ARIA is
   370	  more than **two regimes** above biological cortex on uniformity.
   371	  Real cortex is hub-concentrated; ARIA is uniform. +79.78σ.
   372	- **Clustering coefficient** measures local triangular density.
   373	  ARIA at 0.455 vs HCP at 0.220 — ARIA has more local clustering
   374	  than cortex (consistent with the polytope's local edge density).
   375	  +6.80σ.
   376	
   377	### 4.5 The maximum-symmetry null framing
   378	
   379	The HCP comparison places ARIA as a **principled maximum-symmetry
   380	null reference** for cortex. ARIA is what cortex would look like
   381	under unbroken H₄ symmetry. Real cortex breaks this symmetry through
   382	hub-spoke functional specialisation; the symmetry-breaking is
   383	quantitatively measurable as the σ-distance between ARIA and HCP on
   384	each metric.
   385	
   386	This is the contribution of ARIA to comparative-connectomics
   387	methodology: instead of comparing real cortex to a stochastic null
   388	(Erdős–Rényi, configuration model), one can compare it to a
   389	**deterministic group-theoretic null** with no fitted parameters,
   390	giving precise effect-size statements like "real cortex is +79.78σ
   391	above the H₄-symmetry baseline on participation ratio."
   392	
   393	The σ-distances (−11.6σ, +79.8σ, +6.8σ) far exceed any preprocessing-
   394	induced noise envelope — the gap between ARIA and HCP is robust to
   395	parcellation choice, density threshold, and subject inclusion
   396	criteria.
   397	
   398	### 4.6 What we do NOT claim
   399	
   400	We do **not** claim biological cortex has "drifted from an ideal
   401	polytope" or that the polytope is the ground truth. We claim:
   402	
   403	(a) ARIA is a useful a-priori null with principled group-theoretic
   404	    foundations and zero fitted parameters.
   405	(b) The observable σ-distances quantify the magnitude of biological
   406	    symmetry-breaking.
   407	(c) The signs of those distances (cortex is more hub-concentrated,
   408	    less uniformly connected, more locally clustered) are the
   409	    biological content that any cortical-architecture model must
   410	    explain.
   411	
   412	ARIA does not commit to a normative claim about which symmetry-
   413	breaking is present. The comparison is structural — quantifying
   414	where biology sits relative to the H₄ baseline.
   415	
   416	### 4.7 HCP summary
   417	
   418	ARIA's degree std = 0 (theorem); HCP n=1003 degree std = 3.28 ± 0.28,
   419	range [2.55, 4.16], with zero of 1003 subjects below 2.0. ARIA is
   420	−11.58σ on degree homogeneity, +79.78σ on participation ratio, and
   421	+6.80σ on clustering coefficient. The substrate functions as a
   422	maximum-symmetry null reference for cortical functional connectivity;
   423	biological cortex breaks the symmetry through hub-spoke functional
   424	specialisation that is quantifiable in σ-units against ARIA.
   425	
   426	---
   427	
   428	## 5. Cross-domain summary in one paragraph
   429	
   430	The substrate's geometric structure functions as a domain-invariant
--- validation 142-170 ---
   142	**N=20 fresh-seed deep-dive (`demo_p4_cxp_deep_dive.py`, seeds 32000–32019):**
   143	
   144	```
   145	C×P bootstrap mean:           +0.190
   146	C×P 95% bootstrap CI:         [+0.143, +0.239]
   147	P(interaction ≤ 0):           0.0000
   148	P(interaction < +0.10):       0.0000
   149	```
   150	
   151	The 95% CI is **entirely above the preregistered +0.10 threshold**.
   152	The synergy is decisively positive and decisively above prereg. The
   153	N=3/N=5 estimates were Type II false negatives compounded by
   154	seed-range sampling bias on a high-per-seed-variance interaction term
   155	(per-seed std = 0.089 at N=20).
   156	
   157	**Architectural reading**: this is a substantive shift in the claim.
   158	Original: "C and P are nearly orthogonal stabilisers." Corrected:
   159	"C and P are strongly coupled stabilisers; the interaction (+0.19) is
   160	comparable to the P main effect (−0.22)." See §4 of
   161	`P4_SYNERGY_FINDING.md` for the mechanistic interpretation.
   162	
   163	### 3.3 P13 — Chess LOO substrate lift
   164	
   165	**Threshold:** ≥ +15pp lift (substrate vs raw on LOO at n=25 ticks).
   166	
   167	**Original (N=1) failure:** +3.1pp. Far below threshold.
   168	
   169	**2026-04-29 re-run (with `homeostatic_reset(level=1.0)` between depth
   170	measurements):** **+40.6pp**.

exec
/bin/bash -lc "cd '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper' && echo '--- citation keys used ---'; rg -o \"\\\\citep\\{["'^}]+'"\\}|\\\\cite\\{["'^}]+'"\\}\" -N main.tex sections/*.tex | sed -E 's/.*\\{//; s/\\}.*//' | tr ',' '\\n' | sed 's/"'^ *//; s/ *$//'"' | sort -u > /tmp/used_keys.txt; cat /tmp/used_keys.txt; echo '--- missing in bib ---'; for k in "'$(cat /tmp/used_keys.txt); do rg -q "'"\\{"'$k," references.bib || echo "$k"; done; echo '"'--- bib keys count ---'; rg -n '"'^@'"' references.bib | head -80; echo '--- labels and refs maybe undefined labels used ---'; rg -o \"\\\\ref\\{["'^}]+'"\\}\" -N main.tex sections/*.tex | sed -E 's/.*\\{//; s/\\}.*//' | sort -u > /tmp/refs.txt; cat /tmp/refs.txt; echo '--- labels defined ---'; rg -o \"\\\\label\\{["'^}]+'"\\}\" -N main.tex sections/*.tex | sed -E 's/.*\\{//; s/\\}.*//' | sort -u > /tmp/labels.txt; comm -23 /tmp/refs.txt /tmp/labels.txt" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 605ms:
--- citation keys used ---
/bin/bash: /tmp/used_keys.txt: Read-only file system
rg: regex parse error:
    (?:\citep\{[^}]+\}|\cite\{[^}]+\})
       ^^
error: unrecognized escape sequence
cat: /tmp/used_keys.txt: No such file or directory
--- missing in bib ---
cat: /tmp/used_keys.txt: No such file or directory
--- bib keys count ---
1:@book{CoxeterRegularPolytopes,
10:@misc{Weisstein600Cell,
18:@article{BeggsPlenz2003,
29:@article{Tononi2008,
40:@article{BalduzziTononi2008,
51:@book{Baars1988GWT,
59:@book{Dehaene2014ConsciousAndBrain,
67:@article{FristonFreeEnergy2010,
78:@article{ClarkPP2013,
89:@article{Brodbeck2012Microstates,
100:@article{VanEssen2013HCP,
110:@article{PhysioNet2000,
121:@misc{SleepEDFx,
129:@misc{OpenNeuroDS005620,
137:@misc{OpenNeuroDS004902,
145:@misc{ZenodoDMT3992359,
153:@unpublished{SmartAdaptiveClosureTransport2026,
160:@unpublished{SmartAriaClosureKernel2026,
167:@unpublished{SmartBAnomaly2026,
174:@misc{ariaChessRepo,
--- labels and refs maybe undefined labels used ---
/bin/bash: /tmp/refs.txt: Read-only file system
ax:e8
ax:self-sim
cor:h4-unique
cor:zero-param
def:F-discrete
def:K-amplitude
def:V
def:closure
def:sigma-fixed
eq:7rung
eq:E8-H4-decomp
eq:F-form
eq:F5-invariant-equality
eq:alpha-match
eq:beta-match
eq:cascade
eq:dagger
eq:elkies-icosian
eq:eps-rate
eq:factor-2
eq:gamma-match
eq:lambda-single-cell
eq:sigma-fixed
lem:F5-invariants
lem:non-crystallographic
lem:spin8-reps
lem:triality-unique
prop:F2-basis
rem:F4-diagonal
rem:F5-hypotheses
rem:full-tensor
rem:lorentzian
rem:rate-status
rem:sigma-fixed-ground
rem:spin8-R4
sec:F1
sec:F2
sec:F3
sec:F4
sec:F5
sec:F6
sec:F7
sec:F8
sec:axioms
sec:consolidated
sec:discussion
sec:lambda
thm:BI
thm:F1
thm:F2
thm:F3
thm:F4
thm:F5
thm:F6
thm:F7
thm:F8
thm:FP
thm:deser
thm:lambda
--- labels defined ---
/bin/bash: /tmp/labels.txt: Read-only file system
rg: regex parse error:
    (?:\label\{[^}]+\})
       ^^
error: unrecognized escape sequence
ax:e8
ax:self-sim
cor:h4-unique
cor:zero-param
def:F-discrete
def:K-amplitude
def:V
def:closure
def:sigma-fixed
eq:7rung
eq:E8-H4-decomp
eq:F-form
eq:F5-invariant-equality
eq:alpha-match
eq:beta-match
eq:cascade
eq:dagger
eq:elkies-icosian
eq:eps-rate
eq:factor-2
eq:gamma-match
eq:lambda-single-cell
eq:sigma-fixed
lem:F5-invariants
lem:non-crystallographic
lem:spin8-reps
lem:triality-unique
prop:F2-basis
rem:F4-diagonal
rem:F5-hypotheses
rem:full-tensor
rem:lorentzian
rem:rate-status
rem:sigma-fixed-ground
rem:spin8-R4
sec:F1
sec:F2
sec:F3
sec:F4
sec:F5
sec:F6
sec:F7
sec:F8
sec:axioms
sec:consolidated
sec:lambda
thm:BI
thm:F1
thm:F2
thm:F3
thm:F4
thm:F5
thm:F6
thm:F7
thm:F8
thm:FP
thm:deser
thm:lambda

exec
/bin/bash -lc "cd '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper' && echo 'refs'; rg -n -o '\\\\ref\\{["'^}]+'"\\}' main.tex sections/*.tex; echo 'labels'; rg -n -o '\\\\label\\{["'^}]+'"\\}' main.tex sections/*.tex; echo 'citations'; rg -n -o '\\\\citep\\{["'^}]+'"\\}|\\\\cite\\{["'^}]+'"\\}' main.tex sections/*.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 331ms:
refs
sections/08_discussion.tex:49:\ref{sec:chain}
sections/08_discussion.tex:57:\ref{sec:chain}
sections/08_discussion.tex:163:\ref{ssec:hcp}
sections/08_discussion.tex:185:\ref{sec:limitations}
sections/09_limitations.tex:20:\ref{sec:intro}
sections/09_limitations.tex:27:\ref{ssec:six_signatures}
sections/09_limitations.tex:32:\ref{sec:method}
sections/09_limitations.tex:32:\ref{ssec:six_signatures}
sections/09_limitations.tex:44:\ref{sec:chain}
sections/09_limitations.tex:58:\ref{sec:intro}
sections/09_limitations.tex:63:\ref{ssec:act_bridge}
sections/09_limitations.tex:71:\ref{ssec:cascade}
sections/09_limitations.tex:78:\ref{ssec:cphi}
sections/09_limitations.tex:80:\ref{ssec:cphi}
sections/09_limitations.tex:94:\ref{sec:intro}
sections/09_limitations.tex:94:\ref{sec:chain}
sections/09_limitations.tex:96:\ref{ssec:regime}
sections/09_limitations.tex:101:\ref{sec:chain}
sections/09_limitations.tex:110:\ref{ssec:hcp}
sections/09_limitations.tex:120:\ref{sec:method}
sections/09_limitations.tex:120:\ref{sec:results}
sections/09_limitations.tex:120:\ref{sec:stress}
sections/09_limitations.tex:167:\ref{ssec:regime}
sections/10_conclusion.tex:80:\ref{sec:limitations}
sections/07_cross_domain.tex:5:\ref{ssec:chess}
sections/07_cross_domain.tex:6:\ref{ssec:conv}
sections/07_cross_domain.tex:8:\ref{ssec:hcp}
sections/07_cross_domain.tex:95:\ref{sec:method}
sections/07_cross_domain.tex:145:\ref{sec:limitations}
sections/07_cross_domain.tex:157:\ref{lem:600cell}
sections/07_cross_domain.tex:226:\ref{sec:limitations}
sections/06_stress_tests.tex:21:\ref{sec:chain}
sections/06_stress_tests.tex:139:\ref{sec:limitations}
sections/05_results.tex:5:\ref{ssec:six_signatures}
sections/05_results.tex:7:\ref{ssec:eighteen_prereg}
sections/05_results.tex:8:\ref{ssec:alpha_overlap}
sections/05_results.tex:20:\ref{sec:chain}
sections/05_results.tex:80:\ref{sec:chain}
sections/05_results.tex:84:\ref{sec:limitations}
sections/05_results.tex:84:\ref{ssec:regime}
sections/05_results.tex:135:\ref{sec:stress}
sections/05_results.tex:144:\ref{sec:method}
sections/05_results.tex:192:\ref{lem:600cell}
sections/05_results.tex:193:\ref{ssec:cphi}
sections/05_results.tex:195:\ref{sec:chain}
sections/04_consciousness_chain.tex:5:\ref{sec:substrate}
sections/04_consciousness_chain.tex:6:\ref{sec:results}
sections/04_consciousness_chain.tex:17:\ref{sec:results}
sections/04_consciousness_chain.tex:57:\ref{lem:600cell}
sections/04_consciousness_chain.tex:87:\ref{sec:results}
sections/04_consciousness_chain.tex:158:\ref{sec:stress}
sections/04_consciousness_chain.tex:187:\ref{sec:stress}
sections/02_method.tex:25:\ref{sec:limitations}
sections/02_method.tex:176:\ref{sec:limitations}
sections/03_substrate.tex:5:\ref{ssec:vertices}
sections/03_substrate.tex:6:\ref{ssec:graph}
sections/03_substrate.tex:7:\ref{ssec:cphi}
sections/03_substrate.tex:9:\ref{ssec:shells}
sections/03_substrate.tex:10:\ref{ssec:cascade}
sections/03_substrate.tex:11:\ref{sec:chain}
sections/03_substrate.tex:64:\ref{sec:chain}
sections/03_substrate.tex:89:\ref{sec:chain}
sections/03_substrate.tex:92:\ref{lem:600cell}
sections/03_substrate.tex:101:\ref{sec:chain}
sections/03_substrate.tex:122:\ref{sec:chain}
sections/03_substrate.tex:139:\ref{sec:results}
sections/03_substrate.tex:154:\ref{sec:limitations}
main.tex:55:\ref{sec:chain}
main.tex:88:\ref{sec:chain}
sections/01_introduction.tex:93:\ref{sec:limitations}
sections/01_introduction.tex:128:\ref{sec:results}
sections/01_introduction.tex:147:\ref{sec:method}
sections/01_introduction.tex:148:\ref{sec:substrate}
sections/01_introduction.tex:151:\ref{sec:chain}
sections/01_introduction.tex:153:\ref{sec:results}
sections/01_introduction.tex:155:\ref{sec:stress}
sections/01_introduction.tex:157:\ref{sec:cross_domain}
sections/01_introduction.tex:158:\ref{sec:discussion}
sections/01_introduction.tex:161:\ref{sec:limitations}
sections/01_introduction.tex:162:\ref{sec:conclusion}
labels
sections/08_discussion.tex:2:\label{sec:discussion}
sections/08_discussion.tex:80:\label{ssec:act_bridge}
sections/10_conclusion.tex:2:\label{sec:conclusion}
sections/09_limitations.tex:2:\label{sec:limitations}
sections/09_limitations.tex:12:\label{ssec:regime}
sections/09_limitations.tex:51:\label{ssec:posthoc}
sections/09_limitations.tex:88:\label{ssec:interpretation}
sections/09_limitations.tex:114:\label{ssec:testclaim}
sections/09_limitations.tex:145:\label{ssec:scope}
sections/07_cross_domain.tex:2:\label{sec:cross_domain}
sections/07_cross_domain.tex:16:\label{ssec:chess}
sections/07_cross_domain.tex:40:\label{tab:chess_depth}
sections/07_cross_domain.tex:60:\label{tab:chess_prereg}
sections/07_cross_domain.tex:110:\label{ssec:conv}
sections/07_cross_domain.tex:120:\label{tab:conv_prereg}
sections/07_cross_domain.tex:148:\label{ssec:hcp}
sections/07_cross_domain.tex:166:\label{tab:hcp}
sections/07_cross_domain.tex:236:\label{tab:cross_domain_summary}
sections/06_stress_tests.tex:3:\label{sec:stress}
sections/06_stress_tests.tex:37:\label{tab:cxp_trend}
sections/06_stress_tests.tex:73:\label{tab:cxp_means}
sections/05_results.tex:2:\label{sec:results}
sections/05_results.tex:16:\label{ssec:six_signatures}
sections/05_results.tex:29:\label{tab:per_condition}
sections/05_results.tex:46:\label{tab:six_signatures}
sections/05_results.tex:86:\label{ssec:eighteen_prereg}
sections/05_results.tex:98:\label{tab:eighteen_prereg}
sections/05_results.tex:156:\label{ssec:alpha_overlap}
sections/05_results.tex:166:\label{tab:alpha_overlap}
sections/03_substrate.tex:2:\label{sec:substrate}
sections/03_substrate.tex:14:\label{ssec:vertices}
sections/03_substrate.tex:31:\label{ssec:graph}
sections/03_substrate.tex:39:\label{lem:600cell}
sections/03_substrate.tex:66:\label{ssec:cphi}
sections/03_substrate.tex:70:\label{eq:cphi}
sections/03_substrate.tex:104:\label{ssec:shells}
sections/03_substrate.tex:120:\label{ssec:cascade}
sections/02_method.tex:2:\label{sec:method}
sections/02_method.tex:55:\label{tab:provenance}
sections/04_consciousness_chain.tex:2:\label{sec:chain}
sections/01_introduction.tex:2:\label{sec:intro}
citations
sections/10_conclusion.tex:73:\citep{SmartAdaptiveClosureTransport2026}
sections/10_conclusion.tex:89:\citep{SmartBAnomaly2026}
sections/08_discussion.tex:9:\citep{SmartAdaptiveClosureTransport2026}
sections/08_discussion.tex:46:\citep{Tononi2008,BalduzziTononi2008}
sections/08_discussion.tex:56:\citep{Baars1988GWT,Dehaene2014ConsciousAndBrain}
sections/08_discussion.tex:64:\citep{FristonFreeEnergy2010,ClarkPP2013}
sections/08_discussion.tex:83:\citep{SmartAdaptiveClosureTransport2026}
sections/08_discussion.tex:117:\citep{SmartAriaClosureKernel2026}
sections/08_discussion.tex:119:\citep{SmartBAnomaly2026}
sections/09_limitations.tex:7:\citep{SmartBAnomaly2026}
sections/09_limitations.tex:81:\citep{SmartAriaClosureKernel2026}
sections/09_limitations.tex:84:\citep{SmartBAnomaly2026}
sections/09_limitations.tex:105:\citep{BalduzziTononi2008}
sections/07_cross_domain.tex:151:\citep{VanEssen2013HCP}
sections/05_results.tex:52:\citep{SleepEDFx}
sections/05_results.tex:55:\citep{OpenNeuroDS005620}
sections/05_results.tex:58:\citep{Brodbeck2012Microstates}
sections/05_results.tex:61:\citep{Tononi2008}
sections/05_results.tex:67:\citep{BeggsPlenz2003,SleepEDFx}
sections/05_results.tex:172:\citep{SleepEDFx}
sections/05_results.tex:183:\citep{BeggsPlenz2003}
sections/04_consciousness_chain.tex:86:\citep{Tononi2008,BalduzziTononi2008}
sections/03_substrate.tex:17:\citep{CoxeterRegularPolytopes,Weisstein600Cell}
sections/03_substrate.tex:38:\citep{CoxeterRegularPolytopes,Weisstein600Cell}
sections/03_substrate.tex:80:\citep{SmartAriaClosureKernel2026}
sections/03_substrate.tex:82:\citep{SmartBAnomaly2026}
sections/03_substrate.tex:113:\citep{SmartAriaClosureKernel2026}
sections/02_method.tex:65:\citep{SleepEDFx}
sections/02_method.tex:77:\citep{VanEssen2013HCP}
sections/02_method.tex:87:\citep{SleepEDFx,PhysioNet2000}
sections/02_method.tex:91:\citep{BeggsPlenz2003}
sections/02_method.tex:94:\citep{OpenNeuroDS005620}
sections/02_method.tex:100:\citep{OpenNeuroDS004902}
sections/02_method.tex:105:\citep{ZenodoDMT3992359}
sections/02_method.tex:109:\citep{VanEssen2013HCP}
sections/02_method.tex:118:\citep{Brodbeck2012Microstates}
main.tex:65:\citep{SmartAdaptiveClosureTransport2026}
main.tex:171:\citep{PhysioNet2000,SleepEDFx}
main.tex:172:\citep{OpenNeuroDS005620}
main.tex:173:\citep{OpenNeuroDS004902}
main.tex:174:\citep{ZenodoDMT3992359}
main.tex:175:\citep{VanEssen2013HCP}
main.tex:177:\citep{BeggsPlenz2003}
main.tex:178:\citep{Tononi2008,BalduzziTononi2008}
main.tex:180:\citep{Brodbeck2012Microstates}
main.tex:181:\citep{CoxeterRegularPolytopes,Weisstein600Cell}
main.tex:183:\citep{ariaChessRepo}
main.tex:189:\citep{ariaChessRepo}
sections/01_introduction.tex:6:\citep{Tononi2008,BalduzziTononi2008}
sections/01_introduction.tex:7:\citep{Baars1988GWT,Dehaene2014ConsciousAndBrain}
sections/01_introduction.tex:8:\citep{FristonFreeEnergy2010,ClarkPP2013}
sections/01_introduction.tex:22:\citep{CoxeterRegularPolytopes,Weisstein600Cell}
sections/01_introduction.tex:86:\citep{SmartAdaptiveClosureTransport2026}
sections/01_introduction.tex:104:\citep{SmartAriaClosureKernel2026}

exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/main.tex' | sed -n '70,210p'; printf '%s\\n' '---05 179-205---'; nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/05_results.tex' | sed -n '179,205p'; printf '%s\\n' '---06 117-155---'; nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex' | sed -n '117,155p'; printf '%s\\n' '---08 1-125---'; nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex' | sed -n '1,125p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 392ms:
    70	\begin{abstract}
    71	We test whether a geometry-fixed substrate — the 600-cell regular
    72	4-polytope $\Rsixhundred$ under H$_4$ Coxeter symmetry, with the
    73	shifted graph Laplacian $\Cph = \Lop + \Ph^{-2} I$ as its response
    74	operator — is consistent with cortical signatures across five
    75	neuroscience domains. Eighteen quantitative predictions were
    76	preregistered on 2026-04-18 (\texttt{docs/brain\_mapping/PAPER\_PREDICTIONS.md})
    77	before any validation run; each has a falsifiable threshold. The
    78	preregistered tally is $17/18$ at standard validation methodology
    79	($5$-seed cascade block plus state-reset protocol), and $18/18$ after
    80	a documented $N\!=\!20$ deep-dive on the residual high-variance
    81	interaction (P4); no preregistered threshold has been modified. We
    82	additionally report six drug/sleep EEG signatures tested on a recurrent
    83	self-model layer above the substrate, on a single deterministic
    84	trajectory at seed~$42$. The six signatures are not part of the
    85	P1--P18 preregistration; they are tested against published-reference
    86	thresholds (Sleep-EDFx, OpenNeuro, Brodbeck, Tononi) and were obtained
    87	under condition-specific stimulus models redesigned at v4 to be
    88	biologically realistic (\S\ref{sec:chain}).
    89	
    90	\noindent\emph{(i) Cortical avalanches.}
    91	Wake cascade-event power-law exponent $\alpha = 2.252$,
    92	$95\%$ CI $[1.82, 2.86]$ ($R^{2}=0.956$, $n_{\mathrm{events}}=58$).
    93	This 95\% CI overlaps simultaneously real Sleep-EDFx EEG ($n=30$
    94	subjects, $\alpha=2.51$, CI $[2.50, 2.53]$) and ARIA's prior cascade
    95	pipeline ($\alpha=2.85$, CI $[2.73, 3.25]$) — three-way confidence
    96	overlap.
    97	
    98	\noindent\emph{(ii) Drug/sleep state transitions.}
    99	NREM-N3 phenomenal-intensity variance ratio $0.463\!\times$ wake
   100	(predicted $\sim 0.365$, threshold $<\!0.70$); propofol modality-switching
   101	ratio $1.83\!\times$ wake (threshold $\in[1.5, 5.0]$, empirical
   102	reference $2.96\!\times$ from OpenNeuro \texttt{ds005620}, $n=8$);
   103	propofol continuity drop $+0.066$ (threshold $>\!0.020$); propofol
   104	integrated-information $\Phi$ collapse to $0.33\!\times$ wake (IIT
   105	direction confirmed); recovery deterministically identical to wake.
   106	All six signatures pass against their published-reference thresholds
   107	on the single deterministic substrate trajectory.
   108	
   109	\noindent\emph{(iii) Causal mechanism isolation.}
   110	Two of four cascade mechanisms — context rotation $C$ and partial
   111	emission $P$ — are causally significant, and the original
   112	preregistered C$\times$P synergy prediction $\geq +0.10$ closes
   113	decisively at adequate replication: $N\!=\!20$ fresh seeds give a
   114	bootstrap point estimate of $+0.190$ with $95\%$ CI $[+0.143, +0.239]$
   115	(threshold $\geq +0.10$); $0/2000$ bootstrap resamples were at or
   116	below zero, reported as $0.0000$. We document the original $N\!=\!3$
   117	underestimate ($+0.044$) as consistent with an underpowered interaction
   118	estimate at $N\!=\!3$ and contribute the $N\!\geq\!20$ minimum as a
   119	preregistration-practice recommendation for high-variance interaction
   120	terms.
   121	
   122	\noindent\emph{(iv) Cross-domain selectivity.}
   123	The substrate exhibits domain-invariant selective amplification on
   124	the two tasks tested: chess 4-category position classification on
   125	8-dimensional V2 features lifts $+40.6$ percentage points on
   126	leave-one-out at canonical depth $n\!=\!25$ ticks (raw $53.1\%$
   127	$\to$ substrate-routed $93.8\%$, with state reset; the
   128	preregistered estimator P13 was $5$-fold CV with threshold
   129	$\geq\!+15$pp; the LOO finding above is a stronger validation-protocol
   130	refinement at the same threshold), while conversation utterance
   131	classification at raw $87.5\%$ yields a substrate lift of $-4.4$pp
   132	(threshold $|\cdot| < 10$pp), consistent with selective amplification
   133	only where raw features are ambiguous. On HCP brain functional connectivity
   134	(preregistered $n\!=\!100$ ICA-50 plus full-cohort $n\!=\!1003$
   135	descriptive statistics), the H$_4$-transitive substrate is a
   136	maximum-symmetry deterministic null reference: ARIA degree std
   137	$=\!0$ by transitivity; HCP $3.28\!\pm\!0.28$; ARIA at $-11.58\sigma$
   138	on degree homogeneity, $+79.78\sigma$ on participation ratio, and
   139	$+6.80\sigma$ on clustering coefficient.
   140	
   141	\noindent\emph{What we do not claim.}
   142	We do not claim the 600-cell is the unique substrate consistent with
   143	these signatures, nor that other regular 4-polytopes (24-cell, 120-cell)
   144	have been ruled out. We do not derive the $\Ph^{-2}$ floor from
   145	first principles; it is a design-level stability clamp on the
   146	shifted-Laplacian response. The recurrent layer above the substrate
   147	is reported on a single deterministic trajectory; cross-seed CIs on
   148	the per-condition signatures are an explicit strengthening build.
   149	The structural scope of this paper is: \emph{a geometry-fixed
   150	substrate, with no shape parameters tuned to any neural dataset,
   151	is consistent with eighteen preregistered neuroscience
   152	correspondences and six drug/sleep EEG signatures, with all gaps in
   153	the original preregistration closed by methodology refinement and
   154	without modifying any preregistered threshold.}
   155	\end{abstract}
   156	
   157	% =====================================================================
   158	\input{sections/01_introduction.tex}
   159	\input{sections/02_method.tex}
   160	\input{sections/03_substrate.tex}
   161	\input{sections/04_consciousness_chain.tex}
   162	\input{sections/05_results.tex}
   163	\input{sections/06_stress_tests.tex}
   164	\input{sections/07_cross_domain.tex}
   165	\input{sections/08_discussion.tex}
   166	\input{sections/09_limitations.tex}
   167	\input{sections/10_conclusion.tex}
   168	% =====================================================================
   169	
   170	\section*{Acknowledgements}
   171	We thank the Sleep-EDFx (PhysioNet)~\citep{PhysioNet2000,SleepEDFx},
   172	OpenNeuro propofol cohort \texttt{ds005620}~\citep{OpenNeuroDS005620},
   173	the OpenNeuro DMT cohort \texttt{ds004902}~\citep{OpenNeuroDS004902},
   174	the Zenodo DMT EEG release~\citep{ZenodoDMT3992359}, and the WU-Minn
   175	HCP Consortium~\citep{VanEssen2013HCP} for releasing the public
   176	datasets that made these comparisons possible. Cortical avalanche
   177	methodology follows~\citep{BeggsPlenz2003}; the integrated-information
   178	$\Phi$ proxy is in the IIT family~\citep{Tononi2008,BalduzziTononi2008};
   179	the propofol microstate comparison uses Brodbeck et
   180	al.~\citep{Brodbeck2012Microstates}. The 600-cell construction
   181	follows~\citep{CoxeterRegularPolytopes,Weisstein600Cell}. All code
   182	and processed data are released under MIT licence at the project
   183	repository~\citep{ariaChessRepo}.
   184	
   185	\section*{Reproducibility}
   186	The complete pipeline (substrate construction, six-signature
   187	consciousness chain, $N\!=\!20$ C$\times$P deep-dive, eighteen-prediction
   188	preregistered validation, figure regeneration, this paper) is reproducible
   189	from the project repository~\citep{ariaChessRepo} via the included
   190	\texttt{reproduce\_paper\_claims.sh} script. All scripts are
   191	deterministic given seeds; the substrate's spectral decomposition is
   192	cached at module level. Wallclocks: drug/sleep v4 $\sim 30$\,s;
   193	$N\!=\!20$ deep-dive $\sim 28$\,min; preregistered validation
   194	$\sim 18$\,min.
   195	
   196	\bibliographystyle{plainnat}
   197	\bibliography{references}
   198	
   199	\end{document}
---05 179-205---
   179	The v4 WAKE 95\% CI $[1.82, 2.86]$ contains the upper arm of the
   180	real Sleep-EDFx EEG CI $[2.50, 2.53]$, overlaps the ARIA prior
   181	cascade pipeline CI $[2.73, 3.25]$ on the interval $[2.73, 2.86]$,
   182	and lies inside the cortical-avalanche band
   183	$\alpha\!\in\![1.5, 3.5]$~\citep{BeggsPlenz2003}. The pairwise
   184	intersections (WAKE $\cap$ Sleep-EDFx, WAKE $\cap$ prior pipeline,
   185	WAKE $\cap$ cortical-avalanche band) are non-empty across three
   186	independent reference ranges.
   187	
   188	\textbf{Reading.} The substrate produces self-organised-critical
   189	cascade statistics matching the cortical-avalanche literature with
   190	no fitted parameter on neural data. The bounded-top-$K$ at
   191	$k=12$ is pinned to the substrate's average degree
   192	(Lemma~\ref{lem:600cell}); the $\Ph^{-2}$ shift in $\Cph$ is a
   193	stability clamp (\S\ref{ssec:cphi}); the AR(1) WAKE input has
   194	biological time-scale parameters but is not measurement-fitted to
   195	any specific subject (\S\ref{sec:chain}). Three-way overlap on the
   196	power-law exponent is the strongest single empirical anchor in the
   197	paper.
---06 117-155---
   117	\textbf{Architectural reading (substrate witness).} $C$ creates churn
   118	in \emph{which} vertices are uncrossed (frame rotation churns the
   119	uncrossed pool). $P$ promotes the high-pressure subset of the
   120	uncrossed pool to mini-emitters. The product is a non-additive
   121	novel-event-generation pathway: with both on, the uncrossed pool
   122	churns and $P$ amplifies new vertices entering the high-pressure
   123	region; with either off, the pathway collapses. The interaction
   124	$+0.19$ is comparable in magnitude to the $P$ main effect $-0.22$,
   125	so $C$ and $P$ are \emph{strongly coupled} cascade-state stabilisers
   126	on this substrate, not nearly-orthogonal ones. This reverses an
   127	architectural claim from the original 3-seed validation that held $C$
   128	and $P$ approximately orthogonal.
   129	
   130	\textbf{Disclosure: $N\!=\!20$ ordering.} The $N\!=\!20$ deep-dive
   131	was conducted \emph{after} the original $N\!=\!3$ failure
   132	(2026-04-29 vs 2026-04-20). The seed range $32000$--$32019$ was
   133	selected to be non-overlapping with the original $30000$s seeds.
   134	Two strengthening builds we have not delivered:
   135	(i) a second independent $N\!=\!20$ run at a different seed range
   136	(e.g.\ $33000$--$33019$), and
   137	(ii) an $N\!=\!50$ characterisation of the per-seed sample
   138	distribution. Both are recorded as open builds in
   139	\S\ref{sec:limitations}.
   140	
   141	\textbf{What this stress test does \emph{not} establish.}
   142	\begin{itemize}\itemsep=2pt
   143	\item It does not establish a Lyapunov function on the reduced flow.
   144	\item It does not establish that the substrate is uniquely selected by
   145	  $C\times P$ coupling among regular 4-polytopes.
   146	\item It does not establish an $\eta$-trajectory derivation; $\eta$
   147	  is treated as a condition-dependent constant in this paper.
   148	\end{itemize}
   149	The stress test is what its name says: a high-replication factorial
   150	test of one preregistered interaction prediction, on a fresh-seed
   151	sample, with bootstrap confidence intervals. The architectural reading
   152	is a \emph{description} of what $C$ and $P$ do on the substrate, not a
   153	theorem about why they do it.
   154	
   155	\subsection{Methodological contribution}
---08 1-125---
     1	% =====================================================================
     2	\section{Discussion}\label{sec:discussion}
     3	% =====================================================================
     4	
     5	This section reads the substrate-witness result against existing
     6	theories of consciousness, identifies what is novel here that is not
     7	a re-statement of an earlier theory, and proposes a non-load-bearing
     8	ACT bridge to the companion adaptive-closure-transport
     9	preprint~\citep{SmartAdaptiveClosureTransport2026}. We do not claim a
    10	selection theorem, we do not claim a Lyapunov derivation, and we do
    11	not claim the recurrent layer ``is'' consciousness.
    12	
    13	\subsection{What is novel in this work}
    14	
    15	Three things are claimed novel as a substrate witness:
    16	\begin{enumerate}\itemsep=2pt
    17	\item \textbf{A geometry-fixed substrate that is consistent with
    18	  real-cortex EEG signatures without fitted shape parameters on neural
    19	  data.} The 600-cell + H$_4$ symmetry is fixed by group theory once
    20	  the substrate is chosen; cascade-$\alpha$ matches Sleep-EDFx within
    21	  preregistered tolerance with pairwise CI overlap on three reference
    22	  ranges; six drug/sleep signatures pass at published-reference
    23	  thresholds on a single deterministic substrate. We are not aware of
    24	  a prior geometric substrate that has been tested against this many
    25	  preregistered cortical correspondences from a graph fixed by group
    26	  theory; we cannot rule out that such a model exists.
    27	\item \textbf{The strong-coupling architectural finding.} $C$ and $P$
    28	  are strongly coupled cascade-state stabilisers, not
    29	  nearly-orthogonal ones. The $C\!\times\!P$ interaction
    30	  ($+0.190$, $95\%$ CI $[+0.143, +0.239]$ at $N\!=\!20$) is comparable
    31	  in magnitude to the $P$ main effect ($-0.218$). This was hidden by
    32	  underpowered ablation and emerged only at $N\!\geq\!20$ — a
    33	  substantive correction to the architectural reading from the
    34	  original 3-seed validation.
    35	\item \textbf{The 18/18 preregistered correspondences with no
    36	  threshold modification.} Every prediction in the preregistered set
    37	  passes at the preregistered thresholds. The two interaction tests
    38	  (P3, P4) required $N\!\geq\!5$ and $N\!\geq\!20$ respectively, and
    39	  one test (P13) required the documented state-reset protocol. We
    40	  report this transparently as methodology refinement, not as
    41	  threshold change.
    42	\end{enumerate}
    43	
    44	\subsection{Comparison to existing theories of consciousness}
    45	
    46	\textbf{vs IIT.}~\citep{Tononi2008,BalduzziTononi2008} ARIA produces
    47	IIT-direction-correct $\Phi$ collapse on propofol ($0.33\!\times$
    48	wake). The H$_4$-equivariance argument
    49	(\S\ref{sec:chain}) makes $\Phi\to 0$ when dynamics are
    50	group-symmetric, and $\Phi > 0$ only when dynamics break symmetry.
    51	ARIA does not implement the full IIT axioms (cause-effect repertoires,
    52	exclusion postulate, integration-over-partitions); it reproduces the
    53	observable consequence on the propofol--wake state contrast. This is
    54	a consistency-of-direction result, not a discharge of IIT.
    55	
    56	\textbf{vs Global Workspace Theory.}~\citep{Baars1988GWT,Dehaene2014ConsciousAndBrain}
    57	The $S^{7}$ context-rotation mechanism (\S\ref{sec:chain}) is
    58	functionally analogous to a workspace with rotating attentional
    59	selection; the active observer frame plays the role of a temporary
    60	in-workspace subset of features. ARIA does not commit to the GWT
    61	broadcast/access distinction at the architectural level; the
    62	analogy is descriptive.
    63	
    64	\textbf{vs Predictive Processing.}~\citep{FristonFreeEnergy2010,ClarkPP2013}
    65	ARIA does not implement prediction-error minimisation or hierarchical
    66	generative models.
    67	The recurrent self-model layer ($\eta\!=\!0.20$) provides top-down
    68	modulation of the substrate response by cosine direction alignment
    69	with the prior phenomenal snapshot, not by learned prediction errors.
    70	Predictive-processing-style refinements (e.g.\ $\eta$ as an adaptive
    71	learning rate over a prediction-error norm) are an open build, not
    72	delivered here.
    73	
    74	\textbf{vs neural mass models.} ARIA operates at the
    75	architectural-algorithmic level; it does not specify which neural
    76	circuits implement context rotation or partial emission. The 600-cell
    77	substrate is proposed as an abstract description of the criticality-
    78	maintaining structure of cortex, not as a circuit model.
    79	
    80	\subsection{The non-load-bearing ACT bridge}\label{ssec:act_bridge}
    81	
    82	The companion adaptive-closure-transport
    83	preprint~\citep{SmartAdaptiveClosureTransport2026} proposes a
    84	4-tuple bridge
    85	$(M, L_{M}, W, R_{\mathrm{hom}})$ — substrate $M$, response operator
    86	$L_{M}$, learnable Hebbian-like field $W$, and a homeostatic
    87	regulariser $R_{\mathrm{hom}}$. We propose the dictionary
    88	$D_{\mathrm{ACT}}$:
    89	\[
    90	D_{\mathrm{ACT}}\colon (M, L_{M}, W, R_{\mathrm{hom}})
    91	\;\longmapsto\;
    92	(\Rsixhundred,\ \Cph,\ \text{cascade pressure field}\ W_{\mathrm{p}},
    93	   \ \texttt{homeostatic\_reset}).
    94	\]
    95	\textbf{This bridge is non-load-bearing for the present paper.} It is
    96	included as a route-K (alternative-route) reading; the substrate-
    97	witness claims (six signatures, $18/18$, chess $+40.6$pp,
    98	HCP $\sigma$-distances) do not require any of the ACT theorems.
    99	
   100	\textbf{What ACT would have to deliver to make this load-bearing.}
   101	The companion preprint identifies four open builds, each of which is
   102	deferred:
   103	\begin{itemize}\itemsep=2pt
   104	\item A Lyapunov function $V(W)$ on the reduced flow whose
   105	  monotonicity proves selection — not delivered.
   106	\item An edge-space decomposition of $\mathbb{R}^{E_{M}}$ under the
   107	  Hodge edge Laplacian $L_{\mathrm{edge}} = \delta_{2}\delta_{2}^{\mathsf T} +
   108	  \delta_{1}^{\mathsf T}\delta_{1}$ — not delivered.
   109	\item A formal $2I$-equivariance audit of the closure operator
   110	  family — not delivered.
   111	\item A full reduced-flow convergence theorem on
   112	  $W$-trajectories — not delivered.
   113	\end{itemize}
   114	Until these are delivered, ARIA is positioned as the empirical
   115	\emph{substrate witness} for the family that ACT names; ACT is not the
   116	selection-theorem witness for ARIA. The companion kernel
   117	document~\citep{SmartAriaClosureKernel2026} discusses the same $\Cph$
   118	in a passive-regime witness via the $B\to K^{*}\mu^{+}\mu^{-}$ flavour
   119	anomaly~\citep{SmartBAnomaly2026}; that line shares operator-level
   120	infrastructure with this paper, but does not transfer empirical
   121	support for ARIA.
   122	
   123	\subsection{The strong-coupling reading for cortical architecture}
   124	
   125	Real cortical criticality is maintained by multiple parallel

exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex' | sed -n '145,190p'; nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/06_stress_tests.tex' | sed -n '117,150p'; nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/08_discussion.tex' | sed -n '123,175p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 364ms:
   145	$0/2000$ were below the preregistered floor $+0.10$; we report these
   146	as $0.0000$ rather than $P=0$ to avoid the suggestion of an exact
   147	zero-probability statement on a finite resample.
   148	
   149	\textbf{Factorial interaction estimator.} For the $2{\times}2$
   150	ablation conditions $\{----, -C--, --P-, -CP-\}$, the interaction is
   151	\[
   152	\Delta_{CP}
   153	\;=\;\frac{(\alpha_{\!-CP\!-}+\alpha_{\!-\!-\!-\!-})
   154	        - (\alpha_{\!-C\!-\!-}+\alpha_{\!-\!-P\!-})}{2}.
   155	\]
   156	
   157	\textbf{$\sigma$-distance against external nulls.} For the HCP
   158	comparisons we report
   159	$Z_{m} = (m_{\mathrm{ARIA}} - \mu_{\mathrm{HCP}}) / \sigma_{\mathrm{HCP}}$
   160	on the full $n=1003$ subject distribution.
   161	
   162	\subsection{State-reset protocol}
   163	
   164	The substrate exhibits state drift: across approximately five
   165	successive depth-sweep evaluations the pressure field equilibrates
   166	to a uniform attractor and classification structure collapses to
   167	raw-feature baseline. Multi-trial benchmarks therefore require an
   168	explicit reset between successive evaluations.
   169	\texttt{kernel/dimensional\_monitor.py:DimensionalMonitor.homeostatic\_reset(level=1.0)}
   170	re-initialises pressure-field, crossed-vertex, and training state to
   171	canonical baseline. With reset between depth measurements, the chess
   172	LOO lift recovers from $+3.1$pp (without reset, on a state-drifted
   173	substrate) to $+40.6$pp (with reset, far exceeding the $+15$pp
   174	preregistered floor). The reset protocol is documented in
   175	\texttt{docs/brain\_mapping/NON\_EQUILIBRIUM\_FINDING.md}; a more
   176	generalisable lesson is recorded in \S\ref{sec:limitations}: any
   177	multi-trial benchmark on a non-stationary substrate must specify
   178	state-reset protocol.
   179	
   180	\subsection{Reproducibility commands}
   181	
   182	\begin{itemize}\itemsep=2pt
   183	\item Substrate self-test:
   184	  \texttt{python3 -c "from kernel.sigma\_orbit\_basis import \_self\_test; \_self\_test()"}.
   185	\item Six drug/sleep signatures:
   186	  \texttt{python3 demo\_drug\_sleep\_v4.py} ($\sim 30$\,s).
   187	\item C$\times$P synergy $N\!=\!20$ deep-dive:
   188	  \texttt{python3 demo\_p4\_cxp\_deep\_dive.py} ($\sim 28$\,min).
   189	\item Eighteen preregistered:
   190	  \texttt{python3 run\_preregistered\_validation.py}
   117	\textbf{Architectural reading (substrate witness).} $C$ creates churn
   118	in \emph{which} vertices are uncrossed (frame rotation churns the
   119	uncrossed pool). $P$ promotes the high-pressure subset of the
   120	uncrossed pool to mini-emitters. The product is a non-additive
   121	novel-event-generation pathway: with both on, the uncrossed pool
   122	churns and $P$ amplifies new vertices entering the high-pressure
   123	region; with either off, the pathway collapses. The interaction
   124	$+0.19$ is comparable in magnitude to the $P$ main effect $-0.22$,
   125	so $C$ and $P$ are \emph{strongly coupled} cascade-state stabilisers
   126	on this substrate, not nearly-orthogonal ones. This reverses an
   127	architectural claim from the original 3-seed validation that held $C$
   128	and $P$ approximately orthogonal.
   129	
   130	\textbf{Disclosure: $N\!=\!20$ ordering.} The $N\!=\!20$ deep-dive
   131	was conducted \emph{after} the original $N\!=\!3$ failure
   132	(2026-04-29 vs 2026-04-20). The seed range $32000$--$32019$ was
   133	selected to be non-overlapping with the original $30000$s seeds.
   134	Two strengthening builds we have not delivered:
   135	(i) a second independent $N\!=\!20$ run at a different seed range
   136	(e.g.\ $33000$--$33019$), and
   137	(ii) an $N\!=\!50$ characterisation of the per-seed sample
   138	distribution. Both are recorded as open builds in
   139	\S\ref{sec:limitations}.
   140	
   141	\textbf{What this stress test does \emph{not} establish.}
   142	\begin{itemize}\itemsep=2pt
   143	\item It does not establish a Lyapunov function on the reduced flow.
   144	\item It does not establish that the substrate is uniquely selected by
   145	  $C\times P$ coupling among regular 4-polytopes.
   146	\item It does not establish an $\eta$-trajectory derivation; $\eta$
   147	  is treated as a condition-dependent constant in this paper.
   148	\end{itemize}
   149	The stress test is what its name says: a high-replication factorial
   150	test of one preregistered interaction prediction, on a fresh-seed
   123	\subsection{The strong-coupling reading for cortical architecture}
   124	
   125	Real cortical criticality is maintained by multiple parallel
   126	mechanisms: E/I balance, neuromodulation (acetylcholine, noradrenaline),
   127	homeostatic plasticity, gain control. The naive expectation — and the
   128	one we held until the $N\!=\!20$ deep-dive — is that these are mostly
   129	orthogonal, so losing one removes only its own main effect. The
   130	$N\!=\!20$ result reverses this on the substrate: $C$ and $P$ are
   131	strongly coupled. Disabling one cascades into losing the synergistic
   132	contribution of the other.
   133	
   134	This matches clinical observations: anaesthesia (which targets
   135	GABAergic transmission) and seizure (which targets E/I balance)
   136	produce widespread network-level dysfunction beyond their direct
   137	targets — exactly what strong synergy predicts. We position this as
   138	\emph{a hypothesis the substrate witness raises}, not as a proof.
   139	The bridge from cascade-mechanism interaction on $\Rsixhundred$ to
   140	real-cortex pharmacological coupling is a step we do not take in
   141	this paper.
   142	
   143	\subsection{Methodological contributions}
   144	
   145	Two methodological items are worth recording outside the headline:
   146	\begin{enumerate}\itemsep=2pt
   147	\item \textbf{$N\!\geq\!20$ for high-variance interaction terms.}
   148	  Allocation discipline for preregistration: when preregistering an
   149	  interaction effect on a system with unknown per-seed variance,
   150	  budget for $N\!\geq\!20$ from the start. The original 3-seed plan
   151	  was the source of two underpowered-interaction estimates in this work.
   152	\item \textbf{State-reset protocol on non-stationary substrates.}
   153	  ARIA's substrate is a non-stationary dynamical system; the
   154	  pressure field equilibrates within $\sim 5$ successive evaluations.
   155	  Any multi-trial benchmark must specify a state-reset protocol or
   156	  document the drift. Generalisable lesson: \emph{published
   157	  cross-domain benchmarks on non-stationary substrates should report
   158	  an explicit reset/equilibration discipline}, not just seed.
   159	\end{enumerate}
   160	
   161	\subsection{The substrate as a maximum-symmetry connectivity null}
   162	
   163	The HCP comparison (\S\ref{ssec:hcp}) places ARIA as a principled
   164	deterministic null reference for cortical functional connectivity.
   165	Real cortex breaks the symmetry through hub-spoke functional
   166	specialisation; the $\sigma$-distances from ARIA quantify the
   167	magnitude of biological symmetry-breaking with no fitted parameters.
   168	
   169	This is a methodological contribution to comparative connectomics.
   170	Stochastic nulls (Erd\H{o}s--R\'enyi, configuration model,
   171	edge-randomised graphs) compare cortex to a random graph with matched
   172	density. ARIA is a different kind of null: a deterministic
   173	group-theoretic graph with theorem-level statements of structure
   174	(degree std $=\!0$ by transitivity, eigenvalue spectrum
   175	$\{0, 3, 4\Ph, 6\Ph, 12{-}4\Ph, 12{-}6\Ph, 9, 12\}$ by character

exec
/bin/bash -lc "nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/02_method.tex' | sed -n '115,147p'; nl -ba '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess/paper/sections/04_consciousness_chain.tex' | sed -n '120,151p'" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 330ms:
   115	
   116	\textbf{Microstate baseline (qualifier).} The continuity-drop
   117	signature (Sig~3) follows the EEG microstate methodology lineage of
   118	Brodbeck et al.~\citep{Brodbeck2012Microstates} on wake/NREM
   119	microstates. Brodbeck et al.\ is not a propofol-specific paper; we
   120	use it for the underlying microstate-fragmentation methodology, not
   121	as a propofol reference. A propofol-specific microstate citation
   122	would tighten this section; we treat that as an open
   123	strengthening build.
   124	
   125	\subsection{Statistical methods}
   126	
   127	\textbf{Cascade-$\alpha$ fitting.} Power-law $\alpha$ is fit by
   128	ordinary least squares on the log-CCDF of the cascade-event size
   129	distribution, restricted to the central 80\% mass band (excluding the
   130	bottom 10\% and top 10\% to avoid extreme-tail noise). $R^{2}$ is
   131	reported on the linear fit in log-space. A cascade event is defined
   132	as an attention-vertex shift between consecutive ticks
   133	$\arg\max|\mathrm{state}_{t}|\neq \arg\max|\mathrm{state}_{t-1}|$;
   134	the event size is the $\ell^{1}$ norm of the state-difference vector
   135	at that tick. Zero-size events are excluded.
   136	
   137	\textbf{Bootstrap confidence intervals.} 95\% CIs on $\alpha$ are
   138	estimated by event-resampling bootstrap (500 resamples for the
   139	preregistered cascade-$\alpha$ tests, 2000 resamples for the
   140	$N\!=\!20$ C$\times$P deep-dive). Bootstrap RNG seed: 7919 for
   141	preregistered; 42 for the deep-dive.
   142	
   143	\textbf{Bootstrap one-sided $P$-value reporting.} For the C$\times$P
   144	deep-dive, $0/2000$ bootstrap resamples were at or below zero, and
   145	$0/2000$ were below the preregistered floor $+0.10$; we report these
   146	as $0.0000$ rather than $P=0$ to avoid the suggestion of an exact
   147	zero-probability statement on a finite resample.
   120	\subsection{Stimulus models}
   121	
   122	Implementation: \texttt{demo\_drug\_sleep\_v4.py}. Four conditions
   123	$\times$ $800$ ticks each at seed $42$:
   124	
   125	\textbf{WAKE.} AR(1) cortical noise ($\beta=0.90$), tonic equator-shell
   126	coherence (small always-on bias), and attention episodes (20--50
   127	ticks at amplitude $0.8$, anchored to the largest shell with $15\%$
   128	within-shell rotation per tick). The AR(1) gives temporal correlation
   129	that lets the $\eta=0.20$ self-loop integrate; tonic coherence anchors
   130	modality; attention episodes mimic biological visual fixation
   131	(200--400~ms dwell time analogue); within-shell rotation generates
   132	cascade events without changing modality.
   133	
   134	\textbf{SLEEP\_N3.} Slow oscillation ($\sim 1$\,Hz analogue,
   135	amplitude $1.0$) on a coherent shell, plus spindle bursts ($12$ ticks
   136	every $100$ at amplitude $0.4$ fast modulation), plus K-complexes
   137	($4\%$ of ticks at amplitude $0.8$).
   138	
   139	\textbf{PROPOFOL.} Low-amplitude tonic noise (amplitude $0.05$);
   140	$\eta = 0.00$ (broken recurrence). Residual cortex preserved as
   141	background drive.
   142	
   143	\textbf{RECOVERY.} Identical to WAKE — verifies determinism and
   144	reversibility.
   145	
   146	The stimulus models are deliberately structural rather than
   147	measurement-fitted: amplitudes and durations match published
   148	biological time scales but are not tuned to specific signatures.
   149	The full stimulus code is \texttt{demo\_drug\_sleep\_v4.py}. We
   150	disclose stimulus-shape choice as a methodological design move,
   151	not a derived theorem.

exec
/bin/bash -lc "cd '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess' && rg -n \"0/2000|resamples|zero|below\" docs/brain_mapping/P4_SYNERGY_FINDING.md docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md docs/brain_mapping/MANUSCRIPT_V2.md" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 354ms:
docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:45:  - **P4** (C×P synergy): observed +0.044 at N=3, below +0.10 floor.
docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:47:    far below +15pp floor.
docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:126:threshold. We do not claim point-zero independence (the estimate is
docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:139:**2026-04-29 re-run (N=5):** +0.039. Still below threshold — confirming
docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:167:**Original (N=1) failure:** +3.1pp. Far below threshold.
docs/brain_mapping/P4_SYNERGY_FINDING.md:87:This was below the +0.10 threshold, so P4 was reported as a **fail**
docs/brain_mapping/P4_SYNERGY_FINDING.md:94:N=20 deep-dive presented below shows this was wrong.**
docs/brain_mapping/P4_SYNERGY_FINDING.md:117:We then bootstrapped the interaction distribution (2000 resamples,
docs/brain_mapping/P4_SYNERGY_FINDING.md:162:Bootstrap (2000 resamples) on the 20-seed sample gives:
docs/brain_mapping/P4_SYNERGY_FINDING.md:172:The synergy is decisively positive (p = 0 against zero) and decisively
docs/brain_mapping/P4_SYNERGY_FINDING.md:189:19 of 20 seeds give a positive interaction; one is essentially zero
docs/brain_mapping/P4_SYNERGY_FINDING.md:324:detection** when the effect-size ratio (interaction/main-effect) is below
docs/brain_mapping/P4_SYNERGY_FINDING.md:389:   significantly above zero, comparable to main-effect scale) to be
docs/brain_mapping/MANUSCRIPT_V2.md:294:estimated at +0.044 — below the preregistered +0.10 threshold —
docs/brain_mapping/MANUSCRIPT_V2.md:309:Bootstrap (2000 resamples):
docs/brain_mapping/MANUSCRIPT_V2.md:397:`bounded_topk(ψ, k=12)` (zeros all but the top-12 vertices, scales
docs/brain_mapping/MANUSCRIPT_V2.md:485:95% confidence interval on α is estimated by bootstrap (500 resamples
docs/brain_mapping/MANUSCRIPT_V2.md:486:for cascade-α tests, 2000 resamples for the C×P deep-dive). Random
docs/brain_mapping/MANUSCRIPT_V2.md:529:    f = zeros(N)
docs/brain_mapping/MANUSCRIPT_V2.md:578:- For interaction terms with |effect|/|std| ratio below 2, **N ≥ 20
docs/brain_mapping/MANUSCRIPT_V2.md:708:D main:  +0.063  (small but non-zero)
docs/brain_mapping/MANUSCRIPT_V2.md:808:Zero of 1003 HCP subjects have degree std below 2.0; ARIA is far
docs/brain_mapping/MANUSCRIPT_V2.md:971:interaction-to-main-effect ratio is below 0.5. The original 3-seed
docs/brain_mapping/MANUSCRIPT_V2.md:1044:4. **Sig 2 ratio (1.83×) is below empirical point estimate (2.96×)**
docs/brain_mapping/MANUSCRIPT_V2.md:1132:- Bootstrap n_resamples = 2000, seed = 42

exec
/bin/bash -lc "cd '/mnt/c/Users/nexus/OneDrive/Documents/My Projects/aria-chess' && rg -n \"P\\(|P=0|p = 0|p=0|zero-probability|2\\.96|27\\.2|n=15|unique substrate|is consciousness|selection theorem|Lyapunov function on the reduced flow has been delivered|preregistered thresholds\" paper/main.tex paper/sections/*.tex" in /mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper
 succeeded in 247ms:
paper/sections/10_conclusion.tex:21:drug/sleep EEG signatures pass at preregistered thresholds:
paper/sections/10_conclusion.tex:34:preregistered thresholds, with two interaction tests requiring
paper/sections/10_conclusion.tex:71:derivation of consciousness, not a selection theorem on the
paper/sections/08_discussion.tex:10:selection theorem, we do not claim a Lyapunov derivation, and we do
paper/sections/08_discussion.tex:37:  passes at the preregistered thresholds. The two interaction tests
paper/sections/09_limitations.tex:183:selection theorem on the ACT bridge. We do not claim uniqueness for
paper/sections/05_results.tex:55:   OpenNeuro \texttt{ds005620} ($n=8$, $2.96{\times}$)~\citep{OpenNeuroDS005620} &
paper/sections/05_results.tex:150:all pass at preregistered thresholds, with two interaction tests
paper/sections/01_introduction.tex:76:  the unique substrate consistent with these signatures. Other regular
paper/sections/01_introduction.tex:85:\item \emph{Not a selection theorem.} The companion adaptive-closure-
paper/sections/01_introduction.tex:139:selection theorem on the 4-tuple bridge; circuit-level mechanistic
paper/sections/01_introduction.tex:160:ACT bridge (without claiming a selection theorem).
paper/sections/02_method.tex:97:($2.96\!\times$ wake) in Sig~2.
paper/sections/02_method.tex:146:as $0.0000$ rather than $P=0$ to avoid the suggestion of an exact
paper/sections/02_method.tex:147:zero-probability statement on a finite resample.
paper/main.tex:63:selection theorem, nor a uniqueness claim for the 600-cell among regular
paper/main.tex:102:reference $2.96\!\times$ from OpenNeuro \texttt{ds005620}, $n=8$);
paper/main.tex:142:We do not claim the 600-cell is the unique substrate consistent with

codex
Numerics mostly match the local sources. I’m marking the audit complete and drafting the referee verdict with must-fixes.
  ✓ Read WO context and paper
  ✓ Verify source numerics
  ✓ Audit claims and scope
  → Compile referee verdict
  ✓ Read WO context and paper
  ✓ Verify source numerics
  ✓ Audit claims and scope
  ✓ Compile referee verdict
codex
**1. Claim Audit**
- `main.tex:38`: “Once the 600-cell substrate is chosen, its graph structure is fixed by group theory...” — established for the graph facts and spectrum, provided the graph construction is exactly nearest-neighbour on the canonical 600-cell; appropriately scoped by “once chosen.”
- `main.tex:45`: “this single deterministic structure is consistent with eighteen quantitative correspondences...” — established as a threshold-consistency claim, not as a causal proof. The sentence is acceptable because it says “consistent with.”
- `main.tex:58`: “not a derivation of consciousness, nor a selection theorem, nor a uniqueness claim” — correct and load-bearing scope discipline.
- `main.tex:78`: “17/18 at standard... 18/18 after N=20 deep-dive” — matches `docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:8` and `docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:80`.
- `main.tex:82`: “six drug/sleep EEG signatures... single deterministic trajectory at seed 42” — matches `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:195`; correctly discloses single-seed status.
- `main.tex:86`: “published-reference thresholds” — correct. This is the wording that must be maintained everywhere.
- `main.tex:106`: “All six signatures pass against their published-reference thresholds” — supported by `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:32` through `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:37`.
- `main.tex:111`: “C and P are causally significant” — only established within the factorial ablation model, not in biological cortex. Suggest softening to “causally identifiable within the ablation model.”
- `main.tex:115`: “0/2000 bootstrap resamples...” — correct finite-bootstrap wording; no `P=0` overclaim.
- `main.tex:123`: “domain-invariant selective amplification on the two tasks tested” — slightly too strong: two tasks are insufficient for “domain-invariant.” Suggested edit: “selective amplification in the two cross-domain tasks tested.”
- `main.tex:132`: “selective amplification only where raw features are ambiguous” — softened by “two tasks tested” nearby, but “only where” is still stronger than evidence. Suggested edit: “in these two tasks, amplification appears when raw features are ambiguous.”
- `sections/01_introduction.tex:10`: “mechanism-driven proposals... have not yielded preregistered quantitative signatures that survive on real EEG data” — broad literature overclaim; not established here. Suggested edit: “have not, to our knowledge, yielded the kind of preregistered multi-domain quantitative benchmark tested here.”
- `sections/01_introduction.tex:12`: “structure-driven proposals produce numbers but typically introduce fitted parameters...” — broad overclaim; needs citation or softening.
- `sections/01_introduction.tex:52`: “Six drug/sleep signatures” — numerically supported, but “independent” at `sections/01_introduction.tex:36` is stronger than warranted because all six use one recurrent-layer run/stimulus design. Suggested edit: “six companion drug/sleep EEG signatures.”
- `sections/03_substrate.tex:39`: Lemma on graph facts and spectrum — plausible and internally used correctly; the claim is mathematical, not empirical. It would be stronger if the paper cited a specific spectrum derivation or supplied a short computational verification note.
- `sections/03_substrate.tex:75`: “design-level stability clamp... not a derived theorem” — excellent discipline; establishes the correct status of `\Ph^{-2}`.
- `sections/04_consciousness_chain.tex:76`: “By construction `\Phi\to0` under H4-equivariant dynamics... `\Phi > 0` only when dynamics break symmetry” — too theorem-like for the proxy as defined. Hidden assumptions: block autocorrelation equality, finite-sample behaviour, and the exact relationship between irrep-block autocorrelation and information transport. Suggested edit: “The proxy is designed to be small under H4-equivariant dynamics and to increase when dynamics produce cross-class asymmetries.”
- `sections/04_consciousness_chain.tex:143`: “RECOVERY. Identical to WAKE — verifies determinism and reversibility.” — verifies deterministic repeatability of the simulation, not biological reversibility. Suggested edit: “verifies deterministic repeatability under the WAKE stimulus protocol.”
- `sections/05_results.tex:75`: “All six signatures pass against their published-reference thresholds...” — supported and properly scoped.
- `sections/05_results.tex:88`: “17/18 standard; 18/18 after N=20 deep-dive” — supported and transparent.
- `sections/05_results.tex:149`: “Eighteen preregistered correspondences all pass...” — acceptable because the following clauses disclose methodology refinement; not a threshold-change claim.
- `sections/06_stress_tests.tex:112`: “CI entirely above preregistered threshold” — supported by `docs/brain_mapping/P4_SYNERGY_FINDING.md:162` through `docs/brain_mapping/P4_SYNERGY_FINDING.md:171`.
- `sections/06_stress_tests.tex:117`: mechanistic “pathway collapses” language — supported only inside the ablation architecture; acceptable if read as model-internal. Could soften to “the measured interaction collapses.”
- `sections/07_cross_domain.tex:87`: chess lift claim — supported by `docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:175` through `docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:190`.
- `sections/07_cross_domain.tex:102`: “~65pp architectural” — directionally OK, but “classification power” is not decomposed causally. Suggested edit: “~65% observed accuracy persists under the permutation null.”
- `sections/07_cross_domain.tex:132`: “substrate is correctly null on conversation” — acceptable relative to the preregistered neutrality band; better as “approximately neutral.”
- `sections/07_cross_domain.tex:187`: HCP null reading — acceptable and well scoped by ICA-50/cross-parcellation caveat.
- `sections/08_discussion.tex:134`: clinical anaesthesia/seizure analogy — explicitly presented as a hypothesis, not proof; acceptable but should not migrate into abstract/headline.
- `sections/10_conclusion.tex:20`: “six drug/sleep EEG signatures pass at preregistered thresholds” — incorrect and must fix. These six are not P1–P18 and are published-reference thresholds, not preregistered thresholds.

**2. Internal Consistency**
- Abstract tally is now correct: `main.tex:78` reports `17/18` standard and `18/18` with `N=20`; this matches `sections/05_results.tex:88` and the source `docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:8`.
- Threshold-refinement discipline is mostly consistent: `main.tex:81`, `sections/02_method.tex:35`, `sections/05_results.tex:126`, and `sections/08_discussion.tex:40` all say methodology refinement, not threshold change.
- One inconsistency remains: `sections/10_conclusion.tex:20` says the six drug/sleep signatures pass at “preregistered thresholds,” contradicting `main.tex:84`, `sections/02_method.tex:31`, and `sections/05_results.tex:75`. Must change to “published-reference thresholds.”
- Bootstrap wording is internally correct in the paper: `main.tex:115`, `sections/02_method.tex:143`, `sections/06_stress_tests.tex:99`, and `sections/06_stress_tests.tex:113` use finite-resample wording. No problematic `P=0` claim appears except as an avoided wording example at `sections/02_method.tex:146`.
- HCP `n=100` vs `n=1003` is now correctly handled: `main.tex:134`, `sections/07_cross_domain.tex:150`, and `sections/07_cross_domain.tex:164` distinguish preregistered `n=100` from full-cohort descriptive `n=1003`.
- P13 disclosure is now mostly correct: `sections/05_results.tex:137` through `sections/05_results.tex:146` and `sections/07_cross_domain.tex:80` through `sections/07_cross_domain.tex:85` disclose 5-fold preregistration and LOO reset refinement. However, “validation-protocol refinement on the preregistered estimator” at `sections/05_results.tex:145` is slightly confusing because the estimator changed from 5-fold to LOO. Suggested edit: “validation-protocol refinement relative to the preregistered test.”

**3. External Consistency / Numerics**
- Six v4 signatures: paper matches source.
  - Source: `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:32` through `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:37`.
  - Paper: `sections/05_results.tex:51` through `sections/05_results.tex:70`.
  - Values match: `0.463`, `1.83x`, `+0.066`, `0.33x`, recovery identical, wake `alpha=2.252 [1.82, 2.86] R^2=0.956`.
- Propofol switching ratio: paper correctly reports model ratio `1.83x` and empirical reference `2.96x`.
  - Source: `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:224` through `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:227`.
  - Paper: `main.tex:100` through `main.tex:102`, `sections/05_results.tex:54` through `sections/05_results.tex:56`.
- 18/18 preregistered tally: paper matches source.
  - Source: `docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:8` through `docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:15`, full table at `docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:80` through `docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:99`.
  - Paper: `sections/05_results.tex:88` through `sections/05_results.tex:121`.
- C×P synergy: paper matches source numerics.
  - Source: `docs/brain_mapping/P4_SYNERGY_FINDING.md:162` through `docs/brain_mapping/P4_SYNERGY_FINDING.md:168`.
  - Paper: `sections/06_stress_tests.tex:95` through `sections/06_stress_tests.tex:102`.
  - Values match: `+0.190`, CI `[+0.143, +0.239]`. Paper correctly reports `0/2000` rather than `P=0`.
- Chess lift: paper matches source.
  - Source: `docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:175` through `docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:190`.
  - Paper: `sections/07_cross_domain.tex:45` through `sections/07_cross_domain.tex:49`, `sections/07_cross_domain.tex:87` through `sections/07_cross_domain.tex:95`.
  - Values match: raw `53.1%`, substrate `93.8%`, lift `+40.6pp`, depth `n=25`, with reset.
- HCP values: paper matches source.
  - Source: `docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:347` through `docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:362`, summary at `docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:418` through `docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:421`.
  - Paper: `sections/07_cross_domain.tex:171` through `sections/07_cross_domain.tex:174`.
  - Values match: `-11.58σ`, `+79.78σ`, `+6.80σ`.
- Source-document caveat: `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:40` and `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:286` appear to say Sleep-EDFx CI `[2.50, 2.86]`, while the expected and table value is `[2.50, 2.53]` at `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:37`. The paper uses the correct `[2.50, 2.53]`.

**4. Substrate-Witness Scope Discipline**
- Good scope statements appear at `main.tex:58`, `sections/01_introduction.tex:72`, `sections/06_stress_tests.tex:141`, `sections/08_discussion.tex:95`, and `sections/10_conclusion.tex:70`.
- No sentence claims the substrate is consciousness.
- No sentence claims uniqueness among regular 4-polytopes.
- No sentence claims a delivered Lyapunov function.
- No sentence claims ACT delivers selection here.
- The main scope leak is not selection-theorem territory but threshold-provenance territory: `sections/10_conclusion.tex:20` incorrectly labels the six drug/sleep thresholds as preregistered.
- The closest uniqueness-adjacent phrase is “domain-invariant selective amplification” at `main.tex:123`; this is not a polytope uniqueness claim but is too broad for two tasks.

**5. Tightness**
- `sections/01_introduction.tex:10`: change “have not yielded preregistered quantitative signatures that survive on real EEG data” to “have not, to our knowledge, yielded this kind of preregistered multi-domain quantitative benchmark.”
- `sections/01_introduction.tex:12`: change “typically introduce fitted parameters...” to “often rely on fitted parameters, learned weights, or domain-specific calibration.”
- `main.tex:123`: change “domain-invariant selective amplification on the two tasks tested” to “selective amplification in the two cross-domain tasks tested.”
- `main.tex:132`: change “only where raw features are ambiguous” to “in these two tasks, where raw features are ambiguous.”
- `sections/04_consciousness_chain.tex:76`: change “group symmetry forbids information transport...” to “under the proxy, group-symmetric dynamics are expected to suppress cross-class asymmetry.”
- `sections/04_consciousness_chain.tex:143`: change “verifies determinism and reversibility” to “verifies deterministic repeatability under the WAKE stimulus protocol.”
- `sections/07_cross_domain.tex:103`: change “~65pp of classification power is architectural” to “65.4% accuracy persists under the architecture-only permutation null.”
- `sections/10_conclusion.tex:20`: change “preregistered thresholds” to “published-reference thresholds.”

**6. Surface Issues**
- Must-fix wording: `sections/10_conclusion.tex:20` says “six drug/sleep EEG signatures pass at preregistered thresholds”; should be “published-reference thresholds.”
- Possible wording/LaTeX issue: `sections/05_results.tex:116` table row is very long and may overflow in a standard article layout. Consider shortening the test label and moving the footnote text below the table.
- Possible wording issue: `sections/07_cross_domain.tex:74` says “The 2026-04-18 preregistration P16 specified...” while the surrounding table presents chess null as P10 and conversation null as P16. This is explainable, but reads confusingly; consider “the original combined null-permutation prediction.”
- Macro usage looks consistent for `\Ph`, `\Lop`, `\Cph`, and `\Rsixhundred`.
- Citation keys used in the paper appear represented in `references.bib`.
- Label/ref usage appears internally defined; no obvious missing section/table labels from the line-number scan.
- Capitalisation is mostly consistent: “600-cell,” “H$_4$,” “Sleep-EDFx,” “OpenNeuro,” and “C$\times$P” are used consistently.

**7. Top Three Fixes**
- Fix threshold provenance in the conclusion: `sections/10_conclusion.tex:20` must say “published-reference thresholds,” not “preregistered thresholds.”
- Soften the broad literature and generalisation claims: `sections/01_introduction.tex:10`, `sections/01_introduction.tex:12`, `main.tex:123`, and `main.tex:132` currently overstate what this paper establishes.
- Soften the theorem-like `\Phi` proxy interpretation: `sections/04_consciousness_chain.tex:76` through `sections/04_consciousness_chain.tex:79` currently reads like a proved information-transport theorem, while the paper only defines a proxy.

**8. Verdict**
Publication ready: no — must-fix list above.

The prior must-fixes are mostly closed: P13 disclosure, six-signature framing, abstract tally, bootstrap wording, C×P trend wording, Type II softening, Sleep-EDFx CI in the paper, cross-domain softening, HCP caveats, participation-ratio caveat, novelty softening, citations, and Brodbeck qualification are all substantially addressed. The remaining blocker is small but important: the conclusion mislabels the six non-preregistered EEG signatures as passing “preregistered thresholds,” and a few broad/tone claims should be softened before publication.
tokens used
161,169
**1. Claim Audit**
- `main.tex:38`: “Once the 600-cell substrate is chosen, its graph structure is fixed by group theory...” — established for the graph facts and spectrum, provided the graph construction is exactly nearest-neighbour on the canonical 600-cell; appropriately scoped by “once chosen.”
- `main.tex:45`: “this single deterministic structure is consistent with eighteen quantitative correspondences...” — established as a threshold-consistency claim, not as a causal proof. The sentence is acceptable because it says “consistent with.”
- `main.tex:58`: “not a derivation of consciousness, nor a selection theorem, nor a uniqueness claim” — correct and load-bearing scope discipline.
- `main.tex:78`: “17/18 at standard... 18/18 after N=20 deep-dive” — matches `docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:8` and `docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:80`.
- `main.tex:82`: “six drug/sleep EEG signatures... single deterministic trajectory at seed 42” — matches `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:195`; correctly discloses single-seed status.
- `main.tex:86`: “published-reference thresholds” — correct. This is the wording that must be maintained everywhere.
- `main.tex:106`: “All six signatures pass against their published-reference thresholds” — supported by `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:32` through `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:37`.
- `main.tex:111`: “C and P are causally significant” — only established within the factorial ablation model, not in biological cortex. Suggest softening to “causally identifiable within the ablation model.”
- `main.tex:115`: “0/2000 bootstrap resamples...” — correct finite-bootstrap wording; no `P=0` overclaim.
- `main.tex:123`: “domain-invariant selective amplification on the two tasks tested” — slightly too strong: two tasks are insufficient for “domain-invariant.” Suggested edit: “selective amplification in the two cross-domain tasks tested.”
- `main.tex:132`: “selective amplification only where raw features are ambiguous” — softened by “two tasks tested” nearby, but “only where” is still stronger than evidence. Suggested edit: “in these two tasks, amplification appears when raw features are ambiguous.”
- `sections/01_introduction.tex:10`: “mechanism-driven proposals... have not yielded preregistered quantitative signatures that survive on real EEG data” — broad literature overclaim; not established here. Suggested edit: “have not, to our knowledge, yielded the kind of preregistered multi-domain quantitative benchmark tested here.”
- `sections/01_introduction.tex:12`: “structure-driven proposals produce numbers but typically introduce fitted parameters...” — broad overclaim; needs citation or softening.
- `sections/01_introduction.tex:52`: “Six drug/sleep signatures” — numerically supported, but “independent” at `sections/01_introduction.tex:36` is stronger than warranted because all six use one recurrent-layer run/stimulus design. Suggested edit: “six companion drug/sleep EEG signatures.”
- `sections/03_substrate.tex:39`: Lemma on graph facts and spectrum — plausible and internally used correctly; the claim is mathematical, not empirical. It would be stronger if the paper cited a specific spectrum derivation or supplied a short computational verification note.
- `sections/03_substrate.tex:75`: “design-level stability clamp... not a derived theorem” — excellent discipline; establishes the correct status of `\Ph^{-2}`.
- `sections/04_consciousness_chain.tex:76`: “By construction `\Phi\to0` under H4-equivariant dynamics... `\Phi > 0` only when dynamics break symmetry” — too theorem-like for the proxy as defined. Hidden assumptions: block autocorrelation equality, finite-sample behaviour, and the exact relationship between irrep-block autocorrelation and information transport. Suggested edit: “The proxy is designed to be small under H4-equivariant dynamics and to increase when dynamics produce cross-class asymmetries.”
- `sections/04_consciousness_chain.tex:143`: “RECOVERY. Identical to WAKE — verifies determinism and reversibility.” — verifies deterministic repeatability of the simulation, not biological reversibility. Suggested edit: “verifies deterministic repeatability under the WAKE stimulus protocol.”
- `sections/05_results.tex:75`: “All six signatures pass against their published-reference thresholds...” — supported and properly scoped.
- `sections/05_results.tex:88`: “17/18 standard; 18/18 after N=20 deep-dive” — supported and transparent.
- `sections/05_results.tex:149`: “Eighteen preregistered correspondences all pass...” — acceptable because the following clauses disclose methodology refinement; not a threshold-change claim.
- `sections/06_stress_tests.tex:112`: “CI entirely above preregistered threshold” — supported by `docs/brain_mapping/P4_SYNERGY_FINDING.md:162` through `docs/brain_mapping/P4_SYNERGY_FINDING.md:171`.
- `sections/06_stress_tests.tex:117`: mechanistic “pathway collapses” language — supported only inside the ablation architecture; acceptable if read as model-internal. Could soften to “the measured interaction collapses.”
- `sections/07_cross_domain.tex:87`: chess lift claim — supported by `docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:175` through `docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:190`.
- `sections/07_cross_domain.tex:102`: “~65pp architectural” — directionally OK, but “classification power” is not decomposed causally. Suggested edit: “~65% observed accuracy persists under the permutation null.”
- `sections/07_cross_domain.tex:132`: “substrate is correctly null on conversation” — acceptable relative to the preregistered neutrality band; better as “approximately neutral.”
- `sections/07_cross_domain.tex:187`: HCP null reading — acceptable and well scoped by ICA-50/cross-parcellation caveat.
- `sections/08_discussion.tex:134`: clinical anaesthesia/seizure analogy — explicitly presented as a hypothesis, not proof; acceptable but should not migrate into abstract/headline.
- `sections/10_conclusion.tex:20`: “six drug/sleep EEG signatures pass at preregistered thresholds” — incorrect and must fix. These six are not P1–P18 and are published-reference thresholds, not preregistered thresholds.

**2. Internal Consistency**
- Abstract tally is now correct: `main.tex:78` reports `17/18` standard and `18/18` with `N=20`; this matches `sections/05_results.tex:88` and the source `docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:8`.
- Threshold-refinement discipline is mostly consistent: `main.tex:81`, `sections/02_method.tex:35`, `sections/05_results.tex:126`, and `sections/08_discussion.tex:40` all say methodology refinement, not threshold change.
- One inconsistency remains: `sections/10_conclusion.tex:20` says the six drug/sleep signatures pass at “preregistered thresholds,” contradicting `main.tex:84`, `sections/02_method.tex:31`, and `sections/05_results.tex:75`. Must change to “published-reference thresholds.”
- Bootstrap wording is internally correct in the paper: `main.tex:115`, `sections/02_method.tex:143`, `sections/06_stress_tests.tex:99`, and `sections/06_stress_tests.tex:113` use finite-resample wording. No problematic `P=0` claim appears except as an avoided wording example at `sections/02_method.tex:146`.
- HCP `n=100` vs `n=1003` is now correctly handled: `main.tex:134`, `sections/07_cross_domain.tex:150`, and `sections/07_cross_domain.tex:164` distinguish preregistered `n=100` from full-cohort descriptive `n=1003`.
- P13 disclosure is now mostly correct: `sections/05_results.tex:137` through `sections/05_results.tex:146` and `sections/07_cross_domain.tex:80` through `sections/07_cross_domain.tex:85` disclose 5-fold preregistration and LOO reset refinement. However, “validation-protocol refinement on the preregistered estimator” at `sections/05_results.tex:145` is slightly confusing because the estimator changed from 5-fold to LOO. Suggested edit: “validation-protocol refinement relative to the preregistered test.”

**3. External Consistency / Numerics**
- Six v4 signatures: paper matches source.
  - Source: `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:32` through `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:37`.
  - Paper: `sections/05_results.tex:51` through `sections/05_results.tex:70`.
  - Values match: `0.463`, `1.83x`, `+0.066`, `0.33x`, recovery identical, wake `alpha=2.252 [1.82, 2.86] R^2=0.956`.
- Propofol switching ratio: paper correctly reports model ratio `1.83x` and empirical reference `2.96x`.
  - Source: `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:224` through `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:227`.
  - Paper: `main.tex:100` through `main.tex:102`, `sections/05_results.tex:54` through `sections/05_results.tex:56`.
- 18/18 preregistered tally: paper matches source.
  - Source: `docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:8` through `docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:15`, full table at `docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:80` through `docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md:99`.
  - Paper: `sections/05_results.tex:88` through `sections/05_results.tex:121`.
- C×P synergy: paper matches source numerics.
  - Source: `docs/brain_mapping/P4_SYNERGY_FINDING.md:162` through `docs/brain_mapping/P4_SYNERGY_FINDING.md:168`.
  - Paper: `sections/06_stress_tests.tex:95` through `sections/06_stress_tests.tex:102`.
  - Values match: `+0.190`, CI `[+0.143, +0.239]`. Paper correctly reports `0/2000` rather than `P=0`.
- Chess lift: paper matches source.
  - Source: `docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:175` through `docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:190`.
  - Paper: `sections/07_cross_domain.tex:45` through `sections/07_cross_domain.tex:49`, `sections/07_cross_domain.tex:87` through `sections/07_cross_domain.tex:95`.
  - Values match: raw `53.1%`, substrate `93.8%`, lift `+40.6pp`, depth `n=25`, with reset.
- HCP values: paper matches source.
  - Source: `docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:347` through `docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:362`, summary at `docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:418` through `docs/brain_mapping/CROSS_DOMAIN_RESULTS.md:421`.
  - Paper: `sections/07_cross_domain.tex:171` through `sections/07_cross_domain.tex:174`.
  - Values match: `-11.58σ`, `+79.78σ`, `+6.80σ`.
- Source-document caveat: `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:40` and `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:286` appear to say Sleep-EDFx CI `[2.50, 2.86]`, while the expected and table value is `[2.50, 2.53]` at `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md:37`. The paper uses the correct `[2.50, 2.53]`.

**4. Substrate-Witness Scope Discipline**
- Good scope statements appear at `main.tex:58`, `sections/01_introduction.tex:72`, `sections/06_stress_tests.tex:141`, `sections/08_discussion.tex:95`, and `sections/10_conclusion.tex:70`.
- No sentence claims the substrate is consciousness.
- No sentence claims uniqueness among regular 4-polytopes.
- No sentence claims a delivered Lyapunov function.
- No sentence claims ACT delivers selection here.
- The main scope leak is not selection-theorem territory but threshold-provenance territory: `sections/10_conclusion.tex:20` incorrectly labels the six drug/sleep thresholds as preregistered.
- The closest uniqueness-adjacent phrase is “domain-invariant selective amplification” at `main.tex:123`; this is not a polytope uniqueness claim but is too broad for two tasks.

**5. Tightness**
- `sections/01_introduction.tex:10`: change “have not yielded preregistered quantitative signatures that survive on real EEG data” to “have not, to our knowledge, yielded this kind of preregistered multi-domain quantitative benchmark.”
- `sections/01_introduction.tex:12`: change “typically introduce fitted parameters...” to “often rely on fitted parameters, learned weights, or domain-specific calibration.”
- `main.tex:123`: change “domain-invariant selective amplification on the two tasks tested” to “selective amplification in the two cross-domain tasks tested.”
- `main.tex:132`: change “only where raw features are ambiguous” to “in these two tasks, where raw features are ambiguous.”
- `sections/04_consciousness_chain.tex:76`: change “group symmetry forbids information transport...” to “under the proxy, group-symmetric dynamics are expected to suppress cross-class asymmetry.”
- `sections/04_consciousness_chain.tex:143`: change “verifies determinism and reversibility” to “verifies deterministic repeatability under the WAKE stimulus protocol.”
- `sections/07_cross_domain.tex:103`: change “~65pp of classification power is architectural” to “65.4% accuracy persists under the architecture-only permutation null.”
- `sections/10_conclusion.tex:20`: change “preregistered thresholds” to “published-reference thresholds.”

**6. Surface Issues**
- Must-fix wording: `sections/10_conclusion.tex:20` says “six drug/sleep EEG signatures pass at preregistered thresholds”; should be “published-reference thresholds.”
- Possible wording/LaTeX issue: `sections/05_results.tex:116` table row is very long and may overflow in a standard article layout. Consider shortening the test label and moving the footnote text below the table.
- Possible wording issue: `sections/07_cross_domain.tex:74` says “The 2026-04-18 preregistration P16 specified...” while the surrounding table presents chess null as P10 and conversation null as P16. This is explainable, but reads confusingly; consider “the original combined null-permutation prediction.”
- Macro usage looks consistent for `\Ph`, `\Lop`, `\Cph`, and `\Rsixhundred`.
- Citation keys used in the paper appear represented in `references.bib`.
- Label/ref usage appears internally defined; no obvious missing section/table labels from the line-number scan.
- Capitalisation is mostly consistent: “600-cell,” “H$_4$,” “Sleep-EDFx,” “OpenNeuro,” and “C$\times$P” are used consistently.

**7. Top Three Fixes**
- Fix threshold provenance in the conclusion: `sections/10_conclusion.tex:20` must say “published-reference thresholds,” not “preregistered thresholds.”
- Soften the broad literature and generalisation claims: `sections/01_introduction.tex:10`, `sections/01_introduction.tex:12`, `main.tex:123`, and `main.tex:132` currently overstate what this paper establishes.
- Soften the theorem-like `\Phi` proxy interpretation: `sections/04_consciousness_chain.tex:76` through `sections/04_consciousness_chain.tex:79` currently reads like a proved information-transport theorem, while the paper only defines a proxy.

**8. Verdict**
Publication ready: no — must-fix list above.

The prior must-fixes are mostly closed: P13 disclosure, six-signature framing, abstract tally, bootstrap wording, C×P trend wording, Type II softening, Sleep-EDFx CI in the paper, cross-domain softening, HCP caveats, participation-ratio caveat, novelty softening, citations, and Brodbeck qualification are all substantially addressed. The remaining blocker is small but important: the conclusion mislabels the six non-preregistered EEG signatures as passing “preregistered thresholds,” and a few broad/tone claims should be softened before publication.
