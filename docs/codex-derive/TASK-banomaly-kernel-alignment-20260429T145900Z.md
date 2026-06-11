Read-only pass completed. I did not edit files or commit.

**SECTION A. Insight / External Content Relevance**

Already in cascade papers/docs:

- `C_\varphi = L_M+\varphi^{-2}I` is already canonical in `docs/aria-closure-kernel.md:12-20`; the 600-cell substrate and 9-shell structure are at `:37-47`; the rank-6 compression claim is at `:49-55`.
- The stale single-dataset b-anomaly framing is `docs/aria-closure-kernel.md:57-73`, with the cocycle bridge at `:75-82`.
- `adaptive-closure-transport.tex` already has the passive/active split: passive `G\equiv0` at `:164-174`, active `G\not\equiv0` at `:184-202`, selection hypotheses at `:214-228`, edge-space caveat at `:244-260`, and the stale “external, unaudited” b-anomaly witness at `:401-419`.
- The RH/prime spine already has the κ bridge: `docs/rh-cascade-closure-dynamics.md:56-86`; and its own scope caveat that ẑ is not classical RH is explicit at `:204-224` and `:236-242`.
- `docs/fractal-cascade-projection.md` already reads ẑ as κ-compression trace at `:134-149`, and keeps the God Prime fixed-point refinement scoped at `:168-240`, with honest scope at `:268-275`.
- `docs/projection-narrative.md` already defines the Layer 1 / Layer 2 order at `:7-20`, and currently treats ARIA as the empirical landing at `:70-79`.

Only in shipped b-anomaly repo / external to cascade repo:

- Headline claim: one fixed kernel, no fitted shape parameters, five public datasets, one amplitude per dataset: `README.md:12-15`.
- Verbatim table numbers: `README.md:16-22`. Same table appears in paper §6 at `paper/sections/06_cross_dataset.tex:55-60`.
- Honest caveats: AIC tie `w_VFD=0.348` vs `w_FREE_C9=0.652`, free-width Gaussian proxy, and Mode-B `+2.77` AIC drift: `README.md:30-35`; detailed AIC stack at `06_cross_dataset.tex:102-125`; Mode-B drift at `04_results.tex:85-112`.
- Geometry-first variant test: `README.md:28`; detailed table at `03_derivation.tex:151-198`.
- Cross-channel basis effect: README says `~2.2` with residual overshoot at `README.md:27`; detailed section gives predicted `+2.5` vs observed `+4.98`, factor `~2` remaining gap at `07_cross_channel.tex:129-165`.

Only in `insight.md` or adjacent prior-session material:

- E8 double-cover / two-600-cell interpretation for the factor 2 is in `insight.md:47-64` and `:176-200`. Relevant only as interpretive background; do not use it to strengthen b-anomaly.
- QMS-3 / God-prime / Fano-triad bridge is in `insight.md:670-717`. Relevant to future prime-locus work, not to this alignment.
- Prime closure-locus map `L : F-Irr(...) -> V(600-cell)/H4` is proposed at `insight.md:652-657`; it is not a b-anomaly bridge.
- Pentagonal holonomy proposal is in `insight.md:830-893`. It is partly formalised already in `docs/pentagonal-torsion-derivation.md`, especially the required cocycle build at `:255-280` and weighted zeta route at `:293-325`.

Classical literature routes already cited locally:

- Cyclotomy / Washington route: `docs/pentagonal-torsion-derivation.md:72-101`.
- Elkies / icosian lift: `docs/pentagonal-torsion-derivation.md:166-174`.
- Neukirch adelic compactness route: `docs/pentagonal-torsion-derivation.md:445-453`.
- Lyapunov / Lojasiewicz-Simon route: `adaptive-closure-transport.tex:226-228`, bibliography `:493-515`.

**SECTION B. Priority Gaps / Builds**

B1. Phase 1, `docs/aria-closure-kernel.md:57`  
Object: empirical-witness table  
Type: map from five datasets to `(n, non-linear ΔAIC, A, ΔC9_eff)`  
Bridges: stale single-dataset `r=0.983` witness to shipped 5-dataset structural test.  
Route: shipped b-anomaly README / paper §6.  
First edit: replace §4 lines `57-82` with a section headed:

`## 4. Empirical validation: shipped b-anomaly passive-regime witness`

Include the exact table from `README.md:16-22`:

| dataset | decay | n | non-linear ΔAIC | best-fit A | ΔC9eff |
|---|---:|---:|---:|---:|---:|
| LHCb 2015 | B0 -> K*0 | 32 | -0.24 | +1.24 | -0.96 |
| LHCb 2021 | B+ -> K*+ | 32 | +0.17 | +2.06 | -1.59 |
| CMS 2025 no P4' | B0 -> K*0 | 18 | +0.47 | +1.05 | -0.81 |
| LHCb 2025 | B0 -> K*0 | 32 | +1.09 | +1.14 | -0.86 |
| LHCb 2015 | Bs -> phi, S-basis | 24 | -0.24 | +4.98 | -3.85 |

