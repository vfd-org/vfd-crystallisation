**1. Claim Audit**

- `docs/aria-closure-kernel.md:14-25` defines `C_\varphi = L_M + \varphi^{-2}I` and says it is positive definite, smooth, centred, non-oscillatory. This is only true under unstated assumptions: `L_M` must be a self-adjoint nonnegative Laplacian and the source/domain/boundary conditions must be compatible. As written, the definition is fine; the qualitative regularity claim is under-specified.

- `docs/aria-closure-kernel.md:29-35` gives the continuum Green’s function `G(x)=φ/2 e^{-|x|/φ}`. Correct for the full-line operator `-d²/dx² + φ^{-2}` with decaying boundary condition. The document should say full-line/free-space; otherwise boundary dependence is hidden.

- `docs/aria-closure-kernel.md:49-55` claims rank-6 compression projecting to rank-1 observable. This is not proved in the note. It is backed in the b-anomaly derivation only as a spectral diagnostic: single isotypic block at `λ=9`, multiplicity 6, with full Green response still used in fits (`paper/sections/03_derivation.tex:200-209`). “Rank-1 observable” needs its projection map stated.

- `docs/aria-closure-kernel.md:73-82` five-dataset table: numerically verbatim against `vfd-b-anomaly/README.md:16-22`. Pass.

- `docs/aria-closure-kernel.md:85-102` universality, sign uniformity, cross-channel, variant test: broadly supported by `README.md:24-28`, `paper/sections/06_cross_dataset.tex:55-70`, and `paper/sections/07_cross_channel.tex:129-165`. Cross-channel wording should stay cautious: the paper says factor-2 residual remains.

- `docs/aria-closure-kernel.md:106-119` AIC/statistical caveats: numbers are correct, but line 110 says “Mild FREE_C9 preference.” That violates the WO’s “tie, not preference” discipline even though the source paper sometimes uses “mild preference.” For this alignment task, use “statistically indistinguishable.”

- `docs/aria-closure-kernel.md:121-132` cocycle convergence overclaims. The shipped b-anomaly headline kernel uses the unweighted full-graph Green response; the φ-cocycle edge-weighted variants are tested and lose (`paper/sections/03_derivation.tex:151-198`; `reports/wo009_full_lift.md:122-138`). So b-anomaly supports the `V_600 + φ^{-2}` response operator and shell-grade infrastructure, not empirical strengthening of the κ cocycle as an operative weight. This also affects `docs/rh-cascade-closure-dynamics.md:145-157`, `docs/fractal-cascade-projection.md:151-161`, and `cascade-empirical-grounding.md:32`.

- `docs/aria-closure-kernel.md:136-168` family-membership claims are explicitly declared programme-proposed and unproved. Acceptable as non-load-bearing context, not as theorem.

- `docs/aria-closure-kernel.md:172-209` response-vs-selection scope is correct: passive landed, active selection open.

**2. WO Acceptance Audit**

- **AC1:** Mostly resolved. The five-row table matches `README.md:16-22`; weights match `README.md:31` and `wo016a_akaike_stack.md:19-22`; drift matches `wo016c_nonlinear_refit.md:19-22`. No table drift found.

- **AC2:** Partially resolved. AIC tie and non-unique-shape caveats are present, but “mild FREE_C9 preference” at `docs/aria-closure-kernel.md:110` and `adaptive-closure-transport.tex:429-431` violates the requested no-preference wording. κ empirical strengthening is also stronger than the b-anomaly paper supports.

- **AC3:** Partially resolved. No direct RH/ẑ empirical claim is made, but the κ inheritance language is too strong because the b-anomaly headline fit does not use κ as the winning operator weight.

- **AC4:** Mostly resolved in `docs/aria-closure-kernel.md:177-203` and `adaptive-closure-transport.tex:441-448`. Watch `projection-narrative.md:77-90`, which still reads as if ARIA is already the active-regime empirical witness rather than the named next companion.

- **AC5:** Partially resolved. Main b-anomaly claims are source-consistent, but old support paths at `docs/aria-closure-kernel.md:238-241` are broken: `reports/wo007...` and `reports/wo008...` are actually under `archive/reports/`.

- **AC6:** Resolved for load-bearing math. ACT explicitly marks the b-anomaly subsection non-load-bearing at `adaptive-closure-transport.tex:397-399`; no proof depends on it.

Open items:
- Aria-chess paper draft: not resolved; should remain not delivered.
- Edge-space decomposition: not touched; correctly open at `adaptive-closure-transport.tex:382`.
- Lyapunov derivation from `F`: not touched; correctly open at `adaptive-closure-transport.tex:377`.
- B-anomaly paper itself: not edited; only cited.

**3. Catalogue Audit**

No task-specific math-catalogue was supplied or found for this WO. Existing catalogues are unrelated. If a ledger is required, `docs/aria-closure-kernel.md` currently introduces at least definitions and numerical results without catalogue entries.

**4. Attribution / External Consistency**

- Five-dataset table: verified against `vfd-b-anomaly/README.md:16-22`.
- AIC stack: verified against `README.md:31` and `reports/wo016a_akaike_stack.md:19-22`.
- Mode-B drift: verified against `README.md:33`, `reports/wo016c_nonlinear_refit.md:19-22`, and `paper/sections/04_results.tex:94-107`.
- Geometry-first variant: verified against `README.md:28`, `reports/wo016b_variant_geometry.md:7-14`, and `paper/sections/03_derivation.tex:176-198`.
- RH κ definition exists: `papers/millennium-rh-formal/rh-formal.tex:752-768`.
- κ empirical inheritance is not source-supported as written: b-anomaly’s winning full-graph operator is unweighted (`paper/sections/03_derivation.tex:176-198`; `reports/wo009_full_lift.md:122-138`).

**5. Sim Correctness**

No new sim was supplied for this WO. I did not run the b-anomaly repro pipeline; I audited its shipped README, paper sections, and reports.

**6. Tightness**

- Replace `docs/aria-closure-kernel.md:110`: “Mild FREE_C9 preference, not significant” with “No statistically significant separation; current data cannot resolve the model comparison.”
- Replace κ language at `docs/aria-closure-kernel.md:127-132`: say b-anomaly supports the shared `V_600` response operator and shell-grade context, not κ as an empirically tested weighting.
- Tighten `projection-narrative.md:79`: “contributes to the Layer 1 evidence base” is safer than “realisation reading is earned by Layer 1 holding under multiple independent witnesses.”

**7. Top Three Fixes**

1. Fix κ over-inheritance in `docs/aria-closure-kernel.md:121-132`, `docs/rh-cascade-closure-dynamics.md:145-157`, `docs/fractal-cascade-projection.md:151-161`, and `cascade-empirical-grounding.md:32`. The b-anomaly winner is unweighted `V_600 + φ^{-2}`, not κ-weighted.

2. Remove AIC preference language at `docs/aria-closure-kernel.md:110` and `adaptive-closure-transport.tex:429-431`. The WO requires tie/statistical indistinguishability language.

3. Fix stale b-anomaly support paths at `docs/aria-closure-kernel.md:238-241`: `wo007`/`wo008` live under `archive/reports/`, not `reports/`.

**8. Verdict**

Publication ready: no.

The numerical table is correct and the five-public-datasets framing is fixed, but κ/RH inheritance is still too strong and AIC wording drifts against the WO’s explicit acceptance criteria.
