# Block 2 Status — Search for τ_σ

**Result:** Three progressively wider scans (2A, 2B, 2C) all return **zero**
involutions τ: V_600 → V_600 that produce the closure-cosmogenesis target
structure (2 σ-fixed bulk cycles K=72⊔K=0 + 5 cross-K boundary pairs
K=52↔K=20). Block 2D shows coordinate σ is a transversal (2 fixed per
cycle), not a bulk/boundary discriminator.

## Search history

### Block 2A — 6 standard candidates (`block2_find_tau_sigma.py`)

| candidate | closes on 2I | cycle action | matches target? |
|---|---|---|---|
| quat. conjugation v→v̄  | yes | scrambles cycles (10 verts → 5 cycles) | NO |
| antipodal v→−v          | yes | fixes all 12 cycles                   | NO |
| σ-Galois alone         | NO  | escapes 2I                             | — |
| σ ∘ conj               | NO  | escapes 2I                             | — |
| σ ∘ antipodal          | NO  | escapes 2I                             | — |
| conj ∘ σ               | NO  | escapes 2I                             | — |

### Block 2B — Inner-twist scan (`block2b_inner_automorphism_scan.py`)

For each h ∈ 2I, R ∈ {id, conj, antipodal, σ, σ∘conj, σ∘antipod, conj∘σ}:
- Family A: τ(v) = h R(v) h⁻¹
- Family B: τ(v) = h R(v)
- Family C: τ(v) = R(v) h
- Family D: τ(v) = h R(v) conj(h)

**Result: 0 target hits, 0 near-misses (with both fixed and cross-K pairs).**
Inner automorphisms preserve K-class (they're isometries fixing identity), so
they cannot pair K=52 with K=20. This was theoretical justification for the
null result.

### Block 2C — Exhaustive (h, k) pair scan (`block2c_exhaustive_pair_scan.py`)

Over all 14400 pairs (h, k) ∈ 2I × 2I × 7 outer R:
- 43,200 candidates evaluated
- 2,048 are involutions
- 604 act consistently at the cycle level
- **400 near-misses with structure (4 fixed + 4 cross-K paired + 0 within-K)**
- **0 target hits (2 fixed + 5 cross-K paired)**

**Algebraic explanation of the 4-fixed cap:** for τ(v) = h v k to be an
involution, h² = k² ∈ {±1}. Non-trivial cases require h, k order-4. Order-4
elements in 2I have centraliser of size 4 (the cyclic group ⟨h⟩). The fixed
set of τ has cardinality 4, distributed as 1 vertex per fixed cycle. So the
(h v k)-family CANNOT produce 20-fixed-vertex involutions (= 2 fixed cycles
× 10 vertices). The same algebraic constraint holds for all R-twists.

### Block 2D — 24-cell alignment check (`block2d_24cell_alignment.py`)

Per-cycle distribution of the 24 coordinate-σ-fixed vertices (the 24-cell
embedded in V_600 = 2I) is **uniformly 2 per cycle across all 12 cycles**:

| K-class | # cycles | σ-fixed vertices |
|---|---:|---:|
| K=72 (bulk) | 1 | 2 |
| K=0  (bulk) | 1 | 2 |
| K=52 (boundary) | 5 | 10 |
| K=20 (boundary) | 5 | 10 |

Coordinate σ does **not** identify the bulk. Only **4** of the 24 σ-fixed
vertices lie in bulk cycles; **20** lie in boundary cycles. Conversely
**16** of 20 bulk vertices are σ-mobile (have non-zero √5-content).

**Conclusion:** the doc's claim that "σ-fixed cycles are pointwise σ-fixed"
is **false under coordinate σ**. The doc's σ must refer to a different (so
far un-constructed) involution.

## What we have ruled out

The involution τ_σ that closure-cosmogenesis.md asserts exists is:
1. **Not** any inner automorphism, translation, or two-sided multiplication
   `h R(v) k` for any (h, k) ∈ 2I² and R ∈ {id, conj, antipodal, σ-twists}.
2. **Not** coordinate σ on Q(√5) — that map is a uniform transversal, not
   a bulk/boundary discriminator.
3. **Not** any vertex map with fixed set ≤ 4 (the 4-fixed cap is
   structural for the (h v k) family).

## What remains on the table

1. **H₄ reflections through axes outside 2I.** H₄ has 14400 elements, 60
   reflections. A reflection of the form r(v) = v − 2⟨v, n⟩ n for n NOT
   in 2I closes on V_600 iff the reflection happens to permute 2I. Some do.
   Each such reflection has 30 fixed vertices (the equatorial 3-sphere
   intersection), close to 20 but not equal. **2-3 days of rep theory.**

2. **Vertex maps not of bilinear form.** A general involution V_600 → V_600
   need not factor as `h R(v) k`. A direct combinatorial search — for each
   pair of cycles (one K=52, one K=20), pick a T_τ-equivariant bijection
   (10 choices) — gives 10⁵ ≈ 100K candidate boundary actions; combined
   with bulk-cycle fixings, ~10⁶ candidate involutions, all enumerable.
   **1 day of code, but no algebraic story unless one matches a known
   geometric operation.**

3. **The Elkies E₈ embedding.** σ on E₈ acts on V_600 cycles via the
   composition with the E₈ → V_600 projection (240→120). The σ-involution
   on E₈ might induce the right action on cycles. **1+ week of E₈ code.**

4. **Doc reformulation.** Drop the "pointwise σ-fixed" claim. Define bulk
   purely by K-class (K=72 ∪ K=0). Boundary is K=52 ∪ K=20 with K-pairing
   asserted as additive (K(C) + K(C') = 72 for σ-paired cycles), without
   asserting an explicit involution. This makes the closure-cosmogenesis
   theorems honest — they hold for ANY K-additive partition, with the
   specific σ-pairing left as Conjecture C-σ. **Hours of doc edits.**

## Recommended next move

Option (4) is the only one that closes OD-1 *cleanly* in a publishable
window without depending on a hard E₈/H₄ representation theory result.

**Concrete plan for option (4):**
- Edit `docs/closure-cosmogenesis.md` Lemma 2.3: replace "σ-fixed cycles
  are pointwise σ-fixed" with "Bulk cycles are characterised by K(C) ∈
  {72, 0}; we conjecture (Conjecture 2.4) the existence of an involution
  τ_σ on V_600 that fixes all bulk vertices pointwise and pairs boundary
  vertices in cross-K pairs."
- Add Conjecture 2.4 with explicit content.
- Cite this BLOCK2_STATUS.md as the search log establishing that τ_σ is
  not a bilinear quaternion map.
- Update derivation chains that depended on Lemma 2.3 to use K-class
  bulk/boundary partition instead.

This converts a hidden derivation gap into a named conjecture, which is
publishable without false certainty.

## Hold on the BH sequencing

Step 2 (BH localised collapse) and Step 3 (Bekenstein 1/4) depended on
closing OD-1 via the τ_σ identification. Under option (4), they remain
predicated on Conjecture 2.4 but can be developed in parallel as
*conditional* derivations.

The empirical 1/12 phenomenology is unaffected — the data fits and ladder
predictions remain valid as standalone results.
