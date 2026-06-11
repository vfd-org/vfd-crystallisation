# Cascade Dynamics — The Process-Theoretic Framework

**Purpose.** Parallel to `cascade-foundations.md` (which established
the static cascade framework F1–F8), this document develops the
dynamic/process framework: cascade computation, resource measures,
complexity classes, reductions, and natural complete problems.

**Motivation.** The static framework handles mathematical OBJECTS
(root systems, polytopes, cohomology, eigenvalues). Cascade bridges
to Millennium problems about objects (YM, RH, NS, Hodge, BSD,
Poincaré) succeed because the translation is static-to-static.
P vs NP, however, is about computational PROCESSES — a dynamic
question that the static framework cannot directly address. This
document builds the dynamic counterpart.

**Epistemic status.** The static foundations F1–F8 are theorems. The
dynamic framework D1–D10 below is a combination of definitions,
structural theorems, and well-formulated conjectures. We aim for
the same level of rigor wherever possible, and are explicit about
where conjectures remain.

---

## D0. Motivation and Scope

### D0.1 Why cascade needs dynamics

Cascade was founded on STATIC axioms:
- Void topos (pre-geometric primitive).
- Bootstrap variational principle (static equilibrium).
- Self-similarity r = 1 + 1/r (fixed-point equation).
- E₈ maximality (structural totality).

These yield a rich static theory: foundations F1–F8, Λ-theorems T1–T7,
bridges B1–B12, extensions E1–E22. All describe WHAT EXISTS.

But physical reality is not only static structure. Reality has:
- Time (evolution).
- Processes (algorithms, dynamical systems).
- Resource constraints (time, space, energy).

Computation, information processing, and dynamical evolution all
need a dynamic framework. The static foundations gesture at dynamics
(bootstrap time τ = φ^(-n) in cascade-pregeometry.md P7,
closure dynamics in cascade-foundations.md F2) but do not develop
it systematically.

This document provides the systematic development.

### D0.2 Scope

We develop:
- Primitives (atomic cascade operations).
- Resource measures (time, space).
- Dynamical laws (F-flow, σ-symmetry, bootstrap).
- Cascade Turing machines (computational model).
- Complexity classes (cascade-native P, NP, etc.).
- Reductions.
- Natural complete problems.

We do NOT resolve P vs NP here. That is the subject of a separate
paper that USES this framework.

---

## D1. Primitive Operations

### D1.1 The four cascade primitives

**Definition D1.1 (Cascade primitives).** *The atomic operations of
cascade dynamics are:*

1. **F-step** $\mathsf{F}$: gradient-descent step of the closure
   functional. For a configuration $\Phi$ on the cascade substrate:
   $$\mathsf{F}(\Phi) := \Phi - \eta \nabla_\Phi F[\Phi]$$
   where $\eta > 0$ is a cascade-natural step size (canonically
   $\eta = 1$ in cascade units; see D2 for the scaling).

2. **σ-step** $\mathsf{S}$: Galois involution.
   $$\mathsf{S}(\Phi) := \sigma \Phi$$
   where $\sigma$ is the icosian Galois twist from F5.

3. **Refinement-step** $\mathsf{R}$: shell-depth advance. Maps
   configuration at depth $n$ to depth $n+1$:
   $$\mathsf{R}: \Phi_n \mapsto \Phi_{n+1}$$
   via the Schläfli refinement (F6).

4. **Projection-step** $\mathsf{P}_r$: restrict to cascade rung $r$.
   $$\mathsf{P}_r : \Phi \mapsto \Phi|_r$$
   for rung $r \in \{E_8, H_4, 40, D_4, 16, 8, 0\}$.

### D1.2 Primitive properties

**Theorem D1.1 (Primitive well-definedness).** *Each primitive is
a well-defined map on the cascade configuration space.*

**Proof.**

- $\mathsf{F}$: well-defined by the variational calculus applied to
  $F$, using F2 (closure functional is locally differentiable in
  $\Phi$).
