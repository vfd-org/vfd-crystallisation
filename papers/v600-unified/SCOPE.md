# Unified V_600 framework — paper scope

**Working title:** *A unified framework for black-hole entropy, Hawking radiation, and cosmological tensions from the structure of the binary icosahedral group.*

**One-sentence pitch:** The Bekenstein–Hawking 1/4 coefficient, the discrete Hawking quantum E_q = 5/2, the τ_σ involution, and the (1 ± 1/12) operator-trace ratios — whose cosmological coupling is stated as a Layer-3 hypothesis (Paper 4 H1) — all derive from a single structural source: the cycle and coset decomposition of V_600 = 2I, the 20-vertex bulk subgroup Dic_5, the 24-vertex σ-fixed sublattice V_24 = Fix_σ(V_600) (with |Dic_5 ∩ V_24| = 4 — they are distinct), the σ-Galois twist, and the canonical involution τ_σ; this paper synthesises the four imported results into one mathematical scaffolding without re-proving any of them.

## Why this paper, why now

Paper 5 — the synthesis. **Cites all four prior papers and stands on them.** This is the only paper in the set that makes a "big" claim, but it does so on top of four already-shipped foundation papers. By the time a reader reaches Paper 5, Papers 1–4 have done the heavy lifting; Paper 5 is the integration chapter.

**This paper carries the highest dismissable risk** of the set. Mitigation: it adds NO new theorem-grade physical claim; it synthesises the four imported results, names the cross-cutting structural facts that make all four work, and names future bridge builds (CMB-bulk, cosmic dipole, prediction manifest) as explicitly OUT of scope.

## What's IN scope

1. **Citation-only import of the four foundation theorems** (cite Papers 1–4; NO re-proof):
   - Bekenstein S/A = 1/4 from Dic_5-coset incidence on V_600 (Paper 1).
   - Hawking quantum E_q = 5/2 from σ-pair excitation on V_600 mobile vertices (Paper 2).
   - τ_σ involution: explicit construction with (P1)–(P4) properties + antipodal compatibility, Z_2^5 = 32 phase ambiguity (Paper 3).
   - Exact operator-trace ratios tr(I_C + P_72)/12 = 13/12 and tr(I_C − P_0)/12 = 11/12 on the 12-dim cycle space; K-saturated admissibility theorem; coupling rule as Layer-3 hypothesis (Paper 4).
2. **Structural spine.** The finite tuple Σ_{V_600} = (G = 2I, T_τ, K-multiset {72:1, 0:1, 52:5, 20:5}, H = Dic_5, V_24 = Fix_σ(V_600), right-coset whole-cycle carriers, τ_σ, K-saturated algebra A_K). One table mapping each fact to its source paper(s) + status.
3. **V_24 / Dic_5 distinction (correctness lemma).** Fix_σ(V_600) = V_24 has 24 vertices; H = Dic_5 = (K=72 ∪ K=0 cycles) has 20 vertices; they are NOT equal. The intersection |H ∩ V_24| = 4 per coset is the Bekenstein 1/4 result (Paper 1, not a new claim).
4. **Cross-cutting role of τ_σ phase-independence.** All four imported theorems are independent of which canonical τ_σ lift (out of 32) is chosen. We import this from Papers 3 and 4 directly.
5. **Honest scope statement.** This is a math-scaffolding synthesis. Cosmological coupling (Hypothesis H1, Paper 4) remains Layer-3. CMB-bulk projection, cosmic dipole 1+k/2 ladder, and pre-registered prediction manifests are NAMED future builds with explicit unmet prerequisites — they are NOT claims of this paper.

## What's explicitly OUT of scope

1. **Re-deriving** what Papers 1–4 already proved. Cite, don't re-prove.
2. **Cosmological perturbation theory in V_600.** Tier-2.
3. **Quantum gravity ontology.** No claim; the paper offers a structural scaffold, not a theory of nature.
4. **CMB acoustic peaks** (numerical positions). Tier-2.
5. **τ_reion and recombination physics** (numerical). Tier-2.
6. **Spectral distortions** (μ-type, y-type). Tier-2.

## Section structure (target ~14 pages)

