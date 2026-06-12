# Route B: Build the Substrate's Own Cuspidal Hecke Eigenvalues

The circle test needs a substrate sequence S = {a_P^sub} computed from the
icosians' OWN arithmetic (no modular data injected), to compare against the
genuine target H (`data/genuine_newform_eigenvalues.csv`, 44 eigenvalues,
already locked and verified). Route B builds S.

## Object
- K = Q(√5), 𝒪_K = Z[φ].
- B = (−1,−1 / K): Hamilton quaternions, ramified at both real places.
- I = icosian ring = maximal order; unit group = 2I (order 120) = V_600.
- Level 𝔭₃₁ = (5φ−2), norm 31 (the genuine newform's level).
- This is exactly Dembélé (2007); algorithms in Voight, *Quaternion
  Algebras* (GTM 288), Ch. 41.

## Steps and status

| Step | What | Status | File |
|---|---|---|---|
| 1 | Icosian ring: arithmetic over Z[φ], 120 units = 2I | **DONE, verified** | `icosian.py` |
| 1b | Rank-8 short-vector enumerator + reduced-norm theta | **DONE, verified** | `short_vectors.py` |
| 2 | Dimension at 𝔭₃₁ via P¹ model (class no. 1) | **DONE: dim=2, G1 PASS** | `step2_eichler.py` |
| 3–4 | Hecke operators T_𝔮 on the 2 orbits | **DONE** | `step3_4_hecke.py` |
| 5 | Cuspidal eigenvalues + circle test | **DONE: G4 PASS (11 ideals)** | `step3_4_hecke.py` |

**RESULT (2026-05-30): the circle closes.** Substrate a_𝔮 = genuine H on
all 11 prime ideals tested (N(𝔮) ∈ {4,5,9,11,19,29,41}), exact incl. signs
and split pairings, out-of-sample on 19/29/41. (O2) confirmed at this level.
See `CIRCLE_TEST.md` §9. The class-number-1 P¹ model made steps 2–4 tractable
without explicit Kneser ideal-class enumeration; the original `brandt_level31.py`
scaffold remains as the general-case route.

`icosian.py` verified (exact): 120 units, all reduced norm 1, full
14400/14400 multiplicative closure → binary icosahedral group 2I.

`short_vectors.py` verified (exact), three self-checking gates pass:
- r(2) = 120 (the units are exactly the norm-2 vectors);
- all 120 norm-2 vectors have reduced norm nrd = 1;
- **r_I(ν) = 120·(N(ν)+1)** for every prime ν (N = 4,5,9,11 checked) —
  i.e. the level-1 icosian theta IS the Eisenstein series with eigenvalue
  N(𝔭)+1, independently reproducing L(Θ_I,s) = ζ_K(s)·ζ_K(s−1).

This is the load-bearing primitive: Brandt entries (step 4) are exactly
counts of vectors of a given reduced norm in an ideal lattice — the same
enumeration applied to I_i I_j^{−1} instead of I. The remaining work is
steps 2–3 (build the Eichler order at 𝔭₃₁ and enumerate its ideal
classes); step 4 then reuses `short_vectors.enumerate_short` directly.

## Acceptance gates (cheap → expensive)
1. **G1** ideal-class count h == 2 (1 Eisenstein + 1 cuspidal). If not 2,
   the geometry/level is wrong — stop and recheck before step 4.
2. **G2** Eichler mass formula holds: Σ 1/|𝒪_i^×| = mass(𝒪).
   For B/Q(√5) ramified at both infinities, ζ_K(−1) = 1/30; the level-𝔭₃₁
   mass fixes h. This certifies the enumeration is complete.
3. **G3** the cuspidal eigenvalues are Ramanujan-bounded |a_P| ≤ 2√N(P)
   (else it isn't a cusp form).
4. **G4** `circle_test` exact_matches == 44 with **zero fitting**
   (one global sign allowed for Hecke normalisation). THE result.

## The two genuinely hard pieces (the ~2–4 week build)

### Step 3: ideal-class enumeration
Kneser p-neighbour method: from 𝒪 (as a right ideal), repeatedly form
𝔭-neighbour ideals for small split 𝔭, reduce each to a canonical
Minkowski-reduced representative via short-vector enumeration in the
rank-8 Z-lattice underlying each ideal, and collect inequivalent classes
until G2 (mass) is met. Needs: a reliable rank-8 lattice short-vector
enumerator over the trace form, and an ideal-equivalence test (two right
ideals I, J are equivalent iff I J^{−1} is principal ⟺ contains an element
of the right reduced norm — a short-vector search).

### Step 4: Brandt matrices
B(𝔭)_{ij} = (1/w_j) · #{x ∈ I_i I_j^{−1} : nrd(x) = 𝔭 · (unit-normalised)},
i.e. a theta-series coefficient of the rank-8 lattice I_i I_j^{−1}. Reuses
the step-3 short-vector machinery. The Hecke operator T_𝔭 = B(𝔭); the
cuspidal eigenvalue is its eigenvalue on the non-Eisenstein eigenvector.

## What is decisive
- If **G4 passes** (S == H, no fitting): the icosians' own arithmetic
  reproduces the genuine norm-31 newform. The circle closes; (O2) holds;
  the Fractal Tiling Theorem's hypothesis is genuinely on track at this
  level. This would be the first real, non-circular substrate↔Hecke match.
- If **G4 fails**: (O2) is false at this level — the substrate eigenvalues
  are not these Hecke eigenvalues. Also decisive, also publishable.

## Tooling note
No Python/Sage library does quaternion ideal classes over Z[φ]. Options:
(a) implement steps 3–4 in pure Python on top of `icosian.py` (the rank-8
short-vector enumerator is the main component); (b) use Magma
`HilbertCuspForms`/`Brandt` if access is available, purely to cross-check
the substrate computation — not as a substitute (Magma would compute the
modular side, which we already have via Route A; the point of Route B is
the *substrate-intrinsic* computation).
