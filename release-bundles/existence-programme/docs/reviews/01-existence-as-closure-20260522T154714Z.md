Line refs are to `papers/01-existence-as-closure/main.tex` unless another paper is named.

**Verdict**
No, not publication-ready yet. Round 2 materially improves the framing, especially `\tau_{\mathrm{ico}}` / `\tau_{\mathrm{spec}}` and the Banach-neighbourhood restriction, but the formal core still overclaims `C=\Fix(\tau)` and the programme-status layer needs reconciliation.

**Round-1 Blocker Check**
- 0.1 `\tau_{\mathrm{ico}}` vs `\tau_{\mathrm{spec}}`: mostly resolved. Lines 356-363 explicitly define both conventions and name the 94/116 split. Remaining unqualified uses still need cleanup, especially lines 605, 689, 903, and appendix line 1126.
- 0.2 subspace invariance vs pointwise fixedness: not substantively resolved. Line 371 now states the distinction, but Theorem 2.1 at lines 254-269 still identifies the maximal closure-stable subspace with pointwise `\Fix(\Ccal)`, and lines 377-379 still assert `C=\Fix(\tau)` from insufficient hypotheses.
- 0.3 Banach contraction near `\varphi`: resolved. Line 324 correctly restricts the contraction claim to a strict neighbourhood of `\varphi`.
- 10-paper map: added at lines 1155-1224, but not yet fully coherent with the local companion manuscripts.
- D8 honest residual: conceptually present at lines 390 and 745, but the arithmetic/status is inconsistent: line 745 says 48 fixed and remaining 72 Type-C, while the script comments describe 96 Type-C vertices; `results.json` also lacks D7/D8 because `closure_demo.py` writes it before those demos are added.

**1. Claim Audit**
- “The set of closure-stable subspaces… has a unique maximal element `U:=Fix(C)`” (254-260): not proved and generally false under Definition 2.2. For a contraction-like linear map `aI`, `0<a<1`, every subspace is invariant/equal under image up to scalar, while pointwise `Fix(aI)=0`.
- “A subspace `X` is closure-stable if `C(X)=X`” (248-249) vs “read as subspace invariance… not pointwise fixedness” (371): the paper changes semantics midstream. Choose one and restate the theorem accordingly.
- “`C := U \cap Fix(tau)`” and admissible iff pointwise fixed (261-265): only works if `U` is explicitly the pointwise fixed subspace by definition, not as a Tarski consequence.
- “Existence-as-Closure Principle” (271-275): acceptable as a definition of admissible vectors; not a corollary of the theorem as proved.
- “Capstone identification” (284-289): acceptable only as imported and conditional on G-FIC-a/b, G-loc-a, H-lift-fin. It should be labelled conditional/imported, not presented as locally established.
- “Banach… unique attracting fixed point on this neighbourhood” (324): established with the stated neighbourhood restriction; add “for sufficiently small `\epsilon` so the interval maps into itself.”
- “Cascade chain” and “GH limit” (334-340): imported, not proved locally. Fine if treated as cited precursor content.
- “`\Cph` is symmetric, positive definite, and symmetry-equivariant” (352): SPD/min-eigenvalue is fine; symmetry-equivariance depends on the chosen `\tau`. The contraction belongs to `I-\lambda\Cph`, which line 352 now says correctly.
- “`\dim\Fix(\tau_{\mathrm{ico}})=94`” (365-366): imported theorem, not verified by local demos. OK if cited as imported.
- “Conversely any `\tau`-stable closure-invariant subspace lies inside `\Fix(\tau)`” (377): false as written. `H` itself is `\tau`-stable and `\Cph`-invariant. You need “pointwise `+1`-fixed” as an admissibility axiom.
- “`C=\Fix(\tau)`” (379, 388, 902, 913): not established. D7 verifies invariance of `\Fix(\tau)`, not maximality or equivalence.
- “CP-rung-9.3… dimensions per rung are derived” (514-522): overclaimed. Exact values are given for selected polytope conventions; abstract rungs are only upper-bounded.
- “C1 closes CP-rung-9.3” (755, 759, 911): should be “closes the spectral-polytope demonstration only.” It does not close abstract rungs or the icosian-vs-spectral gap.
- “Per-frame zero-line… `dim <= min(|O|,94)`” (600-605): valid only under `\tau_{\mathrm{ico}}`. Under `\tau_{\mathrm{spec}}`, the cap is 116.
- “Inputs on `\Sigma_I` are invariant under closure ticks” (618-619): overstates. The theorem says the subspace is invariant, not that each vector is pointwise unchanged.
- “Generative excess theorem” (645-647): imported; D6 only demonstrates a chosen sample with `\delta_{AB}=0`, so it does not numerically witness strict excess.
- “Embedding image `!_I(I) subset C`” (665-674): depends on the unresolved `C=\Fix(\tau)` identification.
- “Canonical properties of complexity” (685-692): no proof is given; C3 is convention-dependent, C4 needs “dimension preserved,” not content pointwise preserved.
- “Recursion-depth bound… `<=9`” (707-709): arithmetic is fine for `k=94`; if spectral convention is used, the maximum is different.
- D1-D8 table (738-745): D1/D2/D3 commutation/D5 are fine under spectral convention; D4 conflicts with the 94 cap; D7 does not prove `C=\Fix(\tau)`; D8 is honest but internally inconsistent in counts.
- “29 distinct structural demonstrations” (759) vs “27 sim demonstrations” (790) vs “29 + 6 = 35” (1072): inconsistent.
- ARIA empirical results (775-780): broadly match Paper 03, but are constructed-witness/empirical-correspondence claims, not proof of foundation theorems.
- F1-F10 (895-904): F2 and F10 are cleanest. F3/F4/F9 must specify `\tau` convention. F5/F8 are overclosed. F6 needs explicit `\lambda` step-map wording.
- “Falsifiers of `\Lambda` or `H_0` are simultaneously falsifiers…” (930): too strong. They would pressure the shared cosmology/substrate extension, not automatically falsify the local closure definitions.
- “No tunable parameters” (995): true for the structural operator only; not true for empirical proxies across Solution Lab papers, which use thresholds, feature choices, and diagnostics.

