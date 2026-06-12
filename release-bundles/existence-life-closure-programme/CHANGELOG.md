# Changelog

All notable changes to the Existence / Life / Closure Programme.

This project follows a `MAJOR.MINOR.PATCH-PRE` versioning scheme.
The current release is **1.0.0-rc1** (release candidate 1; pre-peer-review).

## [1.0.0-rc1] — 2026-05-22

### Added
- Programme overview (`00-review-packet-overview.md`).
- Falsifier and roadmap document (`01-falsifiers-and-roadmap.md`).
- Status taxonomy (Theorem / Conditional Proposition / Empirical Result / Empirical Proxy / Pre-registered Proposal) in every paper and note.
- Stable packet IDs (Paper I/II/III, Note A–F, Extension IV withheld) in every paper.
- $\tau_{\mathrm{ico}}$ vs $\tau_{\mathrm{spec}}$ convention appendix in Paper I.
- Central meaning-mechanics section in Paper II.
- Reproducibility infrastructure: smoke-test runner, expected hashes manifest, data-access guide, random-seeds guide.
- Reviewer documentation: start-here, packet-order, status-taxonomy, non-claims, known-limitations.
- Strict-vs-PASS-leaning audit script for Note C.

### Changed
- Paper I §2 title softened: "The unfinished business of fundamental science" → "Motivating open problems: why a closure condition may be useful".
- Paper I compression wording: "structural origin" → "common structure".
- Paper II purpose regimes: Survival/Growth/Decay → Preservation/Growth/Collapse (or negative purpose-gradient).
- Paper II §13 retitled: "Further structural objects" → "Derived applications".
- Paper III CEMI bridge: "EM field becomes the carrier" → "EM field is a candidate carrier... only if".
- Paper III ARIA evidence: "No competitor predicts" → "is not, to our knowledge, a standard prediction of existing comparator theories".
- Note B Introduction: added scope note ("does not claim to detect consciousness directly").
- Note B volume-conduction language softened ("argues against scalp-volume conduction as the sole explanation").
- Note D title retitled: "Cortical Closure Residual as a First-Order Proxy for Chronic Functional Dyscoherence".
- Note D mood-cohort status: cross-cohort replication scoped as acute mood (not trauma), with PTSD pre/post therapy as gold-standard external validation.
- Note E reframed: honest-negative methodology-boundary paper; no real-data PASS yet.
- Note F: formal $\delta_{AB}$ vs empirical $\widehat{\delta}_{AB}^{\mathrm{EEG}}$ notation distinction.

### Demoted (theorem $\to$ conditional proposition)
- Paper II: memory persistence, trust stability, self-deception, boundary maintenance, repair, thought persistence, flow time-dilation, creativity, trauma persistence.
- Paper IV: non-periodic recurrence (under H-aperiodic hypothesis).

### Fixed
- Paper I L324: Banach contraction now restricted to neighbourhood of $\varphi$, not full $[1, 2]$.
- Paper I L352: self-similarity claim corrected (contraction belongs to $I - \lambda C_\varphi$, not $C_\varphi$).
- Paper I L377: $C = \mathrm{Fix}(\tau)$ reframed as definitional stipulation, not derived equality.
- Paper I CP-universal-5.1: language consistent ("operator-invariance closed; equality is definitional").
- Paper I CP-rung-9.3: status consistent ("closed for polytope rungs under spectral $\tau$").
- Paper I demo counts consistent (D1–D8 throughout).
- Paper I references.bib stray `}` removed.
- Paper III: $\Phi_\lambda = I - \lambda C_\varphi$ contraction-update convention added; subject count corrected to 21 unique subjects.
- Paper III ARIA path corrections.
- Note C: "iff" core claim softened to "best predicted by"; PASS-leaning rule restated; 16-case ledger; AF FAIL under current rule; headline t-values recomputed from JSON.
- Note B: LOSO vs in-sample numbers explicitly separated; cross-cohort "matched effect size" → "comparable in-sample".
- Note F: H3 reported honestly as FAIL (was reported as "still met").
- Bibliography hygiene across all 10 papers (`\bibliography{refs}` → `\bibliography{references}`, `SmartLifeClosure` → `SmartLifeAsClosure`).

### Removed
- Extension IV (Cosmic Self-Pruning and Frame Recurrence) is intentionally not part of the primary review packet. PDF moved to `extensions_withheld/`; conceptual content unchanged from earlier draft.

### Validated
- All 10 papers compile cleanly (0 broken refs).
- All synthetic / structural sim demos pass at seed 42 (smoke tests in `repro/shared/run_all_smoke_tests.py`).

## Pre-1.0 history

Multi-round codex review iteration on the 10-paper workspace:

- **Round 1** (2026-05-22 morning): full audit of all 10 papers; identified
  ~15-20 substantive blockers per paper.
- **Round 2** (2026-05-22 day): foundation rebuild applied (τ semantics,
  pointwise/invariant subspace distinction); 10-paper programme map; SL
  status refresh; bibliography hygiene; ~5-10 blockers per paper.
- **Round 3**: theorem demotions in Paper 02; CAD ledger fixes in Paper 07.
- **Round 4**: narrow ledger/count items.
- **Round 5** (2026-05-22 evening): cardiac AF verdict; H3 fail honest;
  non-periodic theorem demoted; Paper 06 monotonicity claim; Paper 03
  operator/update convention; Paper 05 scope note; Paper 08 reproducibility
  block.

Each round flagged tighter and more specific issues, matching the
convergence pattern documented in
`docs/reviews/SYNTHESIS_round1.md` (preserved in the upstream workspace
at `release-bundles/existence-programme/`).