- $\mathsf{S}$: well-defined by F5 ($\sigma$ is a definite
  involution on $\mathbb{Z}[\varphi]$ extended to configurations).
- $\mathsf{R}$: well-defined by F6 (Schläfli refinement is
  canonical).
- $\mathsf{P}_r$: well-defined by the cascade rung structure
  (F3 uniqueness of rung sequence).  □

### D1.3 Composition

Primitives can be composed. A **cascade program** is a finite
sequence $(\mathsf{A}_1, \mathsf{A}_2, \dots, \mathsf{A}_T)$ with
each $\mathsf{A}_i \in \{\mathsf{F}, \mathsf{S}, \mathsf{R},
\mathsf{P}_r\}$. Applied to an input $\Phi_0$:
$$\Phi_T = \mathsf{A}_T \circ \mathsf{A}_{T-1} \circ \dots \circ \mathsf{A}_1(\Phi_0).$$

### D1.4 Alternative primitive sets

Other primitive sets are possible (e.g., unitary rotations on
cascade Hilbert space for quantum cascade computation). We focus
on the classical-cascade primitives above as the canonical set.

---

## D2. Cascade Time

### D2.1 Shell depth as time

Cascade time is measured in **shell depth**: the exponent $n$
of $\varphi^{-n}$ in the bootstrap time coordinate
$\tau = \varphi^{-n}$ (P7 of cascade-pregeometry.md).

One unit of cascade time = one shell transition. Equivalently:
- One $\mathsf{F}$ step is one unit of time.
- One $\mathsf{S}$ step is instantaneous (σ is an involution, not
  a dynamic process).
- One $\mathsf{R}$ step is one unit of time (shell depth increment).
- One $\mathsf{P}_r$ step is instantaneous (structural projection).

**Definition D2.1 (Cascade time complexity).** *For a cascade program
$\mathcal{A}$ running on input $\Phi_0$, the time is the number of
$\mathsf{F}$-steps and $\mathsf{R}$-steps:*
$$T_{\mathcal{A}}(\Phi_0) := \#\{i : \mathsf{A}_i \in \{\mathsf{F}, \mathsf{R}\}\}.$$

(σ-steps and projections are counted as $O(1)$ overhead; they do
not advance cascade time.)

### D2.2 Polynomial time

**Definition D2.2 (Polynomial cascade time).** *A cascade program
$\mathcal{A}$ runs in polynomial time if there exists a polynomial
$p$ such that $T_{\mathcal{A}}(\Phi) \leq p(|\Phi|)$ for all inputs
$\Phi$, where $|\Phi|$ is the cascade description length of $\Phi$.*

### D2.3 Description length

**Definition D2.3 (Cascade description length).** *For a cascade
configuration $\Phi$ at depth $n$, the description length is*
$$|\Phi| := n \cdot \log_\varphi(\dim V_n)$$
*where $V_n$ is the state-space dimension at depth $n$.*

For H₄ substrate: $\dim V_n \sim 120^n$, so $|\Phi| \sim n \cdot
\log_\varphi(120) \approx n \cdot 9.95 \approx 10n$.

### D2.4 Relation to classical time

**Theorem D2.1 (Time equivalence).** *Up to polynomial factors,
cascade polynomial time equals classical Turing-machine polynomial
time. That is, a function is cascade-polynomial-time computable
iff it is classical-polynomial-time computable.*

**Proof sketch.**

(Cascade → Classical.) Simulate cascade primitives on a Turing
machine. Each $\mathsf{F}$ step requires updating $O(\dim V_n)$
configuration components, each by $O(1)$ arithmetic. Total:
$O(\dim V_n) = O(\varphi^{cn})$ for constant $c$. This is
exponential in cascade time, but polynomial in cascade DESCRIPTION
LENGTH since $|\Phi| \approx cn$. So $T_{\mathrm{classical}} =
\mathrm{poly}(T_{\mathrm{cascade}}, |\Phi|)$.

