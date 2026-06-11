**1. Claim Audit**
- `[D.1]` “`𝕊 := (ℤ[ω], A_5 ↷ 𝓕₂₀)`” is fine as a definition. The only soft spot is the next sentence, “`A Caspar–Klug subdivision is an A_5-equivariant choice...`”: that equivariance is not formally defined because no target `A_5`-action on subdivision data is specified. This is a wording defect, not a failure of later proofs. `derivation-capsid.md:112-125`
- `[L.0]` “`π_20 = 𝟏 ⊕ 𝟑 ⊕ 𝟑' ⊕ 𝟒^{⊕2} ⊕ 𝟓`” is plausible and standard, but the document does not actually prove it; “standard character-theoretic calculation” is a pointer, not an argument or citation. Because `[L.2]` only needs the irrep dimensions, this is not currently breaking the main theorem, but it is still under-justified. `derivation-capsid.md:165-171`
- `[D.2]` “`𝒯_casc(z):=z\bar z`” is a clean definition. `derivation-capsid.md:190-208`
- `[L.1]` “`spec(𝒯_casc)=` Loeschian numbers” is established only by reduction to the classical Eisenstein-norm fact. That is acceptable if treated as imported mathematics; it is not self-contained. `derivation-capsid.md:212-219`
- `[L.3]` “uniqueness under `C_6` symmetry” is actually proved. The matrix-centraliser argument is sufficient. `derivation-capsid.md:221-247`
- `[T.1]` “one face-level operator, unique up to positive scale, with CK spectrum” is established at exactly the stated face-level scope. The previous cell-level overclaim is gone. `derivation-capsid.md:257-277`
- `[R.1]` / `[L.2]` settling `T=5` is now mathematically sound: `5` is non-Loeschian; the `5`-dimensional irrep is representation-theoretic, not a T-value. `derivation-capsid.md:291-340`
- `[D.3]` “`μ(T)` = number of `C_6`-orbits” is fine as a definition, and the listed small values match the sim. The explanatory factorisation prose below it is not a proved classification theorem and should not read like one. `derivation-capsid.md:361-430`
- `[C.1]`, `[C.3]`, `[C.4]` are all clearly marked conjectural/speculative. No overclaim remains there. `derivation-capsid.md:433-476,616-630`
- `[C.2]` is now honestly posed as an open problem. The attribution split between Paper XXXII §4 and `cascade-foundations.md §F2` is materially corrected. `derivation-capsid.md:482-614`
- `[N.1]` is supported by the existing artefacts: `data/wo1_prediction.csv` has 36 distinct `T` values and 61 rows/orbits, and includes `μ(91)=4`. `derivation-capsid.md:664-671`, `data/wo1_prediction.csv:1-62`
- `[N.2]` is not established, but the document now says exactly that. `derivation-capsid.md:673-679`

**2. WO Acceptance Audit**
- AC1: resolved, subject to this round’s verdict. `WO-BIOLOGY-RUNG-001-CAPSID.md:141-142`
- AC2: resolved. Every D/L/T/C/N in the derivation is catalogued. `WO...:143-144`
- AC3: not resolved. `wo1_compare.py` is absent; no end-to-end pipeline exists. `WO...:145`, repo check
- AC4: not resolved. No VIPERdb comparison artefact exists, so no hit/partial/miss has been recorded. `WO...:146-149`
- AC5: resolved. `T=5` is settled explicitly and correctly. `WO...:150`, `derivation-capsid.md:291-340`
- O1: partially resolved. It is now explicitly open, with a concrete four-step plan. `WO...:115`, `derivation-capsid.md:482-614`
- O2: resolved. `T=5` is excluded mathematically. `WO...:116`, `derivation-capsid.md:291-340`
- O3: resolved. The derivation now states clearly that face-level action is `A_5`, with `2I` deferred to chirality/cell-level discussion. `WO...:117`, `derivation-capsid.md:173-184`
- O4: partially resolved. A conjectural chirality-bias statement exists; no evidence yet. `WO...:118`, `derivation-capsid.md:452-476`
- O5: not touched. There is no de-biased VIPERdb analysis because there is no VIPERdb analysis at all. `WO...:119`

