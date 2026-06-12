# Prime-number work: full audit — 2026-06-12

What is public, what is local, and the review state of every paper.
"Public-monorepo" = inside github.com/vfd-org/vfd-crystallisation (pushed, but
buried — nobody is routed to it). "Standalone" = its own repo (the shop window).

## A. Public — standalone repos (canonical surfaces)

| repo | pushed | contents | state |
|---|---|---|---|
| **closure-positivity-lab** | 2026-06-11 | 4 papers + prime ledger (10/10) + 5 explorables + figures | **FLAGSHIP, current.** All 4 papers GO after 6 hostile rounds; author/contact blocks done; ledger artifact + falsifiers ship |
| icosian-rh-geometric | 06-08 | flagship Weil-positivity paper (415 lines) + CLAIMS.md | working draft, 3 codex reviews; proves Q_A≥0 ⟺ RH(L) for ONE cuspidal L; positivity open |
| icosian-closure-object | 06-09 | theta-identity papers (L(Θ_I,s)=ζ_K(s)ζ_K(s−1)) | review-draft, honest scope |
| icosian-triad-v600 | 06-09 | 2 papers (945 + 539 lines), v1.1.0 | pre-peer-review; 9-class scheme, C_φ, L-identity verified exactly |
| the-24-600-spectral-bridge | 05-13 | 3-paper λ=12 bridge programme | published v-final, 51 tests |
| closure-kernel-papers | 04-30 | C_φ closure-response operator | published |
| cryptographic-prime-audit / constraint-closure-diagnostics | Jan 2026 | tools | published, older generation |

## B. Public via monorepo only (pushed 06-11, effectively invisible)

| path | artifact | state | note |
|---|---|---|---|
| `papers/millennium-rh/rh-proof.tex` | "The Riemann Hypothesis via the Cascade Closure Functional" | **SUPERSEDED, unmarked** | ⚠ **The one live dismissal vector**: a public file named `rh-proof.tex` with a proof-shaped title and no supersession banner. Fix first. |
| `papers/millennium-rh-formal/rh-formal.tex` | 2,986-line conditional ẑ(z) reformulation | draft, conditional (Bridge hyp.), internally honest, never codex-cleared | superseded rh-proof; σ-attractor + convergence sections |
| `release-bundles/rh-witness-resonance/` | 541-line paper v1.0.0-rc1 | pre-peer-review rc | RH ⟺ substrate spectral completeness (localises Hilbert–Pólya, doesn't close) |
| `release-bundles/critical-line-pullback/` | 938-line paper rc1 + 3 sims | pre-peer-review, unreviewed | 4 findings: L_sub vanishes at first 10 zeros to 1e-13; Eichler–Brandt r(p)=8(1+p²); helix; Galois twin split |
| `papers/closure-prime-statistics-probe/` | FINDINGS.md + 6 sims (75 files) | verified geometry-first, no paper | V_600 9-class Bose–Mesner scheme; NOT distance-regular |
| `papers/primes-as-closure-irreducibles/` | 706-line tex | draft, unreviewed | primes into cascade σ-classes via Dedekind splitting on Z[φ] |
| `release-bundles/translation-engine-v2/` | v0.1 skeleton tracked; **v0.3 code/data UNTRACKED** | prototype, **stale public copy** | memory caveat stands: prime→eigenvalue map hardcoded/fitted; superseded by vfd_math_engine. Deprecate publicly, don't push v0.3 |
| `papers/millennium-bsd-formal`, `-ym` | bsd-formal.tex, ym tex | honest single-conditional-lemma state (2026-04-24 pass) | adjacent, not prime-core |

## C. Local only (unpublished)

| path | contents | state | publish? |
|---|---|---|---|
| `release-bundles/fractal-tiling-theorem/` | ~80 subdirs: the RH research engine | mixed | selectively |
| ├─ `icosian_brandt_cuspidal_geometry/` | icosian-realization.tex + route_b sims | **verified-no-fit** (24/24 primes; the 664/664 extension already ships in closure-positivity-lab) | content already public via provenance_664; the realization paper is the natural Wave-1 anchor source |
| ├─ `vfd_math_engine/` | gate-first geometry↔arithmetic certifier | prototype, load-bearing internally | later, own repo |
| ├─ `route_b/`, `route_c/` | RH⟺contraction + honest negatives (envelope/funnel/scattering) | verified negatives | feed the Wave-4 "where the wall is" paper |
| ├─ `paper/rh-frontier-capstone.tex` | 538 lines | frontier synthesis, unreviewed | Wave-4 source material |
| ├─ 40+ frontier MDs (QUASICRYSTAL, CONNES_POSITIVITY, DEBRANGES, KATZ_SARNAK…) | research log | internal | no (archive) |
| `release-bundles/frontier-run/` | extended Brandt compute package (a_q to norm 4999) | raw compute; its key output `a_q_extended.json` already ships in closure-positivity-lab | no (data already public) |
| local copies of icosian-rh-geometric / icosian-triad-v600 / the-24-600-spectral-bridge | staging mirrors of public repos | — | no action |

## D. Paper state ladder (prime work only)

**Review-hardened, GO (publishable as-is):**
closure-diffraction-rh · prime-phenomena-ledger · how-the-primes-work (Prime
Patterns in Five Computed Pictures) · total-positivity-closure-law — all four
in closure-positivity-lab, 6 hostile rounds, bundle-level GO, numerics traced.

**Working drafts with claims-ledgers (public, defensible, one more pass each
before promotion):** icosian-rh-geometric flagship · icosian-closure-object ·
icosian-triad-v600.

**Pre-review rc's (public-but-buried; harden before routing anyone to them):**
rh-witness-resonance · critical-line-pullback.

**Drafts/unreviewed (public-but-buried):** rh-formal (conditional) ·
primes-as-closure-irreducibles · closure-prime-statistics-probe (findings, no
paper).

**Superseded (must be marked):** millennium-rh/rh-proof.tex.

**Local research (not papers):** fractal-tiling-theorem engine + frontier-run.

## E. Recommended actions, in order

1. **Mark rh-proof.tex superseded** (banner + README pointer to rh-formal and
   the closure-positivity-lab line of work) and push. Two-minute fix, kills
   the only public proof-shaped title in the prime stack.
2. **Decide the Wave-1 anchor**: either (a) write the standalone pure-number-
   theory Brandt paper from icosian_brandt_cuspidal_geometry/icosian-realization.tex
   (landing-plan original intent: VFD mentioned once), or (b) designate
   closure-diffraction-rh as the anchor and skip the standalone. The 664/664
   provenance is already public either way.
3. **Deprecation note on translation-engine-v2** (public copy is stale AND the
   approach was superseded by the gate-first engine; say so in its README).
4. **Wave-4 assembly** when ready: rh-witness-resonance + route_b/route_c
   negatives + rh-frontier-capstone → the "exactly where the wall is" paper;
   harden critical-line-pullback alongside or fold its findings in.
5. Nothing in fractal-tiling-theorem needs pushing wholesale; it is the lab
   notebook, not the shop window.