1. **Introduction** (1.5pp). The five-paper arc; what this synthesis adds (one structural-spine table + four citation-only theorem boxes); what it does NOT add (no new theorem-grade physical claim).
2. **Structural spine: V_600, Dic_5, V_24, T_τ, σ, τ_σ** (3pp). One table of the load-bearing facts with source-paper attribution. Includes the V_24 / Dic_5 distinction lemma.
3. **Imported theorem 1: Bekenstein 1/4 incidence** (1.5pp). Citation-only restatement; one-paragraph commentary on what role this plays in the synthesis.
4. **Imported theorem 2: Hawking quantum E_q = 5/2 + first-law identity** (1.5pp). Citation-only restatement; one-paragraph commentary.
5. **Imported theorem 3: τ_σ involution** (1.5pp). Citation-only restatement; phase-independence remark used by §6.
6. **Imported theorem 4: operator-trace ratios + K-saturated admissibility + coupling hypothesis** (2pp). Citation-only restatement; explicit Layer-1/2/3 separation maintained.
7. **Synthesis** (2pp). The four imported theorems share Σ_{V_600}; we record this without inferring physical unification.
8. **Honest scope and named future builds** (1.5pp). Load-bearing. Explicitly out of scope: (a) CMB-bulk-projection bridge (open builds in `closure-cosmogenesis.md`), (b) cosmic dipole ladder audit (current scripts exploratory + partly fitted), (c) pre-registered prediction manifest (requires reconciliation of `preregister_k.py` with locked sources).
9. **Conclusion** (0.5pp).
10. **Appendix.** Verification certificate (`verify.py`) — computes Σ_{V_600} from `vfd_v600.group.build_state()`, asserts each structural-spine fact, and re-runs each foundation paper's headline number as a cross-check.

## The undismissable spine

> We integrate four prior results — the Bekenstein–Hawking 1/4 coefficient as Dic_5-coset incidence on V_600 (Paper 1); the discrete Hawking quantum E_q = 5/2 from σ-pair excitations (Paper 2); the canonical involution τ_σ : V_600 → V_600 (Paper 3); and the exact operator-trace ratios 13/12 and 11/12 on the 12-dimensional V_600 cycle space, with the cosmological coupling map stated as an explicit Layer-3 hypothesis (Paper 4) — into a single mathematical scaffolding. The synthesis adds NO new theorem-grade physical claim; it records the load-bearing structural tuple Σ_{V_600} = (V_600 = 2I, T_τ-cycle decomposition, K-multiset {72:1, 0:1, 52:5, 20:5}, bulk subgroup H = Dic_5 of order 20, σ-fixed sublattice V_24 = Fix_σ(V_600) of size 24, right-coset whole-cycle carriers, canonical involution τ_σ, K-saturated algebra A_K) and observes that all four foundation theorems factor through Σ_{V_600}. The paper does NOT claim a unified physical theory. CMB-bulk projection, cosmic dipole ladder audit, and pre-registered prediction manifests are named future builds with explicit unmet prerequisites; they are excluded from the scope of this synthesis.

A reviewer reading this *after* having seen Papers 1–4 finds a synthesis backed by foundation work. A reviewer who jumps directly to Paper 5 without reading the others should also be able to evaluate it on the strength of the citations.

## Risk register

| Hook | Mitigation |
|---|---|
| "Five Nobel-tier claims in one paper." | Mitigated by: the synthesis adds NO new theorem-grade physical claim. The four foundation papers (Papers 1–4) each prove a narrow finite-group identity; this synthesis records that they all factor through one structural tuple Σ_{V_600}. CMB-bulk projection, cosmic dipole audit, and pre-registered prediction manifests are all named OUT-of-scope as F1/F2/F3 future builds with explicit unmet prerequisites. |
| "Where is the dynamics?" | §8 acknowledges: this is a math-scaffolding paper, not a complete theory. The papers it cites contain the load-bearing arguments. |
| "What does the synthesis actually add?" | §2 (the structural-spine table Σ_{V_600}) plus §7 Proposition 7.1 (each of IT1–IT4 factors through Σ_{V_600}). The synthesis is exactly that observation, not a unification theorem in physics. |
| "Why publish a synthesis at all?" | §1 explains: the four foundation papers each have narrow scope; the synthesis records the load-bearing structural tuple they share, which is itself a contribution. |

## Files inherited

- All cosmological-folding-rate dynamics scripts.
- `UNIFIED_RESULT.md` — convert to long-form draft.
- All four prior papers' verification scripts.

## Open scoping questions

1. **Should Paper 5 ship at all**, or should the four foundation papers stand without a synthesis? Argument for: synthesis records the structural tuple Σ_{V_600} that readers want named explicitly. Against: bigger target.
2. **Length: 14pp vs 18pp.** Current target 14pp; reviewers may want more discussion.
3. **Venue: PRD synthesis section, or hold for a high-profile review article?** Different audiences.
5. **Should Paper 5 ship in parallel with Paper 4, or wait until Papers 1–4 are all visibly cited?** The latter is safer per credibility-bar discipline.
