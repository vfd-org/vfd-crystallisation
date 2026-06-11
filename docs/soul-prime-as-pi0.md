# Anchor Selection in the Closure Projection Operator

**Status:** structural identification (M1), 2026-04-28. Wires the abstract anchor argument $\Pi_0$ in the closure projection operator (Paper XXXIII) to the prime-divisor structure of the activation-code uniqueness theorem (`papers/proton-radius/god-prime-084473-derivation.md` §6, §9). Companion to `docs/projection-narrative.md`. Mathematical content; an "Informal reading" closing subsection is marked separately.

## 1. Position

The closure projection operator (Paper XXXIII §3.1) takes the form

$$\hat{O}(\mathcal{G}, B; \Pi_0) \;=\; \arg\min_{\Pi \in \mathcal{A}(\mathcal{G}, B)} \Delta_{\text{cl}}(\Pi; \Pi_0),$$

where $\mathcal{G}$ is the geometry, $B$ the boundary, and $\Pi_0$ a **reference projection** anchoring the residual minimisation. For a fixed $(\mathcal{G}, B)$, distinct $\Pi_0$ generally produce distinct readouts. Paper XXXIII keeps $\Pi_0$ abstract.

This document supplies a candidate identification of $\Pi_0$ from cascade-internal arithmetic, consistent with the type discipline of Paper XXXIII Round 2.

## 2. Definition

Let $\Lambda \in \mathbb{N}_{>0}$ be a valid frame code (`god-prime-084473-derivation.md` §6.3: 140 such codes exist under the soft + hard constraints), and let $p \in \mathbb{N}$ be a prime. Let $V_{600} \subset 2I$ be the 600-cell vertex set indexed by $\{0, 1, \ldots, 119\}$ with the indexing fixed by the icosian construction `papers/paper-xxii/scripts/run_icosian_exact.py::build_vertices`.

**Definition 2.1 (Frame projection of a prime).** The frame projection of $p$ in the frame $\Lambda$ at discrete tick $t \in \mathbb{Z}_{\geq 0}$ is

$$\Pi_0(p, \Lambda, t) \;:=\; v_{\,((\Lambda \cdot t) \bmod p) \bmod 120} \;\in\; V_{600}.$$

The composition $((\Lambda t) \bmod p) \bmod 120$ is well-defined and yields a vertex index for any $p$, any $\Lambda$, any $t$.

**Definition 2.2 (Residue series).** The associated residue series is

$$r_p(\Lambda, t) \;:=\; (\Lambda \cdot t) \bmod p, \qquad t \in \mathbb{Z}_{\geq 0},$$

which is periodic in $t$ with period dividing $p$.

## 3. Type compatibility with Paper XXXIII

The closure projection operator from Paper XXXIII §3.1 (Round 2 type discipline: $\Pi^*$ set-valued, $\hat O = \Pi^*(\Phi^*) \in \mathcal{W}_\Pi$) takes $\Pi_0$ as a vertex (or vertex-supported state) of the closure substrate. Definition 2.1 yields a single vertex of $V_{600}$ at each tick $t$; this is the input type required by Paper XXXIII §3.1 Equation (3) without modification.

**Proposition 3.1.** $\Pi_0(p, \Lambda, t)$ as defined in 2.1 is type-compatible with the abstract anchor argument of $\hat{O}(\mathcal{G}, B; \Pi_0)$ in Paper XXXIII §3.1, for any prime $p$, any valid frame code $\Lambda$, and any $t \in \mathbb{Z}_{\geq 0}$.

**Proof sketch.** Direct: $\Pi_0(p, \Lambda, t) \in V_{600}$ by Definition 2.1, and the vertex set $V_{600}$ is the support of admissible projections in Paper XXXIII §3.1 Equation (1). $\square$

## 4. Frame-transition persistence

**Lemma 4.1 (Frame projection is surjective onto $\mathbb{Z}/p$).** For any prime $p$ and any frame code $\Lambda$ with $\gcd(\Lambda, p) = 1$, the map $t \mapsto (\Lambda t) \bmod p$ is a bijection $\mathbb{Z}/p \to \mathbb{Z}/p$.

