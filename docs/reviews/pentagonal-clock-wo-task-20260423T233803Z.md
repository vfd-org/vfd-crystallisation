**Claim Audit**

- `F1`, Theorem 1.1, σ algebra, and unit norm claims at [docs/pentagonal-torsion-derivation.md:21](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/pentagonal-torsion-derivation.md:21), [28](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/pentagonal-torsion-derivation.md:28), [42](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/pentagonal-torsion-derivation.md:42), [52](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/pentagonal-torsion-derivation.md:52), [59](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/pentagonal-torsion-derivation.md:59), [133](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/pentagonal-torsion-derivation.md:133): algebraically OK. `N(u)=uσ(u)` is the field norm, not a new torsion character.
- “Pentagonality is canonical” at [91](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/pentagonal-torsion-derivation.md:91): OK for `n=3,4,5,6`; the broader “exactly when `5 | n`” at [106](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/pentagonal-torsion-derivation.md:106) is true but not proved there.
- “Pentagonal chirality theorem” at [145](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/pentagonal-torsion-derivation.md:145): over-claim. The proof establishes norm-sign nontriviality only. It does not establish chirality, monodromy, or a geometric obstruction.
- `2I` order distribution / two order-10 classes / τ coordinates at [176](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/pentagonal-torsion-derivation.md:176): supported by B5/B6. But τ is canonical only after choosing one of two order-10 conjugacy classes.
- “τ⁵ = -1 is the pentagonal torsion element” at [198](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/pentagonal-torsion-derivation.md:198): τ⁵ = -1 is proved for chosen τ; identifying it with the §4 norm-sign torsion remains a bridge, not a theorem.
- Clock map and B6 facts at [230](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/pentagonal-torsion-derivation.md:230), [236](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/pentagonal-torsion-derivation.md:236): supported computationally. Left multiplication is verified, not justified as uniquely canonical over right multiplication/conjugation.
- Cocycle claims at [255](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/pentagonal-torsion-derivation.md:255), [272](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/pentagonal-torsion-derivation.md:272), [282](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/pentagonal-torsion-derivation.md:282): not established. B7/B8 does not construct `ω : edges -> Z[φ]×`, does not prove gauge-independence, and shows σ does not preserve a single `2I`.
- Weighted zeta at [302](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/pentagonal-torsion-derivation.md:302): formal only. The formula is ambiguous for `v in Fix(T^n)` when the primitive period divides `n`; it should use the `n`-step product, not an unspecified primitive orbit weight.
- Summary claims at [344](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/pentagonal-torsion-derivation.md:344) and “Derived” at [361](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/pentagonal-torsion-derivation.md:361): false as written. The cocycle and weighted zeta are not derived.

**WO Acceptance Audit**

- Checklist 1: resolved. σ(φ) = -1/φ is correct.
- 2: partially resolved. Small `n` checked; general conductor claim not proved.
- 3: resolved algebraically. It is the field norm; geometric use remains open.
- 4: not resolved. The sign is proved; “chirality obstruction” is not.
- 5: partially resolved. B5/B6 proves two order-10 classes, not unique τ.
- 6: partially resolved. Left clock works computationally; canonicity versus right/conjugation is not closed.
- 7: not resolved. B7/B8 exposes that naive cocycle is trivial and σ-covariance on one `2I` fails.
- 8: not resolved. σ symmetry and Mellin/critical-line bridge remain undefined.

Required outputs A-F in the WO are not delivered by the current derivation: no insight line audit, no full named-build table with routes and first steps, no revert-string section, no real alternatives/tradeoffs beyond one B8 note, no per-build exact verification targets, and no ranked top-three build list.

**Catalogue Audit**

No dedicated pentagonal-clock math catalogue was supplied or found. Existing catalogue files are for adjacent tracks, not this derivation. Therefore every introduced object is currently uncatalogued: `F1`, Theorem 1.1, Definitions 2.1/2.3/4.2/6.1/6.3/7.1/7.2, Theorems 2.2/3.2/3.3/4.4, Propositions 2.4/4.1/4.3/5.3/6.2/6.4/6.5/7.3, Corollaries 2.5/4.5/5.4, Facts 3.1/5.1/5.2, and B5-B8 numerical findings. Defect.

**Attribution / External Consistency**

