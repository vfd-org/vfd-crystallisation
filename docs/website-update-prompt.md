# PROMPT: VFD website restructure (paste this into the session that edits vibrationalfielddynamics.org)

---

You are updating the website for Vibrational Field Dynamics (vibrationalfielddynamics.org),
an independent research programme by Lee Smart (@VFD_org, github.com/vfd-org). The site
currently hosts ~60 self-published papers. An external audit (2026-06-11) found the
mathematics increasingly careful and honestly scoped, but the site routes visitors away
from the credible work: the homepage front-loads philosophy, there is no audience routing,
the strongest falsifiable results are buried among 60 papers, and there is no on-page
verification story. Your job is to restructure the narrative so a skeptical mathematician
or physicist finds a checkable result within one click, and the programme's interpretive
layer is reached only AFTER the verifiable layer earns trust.

## The governing principle

**Credibility ladder, strictly ordered.** Unconditional, checkable results first; physics
numbers second; the substrate/programme narrative third; interpretation (existence,
closure philosophy) last. Order is load-bearing: the audience must always be able to ask
"why should I keep reading?" and get a verifiable answer before being shown anything
conditional. A non-academic publisher gets no benefit of the doubt — only "complete +
undismissable" goes in the shop window.

## Register rules (apply to every page you touch)

- NEVER use: "breaking", "proof of consciousness", "unified geometry of reality",
  "theory of everything", "multiverse", "recursive truth", "paradigm shift",
  "had to exist", "the universe is conscious", "primes are alive".
- Every claim states its scope tier: theorem / computation (reproducible) /
  conditional bridge / conjecture / interpretation.
- Every headline result page carries: the claim in one sentence, the numbers
  (computed vs measured/independent), ALL modelling inputs numbered, a
  copy-paste verification block, and a "how to kill this claim" falsifier section.
- Honest negatives are featured, not hidden — they are the strongest credibility
  asset an independent programme has.

## 1. Homepage restructure

Keep the current modest "What This Is" tone but restructure to four audience doors
above the fold, replacing the single papers-list funnel:

> **VFD — spectral geometry with falsifiers.**
> Parameter-free structural results from one classical object (the 600-cell /
> icosian order). Every headline claim ships with the exact script that
> reproduces it and the test that would kill it. This is a constrained research
> programme, not a finished theory; scope labels on every claim.

Doors (each a styled card linking to one page):
1. **For mathematicians** → the L-function/Brandt page (section 2 below).
   Teaser: "664/664 prime ideals: quaternion geometry = elliptic-curve point counts."
2. **For physicists** → the mass-ratio/α canonical result page.
   Teaser: "m_p/m_e and α⁻¹ from one polytope's spectrum, zero fitted parameters."
3. **Run the code** → a reproducibility index page listing every one-command
   verification across the repos (git clone → command → expected output).
4. **The programme** → the closure-picture narrative (explicitly labelled
   "interpretive layer — read the results first").

## 2. NEW flagship page: the icosian L-function (this is the missing content)

A new paper just shipped and is the most review-hardened artifact in the programme.
Create a dedicated page for it (e.g. /articles/closure-diffraction-rh.html), linked
from the mathematicians door. Facts (use exactly these, do not embellish):

- Repo: **github.com/vfd-org/closure-positivity-lab** (paper PDF, lab code, all
  machine-readable artifacts). Paper: `papers/closure-diffraction-rh.pdf`, 6 pages,
  two independent review passes, both GO; a reviewer re-ran every headline number
  live and all reproduced.
- The object: the cuspidal face of the icosian order over Q(√5) gives a degree-4
  L-function of conductor 775 = disc(K)²·31.
- **Provenance (the undismissable core):** two structurally independent algorithms —
  geometric Brandt enumeration in the icosian order, and point-counting elliptic
  curve 31.1-a1/Q(√5) over residue fields — agree on the cuspidal eigenvalues at
  **all 664 shared prime ideals to norm 4999 (664/664, 0 mismatches)**.
  Artifact: `out/provenance_664.json`.
- **Zeros:** 33 non-trivial zeros computed to height 25; first at t₁ = 3.679;
  functional equation self-consistent (lfuncheckfeq ≈ −126 in log₂, sign ε = +1).
- **Sato–Tate:** angle distribution second moment 0.2515 vs 0.25.
- **Prime-wave reconstruction:** the explicit formula, read as one interference wave
  per prime ideal, rebuilds the critical line with NO zero data used — the
  independently-computed zeros fall on the interference fringes. (The repo has
  fig_diffraction.png and anim_diffraction.mp4 — use the animation on the page.)