**2. Internal Consistency**
- The main conflict is closure semantics: pointwise fixedness at 254-265, subspace invariance at 371-375, and dynamic attraction at 352/900 are three different notions.
- `\tau` dimensions are not consistently qualified. The abstract and F-list still use 94 as universal even where the demos use 116.
- CP-universal and CP-rung are called closed at 390, 512, 911, 913, but open at 407, 451, 964, 1105-1106.
- `\Ccal` denotes both the closure operator and frame complexity (681-682), creating avoidable ambiguity.
- Appendix line 1126 says “spectral -> `\Fix(\tau)`, dim 94”; spectral gives 116. This should say icosian or split both rows.
- D8 line 745 has arithmetic/category problems: “48 of 120 (`V_{24}`-cell + 16-cell)” does not match the 24-cell/16-cell counts or the script’s 96 Type-C language.

**3. External Consistency**
- Paper 02: The living-frame summary is broadly right, but Paper 02 has P1-P15, i.e. 15 predictions; line 997 says “13 predictions P1--P15.” Also Paper 02’s demos use spectral `\tau` and report 116-dimensional outputs.
- Paper 03: ARIA, Levin, CEMI, B1-B3, and SL-002 summaries match. But biological bridge claims require H-RP-3, which Paper 01 sometimes omits when generalising beyond cortex.
- Paper 04: C1-C5 match, and H-rec/H-evolve are explicitly open there. Paper 01 should not make recurrence/cosmic closure sound settled.
- Paper 05: Paper 01’s “BETSE + 5 wet-lab predictions” summary matches. Note Paper 05 itself has a “4 total” condition typo while listing six conditions.
- Paper 06: The 14/14, `t=7.11`, sLORETA `t=9.72`, and ds004541 7/7 figures match. For methodology claims, also cite the Paper 07 LOSO `d_z=2.07` as the honest cross-validated refinement.
- Paper 07: CAD-D1-D5-v1 and 14/15 match. However trait anxiety is PASS-leaning/boundary, not a strict clean PASS.
- Paper 08: Paper 01 undersells the current local paper by omitting the ds004315 mood-manipulation replication, and overstates the diagnostic as simple PASS rather than boundary/PASS-leaning.
- Paper 09: Local Paper 09 reports two completed real-data diagnostic-predicted FAILs, MOBA and table tennis. Paper 01 line 1176 reflects this, but line 1209 still calls SL-006 scaffolded.
- Paper 10: Paper 01 reports only the ds007471 musical negative. Local Paper 10 also reports ds006802 collaborative rule-learning as a moderate-positive trend, so Paper 01 now undersells Paper 10.

