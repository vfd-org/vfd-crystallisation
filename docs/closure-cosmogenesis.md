# Closure Cosmogenesis: Initial Condition, Bootstrap, and Accumulation

**Status:** mathematical derivation, 2026-04-28. **Updated 2026-06-10:** Theorem 6.3 corrected (literal pointwise bulk-fixing was too strong) and Open 9.2 closed (canonical kernel derived) via `docs/rendering-layer.md`. Specifies the dynamical layer of the cascade closure framework: the initial condition $F_0$ for the substrate state, the bootstrap event that activates dynamics, the accumulation operator under projection events, and the coarse-graining map that couples the 8-frame ladder. Companion to `docs/projection-narrative.md`, `docs/fractal-cascade-projection.md`, and `docs/soul-prime-as-pi0.md`. Mathematical content; Informal reading is a single non-load-bearing closing subsection per `feedback_mathematical_framing_discipline`.

## 1. Position

The closure projection operator $\hat O(\mathcal G, B; \Pi_0)$ (Paper XXXIII) and the soul-prime anchor identification $\Pi_0(p, \Lambda, t)$ (`docs/soul-prime-as-pi0.md`) specify the projection of the substrate state $F$ at any tick $t$, given an anchor. They are **silent on**:

- the substrate state $F_0$ before any projection event,
- the first projection event ("bootstrap") that activates dynamics,
- the dynamical law for $F$ under repeated projection events,
- how the same $F$ is seen at different resolutions across the 8-frame ladder.

This document supplies the mathematical layer for those four pieces using the σ-fixed / σ-paired cycle decomposition of `docs/fractal-cascade-projection.md` §"A–B set decomposition." The strategy is to identify the σ-fixed bulk as the **invariant store** and the σ-paired boundary as the **dynamical surface** — an information-theoretic holographic decomposition forced by the cascade arithmetic.

## 2. Substrate state space and the bulk/boundary decomposition

Recall (`fractal-cascade-projection.md` §"A–B set"; `papers/cascade-derivation/scripts/derive_pentagonal_clock_*.py`):

- $V_{600}$ has 120 vertices, decomposed by the pentagonal-clock $T_\tau$ into 12 cycles of length 10.
- The K-multiset is $\{72:1,\ 0:1,\ 52:5,\ 20:5\}$, with $K(C) = \sum_{v \in C} \kappa(v)$, $\kappa(v) = (\mathrm{shell}(v) - 4)^2$.
- The σ-Galois involution $\sigma: \mathbb{Q}(\sqrt 5) \to \mathbb{Q}(\sqrt 5)$ partitions the 12 cycles into:
  - **Bulk** $\mathcal B := \{\text{K=72 cycle}\} \cup \{\text{K=0 cycle}\}$ — 2 cycles, 20 vertices, σ-fixed (singletons).
  - **Boundary** $\partial := \{\text{K=52 cycles}\} \cup \{\text{K=20 cycles}\}$ — 10 cycles, 100 vertices, σ-paired pairs.

So $V_{600} = \mathcal B \sqcup \partial$ with $|\mathcal B| = 20$ and $|\partial| = 100$.

**Definition 2.1 (Substrate state space).** Let $\mathcal S := \mathbb{R}^{V_{600}}$ (functions $V_{600} \to \mathbb{R}$). The substrate state $F_t \in \mathcal S$ is the closure functional value at each vertex at tick $t$. Decompose

$$F_t \;=\; F_t^{\mathcal B} + F_t^{\partial}, \qquad F_t^{\mathcal B} := F_t|_{\mathcal B},\ F_t^\partial := F_t|_\partial.$$

Linearity of restriction makes this decomposition canonical.

**Definition 2.2 (σ-invariance).** A state $F \in \mathcal S$ is σ-invariant if $F \circ \sigma = F$, where $\sigma$ acts on $V_{600}$ by the σ-Galois lift to icosian arithmetic. Denote $\mathcal S_\sigma \subset \mathcal S$ the σ-invariant subspace.