- **Mandatory scope box, verbatim sentiment:** "Nothing here proves RH or any GRH.
  RH(L) for this object is GRH for one cuspidal L-function, not the classical
  Riemann Hypothesis. Weil-form margins are positive on every finite test but the
  margin does not stabilize — we report that as NOT evidence of asymptotic
  positivity."
- Falsifier section: extend the prime bound and find one mismatch; recompute zeros
  in PARI/GP (`gp -q out/_curve_zeros.gp`) and find one off the line; break the
  functional-equation check.

## 3. Canonical result pages (replace "60 papers" as the entry experience)

Build/refresh ONE canonical page per headline claim, each following the same
template (claim → numbers → all inputs numbered → run-it block → falsifier → links).
Initial set, in display order:

1. Icosian L-function / 664-prime provenance (section 2).
2. m_p/m_e = φ^(1265/81) ≈ 1835.8 vs 1836.15 (0.02%); exponent leading term
   ΔC = 15 is the top 600-cell Laplacian eigenvalue (spectrum {0,9,12,14,15},
   verifiable by diagonalising the 120×120 Laplacian; script in
   github.com/vfd-org/vfd-crystallisation under papers/paper-xxii/scripts/).
   Honest framing: structural agreement at 10⁻⁴; the exponent counting rule is
   the named modelling input.
3. α⁻¹ = 87 + 50 + π/87 ≈ 137.03611 vs 137.035999 (0.81 ppm); 50 = 9+12+14+15
   (sum of non-zero 600-cell eigenvalues); derivation of 87 is the named
   modelling input (open items exist on deriving α from first principles alone —
   say so).
4. Hypersphere cosmology: 7 observables within 0.5% of Planck simultaneously
   (existing repo hypersphere-cosmology, 94/94 tests) — reuse its README scoping.

The articles index stays, but demoted to "Full archive" behind these canonical pages.

## 4. The papers index: add supersession + status metadata

For every listed paper add two badges: STATUS (reviewed / working draft / superseded)
and TIER (theorem / computation / conditional / interpretation). Where one artifact
supersedes another (the icosian/600-cell thread especially), say "superseded by X"
and link forward. A visitor must never wonder which of seven similar papers is
canonical.

## 5. The honest-RH narrative page

One page telling the RH story truthfully end-to-end (this converts the deep RH work
from liability to asset): what was built (the geometric L-function), what is proved
(Weil-positivity equivalence Q_A ≥ 0 ⟺ RH(L) for this one L-function), what is
computed (664/664, 33 zeros, reconstruction), what was honestly killed (no separable
envelope/geometry/horizon shortcut; per-prime bounds can't force positivity; margins
don't stabilize), and exactly where the wall is (all-places positivity = an infinite
condition no finite computation closes). Title suggestion: "Exactly where the wall
is." Tone: a programme that publishes its own negative results.

## 6. Comparison + falsification page

A like-for-like table: for each headline claim — what mainstream theory says, what
VFD computes, where they agree, what future measurement/computation would
distinguish or kill it. Surface the falsification windows (JUNO mass ordering
~2031-32 is one). This is the page a professional checks to decide you're serious.

## 7. Do NOT

- Do not put consciousness/ARIA/existence content on the homepage or within one
  click of the four doors; it lives under the programme door, clearly labelled
  interpretation.
- Do not list paper counts ("60+ papers") as a selling point — volume reads as
  crank signal; depth + verification reads as serious.
- Do not soften the scope boxes for marketing; they ARE the marketing.
- Do not break existing URLs — add redirects/links from old article pages to their
  canonical result pages where applicable.

## Assets you can pull from

- github.com/vfd-org/closure-positivity-lab — README already follows the
  claim/verify/falsifier template; reuse its copy and figures (incl. the
  diffraction animation).
- The campaign repo content in the main project (campaign/output/pages/*.html) —
  four ready-made canonical result pages in exactly the right template; adapt
  their styling to the site shell.
- Existing CLAIMS.md ledgers in recent repos (icosian-rh-geometric,
  hypersphere-cosmology) for status badges.

Work through sections 1→2→3 first (one session is fine); 4→7 can follow. After the
restructure, the test is: a skeptical number theorist landing cold should reach the
664/664 claim and its verification command in two clicks, never having seen the
word "consciousness".