**4. Narrative Coherence**
The vocabulary is mostly aligned with the programme: structural claims, P-A-conditional phenomenology, and CAD-scoped empirical proxies are all present. The paper still reads partly like a four-paper synthesis plus appendix, not the canonical Paper 01 of a 10-paper programme. Move the 10-paper map forward and make it the organising frame.

The “unfinished business” section is rhetorically too broad before the math is secured. It can stay, but phrases like “all five share a common structural origin” (125) should become an investigated compression claim.

**5. Tightness Edits**
- 125: “The framework investigates whether these five can be compressed by a common closure scaffold.”
- 377-379: “Thus `\Fix(\tau)` is a `\Cph`-invariant admissible candidate; equality with `C` requires the pointwise `+1` admissibility axiom.”
- 390: “CP-universal-5.1: D7 verifies invariance; maximality/equality remains theorem-dependent.”
- 512: “Per-rung `\sigma`-fix inventory: polytope rungs represented; abstract rungs bounded.”
- 618: “Inputs in `\Sigma_I` remain inside `\Sigma_I`; off-`\Sigma_I` components contract under the step dynamics.”
- 930: “Cosmology failures would pressure the shared-substrate cosmology extension.”

**6. Surface Issues**
- `references.bib` has an extra stray `}` after `SolutionLab007`, which will break BibTeX.
- `SolutionLab005`, `006`, and `007` BibTeX notes are stale/scaffolded relative to local papers.
- `closure_demo.py` writes `results.json` at lines 407-408 before D7/D8 are added, so the checked-in JSON contains only D1-D6.
- Several result counts conflict: 29, 27, and 35.
- Undefined/underdefined notation: `\hat{O}`, `A_1(C_{\varphi,I})`, `\pi_\varphi(583)`.
- Use one capitalization convention for zero-line / Zero-Line and sigma-fix / `\sigma`-fix.

**7. Top Three Fixes**
1. Fix the formal core around lines 248-269 and 371-390: define exactly whether closure means pointwise fixedness, invariant subspace, or attraction under `I-\lambda\Cph`, then restate `C`.
2. Reconcile `\tau` and CP status everywhere: 94 vs 116, D7/D8, F3/F4/F8/F9, CP-universal, CP-rung.
3. Update the programme map and empirical status: Papers 08-10 have moved beyond the simplified summaries, and Paper 07’s CAD boundary should gate all real-data language.

**8. Programme-Strengthening Recommendations**
- Add a front-matter status ledger: formal theorem, imported theorem, conditional proposition, computational witness, empirical proxy, CAD-scoped real-data result.
- Make `\tau_{\mathrm{ico}}` the theorem convention and `\tau_{\mathrm{spec}}` the simulation-proxy convention across all papers, with dimensions always stated beside the convention.
- Create a single programme prediction registry: F1-F10, P1-P15, B1-B3, C1-C5, CAD, and SL-001/002/005/006/007.
- Standardise empirical wording: “direct operator,” “constructed witness,” “first-order proxy,” “CAD-licensed test,” and “honest negative” should not be interchangeable.
- Put Paper 07’s CAD diagnostic in Paper 01 before the Solution Lab map, so scope discipline is visibly foundational.

**9. Publication Ready?**
No. Over-claiming remains worse than under-claiming here. The paper is much closer after Phase A, but `C=\Fix(\tau)` and CP-closed language need mathematical repair before this can safely serve as the foundation paper for the ten-paper programme.
