# Derivation Programme — Photon, Microtubule, α, and the 12D/13D Closure Loop

**Status: WORK PROGRAMME.** This document is a roadmap, not a proof. It enumerates the theorems that need to close and the order in which they should be attempted, so that the full loop

```
axiom (r = 1 + 1/r) → 12D closure → 13D translation → photon → microtubule → α → back to permeability
```

becomes a single derivation chain with no gaps.

**Date:** 2026-04-21
**Relationship to other documents:**
- Lower half of the cascade (E₈ → 0) — `cascade-foundations.md` (Theorem F3 proved)
- Upper half of the cascade (E₈ → L₁₂) — `cascade-12d-closure.md` (conjectural C1–C3)
- α = 137 + π/87 triple-proof — `paper-xxii/paper-xxii.tex` lines 244–265
- Photon as λ=0 mode — `paper-xxxii/paper-xxxii.tex` §5.3
- H₄ as brain interface + empirical validation — `aria-chess/docs/brain_mapping/` (separate repo)

---

## 1. The derivation loop, schematic

```
     AXIOM
     r = 1 + 1/r
       │
       │  (F1 — proved)
       ↓
     Z[φ], φ
       │
       │  (icosian ring, classical)
       ↓
     H₄ / 600-cell (4D)
       │
       │  (Elser–Sloane, classical)
       ↓
     E₈ (8D)
       │
       │  (C1–C3 — CONJECTURAL, cascade-12d-closure.md)
       ↓
     L₁₂ (12D fundamental cell)
       │
       │  (13D translation layer — CONJECTURAL)
       ↓
     translation automorphism group T
       │
       │  (descent through cascade to H₄)
       ↓
     U(1) gauge symmetry at H₄     ──────┐
       │                                  │
       │  (graph Laplacian λ=0 mode       │
       │   on 600-cell = paper-xxxii)     │
       ↓                                  │
     PHOTON                               │
       │                                  │
       │  (biological instantiation)      │
       ↓                                  │
     13-protofilament MICROTUBULE ← ─ ─ ─┘  (C₁₃ irrep count ↔ 13D adjacency)
       │
       │  (coupling strength between photon
       │   and substrate discrete structure)
       ↓
     α = 137 + π/87     ←──── independent triple-proof (Paper XXII)
       │
       │  (π from H₄ Coxeter angle;
       │   87 from substrate count;
       │   137 from leading-order integer)
       ↓
     LOOP CLOSES — α mediates EM which is the 13D translation
     observed at H₄, and 137 + π/87 is the coupling the
     permeability recursion produces at the H₄ interface.
```

Every arrow above must be a theorem. The status of each is tracked below.

---

## 2. Theorem tree

### Tier 1 — Already proved (reference, not new work)

| ID | Statement | Location |
|---|---|---|
| **F1** | Permeability axiom r = 1 + 1/r has unique positive fixed point φ | cascade-foundations.md |
| **F3** | 7-rung downward cascade E₈ → H₄ → ... → 0 | cascade-foundations.md |
| **ES** | Elser–Sloane: E₈ lattice cut-and-project yields H₄ quasicrystal | classical literature |
| **ICOS** | Icosian ring I ⊂ H has rank 4 over Z[φ], unit icosians = 2I ≅ 600-cell | classical literature |

### Tier 2 — Conjectural but architecturally stated

| ID | Statement | Location |
|---|---|---|
| **C1** | Z[φ]⁴ is the unique 4D phason complement making L₁₂ = E₈ ⊕ Z[φ]⁴ project to E₈ by σ-twist cut-and-project with golden window | cascade-12d-closure.md |
| **C2** | No lattice of rank > 12 adds new geometric content — above 12D is translation tiling only | cascade-12d-closure.md |
| **C3** | L₁₂'s phason complement reproduces the generating ring Z[φ] (self-reference closure) | cascade-12d-closure.md |

