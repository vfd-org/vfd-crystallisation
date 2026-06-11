**1. Claim Audit**

- `cascade-refinement-compat.tex:232-250`, Theorem 2.1: the proof establishes Schur halving for the stated **edge-midpoint-only** graph, with degree-2 midpoints and no other incident edges. The three proof steps are rigorous under that hypothesis. It does **not** establish the claim for the actual P3/P4 refinement tower, because `cascade-refinement-spaces.tex:273-286` adds face centroids and extra midpoint-centroid edges. This is the central over-claim.

- `:49-56`, abstract Schur claim for the “finite-level P3/P4 refinement tower”: not established for P3/P4 as locally defined. It is established only for the stripped edge-subdivision tower.

- `:175-177`, “unique factor”: over-claimed. The recurrence is unique only up to an overall normalization: any `c_0 2^n` works. Edit to “unique after fixing `\widetilde A_0=A_0`.”

- `:396-404`, Theorem 3.1: valid if Theorem 2.1 applies. The equality case is proved: positive definiteness of `A_II` kills the interior defect. But the P3/P4 discharge inherits the Theorem 2.1 applicability gap.

- `:453-460`, Corollary 3.2: over-claims. “(O3) is closed for the P3/P4 tower” is not supported unless the real P3/P4 refinement is replaced by the edge-midpoint-only tower or a new proof handles centroid edges.

- `:470-487`, Proposition 4.1: the stated one-way vanishing on harmonic extensions is proved. The generic nonzero claim on `{psi_I=0}` is supported by the examples. But the stronger “precisely” language at `:63-68`, `:525-534`, and `:770-772` is not proved and is generally false: in block form
  `D(f,g)=A_BI(g-H_I f)`, so non-harmonic interior deviations in `ker A_BI` also vanish. Large graphs will typically have such directions.

- `:560-580`, Proposition 5.1: correct for the scalar graph Laplacian used in this paper. It is not literally the P3/P4 source state space, whose vertex fibre is 32-dimensional (`cascade-refinement-spaces.tex:464-510`).

- `:616-674`, Tower I computations: match the frozen rational output `expected_outputs/explore_defect.txt:12-49`.

- `:676-706`, Tower II computations: match the frozen output `:58-105`, but this is a 6-vertex edge-subdivided triangle, not a standard barycentric triangle and not the P3/P4 Schläfli refinement with a face centroid. Including the face centroid in the usual triangle barycentric graph gives Schur factor `5/9 A_0`, not `1/2 A_0`.

- `:700-705`, eigenvalues: mathematically correct for the displayed matrix, but the frozen script prints these via floating point, not exact rational eigenvalue computation.

- `:729-740`, §7 status table: internally matches Theorem 3.1 and Proposition 4.1, but the table overstates P3/P4 closure because Theorem 2.1 has not been proved for the actual P3/P4 refinement.

**2. Internal Consistency**

- The paper repeatedly says “P3/P4 tower” (`:44-47`, `:453-460`, `:708-740`) but Theorem 2.1 assumes no extra midpoint edges (`:236-239`). These are incompatible.

- “Use the notation … verbatim” (`:131`) is inaccurate. The source uses vector-valued `F^0`, antisymmetric oriented edge spaces, and a 32-dimensional vertex fibre; this paper uses scalar `\mathbb R^V` (`:135-143`).

- “Defect vanishes precisely” conflicts with Proposition 4.1, which proves only vanishing on harmonic extensions plus generic non-vanishing elsewhere.

- Cross-references appear to resolve to the intended local labels. No obvious broken `\ref`/`\eqref` found.

**3. External Consistency**

- `CascadeClosureDynamics` coboundary relation is verified: `cascade-closure-dynamics.tex:896-937` proves `p^1 d_{n+1} = 1/2 d_n p^0`.

- `CascadeClosureDynamics` explicitly does **not** prove graph-Laplacian refinement compatibility: `:989-995`. This paper is right to treat that as new work.

- `CascadeRefinementSpaces` verifies finite Hilbert spaces and bonding maps (`cascade-refinement-spaces.tex:499-583`, `:655-719`). But it also defines the refinement with centroids and extra edges (`:273-286`), contradicting this paper’s degree-2 midpoint hypothesis.

- `cascade-mechanism.tex:691-710` and claim ledger `:974-976` agree with this paper’s §7 status table. That agreement is textual, not an independent verification; it inherits the same P3/P4 applicability gap.

**4. Tightness**

- `:44-72`: replace “for the finite-level P3/P4 refinement tower” with “for the edge-midpoint-only refinement model” unless a real P3/P4 proof is added.

- `:63-68`, `:770-772`: replace “vanishes precisely” with “vanishes on the harmonic-extension subspace; its full kernel is `H + ker A_BI` unless `A_BI` is injective.”

- `:175-177`: replace “unique factor” with “unique up to an overall normalization.”

- `:783-790`: this is stale relative to current `cascade-mechanism` main, which already contains the update. Rewrite as “This update is reflected in …”

**5. Surface Issues**

- `:500`: `p_{0}^{*}` should be `(p^{0})^{*}` or `(p^0_{n+1,n})^*`.

- `:676`: “barycentric edge-subdivision” is misleading; the worked graph has no face barycenter.

- `:383-386`, `:811-824`: “all linear algebra exact” should exclude the displayed eigenvalue diagnostic, which the script computes with floating point.

- Hyphenation is inconsistent: “positive-semi-definite” vs “positive semi-definite.”

- The reproducibility section tells readers to run `run_audit.sh`; in this read-only workspace that wrapper is known to fail. Document that it requires a writable repro/output directory.

**6. Top Three Fixes**

1. Fix the P3/P4 applicability gap at `:44-72`, `:232-250`, `:453-460`, and `:729-740`. Either prove the Schur identity for the actual Schläfli refinement with centroids, or narrow every claim to the edge-midpoint-only model.

2. Correct the defect-kernel claim at `:63-68`, `:525-534`, and `:770-772`. Add the block formula `D(f,g)=A_BI(g-H_I f)` and state the injectivity condition needed for “precisely.”

3. Replace Tower II or relabel it at `:676-706`. The current 6-vertex example verifies an edge-subdivided triangle, not barycentric/P3 refinement; it cannot support the paper’s stated downstream obligation claim.
