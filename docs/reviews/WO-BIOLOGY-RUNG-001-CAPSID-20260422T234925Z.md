**1. Claim Audit**
- `"[D.1] The face-level icosahedral Eisenstein substrate is the pair 𝕊 := (ℤ[ω], A_5 ↷ 𝓕₂₀)"` at `papers/biology-rung/derivation-capsid.md:83`. As a definition, fine. The added prose at `:96-99` about an "`A_5`-equivariant choice" across faces is still informal: no face-chart/gluing data is defined, so that part is not a formal construction.
- `"[L.0] π_20 = 𝟏 ⊕ 𝟑 ⊕ 𝟑' ⊕ 𝟒^{⊕2} ⊕ 𝟓"` at `derivation-capsid.md:138`. Established modulo the standard character calculation it cites. No over-claim here.
- `"[D.2] 𝒯_casc(z) := z·z̄ = |z|²"` at `derivation-capsid.md:163`. Fine as a definition.
- `"[L.1] spec(𝒯_casc) = {Loeschian numbers}"` at `derivation-capsid.md:185`. The argument is standard and sufficient, but the document still has a notation error in the opening recap: `ω = exp(2πi/3)` is paired with `h²+hk+k²` at `:37-47`. With that `ω`, the norm is `h²-hk+k²`. Later sections switch to `ω = e^{iπ/3}`. Fix the opening or this lemma is stated against inconsistent notation.
- `"[L.3] Then Q = c·𝒯_casc for some c>0"` at `derivation-capsid.md:194`. Established. The matrix argument is enough.
- `"[T.1] ... face-level operator ... whose spectrum is exactly the sequence of Caspar–Klug T-numbers"` at `derivation-capsid.md:230`. Established at face level only. The scope is now mostly honest.
- `"[R.1] ... T=5 entry is misleading"` at `derivation-capsid.md:264`. Established on mathematical grounds.
- `"[L.2] ... overlap = {1,3,4}"` at `derivation-capsid.md:291`. Established.
- `"[D.3] μ(T) := # {C_6-orbits ...}"` at `derivation-capsid.md:333`. The definition is fine. The sample values at `:356-360` are computationally supported by the sim/CSV. The explanatory prose at `:374-379` about factorisations “contributing” orbit structure is heuristic, not proved.
- `"[C.1] Z(T) ∝ μ(T)·exp(-β·c(T))"` at `derivation-capsid.md:398`. Conjecture only. The derivation does not test it, despite catalogue wording to the contrary.
- `"[C.3] ... predicts a small but nonzero empirical asymmetry"` at `derivation-capsid.md:417`. Pure conjecture. The added claim that VIPERdb records chirality “for many species” at `:435-437` is unsupported in this repo.
- `"[C.2] Does 𝒯_casc descend ... ?"` at `derivation-capsid.md:443`. Correctly left open. But the document is internally inconsistent: §6 says four-step plan (`:497-522`), the carried-forward table agrees (`:632`), then the summary regresses to “three-step plan” at `:668`.
- `"[C.4] ... a T=3 capsid should exhibit a discrete structural feature"` at `derivation-capsid.md:572`. Speculative only, and labelled as such.
- `"[N.1] ... 36 Loeschian T-values ≤100, 61 distinct C_6 orbits ... μ(91)=4"` at `derivation-capsid.md:609`. Supported by `papers/biology-rung/scripts/wo1_capsid_predict.py`, `papers/biology-rung/data/wo1_prediction.csv`, and spot-check execution.
- `"[N.2] ... emitted to data/wo1_comparison.md by scripts/wo1_compare.py"` at `derivation-capsid.md:618`. Not established. `papers/biology-rung/scripts/wo1_compare.py` is missing.

**2. WO Acceptance Audit**
- AC1 `derivation-capsid.md passes codex review ... yes` at `WO-BIOLOGY-RUNG-001-CAPSID.md:141`. Not resolved. Current answer is `no`.
- AC2 `math-catalogue.md lists every D/L/T/C/N ... provenance and status filled in` at `WO...:143`. Partially resolved. Coverage is good; statuses are not.
- AC3 `Sim runs end-to-end: prediction → VIPERdb fetch → comparison` at `WO...:145`. Partially resolved. Prediction sim exists; fetch script exists; comparison script is missing.
- AC4 `Comparison result is recorded honestly` at `WO...:146`. Not touched.
- AC5 `T=5 question is settled explicitly` at `WO...:150`. Resolved.

