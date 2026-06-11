# Paper XXX — Codex Review Loop Session
## 2026-04-17

**Tool:** OpenAI Codex CLI v0.121.0, model `gpt-5.4`
**Script:** `scripts/review_paper.sh`
**Target:** `papers/paper-xxx/paper-xxx.tex` (Born-rule derivation)

## Summary

Ten review rounds against Paper XXX with iterative edit passes. The paper moved from "proofs broken" (round 1) to "math is sound, remaining issues are prose asymptote and one residual real-slice-pullback gap in Cor fs_from_closure" (round 10). A new structural feature emerged from round 6: **VFD's observer formalism generalises standard Born to partial observers** (context-dependent conditional probabilities), now called out as a feature of the framework.

## Review trajectory

| Round | Top issue | Character | Review file |
|---|---|---|---|
| 1 | Step 4 proof wrong, Corollary Hadamard proof wrong, Route E overclaimed | **Proofs broken** | `paper-xxx-20260417T004934Z.md` |
| 2 | State-space confusion, closure-preserving ≠ U(N), Theorem Step 1 gap | **Structural** | `paper-xxx-20260417T010022Z.md` |
| 3 | Type discipline between config space and Hilbert space | **Formal coherence** | `paper-xxx-20260417T082440Z.md` |
| 4 | Scope upgrades: restricted results presented as global | **Scope prose** | `paper-xxx-20260417T091027Z.md` |
| 5 | Mcl ⊆ vs = CP(N-1); Prop born sampling hypothesis | **Explicit scope** | `paper-xxx-20260417T092050Z.md` |
| 6 | Probability definition bifurcation (raw mass vs conditional) | **Structural feature emerges** | `paper-xxx-20260417T092947Z.md` |
| 7 | Partial observer feature added, scope carried | **Feature added** | `paper-xxx-20260417T095037Z.md` |
| 8 | Route E scope upgrades in prose, sampling in summaries | **Polish** | `paper-xxx-20260417T095749Z.md` |
| 9 | Real-slice pullback in Cor fs_from_closure; Prop suff hypotheses | **Mop-up** | `paper-xxx-20260417T112549Z.md` |
| 10 | Completeness equivalence typo; theorem-vs-corollary scope mismatch; residual pullback gap | **Final asymptote** | `paper-xxx-20260417T113112Z.md` |

## What moved from "wrong" to "conditionally correct"

- **Corollary p_excluded**: round 1 "proof is wrong" (invalid Hadamard argument in 2D basis not containing Π) → round 3 onwards "proved correctly" with explicit N=3 completion-change counterexample.
- **Theorem born_unique Step 3**: round 1 "smuggles in additional eigenstate assumption" → round 4 onwards "mathematically fine given (U1)-(U4)" with explicit (U4) eigenstate certainty axiom.
- **Prop hessian_fisher**: round 3 "not formally coherent; θ declared as CP coordinates but used as translation parameters" → round 6 onwards "proof does establish a local Laplace-regime asymptotic for the translated density family; correctly local."
- **Prop suff**: round 2 "formally sloppy, type-unstable" → round 10 "basically correct in the exact sector-supported regime" with hypotheses added.

## What remained stable asymptotic

Despite 9 rounds of edits, the following three issues got refined but never fully closed:

1. **Cor fs_from_closure real-slice pullback**: round 4 onwards codex has flagged variations of "the bridge from configuration-space Fisher to real-slice Fubini–Study is asserted rather than proved." Round 9 added an explicit pullback calculation using Theorem chentsov(3) and the Nelson map; round 10 still flagged it as needing a rigorous "dimensional map" / "defined pullback". The fix would require explicit construction of the differential of $\theta \mapsto \Psi^*_\theta$ at $\theta=0$ as a map from config-space tangents to CP tangents, which is more than one round's work.

2. **Theorem born_unique vs Corollary U2_derived scope mismatch**: the Corollary establishes restricted (U2) on a specific observer sub-class, with Route C separation hypotheses; the Theorem then uses full (U2) on all projectors. The paper now flags this explicitly in axiom (U1)'s annotation and Remark `rem:U2_scope`, but codex continues to note the mismatch.

3. **Prose tightness at asymptote**: each round has identified 3-5 summary lines where hypotheses get dropped (sampling, completeness, sector-supported). Each round fixes most of them; 1-2 new ones surface. By round 10, the remaining ones are at the level of single-word improvements ("Derived for" → "Conditionally recovered for").

## Substantive edits made (selected)