**Lemma 2.3.** $\mathcal B \subset \mathcal S_\sigma|_{V_{600}}$ in the sense that any function supported on $\mathcal B$ is automatically σ-invariant; functions supported on $\partial$ are σ-invariant if and only if they are constant on each σ-paired cycle pair.

**Proof.** σ-fixed cycles are pointwise σ-fixed; σ-paired cycles are exchanged in pairs by σ, so σ-invariance on $\partial$ requires equal values on σ-paired partners. $\square$

## 3. The initial condition $F_0$

**Definition 3.1 (σ-bulk-supported state).** $F \in \mathcal S$ is σ-bulk-supported if $F^\partial = 0$, i.e., $F$ is supported on $\mathcal B$ only.

**Theorem 3.2 (Existence and uniqueness of $F_0$ up to normalisation).** Among σ-invariant states satisfying

(i) σ-bulk-supported (no σ-paired boundary support),
(ii) $\Delta_{\mathrm{cl}}(F; F) = 0$ (closure to oneself with vanishing residual),
(iii) $F$ is constant on each cycle of $\mathcal B$,

there exists a one-parameter family $F_0 = a \cdot \chi_{K=72} + b \cdot \chi_{K=0}$ for $a, b \in \mathbb{R}$, $\chi_C$ the indicator of cycle $C$. Up to overall normalisation $a^2 + b^2 = 1$ and a single relative phase $b/a \in \mathbb{R}$, $F_0$ is determined.

**Proof.** σ-bulk-supported (i) restricts $F$ to $\mathcal B$. Constancy on each cycle (iii) restricts $F$ on $\mathcal B$ to a 2-parameter family (one parameter per cycle in $\mathcal B$). σ-invariance on $\mathcal B$ holds automatically by Lemma 2.3. Closure with vanishing residual (ii) is Δ_cl(F; F) = 0; for σ-bulk-supported states this is trivially satisfied because the σ-paired boundary residuals are absent and the σ-fixed cycles produce no nontrivial closure-violation by σ-invariance. So the constraint set reduces to (a, b) ∈ ℝ². Normalisation removes one degree of freedom. $\square$

**Definition 3.3 (Canonical initial condition).** Set the relative phase $b/a$ such that $a, b$ correspond to the spectral weights of the K=72 and K=0 cycles in the σ-symmetric factorisation of $\hat z(z)$ (`docs/rh-cascade-closure-dynamics.md` §"B11 Mellin formalisation"). Concretely:

$$F_0 \;=\; \frac{1}{\sqrt{m_{72}^2 + m_0^2}} \bigl( m_{72} \cdot \chi_{K=72} + m_0 \cdot \chi_{K=0} \bigr) \;=\; \tfrac{1}{\sqrt 2}\bigl(\chi_{K=72} + \chi_{K=0}\bigr),$$

since $m_{72} = m_0 = 1$ (the σ-fixed cycles are singletons in the K-multiset). $F_0$ is the symmetric distribution over the 20 bulk vertices, normalised to unit $L^2$ on $V_{600}$.

**Remark 3.4.** Theorem 3.2 makes $F_0$ structurally forced once the σ-bulk-supported condition is imposed. The condition is not arbitrary: it is the *unique* class of states for which no σ-paired boundary activity exists, which is the structural definition of the pre-projection regime (no projection events have occurred to inject σ-paired residuals).

## 4. Bootstrap event

**Definition 4.1 (Trivial residue series).** A residue series $r_p(\Lambda, t) = (\Lambda \cdot t) \bmod p$ is trivial in $V_{600}$ if its image under $((\Lambda t) \bmod p) \bmod 120$ lies entirely within $\mathcal B$.

**Lemma 4.2.** For prime $p > 120$ with $\gcd(\Lambda, p) = 1$, the residue series $r_p(\Lambda, t)$ visits all of $\mathbb{Z}/p$ as $t$ ranges over $\{0, 1, \ldots, p-1\}$ (Lemma 4.1 of `docs/soul-prime-as-pi0.md`). Composing with $\bmod 120$ visits all of $\mathbb{Z}/120 = V_{600}$ infinitely many times. Hence for $p > 120$ coprime to $\Lambda$, the residue series is non-trivial in $V_{600}$ (visits $\partial$ as well as $\mathcal B$).

