**1. Claim Audit**
No lemmas/theorems/conjectures are introduced in `docs/aria-closure-kernel.md`; the non-trivial objects are definitions, numerical claims, and imported status claims.

- `C_\varphi = L_M+\varphi^{-2}I` and `\psi=C_\varphi^{-1}f` (`docs/aria-closure-kernel.md:13`, `:19-23`): established as definitions.
- “positive definite” / “smooth, centred ... non-oscillatory” (`docs/aria-closure-kernel.md:24-31`): partially established. Positivity is fine under the stated self-adjoint non-negative hypotheses. “Smooth” is not automatic for merely localised `f` and is not meaningful on a finite graph without defining a discrete regularity notion.
- `G(x)=\varphi/2 e^{-|x|/\varphi}` (`docs/aria-closure-kernel.md:37-43`): established for the whole-line/free-space operator with decay boundary condition.
- 600-cell counts/shells (`docs/aria-closure-kernel.md:47-52`): supported by b-anomaly derivation `paper/sections/03_derivation.tex:77-101`.
- Compression diagnostic (`docs/aria-closure-kernel.md:57-70`): mostly fixed, but still not clean. The CSV supports the drop from `0.075874` to `0.040045` at `n=9` and `lambda_max_used=9` at `n=15` (`wo011_spectral.csv:7-16`). It does **not** show another reconstruction-error drop at `n=15`; the error remains `0.040045`. The dropped multiplicity-6 claim is correctly replaced by canonical `λ=9` multiplicity 16, supported by `papers/paper-xxii/paper-xxii.tex:185-193`.
- Five-dataset table (`docs/aria-closure-kernel.md:90-96`): verified verbatim against b-anomaly `README.md:16-22`.
- Universality/sign uniformity (`docs/aria-closure-kernel.md:100-105`): supported by `README.md:24-28` and `paper/sections/06_cross_dataset.tex:194-208`.
- Cross-channel ratio (`docs/aria-closure-kernel.md:106-111`): numerically supported by `paper/sections/07_cross_channel.tex:129-165`, but “consistent with predicted amplification” is a little too generous; the source calls the amplitude prediction only `partial` and leaves a factor-2 gap (`:176-188`).
- Geometry-first variant test (`docs/aria-closure-kernel.md:112-120`, `:139-157`): supported by `paper/sections/03_derivation.tex:151-198` and `reports/wo016b_variant_geometry.md:3-16`. Historical caveat is correctly included.
- AIC tie / non-unique shape / Mode-B drift (`docs/aria-closure-kernel.md:122-137`): supported by `README.md:30-35`, `paper/sections/04_results.tex:85-112`, `paper/sections/05_stress_tests.tex:110-123`, and `reports/wo016c_nonlinear_refit.md:19-36`.
- Cocycle bridge (`docs/aria-closure-kernel.md:159-170`): correctly scoped as structural, not empirical. RH `κ(v)=(s(v)-4)^2` is verified at `papers/millennium-rh-formal/rh-formal.tex:752-760`.
- Programme family membership (`docs/aria-closure-kernel.md:172-208`): now correctly weakened to “programme-positioned” and “not proved.”
- Response vs selection (`docs/aria-closure-kernel.md:210-251`): correctly leaves selection open; ACT open items verify at `papers/adaptive-closure-transport/adaptive-closure-transport.tex:377-382`.

**2. WO Acceptance Audit**
- **AC1** (`TASK...md:76`): partially resolved. Main fit numbers are verbatim. The spectral diagnostic still misstates the `n=15` reconstruction-error behaviour.
- **AC2** (`:78-83`): resolved for AIC tie, non-unique shape, and Mode-B drift. Cross-channel “consistent” should be softened.
- **AC3** (`:84`): partially resolved. `docs/aria-closure-kernel.md:165-170` is clean, but `papers/cascade-derivation/cascade-empirical-grounding.md:32` still says `ẑ inherits operator-level support`, which is the stale overclaim Round 4 was meant to kill.
- **AC4** (`:86`): resolved. Active-regime / aria-chess remains explicitly open (`docs/aria-closure-kernel.md:212-220`).
- **AC5** (`:88`): partially resolved. Most b-anomaly paragraphs survive source checking; the spectral `n=15` wording and cross-channel “consistent” phrasing do not.
- **AC6** (`:90`): resolved. The note is explicitly non-load-bearing (`docs/aria-closure-kernel.md:3-9`) and ACT repeats that status (`adaptive-closure-transport.tex:397-440`).

Open items:
- Aria-chess draft: not touched; correctly open.
- Edge-space decomposition of `R^{E_M}`: not touched; correctly open.
- Lyapunov derivation from `F`: not touched; correctly open.
- B-anomaly paper itself: not edited. Note: its own `paper/sections/03_derivation.tex:200-209` still contains the old false `λ=9`, multiplicity-6 prose, but that repo was out of scope.

**3. Catalogue Audit**
No WO-specific math-catalogue was supplied or found. Existing catalogues are unrelated. If this WO requires a ledger, then `C_\varphi`, the closure response field, the continuum Green kernel, the discrete response, the compression diagnostic, and the b-anomaly numerical result are uncatalogued.

**4. Attribution / External Consistency**
Verified: b-anomaly README table and headline scope (`README.md:14-35`), cross-dataset table and AIC stack (`06_cross_dataset.tex:45-126`), variant test (`03_derivation.tex:151-198`; `wo016b_variant_geometry.md:3-16`), Mode-B drift (`04_results.tex:85-112`; `wo016c_nonlinear_refit.md:19-36`), RH `def:kappa` (`rh-formal.tex:752-760`).

Defects:
- `docs/aria-closure-kernel.md:60-63` overreads `wo011_spectral.csv`; no error drop occurs at `n=15`.
- `papers/cascade-derivation/cascade-empirical-grounding.md:32` keeps the stale “inherits operator-level support” language.
- `papers/millennium-ns-formal/ns-formal.tex:807-816` removes stale `r≈0.98` framing and has the AIC tie, but it does not include the unweighted-variant clarification that landed in RH (`rh-formal.tex:2796-2800`).

**5. Sim Correctness**
No sim artefact was supplied for this WO. I audited shipped b-anomaly source reports; I did not rerun the external repro pipeline.

**6. Tightness**
- `docs/aria-closure-kernel.md:60-63`: replace “and again at n=15” with “the error remains at 0.040 through n=30; n=15 only marks entry into the λ=9 block.”
- `docs/aria-closure-kernel.md:106-111`: replace “consistent with” by “partly explained by.”
- `papers/cascade-derivation/cascade-empirical-grounding.md:32`: replace “inherits operator-level support” with “shares operator-level infrastructure.”
- `docs/aria-closure-kernel.md:30`: replace “smooth” with “regular away from singular support” or restrict `f` to a smooth source.

**7. Top Three Fixes**
1. `docs/aria-closure-kernel.md:60-63`: fix the false `n=15` reconstruction-error wording.
2. `papers/cascade-derivation/cascade-empirical-grounding.md:32`: remove stale `ẑ inherits operator-level support`.
3. `docs/aria-closure-kernel.md:24-31`: tighten the Green-response regularity claim.

**8. Verdict**
Publication ready: no.
