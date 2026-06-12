Reviewed `papers/01-existence-as-closure/main.tex` in full. Line refs below are to that file unless a companion path is named.

**1. Claim Audit**
- L254-L269, “Algebraic existence”: not established as stated. The proof confuses subspace invariance `C(X)=X` with pointwise fixed vectors `C(v)=v`. For an invertible linear map such as `C_\varphi`, the maximal `C(X)=X` subspace is generally all of `H`, not `Fix(C)`.
- L271-L275, Existence-as-Closure corollary: only valid as a definition of admissible vectors after the theorem above is corrected. It does not follow from the stated proof.
- L284-L289, Capstone identification: should be a conditional/imported theorem, not theorem-grade in this paper. It depends on named residual hypotheses and on the ambiguous definition of `C`.
- L324, Banach application: false as written. `r -> 1 + 1/r` is not a contraction on `[1,2]` with Lipschitz constant `\varphi^{-2}`; the derivative bound reaches `1` at `r=1`.
- L334-L340, cascade chain and GH limit: imported claims only. Acceptable if the cited precursor proves them, but this paper does not.
- L352, “`\Cph` … satisfies the self-similarity condition … with `k=\varphi^{-2}`”: not true for `L_{V600}+\varphi^{-2}I`; its eigenvalues exceed `1`, so the definition at L243 fails.
- L356-L357, `dim Fix(tau)=94`: imported, but not verified by this paper’s demos. The local demo output gives spectral `dim Fix(tau)=116`, target `94`, `match=false`.
- L362-L372, `C = Fix(tau) ∩ ker(Cphi-I)` and `dim C=94`: not established. Later “D7” verifies invariance of `Fix(tau)`, not pointwise fixedness under `Cphi`.
- L495-L515, CP-rung-9.3 theorem: overclaimed. The proof gives exact values only under selected `tau` conventions and only upper bounds for abstract rungs. The cited cosmic C1 demo reports spectral dimensions `E8=156`, `H4=116`, `D4=22`, not `120/94/24`.
- L563-L597, anchor, zero-line, closure invariance, decay: imported from precursor notes. The decay theorem supports a spectral lower bound, but L599-L600 overreads it as “inputs on Sigma are invariant”; invariance of a subspace is not pointwise persistence.
- L626-L628, generative excess: imported. D6 only demonstrates a sample with `delta_AB=0`, so it does not numerically verify strict generative excess.
- L638-L648, embedding and image identification: the formula is imported, but `pi_I(Sigma_I) subset C` requires `Sigma_I subset C`; the paper only establishes/inherits `Sigma_I subset Fix(tau)`.
- L666-L673, canonical complexity properties: no proof is given. C3 depends on the unresolved `94` vs `116` convention.
- L675-L690, seven-level scaling and recursion bound: imported. The recursion arithmetic for `k=94` is fine, but the bound rests on the disputed complexity cap.
- L696-L698, rung complexity: internally inconsistent with later claims that CP-rung-9.3 is closed.
- L803-L805, cortex as frame: correctly conditional on H-RP-1/H-RP-2, but biology-facing claims elsewhere also require H-RP-3.
- L714-L724, D1-D6 table: “All six pass” is false. Existing `results.json` has D3 `116` vs target `94`, `match=false`, and D4 `dim_sigma_I=116` with `max_possible=94`.
- L881-L892, F8 / CP-universal closed: not established. “`Cphi` maps `Fix(tau)` into `Fix(tau)`” does not imply `C=Fix(tau)` under the paper’s own pointwise admissibility criterion.

**2. Internal Consistency**
- The largest inconsistency is `tau`: theorem text uses icosian `tau` with `dim Fix(tau)=94`, while the demos and companion sims use spectral `tau` with `dim Sigma=116`.
- “Closure-stable” alternates between pointwise fixed, invariant subspace, and dynamically attracting under `I-lambda Cphi`.
- CP-rung-9.3 and CP-universal-5.1 are called open at L371/L943/L1084-L1085, closed at L878/L890-L892.
- The paper says “six demonstrations D1-D6” at L709-L724, “D1-D7” at L1045/L1165, and “28 sim demonstrations + 6 substrate facts” at L1051.
- `\Ccal` is used both for the closure operator and frame complexity at L662, creating notation collision.
- The programme is described as two companion papers at L67 and four papers at L1137-L1150, not the current ten-paper programme.

