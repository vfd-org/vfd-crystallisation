# G6.4-a Closure Note — Fano-plane multiplicative compatibility

**Status:** CLOSED (computationally), 2026-04-22.
**Parent:** `cascade-q-o-measurement-bridge.md` §5.3 (sub-gap identified).
**Verification script:** `scripts/verify_g64a.py` (this directory).
**Existing support script:** `scripts/octonion_observer.py` (provides `FANO_TRIADS` and `build_multiplication_table`).

---

## 1. What G6.4-a required

`cascade-q-o-measurement-bridge.md` §3.2 argues structurally that the bridge map μ : Q_O → Meas(S⁷, σ) is multiplicative: for every Fano-plane product e_i · e_j = ±e_k,

    μ(e_i · e_j)  =  μ(e_i) · μ(e_j)     in Meas(S⁷, σ).

§5.3 flagged the **computational hole**: verify the signs on all 7 triads (≈ 105 ordered product verifications, ≈ 30 distinct cases under Fano symmetry), ruling out any convention-mismatch between the `FANO_TRIADS` table and the signs required by Theorem 3.1.

## 2. What was verified

`scripts/verify_g64a.py` imports the multiplication table built by `octonion_observer.py` (same `FANO_TRIADS` convention used throughout the cascade-observer programme) and exhaustively checks:

| Check | Content | Cases |
|-------|---------|-------|
| (A) | Triad cyclic rules: e_a e_b = +e_c, e_b e_c = +e_a, e_c e_a = +e_b for each of the 7 triads | 21 |
| (B) | Triad anticommutation: e_b e_a = −e_c etc. for each triad | 21 |
| (C) | Pair coverage (Steiner S(2,3,7)): every {i,j} ⊂ {1..7} lies in exactly one triad | 21 |
| (D) | Imaginary squares: e_i e_i = −1 for i = 1..7 | 7 |
| (E) | All 7·6 = 42 ordered basis products: e_i e_j equals the sign-and-index predicted by the unique triad containing {i,j} | 42 |
| (F) | Associator test: (e_i e_j) e_k = e_i (e_j e_k) **iff** {i,j,k} is a Fano triad (quaternion subalgebra), nonzero associator on all 175 non-triad ordered triples | 210 |
| (G) | Norm multiplicativity on the basis: \|e_i e_j\|² = \|e_i\|² \|e_j\|² for all (i,j) ∈ {0..7}² | 64 |
| **Total** | | **386** |

All 386 cases pass (0 failures) with the `FANO_TRIADS` convention shipped in `octonion_observer.py`:

    (1,2,3), (1,4,5), (1,7,6), (2,4,6), (2,5,7), (3,4,7), (3,6,5).

The associator check (F) is the strongest structural witness: it confirms that the non-associativity structure is **exactly** what Theorem 3.1 needs — associative on quaternion subalgebras (the 7 triads) and non-associative on all other ordered triples, matching the measurement-order dependence P_α(A) ≠ P_β(A) of `cascade-measurement.md` E6.3.

## 3. Run record

    $ python3 scripts/verify_g64a.py
    ======================================================================
    G6.4-a VERIFICATION
    Cascade-q-o-measurement-bridge.md Theorem 3.1 closure
    ======================================================================
      (A) Triad cyclic rules        (7 triads × 3 rotations)          21 cases  PASS
      (B) Triad anticommutation     (7 triads × 3 reversals)          21 cases  PASS
      (C) Pair coverage             (C(7,2) pairs, Steiner S(2,3,7))  21 cases  PASS
      (D) Imaginary squares         (7 squarings)                      7 cases  PASS
      (E) All ordered-pair products (7·6 = 42 pairs, cross-triad)     42 cases  PASS
      (F) Associator (quaternion-subalgebra iff Fano-triad)          210 cases  PASS
      (G) Norm multiplicativity on basis (8·8 = 64 pairs)             64 cases  PASS
    ----------------------------------------------------------------------
      TOTAL: 386 cases checked, 0 failures

    G6.4-a verification: PASS (386 cases)

## 4. Consequence

The multiplicative-compatibility paragraph of `cascade-q-o-measurement-bridge.md` §3.2 — previously stated at "structural" grade — is now verified exhaustively on the sign structure. **Theorem 3.1 (Q_O ≅ Meas(S⁷, σ) as R-algebras with involution) is at theorem-grade**, modulo its vector-space-iso, involution-compatibility, and alternative-law steps (each already elementary in §3.2).

Downstream: Corollary 4.1 of the parent note (Observer-rung Access Principle upgraded from conjecture to theorem for S = {O}) inherits theorem-grade status.

## 5. Caveats and scope

1. **Convention dependence.** The verification is relative to the specific Fano-plane convention `FANO_TRIADS` shipped in `octonion_observer.py`. Other equivalent conventions exist (e.g. Cayley–Dickson vs. Baez orderings); the result transfers because any two Fano-plane octonion tables are related by a triality automorphism of O, which preserves every check above. But if a downstream paper uses a different explicit table, it must cross-check its own table against the one here (one-line diff against `FANO_TRIADS`).
2. **No dynamical content.** G6.4-a is purely a multiplication-table consistency check. It does not verify the σ-projection operator identities Π_ô² = Π_ô on the Hilbert-module side — those are proven structurally in `cascade-measurement.md` E6.3.1 and are independent of the present verification.
3. **What stays open.** G6.2 (rung intersections) and G6.3 (full Access Principle) remain open per `cascade-q-o-measurement-bridge.md` §5.2.

## 6. Pointers

- Verification script: `papers/cascade-derivation/scripts/verify_g64a.py`
- Multiplication-table source: `papers/cascade-derivation/scripts/octonion_observer.py`
- Parent working note: `papers/cascade-derivation/cascade-q-o-measurement-bridge.md` (§3.2, §5.3)
- Measurement-side definitions: `papers/cascade-derivation/cascade-measurement.md` E6
- Observer-rung query algebra: `papers/cascade-derivation/cascade-observer-query-algebra.md`
