# τ_σ involution — paper scope

**Working title:** *A canonical involution on the binary icosahedral group from σ-Galois projection on the icosian ring.*

**One-sentence pitch:** The binary icosahedral group V_600 = 2I admits a canonical involution τ_σ that fixes the binary dihedral subgroup Dic_5 ⊂ 2I pointwise and exchanges the K=52 and K=20 cycle classes within each non-trivial Dic_5-coset; the involution is constructed explicitly via σ-Galois projection in the icosian trace metric, with a residual Z_2^5 orientation ambiguity giving 32 = 2^5 canonical lifts.

## Why this paper, why now

Paper 3 in the V_600 programme. **Pure mathematics — no physics claim.** Provides the involution that Paper 4 (cosmic tensions) needs. Stands alone as a contribution to icosian / Coxeter-group structure theory.

The paper exists because Paper 4's operator-trace argument needs τ_σ to be *constructed*, not assumed. Without Paper 3, Paper 4's "K=52 and K=20 are τ_σ-paired" step is hand-waving.

## What's IN scope

1. **Setup.** V_600 = 2I; T_τ-cycle decomposition; K-class structure {72:1, 0:1, 52:5, 20:5}.
2. **Bulk subgroup theorem (cite Paper 1 / Block 2E).** Dic_5 ⊂ 2I is the self-normalizing, non-normal binary-dihedral subgroup of order 20 produced by the K=72 ∪ K=0 cycle union.
3. **Coset structure.** [2I : Dic_5] = 6. Right cosets Hg are the construction carrier: every non-bulk right coset is one whole K=52 T_τ-cycle plus one whole K=20 T_τ-cycle, because τ ∈ H gives τH = H and hence T_τ(Hg) = (τH)g = Hg (setwise T_τ-invariance). Left cosets gH contain 2 vertices from each of the 10 non-bulk T_τ-cycles and are NOT whole-cycle carriers (Paper 1 "Coset cycle composition" lemma).
4. **Computational reflection observation.** Block 3c (single E₈-Weyl-reflection candidates fixing Dic_5): trivial action on V_600 in the tested embedding. Block 3b (parity-flip candidates fixing Dic_5 and swapping K=52 ↔ K=20 closed-and-involution): zero target hits. No exhaustive enumeration over W(H₄) or full W(E₈) is claimed. This motivates using a vertex permutation rather than a reflection.
5. **Cycle-phase σ-projection construction (Route K).** For each non-bulk right coset Hg = (K=52 cycle (v_k) ∪ K=20 cycle (w_k)), define a T_τ-equivariant phase-j swap by τ_σ(v_k) := w_{(j+k) mod 10}. The phase j is selected by **symmetric** σ-projection maximin: s(j) := min_k min(⟨σ(v_k), w_{(j+k) mod 10}⟩_tr, ⟨σ(w_{(j+k) mod 10}), v_k⟩_tr); j ∈ argmax s(j) yields exactly two admissible phases per coset, j ∈ {0, 5} (in the deterministic base-point convention), where 5 is the antipodal shift of 0.
6. **Main theorem.** τ_σ is a well-defined involution on V_600 with: (i) τ_σ fixes Dic_5 pointwise; (ii) τ_σ swaps K=52 ↔ K=20 within each non-trivial coset; (iii) τ_σ-equivariance under T_τ; (iv) antipodal compatibility.
7. **Z_2^5 residual ambiguity.** Symmetric σ-projection filter gives 32 = 2^5 canonical lifts; the (0,0,0,0,0) phase is named canonical by convention. Discuss what fixes the convention vs. what is genuinely free.

## What's explicitly OUT of scope

1. **Physics interpretation** of τ_σ. None. Paper 4 / 5 territory.
2. **Cosmological observables.** None.
3. **Proof of uniqueness up to Z_2^5.** Sketch + computational verification; full proof a separate result if needed.
4. **Connection to σ-twin universe ontology.** Not in this paper.
5. **τ_σ on E_8, F_4, or higher Coxeter groups.** Tier-2 generalisation.

## Section structure (target ~14 pages)

