**1. Claim Audit**
- `[D.1]` “`A_5` permutes faces … `C_6` acts on `ℤ[ω]` … neither is a subgroup of the other” is now mathematically clean and fixes the earlier stabiliser error ([derivation-capsid.md:98-121](papers/biology-rung/derivation-capsid.md:98)). The round-0 fix holds.
- `[D.2]` “`𝒯_casc(z)=|z|²` … scalar-valued and therefore transforms trivially” is also fixed: the vacuous `A_5`-equivariance claim is gone, and scope is honestly face-level ([derivation-capsid.md:157-177](papers/biology-rung/derivation-capsid.md:157)). The round-0 fix holds.
- `[L.0]` “`π_20 = 1 ⊕ 3 ⊕ 3' ⊕ 4^{⊕2} ⊕ 5`” is true, but the proof is just “standard character-theoretic calculation” ([derivation-capsid.md:132-138](papers/biology-rung/derivation-capsid.md:132)). Correct claim; under-argued, not false.
- `[L.1]` “`spec(𝒯_casc)=` Loeschian numbers” is established exactly as stated ([derivation-capsid.md:179-186](papers/biology-rung/derivation-capsid.md:179)).
- `[L.3]` “any positive-definite `C_6`-invariant quadratic form is `c·𝒯_casc`” is now actually proved, not sketched ([derivation-capsid.md:188-214](papers/biology-rung/derivation-capsid.md:188)). The round-0 fix holds.
- `[T.1]` is established only at face level, and the theorem itself now says that honestly ([derivation-capsid.md:224-244](papers/biology-rung/derivation-capsid.md:224)). The round-0 fix holds. But the document opening still over-claims “cell-level icosahedral substrate” ([derivation-capsid.md:7-14](papers/biology-rung/derivation-capsid.md:7)).
- `[R.1]` correctly establishes “`5` is not Loeschian” and “`5 ∉ spec(𝒯_casc)`” ([derivation-capsid.md:258-283](papers/biology-rung/derivation-capsid.md:258)). But the sentence “whether empirical capsid counts reinforce this … is … resolved computationally in `[N.2]`” is not established: `[N.2]` is still empty and the compare script is missing.
- `[L.2]` is now correctly phrased as “three of the four distinct `A_5` irrep dimensions” ([derivation-capsid.md:285-302](papers/biology-rung/derivation-capsid.md:285)). The round-0 fix holds.
- `[D.3]` is partly sound and the listed small values are correct. The sim confirms `μ(1)=1`, `μ(7)=2`, `μ(49)=3`, and the emergent `μ(91)=4` in `data/wo1_prediction.csv` ([wo1_prediction.csv:34](papers/biology-rung/data/wo1_prediction.csv:34)). But the prose “`μ(T)=2` when `h,k>0` are nonzero and distinct” overstates the pattern ([derivation-capsid.md:354-359](papers/biology-rung/derivation-capsid.md:354)): `T=91` has such representatives and `μ(91)=4`, not `2`.
- `[C.1]`, `[C.3]`, `[C.4]` are properly labelled conjectural/speculative ([derivation-capsid.md:374-413](papers/biology-rung/derivation-capsid.md:374), [522-536](papers/biology-rung/derivation-capsid.md:522)).
- `[C.2]` is no longer sold as proved, but the round-0 fix is not fully propagated. §6 labels it an open problem ([derivation-capsid.md:419-489](papers/biology-rung/derivation-capsid.md:419)); §8 still calls it “Conjecture, sketch only” ([derivation-capsid.md:576-583](papers/biology-rung/derivation-capsid.md:576)). Also the “three-step plan” claim is false: §6 gives four steps ([derivation-capsid.md:457-479](papers/biology-rung/derivation-capsid.md:457)).
- `[N.1]` / `[N.2]` are stale. `[N.1]` says “pending sim run” although `wo1_prediction.csv` already exists; `[N.2]` is not established because there is no comparison artefact or `wo1_compare.py` ([derivation-capsid.md:559-570](papers/biology-rung/derivation-capsid.md:559)).

**2. WO Acceptance Audit**
- `AC1`: not resolved. The artefacts are not publication-ready on substantive honesty/attribution grounds.
- `AC2`: partially resolved. The catalogue includes all named objects, but status/content drift remains.
- `AC3`: not resolved. `wo1_capsid_predict.py` exists and has been run; `wo1_viperdb_fetch.py` exists; `wo1_compare.py` is absent.
- `AC4`: not resolved. No χ²/KL comparison artefact exists.
- `AC5`: partially resolved. The mathematical `T=5` issue is settled in the derivation; the empirical side is still unsupported.
- `O1`: partial. Now honestly open as `[C.2]`, but not answered.
- `O2`: resolved mathematically. Current derivation lands on “the 5 is a rep dimension, not a T-value.”
- `O3`: resolved. Face-level `A_5` action and lattice-level `C_6` action are distinguished cleanly.
- `O4`: partial. Framed conjecturally only.
- `O5`: not touched.

**3. Catalogue Audit**
- Good: every derivation object `[D.1] [D.2] [D.3] [L.0] [L.1] [L.2] [L.3] [T.1] [R.0] [R.1] [R.2] [C.1] [C.2] [C.3] [C.4] [N.1] [N.2]` appears in the catalogue.
- Defect: catalogue `[R.1]` reintroduces the unsourced claim “no `T=5` capsids are observed” ([math-catalogue.md:272-282](papers/biology-rung/math-catalogue.md:272)). That round-0 fix did not stick.
- Defect: catalogue `[C.2]` says “plan of attack sketched in three steps” ([math-catalogue.md:347-349](papers/biology-rung/math-catalogue.md:347)), while the derivation gives four.
- Defect: catalogue `[N.1]` still says “pending sim run” ([math-catalogue.md:396-404](papers/biology-rung/math-catalogue.md:396)) although the csv exists.
- No missing catalogue entries from the derivation.

