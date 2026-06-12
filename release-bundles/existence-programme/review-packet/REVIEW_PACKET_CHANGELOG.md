# Review Packet Changelog

## 2026-05-22 — Review-packet preparation per WO-EXISTENCE-PROGRAMME-REVIEW-PACKET-001

### T1 — Programme overview added
- `primary/00-programme-overview.md`: one-page review-packet overview with thesis, packet structure (5 main + 4 optional), exclusion note for Paper IV, review request (5 evaluation points), conventions, falsifier suite.

### T2 + T3 — Packet IDs and status taxonomy
- Added "Programme map (review-packet 2026-05-22)" paragraph after `\end{abstract}` in all 9 included papers, with stable packet labels (Paper I/II/III, Note A–F, Extension IV withheld).
- Added "Status taxonomy" block (Theorem / Conditional Proposition / Empirical Result / Empirical Proxy / Pre-registered Proposal) to all 9 included papers.

### T4 — Paper I (Existence as Closure)
- §2 title: "The unfinished business of fundamental science" → "Motivating open problems: why a closure condition may be useful".
- "all five share a common structural origin" → "the framework explores whether these five may share a common structural condition".
- New Appendix: "The two $\tau$ conventions" — explicitly states $\tau_{\mathrm{ico}}$ (dim 94, theorem-grade, icosian/Galois) vs $\tau_{\mathrm{spec}}$ (dim 116, basis-robust, used in sim demos); shared properties (involutivity, commutation, non-trivial fixed subspace); the basis-change residual.
- CP-universal-5.1 language audited: now says "operator-invariance closed; equality is definitional" everywhere; CP-rung-9.3 says "closed for polytope rungs, $\tau$-convention-dependent".

### T5 — Paper II (Life as Closure)
- New §2.x "Central claim: a mechanics of meaning-generation" paragraph after the reader's map: explicitly states the framework proposes a universal *mechanics of meaning-generation*, not a universal content of meaning.
- Purpose regimes renamed: "Survival-purpose" → "Preservation regime"; "Growth-purpose" → "Growth regime"; "Decay-purpose" → "Collapse regime / negative purpose-gradient regime". Added explicit note: "the framework does not call collapse a purpose; it identifies it as a negative purpose-gradient regime."
- §13 title renamed to "Derived applications: identity, trauma, flow, creativity, hope, trust, and self-deception".
- Dyscoherence caveat added: "Dyscoherence is not pain itself. It is the measurable structural condition under which pain, distress, disorientation, or trauma may become likely under P-A."
- Qualia caveat added: "Spectral signature is a structural correlate, not an explanation of why experience has qualitative character. The hard problem of consciousness is not addressed by this identification, only mapped onto a structural quantity that can be measured."

### T6 — Note C (Closure-as-Distance)
- Verified previously in Round 5 codex pass: 16-case ledger, "best-predicted-by" wording, RNN CAD-v1.5 calibration-boundary, mood addendum explicit, FTD false positive disclosed, "proxy" language consistent.

### T7 — Note B (Cortical Phase Closure)
- Narrow-claim scope note added at top of Introduction: "this note does not claim to detect consciousness directly. It identifies a reproducible, multi-axis cortical wave-organisation displacement... The consciousness interpretation is handled only in Paper III and remains conditional on P-A."
- Volume-conduction language already softened in Round 5: "argues against scalp-volume conduction as the sole explanation."
- LOSO vs in-sample numbers already separated in Round 5.

### T8 — Paper III (Processing to Point of View)
- "$\Phi_\lambda = I - \lambda C_\varphi$ contraction-update convention" paragraph already added in Round 5.
- "No competitor predicts opposite-signed deviations at this magnitude" → "This pattern of opposite-signed deviations at this magnitude is not, to our knowledge, a standard prediction of existing comparator theories."
- Consciousness-claim boundary already in §scope: "Not a claim that ARIA-chess is conscious."

### T9 — Notes A, D, E, F
- Note A: Programme Position box + abstract scope note already in place (Round 5).
- Note D: Title retitled; "identifies suffering" softened to P-A proxy; full reproducibility-specifics block added (Round 5).
- Note E: MOBA contradictions resolved; "no real-data PASS yet" in abstract; preregistration logic conditional (Round 5).
- Note F: Formal δ_AB vs empirical δ̂_AB^EEG notation distinction; H3 fail honest (Round 5).

### T10 — Folder restructure
- `review-packet/primary/`: 9 PDFs renamed with stable packet IDs (I–III, Note A–F) + `00-programme-overview.md`.
- `review-packet/extensions/`: `IV-cosmic-self-pruning-frame-recurrence.pdf` (withheld from primary review).
- `review-packet/REVIEW_PACKET_CHANGELOG.md` and `REVIEW_PACKET_CHECKLIST.md` at top level.

## Pre-WO history (2026-05-22 day, before this WO)

5 codex review rounds applied to all 10 papers + 1 deeper round on Papers 01, 02, 07. Major changes included:
- τ_ico vs τ_spec disambiguation
- Subspace-invariance vs pointwise-fixed semantic split
- Banach contraction restricted to neighbourhood of φ
- Multiple theorem demotions to Conditional Propositions in Paper 02 (memory, trust, self-deception, boundary, repair, thought, flow-time, creativity, trauma)
- Non-periodic recurrence theorem demoted to Conditional Proposition in Paper 04 (with H-aperiodic hypothesis)
- 15/16 ledger discipline in Paper 07
- CAD-D1–D5-v1 strict-vs-PASS-leaning audit script `src/strict_vs_passleaning_audit.py` added
- Volume-conduction language softened across Papers 03 + 06
- Bibliography hygiene across all 10 papers
- Path corrections, demo counts, repro paths

See `docs/reviews/SYNTHESIS_round1.md` for the full multi-round audit log.
