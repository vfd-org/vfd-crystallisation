Line refs are to `release-bundles/fractal-tiling-theorem/writeup/note-shared-object.tex` unless noted.

**1. Claim Audit**

- “The same geometric object ... appears ... as a substrate in ... cosmological modelling, and ... as the carrier of certain L-functions” ll.16-20. Arithmetic side is supported by Paper I. Cosmology side is not cited here and is not established in this note. As firewall language, this is too quotable: it places cosmology and zeta in the same sentence before the disclaimer.
- “The bridge ... is open ... Riemann ζ ... tested and found negative” ll.22-25. Supported only for the formal `substrate <-> zeta` candidate tested by Paper II, not every conceivable bridge. Say “one formalized strong bridge candidate”.
- “The 600-cell / icosian ring is a single ... object” ll.29-30. Over-compressed. A finite 600-cell vertex set and the icosian maximal order/ring are not literally one object. Use “the 600-cell as the unit-icosian vertex set inside the icosian ring”.
- “arithmetic role ... order whose theta series realizes ζK(s)ζK(s−1), with sub-objects realizing ...” ll.34-36. Paper I contains this claim, but “realizes” is undefined in this note. For the subobjects, Paper I marks them as computational/verification results, not full theorem-grade derivations.
- “That one object recurs in both is true ... natural reason the same vocabulary ... appears” ll.38-40. Not proved. “Natural reason” is sociological/interpretive, not mathematical.
- “certified negative on five independent grounds: the substrate realizes ζK=ζ·L(χ5)” ll.49-52. Internally inaccurate. The five grounds in Paper II are fingerprint, pointwise zeros, density, rigidity, and degree. Also the arithmetic object elsewhere is ζK(s)ζK(s−1), not just ζK.
- “Riemann zeros share their fine statistics (GUE)” ll.61-63. Too strong without citation and qualification. Full GUE statistics are conjectural/empirical, not a theorem as stated.
- “no claim links the cosmological model to the Riemann Hypothesis” ll.67-69. This is the correct firewall sentence. It should be moved into the abstract in this exact RH form.

**2. Internal Consistency**

- ζ-object mismatch: ll.34-36 say the substrate realizes ζK(s)ζK(s−1); ll.51-52 reduce this to ζK=ζ·L(χ5). These are not the same statement.
- “five independent grounds” ll.50-51 conflicts with the single factorization explanation that follows.
- “single object” ll.29-30 conflicts with “600-cell / icosian ring” as two related but categorically different objects.
- No `\ref`, `\eqref`, `\cite`, or `\label` commands occur in the note, so there are no unresolved cross-references. The problem is absence of real citations, not broken references.

**3. External Consistency**

- Paper I attribution, ll.20 and 36: verified locally in `paper-I-geometric-L-functions.tex` ll.29-41, ll.106-122, ll.141-169. Caveat: Paper I’s subobject claims are partly “Computational Result” level; do not cite them as theorem-grade unless that is intended.
- Paper II attribution, ll.24-25 and ll.49-52: verified locally in `paper-II-verification-engine.tex` ll.74-80 and table ll.111-116. The machine atlas also records the rejected `substrate <-> zeta` entry with failed fingerprint, pointwise, density, rigidity, and degree checks in `vfd_math_engine/programme_atlas.json` ll.186-243.
- Paper II explicitly says its certificate is not a proof certificate and implies nothing about RH (`paper-II-verification-engine.tex` ll.123-130). The note should inherit that qualification whenever it says “certified”.
- The cosmology-side source is not cited. Local cosmology material uses `V_600`, but also marks the cosmology module exploratory and conditional. This note currently fails to import that caveat.

**4. Tightness**

- ll.16-20: Replace with “The same 600-cell/icosian construction appears in two separate programme contexts...”  
- ll.22-25: Replace with “For one formalized strong candidate, `substrate realizes ζ`, Paper II reports a negative verification certificate.”  
- ll.29-30: Replace with “The 600-cell vertex set is the unit-icosian part of the icosian-ring construction.”  
- ll.38-40: Replace with “This explains a shared vocabulary within the programme, but not a mathematical map between the two roles.”  
- ll.49-52: Replace with “Paper II rejects this candidate on fingerprint, pointwise, density, rigidity, and degree checks; structurally the substrate carries ζK(s)ζK(s−1), so ζ is only a factor.”  
- ll.61-63: Replace with “The Riemann zeros are empirically/conjecturally modelled by GUE statistics, a universality class shared by many unrelated systems.”

**5. Surface Issues**

- `L(\chi_5)` should be `L(s,\chi_5)` at ll.36 and 52.
- “GUE” is undefined at l.62.
- Prose references “Paper I” and “Paper II” should be real citations or exact filenames.
- `\Q` is defined but unused.
- “certified negative” is jargon. Define it as “negative verification certificate, not proof certificate.”

**6. Top Three Fixes**

1. Fix the abstract firewall, ll.16-25. It currently lets a hostile reader quote “cosmological modelling” and “Riemann zeta function” from the same claim. Add “no cosmology↔RH implication” there, not only at the end.
2. Correct the ζ-negative statement, ll.49-52. It must name the five Paper II checks and use ζK(s)ζK(s−1), not the shortened ζK=ζ·L(χ5).
3. Replace “single object” language, ll.29-40, with category-accurate wording: same 600-cell/icosian construction, two separate roles, no derivation map.
