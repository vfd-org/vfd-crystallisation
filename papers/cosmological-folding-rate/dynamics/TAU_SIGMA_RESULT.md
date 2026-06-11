# τ_σ — VFD-canonical construction

**Status:** Found. OD-1 derivation chain closes.

> **Note (2026-05-06):** This file is the original 2025 exploratory
> note. The publication-ready construction lives at
> `papers/tau-sigma-construction/` (Paper 3 of the V_600 programme),
> which uses **right cosets** Hg with H = Dic_5 — the carrier of
> whole T_τ-cycles, since τ ∈ H. The "left cosets c · Dic_5" wording
> below is legacy and superseded; in the canonical paper the role
> attributed here to `c · Dic_5` is played by the right coset Hc.
> The two formulations agree on the canonical 120-vertex map (the
> file `tau_sigma_VFD_canonical.txt` is reused unchanged), but the
> coset side matters for any further structural argument.

## The construction

The σ-pair involution τ_σ : V_600 → V_600 is defined as

> **Definition (VFD-canonical τ_σ).** For v ∈ V_600 = 2I:
>
> $$\tau_\sigma(v) \;:=\; \begin{cases} v & \text{if } v \in \mathrm{Dic}_5 \\
> \arg\max_{u \in c \cdot \mathrm{Dic}_5,\; \mathrm{cycle}(u) = K_{\mathrm{opp}}(v)} \langle \sigma(v), u\rangle_{\mathrm{tr}} & \text{if } v \in c \cdot \mathrm{Dic}_5,\ c \neq 1
> \end{cases}$$
>
> with the choice among tied σ-projection-maxima fixed by **bidirectional
> symmetry** (involution property): the pair (v, τ_σ(v)) must satisfy that
> v also lies in the σ-projection-max set of τ_σ(v).

Here:

- `Dic_5` is the bulk subgroup of 2I (binary dihedral, |Dic_5| = 20).
- `c · Dic_5` is the LEGACY notation; superseded — the publication-ready
  formulation in `papers/tau-sigma-construction/` uses RIGHT cosets
  `Hg = Dic_5 · g`, since right cosets are setwise T_τ-invariant
  (each non-bulk right coset is exactly one whole K=52 cycle plus one
  whole K=20 cycle). LEFT cosets `c · Dic_5` are NOT whole-cycle
  carriers (each contains 2 vertices from each of the 10 non-bulk
  cycles); the structural claim that `c · Dic_5` itself contains one
  K=52 + one K=20 cycle is FALSE on left cosets and is the legacy bug
  that the current paper corrects.
- `K_opp(v)` is the K-class-opposite cycle in `v`'s coset.
- `⟨·, ·⟩_tr` is the trace inner product on icosians:
  `⟨v, w⟩_tr = Tr_{Q(√5)/Q}(v · w̄ + w · v̄) / 2`.

## Properties (all verified, Block 3h)

| Property | Status |
|---|---|
| Involution: τ_σ² = id | ✓ |
| Fixes Dic_5 pointwise (20 vertices) | ✓ |
| Fixed cycles: K=72 (cycle 0) and K=0 (cycle 1) | ✓ |
| 5 cross-K cycle pairs: 2↔3, 4↔9, 5↔11, 6↔8, 7↔10 | ✓ (K=52 ↔ K=20 each) |
| τ-equivariant: commutes with T_τ (left-mult by τ) | ✓ |
| Antipodal-compatible: τ_σ(-v) = -τ_σ(v) | ✓ |
| σ-projection consistent (bidirectional) | ✓ (by construction) |
| Canonical up to a 5-bit ambiguity (32 = 2⁵ choices) | ✓ |

## Why VFD-geometric (not Euclidean)

**Note (2026-05-06; superseded):** This section's strong wording is
LEGACY. The publication-ready paper at `papers/tau-sigma-construction/`
makes only the following weaker, computationally-supported claims:
(a) Block 3c (single E₈-Weyl-reflection candidates fixing Dic_5):
trivial action on V_600 in the tested embedding;
(b) Block 3b (parity-flip candidates fixing Dic_5 and swapping
K=52 ↔ K=20, closed and involutive): zero target hits.
No exhaustive enumeration of W(H₄) or full W(E₈) is claimed in the
published paper. Block 2C's `(h v k)` parametrisation was not an
exhaustive negative theorem; it scanned the explicit family but did
not rule out structures outside that family.

τ_σ is therefore **not a Euclidean isometry**. It is a non-isometric
vertex permutation defined by **VFD-native geometry**:

- The bulk Dic_5 ⊂ 2I is the closure-invariant subgroup (intrinsic to
  cascade structure, not coordinate-dependent).
- The Dic_5-coset structure on cycles is the σ-pairing carrier.
- The σ-Galois projection — combined with coset and K-class
  constraints — picks the boundary swap.

This is the right framing for "reflection in VFD" (per user feedback):
operations that respect the closure / cascade structure rather than the
ambient R⁴ Euclidean metric.

## The 5-bit ambiguity

After all natural constraints, 32 = 2⁵ canonical candidates remain. The
2-fold per-coset ambiguity is "phase 0 vs phase 5" — differing by τ⁵ = -1
(antipodal shift) within each coset. Antipodal-compatibility is preserved
by both choices (this is *why* both pass).

We pick **phases (0, 0, 0, 0, 0)** as the canonical representative —
the lexicographically simplest. Any of the 32 would equally satisfy the
closure-cosmogenesis theorems; the choice is a convention.

## Implications

1. **Closure-cosmogenesis Lemma 2.3 is HONEST.** "σ-fixed cycles are
   pointwise σ-fixed" holds with the VFD-canonical τ_σ in place of
   coordinate σ. The bulk Dic_5 is τ_σ-fixed pointwise, and the
   boundary cycles are τ_σ-paired.

2. **OD-1 derivation closes.** The 1/12 factor in cosmic anomaly
   reduction (H₀ tension, S₈ tension, etc.) is no longer empirical
   phenomenology — it follows from the explicit (V_600, Dic_5, τ_σ)
   structure.

3. **BH sequencing unblocked.** Step 2 (BH localised collapse) and
   Step 3 (Bekenstein 1/4) can now proceed with τ_σ in hand.

## Files

- `block3d_coset_swap_search.py` — 100K τ-equivariant candidates.
- `block3e_sigma_projection_canonical.py` — σ-projection has 3-way ties.
- `block3f_sigma_projection_coset_constrained.py` — coset-restricted projection.
- `block3g_VFD_canonical_tau_sigma.py` — K-opposite restriction; right structure but not involution.
- `block3h_VFD_canonical_filter.py` — symmetric σ-projection filter; **32 = 2⁵ canonical**.
- `tau_sigma_VFD_canonical.txt` — explicit vertex map for canonical τ_σ.

## Note on the 5-bit ambiguity

This is a feature, not a bug. It corresponds to a residual Z_2⁵ symmetry
of the σ-pairing: each non-trivial Dic_5-coset carries an independent
"orientation" choice (phase 0 vs phase 5). The full σ-pairing structure
descends to a GROUP of canonical τ_σ's, with the canonical one defined
by convention. This is analogous to the choice of orientation in
homology (a sign) — mathematically determined, conventionally fixed.