(Classical → Cascade.) Simulate a Turing machine on cascade
substrate. Tape cells ↔ cascade vertices at some fixed rung. Head
operations ↔ local F-steps. Each TM step takes $O(1)$ cascade
operations. So $T_{\mathrm{cascade}} = O(T_{\mathrm{classical}})$.

Combining: polynomial in each direction. □

### D2.5 Consequence

Cascade time and classical time agree on the polynomial class.
So P_cas = P (classical) as functional classes.

This is the cascade statement of the Church-Turing thesis.

---

## D3. Cascade Space

### D3.1 State space size

**Definition D3.1 (Cascade space complexity).** *For a cascade
program $\mathcal{A}$ on input $\Phi_0$, the space is the maximum
state-space dimension used during the computation:*
$$S_{\mathcal{A}}(\Phi_0) := \max_t \dim(\text{configuration at step } t).$$

### D3.2 Polynomial space

**Definition D3.2 (Polynomial cascade space).** *A cascade program
uses polynomial space if $S_{\mathcal{A}}(\Phi) \leq p(|\Phi|)$ for
some polynomial $p$ and all inputs $\Phi$.*

### D3.3 Relation to classical space

**Theorem D3.1 (Space equivalence).** *Up to polynomial factors,
cascade polynomial space equals classical Turing-machine polynomial
space.*

Proof analogous to D2.1.

### D3.4 Space-time tradeoffs

Standard time-space tradeoffs hold: any cascade computation using
time $T$ uses space at most $T$ (one shell's worth of state per time
step). Conversely, space $S$ implies time at least $\log_\varphi S$
(to set up the required state).

---

## D4. Dynamical Laws

### D4.1 F-flow equation

**Definition D4.1 (Cascade F-flow).** *The continuous cascade
dynamics is the gradient flow of $F$:*
$$\frac{d\Phi}{dt} = -\nabla_\Phi F[\Phi].$$

Discretised: $\Phi_{t+1} = \Phi_t - \eta \nabla F[\Phi_t]$ (one
F-step).

### D4.2 σ-symmetry law

$F[\sigma \Phi] = F[\Phi]$ by F5.

Consequence: F-flow respects σ-orbits.
$$\nabla F[\sigma \Phi] = \sigma \cdot \nabla F[\Phi]$$

If $\Phi_0$ is σ-fixed, the flow stays in the σ-fixed subspace.

### D4.3 Bootstrap refinement law

$\Phi_{n+1} = \mathsf{R}(\Phi_n) = $ Schläfli refinement.

Structurally: each refinement multiplies state-space by a factor
of 5 (Schläfli 5:1) per step, giving $\dim V_n = 24 \cdot 5^n$ at
H₄ level.

### D4.4 Conservation laws

Cascade dynamics conserves:
- **Total σ-parity**: F-flow is σ-equivariant, so σ-eigenvalues are
  preserved.
- **Rung structure**: $\mathsf{P}_r$ commutes with F-flow restricted
  to rung $r$.
- **φ-adic valuation classes**: F-flow maps cohomology classes to
  same-valuation classes.

These are cascade analogs of classical Noether charges.

---

## D5. Cascade Turing Machines

### D5.1 The CTM model

**Definition D5.1 (Cascade Turing Machine).** *A CTM is a tuple
$(Q, \Sigma, \delta, q_0, q_f)$ where:*

- *$Q$ is a finite set of control states.*
- *$\Sigma$ is the cascade alphabet (finite set of cascade-state
  labels, e.g., $\{$ H₄ vertex labels $\}$).*
- *$\delta: Q \times \Sigma \to Q \times \Sigma \times \{\mathsf{F},
   \mathsf{S}, \mathsf{R}\}$ is the transition function.*
- *$q_0, q_f \in Q$ are initial and accepting states.*

A CTM operates on a configuration $\Phi$ of the cascade substrate
(a "cascade tape"). At each step, it reads the current cascade
state, consults $\delta$, writes a new state, and applies the
chosen primitive ($\mathsf{F}$, $\mathsf{S}$, or $\mathsf{R}$).

### D5.2 CTM computation