- F1 attribution is correct: foundations states only `r = 1 + 1/r` and φ uniqueness at [foundations.tex:116](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-correspondence-foundations/foundations.tex:116) and explicitly limits scope at [204](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-correspondence-foundations/foundations.tex:204).
- Paper XXII supports `2I` closure, nearest shell as one conjugacy class, and shell/class bijection at [paper-xxii.tex:171](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/paper-xxii/paper-xxii.tex:171), [200](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/paper-xxii/paper-xxii.tex:200). It also explicitly avoids “double cover” language for the `240/120` pairing at [238](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/paper-xxii/paper-xxii.tex:238).
- B5/B6 attribution is correct for order counts, two order-10 classes, τ⁵ = -1, 12 cycles, and unweighted zeta; see [derive_pentagonal_clock_B5_B6.py:145](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-derivation/scripts/derive_pentagonal_clock_B5_B6.py:145), [169](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-derivation/scripts/derive_pentagonal_clock_B5_B6.py:169), [223](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-derivation/scripts/derive_pentagonal_clock_B5_B6.py:223).

**Sim Correctness**

The three B7/B8 findings are mostly correct, with one important correction.

- Correct: all 1440 directed adjacency transports fall in one order-10 conjugacy class. Script output comes from [derive_pentagonal_clock_B7_B8.py:215](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-derivation/scripts/derive_pentagonal_clock_B7_B8.py:215); orders from identity are `{10: 12}` at [244](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-derivation/scripts/derive_pentagonal_clock_B7_B8.py:244).
- Correct: componentwise σ does not preserve this `2I`; exactly 24/120 vertices remain in `2I`, and in fact those 24 are fixed. See [248](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-derivation/scripts/derive_pentagonal_clock_B7_B8.py:248). The final summary contradicts this at [371](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-derivation/scripts/derive_pentagonal_clock_B7_B8.py:371), falsely saying σ permutes `2I`.
- Correct: naive `ω(v,Tτ(v))=τ` is constant, so cycle product is `τ^10=1`; weighted zeta collapses to unweighted. See [326](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-derivation/scripts/derive_pentagonal_clock_B7_B8.py:326).
- Not correct as stated: the “1/3/8 split” at [365](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-derivation/scripts/derive_pentagonal_clock_B7_B8.py:365) is only the class of `min(cycle)` by array index. The cycles are not generally contained in single conjugacy classes. Exact check gives invariant class-profile patterns `1,1,5,5`, not a well-defined 1/3/8 H4-class distribution.

Revised build name: **B8' — H4/2I class-profile cycle weighting**. Define weights from the full conjugacy-class profile of each `Tτ` cycle, not from an arbitrary representative. Then prove profile invariance, σ-pair formulation on `2I ∪ σ(2I)`, and assignment into `Z[φ]×`.

Can the programme proceed to B9? **No.** B9 is blocked until B8' supplies a canonical nontrivial weight.

**Tightness**

- [docs/pentagonal-torsion-derivation.md:5](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/pentagonal-torsion-derivation.md:5): replace “No step assumes what it is trying to derive” with “The algebraic F1-to-σ part is complete; B4-B13 remain proof obligations.”
- [docs/pentagonal-torsion-derivation.md:341](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/pentagonal-torsion-derivation.md:341): replace “Cocycle `ω(v,w)=φ^{k(v,w)}`” with “Cocycle not yet constructed; naive transport cocycle is trivial on `Tτ`-orbits.”
- [derive_pentagonal_clock_B7_B8.py:371](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-derivation/scripts/derive_pentagonal_clock_B7_B8.py:371): replace “σ permutes 2I” with “σ does not preserve a single 2I; covariance must be reformulated on the conjugate pair.”

**Top Three Fixes**

1. Retract derived cocycle/zeta claims at [docs/pentagonal-torsion-derivation.md:361](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/pentagonal-torsion-derivation.md:361). They are open.
2. Replace B8 representative-class weighting with B8' class-profile weighting at [derive_pentagonal_clock_B7_B8.py:353](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-derivation/scripts/derive_pentagonal_clock_B7_B8.py:353).
3. Fix σ-covariance claims on single `2I` at [docs/pentagonal-torsion-derivation.md:272](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/pentagonal-torsion-derivation.md:272) and [derive_pentagonal_clock_B7_B8.py:371](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-derivation/scripts/derive_pentagonal_clock_B7_B8.py:371).

**Verdict**

Publication ready: no.
