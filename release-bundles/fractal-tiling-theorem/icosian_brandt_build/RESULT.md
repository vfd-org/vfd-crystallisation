# Genuine icosian Brandt computation — RESULT

Built the load-bearing TODO from route_b/brandt_level31.py (the genuine icosian Brandt
action at level p31 = (5φ−2)), from scratch, no Magma, no fitting.

## Method (Dembélé), all from the icosians' own arithmetic
1. Split the order mod p31: B⊗F31 ≅ M_2(F31) via i,j,k matrices; φ ≡ 19 mod (5φ−2).
2. Reduce the 120 icosian units → PGL_2(F31); orbits on P¹(F31) = the ideal classes.
   **Brandt dimension h = 2** (orbit sizes 12, 20) — 1 Eisenstein + 1 cuspidal. GATE PASS.
3. Hecke T_q (q split): enumerate icosian quaternions of reduced norm π_1 (a totally
   positive, even-trace generator of a prime over q), dedupe to the N(q)+1 left-U cosets,
   reduce mod p31, act on the 2 orbits → 2×2 Brandt matrix → eigenvalues.

## Out-of-sample results (cuspidal eigenvalue vs independent point-count a_P)
| q | π_1 | cosets=N(q)+1 | Eisenstein gate | cuspidal | point-count | match |
|---|---|---|---|---|---|---|
| 11 | 3+2φ | 12 ✓ | 12 ✓ | **−4** | −4/4 | ✅ |
| 19 | 5+6φ | 20 ✓ | 20 ✓ | **−4** | −4/4 | ✅ |
| 29 | 5+4φ | 30 ✓ | 30 ✓ | **−2** | −2 | ✅ |
| 41 | 7+8φ | 30 ✗ (need 42) | FAIL | — | −6 | ❌ enumeration incomplete |

**3/3 gate-valid primes match the point-count, out of sample, with no fitting.** The q=41
case is an incomplete `U·seed·U` enumeration (found 30 of 42 cosets) — the row-sum/Eisenstein
gate CAUGHT it (it reported FAIL, not a false match). Fix = a complete norm-π short-vector
enumerator; this is an engineering gap, not a geometry failure.

## What this means (honestly)
- **The icosian geometry GENERATES the cuspidal Hecke eigenvalues** — verified out-of-sample
  on 3 independent primes, each passing the Eisenstein gate. This is the genuine,
  non-fitted Brandt action.
- **This SUPERSEDES the earlier out-of-sample verdict** ("NOT DEMONSTRATED / map was fitted"):
  the fitted/hardcoded map was an artifact of the old engine; the *genuine* method works.
- **It reproduces KNOWN mathematics** (Jacquet–Langlands / Dembélé) computed in-house — it is
  NOT new mathematics and **NOT a proof of RH**. It confirms the geometry encodes the
  arithmetic of the cuspidal form; RH (positivity / the root geometry) is untouched.

Next: (a) complete the norm-π enumerator so q=41+ pass; (b) more primes for a fuller
Sato–Tate-style out-of-sample table.
