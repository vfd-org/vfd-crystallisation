# Changelog

## [1.0.0-rc1] — 2026-05-29 — **SUPERSEDED / WITHDRAWN (see 2.0.0-rc1 below)**

Initial public release. The equivalence claims described in this entry
were withdrawn in v2 after adversarial review; this entry is retained as
a historical record only.

### Paper

**Title:** *RH as Witness Resonance: A substrate-side equivalence
of the Riemann Hypothesis.*

**Main result:** Theorem 2 (Witness Resonance Theorem) proves that
RH is equivalent to substrate spectral completeness on V₆₀₀'s
τ-fixed block.

**Sections:**

- §1 Introduction: why RH is the final reframe
- §2 The substrate framework (brief)
- §3 The Witness Resonance Theorem
  - §3.1 Spectral generator + witness axis
  - §3.2 Main theorem with proof sketch
  - §3.3 The substrate-side equivalence statement
  - §3.4 Extension to L(s, χ_5) on τ-paired block
  - §3.5 Corollaries
- §4 What the reframe accomplishes and what remains open
- §5 Conclusion

### Key reformulation

RH is recast as: "the witness invariant W = V_min on V₆₀₀ admits
a substrate-localised spectral generator T_W whose excited
spectrum equals {γ_n}". This is finite-dimensional algebraic
content; whether it holds is the open question, equivalent to RH.

### Scope discipline

- Pre-peer-review preprint footer enforced.
- No claim of RH settlement.
- Proof sketches transparent: (b) ⇒ (a) assumes Hilbert–Pólya
  construction under RH; (a) ⇒ (b) requires bijectivity of the
  substrate critical-line embedding.
- Explicit "what remains open" section names three concrete open
  questions.

## [2.0.0-rc1] — 2026-06-12

Reframe after adversarial review. **The v1 equivalence claim is withdrawn.**

### What review found (and v2 fixes)

- The (b) ⇒ (a) direction of the v1 "theorem" assumed its own conclusion
  ("we assume here that under RH, the substrate-localised construction can
  be carried out"). Withdrawn; v2 keeps only the classical direction
  (operator ⇒ RH) as a Proposition, with no novelty claimed for it.
- Clause (c) was definitional, not an equivalence. Now stated as
  terminology only.
- The τ-fixed block is 94-dimensional; a finite space cannot carry the
  infinite spectrum {γ_n}. v2 defines a substrate lift (infinite-dimensional,
  anchored to the block) and is explicit that no lift is constructed.
- "Witness resonance" / "resonance depth set" vocabulary removed
  ("resonance depth set" = the positive spectrum; now called that).
- Title changed to "A Conditional Substrate Localisation of the
  Hilbert–Pólya Problem". Theorem renamed; GRH(χ₅) proposition demoted to a
  conjectural target; corollaries demoted to conditional remarks.
- README/CHANGELOG overclaims removed; provenance note added (this bundle
  contains no simulations; all structural counts are imported from cited
  sibling artifacts). Empty sims/ directory removed.

### What v2 contributes

A specification: the substrate constraint list (ground state at V_min,
closure-flow and Hecke commutation on a lift) localising where a
Hilbert–Pólya operator for ζ would have to live, plus the one classical
implication. A constraint list and a target — not an equivalence, not a
reformulation of RH.