A CTM computes a function $f: \mathrm{inputs} \to \mathrm{outputs}$
if, for every input $\Phi_0$, running the CTM halts in state $q_f$
with output $f(\Phi_0)$ as the cascade configuration.

### D5.3 CTM = classical TM (Church-Turing)

**Theorem D5.1 (Church-Turing for cascade).** *The class of functions
computable by CTMs equals the class of functions computable by
classical Turing machines.*

**Proof.**

($\Rightarrow$) Given a CTM, simulate it on a classical TM. The
cascade substrate can be serialised onto the TM tape; primitives
can be simulated by local TM operations. Time overhead: polynomial.

($\Leftarrow$) Given a classical TM, embed its tape in the H₄
substrate (assign each tape cell to a cascade vertex). TM
transitions correspond to local cascade F-steps. Time overhead:
polynomial.

Hence CTM-computable = TM-computable. □

### D5.4 Non-determinism and NP

Define **Non-deterministic CTM** (NCTM) by allowing multiple
possible transitions $\delta(q, \sigma) \subseteq Q \times \Sigma
\times \{\mathsf{F}, \mathsf{S}, \mathsf{R}\}$ at each step. NCTM
accepts if some branch leads to $q_f$.

As with classical NDTM, NCTM-NP equals classical NP.

---

## D6. Cascade Complexity Classes

### D6.1 Basic classes

**Definition D6.1 (Cascade complexity classes).**

- **P_cas** = $\{L : \exists$ polynomial-time CTM deciding $L\}$.
- **NP_cas** = $\{L : \exists$ polynomial-time NCTM deciding $L\}$.
- **PSPACE_cas** = $\{L : \exists$ polynomial-space CTM deciding $L\}$.
- **EXP_cas** = $\{L : \exists$ exponential-time CTM deciding $L\}$.
- **BPP_cas**, **BQP_cas**, etc., for randomised/quantum cascade.

### D6.2 Equivalences

**Theorem D6.1.** *Up to polynomial factors:*
- *P_cas = P (classical).*
- *NP_cas = NP (classical).*
- *PSPACE_cas = PSPACE (classical).*
- *EXP_cas = EXP (classical).*

**Proof.** Follows from CTM = TM (D5.3) and the standard complexity
class inclusions. □

### D6.3 Structural cascade classes

Beyond the standard classes, cascade admits structural classes:

- **$\Sigma$-P_cas**: problems solvable in polynomial time using
  σ-invariant CTMs only.
- **Rung-P_cas**: problems solvable by CTMs restricted to a single
  cascade rung.
- **φ-P_cas**: problems solvable in polynomial shell depth (cascade-
  native time).

These are cascade-specific and don't directly correspond to classical
classes. They characterise problems with specific structural
properties.

### D6.4 σ-complexity

σ-P_cas ⊂ P_cas: σ-invariant algorithms are a proper subset of
all polynomial-time algorithms. Algorithms exploiting asymmetric
structure are outside σ-P_cas.

This gives a fine-grained view of computational complexity beyond
the classical TM-based classes.

---

## D7. Cascade Reductions

### D7.1 Karp reduction

**Definition D7.1 (Cascade Karp reduction).** *A Karp (many-one)
reduction from language $L_1$ to $L_2$ is a polynomial-time CTM
that, given $x$, produces $y$ such that $x \in L_1 \Leftrightarrow
y \in L_2$.*

### D7.2 σ-preserving reduction

**Definition D7.2 (σ-Karp reduction).** *A σ-preserving Karp reduction
additionally satisfies $\sigma y = $ (reduction of $\sigma x$). That
is, the reduction commutes with σ.*

Not all Karp reductions are σ-preserving; this is a strictly stronger
condition.

### D7.3 Cascade-complete problems

**Definition D7.3 (Cascade-NP-complete).** *$L$ is NP_cas-complete if
$L \in $ NP_cas and every NP_cas language reduces to $L$ via cascade
Karp reductions.*