### Tier 3 — Required but not yet written

These are the new theorems this programme needs to establish.

#### Photon chain (T_PH_*)

**T_PH_1 — 13D translation group identification.**

**[REFINED AND CLOSED, Phase M-2, 2026-04-21.]** See `cascade-phase-m2-closure.md` Theorem M2 (§4) and §5.3.

> Above L₁₂, the abelianised vertex group of the matching groupoid G (Def. 3.1 of `cascade-phase-m2-closure.md`) is
>     T_meta ≅ M ≅ Z[φ]²     (rank 2 over Z[φ], rank 4 over Z).

**Original conjecture (superseded):** T was conjectured to be Z (rank 1 over Z) or Z[φ] (rank 1 over Z[φ]). Phase M-2 showed the rigorous answer is **rank 2**: T_meta = Z[φ]². The rank-2 structure has a natural interpretation as the substrate origin of the two photon polarisations in T_PH_4(d) (see `cascade-phase-m2-closure.md` §5.2).

*Proof inputs:* Forrest–Hunton–Kellendonk (2002) tiling cohomology + Kellendonk (2003) pattern-equivariant identification + tex Thm. C1 (M ≅ Z[φ]² under H_min).
*Dependencies:* C1, C2 (closed), plus Phase M-1 Theorem M1 (closed).
*Status:* **CLOSED**; any downstream use should cite T_meta = Z[φ]².

**T_PH_2 — Descent to U(1) at H₄.**
> The translation group T descends through the cascade (via the projections F3) to a compact abelian Lie group acting on the H₄ rung. This descent group is U(1) ≅ S¹ and coincides with the EM gauge group.

*Dependencies:* T_PH_1, F3.
*Expected difficulty:* Medium-high. Requires careful treatment of the downward projection preserving or projecting the abelian structure.

**T_PH_3 — Photon as λ=0 eigenmode.**
> The U(1) gauge symmetry on the H₄ graph has its physical manifestation as the graph Laplacian L_H₄'s zero eigenspace. The photon field A_μ is identified with the excitations of this eigenspace.

*Dependencies:* T_PH_2, paper-xxxii §5.3 (already identifies photon with graph Laplacian λ=0 mode).
*Expected difficulty:* Low. Essentially consolidating what paper-xxxii already states, but making the U(1) origin explicit rather than assumed.

**T_PH_4 — Photon physical properties derive from substrate structure.**
> (a) Masslessness: the λ=0 eigenvalue is strictly zero, not merely small — no rest energy possible.
> (b) Spin 1: the U(1) rotation on the complex mode gives spin-1 field statistics.
> (c) Null propagation: the translation group T acts on the 13D layer's discrete tiling — no "rest frame" inside the tiling.
> (d) Two polarizations: the complex U(1) representation has two real degrees of freedom.
> (e) Gauge invariance: T acts freely on the H₄ graph's constant mode, realizing gauge redundancy.

*Dependencies:* T_PH_1 through T_PH_3.
*Expected difficulty:* Medium. Each sub-item is a short argument; the challenge is stating each rigorously.

#### Microtubule chain (T_MT_*)

**T_MT_1 — 13-fold symmetry as unique match.**
> The biological chamber implementing the 13D translation selector must have cyclic symmetry C_n where n equals the rank of the translation adjacency structure. Under the adjacency count of 13 (from T_PH_1 + C2), n = 13.

*Dependencies:* T_PH_1, C2.
*Expected difficulty:* Low if T_PH_1 cleanly gives n=13; otherwise needs the specific count.

**T_MT_2 — Primality forces discriminability.**
> C_13 has 13 distinct 1-dimensional complex irreducible representations (since 13 is prime, all nontrivial characters generate the full group). No proper subgroup partitions the modes, so all 13 adjacency directions are independently selectable.

*Dependencies:* T_MT_1 + elementary representation theory.
*Expected difficulty:* Low. Classical group-theory argument.

