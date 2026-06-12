# Proof-Status Table — WO-VFD-CLOSURE-CERTIFICATE-THEORY-001

Every claim in `closure_certificate_theory.tex`, graded. Verified numerically by
`verify_certificates.py` (14/14 checks PASS).

| # | Claim | Grade | Basis |
|---|---|---|---|
| Def 1–7 | generated system, boundary, positive form, modes, leakage, capacity, certificate | — | definitions |
| Lem 1 | dissipative certificate exists ⟺ ρ(T)<1 (Lyapunov form) | **PROVEN** | full proof + `L1_*` |
| Lem 2 | isometric certificate exists ⟺ power-bounded invertible (invariant inner product) | **PROVEN** | full proof + `L2_*` |
| Lem 3 | self-adjoint certificate exists ⟺ real-diagonalizable (symmetrizable) | **PROVEN** | full proof + `L3_*` |
| Cor 1 | reversible Markov chain ⟹ diag(π) self-adjoint cert; ergodic ⟹ contraction on 1⊥ | **PROVEN** | proof + `Cor_*` |
| Lem 4 | k-cycle ⟹ n(2^A−q^k)=Σ q^{k−i}2^{s_{i−1}}, 2^A>q^k | **PROVEN** | full proof |
| Prop 1 | only positive-integer 1-cycle of 3n+1 is n=1 | **PROVEN** | full proof (recovers Steiner 1977) + `P1_*` |
| Cor 2 | no nontrivial odd cycle for k≤6, a≤4 (3n+1) | **DIAGNOSTIC** | exhaustive finite check `Cor_no_small_cycles_3` |
| Collatz drift | mean capacity 2ln2−ln3>0 | **DIAGNOSTIC** | not a certificate |
| Collatz (full) | no infinite non-closing braid | **OPEN** | = the conjecture |
| RH | Weil positivity of explicit form | **OPEN** | = Connes arithmetic site |
| Navier–Stokes 3D | coercive high-frequency norm | **OPEN** | supercritical, sign of L_B unresolved |
| Yang–Mills | reflection positivity + spectral floor | **OPEN** | continuum construction |

**Known theorems recovered/reframed:** discrete Lyapunov stability (Lem 1),
detailed-balance self-adjointness of reversible chains (Cor 1), Steiner 1977 (Prop 1).
