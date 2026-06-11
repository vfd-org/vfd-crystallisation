**Publication Ready?** No.

**1. Claim Audit**
- Lines 312-338, Theorem “λ=12 lift identity”: established. The exact rational certificate directly proves the stated inclusion.
- Lines 340-347, floating residual `≤ 6.2e-15`: established. I reran `run_keystone()` and reproduced `6.1610501101611652e-15`.
- Lines 350-355, `dim E_lift = 10`, proper in `E_V600(12)`: established from disjoint supports plus exact `dim E_V600(12)=25`.
- Lines 374-384, selectivity table: the mathematical entries appear correct, but the stated proof package does **not** establish the whole table as advertised. The current implementation computes intersection dimensions numerically; the exact integer-spectrum check omits global nullspace checks at `λ=4,8,10`. I independently computed exact nullities `{4:0, 8:0, 10:0}`, so the claim is true, but the manuscript overclaims the existing certificate.
- Lines 438-455, `{-1}` acts trivially on `E_V600(12)`: established by exact componentwise check.
- Lines 480-497, exact `A_5` characters: established, provided one accepts the preceding invariance assertion. Add one explicit sentence proving right multiplication sends each lifted local eigenspace to another lifted local eigenspace.
- Lines 517-524, `A_5` irrep decomposition: follows from the character table.

**2. Internal Consistency**
- Cross-references resolve to existing labels. I found no broken `\ref`/`\eqref`.
- Main inconsistency: lines 51-57 say the selectivity table is reproduced by exact rational arithmetic, but the runner’s selectivity table is numerical while the exact certificate does not include the `λ=4,8,10` global nullity checks.
- Line 524: “over `\mathbb{Q}`” is imprecise for the displayed complex `A_5` irrep table. Suggested edit: “with exact rational character computation giving zero multiplicity for every other complex irrep.”

**3. External Consistency**
- Paper XXXV attribution checks out: `sec:bio:schlafli` / `thm:schlafli` prove the left-coset Schläfli decomposition; `sec:gr:lorentz` / `thm:A5action` prove the `A_5` coset action. The note correctly states the right-coset version is obtained by inversion.
- Paper V attribution checks out for the 600-cell spectrum. The local 24-cell spectrum is also computed by the cited script, but the note’s exact local multiplicities are really established by the keystone certificate, not Paper V.
- `vfd_v600` supports the coordinate and `σ`-fixed claims. I did not find a standalone full “all 120 vertices are closed under multiplication” test in that package, though the keystone `A_5` computation exercises closure implicitly.

**4. Tightness**
- Lines 51-57: too strong. Replace “the selectivity table … exact rational” with either an actual exact selectivity certificate or “the λ=12 lift, integer multiplicities, and character claims are exact; the displayed residuals are floating-point cross-checks.”
- Lines 400-408: acceptable after adding exact nullity checks at `λ=4,8,10`.
- Lines 457-461: too compressed. Add: “Right multiplication maps `C_i` isometrically to `C_{i\cdot h}` and conjugates the local shell-1 Laplacian, hence maps `E_{C_i}(12)` to `E_{C_{i\cdot h}}(12)`.”

**5. Surface Issues**
No substantive LaTeX or notation blocker found. The only surface-level technical wording worth fixing is the “over `\mathbb{Q}`” representation phrase at line 524.

**6. Top Three Fixes**
1. Lines 51-57 and 602-606: either add exact selectivity certification for `λ=0,4,8,10,12`, especially exact global nullities at `4,8,10`, or stop claiming the table is exact-certified.
2. Lines 457-461 / 480-497: insert the missing explicit invariance argument for `E_lift` and `E_res` before using character theory.
3. Line 166-169: either cite a source/test that explicitly verifies full `2I` closure, or soften the attribution to the `vfd_v600` package.
