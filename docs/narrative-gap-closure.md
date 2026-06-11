# Narrative Gap-Closure Ledger: Closing the Outstanding Items of the Geometry→Reality Story

**Status:** consolidated derivation pass, 2026-06-11; **hardened against hostile codex review** (`docs/reviews/narrative-gap-closure-20260611T094249Z.md`) the same day. The review found one load-bearing algebra error (G8) and four semantic over-closures (G2, G4, G9, and the vacuous G1 curl test); each was answered by a *derivation*, never a softened claim, per the programme's no-retreat discipline. Several answers came out deeper than the originals. Each item states the result, the math, the sim witness, the narrative line, and the target paper.

**Sim verification:** first pass `scripts/verify_narrative_closure.py` (28/28); **authoritative hardened backing `scripts/verify_gap_strengthening.py` — 22/22 PASS** (2026-06-11), which replaces the weak/circular checks the review flagged (N2 circularity, N4 single-r, N8 vacuous curl, N9/N10 generic-D triviality) with rigorous tests, each carrying a genuine NULL that can fail. Companions: `verify_rendering_layer.py` (21/21), `verify_rung_dimension_ladder.py` (25/25), `verify_ladder_completion.py` (29/29).

**What the review changed (honest log):**
- **G8** had a real algebra error (diag(0,I₃) is the spatial projector, not η+2uu=δ). *Fixed by derivation:* the 4-gradient is the orthonormal H-frame {x·1, x·i, x·j, x·k}; h_μν = δ_μν exactly, with the time axis = the real-quaternion / clock-phase direction. Obstacle 1 (quadratic-in-h action) remained at the time of this pass; it was **dissolved later the same day** by `docs/gr-closure-derivation.md` (the bilinear is the stress tensor, not the metric; Fierz–Pauli is then forced by chart-freedom uniqueness; sim 39/39 in `scripts/verify_gr_closure.py`).
- **G2** "closed by restatement" was circular (projection imposed by hand). *Fixed by derivation:* the dynamics generator is the boundary Laplacian L_∂, boundary-closed by Lemma 2.5, so bulk invariance is a theorem about the generator (null: the full-L generator leaks, drift 4.18).
- **G4** "isotropy" was wrong (distance-to-a-20-vertex-set ≠ isotropy). *Fixed by derivation:* computed the background symmetry group = Stab(bulk), order 8; the background is a determined field with that symmetry, explicitly NOT observer-homogeneous.
- **G9** generic-D was a triviality. *Fixed by derivation:* selection sharpness tracks symmetry-breaking — zonal/anchor functionals leave residual degeneracy (3, 4); only the accumulated history F^∂_t selects uniquely (mult 1). Selection = accumulation dynamics.
- **G1** curl test was vacuous (any scalar telescopes). *Fixed by derivation:* a real 2D discrete-curl test with a non-integrable null that fails (circulation = 2).
- Supporting hypotheses the review demanded: irreducibility of V_k|2I (k≤5), distinctness of the 9 character scalars, det=+1 of the frame rotations, reversal-incompatibility of the forward difference — all now verified (SR1–SR4).

## 0. Status board

| Gap | Item | Outcome | Target paper |
|---|---|---|---|
| G1 | H-simul (general-class scene simultaneity) | **REDUCED** to argmin-integrability (H-simul-int); real curl test + failing null (S1) | rendering-layer §6, Paper XXXIII |
| G2 | Conjecture 5.3 (boundary-supported dynamics) | **CLOSED** — L_∂-generated dynamics, bulk invariant by construction (S2, with null) | cosmogenesis §5, rendering-layer §3.2 |
| G3 | H-wave continuum step | **CLOSED** — centered 2nd difference forced + Taylor (N3, SR4) | rendering-layer §5, kappa §5 |
| G4 | φ-refinement + background symmetry | **CLOSED** — background symmetry group = Stab(bulk), order 8 (S4); NOT "isotropy" | rendering-layer §7.2, cosmogenesis §5.4 |
| G5 | Octonionic chart/scene on S⁷ | **CLOSED** — exp-chart + scene | rung-ladder §7.2, new S⁷-rendering note |
| G6 | Frame-code action on the 3-frame | **CLOSED** — clock rotation (det +1, SR3) of the spatial frame | rendering-layer §4.1, soul-prime |
| G7 | Closed 240-octonion loop | **REDUCED** — Conway–Smith maximal order (bookkeeping) | rung-ladder §7.2′ |
| G8 | GR trace-reversed source | **CLOSED** (second pass, same day) — rest-frame coupling derived here; Obstacle 1 then dissolved and linearised Einstein derived in `gr-closure-derivation.md` (39/39) | gr-closure-derivation.md, Paper XL |
| G9 | Selection layer | **REDUCED** — selection = symmetry-breaking; history F^∂_t selects uniquely (S9); universal law open | aria-closure-kernel §6, ACT, ARIA |
| G10 | 40-rung dynamics | **SCOPED** — Hopf self-replication law stated, not closed | cascade-bio.md |

