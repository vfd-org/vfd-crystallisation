Publication ready? **No.**

**1. Claim Audit**
- L214-L236, Theorem 1: the inclusion `lift_i(E_Ci(12)) ⊂ E_V600(12)` is established by the exact certificate. The proof is acceptable for the inclusion. However L51-L52 overstates the method: the code computes local rational nullspaces and applies `L_V600 - 12I` exactly; it does not compute the global rational nullspace.
- L248-L254, Corollary: the dimension count is valid if `dim E_V600(12)=25` is imported as an exact spectral fact. The proof currently just asserts it. Add a direct citation back to the exact spectrum source.
- L258-L303, selectivity table: the intersection-dimension reformulation is basically sound. But L87-L90 is false as written: “No other local-Laplacian eigenvalue lifts...” conflicts with the `λ=0` partial lift at L287-L292. Say “no other eigenvalue lifts in full.”
- L294-L298: “bounded below by 3.16” is stronger than the table/code statement as presented. The runner reports max residuals; if claiming a lower bound over the lifted subspace, state and certify the minimum singular/residual bound.
- L318-L325: false as stated. Right multiplication by `-1` is not the identity on `V_600`; only the coset action has kernel `{±1}`. The `λ=12` subspaces appear numerically to have `-1` acting trivially, but that fact is not proved in the paper.
- L364-L374, Theorem 2: over-claimed. The displayed `A_5` decomposition is supported by floating-point character traces, not an exact proof. Either provide an exact character/projector certificate or downgrade this from theorem to numerical proposition.

**2. Internal Consistency**
- L87-L90 vs L287-L292: contradiction on whether any non-`12` lift exists. The `λ=0` symmetric constant is a nonzero lifted global eigenvector.
- L318-L325 conflates three actions: right multiplication on vertices, induced permutation of cosets, and the quotient `A_5` action. These are not interchangeable without proving `-1` acts trivially on the relevant eigenspaces.
- L82-L83 and L147 use `\ref*{thm:schlafli}` / `\ref*{thm:A5action}` for labels from another LaTeX file. In this standalone document they will resolve as undefined.
- L297: “`E_six(λ)` is empty” should be “zero-dimensional” or `{0}`.

**3. External Consistency**
- L78-L83 / L138 cite Paper XXXV for the coset decomposition. I verified Paper XXXV proves the **left-coset** Schlӓfli decomposition at `papers/paper-xxxv/paper-xxxv.tex` L284-L303. The current right-coset version follows by the parallel/inverse argument, but Paper XXXV does not state it directly.
- L147-L150 cite Paper XXXV Theorem `A5action`. I verified that theorem at Paper XXXV L416-L431, but it is explicitly for left multiplication on left cosets. The current right-multiplication/right-coset claim needs its own one-line equivalence proof or a local certificate.
- L188-L203 cite Paper V for spectra. Paper V does contain the 600-cell spectrum at L104-L127, but it says the exact result is imported from P2. I did not find a Paper V section literally called “polytope spectra,” and the local 24-cell spectrum is in `run_polytope_uniqueness_narrow.py`, not in the Paper V text.
- L437-L442 give Paper XXXV script paths under `papers/paper-xxxv/`; those scripts are actually under `papers/cascade-derivation/scripts/`. This is an attribution/reproducibility error.

**4. Tightness**
- L87-L90: replace with “Full zero-extension occurs only at `λ=12`; at `λ=0` only the symmetric sum of coset constants lands in the global eigenspace.”
- L51-L52: replace “nullspaces of the integer Laplacians” with “local rational nullspaces plus exact application of `L_V600-12I`.”
- L318-L325: replace with “The induced action on the five cosets factors through `A_5`; the action on `E_V600(12)` factors through `A_5` only after verifying that `-1` acts trivially there.”
- L364: replace `\begin{theorem}` with `\begin{proposition}[Numerical A_5 character computation]` unless an exact character certificate is added.

**5. Surface Issues**
- Broken external `\ref*` labels at L83 and L147.
- Wrong script locations in bibliography L437-L442.
- “empty eigenspace” at L297 is mathematically sloppy.
- “Section ‘polytope spectra’” at L189 does not match the Paper V section title I found.

**6. Top Three Fixes**
1. Fix the `A_5` theorem: prove exact factorisation on the eigenspaces and exact character multiplicities, or downgrade L364-L374 to a numerical proposition.
2. Repair the Paper XXXV attribution: distinguish left-coset results from the current right-coset convention and remove unresolved external `\ref*` labels at L82-L83 and L147.
3. Fix the selectivity overclaim at L87-L90 so it does not deny the `λ=0` partial lift proved at L287-L292.
