# WO-VFD-POLYTYPE-STANDING-WAVE-EXT-001 — Standing-Wave Extension (report)

**Status:** run; **spectra validated; one genuine structural finding (H3 ⊂ H4
vertex figure); the "φ-Closure Law" is NOT supported (honest negative).** Modules:
`standing_wave_modes.py`, `information_loading.py`, `symmetry_break_detector.py`,
`refolding_search.py`, `run_standing_wave.py`. **No proof of RH/physics; no claim
φ governs all geometry; no Symmetric Compression Law established.**

## 1. Summary
Added a standing-wave (graph-Laplacian/adjacency) layer to the base polytope
engine and tested the lifecycle "load → symmetry-break → refold." Findings:
1. **Spectra encode symmetry** — every polytope has a characteristic degeneracy
   signature (= irrep dimensions); the **600-cell** signature is
   `[1,4,9,16,25,36,9,16,4]` (the perfect squares 1²–6², summing to 120). Real,
   striking — and **known** spectral graph theory.
2. **Loading/perturbation splits degeneracies ~linearly** — standard level-
   splitting, recovered, not new.
3. **Refolding has a genuine basis:** the **icosahedron is the 600-cell vertex
   figure** (its 12 nearest neighbours form an icosahedron, adjacency degeneracy
   `[1,3,5,3]`), a true **H3 ⊂ H4** containment that the tesseract/24-cell/16-cell
   vertex figures lack. This is the real, non-narrative "H3 refolds into H4" fact.
4. **φ adds no robustness** — icosahedron (H3, φ) has a *smaller* spectral gap
   (2.76) than the octahedron (B3, √2; 4.0) and splits slightly *more* under
   perturbation. **The "φ-Closure Law" is not supported:** φ's role reduces to
   "φ is the tension where H3/H4 exist" (the base-engine finding), not a stability
   or capacity advantage.

**No new universal capacity/refolding invariant; no Symmetric Compression Law.**

## 2. Relationship to the base engine
The base engine (WO-…-TRANSFORMATION-ENGINE-001) showed φ is the 5-fold *closure
tension* (q=2cos(π/5)) — recovered Coxeter finiteness. This extension asked
whether the *dynamic* standing-wave story (saturation → breaking → refolding)
adds a new law. It does not: the spectral layer is known graph theory, and the
one real structural fact (H3 ⊂ H4) is classical polytope geometry.

## 3. VFD standing-wave hypothesis (tested)
"Polytypes are standing-wave carriers; loading saturates symmetry capacity, which
breaks and refolds into a higher polytype preserving an invariant." The testable
content: (a) degeneracy = capacity (yes, = irrep dims); (b) loading breaks
degeneracy (yes, linearly); (c) higher polytype absorbs the source (yes *iff*
genuinely contained — H3 ⊂ H4); (d) φ optimises refolding (**no**).

## 4. Graph/operator construction
1-skeleton via min-distance adjacency (`build_graph`); adjacency `A`, Laplacian
`L = D − A`; degeneracy signature, spectral gap/entropy, participation ratio.

## 5. Spectral results (Phase 2)

| polytype | V | degree | distinct eigs | adjacency degeneracy |
|---|---|---|---|---|
| triangle | 3 | 2 | 2 | [1,2] |
| tetra (A3) | 4 | 3 | 2 | [1,3] |
| octahedron (B3) | 6 | 4 | 3 | [1,3,2] |
| cube (B3) | 8 | 3 | 4 | [1,3,3,1] |
| **icosahedron (H3)** | 12 | 5 | 4 | **[1,3,5,3]** |
| 16-cell | 8 | 6 | 3 | [1,4,3] |
| tesseract | 16 | 4 | 5 | [1,4,6,4,1] |
| 24-cell (D4) | 24 | 8 | 5 | [1,4,9,8,2] |
| **600-cell (H4)** | 120 | 12 | 9 | **[1,4,9,16,25,36,9,16,4]** |

Degeneracies = dimensions of the symmetry group's irreducible representations —
genuine symmetry signatures, but standard.

## 6–7. Loading & symmetry-breaking thresholds (Phases 3–4)
Degeneracy splitting vs perturbation ε (topology fixed, metric strained):