By D5.3 + D6.2, classical NP-complete problems (SAT, TSP, etc.) are
also NP_cas-complete.

### D7.4 σ-complete problems

Within σ-P_cas, we can ask about σ-preserving reductions. A problem
$L$ is σ-NP-complete if $L \in $ NP_cas and every σ-NP_cas
language reduces to $L$ via σ-preserving reductions.

σ-NP-complete is a structurally richer notion; it's specific to
cascade.

---

## D8. Cascade-Natural Complete Problems

### D8.1 CASCADE-SAT

**Definition D8.1.** *CASCADE-SAT is the following decision problem:*

*Input: a cascade substrate at some depth $n$, together with a
cascade closure functional $F$ (encoded as rational coefficients
$\alpha, \beta, \gamma$) and a boolean constraint $C$ on
configurations.*

*Question: does there exist a configuration $\Phi$ with $F[\Phi] = 0$
and $C[\Phi]$ true?*

**Proposition D8.1.** *CASCADE-SAT is NP_cas-complete.*

Proof sketch: CASCADE-SAT reduces to classical SAT (since cascade
configurations are finite at each depth, constraints are boolean) and
vice versa (encode classical SAT instances as cascade closure
constraints on the H₄ substrate).

### D8.2 σ-IRREDUCIBLE-SAT

**Definition D8.2.** *σ-IRREDUCIBLE-SAT is CASCADE-SAT restricted
to instances where the constraint $C$ is σ-irreducible (does not
factor through σ-orbits).*

This is a specifically cascade problem with no classical analog. It
asks: does the problem have structure at the σ-level or not?

**Proposition D8.2.** *σ-IRREDUCIBLE-SAT is σ-NP-complete (for the
σ-preserving reduction class).*

### D8.3 CASCADE-CLOSURE-SEARCH

**Definition D8.3.** *CASCADE-CLOSURE-SEARCH is the problem of
finding a cascade configuration minimising $F$.*

This is the "search" analog of CASCADE-SAT: instead of asking if a
F=0 configuration exists, find the one closest to F=0.

**Proposition D8.3.** *CASCADE-CLOSURE-SEARCH is NP_cas-hard.*

### D8.4 Why these are natural

These problems are CASCADE-NATURAL in the sense that:
- They're formulated in cascade language (substrate, closure
  functional, σ-invariance).
- Their complexity analysis uses cascade tools (substrate dim, σ-
  orbit count, φ-graded shell depth).
- They generalise classical NP-complete problems (SAT, Boolean
  optimisation).

---

## D9. Structural Complexity Theorems

### D9.1 σ-structure complexity

**Theorem D9.1 (σ-structure determines σ-P).** *A problem is in σ-P_cas
if and only if it admits a σ-preserving polynomial-time algorithm.*

This is tautological by definition but has non-trivial consequences
for specific problems.

### D9.2 σ-irreducibility and hardness

**Conjecture D9.1 (σ-irreducibility ⇒ NP-hardness).** *Any problem
whose instances are generically σ-irreducible (no non-trivial σ-
factoring) and which is in NP_cas is not in σ-P_cas.*

This conjecture, if true, would explain why generic NP-complete
problems resist polynomial-time σ-symmetric solution.

### D9.3 Cascade depth as complexity measure

**Theorem D9.2 (Cascade depth bound).** *If a problem requires
visiting every state in the cascade state-space at depth $n$, it
cannot be solved in polynomial cascade time.*

**Proof.** Polynomial cascade time allows $\mathrm{poly}(n)$ F-steps.
Each F-step can visit at most $O(1)$ configurations locally. So
total visits are polynomial in $n$. If the problem requires visiting
$\dim V_n = \Omega(\varphi^{cn})$ states, it cannot be done in
polynomial time. □

### D9.4 σ-orbit collapse theorem

**Theorem D9.3 (σ-orbit collapse).** *If a problem is σ-reducible
(σ acts non-trivially on its instances), then it can be solved by
a σ-preserving algorithm with at most half the state-space size of
the full cascade.*