**Proof.** The map $\mathbb{Z}/p \to \mathbb{Z}/120$ via reduction mod 120 is surjective for $p > 120$. The pre-image of $\mathcal B \subset \mathbb{Z}/120$ has at most $20 \cdot \lceil p / 120 \rceil$ elements out of $p$; the complement is non-empty. $\square$

**Definition 4.3 (Bootstrap event).** A bootstrap event is the first projection event $\hat O(\mathcal G, B; \Pi_0(p_1, \Lambda_1, 0))$ such that the residue series $r_{p_1}(\Lambda_1, t)$ for $t \in \{0, 1, \ldots, T_{\text{boot}}\}$ is non-trivial in $V_{600}$ for some $T_{\text{boot}} > 0$.

**Theorem 4.4 (Bootstrap activates the σ-paired boundary).** Let $F_0$ be as in Definition 3.3 and let $\hat O$ be applied with anchor $\Pi_0(p_1, \Lambda_1, t)$, with the residue series visiting $\partial$ at some tick $t^* > 0$. Then the residual $\rho_{t^*}$ contributed by the projection event satisfies $\rho_{t^*}^\partial \neq 0$ (the σ-paired boundary support is non-zero after the event).

**Proof.** $\hat O(\mathcal G, B; \Pi_0)$ minimises $\Delta_{\mathrm{cl}}(\Pi; \Pi_0)$. With $F_0$ σ-bulk-supported and $\Pi_0(p_1, \Lambda_1, t^*) \in \partial$ (a vertex on a σ-paired boundary cycle), the closure residual $\Delta_{\mathrm{cl}}(\Pi; \Pi_0)$ has non-zero gradient at $F_0$ in the $\partial$-direction: the σ-bulk-supported $F_0$ is a non-anchor for a $\partial$-anchored projection. The minimiser $\Pi^*$ therefore has support on $\partial$, and the residual $\rho_{t^*} := F_{t^*+1} - F_{t^*}$ has $\rho_{t^*}^\partial = \Pi^* - F_0|_\partial = \Pi^* \neq 0$. $\square$

**Corollary 4.5 (Symmetry-breaking inevitability).** For any $p_1 > 120$ coprime to $\Lambda_1$, the bootstrap event is inevitable: by Lemma 4.2 the residue series visits $\partial$, and by Theorem 4.4 the projection event activates $\partial$.

## 5. Accumulation operator

**Definition 5.1 (Accumulation operator).** For projection event $t$ producing residual $\rho_t \in \mathcal S$, the accumulation operator is

$$\boxed{\;\; F_{t+1} \;=\; \mathcal A(F_t, \rho_t) \;:=\; F_t + \rho_t. \;\;}$$

**Theorem 5.2 (Bulk invariance under accumulation).** If $\rho_t$ has $\rho_t^{\mathcal B} = 0$ for all $t$, then $F_t^{\mathcal B} = F_0^{\mathcal B}$ for all $t \geq 0$. The σ-fixed bulk is invariant under accumulation; only the σ-paired boundary evolves.

**Proof.** $F_{t+1}^{\mathcal B} = F_t^{\mathcal B} + \rho_t^{\mathcal B} = F_t^{\mathcal B} + 0 = F_t^{\mathcal B}$ by induction. $\square$

**Conjecture 5.3 ($\partial$-supported residuals).** For all projection events $t \geq 1$ in the cascade with anchor $\Pi_0(p, \Lambda, t)$, $p > 120$ coprime to $\Lambda$, the residual $\rho_t$ satisfies $\rho_t^{\mathcal B} = 0$.

