**Audit Result**

I read the seven named artefacts fully and ran all four verification scripts with `python3`; the advertised pass counts are real. They do not justify several theorem-grade labels. The main document with load-bearing problems is `docs/narrative-gap-closure.md`.

**1. CLOSED-vs-REDUCED Audit**

| Gap | Label honesty |
|---|---|
| G1 | **REDUCED is broadly honest, but the reduction is not proven.** N8 only proves a linear/SPD toy and a telescoping scalar-loop identity. Paper XXXIII still has schematic `Delta_cl` and lists multi-observer compatibility open (`papers/paper-xxxiii/paper-xxxiii.tex:418,445`). |
| G2 | **CLOSED is dishonest.** This is relabeling an open analytic support claim as a definition. N2 proves only: if you zero the bulk component by hand, the bulk does not change (`scripts/verify_narrative_closure.py:134-155`). `closure-cosmogenesis.md:168-176` still asks for exactly the missing theorem. |
| G3 | **Over-closed.** The centered-stencil Taylor step is fine, but only inside a chosen 3-point linear stencil family. N3d is an unconditional `True` assembly check (`scripts/verify_narrative_closure.py:187-189`). |
| G4 | **CLOSED is dishonest.** “Function of graph-distance to a 20-vertex bulk set” is not isotropy about an observer point. CV `0.172` is a real spatial variation; “not free” does not mean “not observable” (`docs/narrative-gap-closure.md:70-78`, `scripts/verify_narrative_closure.py:211-235`). |
| G5 | **Mostly honest for local chart primitives.** The octonion exponential/frame construction is plausible; the sim checks only origin derivatives and sampled anchors, not a full scene theorem (`scripts/verify_narrative_closure.py:260-290`). |
| G6 | **Plausible but under-proved.** The sim checks centraliser size numerically but the theorem needs a finite-group centraliser lemma; N6b labels `det 1` but does not test determinant (`scripts/verify_narrative_closure.py:296-336`). |
| G7 | **REDUCED is honest.** The negative search proves little, but the residual is named. Do not call the Coxeter basis “bookkeeping” unless imported constructively (`scripts/verify_narrative_closure.py:340-389`). |
| G8 | **Contains a load-bearing algebra error.** `diag(0,I3)` is the spatial projector, not `eta+2uu = diag(1,1,1,1)` in the stated convention (`docs/kappa-derivation-math.md:166-169`; G8 at `docs/narrative-gap-closure.md:116-126`). |
| G9 | **Should be SCOPED/TOY, not REDUCED.** A random diagonal `D` generically breaks degeneracy. That is a linear-algebra triviality, not a substrate selection result (`scripts/verify_narrative_closure.py:487-512`). |
| G10 | **SCOPED is honest.** But the cited Hopf fibre construction is not verified; `cascade-bio.md` says it is pending (`papers/cascade-derivation/cascade-bio.md:149-160,443-451`). |

**2. SIM-vs-CLAIM Correctness**

- N2a/N2b/N2c: circular. Boundary projection is imposed at `scripts/verify_narrative_closure.py:139`; the “iff” at lines `153-155` is not tested.
- N3a: valid only for normalized symmetric 3-point stencils. N3b is mislabeled: the forward difference is not shown “reversal-odd” (`170-176`). N3d is a stub (`187-189`).
- N4a: fine for antipodal boundary preservation. N4b tests `A`, not `A sigma_c` (`206-210`). N4c supports distance-to-bulk shells for one `r=1` background, not isotropy (`211-235`). N4d is a status flag.
- N5a-c: local chart derivative checks only; good as smoke tests, not full S7 rendering closure (`260-290`).
- N6a-d: useful finite checks, but N6a tests containment not equality, N6b omits determinant, and `Lambda` is never formalised as more than clock powers (`296-336`).
- N7: passing because a limited search fails is not evidence for the Coxeter loop (`340-389`).
- N8a: vacuous curl test; any scalar field has zero telescoping loop sum (`424-430`). N8b: SPD inverse symmetry by construction (`436-442`).
- N9a: proves static orthonormal-frame bilinear only. N9b makes the false trace-reversal inference (`445-471`).
- N10a: real degeneracy check. N10b-e: generic random perturbation/descent toy; N10d is in-block by construction and N10e is a status flag (`475-512`).

