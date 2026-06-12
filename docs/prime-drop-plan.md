# The Prime Drop — publication plan (2026-06-12)

Goal: publish the prime/RH work as one coherent narrative — papers, tests and
sims all public in git — feeding a website primes section and an X post
series. The prime drop goes FIRST, before the ebook ("The Crystal and the
Clock"); the two drops are coordinated, so everything here must be
hostile-review-clean before any routing begins.

## 1. The drop surface (one repo, five layers)

Everything routes to **github.com/vfd-org/closure-positivity-lab**:

| layer | artifact | state |
|---|---|---|
| 1. The anchor (pure NT) | `realization/` — icosian realization of Hilbert modular forms; 44/44 ideals, 7/7 dimensions, levels 41+61; 23 gate tests + no-fit guard | rc2, codex round 2 in progress |
| 2. The L-function | `papers/closure-diffraction-rh.pdf` — 664/664 provenance, 33 zeros, prime-wave reconstruction | GO (2 reviewers + 6-round bundle gate) |
| 3. The wall | `papers/total-positivity-closure-law.pdf` + the lab table | GO (bundle gate) |
| 4. The ledger | `papers/prime-phenomena-ledger.pdf` — 10 phenomena, 10/10, one command | GO |
| 5. The pictures | `papers/how-the-primes-work.pdf` ("Prime Patterns in Five Computed Pictures") + `explorables/` (5 interactives) | GO |

Reading order for a cold visitor = 1→2→3→4→5 (hardest credibility first).
Play order for a casual visitor = 5→4 (explorables first). Both routes work.

## 2. Website primes section (from docs/website-update-prompt.md, extended)

One new section, `/primes/`, four pages:

1. **/primes/** — landing: the five layers as cards, ordered for the visitor
   type ("check the math" → anchor; "see it" → explorables). The acceptance
   test stands: a cold number theorist reaches a verification command in two
   clicks.
2. **/primes/explore/** — embed `explorables/index.html` (five scenes) and the
   four interactives as-is.
3. **/primes/the-anchor/** — canonical result page for the realization
   (claim, 44/44 + 7/7 numbers, inputs, run-it block, falsifier) + the
   L-function page already specified in the website prompt.
4. **/primes/where-the-wall-is/** — the honest-RH narrative page (already
   specified): what's computed, what's proven, what's open, including the
   published negatives.

## 3. X series (campaign registry, in posting order)

All five claims are registry-ready (`campaign/registry/`); post one per week,
each with figure + repo link, per the §3b funnel. Order:

1. `prime-gap-local-law` — the warm-up (gap-6 doubling; accessible; gap-slider
   explorable as the landing page). Figure: the eight-bullseyes bar chart.
2. `brandt-point-counts` — now upgradeable to the realization framing
   (44 ideals + 664 extension; "quaternion geometry = elliptic point counts").
3. `icosian-l-function-zeros` — the diffraction animation post (anim mp4).
4. NEW: `prime-phenomena-ledger` claim — "ten phenomena, one instrument,
   10/10, one command, ~10 seconds" + scorecard figure.
5. NEW: `five-pictures` claim — the wheels figure + explorables link
   ("derive Hardy–Littlewood by playing").

Each post's landing page must exist on the site before its post goes out.

## 4. Coordination with the ebook

The ebook drop follows the prime drop. The prime series establishes the
register (computed, gated, falsifiable) that the book then narrativizes; the
book's prime/zeros chapters can cite the lab repo and the explorables
directly. **Rule: no book marketing until the prime series has run at least
posts 1–3**, so the programme's first impression in this cycle is the
checkable mathematics, not the narrative.

## 5. Pre-drop checklist

- [x] rh-proof.tex marked SUPERSEDED (pushed 2026-06-12)
- [x] realization/ in the lab repo: 44/44 + 7/7 + 41 + 61, 23 tests, guard PASS
- [ ] realization paper passes hostile review (round 2 running)
- [x] provenance_664.json level-prime row explained (663 good + Steinberg note)
- [x] all four lab papers GO + author/contact blocks consistent
- [x] registry entries for ledger + five-pictures claims (7 claims total, all generate)
- [ ] figures for posts 1, 2, 4, 5 (the bullseyes chart exists as
      fig_gap_bullseyes.png; others to generate/crop)
- [ ] website /primes/ section built (prompt ready; extend with §2 above)
- [ ] Zenodo DOI for the lab repo at drop time (one release tag)
- [ ] pins: closure-positivity-lab pinned on the profile (manual, 30s)

## 6. What stays OUT of the drop

- rh-witness-resonance + critical-line-pullback (pre-review rc's; Wave-4
  material — harden later, do not route to them now)
- rh-formal / millennium papers (conditional; not part of this narrative)
- translation-engine-v2 (deprecation note instead)
- fractal-tiling-theorem research engine (lab notebook; stays local)
