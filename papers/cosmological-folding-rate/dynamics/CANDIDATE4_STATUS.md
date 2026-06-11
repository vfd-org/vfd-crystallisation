# Candidate 4 Verification — Honest Status

**Date:** 2026-05-05
**Verdict:** **Partially confirmed at the structural level, blocked at
the cycle-pairing level.**

## Confirmed

1. **σ-intertwining is real** (per `docs/glossary.md`, Paper XXXVI F5):
   "Galois twist √5 ↦ −√5 on Z[φ] extends to an automorphism of E₈ that
   swaps two conjugate H₄ copies."

2. **Existing pentagonal-clock script B7-B8 EXPLICITLY confirms** σ does
   not preserve 2I, and the natural setting is `E₈ = 2I ⊕ σ(2I)`:
   ```
   "σ is the algebraic Galois involution on Q(√5), but it does not act
    geometrically on a single 2I. Under the Elkies E₈ ← 2I ⊕ σ(2I)
    decomposition (Paper XXII), σ is the map from one 600-cell to the
    other."
   ```

3. **Numerical fact** (this work): of 120 V_600 vertices, exactly **24
   are σ-fixed** (rational icosians), distributed uniformly **2 per cycle**
   across all 12 T_τ cycles.

## Blocked

The closure-cosmogenesis statement of "2 σ-fixed cycles + 5 σ-paired
pairs" does NOT follow from coordinate-Galois σ alone:

- **Every T_τ cycle is mixed** (2 σ-fixed + 8 σ-mobile vertices).
- No cycle is "entirely σ-fixed."
- The 20/100 bulk/boundary split is therefore **NOT the σ-fixed/σ-mobile
  vertex split** (which is 24/96).
- The 20/100 split is **geometric, from K-class** (K=72, K=0 cycles =
  bulk; K=52, K=20 cycles = boundary).

For the "5 σ-paired cycle pairs" to make sense, σ would need to act on
the 10 boundary cycles giving a permutation with 5 transpositions. But
on individual cycles, σ maps each to its image in σ(2I), giving 12
distinct σ-images, not a 5-fold pairing within the 10-cycle set.

So **a missing involution** is needed to combine with σ-Galois to
produce the 5-pair structure. Candidates:

- σ ∘ (quaternion conjugation v → v̄): conj preserves 2I, σ doesn't,
  composition might be an internal involution.
- σ ∘ (left-multiplication by some element h ∈ 2I).
- A K-class-respecting involution that pairs K=52 with K=20 cycles.

## What this means for the BH sequencing

**Step 1 (H₄ rep of σ-antisym):** Cannot proceed cleanly until the
cycle-pairing involution is identified.

**Steps 2–3 (BH analog, Bekenstein 1/4):** Predicated on Step 1; paused.

**Empirical 1/12 results:** Unchanged. The H₀ + S₈ fits don't depend
on the derivation. Pre-registered ladder predictions stand.

## What WOULD close Candidate 4

A clean derivation chain would require:

1. Specify the involution τ_σ: V_600 → V_600 that combines coordinate σ
   with an internal 2I operation.
2. Show τ_σ pairs the 10 boundary cycles into 5 transpositions.
3. Show τ_σ fixes the 2 bulk cycles (K=72, K=0).
4. Compute the 5-dim τ_σ-antisymmetric pair-mode space and decompose
   under H₄.
5. If the H₄ decomposition contains exactly 1 trivial-or-sign-rep
   component, OD-1 closes.

This is roughly a 1–2 week dive into icosian arithmetic + H₄
representation theory, with no guaranteed payoff if step 1 fails to
find a τ_σ that respects K-class.

## Honest recommendation

The empirical 1/12 cosmological result is publishable as **phenomenology**
right now: the data fits are robust, the structural numbers match V_600,
and the pre-registered ladder predictions for SPHEREx/LSST/SKA are
falsifiable. The derivation chain to E₈ + Bekenstein-1/4 is a research
programme, not a closed result — and the right move is to ship the
phenomenology as the load-bearing claim, with the derivation as
"OD-1' open: pending icosian arithmetic clarification."

## Programme-level value

Even though Candidate 4 didn't close cleanly, the work uncovered:

- A previously unstated definitional ambiguity: closure-cosmogenesis's
  "σ" is not coordinate-Galois on V_600 but the σ-intertwining on the
  E₈ extension.
- A specific missing operator: τ_σ on V_600 producing the 5-pair structure.
- The fact that the bulk/boundary distinction is K-class-geometric, not
  σ-direct (which slightly reframes how the framework is described).

These are real findings even though they fall short of the BH derivation.
