# H-grad-1 Verification Harness

**Script:** `papers/cascade-derivation/scripts/verify_h_grad_1.py`
**Status:** OPEN (harness green; A1 PASS, A2/A3/A4 FAIL as discussed below).
**Companion WO:** `WO-H-GRAD-1.md` acceptance criteria A1–A4.
**Date opened:** 2026-04-22.

---

## 1. What the harness does

Pure representation theory — no dynamics, no eigenvalue spectra, no
scorecards. Exact arithmetic over `Q(sqrt 5)` throughout (custom `Zphi`
class: pairs of `Fraction` rationals with `phi^2 = phi + 1`).

For each of A1–A4 of the work-order, the harness runs a specific
computational check against the Conway–Sloane / Wilson icosian
construction (SPLAG Ch. 8 §2.1):

| Criterion | What the harness tests |
|-----------|----------------------------|
| A1        | Build the 120 icosians explicitly (8 axis-aligned + 16 diagonal + 96 phi-mixed). Verify `|2I| = 120`, quaternion closure under multiplication on a 30×30 random sample (900/900), and pick a Z-basis via column-HNF of the 120×8 embedding matrix. |
| A2        | Compute the `F_2`-quadratic form on `I/2I` from the icosian norm via Galois trace `Tr_{Z[phi]/Z}`. Check (i) form is non-degenerate, (ii) `Q=0` count equals 136 (Type II Arf=0 signature), (iii) `Q=1` count equals 120 (the 120 short icosian vectors). |
| A3        | Enumerate the maximal isotropic 4-dim `F_2`-subspaces `L ⊂ F_2^8`. Standard `O^+(8,2)` fact: 270 of them (two families of 135, swapped by spinor norm). Enumeration is flag-based with orthogonality pruning; degenerates to a guarded radical-check when the form is non-canonical. |
| A4        | For one chosen `L`, build `K = L + <e_0>` (Conway–Sloane "kill the real part" Fano choice), then test the candidate μ: Ẑ[φ]⁶ ↠ I/2I ↠ (Z/2)³ on 8 model octonion-basis characters `e_0,...,e_7`. A pass requires injectivity (bijection `C_O → (Z/2)^3`). |

## 2. How to run

```
cd papers/cascade-derivation
python3 scripts/verify_h_grad_1.py
```

Runtime: ~3 seconds on a standard laptop (sympy exact arithmetic, but no
dynamics). No external data files, no numerical tolerance parameters.
Every computation is exact.

## 3. Expected outputs on a PASS

```
A1 (Z-basis of I):                    PASS
A2 (F_2-quadratic form = E_8/2E_8):   PASS   [Q=0: 136, Q=1: 120]
A3 (270 max-isotropic 4-spaces):      PASS   [found 270]
A4 (C_O <-> (Z/2)^3 bijection):       PASS   [8 distinct cosets]
H-grad-1 overall: CLOSED
```

Passing all four would mean:

- (A1) the icosian ring identification with a rank-8 Z-lattice is
  explicit and verified against Conway–Sloane;
- (A2) the mod-2 reduction of the icosian norm matches the canonical
  `E_8/2E_8` Type II even quadratic form;
- (A3) the 30 octonion algebra structures on `E_8` are recovered as
  maximal Lagrangians (half of the 270 total, up to duality family);
- (A4) the Fano-grading (Z/2)³ of the Observer rung `Q_O` lifts to the
  candidate map μ, closing sub-gap H-grad-1 of
  `cascade-fano-grading-lift.md` §5.3 and upgrading
  `cascade-access-principle-theorem.md` Theorem P-A from conditional
  to unconditional.

## 4. Current output (2026-04-22)

```
A1:  PASS   |2I|=120, closure 900/900, rank=8
A2:  FAIL   Q=0: 256, Q=1: 0 — form collapses on chosen Z-basis
A3:  FAIL   radical = full space — form degenerate
A4:  FAIL   |image of C_O in (Z/2)^3| = 4, not 8
```

## 5. Why A2/A3/A4 currently fail — the real obstruction

This is exactly what the user's audit flagged: **the quaternion-only σ we
have is the wrong map**, in a way the harness now makes precise.

The 120 icosian units alone generate a rank-8 Z-sublattice of index 16
inside the true Conway–Sloane icosian ring `I`. Specifically, the
column-HNF of the 120×8 embedding gives a Z-basis with determinant 16
(not 1 after scale normalisation, not `2^8 = 256` after scale=2). The
full icosian ring is obtained by *closing the Z-span under addition* —
i.e. including linear combinations like `b_i + b_j` that are not
themselves icosian units but lie in `I`.

Consequences:

1. A2 sees every Gram diagonal as even-and-divisible-by-4 under our
   scale=2 embedding, making `Q(e_i) = 0` for all basis `e_i` and the
   off-diagonal bilinear form vanishes mod 2 on too many pairs. Result:
   Q ≡ 0 on all of `F_2^8`, i.e. the wrong form.

2. A3 inherits this degeneracy — the radical is the full space and no
   meaningful Lagrangian count is possible.

3. A4's candidate μ is consequently too coarse: `C_O` collapses to just
   4 cosets instead of the required 8.

This is **not a calibration issue** — it is a structural mismatch. The
harness confirms that picking Z-basis vectors from among the 120 unit
icosians does **not** span the icosian ring as a Z-module: the
sublattice `Z<2I_120>` has index 16 in `I` itself.

## 6. What needs to change to close H-grad-1

A future round should:

1. Extend the Z-basis to include combinations like `(b_i + b_j)/1`
   that lie in `I` but are not icosian units themselves, reducing the
   HNF determinant from 16 to 1 (unimodular basis of `I = E_8`).

2. Verify that under this corrected basis, `Q=0` count is 136 and
   `Q=1` count is 120, confirming the Type II Arf-zero form.

3. With a non-degenerate form, A3's flag enumeration will complete in
   seconds and produce 270 Lagrangians.

4. For A4, once the form is canonical, pick `L` in the octonion family
   and verify μ on `C_O` is bijective (this is the step that validates
   the specific Fano-plane choice, canonical up to G₂-action per
   Phase O-2).

## 7. Scope limits — out of this harness

- No cascade eigenvalue simulation (not the intent).
- No GUE statistics, no scorecard (the user's audit specifically warned
  against this — the quaternion-only σ map fails the GUE test, and A2
  failing here confirms the same structural issue from the other side).
- No attempt to verify the `cascade-fano-grading-lift.md` §5.2.2 μ
  uniqueness up to G₂ — that is downstream of passing A4.

## 8. Cross-references

- `WO-H-GRAD-1.md` — parent work-order with acceptance criteria A1–A4.
- `cascade-fano-grading-lift.md` §5.2.2 — the candidate μ.
- `cascade-fano-grading-lift.md` §5.3 — sub-gap H-grad-1 statement.
- `cascade-access-principle-theorem.md` — Theorem P-A, downstream.
- `scripts/build_2I_and_icosahedral.py` — prior 2I group construction
  (confirmed |2I| = 120 + 9 conjugacy classes).
- Conway–Sloane, "Sphere Packings, Lattices and Groups," 3rd ed.,
  Ch. 8 §2.1 (icosian ring Z-basis).