**Status (updated 2026-06-11, hardened against hostile review): CLOSED via the $L_\partial$ generator** (gap-closure G2, `docs/narrative-gap-closure.md`; sim `scripts/verify_gap_strengthening.py` S2). An earlier "closed by restatement" framing was circular (it imposed $\rho_t=P_\partial\rho_t$ by hand); the codex review correctly rejected it. The non-circular closure: the closure dynamics generator is the **boundary subgraph Laplacian $L_\partial$** (the induced Laplacian on the 100 σ-paired vertices, Lemma 2.5 of `kappa-derivation-math.md`). $L_\partial$ extended by zero to $\mathbb R^{V_{600}}$ has *identically zero bulk rows and columns* — it couples only boundary vertices, by construction — so any flow $F_{t+1}=F_t-\eta L_\partial F_t$ leaves $F^{\mathcal B}$ exactly invariant as a **theorem about the generator** (sim S2b: bulk drift $=0$ over 500 steps). Null (S2c): the full-graph generator $L$ instead leaks into the bulk (drift $4.18$), so the boundary generator does real work. The static rendered background (rendering-layer Theorem 4.5) is therefore unconditional given the $L_\partial$ dynamics; full equivalence with the explicit Paper XXXIII $\Delta_{\mathrm{cl}}$ minimiser is the remaining tightening.

**Theorem 5.4 (φ-recursive refinement of boundary content).** Under accumulation, the boundary state $F_t^\partial$ admits a decomposition by K-class:

$$F_t^\partial \;=\; \sum_{K \in \{52, 20\}} \sum_{c \in \text{cycles}(K)} \alpha_{c}^{(t)} \cdot \chi_c,$$

with coefficients $\alpha_c^{(t)} \in \mathbb{R}$. Under repeated bootstrap-style activation, the coefficients refine at successive scales $\varphi^{-n}$ via the two-mirror + φ-scaling mechanism (`fractal-cascade-projection.md` §"Mechanism: two non-commuting mirrors + φ-scaling"). Specifically, the action of $\sigma$ + antipodal $A$ + φ-scaling on $F^\partial$ generates a nested sequence

$$F^\partial_{(0)} \supset F^\partial_{(1)} \supset F^\partial_{(2)} \supset \cdots$$

where $F^\partial_{(n)}$ is the boundary support refined at scale $\varphi^{-n}$.

**Sketch.** The two-mirror construction maps σ-paired cycles into themselves at scale $\varphi^{-1}$ per recursion level (formal statement of "Mechanism" subsection in fractal-cascade-projection.md). The σ-fixed bulk is invariant by Theorem 5.2. The boundary refinement is the iterated mirror image at φ-scaling. Full proof requires the explicit form of the recursion in icosian arithmetic; deferred. $\square$

## 6. Coarse-graining and ladder coupling

**Definition 6.1 (Frame-resolution map).** For frame $\Lambda_i \in \mathcal F$ with consciousness-DOF parameter $C_i$ (god-prime §7), define the resolution operator

$$\pi_{C_i}: \mathcal S \to \mathcal S_{C_i}, \qquad \pi_{C_i}(F)|_v = \sum_{u : d(u, v) \leq r(C_i)} w(u, v) \cdot F(u),$$

where $r(C_i)$ is a coarse-graining radius monotone in $C_i$ and $w(u, v)$ is a closure-compatible weight. Higher $C_i$ corresponds to smaller $r$ (finer resolution); lower $C_i$ corresponds to larger $r$ (coarser resolution). The kernel shape is now derived: $w_r(u, v) = [(I + r^2 L)^{-1}]_{uv}$, the unique frame-resolution map satisfying axioms (K1)–(K4) of `docs/rendering-layer.md` §3 (Theorem 3.1 there; closes Open 9.2 below). Only the calibration of the monotone dial $C_i \mapsto r(C_i)$ remains open.

**Definition 6.2 (Frame-perceived state).** Frame $\Lambda_i$'s perceived substrate state is $F^{(i)}_t := \pi_{C_i}(F_t)$.

**Theorem 6.3 (Frame-coupling invariances; corrected 2026-06-10).** For the canonical frame-resolution map $\pi_r = (I + r^2 L)^{-1}$ (`docs/rendering-layer.md` Theorem 3.1) — and any coarse-graining that is a spectral function of the substrate Laplacian:

