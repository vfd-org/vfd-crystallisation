# VFD Revision Protocol

**Date:** 2026-04-17
**Purpose:** Every revision of every VFD paper follows this protocol to preserve the programme's confident narrative voice and prevent demoting first-principles derivations under review pressure.

---

## The narrative voice — non-negotiable

Every VFD paper adopts the following stance:

> **QM, SM, and GR are correct but incomplete descriptions of physics. Each is a shadow of the richer cascade geometry $E_8 \to H_4 \to 40 \to D_4 \to 16 \to 8 \to 0$. VFD does not replace them — it identifies the geometric substrate that underpins them, derives their equations from cascade structure, and completes them by supplying geometric origins for quantities previously treated as free parameters.**

- ✅ Never say QM, SM, or GR are wrong.
- ✅ Never position VFD as a replacement theory.
- ✅ Always show the explicit recovery map back to the standard equation.
- ✅ Emphasise what VFD *adds* (the completion) over what the shadow already achieves.
- ✅ Claim derivation where the cascade-derivation source has established it.
- ❌ Never down-tier a claim to "benchmark correspondence" or "conjecture" if `papers/cascade-derivation/` establishes it from first principles.

## Before every revision

Open the two authoritative sources first:

1. **`docs/recovery-manifest.md`** — the programme's field-narrative spine. Identify which recovery item(s) the paper carries, and confirm the manifest row for each.
2. **`papers/cascade-derivation/<relevant>.md`** — the first-principles derivation record for the paper's content. Read the source before editing the LaTeX paper; the LaTeX is a presentation layer for this source.

If the cascade-derivation source contains a rigorous derivation, the LaTeX paper must carry that derivation — not a summary, not a demoted "proposition," not a "benchmark correspondence." Transcribe the derivation faithfully. Length is not the problem; underclaiming is.

## The recovery-voice template for every section

Every derivation section in every paper uses this three-part structure:

### 1. Standard form

State the recovered equation / quantity in its textbook form, with full credit to the standard framework. Example:

> *"The Schrödinger equation $i\hbar \partial_t \psi = H \psi$ describes the evolution of a non-relativistic quantum state. It is foundational for atomic, molecular, and condensed-matter physics."*

### 2. Cascade underpinning

Identify the cascade rung and geometric structure that gives rise to the standard form. Example:

> *"In VFD, this equation is recovered from closure dynamics on the $H_4$ rung of the 600-cell. The closure field $\Phi$ evolves under a nonlinear operator governed by the closure functional $F = \alpha R + \beta E - \gamma Q$ of Paper XXXVI (cascade-foundations.md §F2)."*

### 3. Recovery map + completion

Give the explicit derivation map from cascade → standard, and state what the underpinning adds. Example:

> *"The map Nelson pairing + equilibrium tangent limit (Paper XVIII, cascade-schrodinger.md §3) yields the standard Schrödinger equation exactly. VFD completes standard QM by identifying the nonlinear residual $\delta U_{\mathrm{rel}}$ (Paper XLII) as a physical correction at the $\varphi^{-25}$ scale — testable in atom interferometry, consistent with standard Schrödinger at all currently measurable precisions."*

## Handling codex review rounds

When codex flags an issue, apply the following decision procedure:

### 1. Is this a real math / arithmetic bug?

Examples: wrong sign, wrong formula, misattributed citation, inconsistent notation, undefined symbol, broken reference. **Always fix these.**

### 2. Is this a rigour complaint about a claim the cascade-derivation source establishes?

If codex says "this isn't proved" but `cascade-derivation/<file>.md` contains the full derivation: **do not demote the claim**. Instead, **expand the LaTeX section to carry more of the derivation from the source**. Codex is correctly identifying that the LaTeX is thin; the fix is to thicken the LaTeX, not to weaken the claim.

### 3. Is this a rigour complaint about something genuinely not yet derived?

Only then do we demote — to proposition, conjecture, or open question — and say so explicitly. Items like Paper XL's T2–T4 conjectures qualify.

### 4. Is this a "tentative language" suggestion?

If codex says "replace 'the cascade predicts' with 'the model suggests'," but the prediction is a derivation-level result: **decline the edit**. The confident voice is non-negotiable where the derivation exists. Polite but firm.

## What to cite on every claim

Every non-trivial VFD claim in every paper cites **both**:

1. The **LaTeX paper** where the claim is publicly presented (e.g., Paper XXXVI).
2. The **cascade-derivation source** where the first-principles working lives (e.g., `cascade-foundations.md §F5`).

Example citation format:

> *"By F5 of the cascade foundations~\citep{SmartXXXVI} (see cascade-foundations.md §F5 for the working), $F$ is a $\sigma$-intertwiner…"*

## Opening and closing voice for every paper

### Opening paragraph (after abstract)

Every paper opens its Introduction with a paragraph that:

- Names the standard-physics shadow the paper is recovering.
- States the cascade underpinning rung.
- Names the paper's position in the Recovery Manifest.
- Names upstream / downstream papers in the chain.

Template:

> *"This paper recovers [standard-physics result] from the [cascade rung] rung of the VFD cascade. It is Recovery Item [R#] of the Recovery Manifest~\citep{RecoveryManifest}. Upstream: Papers [X, Y] (cascade foundations, prior results). Downstream: Papers [A, B] (extensions). The paper does not replace [standard theory]; it shows how the standard equation emerges as the appropriate-limit projection of cascade closure dynamics."*

### Closing section

Every paper closes with a section titled "Recovery Position" that:

- Restates what standard result was recovered.
- Lists the cascade-derivation source files used.
- Lists what the paper adds (the completion).
- Lists what remains open in the recovery chain.
- References the Recovery Manifest row.

## Forbidden phrases

Never use:

- ❌ "fully derive from first principles" without pointing to cascade-derivation source.
- ❌ "benchmark correspondence" if the cascade-derivation source establishes the result.
- ❌ "not a derivation" for results cascade-masses.md / cascade-mixing.md / cascade-foundations.md actually derive.
- ❌ "structural match only" for results with cascade-structural integer-factor readings.
- ❌ "programme / model-level" for F1–F8 items proven in cascade-foundations.md.

## Preferred phrases

Use:

- ✅ "derived from F[n] of the cascade foundations" for F1–F8 applications.
- ✅ "recovered as the [limit] of cascade [dynamics / geometry]" for standard-physics recovery.
- ✅ "completes standard [QM/SM/GR] by supplying [geometric origin / structural theorem]" for the VFD contribution.
- ✅ "consistent with observation at [X%]" for numerical agreement, with explicit uncertainty.

## Test of every revision

Before committing a revision, ask:

1. Does the paper state the recovery position (which standard-physics result, which cascade rung, which Recovery Manifest item) in its opening?
2. Are all claimed derivations cited to both LaTeX paper and cascade-derivation source?
3. Have any cascade-derivation-established results been demoted under review pressure? (If yes, revert.)
4. Does the closing section restate the recovery and point to the manifest?
5. Are the claims confident where the cascade-derivation source establishes them?

If any answer is "no," revise again before moving on.

---

## Applicability

This protocol applies to every VFD paper, existing or forthcoming. Retroactive revision of existing papers to match the protocol is a programme-maintenance task; forward drafts must adopt the protocol from the first version.

The voice is: **confident about the programme's geometric achievements, humble about open questions, and non-adversarial to existing physics**. This combination is what the programme needs for credibility.
