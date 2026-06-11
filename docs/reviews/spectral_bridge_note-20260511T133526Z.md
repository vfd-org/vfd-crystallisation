**Publication Verdict**

Publication ready: **yes**. I find no substantive math/attribution must-fix remaining.

**1. Claim Audit**

- “Every integer-eigenvalue multiplicity...” at [line 221](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:221>): established. I ran `run_keystone()`; it returned local `{0:1,4:4,8:9,10:8,12:2}` and global `{0:1,9:16,12:25,14:36,15:16}` exactly.
- “For every coset... lift_i(E_C_i(12)) subset E_V600(12)” at [line 253](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:253>): established by the exact rational basis/nullspace certificate; direct run reports `certified=True`, total local dim `10`, nonzero components `0`.
- Floating residual “≤ 6.2e-15” at [line 282](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:282>): established; run reports `6.161050110161165e-15`.
- Dimension corollary at [line 287](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:287>): established. Disjoint supports give 10, exact global nullity gives 25, hence proper.
- Selectivity table at [line 311](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:311>): established. The table matches the runner; the λ=0 exception is correctly identified as the global constant.
- “P_-1 restricted to E_V600(12) is identity” at [line 368](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:368>): established by exact componentwise check; direct run returns `minus_one_acts_trivially=True`.
- Exact A5 character table at [line 410](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:410>): established; direct run returns the stated class characters.
- A5 irrep decomposition at [line 447](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:447>): established by exact character projection; only `Y5` occurs with multiplicities 2, 3, 5.

**2. Internal Consistency**

No substantive inconsistency found. The right-coset convention is stated before use; the vertex action versus coset action distinction is handled explicitly; all `\ref` targets used in the note resolve to existing local labels. No cross-reference mismatch affects the mathematics.

**3. External Consistency**

- Paper XXXV Schläfli attribution at [lines 84-91](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:84>): verified locally in `papers/paper-xxxv/paper-xxxv.tex`, Theorem `thm:schlafli`, lines 284-303.
- Paper XXXV A5 action attribution at [lines 163-168](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:163>): verified locally in `papers/paper-xxxv/paper-xxxv.tex`, Theorem `thm:A5action`, lines 416-432.
- Paper V spectrum attribution at [lines 218-242](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:218>): verified locally in `papers/paper-v/paper-v.tex`, Proposition `thm:eigenvalues` and Table `tab:spectrum`, lines 104-129.
- Right-coset transfer from Paper XXXV’s left-coset statement is valid: inversion sends `gT` to `Tg^{-1}` and conjugates the left action to the corresponding right action by inverse elements.

**4. Tightness**

No substantive overclaim remains. The line-221 round-5 defect is repaired: the note now claims exact certification only for the displayed integer spectral multiplicities, and the code actually certifies that statement.

**5. Surface Issues**

No substantive LaTeX or notation issue affecting publication readiness.

**6. Top Three Fixes**

No ranked substantive fixes. The previous must-fix at [line 221](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/keystone_24_600/spectral_bridge_note.tex:221>) is resolved.