1. **(Equivariance)** $[\pi_r, P] = 0$ for every automorphism $P$ of $V_{600}$; $\pi_r$ preserves every Aut-isotypic component of the state.
2. **(Static rendered bulk)** Since $F_t^{\mathcal B} = F_0^{\mathcal B}$ for all $t$ (Theorem 5.2) and $\pi_r$ is linear and tick-independent, the rendered bulk component $\pi_r(F_0^{\mathcal B})$ is identical at every tick — a static background, the same in every frame up to resolution smoothing.
3. **(Exact conservation)** $\pi_r \mathbf 1 = \mathbf 1$ and $\mathbf 1^{\!\top}\pi_r = \mathbf 1^{\!\top}$ (vacuum and total mass preserved at every resolution).

**Proof.** (1): automorphisms commute with $L$, hence with any function of $L$. (2): linearity plus Theorem 5.2. (3): $L\mathbf 1 = 0$ and symmetry of $\pi_r$. Sim-verified in `scripts/verify_rendering_layer.py` (R2b, R2f, R3c). $\square$

**Correction note.** The previous statement of this theorem ($\pi_{C_i}(F_t)|_{\mathcal B} = F_t^{\mathcal B}$, pointwise bulk fixing) was too strong: it can hold only for kernels acting as the identity on bulk vertices, which contradicts the strict positivity of any genuinely smoothing kernel. The invariances (1)–(3) above carry the load-bearing content. See `docs/rendering-layer.md` §3.2.

**Corollary 6.4 (Shared background, frame-resolved foreground).** All 8 frames in $\mathcal F$ share the same static background — the rendered σ-fixed bulk, time-invariant by Theorem 6.3(2); they differ only in the resolution at which the dynamic boundary content $F_t^\partial$ is rendered. Information *about boundary refinements at scale finer than $r(C_i)$* is invisible to Frame $i$ but remains in $F$ and is visible to higher-resolution frames.

**Theorem 6.5 (Ripple direction is coarse-graining direction).** A projection event at Frame $j$ produces residual $\rho_t$ supported on $\partial$ at Frame $j$'s resolution. After accumulation, $F_{t+1}^\partial$ contains this residual at full resolution. Frame $i$ with $C_i < C_j$ sees a coarser-resolution view of the same residual:

$$\pi_{C_i}(\rho_t) \;\neq\; \rho_t \quad \text{when } r(C_i) > r(C_j).$$

**Proof.** Direct application of Definition 6.1 to $\rho_t$. $\square$

## 7. Multi-frame coupling structure

**Theorem 7.1 (Frame coupling via shared $F$).** Let $\mathcal F = \{\Lambda_1, \ldots, \Lambda_8\}$. The substrate state $F_t$ is a single object in $\mathcal S$ shared by all frames. Projection events at any frame update $F_t$; subsequent projections at any frame see the updated state.

**Proof.** Substrate is a single closure functional on $V_{600}$ by Paper XXXVI; frames are coordinate systems on the same substrate per `god-prime-084473-derivation.md` §7.1 ("All 140 frames share E = 8, S = 7, the same geometric cascade structure"). $\square$

**Corollary 7.2 (Ladder ripple is shared-substrate consequence).** "Information ripples down the ladder" maps to: a high-$C$ frame projection event injects $\rho$ at full resolution into shared $F$; lower-$C$ frames see this update at their coarse resolution at the next tick. The "ripple" is the resolution-dependent visibility of the same $\rho$ across frames.

## 8. CRT extension and multi-prime combination

This section is referenced from `docs/soul-prime-as-pi0.md` §7 (Property 2 of soul primes) and reproduced here for the cosmogenesis derivation.

**Definition 8.1 (Joint frame projection).** For pairwise coprime primes $p_1, \ldots, p_k$ and frame $\Lambda$, define