Must also state: structural pass, not AIC preference; `w_VFD=0.348`, `w_FREE_C9=0.652`; Mode-B drift `+2.77`; free Gaussian proxy comparable. Discharges AC1, AC2, AC5.

B2. Phase 1, `docs/aria-closure-kernel.md:120`  
Object: regime-status map  
Type: `{response, selection} -> {shipped passive witness, active build target}`  
Bridges: b-anomaly passive response to ACT selection distinction.  
Route: ACT passive definition plus b-anomaly shipped repo.  
Replacement content: keep selection as the named build, but change the top paragraph to:

“The closure response primitive now has a shipped passive-regime empirical landing: the b-anomaly paper tests the fixed \(C_\varphi\)-derived \(V_{600}\) kernel without shape retuning across five public flavour-physics datasets. This does not close the selection layer. The active-regime companion remains the ARIA / aria-chess selection paper: a learning-rule / Lyapunov / coherence-descent construction for \(W\)-space, not supplied by the b-anomaly analysis.”

Discharges AC3, AC4, AC6.

B3. Phase 1, `docs/aria-closure-kernel.md:147`  
Object: canonical-source pointer  
Type: bibliography/register update  
Bridges: old WO007/WO008 reports to primary shipped paper.  
Route: b-anomaly `paper/main.pdf` as primary; WO007/WO008 as support.  
First edit: add primary reference before old WO refs:

`- /mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/paper/main.pdf — primary shipped passive-regime empirical witness for the fixed \(C_\varphi\)-derived \(V_{600}\) kernel; five-dataset sign-uniform structural test with honest AIC tie.`

B4. Phase 2, `papers/adaptive-closure-transport/adaptive-closure-transport.tex:401`  
Object: passive-witness paragraph  
Type: interpretive non-load-bearing replacement  
Bridges: ACT passive regime `G\equiv0` to b-anomaly.  
Route: no theorem change; documentation alignment.  
Replace the stale “reported external, unaudited” paragraph at `:401-419` with:

“The response field \(\psi=C_\varphi^{-1}f\) is a programme-level ansatz / explicitly computable operator. In the passive regime \(G\equiv0\), this response primitive now has a shipped flavour-physics witness: the b-anomaly paper tests the fixed \(V_{600}\) shell-mean kernel \((L_{V_{600}}+\varphi^{-2}I)^{-1}f\) across five public \(b\to s\mu\mu\) angular datasets with one amplitude \(A\) per dataset and no shape retuning. The witness is structural: \(A>0\) and \(\Delta C_9^{eff}<0\) in 5/5 fits, while Akaike comparison remains an honest tie / mild FREE_C9 preference.”

B5. Phase 2, `adaptive-closure-transport.tex:421`  
Object: selection-scope lemma  
Type: paragraph replacement  
Bridges: b-anomaly response vs ACT active selection.  
Route: ACT hypotheses, not b-anomaly data.  
Add after B4:

“The b-anomaly witness is passive-regime evidence for the response operator only. It does not verify the active-regime learning rule \(G\), the Lyapunov potential \(V(W)\), the edge-space decomposition of \(\mathbb R^{E_M}\), or full coupled-system convergence. The active-regime empirical target remains the aria-chess companion paper.”

Discharges AC4, AC6.

B6. Phase 2, `papers/realisation/realisation.tex:68`  
Object: Layer-1 empirical register item  
Type: new bullet  
Bridges: realisation Layer 1 to flavour physics.  
Route: b-anomaly README / paper.  
Insert after H4-Coxeter bullet:

`\item B-anomaly kernel paper~\citep{SmartBAnomaly}: fixed \(V_{600}\) response kernel for \(b\to s\mu^+\mu^-\) angular data; five public datasets, no kernel-shape retuning, \(A>0\) and \(\Delta C_9^{eff}<0\) in 5/5 fits, with stacked Akaike weight \(w_{\mathrm{VFD}}=0.348\) vs \(w_{\mathrm{FREE\_C9}}=0.652\).`

Also add BibTeX-style entry near `realisation.tex:345`.

B7. Phase 2, `papers/cascade-derivation/cascade-empirical-grounding.md:11`  
Object: E3 classifier extension  
Type: new subsection  
Bridges: aria E3 cognitive witnesses to b-anomaly passive-regime witness.  
Route: evidence taxonomy already at `:11-22`.  
Insert new §0.1:

`#### 0.1 Flavour-physics passive-regime witness`

State: b-anomaly is Class-E3 for the passive \(C_\varphi\) response kernel, not for active selection, not for RH, not for aria-chess cognitive substrate.

B8. Phase 3, `docs/rh-cascade-closure-dynamics.md:141`  
Object: operator-level inheritance map  
Type: `C_phi witness -> κ cocycle -> ẑ substrate`  
Bridges: b-anomaly to prime-object spine without RH overclaim.  
Route: shared κ only.  
Insert subsection:

“Independent passive-regime witness for the shared kernel. The b-anomaly paper empirically tests the same \(V_{600}\), \(C_\varphi\), shell/cocycle infrastructure used here. The inheritance is operator-level only: it strengthens confidence in the shared closure-response kernel and κ grading, not in classical RH and not in any claim that \(\widehat\zeta\) is witnessed by flavour data.”