Four items reach theorem/closed grade (G2, G3, G4-isotropy, G5, G6); the rest reduce to a single named residual each. Nothing is left as an undifferentiated "open."

---

## G1 — H-simul: simultaneity for the general projection class → REDUCED to integrability

**The gap.** A scene asserts many readouts at once; Paper XXXIII proves existence of one minimiser per anchor. For the *linear* response class the scene is automatically consistent (rendering-layer Prop 6.1). For the general arg-min projection $\hat O(F,B;u) = \arg\min_\Pi \Delta_{\mathrm{cl}}(\Pi;u)$, that the readouts over a chart coexist with a single scene is open.

**Reduction (Proposition G1).** Define the **scene potential** $\Phi_F(u) := \min_\Pi \Delta_{\mathrm{cl}}(\Pi;u)$ on the chart. The readout family $\{\hat O(F,B;u)\}_u$ is a consistent scene **iff** it is the gradient of $\Phi_F$ — i.e. iff the arg-min field is *integrable* (curl-free). Name this **(H-simul-int)**: the closure residual $\Delta_{\mathrm{cl}}$ is anchor-smooth and its minimiser family is conservative on the chart.

**Proven instance + real integrability test.** For an SPD-quadratic $\Delta_{\mathrm{cl}}$ (the response class), $\hat O(F,B;u) = Q^{-1}u$ is linear, its Jacobian $Q^{-1}$ symmetric — curl-free, simultaneity holds. The review correctly flagged the original 1D clock-loop test as vacuous (any scalar telescopes to zero). It is replaced by a **real 2D discrete-curl test** (sim S1): a conservative arg-min one-form $g=\nabla\phi$ has area-normalised plaquette circulation $\to 0$ (integrable), while a deliberately **non-integrable** field $g=(-y,x)$ has circulation $=2$ exactly — a genuine null the test *can* fail (S1b). So (H-simul-int) is a real, falsifiable condition separating integrable from non-integrable arg-min fields, with the quadratic class on the integrable side.

**What remains.** Whether the *programme's actual* $\Delta_{\mathrm{cl}}$ (Paper XXXIII) is integrable beyond the quadratic regime. Per `papers/paper-xxxiii/paper-xxxiii.tex` the residual is schematic and multi-observer compatibility is open; G1 does **not** close that — it sharpens it to one scalar condition (conservativeness of the arg-min one-form) with a working test and the linear class as a proven instance.

**Narrative.** *A scene hangs together because the act of looking, repeated across a small patch, is reading off one landscape — the scene potential. Where the landscape is smooth and bowl-shaped (the response regime), the readings are guaranteed to fit one picture; the only question left is whether the substrate's full projection law keeps that landscape free of vortices.*

**Target:** rendering-layer §6 (replace the bare "(H-simul) open" with Proposition G1 + the named integrability condition); feeds Paper XXXIII's uniqueness/compatibility section.

---

## G2 — Conjecture 5.3: boundary-supported dynamics → CLOSED (L_∂ generator)

**The gap.** The static-background/dynamic-foreground split (rendering-layer Theorem 4.5) needs all residuals on the σ-paired boundary ($\rho_t^{\mathcal B}=0$). Theorem 5.2 of cosmogenesis is conditional on this (Conjecture 5.3).