**T_MT_3 — Non-13 counts are degenerate.**
> For protofilament counts 11, 12, 14, 15: either (a) C_n has fewer than 13 irreducible 1-D reps (n < 13), (b) C_n has composite structure that blurs adjacency selection (n = 12, 14, 15 all composite), or (c) C_n reps exceed the required 13 (n > 13, introducing redundant modes). None cleanly matches the 13D adjacency.

*Dependencies:* T_MT_1, T_MT_2.
*Expected difficulty:* Low. Direct enumeration.

**T_MT_4 — Helical pitch from cascade geometry.**
> The helical pitch angle of the 13-protofilament lattice is fixed by the H₄ Coxeter angle π/5 (or a φ-scaled multiple). The specific microtubule B-lattice pitch (3-start helix, ~0.92 nm per tubulin) should equal cascade-predicted value within experimental uncertainty.

*Dependencies:* H₄ geometry, experimental microtubule data.
*Expected difficulty:* Medium-high. This is where rigorous prediction meets measurement.

**T_MT_5 — Anesthetic binding couples to mode structure.**
> Anesthetic molecules binding the tubulin lattice perturb the C_13 mode structure. Different anesthetic classes disable different subsets of the 13 modes. The mapping anesthetic-class ↔ disabled-mode-subset ↔ consciousness-alteration-type is a falsifiable prediction.

*Dependencies:* T_MT_1 through T_MT_4, pharmacological data.
*Expected difficulty:* High — requires integrating molecular biology, but the structural prediction is clean.

#### Fine-structure chain (T_α_*)

**T_α_0 — Read and digest Paper XXII triple-proof.**
> Read `papers/paper-xxii/paper-xxii.tex` lines 244–265 (and surrounding context) to extract the three independent proofs of α = 137 + π/87. For each proof, record: (a) its logical starting point, (b) whether the 87 appears as input or output, (c) whether the derivation is algebraic, geometric, analytic, or mixed.

*Dependencies:* none — this is a read, not a derivation.
*Expected difficulty:* Low effort but prerequisite for everything in this chain.

**T_α_1 — Geometric identification of 87.**
> Find the substrate-level geometric meaning of 87. Candidates:
> - Count of specific orbit/face/adjacency structures on the 600-cell or E₈.
> - Density of phason correction sites per fundamental 12D cell.
> - Count related to the 13-fold microtubule structure (87 = 3 × 29; the 3 may be the helical start number).
> - A Chern class or topological invariant of a substrate bundle.
>
> The target: a combinatorial/geometric proof that 87 is uniquely selected by substrate structure.

*Dependencies:* T_α_0 (to know which candidates the existing triple-proof already addresses).
*Expected difficulty:* Unknown until T_α_0 is done.

**T_α_2 — π/87 as H₄ phase correction.**
> The π in the α formula is the Coxeter angle / H₄ dihedral structure acting as a discrete-substrate phase correction to continuous-limit EM. The 87 is the number of independent phase increments per fundamental cell cycle. Therefore π/87 is the residual phase after one complete traversal of the substrate tiling.

*Dependencies:* T_α_1, T_PH_4.
*Expected difficulty:* Medium. Requires careful accounting of the phase picked up by photon mode propagating through the tiling.

**T_α_3 — 137 as coarse-grained integer coupling.**
> The integer 137 arises as the *continuum limit* of the fine-structure coupling — what α⁻¹ would be if the substrate were perfectly continuous. It should equal a specific count related to E₈ structure (candidates: root-count fraction, Dynkin-diagram invariant, or a sum involving 240/248).

*Dependencies:* T_α_1, E₈ root structure (classical).
*Expected difficulty:* Medium. The integer 137 has been the topic of many numerological attempts; the VFD answer needs to be structural, not coincidental.