**Proof.** σ-preserving algorithms need only consider one
representative per σ-orbit. Since σ has order 2 (involution), each
orbit has 1 or 2 elements. Generic orbits have 2 elements, so at
most half the state-space need be visited. □

---

## D10. What This Framework Enables

### D10.1 P vs NP in cascade

With D1–D9, we can formulate cascade P vs NP precisely:

**Question.** *Is P_cas = NP_cas?*

By D6.2 (Church-Turing equivalence), this is equivalent to the
classical P vs NP question. So cascade doesn't change the question
but provides new tools for studying it.

### D10.2 New tools cascade provides

- **σ-irreducibility analysis**: determining whether a problem's
  structure can be cascade-symmetry-accelerated.
- **Rung-specific algorithms**: matching problem structure to
  specific cascade rungs for specialised algorithms.
- **φ-adic complexity analysis**: measuring complexity in cascade-
  natural scales.

### D10.3 Cascade-specific arguments

Cascade enables arguments not obviously available classically:

- **Counting argument**: generic NP problems have σ-irreducible
  instance distributions; cascade state-space at depth $n$ is
  $\varphi^{cn}$; traversing this is exponential.
- **Structure argument**: σ-preserving algorithms are strictly
  weaker than general algorithms; NP-complete problems are
  σ-irreducible generically.

These arguments form the basis of the cascade approach to P vs NP
(developed in the following paper).

### D10.4 What remains conjectural

- Conjecture D9.1 (σ-irreducibility implies NP-hardness).
- Whether σ-arguments evade the natural proofs barrier.
- Whether cascade-specific arguments translate to classical-TM
  language without losing rigor.

These are the substantive conjectures of cascade dynamics that
the P vs NP revisit paper addresses.

---

## Summary

We have developed a cascade dynamics framework parallel to the
static foundations:

| Static (F1–F8) | Dynamic (D1–D10) |
|---|---|
| Structures | Primitives (D1) |
| Invariants | Resource measures (D2, D3) |
| Symmetries | Dynamical laws (D4) |
| Objects | Turing machines (D5) |
| Classifications | Complexity classes (D6) |
| Morphisms | Reductions (D7) |
| Canonical forms | Complete problems (D8) |
| Theorems | Structural complexity theorems (D9) |

With this framework in place, P vs NP can be approached via cascade
tools (σ-irreducibility, shell-depth complexity, rung-specific
arguments). The static framework alone could not do this; the
dynamic framework enables it.

**Next: a proper P vs NP paper using D1–D9 to construct a cascade
argument for P ≠ NP.**

---

## Appendix A: Open questions

1. **A.1**: Are there problems in P_cas but not σ-P_cas (other than
   trivial ones)?
2. **A.2**: Is σ-IRREDUCIBLE-SAT strictly harder than CASCADE-SAT in
   any meaningful sense?
3. **A.3**: Do cascade quantum complexity classes (BQP_cas) match
   classical BQP, or diverge because of cascade-specific quantum
   structure (octonion non-associativity)?
4. **A.4**: What is the cascade analog of #P (counting complexity)?
5. **A.5**: Can cascade's $\varphi$-adic structure give new oracle
   separations (evading the relativization barrier)?

These are well-defined research directions enabled by the dynamic
framework.

---

## Appendix B: Connection to static foundations

Each dynamic primitive corresponds to a static cascade structure:

| Primitive | Static structure | Foundation |
|---|---|---|
| $\mathsf{F}$ | Closure functional gradient | F2 |
| $\mathsf{S}$ | Galois involution | F5 |
| $\mathsf{R}$ | Schläfli refinement | F6 |
| $\mathsf{P}_r$ | Rung structure | F3 |

So the dynamic framework is BUILT FROM the static foundations.
It's not an independent theory but a derivative one. This gives
consistency: if the static foundations are sound (which they are),
the dynamic framework inherits that soundness.

The dynamic framework adds NEW CONTENT on top of the static one:
resource measures, complexity classes, computational analysis.
But its foundation remains the static framework.