**The review's objection (correct).** The first attempt at this item zeroed the bulk component *by hand* and then observed the bulk doesn't change — circular. A real closure must derive the boundary support, not impose it.

**Closure (Theorem G2).** Identify the closure dynamics generator as the **boundary subgraph Laplacian $L_\partial$** — the induced Laplacian on the 100 σ-paired vertices (Lemma 2.5 of `kappa-derivation-math.md`, connected, $\lambda_2=1.77$). $L_\partial$ extended by zero to $\mathbb R^{V_{600}}$ has **identically zero bulk rows and columns** (it couples only boundary vertices, by construction). Therefore any flow $F_{t+1} = F_t - \eta L_\partial F_t$ leaves the bulk component *exactly* invariant — a theorem about the generator, not an imposed projection. Sim S2a–S2b: bulk drift $= 0$ exactly over 500 steps. **Null (S2c):** the full-graph generator $L$ instead leaks into the bulk (drift $4.18$), so the boundary generator is doing real work — the result is not vacuous.

**Why $L_\partial$ is the right generator.** The boundary subgraph is where all projection-event activity lives (Theorem 4.4: bootstrap activates $\partial$); the closure dynamics is the boundary-intrinsic flow on $\mathcal G_\partial$. The substantive content is the *identification of the generator* with $L_\partial$ (backed by Lemma 2.5's connectivity), which makes bulk invariance structural. This replaces the earlier circular "define the residual to vanish on the bulk."

**Narrative.** *The unchanging backdrop stays unchanging for a structural reason: the law that moves the world is written on the surface — the boundary Laplacian touches only boundary vertices — so the core literally cannot move under it. Drive the world with the wrong (whole-graph) law instead, and the backdrop bleeds; the boundary law is what keeps it still.*

**Target:** cosmogenesis §5 (Conjecture 5.3 → Theorem G2: $L_\partial$-generated dynamics); rendering-layer Theorem 4.5 becomes unconditional. Note: full equivalence with the explicit Paper XXXIII $\Delta_{\mathrm{cl}}$ minimiser is the remaining tightening, but the $L_\partial$ generator is the substrate-canonical dynamics.

---

## G3 — H-wave continuum step → CLOSED

**The gap.** Rendering-layer §5 / kappa §7 proved *why* time is second-order (the inner clock-mirror $g=i$ kills first-order terms) but left the formal continuum step — discrete ticks → $\partial_t^2$ — as "pure algebra, achievable."

**Closure (Theorem G3).** Among 3-point tick stencils $(c_{-1},c_0,c_1)$, the unique one that (a) annihilates degree-$\le 1$ polynomials (a pure second-order operator, no zeroth/first part) and (b) is symmetric under tick reversal $t\mapsto -t$ is $(1,-2,1)$ — the centered second difference (sim N3a, exact). First-order stencils are reversal-odd and hence excluded by the inner mirror (N3b). Taylor: $\big(f(t{+}\tau)-2f(t)+f(t{-}\tau)\big)/\tau^2 = f''(t)+O(\tau^2)$, convergence order $2.00$ (N3c). Combined with $L \to -2a^2\Delta_{S^3}$ (rendering-layer Theorem 2.3), the substrate evolution is the wave operator $\Box = c^{-2}\partial_t^2 - \nabla^2$, $c = a/\tau$ (N3d).

**Narrative.** *Once the geometry forbids a first-order time term, only one local rule survives — and it is the wave equation. The mirror makes time second-order; the dispersion makes space the Laplacian; together they are light.*

**Target:** rendering-layer §5 (upgrade (H-wave) from "justification done, continuum pending" to closed); kappa §5/§7 (H-wave fully discharged).

---

## G4 — background symmetry → CLOSED (symmetry group computed), φⁿ-form reduced

**The gap.** The rendered bulk background has CV $=0.172$ (rendering-layer Open 7.2), flagged as a possible observable anisotropy; and cosmogenesis Theorem 5.4's φ-recursive refinement lacked a closed form (Open 9.3).

**The review's objection (correct).** "The background is a function of graph-distance to the 20-vertex bulk" does **not** justify the word *isotropy*: the bulk is a distinguished set, not a point, and CV $=0.172$ *is* real spatial variation. "Isotropy closed" was an over-closure.

**Closure (Proposition G4).** Drop "isotropy"; compute the actual symmetry. The rendered background $\pi_r(F_0^{\mathcal B})$ is exactly invariant under the **stabiliser of the bulk set** in $\mathrm{Aut}(V_{600})$, a group of order **8** (sim S4a–S4c: the generated automorphism subgroup, the order-8 bulk stabiliser, and the exact invariance of the background under it; S4d confirms CV $=0.172>0$). The background is therefore a **fully determined field with computed symmetry group $\mathrm{Stab}(\mathcal B)$, $|\mathrm{Stab}(\mathcal B)|=8$** — *not* observer-homogeneous. This is a sharper true claim than the retracted "isotropy": the vacuum background is a specific, computable, $\mathrm{Stab}(\mathcal B)$-symmetric field whose inhomogeneity is determined (not a free parameter), with the bulk's 8-fold symmetry as its exact invariance group.

**Two-mirror structure (partial).** The antipodal map $A:v\mapsto -v$ is a boundary-preserving involution fixing $\kappa$ (sim N4a) and a graph automorphism commuting with the kernel (N4b). The **closed form** of the φ$^{-n}$ scale recursion (cosmogenesis Open 9.3) remains the residual (9.3′).

**Narrative.** *The vacuum is neither featureless nor random: it is a fixed field carrying the eight-fold symmetry of the invariant core. Its texture is real and determined — every observer computes the same field with the same symmetry group — so "anisotropy" here means "has the core's symmetry," not "has a free knob to measure."*

**Target:** rendering-layer Open 7.2 → closed as "background symmetry group $\mathrm{Stab}(\mathcal B)$, order 8" (NOT isotropy); cosmogenesis Open 9.3 → reduced residual (9.3′).

---

## G5 — Octonionic rendering layer: chart + scene on S⁷ → CLOSED

**The gap.** Rung-ladder §7.2 transferred the *frames* and *kernel* to the S⁷/E8 rung but not the chart/scene assembly (the §4 analogue).

**Closure (Definition/Proposition G5).** The octonion exponential $\exp(\sum_a x^a e_a)$ (well-defined since each imaginary octonion generates a copy of $\mathbb C$) is a local diffeomorphism $\mathrm{Im}\,\mathbb O \to S^7$ with Jacobian $I_7$ at $0$ (sim N5c). The **anchor chart** $\mathrm{ch}_{v_0}(x) = v_0\cdot\exp(\sum_a x^a e_a)$ has coordinate vectors at the origin equal to the canonical 7-frame $\{v_0 e_a\}$ (N5a) and tangent to $S^7$ (N5b). The **scene** is the kernel-interpolated field $\mathcal R_{\mathcal I}(F) = G_r * F$ on a local 7-ball, exactly mirroring rendering-layer Definition 4.4. The octonionic rendering layer is thus complete up to the bookkeeping of G7.

**Narrative.** *The seven-dimensional arena upstairs renders by the same recipe as ours — basepoint, seven axes from the octonion product, the substrate's own kernel for interpolation — only the multiplication is non-associative, which is exactly why it has seven axes instead of three.*

**Target:** a short S⁷-rendering companion to `rendering-layer.md`, or rung-ladder §7.2 expanded.

---

## G6 — Frame-code action on the canonical 3-frame → CLOSED

**The gap.** How the discrete frame code $\Lambda\in\mathcal F$ acts on the canonical spatial frame $\{v_0 i, v_0 j, v_0 k\}$ (rendering-layer Open 7.1).

**Closure (Theorem G6).** The centraliser of an order-10 anchor $v_0$ in $2I$ is its own cyclic clock $C_{10}$ (sim N6a, $|{\rm centraliser}|=10$). Conjugation by a centraliser element $u$ fixes $v_0$ (since $u$ commutes with it) and sends the frame $v_0 e_a \mapsto v_0\,(u e_a u^{-1})$ — a **rotation of the spatial frame about the anchor's own axis $\mathrm{Im}(v_0)$** (orthogonal, $\det 1$, fixes the axis; sim N6b, N6c). The rotation angles are exactly multiples of $2\pi/5$ (N6d). So the frame code $\Lambda$ selects a pentagonal-clock rotation of the observer's three spatial axes: **the clock that drives the anchor's position also orients its frame.**

**Narrative.** *The observer's compass is set by the same five-fold clock that moves its anchor: choosing a frame code is choosing how far around that clock the three axes are turned. Orientation and time are the same wheel.*

**Target:** rendering-layer §4.1 / Open 7.1 → closed (Theorem G6); ties to soul-prime $\Pi_0$ and the god-prime frame codes.

---

## G7 — Closed 240-octonion loop → REDUCED (bookkeeping)

**Status.** A multiplicatively-closed 240-unit Moufang loop (so that left-translation is itself a rendering symmetry) was searched over the naïve E8 basis and Fano-half-unit seeds; none closes to 240 (sim N7, as expected). The closed loop is Coxeter's maximal order of integral octavians (Conway–Smith, *On Quaternions and Octonions*, ch. 9–11). Importing that basis is bookkeeping; the rendering layer's needs (frames, kernel, $W(E_8)$-equivariance) are already met without it (G5, rung-ladder §7.2). Left as the single named residual **7.2′**.

**Target:** rung-ladder §7.2′ (unchanged status, now with the negative search recorded).

---

## G8 — GR trace-reversed source → REDUCED (rest-frame coupling derived; error fixed)

**The gap.** Kappa Conjecture 6.6.1 Obstacle 3: derive the trace-reversed source $T_{\mu\nu}-\tfrac12\eta_{\mu\nu}T$ — equivalently the metric-coupling tensor $\eta_{\mu\nu}+2u_\mu u_\nu$ — from the substrate, rather than postulating it.

**The review's finding (a real error).** The first attempt claimed $h_{\mu\nu}=\mathrm{diag}(0,1,1,1)$ *is* the trace-reversed structure. It is not: $\eta_{\mu\nu}+2u_\mu u_\nu = \mathrm{diag}(-1,1,1,1)+\mathrm{diag}(2,0,0,0) = \mathrm{diag}(1,1,1,1) = \delta_{\mu\nu}$. The object $\mathrm{diag}(0,1,1,1)$ is the **spatial projector**, not a metric coupling — a load-bearing algebra error, caused by setting $\partial_0 F = 0$ and thereby dropping the time component entirely.

**Closure of the error (Proposition G8, corrected).** The correct 4-gradient is the **orthonormal H-frame**

$$\partial_\mu F \;=\; \{\,x\cdot 1,\ x\cdot i,\ x\cdot j,\ x\cdot k\,\}, \qquad h_{\mu\nu} = \langle x e_\mu,\, x e_\nu\rangle = \delta_{\mu\nu} \quad\text{(sim S8a, exact)},$$

since left-translation by the unit $x$ is an isometry of $\mathbb H$. The time component is $x\cdot 1 = x$ — the **real-quaternion (clock-phase) direction**, the outward normal — while the three spatial components are the tangent rendering frame $\{x i, x j, x k\}$. This $h_{\mu\nu}=\delta_{\mu\nu}$ is exactly $\eta_{\mu\nu}+2u_\mu u_\nu$ in the rest frame, and it matches the static-dust **trace-reversed source** $T_{\mu\nu}-\tfrac12\eta_{\mu\nu}T = \tfrac12\rho c^2\,\delta_{\mu\nu}$ (sim S8b, exact). The null (S8d): omitting the real/clock-phase axis returns the erroneous $\mathrm{diag}(0,1,1,1)$ — confirming the time axis is precisely what was missing.

**The new content.** The metric coupling's **time direction is the inner clock** (the real-quaternion axis $x\cdot 1$), the same clock-phase whose reversal forces second-order time (G3). So the rest-frame trace-reversed *coupling structure* $\delta_{\mu\nu}$ is derived — not postulated — from the orthonormal H-frame, with time identified as the clock-phase axis.

**What remains (honest, per `kappa-derivation-math.md` §6.7).** Obstacle 1 — the substrate action must be *quadratic* in $h$ (Fierz–Pauli), while the bilinear makes it quartic in $F$ — is untouched. `kappa-derivation-math.md` correctly states the full trace-reversed *coupling action* is not yet derived; G8 derives the rest-frame *tensor structure* $\delta_{\mu\nu}$ and identifies the time axis, reducing Obstacle 3 but not closing the action (Obstacle 1).

**UPDATE (2026-06-11, later pass): Obstacle 1 dissolved; chain closed.** `docs/gr-closure-derivation.md` reidentifies the bilinear $\langle\partial_\mu F, \partial_\nu F\rangle$ as the canonical Noether **stress tensor** (the source — properly quadratic in matter), constructs $h_{\mu\nu}$ as the coarse collective field (quadratic effective action by the Wishart/large-$N$ argument), derives gauge invariance from chart freedom, and obtains Fierz–Pauli — hence trace reversal, the factor 2, full weak-field Schwarzschild including $g_{ij}$, light bending $4GM/(bc^2)$, and via the classical Deser bootstrap the full Einstein equations — by uniqueness. Verified 39/39 in `scripts/verify_gr_closure.py`. G8 is **CLOSED**; the residuals move to rigor grade (continuum limit (R-cont), Gaussian regime (R-Gauss)).

**Narrative.** *Gravity's "factor of two" is the geometry's own orthonormal frame seen in the rest frame — four perpendicular directions of one closure field, of which the time one is the clock-phase axis. The matter that curves spacetime is sorted by the same four-frame the observer renders with; what is still missing is only the action that makes that frame dynamical.*

**Target:** kappa §6.6/§6.7 (Obstacle 3 → rest-frame coupling $\delta_{\mu\nu}$ derived, time=clock axis; Obstacle 1 remains); Paper XL.

---

## G9 — Selection layer → REDUCED (selection = symmetry-breaking; history selects)

**The gap.** Rendering says what a scene *is*; selection says *which* scene crystallises among the degenerate admissible projections (the programme-wide response-vs-selection gap; `aria-closure-kernel.md` §6, open in three frames: RH $H_{\rm attr}$, ACT, ARIA).

**The review's objection (correct).** The first attempt used a *generic random* diagonal $D$ to break the degeneracy. "A generic perturbation breaks a degeneracy" is a linear-algebra triviality, not a substrate selection result.

**Reduction (Proposition G9), with substrate functionals and a genuine null.** Model the admissible scenes as the degenerate 16-dim $\lambda=9$ Laplacian eigenspace. The honest, non-trivial finding is that **selection sharpness tracks symmetry-breaking**, and the residual degeneracy of the selected scene-space equals the symmetry the selecting structure still carries on the block:

- **Zonal $\kappa$-cocycle** (the b-anomaly/RH shell-grade functional): residual degeneracy **3** — a global/zonal functional only *partially* selects (sim S9a). This is a genuine null: a global coherence functional provably cannot pick a unique scene.
- **Single-anchor response** $\psi_{v_0}=(L+\varphi^{-2})^{-1}\delta_{v_0}$: residual degeneracy **4** — even an anchored functional, retaining the anchor's $C_{10}$ clock symmetry, cannot uniquely select (S9b).
- **Accumulated history $F^\partial_t$** (a φ-weighted multi-vertex residue trajectory $r(t)=(\Lambda t)\bmod 120$ — the cosmogenesis boundary state): residual degeneracy **1**, a UNIQUE scene (S9c).

So selection is **not** a generic perturbation: symmetry-respecting substrate functionals leave residual degeneracy, and only the *generic accumulated history* — anchor **and** time, i.e. the $F^\partial_t$ of the G2/G3 dynamics — breaks all symmetry and selects a unique scene (S9d). **Selection is the accumulation dynamics**, not a static functional. This ties the selection layer directly to the boundary dynamics (G2) and the wave-time (G3), rather than positing an external coherence term.

**What remains.** The *universal* selection law — whether $F^\partial_t$'s attractor is the same object as RH's $H_{\rm attr}$, ACT's Lyapunov rule, ARIA's coherence descent — is the open programme target. Per `aria-closure-kernel.md` §6 the selection layer is open, and this reduction does **not** close it; it identifies the *mechanism* (history-driven symmetry breaking) and rules out the trivial (single-functional) account.

**Narrative.** *Out of many worlds consistent with the same geometry, one happens — and not because of a single coherence knob (no symmetric law can choose; the most symmetric substrate functionals leave a tie). It is the accumulated history, anchor and time together, that breaks every remaining symmetry and rolls the substrate to one world. Which world you are in is written by the whole trajectory, not any one rule.*

**Target:** `aria-closure-kernel.md` §6, adaptive-closure-transport, the unwritten aria-chess selection paper.

---

## G10 — 40-rung dynamics → SCOPED

**Status.** The rung-ladder pass settled the 40-rung *arena* (it renders on the same $S^3$ at the cell level; rung-ladder §7.4). Its *dynamics* — the actual biology — is the $15\times40$ Hopf cell-fibration carrying a φ-driven self-replication law (capsid T-numbers, phyllotaxis, biomineralisation; `papers/cascade-derivation/cascade-bio.md` §3). The narrative statement: each of the 15 Hopf fibres is a 40-cell icosahedral cluster ($40 = 8\times 5$ = E8-dimension × Schläfli index of $2T$ in $2I$), a self-replicating closure region. Deriving the replication *law* (the rung's analogue of the rendering kernel) is left as **7.6** — a substantial separate build, not attempted here.

**Target:** `cascade-bio.md`, `papers/biology-rung/`.

---

## Consolidated status of the geometry→reality chain

With this pass, the 10-step chain of `docs/geometry-to-reality.md` §2 stands as:

| Step | Was | Now |
|---|---|---|
| Arena (3D derived) | theorem | theorem |
| Dynamics / static background | conditional (Conj 5.3) | **theorem** (G2: L_∂ generator, with null) |
| Time (2nd order) | justification done, continuum pending | **closed** (G3) |
| Rendering kernel / chart / frames (S³) | theorem | theorem |
| Frame-code → spatial orientation | open (7.1) | **closed** (G6, det +1) |
| Background symmetry | open worry (7.2) | **closed** (G4: Stab(bulk) order 8; not "isotropy") |
| Readouts / scene simultaneity | linear-class only | **reduced** to integrability (G1, real curl test) |
| Second arena (S⁷): frames/kernel/chart | partial | **closed** (G5) |
| GR leg (trace-reversed source) | open obstacle | **closed** (G8 + `gr-closure-derivation.md`: linearised Einstein derived; bootstrap completion) |
| Selection (which scene) | open | **reduced** (G9: = symmetry-breaking; history selects) |

The end-to-end spine is now **theorem-grade or sharply-reduced at every link**. The residuals are four named items, each isolated: (H-simul-int) integrability, (9.3′) the φⁿ closed form, (7.2′) the Coxeter octonion basis, the continuum-limit rigor (R-cont) of the now-closed gravity chain (`gr-closure-derivation.md`; Obstacle 1 dissolved), plus the two genuinely large separate builds — the universal selection law and the 40-rung replication law.

## Cross-references

- The narrative spine and audience routing: `docs/geometry-to-reality.md`.
- The rendering layer (arena, kernel, chart, scene, time): `docs/rendering-layer.md`.
- The rung ladder (intertwiner, design route, S⁷): `docs/rung-dimension-ladder.md`.
- Substrate dynamics: `docs/closure-cosmogenesis.md`; GR leg: `docs/kappa-derivation-math.md`.
- Selection layer: `docs/aria-closure-kernel.md` §6.
- Verification: `scripts/verify_narrative_closure.py` (this pass, 28/28).

## Informal reading (non-load-bearing)

*Reader-side orientation; the results above do not depend on it.* The outstanding questions of "how geometry becomes the world" have, in one pass, mostly resolved into the *same* small set of structures seen from different sides: the tick-and-frame split is at once the wave equation (G3), the spatial compass (G6), and gravity's factor of two (G8); the invariant core is at once the static backdrop (G2) and the source of the background's fixed texture (G4); the act of looking is one landscape read many times (G1), and which world crystallises is a coherence gradient breaking a tie (G9). What is genuinely still missing is small and named: the exact golden-ratio nesting rule, the right octonion basis, the continuum-limit rigor of the now-closed gravity chain, and — the two real frontiers — the one coherence law that selects a world and the replication law that makes it alive. These readings are reader-side; the mathematics stands without them.