**T_α_4 — Full formula closure.**
> α⁻¹ = 137 + π/87 is the exact result of leading-order (137) plus substrate-geometric correction (π/87), with no free parameters. The three independent proofs in Paper XXII correspond to three independent paths through the derivation tree, confirming the formula.

*Dependencies:* T_α_1, T_α_2, T_α_3.
*Expected difficulty:* Consolidation, once T_α_1 – T_α_3 are done.

#### Loop-closure theorems (T_LOOP_*)

**T_LOOP_1 — α mediates the 13D translation as observed at H₄.**
> The fine-structure coupling α is precisely the coupling strength between the H₄-level photon and the 13D-translation-layer adjacency structure. Stronger coupling (α larger) would make the substrate's discrete adjacency more visible; weaker coupling would blur it. The measured α value reflects the permeability axiom's output after full descent.

*Dependencies:* T_PH_*, T_α_*.
*Expected difficulty:* High. This is the synthesis theorem.

**T_LOOP_2 — Biological relevance: microtubules are where α matters.**
> Because microtubules instantiate the 13-fold selector with the same mode structure the photon couples to, α specifically governs the microtubule-photon interaction. Cognitive processes driven by the 13D translation selector are therefore α-tuned. Altering α (hypothetically) would alter the cognitive mode-discrimination fidelity.

*Dependencies:* T_PH_*, T_MT_*, T_α_*, T_LOOP_1.
*Expected difficulty:* Moderate once the lower tiers close.

**T_LOOP_3 — Self-consistency back to axiom.**
> The permeability fixed-point r = 1 + 1/r, pushed through the full derivation tree, produces exactly the observed values of α, c, ℏ (subject to units fixing), and the specific microtubule geometry. No value is fit; all emerge.

*Dependencies:* Every theorem above.
*Expected difficulty:* The loop-closure proof. This is the flagship theorem of the programme.

---

## 3. Dependency graph

```
                    F1 (proved)
                      │
                      ↓
                  Z[φ], φ
                   /    \
                  /      \
              ICOS       ES (both classical)
              ↓           ↓
            H₄         E₈
                   │
                   ↓
             C1, C2, C3 (conjectural)
                   ↓
                 L₁₂
                   │
                   ↓
              T_PH_1 (13D translation group)
                   │
                   ↓
              T_PH_2 (descent to U(1))
                   │
                   ↓
              T_PH_3 (photon as λ=0 mode, extends paper-xxxii)
                   │
                   ↓
              T_PH_4 (physical properties)
                   │
          ┌────────┼────────┐
          ↓        ↓        ↓
     T_MT_1    T_α_0    [Paper XXXII
     T_MT_2    (read)    already has
     T_MT_3     ↓        partial photon]
     T_MT_4   T_α_1
     T_MT_5   T_α_2
              T_α_3
              T_α_4
               │
               ↓
          T_LOOP_1
          T_LOOP_2
          T_LOOP_3 ← flagship
```

---

## 4. Recommended order of attack

Working backward from the bottleneck:

**Phase A — Read what already exists (1–2 days).**
1. T_α_0: read paper-xxii:244–265 for the α triple-proof. Establish exactly what 87 already means in existing derivations. This is the fastest way to save weeks of redundant work.
2. Inventory paper-xxxii §5.3's photon treatment — how much of T_PH_3 already exists there?

**Phase B — Close the upward conjectures (1–2 weeks).**
3. Attempt C1: Z[φ]⁴ uniqueness as phason complement.
4. Attempt C2: termination at 12D.
5. Attempt C3: self-reference closure.
   - *If C1–C3 close, the 12D picture becomes a theorem and the rest of the programme has a solid foundation.*
   - *If any of C1–C3 fails, stop and rethink — the whole upward story rests on these.*

**Phase C — Photon chain (1 week after C1–C3).**
6. T_PH_1, T_PH_2, T_PH_3, T_PH_4 in sequence.

