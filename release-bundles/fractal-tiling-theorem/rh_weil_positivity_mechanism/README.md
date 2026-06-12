# RH — Weil Positivity Mechanism

**WO-RH-WEIL-POSITIVITY-MECHANISM-001** — can VFD closure geometry factor or
explain the Weil positivity criterion as a norm-square, positive kernel,
boundary-capacity inequality, or self-adjoint closure form?

## Result

```
GRADE 2 — candidate bridge object (canonical H−R capacity decomposition),
          reduces to Weil positivity.   NO_RH_PROOF_CLAIMED.
```

The Weil functional factors **canonically** as
```
Q_Weil = H − R,   H = archimedean capacity (POSITIVE kernel),   R = prime load (INDEFINITE)
```
so RH `⇔` `H ⪰ R` for all admissible test functions ("capacity dominates load").
Positivity lives in the archimedean completion; the prime/Euler side alone is
never positive. This is faithful, non-circular, and completion-aware — but it is
the classical Weil structure, and the universal dominance is RH.

### What is genuinely solid (all computed, not asserted)
- **Explicit formula validated:** formula side (`ARCH+POLE−PRIME`, no zeros) =
  zero side to machine precision, with a truncation study proving independence.
- **`H` is a positive kernel; `R` is indefinite** → positivity *requires* the
  completion (the prime side alone cannot be positive).
- **Norm-square `Q=|Ah|²`** exists on PSD bases, with **off-line teeth**: the
  on-line Gram is at the PSD *edge* (min eig ≈ 0), and moving any zero off the
  line makes it indefinite. So `Q=|Ah|² ⇔ zeros on the line ⇔ RH`.
- **`K`** (Weil kernel/operator) is Hermitian, self-adjoint, PSD on bases;
  `K⪰0` universally `=` RH.

### The wall (unchanged, now anatomised)
The factor `A` and the operator `K` are zero-side / Weil-functional re-dressings.
A **canonical self-adjoint operator with the zeros as spectrum, built from the
completion** — the archimedean–adelic Hilbert–Pólya object — is not constructed.
Universal `H ⪰ R` is RH.

## Files

```
weil_functional_harness.py          core: Q = H − R, formula vs zero side (validated)
norm_square_factorisation_search.py Q=|Ah|² + off-line teeth
boundary_capacity_tests.py          H positive, R indefinite, completion essential
kernel_positivity_search.py         Weil kernel K = K_arch − K_prime
operator_candidate_tests.py         self-adjoint K, K⪰0 = RH
WEIL_CRITERION_FORMALISATION.md     A    VFD_WEIL_TRANSLATION_TABLE.md       B
WEIL_FUNCTIONAL_RESULTS.md          C    NORM_SQUARE_FACTORISATION_REPORT.md D
BOUNDARY_CAPACITY_DECOMPOSITION.md  E    KERNEL_POSITIVITY_REPORT.md         F
ARCHIMEDEAN_ADELIC_COMPLETION_ANALYSIS.md G  SELF_ADJOINT_OPERATOR_CANDIDATE.md  H
FAILURE_MODE_CATALOGUE.md           I    CLAIM_BOUNDARY.md  J  FINAL_CLASSIFICATION.md
results/                            phase_*/ + plots/ + tables/
```

## Run

```bash
python3 weil_functional_harness.py
python3 norm_square_factorisation_search.py
python3 boundary_capacity_tests.py
python3 kernel_positivity_search.py
python3 operator_candidate_tests.py
```

Pure Python (`numpy`, `mpmath`). Zeros (`mpmath.zetazero`) are used **only** to
validate the explicit formula and to demonstrate the teeth — never in any
construction. See `CLAIM_BOUNDARY.md` / `FINAL_CLASSIFICATION.md`.
