# Follow-up paper map — "Closure & Resonance across Three Domains"
## Resumable skeleton (do NOT need to re-derive; pick up here)

*Companion to `CLOSURE_RESONANCE_THREE_DOMAINS.md`. This is the paper plan + status ledger
so the work can be resumed cold. Every claim carries a status: VERIFIED / ANALOGY / OPEN /
INTERPRETIVE. Honest-scope guardrail (non-negotiable): the unification is shared mathematical
structure, not physical identity; RH is not proven; the cognitive layer is the reader's.*

---

### Working title
"The Lossless Boundary: a closure/resonance certificate shared by the Riemann zeros, black-hole
ringdown, and dissipative cognition."

### One-sentence thesis
A single certificate algebra — *closure = a positive invariant form; lossless (self-adjoint) vs
lossy (dissipative/amplifying)* — and its frequency-domain face (resonance) organize three
domains; RH is the lossless-boundary case, black holes the dissipative neighbour with the same
scattering math, cognition a dissipative-closure model.

---

### Section skeleton (with status + the next concrete step for each)

**§1 The certificate algebra (FOUNDATION — VERIFIED).**
- Source: `closure_certificate_theory/` (PDF, 4 lemmas + corollary + proposition, 14/14 checks).
- Content: dissipative⟺ρ<1 (Lyapunov); isometric⟺|λ|=1; self-adjoint⟺real spectrum; critical⟺defective ρ=1. Closure = positive invariant form B.
- NEXT: lift the lemmas verbatim; no new work needed.

**§2 Resonance = the frequency face (FRAMING — VERIFIED restatement).**
- real frequency = lossless bound state; complex = resonance (leaky/amplifying).
- NEXT: the only-narrative result to report honestly — the naive P_σ leakage metric
  (`prime_resonance_closure/`) is tautological at σ=½ and blind to zeros; the *correct* object
  is the explicit-formula fluctuation x^β. Cite both (the negative is part of the honesty).

**§3 RH — the lossless boundary (CORE; coefficient-side VERIFIED, wall OPEN).**
- RH ⟺ no amplifying mode ⟺ ‖K‖≤1 ⟺ Weil positivity ⟺ lossless. [RH-EQUIVALENT]
- VERIFIED: icosian Brandt → cuspidal Hecke eigenvalues 24/24 OOS, dimension sequence
  (level-31 threshold), W₃₁=+1 (`icosian_brandt_cuspidal_geometry/`).
- OPEN: the self-adjoint engine (Hilbert–Pólya / Connes / arithmetic site).
- NEXT (optional, bounded): extend the Brandt out-of-sample table to norm ~500 (more forms);
  complete the cuspidal-dimension cross-check vs Dembélé/LMFDB tables.

**§4 Black holes — the dissipative neighbour (ANALOGY; shared math VERIFIED in toy).**
- QNMs = resonances (complex ω); ω_I>0 = superradiance = the off-line/amplifying analog.
- Correspondence table (zero↔QNM, off-line↔superradiance, ‖K‖≤1↔no over-reflection, σ=½↔extremal threshold).
- VERIFIED toy: `horizon_capacity_bridge/` — Pöschl–Teller, fake-Γ→‖K‖=1.67, true→‖K‖→1.
- HONEST: structural correspondence (Berry–Keating xp, near-horizon CFT, Lax–Phillips); BH gives
  vocabulary + solvable toy, NOT a proof; the "Riemann black hole" = same unbuilt object.
- NEXT (optional): a clean Pöschl–Teller QNM-vs-bound-state computation contrasting complex
  (leaky) and real (lossless) spectra, as the figure that makes §4 concrete.

**§5 Mind / ARIA — dissipative closure (MODEL; structure VERIFIED, meaning INTERPRETIVE).**
- VERIFIED: C_φ classified; crystallisation operator = MIXED (dissipative + 1 gauge mode),
  F a Lyapunov function (`vfd_core.closure`, certify); ARIA layer-0/3 audit 6/6.
- INTERPRETIVE: "attractor = thought / C_φ = cognition" is hypothesis, the human seat.
- NEXT (optional): run a real ARIA session trajectory through `interpret_states` and report its
  closure mode — live data, clearly flagged as model not proof.

**§6 The unified table + the honest line.**
- One structure, three regimes (RH lossless-boundary / BH dissipative-superradiant / mind
  dissipative-closure). The single shared missing object = the lossless self-adjoint engine
  (RH and the Riemann-BH both need it).
- NEXT: lift the table from `CLOSURE_RESONANCE_THREE_DOMAINS.md` §4.

---

### Status ledger (the spine of the paper's credibility)
| claim | status | source |
|---|---|---|
| certificate lemmas | **VERIFIED (proved)** | closure_certificate_theory |
| geometry → cuspidal arithmetic (24/24) | **VERIFIED (no fit)** | icosian_brandt_cuspidal_geometry |
| HMF dimension sequence (31-threshold) | **VERIFIED** | icosian_brandt_build |
| W₃₁ = +1 | **VERIFIED** | curve reduction + Brandt |
| resonance ⟺ RH | **RH-EQUIVALENT (restatement)** | route_c, ‖K‖≤1 |
| naive P_σ leakage metric | **REFUTED (narrative)** | prime_resonance_closure |
| BH ↔ RH (QNM/superradiance) | **ANALOGY (shared scattering math)** | horizon_capacity_bridge + lit |
| mind = dissipative closure | **MODEL; structure VERIFIED, meaning INTERPRETIVE** | vfd_core.closure |
| RH itself | **OPEN** (lossless self-adjoint engine unbuilt) | — |

### Open research questions (the "come back to it" list)
1. Construct (or rule out) a lossless self-adjoint operator whose spectrum = the zeros, using
   the resonance/scattering selection principle (real spectrum, √p normalization, GUE). [the wall]
2. Does the BH↔RH correspondence give any *transportable* positivity (Hodge-index analog via
   near-horizon CFT)? — likely no, same wall; worth stating precisely.
3. Extend Brandt OOS table + dimension cross-check (bounded, real, more forms).
4. Live-ARIA closure-mode trajectory (model-level, interpretive).

### References to gather (for the eventual paper)
Weil (RH for curves), Connes 1999 (trace formula / adele class space), Connes–Consani
(arithmetic site), Berry–Keating (xp), Deninger (foliated flow), Hilbert–Pólya, Dembélé
(ℚ(√5) HMF), Jacquet–Langlands, Davenport–Heilbronn (mirror ≠ on-line), Montgomery–Odlyzko (GUE),
Pöschl–Teller / BH QNM literature, Li's criterion / Bombieri–Lagarias.

### Honest-scope guardrail (put in the abstract, verbatim spirit)
"This paper proves no Millennium problem. It exhibits one verified result (the icosian geometry
generates a cuspidal automorphic form's arithmetic, out-of-sample, with no fitting), and maps a
shared closure/resonance structure across RH, black-hole ringdown, and dissipative cognition.
The shared missing object — a lossless self-adjoint engine — is named, not constructed."
