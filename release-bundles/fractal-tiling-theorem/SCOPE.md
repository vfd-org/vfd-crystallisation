# Real Scope: Genuine Hilbert Modular Hecke Data over Q(√5)
### and the (O2) Circularity Test

This document scopes, for real, the construction needed to discharge the
Fractal Tiling Theorem's conditional hypothesis (O1)–(O3), and designs the
test of whether the substrate↔Hecke identification (O2) is genuine or
circular ("test the circle").

---

## 0. Two corrections surfaced by scoping

Before any construction, the arithmetic of the target was checked:

| Claim in paper | Reality | Consequence |
|---|---|---|
| Level 𝔑 = (2)·(φ−2) | φ−2 = −φ⁻² is a **unit**, so (φ−2)=(1) | The stated level collapses to (2) |
| (2) is the relevant level | (2) is **inert**, N((2))=4 | No cuspidal form lives there |
| (proxy used N=31 over Q) | 31 **splits** in Q(√5); first cuspidal Hilbert newform over Q(√5) sits at a prime level of **norm 31** | The proxy was pointing at the correct object |

**Action:** the paper's level statement (§2.1, §6.1) must be corrected to
"a prime ideal 𝔭₃₁ ⊂ 𝒪_K of norm 31" and the (φ−2) factor removed. This
is a real error scoping caught; it does not damage the theorem (which is
level-agnostic) but the construction must target the right level.

---

## 1. The object we actually need

- **Field:** K = Q(√5), 𝒪_K = Z[φ], LMFDB label `2.2.5.1`.
- **Quaternion algebra:** B = (−1,−1 / K), the Hamilton quaternions over K.
  Ramified at exactly the two real places ∞₁, ∞₂ (definite). This is the
  algebra whose maximal order is the **icosian ring** — the same object
  underlying V_600.
- **Order:** an Eichler order 𝒪 ⊂ icosian ring of level 𝔭₃₁ (norm 31).
- **Forms:** cuspidal Hilbert modular forms of parallel weight 2, level
  𝔭₃₁, obtained via Jacquet–Langlands from B^×.
- **Hecke data wanted:** eigenvalues a_𝔭 for all prime ideals 𝔭 ∤ 𝔭₃₁
  with N(𝔭) ≤ 200 (≈ 46 prime ideals).

This is **exactly** Dembélé's 2005 setting (*Math. Comp.* 74, "Quaternionic
Manin symbols, Brandt matrices and Hilbert modular forms over Q(√5)").
He used Hamilton quaternions over Q(√5) and the icosian ring. The first
rational Hilbert newform over Q(√5) appears at level norm 31 and matches an
elliptic curve over Q(√5).

---

## 2. Three routes to the eigenvalues, ranked by realism

### Route A — LMFDB lookup (FAST, do this first)
The L-functions and Modular Forms Database has **precomputed** Hilbert
modular forms over Q(√5), including Hecke eigenvalues, and elliptic curves
over Q(√5) by conductor norm.

- **Effort:** hours to one day.
- **Deliverable:** table {𝔭, N(𝔭), a_𝔭} for N(𝔭) ≤ 200 at level norm 31.
- **Risk:** tabulated eigenvalue range may stop short of N(𝔭)=200; the
  exact level (which of the two norm-31 primes, plus weight/character) must
  be matched to the substrate. Both are checkable on the site.
- **URL path:** `lmfdb.org/ModularForm/GL2/TotalReal/2.2.5.1/holomorphic/`
  and `lmfdb.org/EllipticCurve/2.2.5.1/`.

### Route B — Reimplement Dembélé's Brandt-matrix algorithm (REAL BUILD)
If LMFDB is insufficient (e.g. need higher N(𝔭), or need the full Brandt
module not just one newform), build it:

1. Quaternion arithmetic over Z[φ] (Hamilton quaternions, icosian ring).
2. Right-ideal class set of the Eichler order of level 𝔭₃₁
   (enumeration via theta/neighbour method).
3. Brandt matrices B(𝔭) acting on the class set.
4. Diagonalise; Eisenstein projection (subtract N(𝔭)+1); read cuspidal a_𝔭.

- **Effort:** 2–4 weeks (this is the genuine engineering cost).
- **Risk:** correctness of ideal-class enumeration is the hard part;
  validate against LMFDB on the norm-31 newform before trusting new levels.
- **No SAGE support exists** for this over number fields; it is a from-
  scratch implementation. Voight, *Quaternion Algebras* (GTM 288), Ch. 41
  has the algorithms.

### Route C — Magma `HilbertCuspForms` (if access available)
Magma has the most complete implementation (the code LMFDB itself ran).
```
K := QuadraticField(5);
ZK := Integers(K);
p31 := Factorisation(31*ZK)[1][1];
M := HilbertCuspForms(K, p31);          // parallel weight 2
N := NewformDecomposition(M);
// HeckeEigenvalue(N[i], p) for primes p, N(p) <= 200
```
- **Effort:** days, IF Magma is available (commercial; free online
  calculator has a time/output cap that ~46 eigenvalues may fit under).
- **Risk:** licence/access only.

**Recommendation:** Route A first (cheap, may be sufficient and gives the
dimension check below for free). Fall back to C if reachable, B only if
both fail or higher N(𝔭) is needed.

---

## 3. The cheapest test runs BEFORE any eigenvalue: dimension match

(O2) claims the substrate's 26-dim block ↔ a Hecke-stable space. A
**necessary** condition, checkable in minutes:

> dim (cuspidal Hilbert modular space at level 𝔭₃₁, weight 2)
> must equal the dimension of the substrate block it is claimed to match.

