# Block 3 Status — E₈ extension and τ_σ

**Result:** the σ-pairing structure of closure-cosmogenesis is **canonical
at the COSET level** (Dic_5-coset structure of 2I), but a **vertex-level
involution τ_σ realising the structure does not exist as any quaternion-
isometric map**, including:

- All 4D quaternion-bilinear maps `h v k` for h, k ∈ 2I (Block 2C).
- All 4D coordinate transpositions composed with σ-Galois (Block 3b).
- Any reflection through a 3D hyperplane in R⁴ (Dic_5 spans R⁴, so no
  hyperplane contains it pointwise).

## Structural picture (now clear)

### What σ does geometrically

σ-Galois acts on the icosian ring I componentwise (a + b√5 → a − b√5).
On V_600 = 2I (even-permutation 600-cell), σ acts as:

- 24 vertices (the 24-cell ⊂ 2I) are σ-fixed.
- 96 vertices map to the **odd-permutation 600-cell** = a different
  600-cell in the SAME R⁴, sharing only the 24-cell with V_600.

So σ takes V_600 → V_600 ∪ (odd-perm 600-cell). The "Elkies E₈ = 2I ⊕
σ(2I)" decomposition refers to the union of these two enantiomeric
600-cells (with 24 shared vertices), totalling 216 elements; a full
unimodular E₈ rank-8 lattice requires gluing in 24 more elements.

### What Dic_5 does

Bulk = K=72 ∪ K=0 cycles = 20 vertices is a SUBGROUP of 2I, specifically
the **binary dihedral group Dic_5 = ⟨τ, c'⟩** where c' is the order-4
generator with c'² = -1 = τ⁵. Index [2I : Dic_5] = 6.

The 5 non-trivial **left cosets** of Dic_5 in 2I each contain exactly
one K=52 cycle and one K=20 cycle, giving the 5 K-class pairs that
closure-cosmogenesis calls the "σ-paired boundary."

This is canonical: it follows from Dic_5 ⊂ 2I, with no need for σ.

### Why no vertex-level τ_σ exists in 4D

For τ_σ to fix Dic_5 pointwise as an isometry of R⁴, the 20 Dic_5
vertices must lie in a 3-dim hyperplane of R⁴ (the reflection plane).
But Dic_5 contains both ⟨τ⟩ (in a 2-dim plane) and c'·⟨τ⟩ (in an
orthogonal 2-dim plane), so it spans the full R⁴. Hence:

> **Theorem (4D obstruction)**: No Euclidean isometry of R⁴ fixes Dic_5
> pointwise except the identity.

So τ_σ as a 4D vertex map cannot be an isometry. The exhaustive (h, k)
scan in Block 2C confirms this empirically: 0 hits among 14400 candidates.

### What COULD give τ_σ (8D / non-isometric routes)

1. **8D Weyl reflection in W(E₈)** through a hyperplane that contains
   Dic_5 ⊂ 2I (4-dim subspace of R⁸) and is orthogonal to a specific
   E₈-root in σ(2I). Building the full E₈ unimodular lattice in icosian
   form is non-trivial — Block 3a found that Z⟨2I⟩ has discriminant
   625/256 (not E₈'s 1), so naive icosian Z-spans are sub-lattices.

2. **Non-isometric combinatorial swap**: a vertex permutation that
   fixes Dic_5 pointwise and swaps K=52/K=20 cycles within each
   non-trivial Dic_5-coset. The space of such involutions is (10!)^5
   per cycle-pairing assignment ≈ 10^32 — needs additional
   constraints (e.g., cycle-equivariance with some structure).

3. **σ-pairing as coset-level only**: drop the vertex-level τ_σ
   requirement entirely. The bulk/boundary structure and 5-pair
   structure are well-defined at the coset level. Closure-cosmogenesis
   theorems hold under this weaker reformulation.

## Recommended path: option 3 (cleanest, publishable now)

The closure-cosmogenesis doc currently asserts (Lemma 2.3) that "σ-fixed
cycles are pointwise σ-fixed." Under coordinate σ this is empirically
false (only 4 of 20 bulk vertices are coord-σ-fixed; the 24-cell sits
across all 12 cycles uniformly).

**Reformulation:** replace "σ-fixed cycles are pointwise σ-fixed" with:

> **Definition (Bulk).** The bulk 𝓑 ⊂ V_600 is the binary dihedral
> subgroup Dic_5 ⊂ 2I, equivalently the union of the K=72 and K=0
> cycles. The boundary ∂ = V_600 \ 𝓑 is the union of the 5 non-trivial
> Dic_5-cosets, each consisting of one K=52 and one K=20 cycle.
>
> **σ-pairing.** Two boundary cycles C, C' are σ-paired iff they belong
> to the same Dic_5-coset, equivalently iff K(C) + K(C') = 72 with
> {K(C), K(C')} = {52, 20}.

With this definition, all closure-cosmogenesis theorems (3.2 existence
of F_0, 4.4 bootstrap, 5.2 bulk invariance, 5.4 boundary refinement)
go through using Dic_5 explicitly. The vertex-level τ_σ becomes
**Conjecture C-σ**: there exists an involution τ_σ : V_600 → V_600
that fixes 𝓑 pointwise and swaps the K=52 and K=20 cycles within each
non-trivial Dic_5-coset.

Conjecture C-σ may be empirically false (4D obstruction) or require
the 8D E₈ extension; either way, it's no longer load-bearing for the
dynamics layer.

## What's been definitively established (Blocks 1, 2A-E, 3a-b)

- ✓ K-multiset {72:1, 0:1, 52:5, 20:5} verified (Block 1).
- ✓ Bulk 𝓑 = Dic_5 ⊂ 2I (Block 2E).
- ✓ 5 K-class boundary pairs = 5 non-trivial Dic_5-cosets (Block 2E).
- ✓ τ_σ ∉ W(H₄) (Block 2C exhaustive 43,200 candidates).
- ✓ τ_σ ≠ P∘σ for P a 4D reflection/transposition (Block 3b).
- ✓ τ_σ cannot be an R⁴ isometry fixing 𝓑 (Dic_5 spans R⁴).
- ✓ σ takes V_600 to odd-perm 600-cell, sharing 24-cell only.

## Files

- `block1_kclass.py` — Block 1, K-multiset verified.
- `block2_find_tau_sigma.py` / `block2b_*` / `block2c_*` — exhaust W(H₄).
- `block2d_24cell_alignment.py` — coord-σ doesn't identify bulk.
- `block2e_bulk_subgroup_check.py` — bulk = Dic_5 confirmed.
- `block3a_e8_icosian_lattice.py` — naive icosian Z-span has det 625/256
  (not E₈ unimodular).
- `block3b_parity_flip_tau_sigma.py` — P∘σ scan, no target hit.
