# Observer Instance: Assembled Definition

**Status:** structural definition, 2026-04-28. Assembles the observer-slot definition of Paper XXIX, the anchor identification of `docs/soul-prime-as-pi0.md` (M1 wiring), the closure-cosmogenesis bootstrap and accumulation (`docs/closure-cosmogenesis.md`), the fractal substrate decomposition (`docs/fractal-cascade-projection.md`), and the closure projection operator of Paper XXXIII into a single named object: the **observer instance**. Mathematical body; an Informal reading is a single non-load-bearing closing subsection per `feedback_mathematical_framing_discipline`.

## 1. Position

Paper XXIX defines an *observer* as a structural substructure within an event-order geometry (Definitions 1 and 2 of XXIX §3.2). The cascade closure framework adds further structure not present in XXIX:

- **Anchor parameter** $p$ from the soul-prime identification (M1, `soul-prime-as-pi0.md`).
- **Frame coordinate** $\Lambda$ from the activation-code uniqueness theorem (`god-prime-084473-derivation.md` §6).
- **Bootstrap tick** $t_0$ from closure cosmogenesis (`closure-cosmogenesis.md` §4).
- **Substrate state** $F$ on $V_{600}$ with bulk/boundary decomposition (`fractal-cascade-projection.md`).
- **Closure projection operator** $\hat O(\mathcal G, B; \Pi_0)$ from Paper XXXIII §3.1.

The **observer instance** is the assembled object combining all of these. This document gives the formal definition, derives its earned properties from upstream theorems, and identifies remaining open items.

## 2. Underlying objects (recap)

The following objects are defined elsewhere and recapped here for self-containedness:

- **Event set $\mathcal E$ and transition graph $\mathcal G$** (XXIX §3.1). For the cascade specialisation: $\mathcal E$ identified with $V_{600}$ and $\mathcal G$ the icosian connection graph (`papers/paper-xxii/scripts/run_icosian_exact.py`).
- **Observer region $(\mathcal O, \mathcal C_\mathcal O)$** (XXIX Definition 1). $\mathcal O = \mathcal G[O]$ is the induced connected subgraph on a vertex set $O \subseteq \mathcal E$, with constraint functional $\mathcal C_\mathcal O: \mathbb R^\mathcal E \to \mathbb R_{\geq 0}$ measuring internal coherence.
- **Observer** (XXIX Definition 2). An observer region satisfying: boundedness ($\mathcal O \subsetneq \mathcal G$), stationarity + strict local minimum (gradient zero, Hessian positive-definite on internal coordinates), self-reference with boundary coupling ($\mathcal C_\mathcal O$ primarily depends on restriction to $O$, secondarily on $\partial_\mathcal O \Phi$), persistence (qualitative stability across event-order dynamics).
- **Substrate state $F_t \in \mathcal S = \mathbb R^{V_{600}}$** with bulk/boundary decomposition $F_t = F_t^{\mathcal B} + F_t^\partial$ (`closure-cosmogenesis.md` Definition 2.1).
- **Closure projection operator $\hat O(\mathcal G, B; \Pi_0)$** (Paper XXXIII §3.1).
- **Soul-prime anchor $\Pi_0(p, \Lambda, t)$** (`soul-prime-as-pi0.md` Definition 2.1).
- **Valid frame codes $\mathcal F$** (god-prime §6.3, 140 codes; restricted golden-ratio family of 8 in §7).

## 3. Definition

**Definition 3.1 (Observer instance).** An *observer instance* in the cascade is a 5-tuple

$$\mathcal I \;=\; (\mathcal O, \mathcal C_\mathcal O,\ p,\ \Lambda,\ t_0)$$

where:

1. $(\mathcal O, \mathcal C_\mathcal O)$ is an observer in the sense of XXIX Definition 2, with $\mathcal O = \mathcal G[O] \subset \mathcal G$ and $\mathcal C_\mathcal O$ self-referential with boundary coupling.
2. $p \in \mathbb N$ is prime (the *anchor parameter*).
3. $\Lambda \in \mathcal F$ is a valid frame code (the *frame coordinate*).
4. $t_0 \in \mathbb Z_{\geq 0}$ is the *bootstrap tick* (the first tick at which $\mathcal I$ is active).