- O1 `Is 𝒯_casc a restriction of F ... or a new object?` at `WO...:115`. Partially resolved: reframed honestly as open problem with plan, not answered.
- O2 `T=5 ... which is right?` at `WO...:116`. Resolved: excluded from `spec(𝒯_casc)`; 5-dim irrep reinterpreted.
- O3 `2I vs A_5 ... which equivariance?` at `WO...:117`. Resolved enough for current scope: face action is `A_5`, `2I` deferred to chirality/open-problem context.
- O4 `Laevo/dextro chirality weighting` at `WO...:118`. Partially resolved only as conjecture.
- O5 `VIPERdb coverage bias` at `WO...:119`. Not touched.

**3. Catalogue Audit**
- Coverage: all labelled derivation objects `D.1, D.2, D.3, L.0, L.1, L.2, L.3, T.1, R.0, R.1, R.2, C.1, C.2, C.3, C.4, N.1, N.2` appear in `papers/biology-rung/math-catalogue.md`.
- Defect: `C.1` says `Status. Conjectured; tested against VIPERdb.` at `math-catalogue.md:329`. False. `N.2` is still pending and `wo1_compare.py` does not exist.
- Defect: `N.1` says the sim is present and ran successfully at `math-catalogue.md:432-445`, then marks status as `Computational (pending sim run)` at `:447`. Self-contradiction.
- Defect: `N.2` claims `scripts/wo1_compare.py` emits comparison output at `math-catalogue.md:453-457`. That artefact is not in the repo.

**4. Attribution / External Consistency**
- Fixed correctly: the distinction between Paper XXXII’s point-wise `F_ε^V : M → ℝ` and the density functional `F[Φ] = ∫(αR+βE−γQ)dV` is now right. `paper-xxxii.tex:363-389` supports the point-wise theorem; `cascade-foundations.md:99-155` supports the density form.
- Fixed correctly: the source of the open item `"Full derivation of all T-numbers from one cascade operator"` is exactly `cascade-bio.md:312-320`.
- Fixed correctly: the misleading `T=5 ↔ A_5 5-dim irrep` table entry is indeed in `cascade-bio.md:274-291`.
- Still wrong: `derivation-capsid.md:72-77` states the 600 tetrahedral cells are “partitioned into 15 Hopf-fibre classes of 40 cells each.” The cited source does not establish that; it calls it a “conjectured” fibration and “structural candidate” at `cascade-bio.md:149-159`.
- Same overreach again: `derivation-capsid.md:505-511` treats the Hopf cell-fibre structure as available input for the `C.2` plan. The source at `cascade-bio.md:205-206` only says each fibre “carries” 40 cells within a candidate picture, not that the full projection machinery exists.

**5. Sim Correctness**
- The predictor implements the face-level claim it says it implements: `T(h,k)=h²+hk+k²`, `C_6` via `(h,k)↦(-k,h+k)`, per-orbit counting, and per-orbit chirality labels.
- The round-2 spot-check passes: `μ(91)=4`. The generated CSV has four `T=91` rows, and the diagonal cases `T=3,12,27,48,75` are all marked `achiral`.
- The CSV is now correctly per-orbit, not per-`T`, and the diagonal `h=k` cases are labelled correctly.
- But the sim does not implement the full WO computational claim. It does not compute `Z(T)`, does not perform χ²/KL comparisons, and the claimed `wo1_compare.py` does not exist.
- Minor but real artefact inconsistency: the predictor docstring at `wo1_capsid_predict.py:12-19` still describes an older CSV shape and extra output file that the code no longer produces.

**6. Tightness**
- `derivation-capsid.md:37`: replace `ω = exp(2πi/3)` with `ω = exp(iπ/3)`, or change the vector convention so the plus-sign norm formula is actually true.
- `derivation-capsid.md:72`: replace `partitioned into 15 Hopf-fibre classes` with `conjecturally partitioned into 15 Hopf-fibre classes`.
- `derivation-capsid.md:668`: replace `three-step plan` with `four-step plan`.
- `derivation-capsid.md:592`: do not say `scripts/wo1_compare.py` “then tests” anything until that file exists.

**7. Top Three Fixes**
1. Fix the Eisenstein-root convention in the opening recap at `papers/biology-rung/derivation-capsid.md:33-47`. Right now the stated `ω` and stated norm formula do not match.
2. Downgrade the Hopf `15×40` structure from fact to conjectural/candidate everywhere it is imported from `cascade-bio.md`, especially `derivation-capsid.md:72-77` and `:505-511`.
3. Remove unbacked empirical/comparison claims until the artefacts exist: `derivation-capsid.md:592-624` and `math-catalogue.md:319-330,432-460`. In particular, `wo1_compare.py` is missing, `N.2` is unbacked, and `C.1` has not been tested.

**8. Verdict**
Publication ready: no.
