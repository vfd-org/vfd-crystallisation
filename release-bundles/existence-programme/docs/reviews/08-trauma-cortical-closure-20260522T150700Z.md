**1. Claim Audit**
No theorem/proposition environments appear; the load-bearing claims are empirical and conditional-methodological.

- `main.tex:33,38`: “identifies suffering with chronic dyscoherence” is too strong. Paper 02 says dyscoherence is a structural proxy for suffering under P-A, and explicitly says it does not exhaust suffering (`02 main.tex:458-466`). Use “treats sustained dyscoherence as a P-A-conditional structural proxy.”
- `main.tex:33,43,66`: CCR as first-order proxy is defensible only as a heuristic. The proof is not in this paper; it depends on Paper 07. The “if and only if” diagnostic wording is too strong because this draft itself reports borderline/false-negative behavior (`main.tex:102,130`).
- `main.tex:58-62`: “SL-002 pipeline unchanged” is under-described and partly inconsistent with SL-002: Paper 06 defines beta as `15--30 Hz` (`06 main.tex:54`), while this paper says `13--30 Hz`.
- `main.tex:73-77`: preregistered H1-H5 are not all tested as stated. H2 is specified as Spearman `rho`, but synthetic H2 reports `d_z` (`main.tex:88`). H5 asks for a comparable clinical-trait cohort, but `ds004315` is acute mood induction with non-clinical BDI range (`main.tex:124,132`).
- `main.tex:84-94`: synthetic `5/5 PASS` establishes pipeline responsiveness to injected features, not clinical sensitivity. H5 `d=+41.38` is implausibly large and needs explanation or demotion.
- `main.tex:98-106`: `ds007609 d=+0.79` supports an effect-size-threshold pass, but not conventional significance (`p=0.07`). H2 fails its preregistered threshold (`rho=0.28 < 0.3`, `main.tex:104`) and should be reported as FAIL/borderline, not softened.
- `main.tex:102`: “diagnostic prediction PASS” overstates the companion paper. Paper 07 says anxiety fails strict `D2/D3` but is classified PASS-leaning under immature unpaired thresholds (`07 main.tex:200-207,252`).
- `main.tex:110-120`: the dispersion-signature interpretation is interesting but under-proven. Hotelling details, variance-ratio uncertainty, regularisation, and artifact/confound checks are missing. “precise multivariate signature” and “appropriate statistic” are stronger than the methods support.
- `main.tex:122-134`: mood manipulation is not a PTSD/trauma replication and not a chronic clinical-state cohort. It is an independent real-data extension to acute mood induction.
- `main.tex:136-140`: dementia scope claim matches Paper 07 for AD (`07 main.tex:256,315-328`), but this paper only reports CCR `d`; if it invokes mean-shift/dispersion, it must report the Hotelling and variance-ratio numbers here too.
- `main.tex:144`: two-feature transfer result actually shows the minimal SL-002 feature subset does not transfer (`d=+0.22`). “methodology transfers” is okay; “discovery procedure transfers” needs evidence.
- `main.tex:148-150`: the centroid-as-`P_{\Sigma_I}` proxy is a hidden assumption. “instantiates” and “empirical anchor” should become “preliminary operational support.”
- `main.tex:152`: wrong companion section attribution. Paper 09 says Life §13.3 is flow (`09 main.tex:36`); trauma/healing is the trauma subsection in Paper 02 (`02 main.tex:785-812`).
- `main.tex:158-160`: PTSD falsifiers need power logic, clinical recovery thresholds, and minimum usable EEG duration/channel criteria.
- `main.tex:191`: data/code availability omits `ds004315` and its adapter despite reporting it as completed.

**2. Internal Consistency**
- Mood is completed in results/conclusion (`main.tex:122-134,162,195`) but “not performed,” “pending,” and absent from data availability (`main.tex:175,181,191`).
- Abstract calls `ds004315` “within-subject” with `25 per arm` (`main.tex:33`); methods call it randomized between-subject (`main.tex:124`).
- Diagnostic status oscillates: clean PASS (`main.tex:33,150`), borderline PASS-leaning (`main.tex:102,195`), and false negative (`main.tex:130`).
- “Within-cohort reference centroid” (`main.tex:33,148`) conflicts with “reference-cohort mean/std” for unpaired designs (`main.tex:60`).
- H2 is specified as correlation but synthetic validation uses an effect-size proxy (`main.tex:74,88`).