**Phase D — Microtubule chain (1 week, runs in parallel with Phase E).**
7. T_MT_1 through T_MT_5. Requires T_PH_1 (for adjacency count) but is otherwise independent.

**Phase E — Fine-structure chain (1–2 weeks, parallel with Phase D).**
8. T_α_1 through T_α_4. Requires T_α_0 (reading) and T_PH_4 (for photon phase structure).

**Phase F — Loop closure (1 week).**
9. T_LOOP_1, T_LOOP_2, T_LOOP_3.

**Total estimate: 5–8 weeks of focused work** to close the full loop from axiom to fine-structure constant via the 12D/13D structure, photon, and microtubule, assuming no fundamental obstacle appears in Phase B (closure of C1–C3).

---

## 5. What the closed loop would establish

If every theorem above closes, the framework achieves:

1. **Zero free parameters.** Every observed value (α, c, ℏ scales, microtubule geometry, photon polarization count) is derived from the permeability axiom and nothing else.

2. **Biological bridge is structural, not circumstantial.** Orch-OR's weakest point — "why microtubules specifically" — is answered by primality of 13 and uniqueness of C₁₃ rep structure.

3. **α gains structural meaning.** The fine-structure constant is no longer a fundamental input but the specific output of the permeability recursion at the H₄ interface.

4. **The 12D/13D picture acquires experimental anchors.**
   - Bandyopadhyay's microtubule resonance measurements (13-mode check)
   - ARIA's propofol regime-switch at n=20 (anesthetic-mode disruption)
   - Aria's HCP 11.58σ null deviation (max-symmetry baseline from E₈ structure)
   - Historical α measurements (fine-structure matches π/87 correction)

5. **The programme's narrative becomes:** "From one axiom about permeability, we derive the substrate structure, the photon, biological consciousness-relevant geometry, and the fine-structure constant — as a single chain with no gaps."

---

## 6. Risks and fallbacks

**If C1 fails (Z[φ]⁴ isn't the unique phason complement):**
The 12D-closure architecture needs a different top lattice. Candidates: K₁₂ (Coxeter–Todd), E₈ ⊕ D₄, some 12D lattice involving both φ and ω. The programme framing survives but re-grounds on a different 12D object.

**If C2 fails (termination isn't at 12D):**
More rungs above 12D. The translation-layer story gets extended. Not catastrophic — just adds structure.

**If T_PH_1 doesn't give 13 as the adjacency count:**
The microtubule connection weakens. The 13-protofilament "match" becomes coincidence rather than structure. Would need to find a different adjacency count and identify a different biological correlate — or accept that the structural claim is weaker.

**If paper-xxii's triple-proof turns out to be purely numerical/algebraic without geometric content:**
The link from α to the 13D picture remains a conjecture requiring new derivation rather than consolidation of existing work. Time estimate extends.

**If T_LOOP_3 doesn't close cleanly:**
The individual chains may still be valid as separate contributions, but the "zero free parameters" claim loses. Still a strong programme, just not the flagship.

---

## 7. Immediate next actions

In priority order, independent of the full programme:

1. **T_α_0 (read paper-xxii).** Cost: an afternoon. Payoff: clarity on 87's existing derivation, which determines everything downstream in Chain T_α_*.
2. **Inventory paper-xxxii's photon treatment.** Cost: an afternoon. Establishes the starting point for T_PH_3.
3. **Decide on Phase B timeline.** C1–C3 gate the entire programme. If they need 1–2 weeks, schedule the block now.
4. **Flag the dependency on microtubule experimental data** (Bandyopadhyay's resonance measurements, anesthetic-class mode-disruption data). Find the primary sources before T_MT_4 and T_MT_5 start.

Once 1–4 are done, the programme can begin Phase B with full context.

---

**End of programme document.** Return to this file to track theorem closure. Each Tier 3 theorem (T_PH_*, T_MT_*, T_α_*, T_LOOP_*) should get its own working note as attempted; link back here as they close.