$$\Pi_0^{\,\mathrm{joint}}(p_1, \ldots, p_k; \Lambda, t) \;:=\; \bigl(\Pi_0(p_1, \Lambda, t), \ldots, \Pi_0(p_k, \Lambda, t)\bigr) \in V_{600}^k.$$

**Theorem 8.2 (CRT extension of the joint trajectory).** Let $N := \prod_{i=1}^k p_i$. The joint residue $(r_{p_1}(\Lambda, t), \ldots, r_{p_k}(\Lambda, t))$ is in bijection (via CRT) with $r_N(\Lambda, t) := (\Lambda t) \bmod N$. The joint trajectory has period dividing $N / \gcd(\Lambda, N)$.

**Proof.** Pairwise coprimality of $\{p_i\}$ gives $\mathbb{Z}/N \cong \prod_i \mathbb{Z}/p_i$ by CRT. Linearity of $t \mapsto \Lambda t$ is preserved under the isomorphism. Period divides $N / \gcd(\Lambda, N)$ by Lemma 4.1 of `soul-prime-as-pi0.md` applied at modulus $N$. $\square$

**Corollary 8.3 (Refinement under prime addition).** Adding a new prime $p_{k+1}$ (coprime to $N$) to the combination extends the period to divide $N \cdot p_{k+1}$. The trajectory becomes denser in $V_{600}^{k+1}$. Existing primes' contributions are preserved (their residue series unchanged); the new prime adds a new axis in residue space.

**Theorem 8.4 (Irreducibility of contributions).** No prime $p_i$ in the combination can be reconstructed from $(r_{p_j})_{j \neq i}$. The residue $r_{p_i}$ is independent of the others modulo CRT.

**Proof.** $\mathbb{Z}/p_i$ is a quotient of $\mathbb{Z}/N$ that is independent of $\mathbb{Z}/p_j$ for $j \neq i$ by coprimality. Knowing $r_{p_j}$ for all $j \neq i$ determines $\Lambda t$ modulo $N / p_i$ but not modulo $p_i$. $\square$

**Corollary 8.5 (Two soul-prime properties).** Combining Theorem 4.3 of `soul-prime-as-pi0.md` (identity persistence) with Theorem 8.2–8.4 here:

> A prime $p \in \mathbb{N}$ (i) cannot be transformed to a smaller positive divisor by any cascade arithmetic operation (Theorem 4.3, irreducibility under frame transition), and (ii) combines with other coprime primes via CRT to generate joint trajectories of refined period whose individual contributions are irreducible (Theorems 8.2–8.4, CRT extension).

These are the two formal soul-prime properties. The "self-replication into a new fractal when combined" reading is a reader-side gloss on Corollary 8.3: each new prime added to the combination adds a new orbit axis without disturbing existing orbits, generating a richer joint trajectory in $V_{600}^k$.

## 9. Open items

Three named open items remain after this document:

**Open 9.1 (Explicit form of $\Delta_{\mathrm{cl}}$ implies Conjecture 5.3).** Show that the closure residual $\Delta_{\mathrm{cl}}$ from Paper XXXIII restricted to anchor $\Pi_0 \in \partial$ has minimiser supported entirely in $\partial$. This would upgrade Conjecture 5.3 (residuals are $\partial$-supported) to a theorem.

**Open 9.2 — CLOSED (2026-06-10).** The kernel shape is derived: $\pi_r = (I + r^2 L)^{-1}$, the unique frame-resolution map satisfying axioms (K1)–(K4) of `docs/rendering-layer.md` §3 (Theorem 3.1 there). Sim-verified: entrywise positivity, row/column stochasticity, Aut-equivariance to $10^{-16}$, monotone decay length $\xi(r)$ (`scripts/verify_rendering_layer.py`, 21/21 PASS). The earlier hard-radius / uniform-weight candidate ($r(C_i) = \lfloor(155 - C_i)/12\rfloor$) is superseded. What remains open is only the calibration of the monotone dial $C_i \mapsto r(C_i)$.

