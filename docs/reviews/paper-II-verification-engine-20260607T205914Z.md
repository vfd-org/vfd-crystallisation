**Claim Audit**

- [Paper II:21](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-II-verification-engine.tex:21>) “reproducible, gate-first engine” is locally supported by `vfd_math_engine/`, but “certifies that the icosian substrate realizes `ζ_K`” is too strong as a mathematical claim. The builders in [run_programme.py:15](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/vfd_math_engine/run_programme.py:15>) return the same precomputed zero lists used as targets. The gate verifies consistency of declarations, not a geometry-derived prediction.

- [Paper II:49](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-II-verification-engine.tex:49>) “eight checks” is broadly accurate, but the list has seven bullets because degree/pole are merged. The implementation really has eight checks: no-hardcoding, provenance, fingerprint, pointwise, density, rigidity, degree, pole. Pointwise is first 8 zeros with tolerance `0.2`, not an unspecified `k` ([engine_v2.py:43](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/vfd_math_engine/engine_v2.py:43>)).

- [Paper II:51](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-II-verification-engine.tex:51>) no-hardcoding is not established by the code. It is a boolean field supplied by the expression; the gate does not inspect whether the builder closes over the target data ([engine_v2.py:59](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/vfd_math_engine/engine_v2.py:59>)).

- [Paper II:69](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-II-verification-engine.tex:69>) “verified (all eight checks)” matches the saved atlas, but only at the certificate level. Paper I supports `icosian -> ζ_K(s)ζ_K(s-1)` by a proof sketch ([Paper I:106](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-I-geometric-L-functions.tex:106>)); the `φ`-shell result remains computational ([Paper I:165](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-I-geometric-L-functions.tex:165>)).

- [Paper II:75](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-II-verification-engine.tex:75>) the rejection of `substrate <-> ζ` is supported by the atlas: fingerprint, pointwise, density, rigidity, degree fail ([programme_atlas.json:202](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/vfd_math_engine/programme_atlas.json:202>)). But “five independent checks” is overclaimed. They are five diagnostics on the same declared predicted list, not independent evidence.

- [Paper II:76](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-II-verification-engine.tex:76>) “first-zero displacement ≈ 22” is wrong. The atlas value `22.305` is `max|dz| first8`, not the first-zero displacement ([programme_atlas.json:207](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/vfd_math_engine/programme_atlas.json:207>)). The first-zero displacement is about `7.49`.

- [Paper II:77](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-II-verification-engine.tex:77>) “degree (4 vs 1)” conflicts with the next sentence’s shorthand `ζ_K=ζL(χ_5)`, which has degree 2 over `Q`. Degree 4 belongs to `ζ_K(s)ζ_K(s-1)`. The notation must be fixed.

- [Paper II:81](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-II-verification-engine.tex:81>) the “independent second route” is valid only as a finite computed-list count. I reproduced ratios roughly `4.67` at height 30, `3.67` at 40, `3.10` at 50. The asymptotic claim “tending to 2” for on-line zeros is not proved unconditionally; it assumes the relevant zeros lie on the line with the expected asymptotic density.

- [Paper II:90](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-II-verification-engine.tex:90>) “independent and agree” is too strong because Result 1 already lists density as one of the five failed checks. Spacing/fingerprint and counting are disjoint computations; density is not disjoint from density.

- [Paper II:94](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-II-verification-engine.tex:94>) fitted-map control is supported for the declared test case: only provenance fails ([programme_atlas.json:257](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/vfd_math_engine/programme_atlas.json:257>)). But the provenance detector is a string search for `fit`/`tuned`; it relies on honest self-report.

- [Paper II:99](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-II-verification-engine.tex:99>) GUE control is internally false as stated. The atlas says generic GUE fails rigidity as well as pointwise and density ([programme_atlas.json:327](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/vfd_math_engine/programme_atlas.json:327>)). The paper’s prose says it passes rigidity. It does not.

- [Paper II:123](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-II-verification-engine.tex:123>) scope language is sound. The paper explicitly avoids RH proof/disproof claims at [Paper II:31](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-II-verification-engine.tex:31>) and [Paper II:127](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-II-verification-engine.tex:127>). I do not see a claim proving RH or bearing on RH.

**Internal Consistency**

- `ζ_K` is used inconsistently: sometimes the paper means `ζ_K(s)`, sometimes `ζ_K(s)ζ_K(s-1)`. This contaminates the degree claim at [Paper II:77](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-II-verification-engine.tex:77>).

- The GUE control contradicts itself: [Paper II:100](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-II-verification-engine.tex:100>) says rigidity passes; [Paper II:116](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-II-verification-engine.tex:116>) says rigidity fails.

- “First-zero displacement” conflicts with the atlas’s “first8 max” statistic.

- Cross-references `res:o2`, `res:o2b` resolve to the intended result environments. There are no `\cite` commands in Paper II.

**External Consistency**

- Paper I verifies the positive atlas story only partially: `icosian -> ζ_K(s)ζ_K(s-1)` has a proof sketch; `24`-cell and `φ`-shell are stated as computational results.

- The engine README and code support the eight-check architecture, but not the stronger claim that the gate proves non-hardcoding or mathematical realization.

- The W5 audit supports the existence of a fitted-map trap ([CIRCLE_TEST.md:59](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/CIRCLE_TEST.md:59>)). But the same file later says a different Brandt-level `(O2)` holds for 11 prime ideals ([CIRCLE_TEST.md:213](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/CIRCLE_TEST.md:213>)). Paper II must disambiguate its `(O2)` from that one.

- I found no local Paper XVIII/XXIX-style citation in this file.

**Tightness**

- [Paper II:29](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-II-verification-engine.tex:29>): replace “five independent grounds” with “five gate diagnostics.”

- [Paper II:42](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-II-verification-engine.tex:42>): replace “cannot” with “is rejected when the fitting is declared in provenance.”

- [Paper II:75](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-II-verification-engine.tex:75>): replace “substrate realizes `ζ_K=...`” with “the certified full icosian theta object realizes `ζ_K(s)ζ_K(s-1)`, whose on-line content is `ζ_K(s)`.”

- [Paper II:82](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-II-verification-engine.tex:82>): replace “confirmed” with “corroborated on the computed zero range.”

- [Paper II:100](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-II-verification-engine.tex:100>): replace “passes fingerprint and rigidity” with “passes fingerprint in the saved atlas; rigidity currently fails.”

**Surface Issues**

- “eight-check gate” should be listed as eight bullets, not seven with degree/pole merged.

- `no-hardcoding` in the paper vs `no_hardcoding` in the atlas: standardize.

- `\Sigma^2(L)` is bad notation here because `L` also means `L`-function. Use `\Sigma^2(\ell)`.

- Add citations or explicit local pointers for the W5 audit and the atlas file.

- The GUE density failure is partly an arbitrary scaling artifact from mapping eigenvalues to `[14,50]`; do not sell it as an intrinsic individual discriminator.

**Top Three Fixes**

1. Fix the `(O2)` statement at [Paper II:75](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-II-verification-engine.tex:75>): remove “independent,” correct the `22` statistic, and disambiguate `ζ_K` from `ζ_K(s)ζ_K(s-1)`.

2. Rewrite the GUE control at [Paper II:99](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-II-verification-engine.tex:99>) to match the atlas. Current prose is contradicted by the certificate table.

3. Downgrade “certifies realization” throughout [Paper II:69](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-II-verification-engine.tex:69>) and [Paper II:123](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/paper-II-verification-engine.tex:123>) unless the builders are replaced by genuinely geometry-derived predictors rather than target zero-list emitters.
