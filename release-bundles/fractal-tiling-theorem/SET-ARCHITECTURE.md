# Set architecture — proposal for approval
### *what to publish, what is companion, what is scaffolding — and the spine*

> **Status: PROPOSAL. Nothing is moved, renamed, or deleted until you say go.**
> This document only *proposes* a structure. Read it, change anything, then approve.

---

## 0. The situation, stated honestly

This bundle is a **research workspace**, not a paper set. It currently holds:

- ~40 top-level `.md` notes (exploratory: `MIRROR.md`, `THE_ADJOINT.md`,
  `RH_DEBRANGES_*`, `RH_PRIME_PRESSURE_*`, `ADELIC_*`, dozens more);
- ~50 sim/probe directories (`route_b/`, `route_c/`, `rh_weil_positivity_mechanism/`,
  `positive_witness_operator/`, `icosian_brandt_cuspidal_geometry/`, …);
- a 4-paper `writeup/` (I, II, III, note) trying to be the publication;
- two newer interpretive `.md` files (`from-a-point-to-a-universe`,
  `vfd-rh-reformulation`);
- the `vfd_math_engine/` (gate + ledgers).

**A publication is a small curated extract from a workspace this size — not the
workspace itself.** The job of this document is to name that extract and wall off the
rest as provenance. Three tiers: **publishable**, **companion**, **scaffolding**.

---

## 1. The single claim (one sentence)

Everything publishable must serve exactly one honest, defensible claim:

> **The icosian / 600-cell closure geometry realizes the Dedekind-type $L$-function
> $\zeta_K(s)\zeta_K(s-1)$ over $K=\mathbb{Q}(\sqrt5)$, and a mechanical verification
> gate certifies that it does *not* realize the Riemann $\zeta$ itself: the natural
> "substrate $\to \zeta$" bridge is negative on multiple independent diagnostics. The
> closure geometry's arithmetic reach is exactly $\zeta_K$, not $\zeta$.**

This is a **reach-and-limit** result. It is modest, true, verified, and — crucially —
it does **not** claim to approach RH. It *maps a boundary and stops at it.* That is its
strength and its honesty.

It also has a clean relationship to your published work (see §5): it is the **next
rung** after `icosian-triad-v600`, which established the $\zeta_K$ reach; this adds the
certified limit.

---

## 2. PUBLISHABLE — one paper

**`reach-and-limit.tex`** (new, assembled from existing material):

- **Title (working):** *The Closure Geometry Reaches $\zeta_K$, Not $\zeta$: a Certified
  Negative on the 600-Cell Bridge.*
- **Built from:** the $(O2)$ negative + the verified correspondences. Specifically, it
  absorbs the honest, surviving content of **Paper II** (the engine + the $(O2)$
  negative, two independent routes) and the **verified-correspondence core** of
  **Paper I** (icosian $\to \zeta_K(s)\zeta_K(s-1)$; 24-cell $\to \zeta(s)\zeta(s-1)$;
  $\varphi$-shell $\to L(s,\chi_5)$) — with Paper I's $\zeta_K$ realization **cited to
  the published `icosian-triad-v600`** rather than re-proved.
- **Scope stamps:** no RH claim; no positivity/operator claim; no cosmology. The
  Siegel–Weil identity stays a clearly-labelled sketch + numerical corroboration; the
  class-number-one input stays pinned to Kirschmer–Voight.
- **Why one paper, not four:** the genuinely new, publishable content is narrow (the
  certified negative + the method). One disciplined paper reads as rigor; four thin ones
  read as padding.

**Reproducibility appendix:** the `vfd_math_engine/` (gate, certificates, ledgers) — the
machine-checkable backing for the negative. Stays as a code companion to the one paper.

---

## 3. COMPANION — clearly labelled, not claimed as papers

These ship *with* the paper as context, each explicitly marked non-load-bearing:

| file | role | format |
|---|---|---|
| `paper-III-positivity-wall` | expository background: RH = one positivity, many faces; the $\mathbb{F}_1$ ledger; the wall | keep `.tex`/PDF **or** demote to `.md` appendix (your call) |
| `from-a-point-to-a-universe.md` | intuition: the scale–phase / Riemann-sphere picture | `.md`, interpretation only |
| `vfd-rh-reformulation.md` | the falsifiable $\mathcal{V}_1$ / witness-operator proposal | `.md`, conjectural + falsifiable |
| `note-shared-object` | the cosmology↔RH firewall note | keep only if the paper ever touches the programme; otherwise **fold into the paper's scope section** |

---

## 4. SCAFFOLDING — provenance, not publication

The ~40 exploratory `.md` notes and ~50 sim directories are the **research trail**. They
should **stay in the repo as provenance** (they show the work was done honestly and is
reproducible) but be **clearly designated not-for-publication** — ideally moved under a
single `research-notes/` and `sims/` umbrella so the bundle root shows only the paper +
companions + engine. *Nothing deleted; just organized so the signal isn't buried.*

---

## 5. Where it sits vs `icosian-triad-v600` (already published)

- `icosian-triad-v600` (PUBLISHED): established the geometry $\to \zeta_K$ realization
  (the *reach*).
- **This paper (NEW):** certifies the *limit* — the same geometry does **not** reach
  $\zeta$; the bridge is negative. **Reach-and-limit rung.**
- Relationship is **citation, not duplication:** the new paper cites the published
  $\zeta_K$ result and adds the certified negative + the verification method. This avoids
  the overlap codex flagged in Paper I.

---

## 6. Proposed reading order (the spine)

1. **`reach-and-limit.tex`** — the claim, the verified correspondences (citing the
   published $\zeta_K$ work), the certified $(O2)$ negative, scope.
2. **`vfd_math_engine/`** — reproduce every certificate.
3. **`paper-III`** *(companion)* — where the wall sits in the broader RH landscape.
4. **`from-a-point-to-a-universe.md`** *(companion)* — the intuition.
5. **`vfd-rh-reformulation.md`** *(companion)* — the falsifiable forward-look.

One paper, one engine, three clearly-marked companions. The ~90 scaffolding items sit in
`research-notes/` + `sims/` as honest provenance.

---

## 7. What I'd do on "go"

1. Assemble `reach-and-limit.tex` from the surviving Paper I + Paper II content (citing
   `icosian-triad-v600`); compile to PDF.
2. Finish the honesty fixes codex flagged (the GUE-rigidity contradiction, the
   "first-zero ≈ 22" stat, "five independent" → "five diagnostics") *in the assembled
   paper* — not in the soon-to-be-retired Paper II.
3. Demote/relocate companions and scaffolding per §3–§4 (move, never delete).
4. Rewrite `INDEX.md` as the spine in §6.
5. Re-run codex on the single assembled paper for a clean second-pass verdict.
6. Rebuild all PDFs.

**Decision points for you:**
- (a) Keep Paper III as a `.tex`/PDF companion, or demote to `.md`?
- (b) Title for the one paper — the §2 working title, or your own?
- (c) Move scaffolding under `research-notes/` + `sims/`, or leave the root as-is?

Approve as-is, or change any of it. Nothing happens until you do.