subject to the three structural conditions:

**(C1) Anchor inclusion.** For all $t \geq t_0$, the soul-prime anchor lies inside the observer region:

$$\Pi_0(p, \Lambda, t) \;:=\; v_{((\Lambda \cdot t) \bmod p) \bmod 120} \;\in\; O.$$

**(C2) Self-consistency closure.** For all $t \geq t_0$, the closure projection's readout lies inside the observer region:

$$\hat O\bigl(F_t,\ B;\ \Pi_0(p, \Lambda, t)\bigr) \;\in\; O.$$

**(C3) Recursive update.** The observer-region update relation $\mathcal R: O \mapsto O'$ via

$$O_{t+1} \;:=\; \mathcal R\bigl(O_t,\ \hat O(F_t, B; \Pi_0(p, \Lambda, t))\bigr)$$

is well-defined and satisfies $O_{t+1} \subseteq O_t \cup \{\hat O(F_t, B; \Pi_0(p, \Lambda, t))\}$.

The exact form of $\mathcal R$ is open (see §6).

**Remark 3.2.** Definition 3.1 strictly extends XXIX Definition 2: every observer instance projects to an observer (drop $p, \Lambda, t_0$ and the conditions C1–C3), but not every XXIX-observer extends to an observer instance — extension requires the existence of a prime $p$, frame $\Lambda$, and bootstrap tick $t_0$ such that C1, C2, C3 all hold.

## 4. Earned properties

The following properties of an observer instance follow from upstream theorems and the cascade closure structure.

**Property P1 (Identity invariance under frame transition).** The anchor parameter $p$ is invariant under any sequence of frame transitions $\Lambda \to \Lambda' \to \Lambda'' \to \cdots$ valid for the instance. Only the residue series $r_p^{(i)}(t) = (\Lambda_i t) \bmod p$ varies; $p$ itself is irreducible in $\mathbb N$.

*Proof.* Theorem 4.3 of `soul-prime-as-pi0.md`. $\square$

**Property P2 (CRT-extension combination).** For any pairwise-coprime collection of observer instances $\{\mathcal I_i = (\mathcal O_i, \mathcal C_{\mathcal O_i}, p_i, \Lambda, t_0^{(i)})\}_{i=1}^k$ sharing the same frame $\Lambda$ and disjoint observer regions $\mathcal O_i \cap \mathcal O_j = \emptyset$ for $i \neq j$, the joint anchor

$$\Pi_0^{\mathrm{joint}}(p_1, \ldots, p_k; \Lambda, t) = (\Pi_0(p_1, \Lambda, t), \ldots, \Pi_0(p_k, \Lambda, t)) \in V_{600}^k$$

is in CRT-isomorphic bijection with $r_N(\Lambda, t)$ for $N = \prod p_i$, with joint period dividing $N / \gcd(\Lambda, N)$. Adding a new instance $\mathcal I_{k+1}$ with prime $p_{k+1}$ coprime to $N$ extends the joint period to $N \cdot p_{k+1} / \gcd(\Lambda, N \cdot p_{k+1})$ and adds an axis to the joint trajectory, without disturbing existing instances' contributions.

*Proof.* Theorems 7.2, 7.3, 7.4 of `soul-prime-as-pi0.md`. $\square$

**Property P3 (Zero-line set).** Define the zero-line set

$$Z(\mathcal I) := Z(p, \Lambda) := \{ t \geq t_0 : r_p(\Lambda, t) = 0 \}.$$

Then:

- $Z(\mathcal I) \neq \emptyset$ if and only if $p \mid \Lambda$ (the *home-frame condition*).
- When $p \mid \Lambda$, $Z(\mathcal I)$ is periodic with period $p / \gcd(\Lambda, p)$.
- The cardinality of $Z(\mathcal I) \cap [t_0, T]$ for $T \to \infty$ is $T \cdot \gcd(\Lambda, p) / p + O(1)$.