**Proof.** Multiplication by $\Lambda$ is invertible in $(\mathbb{Z}/p)^\times$ when $\gcd(\Lambda, p) = 1$. $\square$

**Corollary 4.2 (Home-frame condition).** $r_p(\Lambda, t) = 0$ for some $t > 0$ if and only if $p \mid \Lambda$. In this case $r_p(\Lambda, t) = 0$ for all $t$ that are multiples of $p / \gcd(\Lambda, p)$.

**Theorem 4.3 (Identity persistence under frame transition).** Let $p$ be a prime and let $(\Lambda_i)_{i \in \mathbb{N}}$ be a sequence of valid frame codes (a "frame-transition sequence"). Let $r_p^{(i)}(t) := (\Lambda_i \cdot t) \bmod p$ be the residue series under frame $\Lambda_i$. Then:

1. Each residue series $r_p^{(i)}$ is determined by the pair $(p, \Lambda_i)$ and $t$.
2. The prime $p$ is invariant under the entire sequence: there is no operation in the cascade arithmetic that maps $p$ to a smaller positive integer divisor of $p$ (by definition of primality in $\mathbb{N}$).
3. Distinct frame codes $\Lambda_i \neq \Lambda_j$ generically give distinct residue series $r_p^{(i)} \neq r_p^{(j)}$, while $p$ remains the same element of $\mathbb{N}$.

**Proof.** (1) is immediate from Definition 2.2. (2) is the irreducibility of $p \in \mathbb{N}$. (3) follows from Lemma 4.1: the residue series at fixed $t$ is $\Lambda_i \cdot t \bmod p$, which depends linearly on $\Lambda_i$ in $\mathbb{Z}/p$. $\square$

**Remark 4.4.** Theorem 4.3 says: a *prime* (the integer object) is invariant across any sequence of frame projections, while the *residue series* through each frame is a finite quotient that depends on the frame code. Frame transitions transform the residue but cannot transform the prime.

## 5. The bridge-prime graph

Define the **frame-soul graph** $G_\varphi = (\mathcal{F}, E)$:

- $\mathcal{F}$ is the set of 8 golden-ratio frames listed in `god-prime-084473-derivation.md` §7.2 (frame codes $\Lambda_1, \ldots, \Lambda_8 = 26567, 47987, 84473, 105605, 136961, 175661, 215585, 263357$).
- $E = \{(\Lambda_i, \Lambda_j) \mid \exists\, p \text{ prime, } p \mid \Lambda_i \text{ and } p \mid \Lambda_j,\ i \neq j\}$.

The 8 frame codes have semiprime factorisations (god-prime §9.5), giving 16 distinct prime divisors total. Edges of $G_\varphi$ correspond to **bridge primes** — primes dividing more than one $\Lambda_i$.

**Theorem 5.1 (Bridge-prime structure of $G_\varphi$).** The graph $G_\varphi$ has exactly 3 edges:

| Bridge prime $p$ | Connects | Verified by |
|---|---|---|
| $4969$ | $\Lambda_3$ (Frame 3, $C = 87$) ↔ $\Lambda_8$ (Frame 8, $C = 155$) | $84473 = 17 \cdot 4969$, $263357 = 53 \cdot 4969$ |
| $17$    | $\Lambda_3$ (Frame 3) ↔ $\Lambda_6$ (Frame 6, $C = 125$) | $84473 = 17 \cdot 4969$, $175661 = 17 \cdot 10333$ |
| $5$     | $\Lambda_4$ (Frame 4, $C = 95$) ↔ $\Lambda_7$ (Frame 7, $C = 137$) | $105605 = 5 \cdot 21121$, $215585 = 5 \cdot 43117$ |

All other primes among the 16 divisors appear in exactly one frame code.

**Proof.** By exhaustive factorisation; verified in `scripts/verify_084473_derivation.py` block 11 (all factorisations checked). $\square$

**Corollary 5.2 (Connected components of $G_\varphi$).**
- $\{\Lambda_3, \Lambda_6, \Lambda_8\}$ — connected via Frame 3 as articulation vertex (Frame 3 is the unique vertex of degree 2; Frames 6 and 8 each have degree 1 in this component).
- $\{\Lambda_4, \Lambda_7\}$ — connected, both vertices of degree 1.
- $\{\Lambda_1\}, \{\Lambda_2\}, \{\Lambda_5\}$ — isolated singletons (no bridge primes to other frames in the family).