- The genuine cuspidal dimension at norm 31 over Q(√5) is **small** (the
  first newform is rational, 1-dimensional Galois orbit; total cuspidal
  dimension at that level is a handful).
- The substrate block is **26-dim** (τ-fixed) per the V_600 spectral work.

**These do not obviously match.** If the genuine space is (say) 1- or
2-dimensional and the substrate block is 26-dimensional, then the
identification cannot be a naive equality — it must be "the substrate block
*contains* / *surjects onto* / *is graded by* the Hecke eigenform," and that
weaker claim has to be stated precisely or (O2) fails immediately.

**This dimension reconciliation is the first deliverable** and may already
kill or reshape (O2) at near-zero cost. Do it before computing eigenvalues.

---

## 4. The substrate side (independent input)

For the test to mean anything, the substrate numbers must be produced
**without ever consuming modular/Hecke data.** Provenance to pin down:

- **C_φ = (12 + φ⁻²)I − A₁** is defined purely from V_600 geometry
  (A₁ = adjacency). Its eigenvalues are geometric → independent. ✓
- **The prime-indexing map** p ↦ (substrate eigenvalue at p) is the
  suspicious step. In the proxy this came from a "𝔭-graded subspace."
  **Required:** this grading must be defined from geometry alone — e.g. via
  the icosian norm form representing 𝔭, or the Hecke-at-𝔭 action *intrinsic
  to the icosian ring* (which is geometric, not imported). If the grading
  was ever defined by reference to Brandt/Hecke eigenvalues, the whole test
  is circular and the result is empty.

**Deliverable:** a written provenance audit of the substrate→prime map,
with the exact line of code / definition that fixes it, confirming no
modular input.

---

## 5. The circle test (O2), designed to be non-circular

Two independent sequences:
- `H = {a_𝔭}` from LMFDB/Brandt (genuine Hecke), N(𝔭) ≤ 200.
- `S = {μ_𝔭}` from the substrate closure-flow, same primes.

### Test 1 — Provenance (logical, binary)
Does S consume any modular data anywhere in its definition? If yes →
circular, STOP. (See §4.)

### Test 2 — Out-of-sample prediction (the real test)
Defeats circularity even if the substrate map has free parameters:

1. Fix the substrate→prime map and any free constants using **only** primes
   with N(𝔭) ≤ P_split (e.g. P_split = 50).
2. **Predict** μ_𝔭 for primes in (P_split, 200] with no further tuning.
3. Compare against the genuine a_𝔭 on that held-out range.

- Match on held-out primes with **zero** free parameters → strong, genuine
  evidence the identification is real.
- Match only after fitting k parameters → discount by k; report honestly.
- No match → (O2) is false; the substrate eigenvalues are not Hecke
  eigenvalues. This is also a real, publishable result (boundary found).

### Test 3 — Normalisation / Ramanujan / Sato–Tate cross-check
Genuine a_𝔭 satisfy |a_𝔭| ≤ 2√N(𝔭) and Sato–Tate. Substrate μ_𝔭 must too,
*after the same normalisation fixed in step 1* — no per-prime rescaling.

**Acceptance criterion for "the circle holds":** Test 1 passes (no modular
input) AND Test 2 matches out-of-sample with ≤1 global normalisation
constant AND Test 3 holds. Anything less is reported as partial / negative.

---

## 6. Concrete work order

| # | Task | Route | Effort | Gate |
|---|---|---|---|---|
| W1 | Correct paper level: 𝔭₃₁ (norm 31), drop (φ−2) | — | 30 min | — |
| W2 | Locate level-31 HMF / curve over Q(√5) on LMFDB; record its cuspidal dimension | A | 0.5 day | — |
| W3 | Dimension reconciliation vs 26-dim block (§3) | A | 0.5 day | **kills/reshapes O2 if mismatch unhandled** |
| W4 | Extract genuine {a_𝔭}, N(𝔭) ≤ 200 | A→C→B | 1 day–4 wk | needs W2 |
| W5 | Provenance audit of substrate→prime map (§4) | — | 1 day | **circular if it fails** |
| W6 | Compute substrate {μ_𝔭} on the 26-dim block, primes ≤ 200 | — | 1–2 days | needs W5 clean |
| W7 | Run circle test 1/2/3 (§5) | — | 1 day | the verdict |
| W8 | Write honest result (match / partial / negative) | — | 1 day | — |

**Critical-path realism:** W1–W3 and W5 are cheap and *gate everything*.
Either of two near-free checks (dimension mismatch in W3, or modular input
in W5) can sink (O2) before we spend a single week on Route B. That is the
right order: run the cheap kill-tests first.

---

## 7. Honest expectations

- **Most likely cheap outcome:** W3 shows the genuine cuspidal space at
  norm 31 is far smaller than 26 dimensions, forcing (O2) to be restated as
  a *grading/projection* claim rather than equality. Whether that restated
  claim survives W7 is the real question.
- **The circularity risk is concentrated in W5.** If the substrate's
  prime-indexing was ever back-fitted to Hecke data, the entire "RH falls
  out" chain is empty, and we should say so plainly.
- **Best honest outcome:** W7 Test 2 matches out-of-sample with one
  normalisation constant. That would be genuine, checkable evidence — not a
  proof of RH, but the first non-trivial confirmation that the substrate
  eigenvalues *are* arithmetic Hecke data.
- **A negative is still worth having:** it draws the exact boundary of the
  programme and is publishable as such.

No step here proves RH. The scope's job is to make the one load-bearing
claim (O2) cheaply falsifiable. It now is.
