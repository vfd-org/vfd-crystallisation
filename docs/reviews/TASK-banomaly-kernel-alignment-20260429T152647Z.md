**1. Claim Audit**

- `docs/aria-closure-kernel.md:3-8`: “response primitive derived and empirically validated” is too strong. The b-anomaly source supports a structural sign-uniform pass, not validation or model preference. Needs “externally witnessed by a structural test.”
- `docs/aria-closure-kernel.md:12-25`: definition of `C_\varphi` is fine. “positive definite” needs the hidden hypothesis that `L_M` is self-adjoint non-negative. “smooth, centred, non-oscillatory” is not established for arbitrary substrates.
- `docs/aria-closure-kernel.md:29-35`: continuum Green function is correct for the whole-line operator `-d²/dx² + φ⁻²`. State the domain/boundary convention.
- `docs/aria-closure-kernel.md:39-48`: 600-cell facts are supported by the b-anomaly derivation source.
- `docs/aria-closure-kernel.md:49-55`: rank-6 compression fix landed cleanly. Source supports a rank-6 spectral diagnostic, not rank-1.
- `docs/aria-closure-kernel.md:59-119`: table, AIC tie, Mode-B drift, Gaussian caveat, and sign-uniformity are supported by the b-anomaly README/paper.
- `docs/aria-closure-kernel.md:97-102` and `121-139`: variant-name and `13.555` fixes landed cleanly. `13.555` is correctly data `χ²`, not ΔAIC. Add one caveat: variant selection is criterion-independent, not historically blind; the b-anomaly limitations admit data was seen first.
- `docs/aria-closure-kernel.md:141-150`: RH/ẑ inheritance is mostly scoped correctly: operator-level only, no RH empirical claim.
- `docs/aria-closure-kernel.md:154-185`: residual overclaim. Line 156 says the listed objects “are members” of the family; the cited papers support only “programme-proposed / candidate / positioned as” family membership. The final caveat at lines 181-185 helps, but the opening still overstates.
- `docs/aria-closure-kernel.md:189-226`: response-vs-selection section is correctly scoped. Selection remains open.

**2. WO Acceptance Audit**

- **AC1:** Mostly resolved. Headline numbers match b-anomaly README/reports. Minor issue: cross-channel detail mixes README summary with paper §7 detail; cite the detailed source explicitly.
- **AC2:** Partially resolved. The AIC tie, non-unique shape, and Mode-B drift caveats are present. Blocker: “empirically validated” and “are members” are stronger than the sources support.
- **AC3:** Resolved. Cocycle bridge is structural/operator-level only; no RH detection claim.
- **AC4:** Resolved. Active-regime / aria-chess remains explicitly open.
- **AC5:** Partially resolved. Most b-anomaly claims cite source paths, but the geometry-first wording needs the data-discovered caveat.
- **AC6:** Resolved. The b-anomaly result is framed as non-load-bearing context.

Open items:
- Aria-chess paper draft: not touched, correctly open.
- Edge-space decomposition of `R^{E_M}`: not touched; still open.
- Lyapunov derivation from `F`: not touched; still open.
- B-anomaly paper itself: not edited.

**3. Catalogue Audit**

No WO-specific math catalogue is supplied. If a catalogue is required, the following are currently uncatalogued: `C_\varphi`, closure response field, continuum kernel, rank-6 spectral diagnostic, b-anomaly numerical table, variant-selection result, and programme-family membership claim.

**4. Attribution / External Consistency**

- B-anomaly README supports the five-dataset table, sign uniformity, AIC weights, non-unique-shape caveat, and Mode-B drift.
- B-anomaly paper/report supports `UNWEIGHTED / PHI_GEOMETRIC / PHI_ARITHMETIC` and `χ² = 13.555`.
- RH source supports `κ(v) = (s(v)-4)^2`.
- Adaptive-closure source supports passive regime and leaves Lyapunov / edge-space items open.
- Millennium source files support only candidate/programme-positioned family membership, not formal canonical membership.

**5. Sim Correctness**

No sim is supplied for this WO. The b-anomaly repro pipeline is an external source here, not audited as a sim in this review.

**6. Tightness**

- `docs/aria-closure-kernel.md:3-4`: replace “empirically validated” with “externally witnessed by a structural sign-uniform test.”
- `docs/aria-closure-kernel.md:97-102`: add “criterion-independent; historically data-discovered.”
- `docs/aria-closure-kernel.md:154-156`: replace “are members” with “are positioned as programme-proposed members.”
- `docs/aria-closure-kernel.md:222-226`: “strongest evidence” → “strongest programme-level indication.”

**7. Top Three Fixes**

1. `docs/aria-closure-kernel.md:154-185`: fix family-membership overclaim throughout the section, not just in the closing caveat.
2. `docs/aria-closure-kernel.md:3-4`: downgrade “empirically validated.”
3. `docs/aria-closure-kernel.md:97-102` / `121-132`: add the data-discovered caveat to the geometry-first variant claim.

**8. Verdict**

Publication ready: no.

Round 2 fixes landed cleanly. The remaining blockers are substantive scope defects: empirical-validation wording and family-membership overclaim.