1. **Introduction** (1.5pp). Why involutions on 2I matter; what Block 2E established; what's missing without τ_σ.
2. **Preliminaries: V_600, K-classes, Dic_5** (2pp). Recap with the K-multiset and coset structure.
3. **Why Coxeter reflections fail** (2pp). Block 3a–3c summary: E_8 reflection orthogonality argument.
4. **σ-projection construction** (3pp). Full definition, pseudocode, worked example for one coset.
5. **Main theorem and proof** (3pp). Verification of involution, fixity, swap, equivariance, antipodal compatibility.
6. **Z_2^5 residual ambiguity** (1.5pp). The 32 candidates, what choices are canonical, what remains free.
7. **Conclusion + outlook** (1pp). Pointers to Paper 4 + open generalisations.
8. **Appendix.** Verification scripts and full 120-vertex map.

## The undismissable spine

> We construct an explicit involution τ_σ : V_600 → V_600 on the vertex set of the 600-cell (equivalently, the binary icosahedral group 2I). The involution is defined via σ-Galois projection in the icosian trace metric on right cosets of H = Dic_5: each non-bulk right coset Hg is the disjoint union of one whole T_τ-cycle of K-class 52 and one whole T_τ-cycle of K-class 20 (Paper 1, "Coset cycle composition" lemma), and τ_σ pairs the two cycles by a phase-j swap selected by the symmetric maximin of the icosian trace inner product with σ, where σ is the Galois automorphism √5 ↦ −√5. The maximin yields exactly two admissible phases per coset (the antipodal pair {0, 5} in the deterministic base-point convention), giving a Z_2^5 = 32 canonical lift; the (0,0,0,0,0) phase is named canonical. We prove τ_σ is a well-defined involution that fixes Dic_5 pointwise, exchanges the K=52 and K=20 cycle classes within each non-bulk right coset, is T_τ-equivariant, and is antipodal-compatible. We use right cosets, not left, since right cosets Hg are setwise T_τ-invariant (because τ ∈ H), whereas left cosets gH are not whole-cycle carriers (Paper 1).

This reads as a structure paper in the icosian / Coxeter literature. Reviewers in that genre evaluate it on technical merit alone.

## Risk register

| Hook | Mitigation |
|---|---|
| "Why this construction, of all possible involutions?" | §4 motivates from the failure modes in §3; the σ-projection is the unique construction satisfying both K-swap and τ-equivariance derived from finite-group geometry. |
| "32 candidates is too much ambiguity." | §6 explains: 5 cosets × 2 phase choices = Z_2^5 is the natural residual, with the (0,0,0,0,0) lift fixed by symmetric projection; physical meaning of phases is open. |
| "How does this relate to known icosian / E_8 work (Conway–Sloane, Elkies)?" | §3 cites; explicitly notes that τ_σ is *not* a Weyl reflection of E_8. |
| "No physics here." | Correct. The paper is pure mathematics. State it openly; this is the strength. |
| "Computational verification only." | §5 includes a hand-checkable proof for one coset; computational verification covers the remaining four. Standard for finite-group structure theorems. |

## Files inherited

- `papers/cosmological-folding-rate/dynamics/block3h_VFD_canonical_filter.py` — construction.
- `papers/cosmological-folding-rate/dynamics/tau_sigma_VFD_canonical.txt` — explicit map.
- `papers/cosmological-folding-rate/dynamics/TAU_SIGMA_RESULT.md` — convert to draft text.
- `papers/cosmological-folding-rate/dynamics/block3a_e8_icosian_lattice.py`, `block3b_parity_flip_tau_sigma.py`, `block3c_e8_reflection_obstruction.py` — failure-mode analyses for §3.

## Open scoping questions

1. Should §3 (Coxeter-failure analysis) be its own short paper instead, with this paper a clean construction-only document?
2. Is the **Z_2^5 ambiguity** a flaw or a feature? Argument either way; current draft treats it as feature (residual orientation freedom).
3. Length: 14pp standard, or aim for 8pp short-paper format (CMP / Algebra & Number Theory style)?
4. Should we **cite the cosmological motivation** at all, or hold the paper to pure-math scope and let Paper 4 do the linking?