1. **Corollary p_excluded** proof: replaced broken 2D Hadamard argument with explicit N=3 completion-change counterexample.
2. **Theorem 5** axiom system: added explicit (U4) eigenstate certainty; removed smuggled assumption in Step 3.
3. **Non-contextuality**: unified framing to "theorem within XXIX localised-probe sub-class for complete observers"; removed three contradictory statements across abstract/discussion/synthesis.
4. **Kochen–Specker reference**: corrected (KS doesn't apply to N=2).
5. **Closure-preserving vs U(N)**: split into two distinct groups — sector-preserving (U(1)^N ⋊ S_N) and equilibrium-tangent U(N) imported from Paper XXI.
6. **State-space notation**: dictionary added, config space / Hilbert space / projective space typed consistently.
7. **Probability definition**: unified to normalised conditional mass $\int_{B_{\phi_i} \cap \Phi_{\mathrm{adm}}(\Ocal)} |\Psi|^2 / \int_{\Phi_{\mathrm{adm}}(\Ocal)} |\Psi|^2$.
8. **Partial observer feature (ROUND 6)**: VFD predicts conditional probabilities for partial observers, extending standard Born beyond its implicit complete-measurement assumption. Added as a *feature*, not a bug, with dedicated remarks and conclusion paragraph.
9. **Real-slice pullback in Cor fs_from_closure (ROUND 9)**: added explicit calculation using Theorem chentsov(3) + Nelson pairing, yielding $g_{\mathrm{FS}}|_{\mathbb{RP}^{N-1}_+} = (1/2\sigma^2) H[\phi^*]$.
10. **Completeness vs universal completeness distinction (ROUND 10)**: corrected false equivalence; state-completeness and universal completeness ($\Mcl = \mathbb{CP}^{N-1}$) are now properly separated.

## Structural feature: Complete vs Partial Observers

Emerged from the review loop in round 6. The paper now explicitly distinguishes:

- **Complete observer for $\Psi$** (state-specific): $\rho_\Psi$ entirely supported in $\Phi_{\mathrm{adm}}(\Ocal)$. Normalised conditional $P$ reduces to unconditional sector mass. **Standard Born rule recovered.**
- **Universally complete observer** ($\Mcl(\Ocal) = \mathbb{CP}^{N-1}$): complete for every pure state. Strictly stronger. Required by Theorem 5.
- **Partial observer for $\Psi$**: $\rho_\Psi$ has weight outside $\Phi_{\mathrm{adm}}(\Ocal)$. **VFD predicts** $P(\Pi_i, \Psi; \Ocal) = |c_i|^2 / \sum_{j \in \mathrm{adm}}|c_j|^2$ (in sector-supported regime), with non-detection mass $1 - \sum_{j \in \mathrm{adm}}|c_j|^2$ as a structural prediction.

Standard QM handles this via POVMs or no-click outcomes; VFD delivers it from the admissibility structure. The framework is therefore a *generalisation* of standard Born, not a contradiction.

## Final paper state

- `papers/paper-xxx/paper-xxx.tex` — 962 lines, 131/131 env-balanced, no broken tags
- 10 review files in `docs/reviews/` capture the full trajectory
- Upstream Papers XVIII, XXI, XXIX updated earlier to carry the structures XXX references

## Remaining known issues (acknowledged in paper, fixable in further rounds)

- **Cor fs_from_closure real-slice pullback**: round 9's explicit calculation is present but codex round 10 still flags the "dimensional map" as insufficiently rigorous. A proper fix would require explicit construction of $d(\Psi^*_\theta)|_{\theta=0}$ as a map from $\mathbb{R}^d$ to $T_{[\Psi^*]}\mathbb{CP}^{N-1}$. Estimated 1-2 more rounds.
- **Prop suff statement vs proof**: round 9 added sector-supported hypothesis; codex round 10 still notes "also needs normalised sector modes, and that $T\Psi$ remains in the admissible class". Fixable in ~10 min.
- **Assorted prose asymptote** (~5-10 single-sentence tightenings per round, diminishing).

## Practical observations about the codex review loop

- **gpt-5.4 as reviewer**: accurate on math (catches real proof errors cleanly), fair about scope, reliable on citations. Occasionally hallucinates theorem numbers when citing upstream papers (codex can't compile). Lesson: cite descriptively to upstream papers, not numerically.
- **Trajectory shape**: rounds 1-4 each resolved 5+ substantive issues with sharp category transitions (proofs → structure → type → scope). Rounds 5-10 each resolved 2-3 real issues plus revealed 2-3 newly-visible smaller ones. Natural stopping point at "math is sound, prose is at polish asymptote".
- **Feature discovery**: the probability-definition bifurcation codex flagged in round 6 turned into the partial-observer feature section in round 7 — value the direct author-reviewer loop wouldn't have produced as directly.
- **Cost**: ~20 min of edits plus ~1 min of review per round. Ten rounds = ~3.5 hours of active work, not counting context-loading.