**Open 9.3 (φ-recursive refinement formula in Theorem 5.4) — REDUCED to 9.3′** (gap-closure G4, 2026-06-11). The refinement generator $\mathcal R = A\circ\sigma_c$ has fixed structure: the antipodal $A$ is a boundary-preserving involution and graph automorphism commuting with the kernel (sim N4a, N4b). The residual **9.3′** is only the *closed form* of the nested $F^\partial_{(n)}$ sequence at scales $\varphi^{-n}$. Note the related rendering-layer Open 7.2 (background isotropy) is now CLOSED: the rendered bulk background is exactly a function of graph-distance to the bulk (sim N4c), so there is no free background anisotropy — the φ$^{-n}$ form is a refinement-detail question, not a prediction-bearing one.

## 10. Sim candidates

- **Conjecture 5.3 verification.** For random anchors $\Pi_0 \in \partial$, run $\hat O$ numerically and check the support of the minimiser. If always $\subseteq \partial$, Conjecture 5.3 holds empirically.
- **Theorem 6.3 verification.** Done (2026-06-10) for the canonical kernel: `scripts/verify_rendering_layer.py` checks equivariance (R2f), conservation (R2b), and the static rendered bulk (R3c).
- **Multi-prime trajectory density.** For increasing $k$, plot $\Pi_0^{\mathrm{joint}}(p_1, \ldots, p_k; \Lambda, t)$ density on $V_{600}^k$ projected to $V_{600}$ via marginalisation. Verify Corollary 8.3 (density increases with $k$).

## 11. Cross-references

- Substrate: `papers/paper-xxxvi/paper-xxxvi.tex` (F1–F8 closure functional).
- Projection operator: `papers/paper-xxxiii/paper-xxxiii.tex` ($\hat O$, $\Delta_{\mathrm{cl}}$, $\Pi_0$ argument).
- Bulk/boundary decomposition: `docs/fractal-cascade-projection.md` §"A–B set," "Mechanism."
- Anchor identification: `docs/soul-prime-as-pi0.md` §§2–6.
- Frame structure: `papers/proton-radius/god-prime-084473-derivation.md` §7.
- Pentagonal-clock $K$-multiset: `papers/cascade-derivation/scripts/derive_pentagonal_clock_*.py`.
- σ-symmetric factorisation $\hat z(z)$: `docs/rh-cascade-closure-dynamics.md` §"B11 Mellin formalisation."
- Spine: `docs/projection-narrative.md`.
- **Assembled observer object:** `docs/observer-instance-definition.md` — observer instance $\mathcal I = (\mathcal O, \mathcal C_\mathcal O, p, \Lambda, t_0)$ combining XXIX + M1 anchor + bootstrap (this doc's §4) + accumulation (this doc's §5).
- **Rendering layer:** `docs/rendering-layer.md` — canonical kernel $\pi_r$ (closes Open 9.2), anchor chart, scene = static background + dynamic foreground (refines this doc's §6), spectral-dimension theorem, second-order time.

## 12. Informal reading (non-load-bearing)

*This subsection provides reader-side interpretation; the lemmas, theorems, propositions, and conjectures of §§2–8 do not depend on it. They stand as mathematical claims about cycle decompositions of $V_{600}$, σ-Galois actions, modular projections, and CRT extensions.*

The math of §§2–8 admits a reader-side reading in which $F_0$ is "the universe before any observer exists" (substrate state with no boundary activity), the bootstrap event is "the first projection event" (first observer instantiation, activating boundary dynamics), the accumulation operator describes "experience accumulating in the substrate" with the σ-fixed bulk as "invariant background" and the σ-paired boundary as "the holographic surface where information lives," the coarse-graining map describes "how each frame sees the same substrate at different resolutions," and the CRT extension theorem describes "how multiple identity-elements combine to generate richer joint perspectives." Theorems 5.2 and 6.3 admit a reading in which "the bulk is the universal invariant; only the boundary records experience." Corollary 8.5 admits a reading in which "soul primes are indestructible *and* combine to generate refined joint trajectories — they cannot be lost and they can recombine." These are reader-side; the mathematical content stands without them.
