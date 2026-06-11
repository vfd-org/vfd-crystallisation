**1. Claim Audit**

- `docs/aria-closure-kernel.md:12-25` defines `C_\varphi` and claims positivity / smooth non-oscillatory response. Mostly OK for a self-adjoint PSD Laplacian plus positive mass term; hidden hypothesis: `L_M` must be PSD/self-adjoint. “Smooth, centred” is not automatic on arbitrary substrates.
- `docs/aria-closure-kernel.md:29-35` Green kernel `(\varphi/2)e^{-|x|/\varphi}` is correct for the whole-line operator `-d²/dx²+\varphi^{-2}`.
- `docs/aria-closure-kernel.md:39-47` 600-cell counts/shells are source-consistent.
- `docs/aria-closure-kernel.md:49-55` overstates: “compresses to a rank-6 spectral sector, which projects to a rank-1 observable.” The b-anomaly source supports a rank-6 spectral diagnostic, not the rank-1 projection map as stated. Needs a defined projection or softer wording.
- `docs/aria-closure-kernel.md:73-82` table is verbatim against `vfd-b-anomaly/README.md:16-22`. Pass.
- `docs/aria-closure-kernel.md:85-119` universality, sign-uniformity, AIC tie, non-unique-shape, Mode-B drift are source-consistent with `README.md:24-35` and paper sections.
- `docs/aria-closure-kernel.md:121-134` fixes the main κ over-inheritance: it now says unweighted wins and φ-cocycle variants lose. But it introduces two source defects:
  - `docs/aria-closure-kernel.md:123-124` says “shell-grade-weighted”; the shipped variants are unweighted, φ-cocycle geometric mean, φ-cocycle arithmetic mean (`paper/sections/03_derivation.tex:151-158`).
  - `docs/aria-closure-kernel.md:126-128` says “χ² ΔAIC = 13.555”; `13.555` is χ², not ΔAIC (`reports/wo016b_variant_geometry.md:7-14`).
- `docs/aria-closure-kernel.md:136-145` is now correctly scoped: structural convergence only, no empirical RH/ẑ claim.
- `docs/aria-closure-kernel.md:176-181` still has a tension: “They are members” is stronger than “programme-proposed family instances; not proved.” Use the weaker phrase throughout.

**2. WO Acceptance Audit**

- **AC1:** Partially resolved. Main b-anomaly numbers are verbatim. Defect: `13.555` is mislabeled as “χ² ΔAIC” at `docs/aria-closure-kernel.md:126-128`.
- **AC2:** Resolved on AIC preference, non-unique shape, and Mode-B drift. No remaining “mild FREE_C9 preference” wording in the reviewed target docs.
- **AC3:** Resolved in substance. κ is structural only; no empirical ẑ/RH claim.
- **AC4:** Resolved. Active-regime / selection layer remains open at `docs/aria-closure-kernel.md:185-222` and `adaptive-closure-transport.tex:442-449`.
- **AC5:** Partially resolved. The main b-anomaly claim matches the source, but the variant-name and metric-label errors above fail hostile source checking.
- **AC6:** Resolved. The b-anomaly material is non-load-bearing context, especially `adaptive-closure-transport.tex:397-440`.

Open items:
- Aria-chess paper: not touched; correctly left open.
- Edge-space decomposition of `R^{E_M}`: not touched; correctly preserved open.
- Lyapunov derivation from `F`: not touched; correctly preserved open.
- B-anomaly repo itself: not edited. Correct.

**3. Catalogue Audit**

No relevant math-catalogue was supplied or found for `docs/aria-closure-kernel.md`. Existing catalogues are unrelated. If this WO requires a ledger, missing entries include the `C_\varphi` definition, response field, continuum Green kernel, 600-cell discrete lift, compression result, and b-anomaly numerical result.

**4. Attribution / External Consistency**

- B-anomaly table, AIC weights, Mode-B drift, and non-unique-shape caveat verify locally.
- Round-1 path issue is fixed: `wo007` / `wo008` now point under `archive/reports/` at `docs/aria-closure-kernel.md:251-254`.
- Variant attribution is not exact: source has `PHI_GEOMETRIC` and `PHI_ARITHMETIC`, not “shell-grade-weighted.” Same defect appears in `docs/rh-cascade-closure-dynamics.md:149-150` and `docs/fractal-cascade-projection.md:153`.
- `rh-formal.tex` does contain `def:kappa` as cited (`papers/millennium-rh-formal/rh-formal.tex:752-760`).
- The cited Millennium family-member sources generally say “positioned/proposed/candidate,” not theorem-level membership. `docs/aria-closure-kernel.md:176` should match that weaker status.

**5. Sim Correctness**

No sim artefact was supplied for this WO. I did not run the external b-anomaly repro pipeline; I audited shipped source reports and paper sections.

**6. Tightness**

- Replace “χ² ΔAIC = 13.555” with “data χ² = 13.555.”
- Replace “shell-grade-weighted” with “φ-cocycle arithmetic mean.”
- Replace “are members” with “are positioned as programme-proposed family instances.”
- Replace “verbatim scope” at `docs/aria-closure-kernel.md:83` with “source scope”; the bullets are summaries, not verbatim quotations.

**7. Top Three Fixes**

1. `docs/aria-closure-kernel.md:123-128`, plus `docs/rh-cascade-closure-dynamics.md:149-155` and `docs/fractal-cascade-projection.md:153`: correct the variant list and metric label.
2. `docs/aria-closure-kernel.md:49-55`: either define the rank-1 observable projection or downgrade the compression claim to the b-anomaly spectral diagnostic.
3. `docs/aria-closure-kernel.md:176-181`: make family membership uniformly “programme-proposed / not proved,” matching the cited papers.

**8. Verdict**

Publication ready: no.  
Round-1 must-fixes are substantially resolved, but the variant-catalogue misstatement, χ²/ΔAIC metric error, and unsupported rank-1 compression claim are substantive enough to block.
