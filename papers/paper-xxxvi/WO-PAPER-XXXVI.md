# WO-PAPER-XXXVI — Cascade Foundations: F1 through F8 Consolidated

## Programme Position
This paper is the mathematical spine of the VFD programme. It consolidates the eight cascade-foundation theorems (F1–F8, currently developed across multiple markdown files in `papers/cascade-derivation/`) into one rigorous publishable paper. Without this consolidation every downstream claim has an implicit axiom chain that is not written in one place. XXXVI is the reference every subsequent paper cites when it says "by cascade foundations…"

## Scope
- State and prove F1 (base permeability $r = \varphi$ from self-similarity + Banach fixed-point).
- State and prove F2 (closure functional $F = \alpha R + \beta E - \gamma Q$ from minimal-order invariants).
- State and prove F3 (7-rung cascade $E_8 \to H_4 \to 40 \to D_4 \to 16 \to 8 \to 0$ from finite-Coxeter classification).
- State and prove F4 ($\mathrm{coker}(F) = 24^2 + 7$ as a theorem of rigorous linear algebra).
- State and prove F5 ($\sigma$-invariance of $F$ from rational-coefficient structure).
- State and prove F6 (Burago–Ivanov continuum hypotheses verified for the cascade's discrete-to-smooth passage).
- State and prove F7 (rank-2 $\Lambda$ on $D_4$ from Fierz–Pauli / Deser bootstrap rigour).
- State and prove F8 (the three coefficients $\alpha, \beta, \gamma$ fixed by cascade couplings: Newton's $G$, $\alpha_{\mathrm{em}}$ from Paper XXII, $\sin^2\theta_W$ from cascade-qm).
- Prove the zero-parameters corollary: the cascade has no free parameters after the coupling-matching of F8.
- Prove the $\Lambda$ derivation: $\Lambda \cdot \ell_P^2 = 2\varphi^{-583}$ as a theorem chain.

## Inputs
- Prior papers: I–V (mass core uses F1–F3 implicitly); XXII (spectral bridge, supplies $\alpha_{\mathrm{em}}$ and $\sin^2\theta_W$ for F8); XXIII–XXVII (GR scaffolding, supplies the $D_4$ context for F6/F7); XXXV (three-pillar synthesis, references F1–F8 by name).
- Cascade-derivation source: `cascade-foundations.md` (920 lines), plus supporting files `cascade-lambda.md`, `cascade-embeddings.md`, `cascade-hierarchy.md`, `cascade-constants-extended.md`, `cascade-metaprinciples.md`, `cascade-mathematics-emergence.md`, `WO-CASCADE.md` (the cascade-derivation work order).
- External mathematics: Banach fixed-point theorem; finite-Coxeter classification (Coxeter 1934, Bourbaki, Humphreys); Fierz–Pauli spin-2 uniqueness; Deser self-coupling bootstrap; Burago–Ivanov / Gromov–Hausdorff convergence; Schläfli differential formula; rational-coefficient invariant theory.

## Outputs
- Observable predictions: none directly — this is a structural foundations paper. However, the paper's F8 corollary (zero free parameters) and its $\Lambda$-derivation chain are pre-requisites for every downstream observable claim.
- Structural theorems: **Theorem F1** through **Theorem F8**, each as a labelled theorem in the paper. Plus the overarching **Cascade Theorem** ("the 7-rung cascade is uniquely determined by F1–F8 up to the choice of rung-0 boundary condition"). Plus the **Zero-Parameter Corollary** and the **$\Lambda$-Derivation Theorem**.
- Additions to VFD Explorer library: `cascade_foundations_check.py` (verifies F1 iteration convergence numerically; confirms F3 rung cardinalities; confirms F4 coker count; confirms F8 coefficient matching), `lambda_derivation.py` (computes $\varphi^{-583}$ and the coupling chain).

## Key derivations needed
1. **F1 proof.** Self-similarity axiom $r(2L) = 1 + 1/r(L)$ + fixed-point condition $r(2L) = r(L)$ gives quadratic $r^2 - r - 1 = 0$. Banach fixed-point theorem applied to $T(r) = 1 + 1/r$ on $[1,2]$ with Lipschitz constant $4/9 < 1$ proves uniqueness and global attraction. Output: $r = \varphi$ rigorously.
2. **F2 proof.** Variational argument: the only closure functional respecting closure, energy, and charge invariants at leading order with rational coefficients is $F = \alpha R + \beta E - \gamma Q$, with the three coefficients free parameters at this stage (pinned by F8).
3. **F3 proof.** Finite-Coxeter classification says the only finite real irreducible Coxeter groups in dimension $\geq 4$ are $A_n, B_n, D_n, E_6, E_7, E_8, F_4, H_3, H_4$. The cascade's self-similarity (F1) plus E8 maximality selects the unique chain $E_8 \to H_4 \to 40 \to D_4 \to 16 \to 8 \to 0$. Each reduction is a specific polytope projection (Coxeter, icosahedral, D-series, hypercube, octonionic, point).
4. **F4 proof.** $\mathrm{coker}(F) = 24^2 + 7 = 583$ by direct linear algebra: the closure functional restricted to $E_8$ roots has a finite cokernel whose dimension is counted by orbit-decomposition of Coxeter elements. The exponent 583 is what appears in the $\Lambda$ formula.
5. **F5 proof.** Rational-coefficient structure of $F$ (from F2) is preserved under the $\sigma$ automorphism of $\mathbb{Z}[\varphi]$. This establishes the matter/antimatter duality used in Paper XXII.
6. **F6 proof.** Burago–Ivanov precompactness requires: (a) uniform bounded diameter, (b) lower Ricci bound, (c) volume non-collapse. Verify each for the Schläfli-refined $D_4$ metric candidates of Paper XXVII.
7. **F7 proof.** Rank-2 $\Lambda$ on $D_4$: by Fierz–Pauli, the only consistent spin-2 massless field on Minkowski space is the linearised Einstein field. Deser's bootstrap from self-coupling then gives full GR. Applied to the $D_4$ rung of the cascade, this forces rank-2 tensor structure as the gravitational sector.
8. **F8 proof.** The three coefficients $(\alpha, \beta, \gamma)$ of F2 are fixed by: $\alpha \leftrightarrow G$ (Newton's constant, via Paper XXIII's metric normalisation), $\beta \leftrightarrow \alpha_{\mathrm{em}}$ (Paper XXII's $\alpha^{-1} = 137 + \pi/87$), $\gamma \leftrightarrow \sin^2\theta_W = 3/8$ (Paper XXII / cascade-qm). Zero free parameters after this step.
9. **$\Lambda$ chain.** Combine F1 (gives $\varphi$), F4 (gives 583), F8 (gives coupling matches) to derive $\Lambda \cdot \ell_P^2 = 2\varphi^{-583} \approx 2.89 \times 10^{-122}$, comparing to CODATA 2022 observed value $\sim 2.88 \times 10^{-122}$ for agreement at 0.88%.

## Open questions / risks
- F4's exponent 583 needs a clean combinatorial proof, not just orbit-counting — if the cokernel dimension is not 583 in rigorous linear algebra, the $\Lambda$ derivation fails.
- F6's Burago–Ivanov hypotheses may not hold for every Schläfli refinement sequence — specific refinements must be selected to satisfy the lower Ricci bound. This overlaps with Paper XL.
- F8's coupling-matching is not a derivation of $G$, $\alpha_{\mathrm{em}}$, $\sin^2\theta_W$ from first principles — they are inputs. The "zero free parameters" claim applies after this input.
- The cascade's specific chain $E_8 \to H_4 \to 40 \to D_4 \to 16 \to 8 \to 0$ is one of several consistent finite-Coxeter chains; the F3 proof must show selection uniquely.
- Length risk: consolidating 920+ lines of markdown across multiple files into one proper paper may produce something too long. Consider an appendix structure or companion papers for F6 and F7 if the main paper bloats past 60 pages.

## Dependencies
- Blocked by: none (this is the root foundation paper).
- Blocks: XXXVII, XXXVIII, XXXIX, XL, XLII, XLIII, XLIV, XLV — all downstream new papers.

## Estimated scope
- Rigor level: rigorous-with-proofs
- Page count: 40–60
- Review rounds expected: 5–8 (this is the most important foundation paper; it must be tight)
