Publication ready: **no**.

**1. Claim Audit**
- Theorem 1, “lift_i(E_C_i(12)) ⊂ E_V600(12)” at [spectral_bridge_note.tex:239](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:239): established. I ran the exact certificate; it reports `certified=True`, per-coset local nullity 2, and zero nonzero rational residual components.

- Corollary 2, “dim E_lifted = 10 … proper” at [line 273](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:273): established, conditional on Paper V’s `dim E_V600(12)=25`. Paper V does contain multiplicity 25 at λ=12.

- Selectivity table at [lines 297-307](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:297): established for the stated tested local eigenvalues. Exact/non-exact status should be stated more carefully: λ=4,8,10 follow exactly from the imported global spectrum; the table’s computational reproduction uses numerical eigenspace/SVD logic.

- Lemma 3, “P_-1 restricted to E_V600(12) is the identity” at [line 354](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:354): mathematically established by the exact trace criterion, since `P_-1` is an involution on an invariant real subspace. But the proof text says the code checks componentwise equality of every rational basis vector at [lines 362-364](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:362); the current code checks trace equality, not componentwise equality. Fix wording or add the componentwise check.

- Theorem 4, exact A5 class characters at [lines 387-404](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:387): **not yet established to hostile-review standard**. The exact routine does not correctly group the two A5 5-cycle conjugacy classes. It counts only the chosen 5-cycle and its inverse as one class, giving preimage counts `5A=4`, `5B=44`, rather than `24/24` in `2I`. The final table is probably still right here because all 5-cycle traces are numerically zero, but the stated exact class-character proof is defective.

- Corollary 5, `2·Y5 / 3·Y5 / 5·Y5` at [lines 424-431](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:424): conditional on fixing Theorem 4’s class grouping. The reported multiplicities match the current run, but the proof route needs the corrected class audit.

**2. Internal Consistency**
- All LaTeX `\ref` targets in this file resolve to defined labels.
- The text says Paper XXXV treats the left-coset version in “Section 6.1” at [line 135](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:135). That is wrong for the local source: the Schläfli theorem is in Paper XXXV’s Biology/Schläfli subsection, and the A5 action is in the GR/Lorentz subsection.
- The A5 proof text says actual A5 conjugacy classes are used at [lines 382-385](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:382); the exact code does not do that for 5-cycles.

**3. External Consistency**
- Paper XXXV verifies the left-coset Schläfli decomposition and left-coset A5 action. The note’s right-coset transfer by inversion is plausible and sufficient, but it is the note’s argument, not directly a theorem in Paper XXXV.
- Paper V verifies the 600-cell spectrum and `dim E_V600(12)=25`.
- The claim that `run_polytope_uniqueness_narrow.py` reproduces the local 24-cell spectrum “exactly” at [lines 223-225](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:223) is not supported. That script uses floating-point nearest-neighbour construction and numerical eigenvalues. Replace “exactly” with “numerically” or cite/add an exact 24-cell spectrum certificate.

**4. Tightness**
- [Lines 382-385](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:382): replace with “grouped by actual conjugacy classes in the A5 image” only after fixing the code.
- [Line 225](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:225): change “reproduced exactly” to “reproduced numerically” unless an exact local spectrum proof is added.
- [Lines 362-364](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:362): change to “the exact trace equals the dimension; since `P_-1` is an involution, it acts as identity.”

**5. Surface Issues**
- `EMPTY` in the selectivity table at [lines 304-306](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:304) still reads like the old wording. Use `ZERO-DIM` or `{0}`.
- The Paper V script path should be explicit as `papers/paper-v/scripts/run_polytope_uniqueness_narrow.py`.
- No undefined macros or broken LaTeX references found in this file.

**6. Top Three Fixes**
1. Fix the exact A5 5-cycle conjugacy-class grouping and rerun the character certificate. This is the blocker for Theorem 4 and Corollary 5.
2. Correct the Paper XXXV section attribution at line 135; cite the actual Schläfli and A5-action locations.
3. Remove the unsupported “exactly” attribution for the Paper V 24-cell spectrum script at lines 223-225, or add an exact local 24-cell spectrum certificate.
