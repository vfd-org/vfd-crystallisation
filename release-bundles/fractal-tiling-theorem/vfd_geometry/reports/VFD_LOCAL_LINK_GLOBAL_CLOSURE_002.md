# WO-VFD-LOCAL-LINK-GLOBAL-CLOSURE-002 — Local-Link to Global-Closure (report)

**Status:** run; **local-link picture VALIDATED as a precise restatement of known
regular-polytope/Coxeter geometry; one WO error caught (24-cell vertex figure);
one genuine refinement (closure = PD geometry + rational dihedral angle).**
Modules: `local_links.py`, `coxeter_signature.py`, `run_local_link_global_closure.py`.
**No proof of RH/physics; no claim φ governs all geometry; no new VFD law.**

## 1. Summary
Tested the sharper rule suggested by the prior WO ("H3 = vertex figure of H4"):
*a higher-dimensional polytype is stable when a lower-dimensional symmetry serves
as the consistent local link around every vertex.* Findings:
1. **Vertex figures all validate** (9/9 anchors), including correcting the WO's
   own error: the **24-cell vertex figure is a cube `{4,3}` (8 vertices), not an
   octahedron**. `{3,4,3}` → vertex figure `{4,3}` = cube. The engine detects it.
2. **600-cell link = icosahedron CONFIRMED** — the H3 ⊂ H4 prototype.
3. **Refinement of the closure criterion (genuine, but classical):** finite
   global closure ⟺ the Coxeter Gram is **positive-definite (spherical curvature)
   AND the dihedral angle is π/integer (rational holonomy)**. The determinant
   alone classifies **curvature, not group finiteness**: a *generic* `q` gives a
   PD (spherical) form yet an **infinite** group — even `q=1.62`, right beside
   φ, explodes (its angle is π/5.013, non-integer). So φ is an **exact isolated**
   closure point, not a basin.
4. **No clean local→global spectral induction:** the icosahedron's adjacency
   eigenvalues `{5, ±√5, −1}` share **nothing** with the 600-cell's
   `{12, 9.71, 6.47, 3, 0, −2, −2.47, −3, −3.71}`.

**The "Local-Link Closure Law" = this classical condition restated. Real and
useful as a restatement, not new mathematics.**

## 2. Why this followed
The base engine recovered Coxeter finiteness; the standing-wave WO found the one
genuine structural fact (H3 ⊂ H4 vertex figure). This WO sharpened "transforms by
pressure" into "closes when local links glue" — the correct framing — and tested
it precisely.

## 3. Local-link hypothesis
A stable higher polytype exists when a lower-dim symmetry is the link of every
vertex and glues across all adjacencies with vanishing residual. Tested via
vertex-figure extraction + Coxeter classification + orbit generation.

## 4. Method
`link_graph(V,i)`: neighbours of vertex `i` at min distance, with link-edges =
neighbour pairs themselves at min distance (the vertex figure). Classify by
(vertices, degree, adjacency spectrum). `coxeter_signature`: Gram determinant →
spherical / affine / hyperbolic; compare to base-engine orbit generation.

## 5. Anchor validation (vertex figures)

| polytope | V | link size | detected | classical | match |
|---|---|---|---|---|---|
| tetrahedron | 4 | 3 | triangle | triangle | ✓ |
| cube | 8 | 3 | triangle | triangle | ✓ |
| octahedron | 6 | 4 | square | square | ✓ |
| icosahedron | 12 | 5 | pentagon | pentagon | ✓ |
| dodecahedron | 20 | 3 | triangle | triangle | ✓ |
| 16-cell | 8 | 6 | octahedron | octahedron | ✓ |
| tesseract | 16 | 4 | tetrahedron | tetrahedron | ✓ |
| **24-cell** | 24 | **8** | **cube** | **cube `{4,3}`** | ✓ (WO said octahedron — **wrong**) |
| **600-cell** | 120 | **12** | **icosahedron** | **icosahedron** | ✓ |

All links uniform across vertices (single link spectrum per polytope) — the
gluing is globally consistent, as expected for regular polytopes.

## 6. 600-cell / H3 result
600-cell vertex figure = icosahedron (12 neighbours, degree 5, spectrum
`[1,3,5,3]`). This is the **H3 ⊂ H4** local-link containment — the real,
non-narrative prototype for "H3 refolds into H4." (Classical; verified.)

## 7–8. Coxeter classifier vs orbit — and the key subtlety