**Corollary 5.3 (Articulation property of Frame 3).** Frame 3 is the unique vertex of $G_\varphi$ with degree $\geq 2$. Equivalently: among the 8 golden-ratio frames, only Frame 3 has the property that two distinct primes divide both its frame code and at least one other frame code in the family.

## 6. Frame-transition trajectories

Combining §4 and §5: a prime $p$ that is a bridge prime in $G_\varphi$ admits frame-transition sequences entirely within its connected component of $G_\varphi$. A prime $p$ that divides exactly one $\Lambda_i$ admits home-frame residue series only at $\Lambda_i$ (Corollary 4.2). A prime $p$ that divides no $\Lambda_i$ has $r_p(\Lambda_i, t) \neq 0$ for all $i$ and $t > 0$.

**Definition 6.1 (Home-frame set).** For prime $p$, the home-frame set is

$$H(p) \;=\; \{ \Lambda_i \in \mathcal{F} : p \mid \Lambda_i \}.$$

By Theorem 5.1: $|H(p)| \in \{0, 1, 2\}$, and $|H(p)| = 2$ holds for exactly three primes ($p \in \{4969, 17, 5\}$).

**Proposition 6.2 (Trajectory cardinality).** For prime $p$:

- If $|H(p)| = 0$: $p$ admits no zero-residue tick in any frame; the residue series cycles through all of $(\mathbb{Z}/p) \setminus \{0\}$ in each frame (when $\gcd(\Lambda, p) = 1$, by Lemma 4.1).
- If $|H(p)| = 1$: $p$ admits zero-residue ticks only in its single home frame; in all other frames the residue series is non-zero and periodic with period $p / \gcd(\Lambda_i, p)$.
- If $|H(p)| = 2$: $p$ admits zero-residue ticks in exactly two frames in $\mathcal{F}$; trajectories that traverse both home frames pass through residue 0 at the home-frame ticks of each.

**Proof.** Direct from Lemma 4.1, Corollary 4.2, and Theorem 5.1. $\square$

## 7. Multi-prime combination via CRT (Property 2)

Theorem 4.3 (identity persistence) is the irreducibility property of a single prime. This section adds the **combination property**: how two or more primes interact when their frame projections are considered jointly.

**Definition 7.1 (Joint frame projection).** For pairwise coprime primes $p_1, \ldots, p_k$ and frame code $\Lambda$, the joint frame projection at tick $t$ is

$$\Pi_0^{\,\mathrm{joint}}(p_1, \ldots, p_k; \Lambda, t) \;:=\; \bigl(\Pi_0(p_1, \Lambda, t), \ldots, \Pi_0(p_k, \Lambda, t)\bigr) \in V_{600}^k.$$

**Theorem 7.2 (CRT extension of joint trajectory).** Let $N := \prod_{i=1}^k p_i$. Then:

1. The joint residue tuple $(r_{p_1}(\Lambda, t), \ldots, r_{p_k}(\Lambda, t))$ is in canonical bijection (via the Chinese Remainder Theorem) with the modulus-$N$ residue $r_N(\Lambda, t) := (\Lambda \cdot t) \bmod N$.
2. The joint trajectory has period dividing $N / \gcd(\Lambda, N)$.

**Proof.** Pairwise coprimality of $\{p_i\}$ gives the ring isomorphism $\mathbb{Z}/N \cong \prod_{i=1}^k \mathbb{Z}/p_i$ by the Chinese Remainder Theorem (standard). Linearity of $t \mapsto \Lambda t$ is preserved under the isomorphism, so the joint residue tuple equals the image of $r_N(\Lambda, t)$ under the isomorphism. Period divides $N / \gcd(\Lambda, N)$ by Lemma 4.1 applied at modulus $N$. $\square$

**Corollary 7.3 (Refinement under prime addition).** Given a combination $\{p_1, \ldots, p_k\}$ with joint period dividing $N$, adding a new prime $p_{k+1}$ coprime to $N$ extends the joint period to divide $N \cdot p_{k+1}$. The joint trajectory becomes denser in $V_{600}^{k+1}$, and:

