**Claim Audit**
Round 3 fixes landed cleanly: status is downgraded at `docs/aria-closure-kernel.md:3-6`; geometry-first history is caveated at `98-106`; family membership is explicitly unproved at `158-162`; “strongest evidence” is now only “programme-level indication” at `229-232`.

- “`C_\varphi = L_M + \varphi^{-2}I`” and “`C_\varphi` is positive definite” (`13-26`): definition is fine, but the positivity/smooth/non-oscillatory language needs hypotheses: self-adjoint nonnegative Laplacian, connected standard graph/continuum operator, and nonnegative localized source. As written it overgeneralises “graph, simplicial complex, or projected coordinate.”
- “`G(x)=\varphi/2 e^{-|x|/\varphi}`” (`30-36`): established for the free-space operator on `R` with decay at infinity. Needs that domain assumption stated.
- 600-cell facts: 120 vertices, 720 edges, 12-regular, 9 shells (`40-45`): locally supported by b-anomaly `reports/wo009_full_lift.md:13-32`.
- “`λ=9`, multiplicity 6 — rank-6 spectral sector” (`50-56`): **not established; likely wrong as stated.** Local canonical spectrum gives `9^{16}` (`papers/millennium-rh-formal/rh-formal.tex:1768-1770`; `papers/millennium-ym/ym-mass-gap.tex:871-879`). Worse, b-anomaly’s own `archive/reports/wo011_spectral.csv:10-15` shows the 6-mode jump at `lambda_max_used = 5.527864...`, not 9. The b-anomaly prose repeats the `λ=9, multiplicity 6` claim, but the CSV contradicts it. Must fix.
- Five-dataset table (`74-83`): supported verbatim by b-anomaly `README.md:16-22`.
- Universality/sign-uniformity (`86-91`): supported by b-anomaly `README.md:24-28` and paper `06_cross_dataset.tex:196-208`; caveats are present.
- Cross-channel ratio (`92-97`): the `+2.5` vs `+4.98`, factor `~2` gap is supported by `07_cross_channel.tex:129-165`, not by `README.md:24-28` alone. Attribution line `84` is too narrow.
- Geometry-first variant test (`98-106`, `125-143`): supported by `reports/wo016b_variant_geometry.md:3-14` and historical caveat by `09_limitations.tex:29-38`.
- AIC/statistical caveats (`108-123`): supported by `README.md:30-35`, `06_cross_dataset.tex:92-126`, and `04_results.tex:85-112`.
- Cocycle convergence/operator-level inheritance (`145-154`): carefully scoped; supported by RH `def:kappa` at `rh-formal.tex:752-768`. The word “inherits” is still slightly strong; the actual established content is shared substrate/shell-grade context, not support for zeta claims.
- Programme family membership (`158-192`): now correctly programme-positioned, not proved. RH/NS/BSD/Hodge/PNP local files support only this weak status.
- Response vs selection (`196-235`): established as a scope statement. Active regime remains open; no b-anomaly-to-RH overclaim.

**WO Acceptance Audit**
- AC1 (`TASK...md:76`): partially resolved. The b-anomaly fit numbers are verbatim. The spectral `λ=9, multiplicity 6` numerical claim is not cleanly supported.
- AC2 (`78-83`): resolved for empirical b-anomaly claims. No AIC preference or uniqueness claim is made.
- AC3 (`84`): resolved. ẑ/RH are not empirically claimed.
- AC4 (`86`): resolved. Active-regime selection remains open and aria-chess is named as not written.
- AC5 (`88`): partially resolved. Most b-anomaly paragraphs survive. The spectral-compression attribution does not.
- AC6 (`90`): resolved. The note is explicitly non-load-bearing.

Open items not in scope (`94-99`): aria-chess draft not touched; edge-space decomposition not addressed; Lyapunov derivation not addressed; b-anomaly repo itself not edited. That matches scope.

**Catalogue Audit**
No math-catalogue artefact was supplied for this WO. Existing catalogues found are unrelated (`biology-rung`, `h-grad-1`, `observer-zeta`). If this WO requires a ledger, then the definition-like objects in `docs/aria-closure-kernel.md:13-26` and numerical claims in `50-56`, `74-83`, `125-143` are uncatalogued.

**Attribution / External Consistency**
Supported: b-anomaly table/stat caveats; variant table; limitations caveat; RH `def:kappa`; programme-positioned family references.

Defect: `docs/aria-closure-kernel.md:50-56` imports a spectral claim that conflicts with local full-spectrum references and b-anomaly’s own CSV output. This is the substantive attribution failure.

Residual repo drift: some Millennium closing subsections still contain stale single-dataset `r≈0.98` b-anomaly language, e.g. `rh-formal.tex:2785-2789` and `ns-formal.tex:807-810`. Not in the reviewed derivation’s main claim chain, but not repository-wide aligned.

**Sim Correctness**
No sim artefact was supplied with this WO. I did inspect b-anomaly generated reports where relevant; I did not rerun simulations.

**Tightness**
- `docs/aria-closure-kernel.md:50-56`: replace the spectral claim or remove it until WO-011 is reconciled.
- `docs/aria-closure-kernel.md:23-26`: add “for standard self-adjoint nonnegative Laplacians and nonnegative localized sources.”
- `docs/aria-closure-kernel.md:84`: change source note to “README plus paper §§6-7” for cross-channel details.
- `docs/aria-closure-kernel.md:151-153`: “ẑ shares operator-level infrastructure” is tighter than “ẑ inherits support.”

**Top Three Fixes**
1. `docs/aria-closure-kernel.md:50-56`: fix the false/unsupported `λ=9`, multiplicity-6 compression statement.
2. `docs/aria-closure-kernel.md:23-26`: state hypotheses for positivity, smoothness, centering, and non-oscillation.
3. `docs/aria-closure-kernel.md:84-97`: correct attribution for the cross-channel factor claim.

**Verdict**
Publication ready: no. The Round 3 fixes landed, but the spectral-compression claim is a substantive math/attribution must-fix.
