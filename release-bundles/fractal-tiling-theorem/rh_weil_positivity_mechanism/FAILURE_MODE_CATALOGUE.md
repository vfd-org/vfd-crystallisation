# Deliverable I — failure-mode catalogue

Every way this work could be (or was) overclaimed, and the guard against it.

1. **Finite positivity that does not generalise.** The Gram is PSD on every tested
   basis, but this is finite-dimensional. PSD on finite subspaces is **necessary,
   not sufficient** for RH. Guarded: every positivity claim is tagged "on basis".

2. **Cholesky factorisation depends on cutoff / is zero-side.** `Q=|Ah|²` holds
   when PSD, but `A` is built from the **zeros**. There is no constructive
   prime-side `A`. Guarded: stated explicitly in `NORM_SQUARE_FACTORISATION_REPORT.md`.

3. **Kernel positivity that fails on richer bases.** The off-line teeth show `K`
   loses PSD when a zero leaves the line; so PSD on a fixed basis is not RH.
   Guarded: teeth experiment reported; the on-line Gram sits at the PSD **edge**
   (min eig ≈ 0), i.e. it is *not* comfortably positive.

4. **`H−R` merely restating `Q`.** The split is canonical (explicit-formula
   terms) and explanatory (`H` positive, `R` indefinite), but `H⪰R ∀h` **is**
   Weil positivity — no new theorem. Guarded: said plainly throughout.

5. **Test-function classes too narrow.** Wide Gaussians make positivity
   archimedean-dominated (weak). We deliberately use a **rich, tight** basis where
   the on-line Gram is at the positivity edge, so the test has teeth. Guarded:
   `WEIL_FUNCTIONAL_RESULTS.md`.

6. **Numerical stability.** The explicit formula could be mis-implemented.
   Guarded: formula-side vs zero-side agree to machine precision, with a
   truncation study confirming independence (`harness.json`).

7. **Hidden RH assumptions.** None: no construction uses zero locations. Zeros are
   used only to validate the formula and to *demonstrate* the teeth. Test 1
   (non-circularity) passes.

8. **Fitted zero-side constructions.** Nothing is fitted; the prime/archimedean
   side is parameter-free; the zeros are computed (`mpmath.zetazero`), not tuned.

9. **Loss of completion.** Dropping the archimedean term destroys positivity
   (`R` indefinite). We keep the completed object throughout. Test 2 passes.

10. **Loss of arithmetic meaning.** `H`, `R` are the genuine archimedean and prime
    terms; no step trades arithmetic meaning for positivity.

## Net

The strongest honest statement survives all ten guards: a canonical, non-circular,
completion-aware decomposition `Q = H − R` with `H` a positive kernel and `R`
indefinite, plus a faithful norm-square diagnostic with working teeth — all
**RH-equivalent at the universal quantifier**, none of it a proof.
