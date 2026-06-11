Line numbers refer to [reach-and-limit.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/writeup/reach-and-limit.tex:1>).

**Claim Audit**
- L30-L39, L50-L52, L100-L107, L220-L221: the headline claim “exactly \(\zeta_K(s)\zeta_K(s-1)\)” is not supported by the cited IcosianTriad source as written. That paper’s theorem states \(L(\Theta_\mathcal I,s)=\zeta_K(s)\zeta_K(s-1)C_2(s)\), with equality to the clean product only away from the prime \(2\): [icosian-triad.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/icosian-triad-v600/papers/01-icosian-triad/icosian-triad.tex:713>). This is publication-blocking unless the paper defines an imprimitive/local-2-removed \(L\)-function.
- L83-L93: class-number-one lemma is acceptable. Kirschmer-Voight Table 8.2 supports \((n,d_F,D,N)=(2,5,1,1)\); the paper correctly cites it and does not make an independent false Conway-Sloane argument. KV tabulates right ideal classes, but left/right are harmless here by conjugation.
- L110-L112: “The rational \(24\)-cell ... realizes \(\zeta(s)\zeta(s-1)\)” has no proof or citation in this consolidated paper. The atlas row is not independent: the builder returns the Riemann zero list directly.
- L113-L124: Proposition on on-line zeros of \(\zeta(s)\zeta(s-1)\) is proved correctly and does not assume RH.
- L126-L130: \(\varphi\)-shell “realizes \(L(s,\chi_5)\)” is stronger than the evidence shown. The saved atlas verifies declared zero-list consistency, not a geometric derivation.
- L132-L135: the factor assignment to Galois-fixed/sign parts is plausible programme language, but the displayed product again omits \(C_2(s)\), and the sub-object-to-factor split is not proved here.
- L140-L157: gate description mostly matches code, provided “no-hardcoding” and “provenance” are read as declared-procedure checks, not program analysis.
- L160-L169: O2 negative numbers check out: fingerprint \(0.077\) vs \(0.000\), max first-eight displacement \(22.305\), first displacement \(7.486\), degree \(4\) vs \(1\), matching [programme_atlas.json](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/vfd_math_engine/programme_atlas.json:186>). The claim inherits the local-2 caveat.
- L171-L179: finite counting ratios are correct: \(14/3\approx4.7\), \(22/6\approx3.7\), \(31/10=3.1\). But “and their \(s-1\) shifts” is irrelevant to on-line density, and “tending to \(2\) asymptotically” is not certified for on-line zeros without GRH-style assumptions.
- L182-L187: fitted-map control is established only for declared provenance. That is fine, but cite the W5 audit explicitly; local support is [CIRCLE_TEST.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/CIRCLE_TEST.md:59>).
- L188-L196: GUE prose now matches the saved atlas: fingerprint passes, pointwise/density/rigidity fail. But this is one seeded, rescaled control from [grow_atlas.py](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/release-bundles/fractal-tiling-theorem/vfd_math_engine/grow_atlas.py:6>), not a theorem about generic GUE operators.

**Internal Consistency**
- The dominant inconsistency is \(C_2(s)\): every “exactly \(\zeta_K(s)\zeta_K(s-1)\)” line conflicts with the cited source.
- L162 says “on-line content” of a degree-4 product; L173-L176 counts only the unshifted \(\zeta\) and \(L(\chi_5)\) factors on \(\Re s=1/2\). Distinguish completed degree from on-line zero count.
- L191-L193 says GUE also fails density/rigidity; table L208 lists only pointwise under “failing checks.” Either include all failures or rename the column “load-bearing rejection.”
- Cross-references resolve in the existing aux/log. I found no undefined refs/cites.

**External Consistency**
- IcosianTriad: locally verifiable, but it supports the clean product only modulo/local-away-from-2; exact theorem includes \(C_2(s)\). The bibliography entry L228-L230 is therefore false as phrased.
- IcosianTriad “out-of-sample verification”: I found finite simulations and coefficient checks, but not a clearly documented out-of-sample split. Do not use that phrase unless you point to the exact artifact.
- Kirschmer-Voight: citation is materially correct. I checked the primary PDF: https://jvoight.github.io/articles/quatideal-fixed-errata-111614.pdf
- Prior W5 audit: locally supported, but uncited in the draft.

**Tightness**
- L38-L39: replace “exactly \(\zeta_K(s)\zeta_K(s-1)\)” with “the imprimitive \(\zeta_K(s)\zeta_K(s-1)\) identity, with the local-2 factor stated separately.”
- L59: replace “the natural correspondence does not hold” with “the specified strong bridge candidate is rejected.”
- L127: replace “realizes \(L(s,\chi_5)\)” with “has tested on-line zeros matching \(L(s,\chi_5)\).”
- L174-L176: replace the asymptotic sentence with “In the computed windows the count ratios are \(4.7,3.7,3.1\); a leading-order doubled density is heuristic unless the on-line assumption is stated.”
- L221: replace “provably” with “certifiably, for this declared candidate and this gate.”

**Surface Issues**
- Define “substrate” before L58/L161.
- Define GUE on first use.
- Add `\cite{Siegel,Weil1965}` where Siegel-Weil is invoked at L103.
- Bibliography entry for IcosianTriad must mention \(C_2(s)\), not the clean product.
- Reproducibility: `run_programme.py` does not generate the GUE row; `grow_atlas.py` does. Say which command produced the saved atlas.

**Top Three Fixes**
1. Fix the local-2 factor everywhere: L30-L39, L100-L107, L132-L135, L160-L164, L220-L221.
2. Downgrade “verified/realizes” for the positive rows unless actual geometric derivations are supplied: L110-L130 and L203-L205.
3. Narrow the counting-route and GUE/table language: L171-L179 and L188-L208.

Geometry-first reframing: viable only if the headline object is the icosian/Hilbert-Eisenstein arithmetic object with the local-2 factor honestly included. The class-number-one input is solid; the certified zeta-negative is solid for the specified bridge candidate. It is not solid enough to advertise RH as an “arithmetic by-product” beyond “\(\zeta\) appears as one factor.” Calling this a primary physics object would over-elevate the result unless independent physical structure is added.