**3. Supporting Theorem Audit**

- Rendering Thm 2.2: central class-sum proof needs an explicit “all central character scalars are distinct” lemma; otherwise square irrep blocks can merge (`docs/rendering-layer.md:34-42`).
- Rendering Thm 2.3: depends on irreducibility/branching of `V_k|_{2I}` for `k<=5`; cite/prove the character table, not just McKay prose (`46-56`).
- Rendering Thm 3.1: mathematically fine, but uniqueness is essentially imported by K4, the response equation (`72-84`).
- Rendering Prop 5.2: inner reversal forbids odd time terms under strong effective-equation assumptions; it does not alone derive the wave equation (`156-164`).
- Rung Thm 3.2: conditional on irreducibility; the verifier checks scalar action/rank, not irreducibility (`docs/rung-dimension-ladder.md:34-42`).
- Rung Thm 3.4: design-injectivity proof is fine, but design strengths need explicit citations/proofs; sharpness is numerical (`50-59`).
- Rung Thm 7.1: association-scheme proof is under-verified. Counting inner-product classes and eigenspaces is not a commutative Bose-Mesner proof; V24 is claimed but not checked in C1 (`107-112`, `scripts/verify_ladder_completion.py:210-235`).

**4. Attribution Consistency**

- `closure-cosmogenesis.md` supports conditional bulk invariance, not G2 closure: compare `84-90` with still-open `168-176`.
- `kappa-derivation-math.md` explicitly says trace-reversed coupling is not derived (`287-300`), so G8 overclaims.
- `aria-closure-kernel.md` says selection remains open and response does not reduce it (`216-257`), so G9’s reduction is not attributable there.
- `cascade-bio.md` identifies the 15x40 Hopf target but says verification is pending (`443-451`); ladder C5f checks only arithmetic.
- Paper XXXIII does not provide the actual residual needed for G1; it says the residual is schematic and compatibility remains open (`418,445`).

**5. Hidden Retreats / Over-closures**

The main pattern is semantic closure: G2 defines away support, G4 renames anisotropy as fixed radial texture, G8 renames a spatial projector as trace reversal, and G9 renames generic perturbation theory as selection. Those are not derivations.

**6. Top Five Derivation Targets**

1. Prove actual boundary support: from explicit `Delta_cl`, show `rho_t^B=0`, or derive a projected residual law that preserves the projection principle (`docs/narrative-gap-closure.md:42-50`; `docs/closure-cosmogenesis.md:168`).
2. Derive real isotropy: prove observer-indistinguishability or vanishing continuum anisotropy, not merely distance-to-bulk-set constancy (`docs/narrative-gap-closure.md:70-78`).
3. Fix GR algebra: derive `eta+2uu` or the trace-reversed source from a substrate action; do not use `diag(0,I3)` as a substitute (`docs/narrative-gap-closure.md:116-126`).
4. Replace N8 with a real nonlinear integrability test: explicit `Delta_cl`, discrete curl of the argmin one-form, and counterexample/null handling (`scripts/verify_narrative_closure.py:400-442`).
5. Derive the selection functional: replace random `D` with a canonical substrate `V_sel` and a nontrivial null where generic perturbations are insufficient (`docs/narrative-gap-closure.md:134-140`).

**7. Verdict Per Document**

- `docs/narrative-gap-closure.md`: **contains a load-bearing error**.
- `scripts/verify_narrative_closure.py`: **contains load-bearing verification errors**.
- `docs/rendering-layer.md`: **needs the listed fixes**.
- `scripts/verify_rendering_layer.py`: **needs the listed fixes**.
- `docs/rung-dimension-ladder.md`: **needs the listed fixes**.
- `scripts/verify_rung_dimension_ladder.py`: **needs the listed fixes**.
- `scripts/verify_ladder_completion.py`: **needs the listed fixes**.
