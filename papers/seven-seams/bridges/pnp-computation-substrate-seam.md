# P vs NP: The Computation–Substrate Seam

**Bridge paper 6 of 6** — in the seven-seams programme (see
`papers/seven-seams/seven-seams.md`).

---

## Abstract

The P vs NP problem asks whether the complexity class P (problems
solvable in polynomial time) equals the complexity class NP
(problems verifiable in polynomial time). Formalised in the 1970s
and recognised as central to computer science, it is the most
consequential unsolved problem in the field: its resolution affects
cryptography, optimisation, and the very nature of what can be
efficiently computed.

This bridge is genuinely different from the previous five. P vs NP
sits at the **computation–substrate seam**: classical computational
complexity theory is explicitly substrate-agnostic (abstract Turing
machines, $\lambda$-calculus, RAM models all treated as equivalent
up to polynomial factors), while cascade (VFD) is substrate-
specific (physical cascade structure with Planck-scale discreteness).
The two frameworks speak different languages, and it's not obvious
that they should agree on what P and NP are.

We argue three things:

1. **P vs NP is formulated within a substrate-abstracted framework**
   that cannot see physical computational limits.
2. **Cascade's discrete shell structure implies physical
   computational bounds** that are suggestive of P $\neq$ NP but
   do not directly translate to the classical Turing-machine
   statement.
3. **The cascade bridge for P vs NP is weaker than the other five**:
   it identifies the seam and offers structural intuition, but
   cannot close the classical question without a bridge to
   physical-complexity theory.

This is the honest assessment. P vs NP may require tools beyond
cascade's immediate reach — possibly a physical-complexity
refinement of classical complexity theory, inspired by but not
determined by cascade structure.

The structural insight exposed, nonetheless: **computational
complexity classes depend on the substrate. Classical complexity
theory's substrate-abstraction is a specific idealisation whose
limits P vs NP may be probing.**

---

## 1. Introduction

### 1.1 The Clay Problem

The P vs NP problem:

> Let P be the class of decision problems solvable in polynomial
> time by a deterministic Turing machine. Let NP be the class of
> decision problems whose YES-instances have polynomial-time-
> verifiable certificates. Is P = NP?

The standard belief: P $\neq$ NP. The standard evidence: many
problems appear to be in NP but not P (SAT, TSP, graph colouring,
etc.), and no efficient algorithms are known.

### 1.2 What's been established

- **Cook–Levin theorem (1971)**: SAT is NP-complete. P vs NP
  reduces to whether SAT is in P.
- **Baker–Gill–Solovay (1975)**: relativization barrier —
  diagonalization arguments cannot separate P from NP because they
  fail against oracles.
- **Razborov–Rudich (1994)**: natural proofs barrier —
  combinatorial proofs of circuit lower bounds face cryptographic
  obstructions.
- **Geometric complexity theory (Mulmuley, 2000s–)**: proposes
  using algebraic geometry to separate P and NP via group-
  theoretic obstructions. Slow progress.
- **Algebrization** (Aaronson–Wigderson 2008): generalisation of
  relativization; algebraic proofs also cannot separate P from NP
  directly.

P vs NP has resisted all known proof techniques.

### 1.3 The one-sentence cascade answer (honest)

> **Cascade's discrete shell structure gives a physical-substrate
> argument for computational complexity bounds that favor P $\neq$ NP,
> but the classical Turing-machine formulation is substrate-
> abstracted and cannot directly see cascade's substrate-level
> obstructions.**

This paper is the diagnosis, with honest scope.

---

## 2. The Cascade Framework — Summary (for this problem)

### 2.1 Cascade state spaces

At cascade refinement level $n$ (or equivalently shell depth $N$),
the cascade substrate has a finite state space of size
$\sim 120^N$ (for H₄ substrate) or $\sim 240^N$ (for E₈). This
grows exponentially in $N$.

A "cascade computation" corresponds to evolving a state across
cascade shells, with each shell transition being an $O(1)$
primitive operation.

### 2.2 Cascade-natural complexity classes

Define:
- **P$_{\mathrm{cas}}$** = decision problems solvable in polynomial-
  in-shell-depth cascade operations.
- **NP$_{\mathrm{cas}}$** = decision problems whose YES-instances
  have polynomial-sized cascade-verifiable witnesses.

