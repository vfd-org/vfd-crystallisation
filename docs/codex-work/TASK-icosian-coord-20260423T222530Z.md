**Files Edited**
- [cascade-12d-closure.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-12d-closure.md:38>) — 218 lines. Corrected Level 2 icosian-ring description; removed naive `Z[φ]{1,i,j,k}` implication.
- [cascade-observer-zeta.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-observer-zeta.md:394>) — 731 lines. Marked O6 resolved, updated P5/C7 status, kept C7 downgraded for simplified-decomposition reasons.
- [cascade-observer-zeta-catalogue.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-observer-zeta-catalogue.md:35>) — 100 lines. Marked catalogue O6 resolved and removed O6 as active blocker.

**Files Created**
- None.

**Key Decisions**
- Used `papers/cascade-algebraic-substrate/cascade-algebraic-substrate.tex:480-514` as source of truth.
- Kept rank claims: rank 4 over `Z[φ]`, rank 8 over `Z`.
- Left `WO-H-GRAD-1.md` unchanged: §O2 only states ranks and does not imply `{1,i,j,k}` is a basis.
- Left `cascade-h-grad-1-closure.md` unchanged: §2 already uses half-integer `ω` generators.

**Checks**
- Ran `git diff --check` on edited paths: no whitespace errors reported.
- Scanned for stale naive references: old `Z[φ] extended by quaternion units` and bad `cascade-12d-closure.tex` reference are gone.

**Residual Caveats**
- C7 remains downgraded because `dual_600cell_factor2.py:142-145` still says the decomposition is simplified, and `cascade-12d-closure.md` remains a working note.
- No new script was added; this round only reconciled wording/status against an existing canonical source, with no new numerical result.

**Open Sub-Questions**
- Whether the C7 σ-swap claim can be upgraded beyond working-note status.
- H-grad-1 still needs the planned explicit basis/mod-2 verification round.
