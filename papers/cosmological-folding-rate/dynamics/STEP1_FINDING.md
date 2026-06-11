# Step 1 — H₄ Rep Theory of σ-Antisymmetric Module

**Status:** Did not close. Found a definitional ambiguity that has to be
resolved before the H₄ rep computation can run.

## What we tried

Compute the H₄-rep decomposition of the 5-dim σ-antisymmetric cycle-pair-mode
space, in the hope that it equals `V_sign ⊕ V_4` (giving 1 surviving 1-dim
mode → 13/12).

## What we found

V_600 has full H₄-Laplacian spectral decomposition:

```
ℝ^120 ≅ V_1 ⊕ 2·V_4 ⊕ 2·V_9 ⊕ 2·V_16 ⊕ V_25 ⊕ V_36
                     1 + 4·2 + 9·2 + 16·2 + 25 + 36 = 120 ✓
```

V_1 trivial rep is the constant function — σ-fixed by construction. So
the σ-antisymmetric module *cannot* contain a V_1 component.

## The blocking issue

Naïve Galois σ on Q(√5) coordinates **does NOT preserve V_600**:

```
build_vertices() → 120 unit icosians
σ-fixed (σ(v) = v):        24 vertices
σ ↦ ∈ V_600:               24 vertices  (= σ-fixed only)
σ ↦ ∉ V_600:               96 vertices
```

So the Galois σ maps 96 of 120 V_600 vertices *outside* the standard 2I
embedding. (It maps them to a σ-conjugate copy 2I' which is a *different*
maximal order in the icosian ring.)

Meanwhile, `closure-cosmogenesis.md` claims a 20/100 split via "σ-Galois
involution partitioning the 12 cycles." But:

- 20 ≠ 24 (Galois σ-fixed count)
- 100 ≠ 96 (Galois σ-non-fixed count)
- The 20/100 split comes from **K-class structure** (K=72⊔K=0 = bulk),
  not from Galois σ directly.

So **the σ in closure-cosmogenesis is NOT the Q(√5) Galois conjugation**.
It must be a different involution.

## Candidate involutions for the closure-cosmogenesis σ

1. **K-class reflection.** σ might be the involution that pairs the K=52
   cycles among themselves and K=20 cycles among themselves. With odd
   counts (5 each), this can't pair cleanly into 2-orbits — there must be
   self-paired cycles, contradicting the doc's claim.

2. **K=52 ↔ K=20 swap.** σ could swap K=52 ↔ K=20, giving 5 σ-pairs
   across K-classes. This pairs 10 cycles into 5 pairs cleanly. But it's
   not clearly "Galois."

3. **A specific H₄ reflection.** σ could be a generator of an H₄ subgroup
   (like the central inversion or a face-reflection) that happens to
   produce the 20/100 split. The "Galois" name might be a structural
   analogy not a definitional identity.

4. **σ on extended substrate.** σ-Galois might naturally act on the
   E₈-extended object V_600 ∪ σV_600 (≈ E₈ roots) where it does close.
   The bulk = E₈-trivial-rep part, boundary = E₈-nontrivial part. This
   would explain the K-class numbers via E₈ structure.

## What this means

**For the 1/12 phenomenology**: unchanged. The empirical fits stand —
H₀ at 0.06σ, S₈ at 0.14σ, etc. These don't depend on the derivation.

**For the derivation**: blocked at an earlier step than OD-1. Before we
can compute the H₄ rep content of σ-antisym modes, we must first **define
σ properly** so it preserves V_600 and gives the 20/100 split.

The cleanest path:
1. Read the explicit cycle decomposition produced by
   `papers/cascade-derivation/scripts/derive_pentagonal_clock_*.py` and
   identify the σ-action on cycles directly from those scripts.
2. With that σ in hand, redo the H₄ rep computation.
3. Then return to the original Step 1 plan.

## Implication for the BH sequencing

The BH plan (Steps 1 → 2 → 3) is **paused at Step 1** until the σ
definition is unambiguous. Steps 2 and 3 are predicated on Step 1
closing, so they can't be attempted yet.

This is honest research progress — finding the definitional ambiguity
NOW (rather than after writing a paper that asserts the bulk/boundary
decomposition is "Galois-σ-induced") is exactly what the credibility-bar
discipline requires.

## Possible upside

If candidate 4 holds (σ is naturally defined on the E₈-extended substrate),
then the cosmological 1/12 effect, the H_4 rep content, and the BH
information-encoding question all live on the *same* E₈ object. That
would be a unification — but it's speculative until the σ-action is
nailed down.

## Recommendation

Either:
(a) Pause OD-1 derivation work until someone clarifies σ in the cascade
    derivation scripts. The empirical 1/12 result can be reported as
    *phenomenologically robust, derivation pending* without overclaiming.
(b) Attempt to reconstruct σ ourselves by reading the K-class assignment
    code and reverse-engineering the involution that gives the 20/100
    split.

(b) is more work but informative. (a) lets us move on to other testable
predictions without blocking on this.
