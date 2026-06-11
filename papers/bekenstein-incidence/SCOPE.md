# Bekenstein 1/4 from V_600 incidence — paper scope

**Working title:** *The Bekenstein–Hawking 1/4 coefficient as exact incidence on the 600-cell.*

**One-sentence pitch:** The 1/4 in S = A/(4ℓ_P²) is the rational identity 4/16 — the count of coordinate-σ-fixed vertices per left coset of Dic_5 ⊂ 2I, divided by the count of σ-mobile vertices in the same coset. No fitting, no continuum approximation, no free parameters.

## Why this paper, why now

The 1/4 coefficient is the cleanest, narrowest, most undismissable result we have. It is:

- **Pure arithmetic.** 4/16 = 1/4. Anyone with a group-theory package can verify it in 30 lines.
- **Parameter-free.** No tunables, no choices, no priors.
- **Independent of cosmology, ΛCDM, Hawking continuum.** Stands alone.
- **Pre-existing literature anchor.** Mainstream cares about deriving 1/4 from microscopics — string theory and LQG each have their own derivations and reviewers know the genre.

A standalone paper here is the right lead artifact: small claim, complete proof, no rhetorical leverage required.

## What's IN scope

1. **Setup.** Binary icosahedral group 2I = V_600 ⊂ unit icosian quaternions. The σ-Galois twist (√5 ↦ -√5). The 24-cell as the σ-fixed sublattice of V_600.
2. **Bulk subgroup.** Identification Dic_5 ⊂ 2I (binary dihedral, order 20) as a distinguished index-six binary dihedral subgroup produced by the T_τ-cycle bulk/boundary partition (already proved in Block 2E). Dic_5 is *not* normal in 2I; we use both left- and right-coset enumeration explicitly.
3. **Coset incidence theorem.** *For every left coset gDic_5 and every right coset Dic_5 g of Dic_5 in 2I, the intersection with V_24 has exactly 4 vertices; hence each coset has 4 σ-fixed and 16 σ-mobile vertices.* No normality assumption is used.
4. **The 4/16 identity.** Per non-trivial coset: 4 σ-fixed + 16 σ-mobile = 20.
5. **Interpretation as entropy/area.** σ-fixed = "twin-anchored" information bits (entropy). σ-mobile = "dynamical" horizon channels (area). S/A = 4/16 = 1/4.
6. **Match to standard Bekenstein–Hawking.** S/A invariant under unit choice; the 1/4 is the structural ratio that fixes the Bekenstein coefficient regardless of the (cascade-unit ↔ Planck-unit) calibration.
7. **Scope statement (load-bearing, marked clearly).** The structural ratio is exact and unconditional. The numerical match to T_H = ℏc³/(8πGM) requires a frame-resolution↔horizon-radius calibration that is **not** in this paper.

## What's explicitly OUT of scope

- **All cosmology.** No H(z), no σ_8, no CMB, no ΛCDM. (Those go to a separate paper.)
- **Hawking radiation continuum.** The single-quantum Hawking result stays out — it's a separate question and adds dismissable surface.
- **Quantum gravity claims.** No "we have a theory of QG." The paper claims one ratio.
- **τ_σ involution construction.** Not needed for the 1/4 result. Cite for context only.
- **Cascade-cosmogenesis machinery.** Not needed. Cite as context.
- **Any claim that V_600 is THE substrate of physical BHs.** The paper claims a structural identity, not an ontology.

## Section structure (target ~12-15 pages)