**3. External Consistency**
- Life paper: use P-A-conditional “proxy,” not “identifies suffering” (`02 main.tex:458-466`).
- CAD paper: anxiety is PASS-leaning despite strict `D2/D3` failure, not clean PASS (`07 main.tex:200-207,252`). Paper 07 also reports zero official false negatives in its 15-case accounting (`07 main.tex:209-216`), so SL-005’s “second false negative” framing needs coordination.
- CAD paper includes mood only in the two-statistic table (`07 main.tex:315-316`), not in the 14/15 classification table. Either update Paper 07 or make SL-005’s mood claim local.
- Programme overview still labels SL-005 as “first real-data result” centered on `ds007609` (`01 main.tex:1176,1182`). This draft should either stay Round-1 first-result focused or trigger updates across Papers 01/02/07.

**4. Narrative Coherence**
The paper mostly uses the programme’s bounded vocabulary, but it should copy the stricter honesty style of Papers 09/10. The strongest coherent framing is: “SL-005 is a first clinical-trait transfer of SL-002, not a trauma validation.” The title and abstract currently read as if PTSD replication is part of the result (`main.tex:15-17,33`), while the actual anchor is trait anxiety.

**5. Tightness Edits**
- Title: “Trait-Anxiety Real-Data Anchor and Pre-Registered PTSD Replication Target.”
- `main.tex:33`: replace “identifies suffering with” with “treats, under P-A, as a structural proxy for.”
- `main.tex:100`: add “passes the preregistered effect-size threshold, not `p<0.05`.”
- `main.tex:102`: replace “confirms PASS” with “is consistent with the PASS-leaning classification.”
- `main.tex:118`: replace “precise multivariate signature” with “a multivariate signature consistent with.”
- `main.tex:126`: replace “chronic-dyscoherence interpretation” with “dispersion-based dyscoherence proxy interpretation.”
- `main.tex:150`: replace “instantiates” with “provides preliminary operational support for.”
- `main.tex:181`: revise to “One chronic clinical-trait anchor; one acute mood extension.”

**6. Surface Issues**
- Unicode arrow `→` at `main.tex:90` may break pdfLaTeX; use `$\to$`.
- `pre-registered` / `preregistered` inconsistent.
- `SmartLifeClosure` citation key differs from `SmartLifeAsClosure` used elsewhere.
- Repository org alternates across programme refs (`vfd-aria` vs `vfd-org`).
- `ds004315` result lacks bibliography DOI/version and adapter listing.
- Quartile selection from `n=51` to `12+12` needs exclusion/ranking explanation.

**7. Top Three Fixes**
1. Re-scope the claim: `ds007609 d=+0.79, p=0.07` is a preliminary trait-anxiety anchor, not PTSD or trauma validation (`main.tex:98-106,150,195`).
2. Add a real Methods section: preprocessing, channel list, exclusions, durations, artifact handling, standardisation, quartile rule, prereg timestamp, diagnostic computation, Hotelling implementation, CIs/permutation tests (`main.tex:54-67,98-104,110-120`).
3. Fix cross-paper attribution: P-A proxy language, PASS-leaning diagnostic, Paper 07 false-negative accounting, and the incorrect Life §13.3 therapy reference (`main.tex:33,102,130,152`).

**8. Programme-Strengthening Recommendations**
- Add a shared “claim status box” to all Solution Lab papers: formal / proxy / empirical / P-A-conditional / diagnostic-conditioned.
- Maintain one programme-wide result registry so Papers 01/02/07/08 do not disagree about whether mood, dementia, or SL-005 are pending/completed.
- Standardise CCR/CAD feature definitions, especially frequency bands and reference-centroid conventions.
- Separate “effect-size-threshold PASS” from “statistical-significance PASS” across all papers.

**9. Publication Ready?**
No. The `d=+0.79` first-result is worth keeping, but the paper is not publication-ready on substantive-methods/attribution scope. It needs tighter claims, a paper-grade methods/limitations section, and cross-paper consistency fixes before release.