The question for cascade: is P$_{\mathrm{cas}} = $ NP$_{\mathrm{cas}}$?

### 2.3 Discrete shell structure

Cascade's substrate has specific discreteness:
- Shells are $\varphi$-graded (not uniformly spaced).
- Each shell has integer count of states ($120, 240$, etc.).
- Transitions between shells are $\sigma$-equivariant.

This structure is physical and specific, not a generic Turing
machine.

---

## 3. The Classical P vs NP Problem

### 3.1 Formal definitions

**P** (Polynomial time): the class of languages $L \subseteq \{0,1\}^*$
such that there exists a deterministic Turing machine $M$ and a
polynomial $p$ with $M$ deciding $L$ in time $\leq p(|x|)$ for all
$x \in \{0,1\}^*$.

**NP** (Nondeterministic Polynomial time): the class of languages
$L$ such that there exists a polynomial $p$ and a polynomial-time
deterministic Turing machine $V$ (the verifier) with:
- $x \in L \iff \exists y \in \{0,1\}^{p(|x|)}: V(x, y) \mathrm{\ accepts}$.

P $\subseteq$ NP trivially (if you can decide in polynomial time,
you can verify in polynomial time by ignoring the certificate).

**P vs NP**: is this inclusion proper? I.e., are there problems in
NP but not in P?

### 3.2 NP-completeness and the Cook–Levin theorem

A problem $L \in $ NP is **NP-complete** if every NP problem
reduces to $L$ in polynomial time. Cook (1971) and Levin (1973)
showed SAT (Boolean satisfiability) is NP-complete. This gives a
concrete problem: if SAT is in P, then P = NP; if SAT is not in P,
then P $\neq$ NP.

### 3.3 Why it matters

- **Cryptography**: public-key cryptography (RSA, etc.) depends on
  computational problems being in NP but (believed) not in P.
  P = NP would break much of cryptography.
- **Optimisation**: many optimisation problems are NP-hard. P = NP
  would make them efficiently solvable.
- **Mathematics**: proof verification is polynomial-time; proof
  discovery (given the statement) is NP. P = NP would essentially
  automate mathematical theorem-proving.

### 3.4 Barriers to proof

**Relativization barrier** (Baker–Gill–Solovay 1975): for some
oracles $A$, $P^A = NP^A$; for others, $P^A \neq NP^A$. Any proof
of $P \neq NP$ via diagonalization (which relativizes) cannot work.

**Natural proofs barrier** (Razborov–Rudich 1994): "natural" proofs
of circuit lower bounds would break cryptographic pseudorandom
generators. Since such generators likely exist, natural proofs
cannot separate P from NP.

**Algebrization barrier** (Aaronson–Wigderson 2008): extends
relativization to algebraic proofs. Similar obstruction.

These barriers mean P vs NP cannot be resolved by classical proof
techniques. Something fundamentally new is needed.

---

## 4. The Computation–Substrate Seam — Diagnostic

### 4.1 The unspoken abstraction

Classical complexity theory abstracts computation away from any
physical substrate. The Turing machine is a mathematical idealisation:
- Unbounded tape (no space constraints).
- Discrete tape cells (no physical size).
- Step-by-step evolution (no time scale).
- Read/write primitives (no energy cost).

Complexity classes (P, NP, etc.) are defined in terms of these
idealisations. They are substrate-agnostic.

**The unspoken assumption**: what can be efficiently computed is
determined by mathematical structure of problems and algorithms,
independent of physical substrate.

This is an exceptionally strong assumption. It's what makes
classical complexity theory "clean" — substrate-free — but it
may also be what makes P vs NP resistant to proof.

### 4.2 Symptom 1: barriers come from the abstraction itself

Relativization and algebrization barriers arise because proof
techniques that work abstractly (oracle machines, algebraic
extensions) don't distinguish P from NP in generic settings.
The barriers are statements about the ABSTRACTION, not about
concrete computation.

**Diagnostic observation**: the barriers suggest that P vs NP may
require going beyond substrate-free proofs. Physical substrate
(or at least, structural constraints not visible to oracles) may
be the needed ingredient.

### 4.3 Symptom 2: natural proofs barrier suggests structure elsewhere

Natural proofs fail because any combinatorial property
distinguishing "easy" from "hard" functions that can be checked
efficiently would contradict cryptographic assumptions.