1. **Introduction** (1.5pp). Bekenstein 1/4 history, why microscopic derivations matter, what this paper does (one identity).
2. **The 600-cell and its bulk subgroup** (2pp). 2I, T_τ-cycles, K-multiset, Dic_5 as bulk. Cite Block 2E proof.
3. **The σ-Galois twist and the 24-cell** (1.5pp). σ on icosians, V₂₄ as σ-fixed sublattice, classical fact 24-cell ⊂ 600-cell.
4. **Main theorem** (2pp). Per-coset incidence = 4 σ-fixed + 16 σ-mobile = 20. Proof by exact Q(√5) finite enumeration plus a Dic_5 generator/presentation certificate; cardinalities alone do not imply uniform incidence.
5. **Interpretation** (2pp). 4 = entropy bits, 16 = horizon area channels, S/A = 1/4. Match to standard formula.
6. **Scope and what is NOT claimed** (1pp). Load-bearing honest section. Calibration is open; ontology is open; the *ratio* is what's derived.
7. **Falsifiable corollaries** (1pp). PBH evaporation cutoff if discrete spectrum extends here. (Brief — keep teeth out unless they sharpen the case.)
8. **Comparison to existing microscopic derivations** (1.5pp). String theory (Strominger–Vafa), LQG (Ashtekar–Lewandowski). Note: no claim of superiority, just methodological complementarity (rational identity vs. partition function vs. spin-network counting).
9. **Conclusion** (0.5pp).
10. **Appendix.** Computational verification script (the existing `bh_bekenstein_1_4.py`).

## The undismissable spine

The paper must survive the abstract-level reject test. The abstract should read like:

> We prove that for every left coset of the binary dihedral subgroup Dic_5 ⊂ 2I in the binary icosahedral group of order 120, the intersection with the σ-Galois-fixed 24-cell consists of exactly 4 vertices, and the complement (σ-mobile vertices) has exactly 16. The ratio 4/16 = 1/4 is the structural source of the Bekenstein–Hawking entropy coefficient when σ-fixed vertices are interpreted as anchor-state bits and σ-mobile vertices as horizon channels. The result is parameter-free and follows from finite-group arithmetic alone.

A reviewer reading that does not see "we solved quantum gravity." They see "here is a finite-group fact, here is its interpretation, decide for yourself." That's the bar.

## Risk register

| Hook | Mitigation |
|---|---|
| "Why this interpretation (4=entropy, 16=area)?" | §5 must give *one* specific reason — σ-fixed = invariant under twin-twist = informational; σ-mobile = exchanges with σ(V_600) = dynamical. State as definition with motivation, not as proof. |
| "Why V_600 specifically?" | §2 cites it as one element of a broader programme (substrate cascade, H₄ Coxeter); main theorem doesn't depend on programme being true. |
| "This is numerology." | Mitigated by §4 proof being one-page finite-group computation, and by §8 explicitly comparing to S–V and LQG — the genre exists. |
| "Where's the dynamics?" | §6: explicitly out of scope. The paper claims a coefficient, not a theory. |
| "Cascade-unit calibration is hand-wavy." | §6 acknowledges, frames as future work. The *ratio* is dimensionless. |

## Files this paper inherits

- `papers/cosmological-folding-rate/dynamics/bh_bekenstein_1_4.py` — verification script. Move/copy here.
- `papers/cosmological-folding-rate/dynamics/block2e_bulk_subgroup_check.py` — Dic_5 = bulk proof. Cite + summarise.
- `papers/paper-xxii/scripts/run_icosian_exact.py` — exact icosian arithmetic. Cite as dependency.

Nothing else from the cosmology paper is needed.

## Open questions before drafting

1. **Author line / affiliation.** Same as recent VFD papers, or new minimal affiliation for narrow-scope?
2. **Venue target.** arXiv hep-th + gr-qc cross-list, or a dedicated journal (CMP, JHEP)?
3. **Length target.** 12 pages or pad to 18 with more discussion?
4. **Should the τ_σ construction be mentioned at all?** Argument for: shows the cascade has a self-consistent involution; argument against: dismissable surface area.
5. **Should we include the single-quantum Hawking result as a §7 corollary?** Argument for: ties the 1/4 to a falsifiable prediction; argument against: same dismissable-surface tradeoff.

## Recommended next step

Draft a tight 12-page version with:
- §1–§5 doing the math (no rhetorical leverage)
- §6 the scope statement (one short page, marked)
- §7–§9 minimal context

Skip τ_σ. Skip Hawking. Skip cosmology. **One claim.**

If the math survives a hostile read, *then* we can write the cosmology paper citing this one as a foundation.
