# Paper 3 — Math Catalogue (D/L/T/N/R entries)

Cross-references use stable LaTeX labels. Each entry's status records
how it is established. Most are exact computational claims established
by `verify.py`; the reflection-obstruction entry is presented as a
computational remark (Remark 3.1, label `rem:reflfail`), not a proved
theorem.

The shared pytest suite at `papers/v600-programme/tests/` (currently
39 tests) covers the static-map P1–P4 properties via
`test_tau_sigma.py`; this paper adds a stronger reproducible
construction-and-rebuild certificate in `verify.py`.

## Definitions

- **D1.** Trace inner product
  ⟨v, w⟩_tr := Tr_{K/Q}(Re(v · conj(w))) (defined in §2.1, "Trace
  inner product"; not a numbered LaTeX label). Rational-valued on
  cross-Galois pairs (in fact in (1/4)·Z) for the V_600 vertices.
  *Status:* explicit definition.

- **D2.** Phase-j swap τ_σ^(j) per non-bulk right coset
  (label `def:phaseswap`, §4). 10 phases per coset; involution on
  each coset by construction.  *Status:* explicit; verified.

- **D3.** Symmetric maximin score
  s(j) = min_k min(⟨σ(v_k), w_{(j+k) mod 10}⟩_tr,
                   ⟨σ(w_{(j+k) mod 10}), v_k⟩_tr)
  (label `def:maximin`, §4). Two-sided minimum makes the score
  symmetric in the two cycles; matches the form verified in
  `verify.py`. Selects admissible phases per coset.
  *Status:* explicit; verified.

- **D4.** Canonical τ_σ (label `def:canonical`, §4). Phase-(0,0,0,0,0)
  composition; 120-vertex map in `data/tau_sigma_canonical.txt`.
  *Status:* explicit; rebuilt and matched in `verify.py`.

## Lemmas

- **L1.** *Right-coset carrier* (label `lem:rightcoset`, §2). Every
  non-bulk right coset Hg is one whole K=52 cycle + one whole K=20
  cycle. Cited from Paper 1 ("Coset cycle composition" lemma);
  this paper does NOT re-prove it.
  *Status:* shared-pytest regression confirms left/right asymmetry;
  whole-cycle right-coset structure verified in `verify.py`.

## Remarks (computational, not theorems)

- **R1.** *Reflection obstruction* (label `rem:reflfail`, §3).
  Computational observation, two families:
  (a) `block3c_e8_reflection_obstruction.py` (with embedding helpers
  in `block3a_e8_icosian_lattice.py`) checks single Euclidean-reflection
  candidates fixing H = Dic_5 pointwise; each such candidate acts
  trivially on V_600 in the tested embedding.
  (b) `block3b_parity_flip_tau_sigma.py` searches the parity-flip
  family for a V_600-permutation fixing H pointwise, swapping
  K=52 ↔ K=20, and closed under 2I; it reports zero target hits.
  The paper does NOT claim a closed-form non-existence theorem and
  does NOT claim an exhaustive Weyl-group enumeration. The τ_σ
  construction does not depend on this remark mathematically.

- **R2.** *Convention vs. freedom* (unlabelled remark, §6, after
  Theorem 5.1). The labels {0, 5} for the maximin phase set are
  convention-dependent; what is intrinsic is |Φ(Hg)| = 2 and that
  the two winning phases are antipodal (separated by 5 on Z/10,
  equivalently related by τ^5 = −1). The specific labels arise
  from (i) the choice of base points v_0 ∈ C_52 and w_0 ∈ C_20 in
  Definition 4.1 (both fixed by `vfd_v600.icosian.build_vertices()`),
  and (ii) the deterministic vertex ordering. A different choice of
  base points relabels phases by a shift j → j + c, but the Z_2^5
  orbit of canonical lifts is intrinsic.
  *Status:* convention-tracking remark.

## Theorems

- **T1.** *Phase selection* (label `thm:phases`, §4). For every
  non-bulk right coset, the maximin admissible phase set is {0, 5}
  (in the canonical cycle/base-point ordering) with s(0) = s(5) = 0
  and s(j) = −5/4 otherwise. The two winning phases are intrinsically
  separated by 5 (antipodal index shift).
  *Status:* Verified — `verify.py` enumerates all 5 cosets × 10
  phases and asserts the EXACT score table, not just the argmax set.

- **T2.** *Canonical τ_σ properties* (label `thm:main`, §5). The four
  canonical properties (P1)–(P4) plus antipodal compatibility. The
  theorem statement covers (P1) involution, (P2) fixes Dic_5,
  (P3) cross-K coset swap, (P4) T_τ-equivariance, and antipodal
  compatibility — these are the load-bearing claims.
  *Status:* Proved in §5 and re-verified by `verify.py` on the
  rebuilt 120-vertex map.

- **T2b.** *Right-coset preservation* (post-build certificate; not in
  Theorem 5.1 statement). Setwise preservation of right cosets holds
  by Definition 4.3, since the canonical τ_σ is built coset-by-coset
  with each phase swap internal to a single right coset. (P1)–(P4)
  alone do NOT imply this — one could in principle pair a K=52 cycle
  of one coset with a K=20 cycle of another and still satisfy
  (P1)–(P4); the per-coset internality is an additional input from
  the construction.
  *Status:* Verified — `verify.py` "right-coset preservation"
  assertion.

## Numerical results

- **N1.** Phase-(0,0,0,0,0) lift = canonical map.
  *Status:* Verified — `verify.py` rebuilds and compares
  vertex-by-vertex against `data/tau_sigma_canonical.txt`.

- **N2.** Z_2^5 = 32 valid phase combinations all yield (P1)–(P4)
  involutions.
  *Status:* Verified — `verify.py` enumerates all 32 phase
  combinations.

- **N3.** Worked example: cycles 2 and 3 have explicit vertex lists,
  paired by phase-0 swap.
  *Status:* Documented in §4.4 of the paper; reproducible by inspecting
  `state["cycles"]` from `vfd_v600.group.build_state()`.

## Verification entry points

- `papers/tau-sigma-construction/verify.py` — primary certificate.
- `papers/v600-programme/tests/test_tau_sigma.py` — shared P1–P4 test.

## Out-of-scope (reserved for companion papers)

- Physics interpretation of τ_σ (Paper 4 / 5 territory).
- Operator-trace cosmology applications using τ_σ (Paper 4).
- Unified V_600 framework (Paper 5).
- Cosmology, BH, Hawking spectrum.
- Generalisation to higher Coxeter groups (Tier-2).
- Closed-form proof of the reflection obstruction (Tier-2; current
  status: computational observation in Remark 3.1).
