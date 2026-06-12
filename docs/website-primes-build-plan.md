# Website build plan: the /primes/ section (2026-06-12)

Self-contained build spec for vibrationalfielddynamics.org. Every content
source is a file in **github.com/vfd-org/closure-positivity-lab** (the single
canonical repo for the prime narrative — "the lab" below). Nothing on the
site should restate a number that isn't in a repo artifact; every page links
the file that proves its claims.

**Acceptance test (unchanged):** a cold-landing number theorist reaches a
verification command in two clicks, never having seen the word
"consciousness". A casual visitor reaches a playable explorable in one.

## 0. Register rules (apply to every page)

- Banned: "breaking", "proof of consciousness", "unified geometry of
  reality", "theory of everything", "multiverse", "paradigm", "resonance"
  as decoration. RH/GRH never claimed; scope boxes are verbatim from the
  papers, never softened or hyped.
- Every result block: claim → numbers → ALL inputs → run-it command →
  falsifier → artifact link. (Template: `campaign/output/pages/*.html` in
  the vfd-crystallisation repo — adapt styling, keep structure.)
- Status badges everywhere: `reviewed-GO` / `rc` / `theorem anchor` /
  `boundary row`.

## 1. Pages and their git sources

### /primes/ — the landing page
Two doors above the fold:
- **"Check the math"** → /primes/the-anchor/ — teaser: "All 44 prime ideals,
  individually. 7/7 dimension sequence. Zero fitted parameters."
- **"See it"** → /primes/explore/ — teaser: "Derive Hardy–Littlewood by
  playing — a live sieve in your browser."
Below the fold, the five-layer narrative as cards (order = credibility
ladder): anchor → L-function → wall → ledger → pictures. Each card: one
sentence, status badge, link. Footer: the scope statement from
`explorables/index.html` (the `.scope` block) verbatim.

### /primes/the-anchor/ — the realization
Source of truth: `realization/README.md` (mirror its claims table exactly).
- PDF: `realization/paper/icosian-realization.pdf` (v1.0.0-rc2, 6 review rounds)
- Claims table rows link artifacts: `realization/data/level31_per_ideal.json`
  (44/44 per-ideal + the σ-convention sentence — quote it),
  `realization/data/dimension_sequence.json` (7/7),
  `realization/data/level41_results.json` (9/9),
  `realization/data/level61_results.json` (genus-2 RM).
- Run-it block: `cd realization && python3 -m pytest tests/` (23 gates) +
  `python3 route_b/no_fit_guard.py`.
- Falsifier section from the README's "How it stays honest" + the per-ideal
  script's fail-on-any-ideal property.

### /primes/the-l-function/ — closure-diffraction
(As specified in docs/website-update-prompt.md §2 — unchanged.)
- PDF: `papers/closure-diffraction-rh.pdf`; artifacts
  `out/provenance_664.json` (now with the 663-good-prime/Steinberg note),
  `out/curve_zeros.json`; media `figures/fig_diffraction.png`,
  `figures/anim_diffraction.mp4` (use the animation).
- Mandatory scope box verbatim from the lab README lines 9–13.

### /primes/where-the-wall-is/ — the honest-RH page
- Sources: `papers/total-positivity-closure-law.pdf` (the finite law +
  localisation), the lab README "The lab underneath" table (positivity
  verdicts incl. FINITE_POSITIVE_ASYMPTOTIC_OPEN), and the scope box.
- Structure: what is proven (Q_A ≥ 0 ⟺ RH(L), cite icosian-rh-geometric
  repo) → what is computed (664/664, 33 zeros) → what was honestly killed
  (margins don't stabilize — quote the lab README) → where the wall is
  (all-places positivity). Tone: "a programme that publishes its own
  negative results."
- Upstream material (now hardened, 2026-06-12): link as "supporting
  material" at the bottom of this page —
  [critical-line-pullback](https://github.com/vfd-org/critical-line-pullback)
  (v1.1: the exact negative Galois result + status-stamped computational
  checks) and
  [rh-witness-resonance](https://github.com/vfd-org/rh-witness-resonance)
  (v2: the conditional Hilbert–Pólya localisation target — the equivalence
  of v1 was withdrawn after review, and the page may say so: publishing
  withdrawals is part of the programme's credibility story).

### /primes/the-ledger/ — ten phenomena
- PDF: `papers/prime-phenomena-ledger.pdf`; artifact `out/prime_ledger.json`.
- Render the lab README's 10-row table as-is (badges for theorem anchors and
  the boundary row). One-command block: `python3 -m lab.prime_ledger`.

### /primes/explore/ — the five scenes
- Embed the lab's `explorables/` directly (they are self-contained HTML +
  data JS; host them as static files, do not rewrite):
  `index.html` (the tour — adapt as the page itself), `residue-wheels.html`,
  `gap-slider.html` + `gap_data.js`, `chebyshev-race.html` + `race_data.js`,
  `crystal-diffraction.html` + `crystal_data.js`.
- PDF: `papers/how-the-primes-work.pdf` ("Prime Patterns in Five Computed
  Pictures") linked from the tour's scene 5.
- Figures for social cards: `figures/fig_wheels.png`,
  `figures/fig_gap_bullseyes.png`, `figures/fig_bias_race.png`,
  `figures/fig_prime_diffraction.png`, `figures/fig_fibonacci.png`.

## 2. Site integration

- Nav: add "Primes" as a top-level item → /primes/.
- Homepage: the "For mathematicians" door (from the main website prompt)
  points to /primes/the-anchor/; a new small "Play" card points to
  /primes/explore/.
- Articles index: add the five /primes/ pages under a "Prime numbers and
  the zeta function" group; mark rh-witness-resonance and
  critical-line-pullback entries (if listed) as "undergoing review — not
  yet part of the narrative" or remove them from the index until §3 lands.
- Each X post in the campaign series (docs/prime-drop-plan.md §3) lands on
  its page: post 1 → /primes/explore/ (gap slider), post 2 →
  /primes/the-anchor/, post 3 → /primes/the-l-function/, post 4 →
  /primes/the-ledger/, post 5 → /primes/explore/ (wheels).

## 3. Gating: what must be true before each page ships

| page | gate | status |
|---|---|---|
| the-anchor | realization GO | ✅ done (round 6, 2026-06-12) |
| the-l-function | paper GO + provenance clarified | ✅ done |
| the-ledger, explore | papers GO, explorables register-clean | ✅ done |
| where-the-wall-is (core) | total-positivity GO | ✅ done |
| where-the-wall-is (extensions) | rh-witness-resonance (5 rounds → GO, v2 reframe) + critical-line-pullback (7 rounds → GO, v1.1) — both in standalone public repos | ✅ done (2026-06-12) |

Build order: explore → the-anchor → the-l-function → the-ledger →
where-the-wall-is → landing. (Explore first: it has zero dependencies and
is the highest-traffic target.)

## 4. Mechanics

- Pull content at build time from the GitHub repo (raw URLs or a git
  submodule) so site numbers can never drift from repo artifacts; show the
  source commit hash in each page footer ("content from
  closure-positivity-lab@<sha>").
- PDFs: link to the repo blob AND serve a copy; explorables: serve from the
  site (same directory layout so relative `*.js` data files resolve).
- At drop time: tag the lab repo `v1.0.0`, mint the Zenodo DOI, and put the
  DOI badge on /primes/ and in the repo README.