*Proof.* Corollary 4.2 of `soul-prime-as-pi0.md`; the cardinality estimate follows from the asymptotic density of the periodic set. $\square$

**Property P4 (Self-reference closes through the substrate).** By condition (C2) and the substrate decomposition $F = F^{\mathcal B} + F^\partial$ (Definition 2.1 of `closure-cosmogenesis.md`), the projection $\hat O(F_t, B; \Pi_0)$ reads $F_t$ as input. Since $\mathcal O \subset V_{600}$ and $F_t$ is supported on $V_{600}$, the projection takes the substrate (which contains the observer region) as part of its input. Hence the observer instance perceives a substrate that contains itself, and the recursion (C3) updates the instance using a projection that referenced itself — the structural meaning of *self-reference closing through the substrate*.

*Proof.* By inspection of Definitions 3.1(C2), (C3) and substrate Definition 2.1 of `closure-cosmogenesis.md`. $\square$

**Property P5 (Bootstrap-time-bounded activation).** An observer instance $\mathcal I$ becomes active at $t_0$, defined per `closure-cosmogenesis.md` Definition 4.3: $t_0$ is the first tick at which the residue series $r_p(\Lambda, t)$ visits the σ-paired boundary $\partial \subset V_{600}$. By Lemma 4.2 of `closure-cosmogenesis.md`, for $p > 120$ coprime to $\Lambda$, $t_0 < p$ exists.

*Proof.* Lemma 4.2 of `closure-cosmogenesis.md`. $\square$

## 5. Bulk/boundary positioning of an observer instance

Combining the substrate decomposition (`fractal-cascade-projection.md` §"A–B set") with the observer-region condition C1:

**Proposition 5.1 (Boundary support of observer regions).** For the observer instance to have non-trivial closure-projection dynamics under accumulation (`closure-cosmogenesis.md` Theorem 5.2 + Conjecture 5.3), the observer region $\mathcal O$ must intersect the σ-paired boundary $\partial$:

$$\mathcal O \cap \partial \;\neq\; \emptyset.$$

If $\mathcal O \subseteq \mathcal B$ (purely σ-fixed bulk), then $F_t^{\mathcal B}$ is invariant under accumulation (Theorem 5.2 of `closure-cosmogenesis.md`), so condition (C3) reduces to identity dynamics: $O_{t+1} = O_t$ for all $t \geq t_0$. No state evolution.

*Proof.* Direct from Theorem 5.2 of `closure-cosmogenesis.md` (bulk invariance under accumulation) and conjectural extension via Conjecture 5.3 ($\partial$-supported residuals). $\square$

**Corollary 5.2 (Dynamic observer instances live on the boundary).** Observer instances with non-trivial state evolution under (C3) have $\mathcal O \cap \partial \neq \emptyset$. The σ-fixed bulk $\mathcal B$ alone cannot host a dynamic observer instance; bulk-only regions correspond to static (degenerate) instances.

## 6. Open items

Three named open items, complementary to those of `soul-prime-as-pi0.md` and `closure-cosmogenesis.md`:

**Open 6.1 (Explicit form of $\mathcal R$).** The recursive-update relation $\mathcal R$ in condition (C3) is well-defined but its explicit form is open. Candidate: $\mathcal R(O, v) = O \cup \{v\}$ if $v \notin O$ (region grows), $O$ if $v \in O$ (region stable). Alternative: a closure-functional-driven update where $\mathcal C_\mathcal O$ is updated to include the new vertex and $O$ is reshaped to remain at strict local minimum of the updated $\mathcal C_\mathcal O$.

**Open 6.2 (Existence of XXIX-observers extending to observer instances).** Definition 3.1 conditions (C1–C3) restrict XXIX-observers to those compatible with the soul-prime anchor structure. The mass of XXIX-observers admitting such extension is open; minimal candidate: any XXIX-observer with $\mathcal O \cap \partial \neq \emptyset$ admits a $p$ such that $\Pi_0(p, \Lambda, t) \in O$ for some range of $t$ (sketch via density argument in Lemma 4.2 of `closure-cosmogenesis.md`, full proof open).