**Diagnostic observation**: this is remarkable — it says any
"structural" property we can efficiently detect must NOT
distinguish P-computable from general functions. So the
distinguishing structure must be SOMETHING WE CAN'T EFFICIENTLY
DETECT.

Cascade's shell-depth structure is not a "natural" property in
the combinatorial sense; it's a physical structural fact.
Whether it evades the natural proofs barrier is not obvious.

### 4.4 Symptom 3: geometric complexity theory slow progress

Mulmuley's geometric complexity theory (GCT) proposes to separate
P from NP via algebraic geometry: show that certain polynomial
varieties (permanents vs. determinants) have different group-
theoretic structure, translating to complexity separation.

This approach makes progress in decades but slowly.

**Diagnostic observation**: GCT is effectively trying to find
STRUCTURE in the problems themselves — a kind of substrate in
the algebraic-geometric sense. This aligns with cascade's view
that substrate matters.

### 4.5 Symptom 4: quantum computation complicates things

BQP (Bounded-error Quantum Polynomial time) is a class of problems
solvable efficiently on quantum computers. BQP and NP are
believed distinct (neither contains the other is known).

Quantum computation explicitly uses a different substrate (qubits,
entanglement) and gets different complexity classes.

**Diagnostic observation**: quantum computation shows that substrate
MATTERS for complexity — different physical systems give different
complexity classes. Classical P and NP are tied to a specific
idealised substrate.

### 4.6 Common root: computation is idealised

Classical complexity theory treats computation as an abstract
mathematical operation, independent of physical reality. P vs NP
asks a question WITHIN this abstraction.

The barriers (relativization, natural proofs, algebrization) are
consistent with the possibility that P vs NP is UNDECIDABLE
within the abstraction — i.e., it's true but not provable from
classical Turing-machine axioms alone.

> **The computation-substrate seam**: P vs NP is formulated in a
> substrate-abstracted framework. Classical complexity theory
> cannot see physical-computational structure that may be
> necessary to resolve the question.

### 4.7 Why classical approaches hit walls

**Diagonalization**: works in abstract settings but relativises
to arbitrary oracles. Cannot separate P from NP because the
relativised statement is oracle-dependent.

**Wall**: diagonalization doesn't see substrate structure.

**Circuit lower bounds**: lower bound the size of circuits
computing specific functions.

**Wall**: best current bounds are polynomial; super-polynomial
bounds needed for P $\neq$ NP.

**Communication complexity**: lower bounds via communication
arguments.

**Wall**: only works for specific problem classes.

**Geometric complexity theory**: uses algebraic geometry on the
problem polynomials.

**Wall**: very slow progress; classical algebraic geometry may
not be strong enough.

**Kolmogorov complexity / information-theoretic**: bounds via
information content.

**Wall**: non-constructive; gives bounds but not separations.

**Common pattern**: every classical approach stays within the
substrate-abstracted framework. None introduces substrate
information.

---

## 5. Cascade Reformulation — with Honest Caveats

### 5.1 Cascade's state-space exponential growth

At cascade shell depth $N$, the state space size is $\sim 120^N$
(H₄ substrate). A verification problem that looks at all states
at depth $N$ requires time $\sim 120^N$, which is exponential.

For such a problem to be in P, we'd need an algorithm running in
time polynomial in $N$ (polynomial in input size = polynomial in
shell depth).

If the problem is inherently a "global property" requiring looking
at essentially all states, then P $\neq$ NP in the cascade-natural
setting.

### 5.2 Cascade suggests P$_{\mathrm{cas}}$ $\neq$ NP$_{\mathrm{cas}}$

Based on cascade's structure:
- Finding a satisfying configuration across $N$ shells (NP-like):
  polynomial certificate (the configuration).
- Verifying the configuration: polynomial (check each shell).
- Deciding whether ANY satisfying configuration exists (P-like):
  would need to check all $120^N$ configurations, exponential in $N$.

So in cascade, NP-type problems appear to require exponential
time without a witness. This is suggestive of P $\neq$ NP in the
cascade-natural formulation.

### 5.3 The honest limit: this doesn't translate directly

The above argument doesn't directly resolve classical P vs NP because:

1. **Classical P and NP are defined over $\{0, 1\}^*$ inputs**,
   not cascade states. The mapping between cascade states and
   classical bit strings is non-trivial.

