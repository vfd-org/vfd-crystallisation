**Files Edited**
- [WO-CASCADE-MECHANISM.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-mechanism/WO-CASCADE-MECHANISM.md>) — 721 lines. Refined WO into the requested 9-section mechanism-paper plan with new load-bearing ARIA §6 and Millennium §8.

**Files Created**
- None.

**Key Decisions**
- Kept the mechanism triad unchanged: `Instability -> Cascade -> Crystallisation`.
- Moved the old claim-ledger material into the new structure rather than keeping it as old §7, because §7 is now case studies.
- Used actual ARIA paths found in repo; `papers/aria-chess-paper/aria-chess-paper.tex` is absent, so the WO points to `papers/aria-chess-paper/paper/main.tex`.
- Marked missing ARIA runtime pieces as reserved instead of guessing: `SystemTickCoordinator`, refusal/governance stack, action interface, provenance/replay, persistent polytope memory.
- Used audited Millennium hypothesis names from current `.tex` sources, not stale scope labels where they differ.

**Verification**
- Re-ran `papers/cascade-derivation/scripts/test_sigma_attractor_spectrum.py`: confirmed `94/120 = 78.3%` sigma-fixed and `26/120 = 21.7%` sigma-paired.
- Checked the WO has the 9 required paper sections and updated acceptance/risk/phasing/page estimate.

**Residual Uncertainty / Caveats**
- ARIA governance/action/provenance modules may exist outside this repo; current WO correctly treats them as unconfirmed.
- Some legacy dependency line counts were preserved rather than re-audited; ARIA and Millennium counts were refreshed.
- Poincare has no load-bearing `78.3/21.7` spectral split; the WO scopes it as classical-proof import plus cascade coherence.

**Open Sub-Questions**
- Confirm whether an external ARIA repo has the missing `SystemTickCoordinator` and persistent memory/provenance modules.
- Decide during `.tex` build whether to introduce an alias between older `H_attr` wording and current `H_{sigma-fix}` source language.
- Decide how much of §8 becomes main text versus appendix without weakening the “give the game away” requirement.
