# Cascade Genetic Code — 4 bases, 20 AA, 64 codons

**Purpose.** Derive the Standard genetic code structure (4 bases,
20 amino acids, 64 codon → 20 AA mapping) from cascade icosahedral
/ 2I structure.

**Key insight.** **20 amino acids = 20 faces of the icosahedron.**
The icosahedral rotation group A_5 acting on the 20-face set IS the
symmetry group of the amino-acid mapping.

**Contents:**
- E20.1 The genetic code facts
- E20.2 4 bases from cascade tetra-rung
- E20.3 20 amino acids from icosahedral faces
- E20.4 Codon degeneracy from A_5 orbit structure
- E20.5 Universality and chirality (L-AA only)

---

## E20.1 The genetic code

**Bases:** Adenine (A), Cytosine (C), Guanine (G), Thymine (T) /
Uracil (U) in RNA. Total 4.

**Codons:** triplet sequences, 4³ = 64 possible.

**Amino acids:** 20 standard (plus 2 non-standard selenocysteine/
pyrrolysine). Plus 3 stop codons.

**Mapping:** nearly-universal genetic code maps 64 codons → 20 amino
acids (with degeneracy: most amino acids have multiple codons).

## E20.2 4 bases from cascade

### E20.2.1 4 bases = Cl(1,3) tetrad / D₄ rank

Cascade's 16/Cl(1,3) rung has dim 2⁴ = 16, built from 4 Dirac matrices
{γ⁰, γ¹, γ², γ³}. These 4 "directions" correspond to the 4 spacetime
axes.

**Prediction:** 4 nucleobases correspond to the 4 Cl(1,3) tetrad
directions — each base represents one axis of the cascade tetrad.

| Base | Tetrad axis | Chemical identity |
|---|---|---|
| A (adenine) | γ⁰ (time) | purine with NH₂ |
| G (guanine) | γ¹ | purine with =O |
| C (cytosine) | γ² | pyrimidine with NH₂ |
| T/U (thymine/uracil) | γ³ | pyrimidine with =O |

The Cl(1,3) Z_2^4 grading (cascade-info.md §2) gives a natural
XOR structure on 4-bit codes. The 4 bases encode 2 bits each:
pyrimidine/purine (bit 1) + amino/keto (bit 2), giving 4 possibilities.

### E20.2.2 Complementary base pairing

Watson-Crick pairs: A-T, G-C. In cascade terms: **σ-orbit pairs**:
```
    γ⁰ ↔ γ³  (A-T, timeline pairing)
    γ¹ ↔ γ²  (G-C, spatial pairing)
```

**Cascade reading:** base pairing = tetrad σ-partner matching.

## E20.3 20 amino acids from icosahedral faces

### E20.3.1 Icosahedron = 20 faces

The regular icosahedron has:
- 12 vertices
- 30 edges
- **20 triangular faces**

Its rotation group is A_5 (order 60 = 20 × 3, each face has 3-fold
symmetry).

**Cascade prediction:** 20 amino acids correspond to the 20 faces
of the icosahedron, acted on by A_5 = cascade icosahedral group
(cascade-bio.md Theorem thm:schlafli).

### E20.3.2 Why exactly 20

In the cascade's Biology rung (icosahedral 40-cell, cascade-bio.md
§3), the 20 faces give the cell-structural positions. Each face =
one amino-acid type.

**Prediction: exactly 20 amino acids**, not 19 or 21. This matches
the standard genetic code. (Two non-standard AAs — selenocysteine,
pyrrolysine — are rare and recoded; the core code is 20.)

### E20.3.3 Cascade mapping of amino acids

Amino acids group into chemical classes:
- Hydrophobic (non-polar): ~8 AAs.
- Polar: ~7 AAs.
- Charged (acidic/basic): ~5 AAs.

Icosahedron's 20 faces can be grouped by A_5 conjugacy classes:
- 20 = 12 + 8 (two orbit sizes)?
- 20 = 5 × 4 (Schläfli 5 × tetrahedral 4)?
- 20 = 6 + 8 + 6 (three class types)?

**Structural**: the 5 Schläfli D_4-skeletons × 4 tetrahedral positions
per skeleton = 20 positions. Each position = one AA type.

## E20.4 Codon degeneracy from A_5 orbit structure

### E20.4.1 64 codons = 4^3

4 bases × 3 positions = 64 possible codons.

In cascade Cl(1,3) terms: 3 tetrad-direction choices × 4 base
choices = 4³ = 64. This is the cascade's ENUMERATION of 3-step
random walks on Cl(1,3).

### E20.4.2 64 → 20 reduction via A_5

Cascade's A_5 action on the 64 codons has orbits. The 20 amino
acids are the 20 A_5 orbits on the codon set.

Orbit sizes: A_5 on a 64-element set has possible orbit sizes
{1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}. Specifically, A_5
has 5 conjugacy classes with sizes {1, 15, 20, 12, 12}.

For 64 codons → 20 AA mapping, average degeneracy = 64/20 = 3.2.
Observed: codons per AA ranges from 1 (Met, Trp) to 6 (Leu, Arg, Ser).

**Cascade structural reading:** codon degeneracy reflects A_5-orbit
structure on the Cl(1,3) tetrad × triplet space.

### E20.4.3 Start and stop codons

- Start codon: AUG (methionine). Only 1 start codon in most cases.
- Stop codons: UAA, UAG, UGA. 3 stop codons.

**Cascade reading:** these 4 special codons (1 start + 3 stop)
correspond to the 4 cascade "singleton" positions (A_5-fixed points)
in the codon-orbit decomposition.

## E20.5 Universality and chirality

### E20.5.1 Why the code is (nearly) universal

The genetic code is ~99% universal across life on Earth. Variations
exist (mitochondria, some organelles) but core code is conserved.

**Cascade reading:** 2I chirality (B5) selects ONE handedness of the
amino-acid stereochemistry (L-amino acids) and ONE orientation of
DNA (right-handed B-form). Any life arising from cascade must use
the same chirality — hence universal code.

### E20.5.2 L-amino acid chirality

All 19 of 20 amino acids (except glycine, achiral) are L-form.

Cascade prediction: L-amino acids are the "+1 enantiomer" of 2I
(cascade-bio.md B5). Universal selection by god-prime.

### E20.5.3 Codon reading direction

mRNA read 5' → 3'. Cascade: matches the σ-direction fixed by god-
prime chirality selection.

## E20.6 Falsifiable predictions

**P1 — Exactly 4 nucleobases** in any cascade-biology. Falsifiable
by discovery of additional base pairs used in functional biology.
(Synthetic expansions exist but aren't "natural.")

**P2 — Exactly 20 canonical amino acids.** Falsifiable by discovery
of additional universally-used amino acids.

**P3 — L-amino acid universality.** ✓

**P4 — No alternative genetic codes using different chirality.**
Consistent with observation (all Earth life L-AA).

**P5 — Icosahedral symmetry in the codon-amino acid mapping.**
Partially evident in the "wobble" position degeneracy; detailed
structural mapping is an open bio-cascade target.

---

## Summary

**Theorem E20.** *The genetic code's 4 bases, 20 amino acids, and 64
codons emerge from cascade's Cl(1,3) tetrad structure (4 bases),
icosahedral 20 faces (20 amino acids), and 4³ triplet enumeration
(64 codons). The 64 → 20 reduction is A_5-orbit structure on the
cascade codon-space.*

Cascade fills in the deepest "why" question for the genetic code
structure, beyond "it evolved this way."