**3. Catalogue Audit**
- No missing catalogue objects: `[D.1]`, `[D.2]`, `[D.3]`, `[L.0]`, `[L.1]`, `[L.2]`, `[L.3]`, `[T.1]`, `[C.1]`, `[C.2]`, `[C.3]`, `[C.4]`, `[N.1]`, `[N.2]` all appear in `math-catalogue.md`.
- No obvious spurious D/L/T/C/N entries in the catalogue lack a counterpart in the derivation.
- Status labels are now aligned with the derivation: `[C.2]` open, `[N.1]` computational, `[N.2]` not implemented.

**4. Attribution / External Consistency**
- `cascade-bio.md §B3.1` really does write `ω = e^{2πi/3}` while also writing `|h+kω|² = h²+hk+k²`; the derivation is right to call this a notation mismatch. `cascade-bio.md:259-263`
- `cascade-bio.md §B3.2` really does contain the bad `T=5 ↔ A_5 5-dim irrep` table entry and the “four smallest ... 1,3,4,5” overclaim. The correction in `[R.1]/[L.2]` is accurate. `cascade-bio.md:278-297`
- `cascade-bio.md §B3.4` really does mark “Full derivation of all T-numbers from one cascade operator” as open. `cascade-bio.md:314-320`
- `cascade-bio.md §3.1` really does place biology at the cell level. `cascade-bio.md:198-201`
- `cascade-bio.md §3.2` really does treat the `15 × 40` Hopf structure as a candidate/conjectural target, not a theorem. `cascade-bio.md:149-160,205-214,450-451`
- `cascade-bio.md §2.1–2.3` supports the `2I`/`A_5` substrate statements. `cascade-bio.md:43-70`
- `cascade-bio.md §2.7` does make the chirality/L-amino-acid claim the derivation says it is extending. `cascade-bio.md:162-180`
- `paper-xxxii.tex §3` around line 237 does state `thm:600cell` with `(H1)-(H4)` selecting `2I`. `paper-xxxii.tex:237-279`
- `paper-xxxii.tex §4` around line 363 does state Theorem F, with A1 continuity, A2 sharp limit, A3 extensivity; permutation symmetry of `R` is in the class definition, not in A1-A3. The corrected paraphrase is now accurate. `paper-xxxii.tex:340-405`
- `cascade-foundations.md §F2` does state the density-level form `F[Φ]=∫(αR+βE−γQ)dV` under locality/invariance/order-≤2/scalar assumptions. `cascade-foundations.md:91-155`

**5. Sim Correctness**
- The supplied sim correctly implements the face-level mathematical claim it says it implements: `T(h,k)=h²+hk+k²`, `ω:(h,k)↦(-k,h+k)`, `C_6`-orbit enumeration, and per-orbit chirality classification. `wo1_capsid_predict.py:36-160`
- The existing CSV matches the stated `[N.1]` summary: 36 Loeschian `T ≤ 100`, 61 `C_6`-orbits, `μ(49)=3`, `μ(91)=4`. `data/wo1_prediction.csv:1-62`
- There is no χ² / KL / null-hypothesis code yet. That part of the WO is simply absent, not incorrectly implemented. `wo1_compare.py` does not exist; `wo1_viperdb_observed.csv` does not exist.
- I could run the predictor under `python3` far enough to verify the printed counts and checks; it then failed only because this review environment is read-only on writes. That is an environment constraint, not a scientific defect.

**6. Tightness**
- `derivation-capsid.md:7-13`: “cascade operator” is rhetorically stronger than the proof. Safer: “the classical Eisenstein norm, singled out at face level by `C_6` symmetry.”
- `derivation-capsid.md:123-129`: replace “`A_5`-equivariant choice” with “a coherent choice replicated across all faces, up to unit ambiguity.”
- `derivation-capsid.md:391-418`: the factorisation discussion should either be proved or marked as heuristic/explanatory, not half-stated as a rule.

**7. Top Three Fixes**
1. Add an actual proof or citation for `[L.0]` in `derivation-capsid.md:165-171`. Right now a standard fact is being used without either.
2. Remove or formalise “`A_5`-equivariant choice” in `derivation-capsid.md:123-125`. As written, it gestures at structure that has not been defined.
3. Demote the norm-factorisation narrative in `derivation-capsid.md:391-418` to heuristic prose unless you are prepared to prove it.

**8. Verdict**
- Publication ready: yes.

That verdict is on the narrow gate you specified: substantive math / attribution / sim-correctness must-fix items. The two Round-4 blockers are fixed, and I do not see a new blocker in those categories. The WO itself is still incomplete: AC3-4 and O5 remain open because the VIPERdb comparison pipeline is not built.