**4. Attribution / External Consistency**
- `cascade-bio.md §B3.2` really does contain the bad `T=5 ↔ A_5 5-dim irrep` row at line 283, and §B3.4 really does leave “Full derivation of all T-numbers from one cascade operator” open at line 320 ([cascade-bio.md:274-320](papers/cascade-derivation/cascade-bio.md:274)). Those citations are accurate.
- `paper-xxxii.tex §3` Theorem `thm:600cell` really is the `(H1)-(H4) ⇒ 2I` theorem ([paper-xxxii.tex:237-247](papers/paper-xxxii/paper-xxxii.tex:237)). Citation corrected correctly.
- `paper-xxxii.tex §4` Theorem F really is the `A1-A3` soft-min/log-sum-exp uniqueness theorem ([paper-xxxii.tex:363-379](papers/paper-xxxii/paper-xxxii.tex:363)). Citation corrected correctly.
- `cascade-foundations.md §F2` really is the `F = αR + βE − γQ` theorem ([cascade-foundations.md:135-155](papers/cascade-derivation/cascade-foundations.md:135)). Path correction is correct.
- Defect: §6 says “Write the closure functional of Paper XXXII as `F : C^∞(S³, 𝒜) → ℝ` … this domain is implicit in Paper XXXII” ([derivation-capsid.md:452-455](papers/biology-rung/derivation-capsid.md:452)). That is not what the cited paper states; Paper XXXII defines a pointwise closure functional on `x ∈ M`, not a field functional on `C^∞(S³,𝒜)`. This is an attribution overreach.

**5. Sim Correctness**
- For `[L.1]`: yes. `T_of(h,k)=h²+hk+k²` is correct ([wo1_capsid_predict.py:34-36](papers/biology-rung/scripts/wo1_capsid_predict.py:34)).
- For `[D.3]`: yes. The `ω` action `(h,k)↦(-k,h+k)` is correct, the `C_6` orbit generation is correct, and wedge enumeration is complete for the stated task ([wo1_capsid_predict.py:39-61](papers/biology-rung/scripts/wo1_capsid_predict.py:39), [76-106](papers/biology-rung/scripts/wo1_capsid_predict.py:76)). I brute-force cross-checked the orbit table up to `T≤120`; no mismatches.
- The spot-check assertions are honest as far as they go ([wo1_capsid_predict.py:147-170](papers/biology-rung/scripts/wo1_capsid_predict.py:147)). They verify the values actually stated in §5 and some forbidden non-Loeschians. They do not verify the novel `μ(91)=4`; they simply omit it.
- The emergent `μ(91)=4` does hold. The generated csv records `91,4` with representatives `(1,9);(5,6);(6,5);(9,1)` ([wo1_prediction.csv:34](papers/biology-rung/data/wo1_prediction.csv:34)).
- Bug/risk: the csv `chirality` field is too coarse. It marks a whole `T` as `chiral` if any orbit at that `T` is chiral ([wo1_capsid_predict.py:122](papers/biology-rung/scripts/wo1_capsid_predict.py:122)). For `T=49` that collapses one achiral orbit plus a chiral pair into a single label. If downstream code uses that column statistically, it will be wrong.
- I cannot audit χ²/KL/null-hypothesis handling because `wo1_compare.py` is not present.

**6. Tightness**
- Opening claim too strong: “single operator on the cell-level icosahedral substrate” should be “face-level Eisenstein substrate” ([derivation-capsid.md:7-10](papers/biology-rung/derivation-capsid.md:7)).
- `[D.3]` should weaken “`μ(T)=2` when `h,k>0` are nonzero and distinct” to “a single chiral pair contributes two `C_6`-orbits” ([derivation-capsid.md:354-356](papers/biology-rung/derivation-capsid.md:354)).
- `[C.2]` should stop saying “three-step plan” anywhere until the section actually has three steps ([math-catalogue.md:347-349](papers/biology-rung/math-catalogue.md:347), [derivation-capsid.md:610-613](papers/biology-rung/derivation-capsid.md:610)).
- Derivation status line “Round 0 draft, pre-codex-review” is stale after the claimed round-0 fixes ([derivation-capsid.md:5](papers/biology-rung/derivation-capsid.md:5)).

**7. Top Three Fixes**
1. Fix the scope drift at the top level. The derivation opening and the WO executive summary/goals still promise a cell-level / `2I`-invariant operator, but the proved result is face-level only ([derivation-capsid.md:7-14](papers/biology-rung/derivation-capsid.md:7), [WO-BIOLOGY-RUNG-001-CAPSID.md:27-32](papers/biology-rung/WO-BIOLOGY-RUNG-001-CAPSID.md:27), [40-47](papers/biology-rung/WO-BIOLOGY-RUNG-001-CAPSID.md:40)).
2. Purge the residual false empirical `T=5` claim and stale `[N.2]` language. The worst offender is catalogue `[R.1]` (“no `T=5` capsids are observed”) ([math-catalogue.md:274-279](papers/biology-rung/math-catalogue.md:274)).
3. Repair `[C.2]` consistency and attribution. Do not claim a field-theoretic Paper XXXII domain that the cited source does not define, and make the open-problem status/plan consistent across §6, §8, and the catalogue ([derivation-capsid.md:452-455](papers/biology-rung/derivation-capsid.md:452), [576-583](papers/biology-rung/derivation-capsid.md:576), [math-catalogue.md:324-349](papers/biology-rung/math-catalogue.md:324)).

**8. Verdict**
Publication ready: no.