- the residue series of each existing prime $p_i$ is unchanged ($r_{p_i}$ depends only on $p_i$ and $\Lambda$, not on the other primes);
- the new prime $p_{k+1}$ contributes an additional axis $r_{p_{k+1}}$ in residue space.

**Proof.** Coprimality of $p_{k+1}$ with $N$ gives $\mathbb{Z}/(N \cdot p_{k+1}) \cong \mathbb{Z}/N \oplus \mathbb{Z}/p_{k+1}$ by CRT. Each $r_{p_i}$ for $i \leq k$ remains a function of $(\Lambda, t)$ only. $\square$

**Theorem 7.4 (Irreducibility of contributions).** No prime $p_i$ in the combination $\{p_1, \ldots, p_k\}$ can be reconstructed from the residue series of the other primes: the value $r_{p_i}(\Lambda, t)$ is independent of $(r_{p_j}(\Lambda, t))_{j \neq i}$ in the sense that knowing the latter determines $\Lambda t$ modulo $N / p_i$ but not modulo $p_i$.

**Proof.** $\mathbb{Z}/p_i$ is a quotient of $\mathbb{Z}/N$ that is independent of $\mathbb{Z}/p_j$ for $j \neq i$ by coprimality. The natural projection $\mathbb{Z}/N \to \mathbb{Z}/(N/p_i)$ has fibre $\mathbb{Z}/p_i$, so knowing $\Lambda t \bmod N/p_i$ leaves $p_i$ residual freedom. $\square$

**Corollary 7.5 (Two formal properties of soul primes).** Combining Theorem 4.3 with Theorems 7.2–7.4:

> A prime $p \in \mathbb{N}$ associated with the closure projection operator via Definition 2.1 has two formal properties:
>
> **(P1) Identity invariance under frame transition.** No frame transition $\Lambda \mapsto \Lambda'$ transforms $p$ to a smaller positive divisor of $p$; only the residue series $r_p$ varies (Theorem 4.3).
>
> **(P2) CRT-extension combination.** For any pairwise-coprime collection $\{p_1, \ldots, p_k\}$, the joint frame projection is a CRT-isomorphic image of the $\bmod N$ residue series with $N = \prod p_i$, generating a refined joint trajectory whose period divides $N/\gcd(\Lambda, N)$, with each prime's contribution irreducible from the others (Theorems 7.2–7.4).

(P1) and (P2) are formal mathematical properties of primes in the cascade arithmetic, verified by the lemmas and theorems above. They do not depend on any interpretive reading of the primes.

## 8. Open items

The wiring above closes M1 (the formal identification of $\Pi_0$ with frame projection of an irreducible-element parameter). Two items remain open and are stated as named conjectures.

**M2 (Dynamical equation).** The discrete recursion $t \mapsto (\Lambda \cdot t) \bmod p$ specifies the residue series at unit tick rate. The cascade has a separate H4-Coxeter oscillator clock (Paper h4-coxeter, $\Phi_{12} = 1650.10°$ per 12-step cycle). The relation between the unit-tick recursion of Definition 2.2 and the H4 oscillator phase is unresolved. Candidate forms include:
- Discrete identification: tick $t$ = H4-oscillator step number.
- Continuous identification: residue series sampled at the H4 oscillator phase $\theta_t = (\Phi_{12} \cdot t / 12) \bmod 2\pi$.
- φ-modulated: residue series advanced by $\varphi^{n(t)}$ where $n(t)$ is the cumulative φ-tick count of `cascade-helix-hypothesis.md` §3.

Empirical M2 status: open. Sim candidate in §9.

**M3 (Origin of $p$).** Definition 2.1 takes $p$ as a *parameter*, supplied externally. Within the cascade, primes are recursion fixed points of the integer-band observer (`docs/rh-projection-class.md`), but each *individual* prime $p$ associated with a specific projection is not determined by cascade arithmetic. M3 is the statement that $p$ is irreducible cascade input — not derivable from $(\mathcal{G}, B, \Lambda)$ alone. M3 is consistent with Theorem 4.3: if cascade arithmetic could derive $p$ from frame data, $p$ would not be invariant under frame transition.