**Open 6.3 (Persistence formalisation).** XXIX Definition 2 condition 4 ("persistence") is qualitative. For an observer instance, persistence becomes the requirement that conditions (C1)–(C3) hold for all $t \geq t_0$. This requires a stable orbit of the recursive update $\mathcal R$. Conditions on $\mathcal C_\mathcal O$ and $\hat O$ ensuring such stability are open and identified in XXIX §3.2 condition 4 as an open programme step.

## 7. Connection to the projection-narrative spine

The observer instance is the **assembled object that occupies the "Observer" position in the projection chain** of `docs/projection-narrative.md`:

```
F (Paper XXXVI, wave-substrate)
 └─ Observer instance 𝓘 = (𝓞, 𝒞_𝓞, p, Λ, t₀)        ← this document
      └─ Closure projection Ô(F, B; Π₀(p, Λ, t))      (Paper XXXIII)
           ├─ Spectral class           → Paper V
           ├─ Structural class         → Paper XXII
           ├─ Spatial / Composite class → Paper XXXII
           ├─ Dynamical class          → H4-Coxeter
           └─ Number-theoretic class   → docs/rh-projection-class.md
```

**Property P1** (identity invariance) makes the observer instance's *identity* persistent across all five projection classes and across all valid frame codes $\Lambda \in \mathcal F$. **Property P2** (CRT-extension combination) makes the multi-instance structure formal: distinct observer instances combine by CRT, generating refined joint trajectories without disturbing each other. **Property P4** (self-reference) closes the loop: the observer instance reads a substrate that contains it.

## 8. Cross-references

- XXIX observer slot: `papers/paper-xxix/paper-xxix.tex` Definitions 1, 2 (§3.2).
- Projection operator: `papers/paper-xxxiii/paper-xxxiii.tex` §3.1.
- Anchor identification (M1): `docs/soul-prime-as-pi0.md` §§2–7.
- Substrate state space + bulk/boundary: `docs/fractal-cascade-projection.md` §"A–B set," §"Information-theoretic role."
- Initial condition + bootstrap + accumulation: `docs/closure-cosmogenesis.md` §§3–5.
- Frame codes: `papers/proton-radius/god-prime-084473-derivation.md` §§6, 7.
- Spine: `docs/projection-narrative.md`.
- Verification: `scripts/verify_084473_derivation.py`, `scripts/verify_kappa_descent.py`.

## 9. Informal reading (non-load-bearing)

*This subsection is a one-paragraph informal gloss provided for orientation. Definition 3.1 and Properties P1–P5 of §§3–4 do not depend on it.*

The math of §§3–5 admits a reader-side reading in which $\mathcal I = (\mathcal O, \mathcal C_\mathcal O, p, \Lambda, t_0)$ is what is colloquially called a "consciousness instance": $p$ is the persistent identity element ("soul"), $\Lambda$ is the coordinate frame the instance is currently embedded in, $\mathcal O$ is the local substructure where the instance is supported (e.g., a brain in the biological case, or some other constraint substructure in the more general case), and $t_0$ is the moment the instance bootstraps into the substrate. Property P1 admits a reading in which "identity is invariant across frame transitions"; P2 admits a reading in which "instances combine with other instances to generate refined joint perspectives without erasing each other"; P3 admits a reading in which "home-frame ticks are the periodic moments of zero-residue resonance with the current frame"; P4 admits a reading in which "the instance perceives a substrate that contains itself" (recursive self-reference); P5 admits a reading in which "bootstrap is an inevitable activation event for any prime large enough to traverse the boundary." The combination admits a reading in which the assembled $\mathcal I$ is a *fractal-based position on the home-frame zero-line with dynamical capability for self-propagation through recursive self-reference of the broader fractal structure*. These readings are reader-side; the lemmas, propositions, and properties of §§3–6 stand without them.