B9. Phase 3, `docs/fractal-cascade-projection.md:134`  
Object: κ-compression witness note  
Type: explanatory paragraph  
Bridges: κ trace to b-anomaly.  
Route: Route Q-min κ already in file.  
Add after the κ-compression trace paragraph:

“The same radial grade \(\kappa(v)=(s(v)-4)^2\) now has an independent passive-regime empirical landing through the b-anomaly kernel. This supports the κ-compression operator as shared programme infrastructure; it does not alter the document’s scope boundaries on classical RH, A/B σ-fixed vs σ-paired structure, or the God Prime selection-restricted fixed-point theorem.”

B10. Phase 3, `docs/projection-narrative.md:15` and `:70`  
Object: empirical-landing register  
Type: new Layer-1 bullet and short empirical-landing paragraph  
Bridges: flavour physics into Layer 1 without replacing ARIA.  
Route: b-anomaly README.  
Add bullet after H4-Coxeter:

`- B-anomaly kernel paper — fixed \(V_{600}\) response kernel across five public \(b\to s\mu\mu\) angular datasets; sign-uniform structural pass with honest AIC tie against FREE_C9.`

At `:70`, add before ARIA paragraph:

“Separate from ARIA’s cognitive-substrate programme, the passive \(C_\varphi\) response kernel now has a flavour-physics empirical landing through the shipped b-anomaly paper. This strengthens Layer 1 reach; it is not a realisation proof and it does not deliver the active selection layer.”

**SECTION C. Reversals / Corrections**

- At any new edit, replace `five LHCb datasets` with `five public datasets covering LHCb and CMS, two isospin partners, and three decay channels`. The task wording at `TASK-banomaly-kernel-alignment.md:68` says “5 LHCb datasets,” but the README says two collaborations at `README.md:14`.
- At `docs/aria-closure-kernel.md:57`, replace `Empirical validation: LHCb $B^0\to K^{*0}\mu\mu$` with `Empirical validation: shipped five-dataset b-anomaly structural test`.
- At `adaptive-closure-transport.tex:415`, replace `a reported external, unaudited empirical witness ($r \approx 0.98$ ... ) lives in the separate ... repository and is not verified here` with `a shipped passive-regime flavour-physics witness lives in the b-anomaly repository and is summarised here only as non-load-bearing programme context`.
- Avoid the standalone phrase `~50% residual overshoot` unless quoting README. Safer hostile-review wording: `README summarises a residual overshoot; the detailed cross-channel section reports predicted +2.5 vs observed +4.98, a factor ~2 remaining gap`.

**SECTION D. Alternative Routes**

Route Q, use now: existing Route Q-min κ. This is the alignment route. It uses \(C_\varphi\), \(V_{600}\), shell grade \(\kappa(v)=(s(v)-4)^2\), and the shipped b-anomaly witness. No new theorem required.

Route K, do not use for this edit: pentagonal holonomy connection. `insight.md:878-882` proposes \(\omega:E(V_{600})\to\mathbb Z[\varphi]^\times\); `docs/pentagonal-torsion-derivation.md:255-280` already names the cocycle proof obligations. This is a future derivation route for a stronger local-frame operator, not a source for current b-anomaly claims.

Route L, do not use for this edit: prime closure-locus map \(L\). `insight.md:652-657` and `:682-717` tie it to God Prime/QMS-3. Relevant to future prime-spine work, not to b-anomaly kernel alignment.

**SECTION E. Top-3 Risk Register**

1. AIC drift into preference language.  
Guard: always pair “5/5 sign-uniform structural pass” with `w_VFD=0.348` vs `w_FREE_C9=0.652` and “statistically indistinguishable / mild FREE_C9 preference.”

2. RH / ẑ over-inheritance.  
Guard: say “operator-level κ/Cφ support only.” Do not say b-anomaly witnesses ẑ, RH, prime structure, or the critical line.

3. Dataset and cross-channel numerical drift.  
Guard: use README table verbatim for headline numbers; use “five public datasets,” not “five LHCb datasets”; if discussing cross-channel amplitude, cite both `~2.2` basis factor and the detailed `+2.5` vs `+4.98` residual.

**SECTION F. Top 3 Next Builds**

1. `docs/aria-closure-kernel.md:57` + `adaptive-closure-transport.tex:401`  
Replace stale single-dataset / unaudited framing with shipped passive-regime b-anomaly witness. This is the highest-risk stale wording.

2. `papers/cascade-derivation/cascade-empirical-grounding.md:11` + `papers/realisation/realisation.tex:68`  
Add b-anomaly as Class-E3 passive-regime flavour witness, distinct from aria-chess cognitive E3. This prevents empirical-credit bleed.

3. `docs/rh-cascade-closure-dynamics.md:141` + `docs/fractal-cascade-projection.md:134`  
Add the κ/Cφ operator-level bridge with explicit “not RH, not ẑ empirical witness” guard. This closes the prime-spine alignment without over-claim drift.