| diagram | q | Coxeter class | curvature | orbit |
|---|---|---|---|---|
| [5,3] (φ) | 1.6180 | spherical | + | **finite 120** (H3) |
| [4,3] (√2) | 1.4142 | spherical | + | finite 48 (B3) |
| [6,3] (√3) | 1.7321 | affine | 0 | non-PD (∞) |
| [7,3] | 1.8019 | hyperbolic | − | non-PD (∞) |
| **generic q=1.50** | — | **spherical (PD!)** | + | **EXPLODES (∞)** |
| **generic q=1.62** | — | **spherical (PD!)** | + | **EXPLODES (∞)** |

**The crux:** a PD Gram means **spherical geometry**, but a **finite reflection
group** *additionally* requires the dihedral angle to be **π/integer** (rational).
Generic `q` is PD yet its angle `π/m` has non-integer `m` → the group is infinite
(dense), the links never glue (nonzero rotational **holonomy** residual), the
orbit explodes. So the determinant classifies **curvature, not finiteness**; orbit
generation is the true closure test. **`q=1.62` (≈ but ≠ φ) explodes** — φ is an
exact isolated value (`m=5`), confirming the base-engine "measure-zero" finding
from the local-link side.

## 9. q-scan reinterpreted (link-closure)
Finite closure occurs only at exact `q = 2cos(π/m)`, integer `m` — where the local
link glues with **zero holonomy**. φ is the exact **5-fold** H-type gluing value
(not a stability basin). This is the disciplined restatement of φ's role.

## 10. Curvature / angle residual
Tied to the determinant sign: spherical (PD, positive curvature) ↔ finite-capable;
affine (PSD, flat) ↔ marginal/∞; hyperbolic (indefinite, negative) ↔ ∞. The
*additional* finiteness condition is angular rationality (holonomy = 0). This is
the classical Schläfli/Coxeter picture.

## 11. Local vs global spectra (Phase 6, honest)
Icosahedron adjacency eigenvalues `{5, √5(×3), −1(×5), −√5(×3)}`; 600-cell
`{12, 9.71, 6.47, 3, 0, −2, −2.47, −3, −3.71}`. **Zero shared values** — the link
spectrum is **not** a subset of the global spectrum, and there is **no clean
local→global spectral induction** (global modes are set by the global graph).
The H3 ⊂ H4 relation is *structural* (vertex figure), not spectral-inductive.

## 12. Failure cases
Generic `q` (1.50, 1.62, 1.66): PD-but-irrational → infinite group → orbit
explosion = links cannot glue (nonzero holonomy). Affine/hyperbolic `q`: non-PD →
infinite. All failure modes = nonzero closure/holonomy residual, as hypothesised.

## 13. Candidate law — verdict
> **Local-Link Closure Law (correct, classical form):** a finite global polytype
> exists ⟺ its Coxeter Gram is positive-definite (spherical) **and** every dihedral
> angle is π/integer (rational holonomy), so the uniform local links glue with zero
> residual. φ = the exact 5-fold (π/5) H-type gluing value.

This is **viable and exactly correct** — and it is the **classical Coxeter/Schläfli
finiteness theorem** stated in local-link language. It is **not new mathematics**.

## 14. Obstructions & limits
- Vertex figures and the finiteness criterion are classical (recovered).
- The determinant gives only curvature; finiteness needs the integrality
  (rational-angle) condition — so a "determinant-only" closure rule is incomplete.
- No local→global spectral induction (Phase 6 negative).
- The H3 ⊂ H4 relation is structural, not a generative law across families.

## 15. What this does and does NOT claim
- **Does:** validate all vertex figures (and correct the WO's 24-cell error);
  confirm H3 ⊂ H4; establish the correct closure condition (PD + rational angle =
  zero holonomy); show generic-q (incl. near-φ) explosion; show no spectral
  induction.
- **Does NOT:** establish a new VFD law (the criterion is classical Coxeter);
  claim φ universal; claim local→global spectral induction; complete H4→E8.

## 16. Recommended next WO
This is the WO's **"validate the local-link picture as a restatement of known
geometry"** outcome → **WO-VFD-LOCAL-LINK-ATLAS-003** (a validated atlas of
vertex-figure / closure relations as a VFD reference tool) is the honest next
step. The one genuinely *open* technical thread is **WO-VFD-H4-E8-TRACE-FORM-003**
(implement the weighted Q(√5) trace form to test the exact `E8 = H4 + φH4` gluing
the prior WO only reproduced partially). A new-law claim is **not** warranted.