**3. External Consistency**
- Paper 02 agrees on the living-frame definition and 18 objects, but its demo output uses `dim_Sigma=116`, not the foundation paper’s `94` cap.
- Paper 03 supports the ARIA `17/18` and `18/18` summary, plus SL-001/SL-002 details. Foundation should also import H-RP-3 when discussing Levin/bioelectric bridges.
- Paper 04 C1 supports “non-trivial spectral Sigma and commuting tau,” not the exact rung dimensions claimed in Paper 01.
- Paper 07 supports CAD-D1-D5-v1 and `14/15` classification, but it explicitly frames closure-as-distance as a first-order proxy, not direct validation of the closure operator.
- Paper 08 is oversimplified here: foundation says trait anxiety was a clean diagnostic PASS; Paper 08 reports borderline/marginal diagnostic features and later additional mood/dementia scope refinements.
- Paper 09 is stale: foundation says SL-006 is scaffolded, while the current Paper 09 reports two real-data FAILs and says FlowIndex has no real-data PASS yet.
- Paper 10 is incomplete: foundation reports only the musical-joint-action negative, while current Paper 10 also reports ds006802 collaborative rule learning with a moderate-positive trend.

**4. Narrative Coherence**
- As the foundation paper for a ten-paper programme, it should stop presenting itself as a four-paper synthesis. L1137-L1182 is now structurally obsolete.
- The “unfinished business” section L125-L159 over-centres cosmology, measurement, fine-tuning, and flavour/cosmology support before the closure mathematics is stable.
- The foundation should introduce the CAD applicability boundary earlier, because Papers 07-10 now make empirical scope a central discipline.
- The Access Principle discipline is mostly coherent, but cosmic recurrence should be marked as H-rec/H-evolve conditional and held back, matching programme framing.

**5. Tightness Edits**
- L125: change “all five share a common structural origin” to “the framework investigates whether these five can be compressed by a common closure scaffold.”
- L352: replace with “`\Cph` is symmetric, positive definite, and `tau`-equivariant; contractive dynamics require a step map such as `I-\lambda\Cph`.”
- L714: replace “All six pass” with “The demos verify substrate construction and selected spectral facts; `tau`-dimension claims depend on the chosen `tau` construction.”
- L738: replace “verify the framework’s load-bearing claims” with “exercise the claimed mechanisms under explicit simulation conventions.”
- L881/L892: replace “closed structurally” with “open until pointwise fixedness versus invariant-subspace closure is resolved.”
- L909: replace “simultaneously falsifiers” with “would pressure the shared-substrate extension, not the core closure definitions alone.”

**6. Surface Issues**
- Repro paths are wrong for this release bundle: e.g. L709 and L1045 use `papers/existence-as-recursive-closure/...`, but the actual path is `papers/01-existence-as-closure/...`.
- `scripts/run_all_sims.sh` uses unnumbered paper paths and would skip the current release-bundle directories.
- `closure_demo.py` writes `results.json` before D7/D8 are added, so the JSON lacks the later claimed results.
- L1045-L1051 demo counts are inconsistent with L738 and with actual result files.
- Table L1205 in Paper 02 says “All ten pass” while listing L1-L13; not this paper’s fault, but it affects cross-paper consistency.
- Several “release-ready” status labels in Paper 01 are stronger than the companion papers’ “pre-peer-review draft/open research note” status.

**7. Top Three Fixes**
1. Resolve the `tau`/closure semantics problem: icosian `94` vs spectral `116`, pointwise fixed vs invariant subspace, and `C=Fix(tau)` claims. This affects L254-L269, L352, L362-L372, L495-L515, L881-L892.
2. Replace the four-paper programme map with a ten-paper map and update SL-005/006/007 summaries to match current companion files. Key stale block: L1137-L1182.
3. Rebuild the reproducibility story: correct paths, fix `run_all_sims.sh`, regenerate JSON, and do not claim D3/D4/D7/C1 verify exact theorem values until they actually do.

**8. Programme-Strengthening Recommendations**
- Add a ten-paper status matrix in Paper 01: structural theorem, conditional bridge, first-order empirical proxy, diagnostic scope, current evidence.
- Standardise `tau` conventions across all papers: “icosian tau” and “spectral proxy tau” should never share the same dimension claims.
- Add a programme-wide empirical language rule: “direct operator,” “constructed witness,” “first-order proxy,” “CAD-licensed real-data test,” and “honest negative” should be used consistently.
- Move cosmology/flavour claims into a bounded cross-anchor appendix unless they are necessary for Paper 01’s core theorem chain.
- Make Paper 07’s CAD diagnostic the explicit gatekeeper for all real-data claims cited by Papers 01, 02, 08, 09, and 10.

**9. Publication Ready?**
No. The paper is not publication-ready on substantive math/attribution scope. The main issue is not presentation; it is that key formal claims rely on an unresolved change in the meaning of closure and on incompatible `tau` conventions. Fixing that should come before tightening prose or adding more cross-paper evidence.