| polytype | ε=0 | 0.02 | 0.05 | 0.10 |
|---|---|---|---|---|
| icosahedron (H3) | 0 | 0.027 | 0.066 | 0.127 |
| 600-cell (H4) | 0 | 0.391 | 0.961 | 1.892 |
| cube (B3) | 0 | 0.010 | 0.025 | 0.049 |

Splitting is **linear in ε** (level-splitting). The 600-cell splits most because
it carries the most (and highest) degeneracies — more modes to split, not a
special instability. No non-trivial "threshold"; the onset is smooth from ε=0.

## 8. Refolding (Phase 5) — the genuine result
The icosahedron (H3) is the **vertex figure** of the 600-cell (H4):

| target | vertex-figure size | is icosahedron? |
|---|---|---|
| **600-cell (H4)** | **12** | **YES** (degeneracy [1,3,5,3]) |
| tesseract | 4 | no |
| 24-cell (D4) | 8 | no |
| 16-cell | 6 | no |

So H3 sits *inside* H4 as its local standing-wave structure — a true structural
containment that justifies "H3 → H4 refolding" non-narratively. Unrelated
4-polytopes lack it. (This is classical: the 600-cell's vertex figure is an
icosahedron — verified here, not discovered.)

## 9. φ-tension under loading (Phase 6) — honest negative
| structure | spectral gap | splitting @ ε=0.05 |
|---|---|---|
| icosahedron (H3, φ) | **2.76** | 0.066 |
| octahedron (B3, √2) | **4.00** | 0.058 |

φ gives a **smaller** gap and **slightly more** splitting — i.e. **no robustness
or capacity advantage**. The "φ-Closure Law" (φ uniquely enables low-leakage
refolding) is **not supported**. φ is special only as the *tension where the
icosahedral group is finite* (base engine), not as a stability optimum.

## 10. Capacity law (Phase 7)
"Capacity" (degeneracy richness, distinct-eigenvalue count) grows with vertex
count and symmetry order — but monotonically and predictably (more vertices →
richer spectrum). There is **no exceptional capacity jump** at H4/600-cell beyond
what its size dictates, and **no invariant** that is preserved across families.
Capacity is descriptive, not a law.

## 11. Failure / leakage modes (Phase 8)
A perturbation off any symmetric configuration splits degeneracies (leakage);
larger/denser polytopes leak more in absolute terms. This is the geometric
echo of the RH-route "stable closure vs leakage" *shape*, but here it is
elementary perturbation theory, not a deep link.

## 12. Candidate VFD law — verdict
- **Symmetric Compression Law:** *not established.* No invariant survives across
  families; "capacity" is just spectrum size.
- **φ-Closure Law:** *refuted* in the stability sense (φ gives no robustness
  advantage; §9).
- What *is* true and useful: degeneracy = symmetry capacity (known); H3 ⊂ H4 as
  vertex figure (known, verified); these support a *spectral atlas*, not a law.

## 13. Obstructions
- The spectral layer is standard graph theory; degeneracy = irrep dims.
- Symmetry breaking is generic level-splitting (no special threshold).
- The one real containment (H3 ⊂ H4) is classical, not new.
- φ confers no stability/capacity advantage — refutes the φ-closure hypothesis.
- No cross-family invariant → no law.

## 14. What this does and does NOT claim
- **Does:** compute validated standing-wave spectra (degeneracy = symmetry);
  show loading splits degeneracies; verify the genuine H3 ⊂ H4 vertex-figure
  containment; honestly **refute** the φ-robustness/closure claim.
- **Does NOT:** establish a Symmetric Compression Law; show φ governs refolding;
  find a universal capacity invariant; connect to RH/black-holes beyond the
  shared "closure vs leakage" shape.

## 15. Recommended next WO
This is the WO's **"only atlas results"** outcome → **WO-VFD-POLYTYPE-SPECTRAL-
ATLAS-002**: a validated spectral atlas (degeneracy signatures, gaps, vertex-
figure containments) as a VFD *reference tool*. The **φ-closure** and
**Symmetric-Compression-Law** follow-ons are **not** warranted (one refuted, one
unsupported). The H3 ⊂ H4 containment is the single genuine thread worth keeping —
as documented geometry, not a new law.
