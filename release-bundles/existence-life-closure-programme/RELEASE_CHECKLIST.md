# Release Checklist — v1.0.0-rc1

WO-ELC-GITHUB-REPRO-REVIEW-PACKET-001 final checklist.

## Structural

- [x] All PDFs rebuilt (compile cleanly, 0 broken refs across all 10 papers).
- [x] All source files included (`source/main.tex`, `source/references.bib`, figures).
- [x] Programme map present in every paper/note (after `\end{abstract}`).
- [x] Status taxonomy block present in every paper/note.
- [x] Extension IV withheld from primary packet (`extensions_withheld/` only).

## Content discipline

- [x] No `? ]`, `§??`, broken citations remain (audited Notes E and F).
- [x] Note C classification denominator consistent: **15/16** cases (12/12 paired + 3/4 post-draft).
- [x] Note D mood-cohort limitation fixed (acute mood, scoped, not trauma; PTSD pre/post named as gold-standard).
- [x] Note E "no real-data PASS yet" visible in abstract and conclusion.
- [x] Note F formal $\delta_{AB}$ vs empirical $\widehat{\delta}_{AB}^{\mathrm{EEG}}$ distinction clean.
- [x] Paper III does not claim ARIA is conscious (`\item Not a claim that ARIA-chess is conscious...`).
- [x] Paper III CEMI bridge says "is a candidate carrier... only if" (not "becomes the carrier... only when").
- [x] Paper I no longer depends rhetorically on cosmic-pruning extension (cosmic_demo.py mirrored as `repro/rung_tower_demo.py` with explicit standalone-artifact note).
- [x] Paper I $\tau_{\mathrm{ico}}$ vs $\tau_{\mathrm{spec}}$ appendix present.
- [x] Paper I "structural origin" softened to "common structure".

## Reproducibility

- [x] Smoke tests pass (`python repro/shared/run_all_smoke_tests.py`).
- [x] `expected_hashes.json` generated for committed artifacts.
- [x] `data_access.md` complete (every empirical claim has dataset + script + expected result).
- [x] `requirements.txt` and `environment.yml` valid.
- [x] Random-seeds discipline documented (`repro/shared/random_seeds.md`).

## Reviewer materials

- [x] `00-review-packet-overview.md` one-page entry point.
- [x] `01-falsifiers-and-roadmap.md` falsifier catalogue.
- [x] `review/reviewer_start_here.md` written.
- [x] `review/packet_order.md` written.
- [x] `review/status_taxonomy.md` written.
- [x] `review/non_claims.md` written.
- [x] `review/known_limitations.md` complete.

## Repository hygiene

- [x] README review path clear.
- [x] LICENSE present (Apache-2.0 code + CC BY 4.0 prose dual licence).
- [x] CITATION.cff present.
- [x] CONTRIBUTING.md present.
- [x] CHANGELOG.md present.
- [x] No raw data committed unless licence permits (external datasets accessed via `data_access.md`).

## Final acceptance condition (per WO §"Final acceptance condition")

A reviewer can:

1. Clone the repository. ✓ (when pushed to GitHub)
2. Read the overview. ✓ (`00-review-packet-overview.md`)
3. Understand the packet order. ✓ (REVIEW_PACKET.md and `review/packet_order.md`)
4. See that Extension IV is withheld. ✓ (explicit in overview §3 and README "Withheld" section)
5. Run smoke tests without external data. ✓ (`python repro/shared/run_all_smoke_tests.py`)
6. Find data-access instructions for full analyses. ✓ (`repro/shared/data_access.md`)
7. Reproduce synthetic / structural demos. ✓ (smoke test runner exercises all)
8. See all limitations and falsifiers upfront. ✓ (`01-falsifiers-and-roadmap.md` + `review/known_limitations.md` + `review/non_claims.md`)
9. Distinguish formal claims, conditional bridges, empirical proxies, completed results, and future proposals. ✓ (status taxonomy block in every paper + `review/status_taxonomy.md`)

**Release status: ready for `git init` and push to vfd-org/existence-life-closure-programme as v1.0.0-rc1 (pre-peer-review).**

## Recommended next strengthening move (post-release)

Per the strategic recommendation in the parent WO: build the **PTSD pre/post-therapy
longitudinal EEG validation** as the single highest-impact next step. The
hypothesis pair is:

- Primary: $\mathrm{CCR}_{\mathrm{pre}} > \mathrm{CCR}_{\mathrm{post}}$ for clinical responders, $d_z > 0.5$.
- Secondary: $\rho(\Delta \mathrm{CCR}, \Delta \mathrm{PCL\textnormal{-}5}) > 0.3$.

Required controls: healthy controls measured twice; waitlist or
delayed-treatment arm; band power + global synchrony + PLV baselines;
D1–D5 diagnostic pre-check; no feature retuning after seeing outcomes.

This converts the trauma identification from "structural account" to
"preregistered clinical prediction" and is the next major release target.