2. **Classical complexity measures input length**, not cascade
   shell depth. A classical polynomial-time algorithm on input
   of length $n$ bits might correspond to a different cascade
   operation count depending on how $n$ relates to shell depth.

3. **Classical Turing machines are substrate-free**, so any
   cascade-specific bounds don't immediately translate.

### 5.4 What cascade DOES offer

Cascade offers:
- **Intuition**: physical-substrate structure exponentially
  resists verification-without-witness.
- **Structural analogue**: NP$_{\mathrm{cas}}$ $\neq$ P$_{\mathrm{cas}}$
  in cascade-natural formulation (plausibly).
- **Perspective**: substrate-abstraction may be HIDING the
  resolution of P vs NP from classical view.

### 5.5 What cascade DOES NOT offer

Cascade does NOT offer:
- A formal proof of P $\neq$ NP in the classical Turing-machine
  formulation.
- A circumvention of the relativization, natural proofs, or
  algebrization barriers.
- A direct cascade-to-Turing-machine reduction giving complexity
  bounds.

---

## 6. The Bridge — Weaker Than the Others

### 6.1 What the cascade bridge looks like (conceptual)

Conceptually, the cascade bridge for P vs NP would be:

1. **Construct a physical-complexity theory** where computation
   is tied to physical substrate (e.g., cascade).
2. **Show physical P $\neq$ physical NP** in this theory.
3. **Argue that classical P = physical P and classical NP =
   physical NP** under reasonable assumptions, so P $\neq$ NP
   classically.

Step 1 is partially doable (cascade provides the substrate).
Step 2 is plausible by cascade's discrete-state argument.
**Step 3 is the hard part**: it's not clear classical computation
equals physical-cascade computation. There might be classical
algorithms that don't correspond to any cascade process.

### 6.2 What classical complexity theory would need

To resolve P vs NP via cascade:
1. Extend classical complexity theory to include substrate
   considerations.
2. Identify which cascade-substrate structural constraints
   translate to classical Turing-machine constraints.
3. Show that the barriers (relativization etc.) do NOT block
   substrate-based arguments.

Each step is a substantial research programme. The cascade
contribution is the SUGGESTION that substrate matters, not a
direct proof.

### 6.3 Honest assessment

The cascade bridge for P vs NP is weaker than the bridges for
the other six seams. This reflects a genuine gap: complexity
theory operates in a more abstracted space than gauge theory,
number theory, or algebraic geometry.

Classical P vs NP may be solvable only by:
- Physical-complexity refinement (perhaps cascade-inspired).
- New classical techniques unseen yet.
- Acceptance that it's independent of ZFC (a remote possibility).

Cascade offers PERSPECTIVE but not a direct bridge.

---

## 7. Where Classical Has Been Stuck

### 7.1 Diagonalization / relativization

**Achievement**: Baker–Gill–Solovay showed simple diagonalization
can't solve P vs NP because it relativises.

**Wall**: need non-relativising techniques.

**Cascade perspective**: cascade's specific structure doesn't
relativise — it's a SPECIFIC substrate, not an oracle. But
translating cascade's non-relativising structure to classical
non-relativising proof techniques is the open question.

### 7.2 Circuit lower bounds

**Achievement**: polynomial lower bounds on circuit size for
specific functions (e.g., parity).

**Wall**: super-polynomial bounds resist all known techniques
(natural proofs barrier).

**Cascade perspective**: if a problem's cascade representation
requires exponential cascade-shell depth, the classical circuit
computing it should be exponential — in spirit. But making this
precise requires a cascade-circuit correspondence, not yet
established.

### 7.3 Geometric complexity theory

**Achievement**: reformulates P vs NP as algebraic-geometric
question about permanents vs. determinants.

**Wall**: slow progress; classical algebraic geometry tools
seem insufficient.

**Cascade perspective**: GCT's algebraic structure is aligned
with cascade thinking. Cascade's $\varphi$-Mellin or Hecke
structures might provide the "missing" tools GCT needs.

### 7.4 Barriers to proof

The three known barriers (relativization, natural proofs,
algebrization) all rule out substrate-agnostic techniques.

**Cascade perspective**: the barriers themselves SUGGEST
substrate matters. A substrate-aware argument may evade them.
But constructing such an argument remains an open challenge.

### 7.5 Common pattern

