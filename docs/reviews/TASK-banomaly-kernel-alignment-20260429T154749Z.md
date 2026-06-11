**1. Claim Audit**

No new lemmas/theorems/conjectures are introduced in `docs/aria-closure-kernel.md`; it contains definitions, numerical claims, and imported status claims.

- `C_\varphi = L_M+\varphi^{-2}I`, `\psi=C_\varphi^{-1}f` (`docs/aria-closure-kernel.md:13-23`): established as definitions.
- Green-response regularity/positivity (`docs/aria-closure-kernel.md:24-37`): now adequately scoped. The Round 5 “smooth” overclaim is gone.
- `G(x)=\varphi/2 e^{-|x|/\varphi}` (`docs/aria-closure-kernel.md:41-47`): correct for the 1D free-space operator.
- 600-cell counts/shells (`docs/aria-closure-kernel.md:51-56`): locally supported by b-anomaly `paper/sections/03_derivation.tex:77-101`.
- Compression diagnostic (`docs/aria-closure-kernel.md:61-74`): fixed. `wo011_spectral.csv` shows the error drops to `0.040` at modes 9-14 and stays there through mode 30; mode 15 only enters the `lambda=9` block. Canonical `lambda=9` multiplicity 16 is supported by `papers/paper-xxii/paper-xxii.tex:185-193`.
- Five-dataset table (`docs/aria-closure-kernel.md:92-100`): verified verbatim against b-anomaly `README.md:16-22`.
- Universality/sign-uniformity (`docs/aria-closure-kernel.md:104-109`): supported by `README.md:24-28` and `paper/sections/06_cross_dataset.tex:194-208`.
- Cross-channel claim (`docs/aria-closure-kernel.md:110-115`): mostly honest now because it states the predicted `+2.5` vs observed `+4.98` factor-2 residual. “Consistent with” is still a little generous; “partly explained by” would be tighter.
- Variant test / cocycle scope (`docs/aria-closure-kernel.md:143-174`): correct. The unweighted operator is the empirical winner; κ-edge-weighting is not.
- AIC tie / Mode-B drift (`docs/aria-closure-kernel.md:126-141`): supported. Gaussian charm-loop comparison should ideally say it is from the Mode-B stress-test section, but this is not a gating overclaim.
- Programme-family claims (`docs/aria-closure-kernel.md:176-212`): properly weakened to “programme-positioned” and “not proved.”
- Response vs selection (`docs/aria-closure-kernel.md:214-255`): correctly leaves selection open.

**2. WO Acceptance Audit**

- **AC1** (`TASK-banomaly-kernel-alignment.md:76`): resolved. Headline numerical claims match b-anomaly README/reports.
- **AC2** (`:78-83`): resolved. AIC tie, non-unique-shape caveat, and Mode-B drift are preserved.
- **AC3** (`:84`): resolved in artefacts. `docs/aria-closure-kernel.md:169-174` and `cascade-empirical-grounding.md:32` avoid empirical inheritance for ẑ.
- **AC4** (`:86`): resolved. Active-regime / aria-chess remains open.
- **AC5** (`:88`): resolved substantively. The b-anomaly claims survive source checking; only wording tightness remains.
- **AC6** (`:90`): resolved. The b-anomaly material is explicitly non-load-bearing.

Open items (`TASK-banomaly-kernel-alignment.md:94-99`): all correctly untouched. Aria-chess draft, edge-space decomposition, Lyapunov derivation from `F`, and b-anomaly paper edits remain out of scope. The b-anomaly paper itself still has stale spectral prose in `paper/sections/03_derivation.tex:200-209`, but this WO explicitly says not to edit it.

**3. Catalogue Audit**

No WO-specific math-catalogue was supplied or found. Existing catalogues are unrelated. Since this WO says no new theorems are introduced, absence of a catalogue is not a substantive gate, but the unlabelled definitions/numerical results are not ledgered.

**4. Attribution / External Consistency**

Verified locally:

- b-anomaly README table and headline scope: `README.md:14-35`.
- Cross-dataset/AIC stack: `paper/sections/06_cross_dataset.tex:45-126`.
- Variant test: `paper/sections/03_derivation.tex:151-198`, `reports/wo016b_variant_geometry.md:3-16`.
- Mode-B drift: `paper/sections/04_results.tex:85-112`, `reports/wo016c_nonlinear_refit.md:19-36`.
- RH `def:kappa`: `papers/millennium-rh-formal/rh-formal.tex:752-768`.
- RH `def:closure_flow`: `papers/millennium-rh-formal/rh-formal.tex:1851-1876`.
- ACT selection/open-layer status: `papers/adaptive-closure-transport/adaptive-closure-transport.tex:442-464`.
- Round 5 cascade-grounding fix: `papers/cascade-derivation/cascade-empirical-grounding.md:32`.
- NS/RH unweighted-variant alignment: `ns-formal.tex:807-820`, `rh-formal.tex:2796-2800`.

**5. Sim Correctness**

No WO-local sim was supplied. I checked source reports used as attribution; I did not rerun the external b-anomaly repro pipeline.

**6. Tightness**

Non-gating edits:

- `docs/aria-closure-kernel.md:110-115`: replace “consistent with” by “partly explained by.”
- `docs/aria-closure-kernel.md:134-136`: add “in the Mode-B stress test” to the Gaussian charm-loop caveat.

**7. Top Three Fixes**

No substantive must-fix remains. Top non-gating tightening is `docs/aria-closure-kernel.md:110-115`.

**8. Verdict**

Publication ready: yes.
