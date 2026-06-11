# Unblock Plan for OD-1 / Candidate 4

**Goal:** identify the involution τ_σ: V_600 → V_600 that produces the
2-fixed + 5-paired cycle structure asserted by closure-cosmogenesis.

The empirical 1/12 result rests on this structure. Without τ_σ, the
derivation chain stays open.

## What's needed (in dependency order)

### Block 1 — K-class of each T_τ cycle (CHEAP — 30 min)

**Status:** Tractable now.
**Inputs available:** `build_vertices()`, T_τ permutation, vertex shells from
graph distance.
**Deliverable:** explicit K(C) for each of the 12 cycles. Confirm the
{72:1, 0:1, 52:5, 20:5} multiset asserted in `docs/closure-cosmogenesis.md`.
**Why it unblocks:** identifies which 2 cycles are bulk, which 10 are boundary,
giving the target set for τ_σ.

### Block 2 — Find candidate internal involution R (MEDIUM — 1-2 days)

**Status:** Tractable but exploratory.
**Inputs needed:** Block 1 output.
**What to try (each as `R ∘ σ` and test if it gives 5 transpositions on 10
boundary cycles):**
- `R = quaternion conjugation v → v̄` (preserves 2I, has order 2)
- `R = central inversion v → −v` (preserves 2I, equals T_τ⁵)
- `R = left-multiplication by τ²` or `τ⁵`
- `R = an H₄ reflection through a specific hyperplane` (e.g., one preserving
  the K-class)
- Iterate over all order-2 elements of 2I (there's only one: −1, but inner
  automorphisms by 2I elements give a richer family)
**Deliverable:** explicit τ_σ definition or proof none of these candidates work.
**Why it unblocks:** without τ_σ, no σ-antisym pair-mode space is well-defined.

### Block 3 — H₄ representation content of the τ_σ-antisym module (HARD — 1 week)

**Status:** Specialist computation.
**Inputs needed:** Blocks 1 + 2.
**What's needed:**
- Build the 14400-element H₄ Coxeter group as a permutation representation
  on V_600's 120 vertices.
- Build the 5-dim τ_σ-antisymmetric pair-mode subspace.
- Decompose this 5-dim H₄-module into irreducibles.
- Check if exactly one 1-dim component (trivial or sign) appears.
**Deliverable:** explicit irreducible decomposition.
**Why it unblocks:** if `5-dim ≅ V_sign ⊕ V_4` (or `V_trivial ⊕ V_4`), OD-1
closes — exactly 1 mode survives 1-dim projection, giving 12 + 1 = 13 live
modes → 13/12 ratio.

### Block 4 — Apply same projection to localised collapse (Step 2 of BH plan)

**Status:** Predicated on Blocks 1-3.
**What's needed:** restrict the H₄ projection rule to a localised subset of
V_600 (analog of a black hole's neighbourhood). Verify the same trivial-or-sign
projection gives a singleton anchor (BH no-hair analog).

### Block 5 — Bekenstein 1/4 coefficient check (Step 3 of BH plan)

**Status:** Predicated on Blocks 1-4.
**What's needed:** count surviving modes per "horizon area" (number of σ-paired
cycles enclosed) and compare to Bekenstein-Hawking S = A/(4ℏG).

## Critical-path summary

```
Block 1 (cheap) → Block 2 (medium) → Block 3 (hard) → OD-1 closed
                                                    └→ Block 4 → Block 5 (BH)
```

Block 1 is doable in this session. If Block 1's K-class structure matches
closure-cosmogenesis's {72:1, 0:1, 52:5, 20:5}, the framework's K-class
claim is verified and we have the bulk/boundary cycle assignment in hand.
That doesn't close OD-1, but it's a load-bearing prerequisite.

## What this does NOT need

- No new experimental data.
- No further consultation with the framework's other docs (the math is
  self-contained once τ_σ is identified).
- No Hodge / E₈-extension machinery for Block 1.