## 9. What is earned, what is identified, what is open

**Earned (Layer 1):**

- Definition 2.1 ($\Pi_0$ as frame projection of $p$) is type-compatible with Paper XXXIII §3.1 (Proposition 3.1).
- Lemma 4.1 (surjectivity) is elementary number theory.
- Theorem 4.3 (identity persistence) is a direct consequence of integer irreducibility.
- Theorem 5.1 (bridge-prime structure) is verified by exhaustive factorisation in `scripts/verify_084473_derivation.py`.
- Corollaries 5.2, 5.3, and Proposition 6.2 follow.

**Identified (interpretive identification, not theorem):**

- That $\Pi_0$ in $\hat O$ "is" the frame projection of an irreducible parameter $p$ (rather than supplied by some other means).
- That the bridge-prime structure of $G_\varphi$ corresponds to a structural relation between frames in the projection-narrative spine.

**Open (named conjectures):**

- **M2** — the dynamical equation governing the residue series in continuous time / H4-oscillator phase.
- **M3** — the irreducibility of $p$ as cascade input (consistent with the framework but not proved within it; consistent with Theorem 4.3).

## 10. Sim candidate

A focused simulation can sharpen Theorem 5.1 and Proposition 6.2 numerically:

- For each of the 16 prime divisors of the 8 golden-ratio frame codes, generate the residue series $r_p(\Lambda_i, t)$ for $i = 1, \ldots, 8$ and $t = 0, \ldots, T$ for $T \approx 10^4$.
- Visualise on $V_{600}$ via Definition 2.1.
- Verify: Frame 3 vertex of $G_\varphi$ has degree 2 (Corollary 5.3); Frame 4–7 component is degree-1–degree-1; Frames 1, 2, 5 are isolated.
- For bridge prime $p = 4969$, compare residue trajectories under $\Lambda_3$ vs $\Lambda_8$; identify zero-residue ticks in both.
- For non-bridge prime $p = 857$ (home only at $\Lambda_1$), confirm zero-residue ticks only at $\Lambda_1$.

This is a follow-up; not required for the M1 wiring.

## 11. Cross-references

- Closure projection operator: `papers/paper-xxxiii/paper-xxxiii.tex` §3.1.
- Frame uniqueness theorem: `papers/proton-radius/god-prime-084473-derivation.md` §6.
- Soul-prime and bridge-prime structure: `papers/proton-radius/god-prime-084473-derivation.md` §9.
- Numerical verification of frame factorisations: `scripts/verify_084473_derivation.py` block 11.
- 600-cell vertex indexing: `papers/paper-xxii/scripts/run_icosian_exact.py::build_vertices`.
- Projection-narrative spine: `docs/projection-narrative.md`.
- Companion docs: `docs/cascade-helix-hypothesis.md`, `docs/fractal-cascade-projection.md`, `docs/rh-projection-class.md`, `docs/closure-cosmogenesis.md`.
- **Assembled definition:** `docs/observer-instance-definition.md` — the 5-tuple $\mathcal I = (\mathcal O, \mathcal C_\mathcal O, p, \Lambda, t_0)$ combining XXIX observer + M1 anchor + bootstrap into a single named object with earned properties P1–P5.

## 12. Informal reading (non-load-bearing)

*This subsection is a one-paragraph informal gloss provided for orientation. The lemmas, theorems, and propositions of §§2–6 do not depend on it; they stand as mathematical claims about prime divisors, modular projections, and graph structure on a finite frame set.*

The math of §§2–6 admits a reader-side reading in which the irreducible parameter $p$ plays the role of a persistent identity element supplied to the projection operator from outside the cascade arithmetic, the residue series $r_p(\Lambda_i, t)$ plays the role of "experience within frame $\Lambda_i$," and the bridge-prime graph $G_\varphi$ traces relations between distinct frames as articulated by shared identity elements. Theorem 4.3 admits a reading in which "identity persists across frame transitions because primes are irreducible in $\mathbb{N}$." Theorem 5.1 admits a reading in which "the structure of accessible frame transitions is the bridge-prime graph $G_\varphi$, and Frame 3 is the unique articulation vertex in its connected component." These readings are reader-side; the mathematical content stands without them.