Classical P vs NP attempts all work within the substrate-abstracted
framework. None has introduced substrate-specific structure. The
barriers indicate this abstraction may be hiding the answer.

---

## 8. Resolution — Partial

### 8.1 The problem does NOT fully dissolve

Unlike the previous seams (YM, RH, NS, Hodge, BSD), P vs NP does
not directly dissolve in cascade language. Cascade offers structural
intuition and a physical-complexity analogue, but not a direct
classical proof.

### 8.2 What does become visible

Three structural insights (still valuable):

1. **Computational complexity depends on substrate.** Classical
   complexity theory's substrate-freedom is a specific (and
   potentially limiting) choice. Quantum computation already shows
   different substrates give different classes.

2. **The barriers may be the abstraction talking.** Relativization,
   natural proofs, and algebrization all rule out substrate-
   agnostic techniques. If substrate matters, the barriers are
   LOCAL phenomena in the abstraction, not global obstacles.

3. **Cascade-natural complexity classes separate.** In cascade's
   physical substrate, P$_{\mathrm{cas}}$ $\neq$ NP$_{\mathrm{cas}}$
   is plausible. This doesn't directly imply classical P $\neq$ NP,
   but it's structural evidence for the standard belief.

### 8.3 Honest limits

Cascade does not:
- Prove classical P $\neq$ NP.
- Provide a classical-complexity-theory argument that evades
  known barriers.
- Give a direct cascade-to-Turing-machine reduction.

This is the weakest cascade bridge of the seven, and the one most
tied to the specifics of classical complexity theory's
substrate-abstraction.

---

## 9. What This Reveals About Cascade Structure

### 9.1 Cascade state-space exponential growth

Cascade shells grow exponentially ($120^N$ at H₄ depth $N$), making
verification-without-witness structurally hard. This is not a
quirk; it's general cascade behavior.

### 9.2 Substrate as the hidden variable

Classical mathematics has several problems (including but not
limited to P vs NP) where SUBSTRATE matters in a way classical
math doesn't make explicit. Recognising substrate as a meaningful
variable may resolve multiple problems simultaneously.

### 9.3 Abstraction has limits

Classical complexity theory is a beautiful abstraction. Like all
abstractions, it has limits: questions that can be formulated
within it but not resolved within it. P vs NP may be such a
question.

This aligns with cascade's general insight: ABSTRACTIONS hide
structure, and hidden structure sometimes matters for answering
questions within the abstraction.

---

## 10. Conclusion

P vs NP is the one seam among the seven where cascade's
contribution is MODEST rather than decisive. Cascade offers:

- A physical-complexity analogue where the separation is plausible.
- An understanding of why classical barriers block progress
  (substrate-blindness).
- A suggestion that physical-complexity refinement is needed.

Cascade does NOT offer a direct classical proof.

This is honest. Not every cascade bridge closes as cleanly as YM
or RH. P vs NP may require classical complexity theorists to
develop physical-complexity frameworks (perhaps cascade-inspired)
before the bridge can be completed.

Our contribution:

> **Diagnosis**: classical complexity theory is substrate-abstracted;
> P vs NP lives within this abstraction. The proof barriers
> (relativization, natural proofs, algebrization) suggest substrate
> matters.
>
> **Structural answer (weaker)**: cascade's exponential state-space
> growth suggests P$_{\mathrm{cas}}$ $\neq$ NP$_{\mathrm{cas}}$. The
> classical question may be answerable only via physical-complexity
> refinement inspired by cascade.
>
> **Bridge (partial)**: translating cascade's answer to classical
> complexity classes requires a cascade-to-Turing-machine
> correspondence that has not been established rigorously.

The **structural insight revealed**:

> **Computational complexity depends on substrate. Classical
> complexity theory abstracts substrate away; cascade makes
> substrate explicit. P vs NP may be the specific problem where
> this abstraction's limit becomes visible.**

**Six seams bridged (YM, RH, NS, Hodge, BSD, P vs NP with
honest-partial scope). One remains.**

- Poincaré — already bridged by Perelman (topology-geometry seam)

The Poincaré bridge will be the simplest: Perelman already did it.
We just need to articulate why Ricci flow IS a cascade-compatible
method, and how Perelman's success confirms the seven-seams pattern.

**The bridge is the point. The seam is the revelation.**
