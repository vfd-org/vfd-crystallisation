# WO-ARIA-VFD-OPTIMISER-001: Research Log

## Closure-Constrained Resonant Optimiser (CCRO) — a VFD-native optimisation class

**Status:** PAUSED 2026-04-16 — deferred in favour of VFD Explorer (see `papers/vfd-explorer/`). CCRO remains valid as a downstream application of VFD logic to ML, but the explorer is the more foundational build and should land first. Resume after explorer v1 ships.
**Date opened:** 2026-04-16
**Classification:** Method design + empirical validation

---

## 1. Executive Summary

We propose a new optimiser class in which parameter updates are not
chosen by steepest descent, but by **deterministic selection of the
highest-coherence admissible candidate** from a small family of
locally-reachable updates.

Standard optimisers minimise a scalar loss $L(\theta)$ via
$\theta_{t+1} = \theta_t - \eta P_t \nabla L$.

CCRO replaces this with a crystallisation rule:

$$
\theta_{t+1} = \operatorname{Crystalise}\!\bigl(\theta_t,\, G_t,\, \mathcal{C}_t,\, \mathcal{R}_t,\, \mathcal{B}_t\bigr)
$$

where $G_t$ is the local gradient signal, $\mathcal{C}_t$ a coherence
field, $\mathcal{R}_t$ a resonance functional, and $\mathcal{B}_t$ a
closure/boundary constraint set.

SGD, Adam, Muon, and Newton-Muon appear as **limiting cases** where
$\mathcal{C}_t, \mathcal{R}_t, \mathcal{B}_t$ collapse to triviality.

**Goal of this WO:** define the minimal governed optimiser, implement
it as a PyTorch wrapper over existing step families, and demonstrate
that governance (not a new step direction) yields measurable gains on
at least one metric where coherence/closure should matter —
long-run stability, cross-module consistency, or multi-objective
robustness.

**Non-goal:** we are not trying to beat Adam on raw convergence speed.
That is fighting on the wrong axis.

---

## 2. Position vs Existing Optimisers

| Family | Signal used | Step rule | Admissibility |
|---|---|---|---|
| SGD | $g_t$ | $-\eta g_t$ | none |
| Adam / RMSProp | $g_t$, running $g^2$ | $-\eta P_t g_t$ | none |
| Muon | $g_t$, orthogonalization | orthogonalised $g_t$ | none |
| Newton / K-FAC | $g_t$, curvature $H$ | $-\eta H^{-1} g_t$ | none |
| **CCRO** | gradient, curvature, coherence, resonance, closure | argmax of crystallisation score over candidate set | closure residual + energy budget |

The key shift: CCRO does not commit to a single step geometry. It
generates several geometrically plausible candidate steps and selects
among them under structural constraints.

---

## 3. Formal Framework

### 3.1 State variables

At step $t$, with parameters $\theta_t \in \mathbb{R}^n$, define:

1. Gradient $g_t = \nabla_\theta L(\theta_t)$
2. Curvature proxy $H_t$ (diagonal Fisher, low-rank Hessian, or layerwise covariance)
3. Metric tensor $M_t \succeq 0$ (may equal $H_t + \lambda I$)
4. Coherence functional $C(\delta\theta; \theta_t) \in \mathbb{R}$
5. Resonance functional $R(\delta\theta; \theta_t, \mathcal{M}) \in \mathbb{R}$
6. Closure residual $\Xi(\delta\theta; \theta_t) \geq 0$
7. Energy budget $E_t > 0$
8. Closure tolerance $\varepsilon_t \geq 0$

### 3.2 Crystallisation score

For a candidate update $\delta\theta$:

$$
\mathcal{S}(\delta\theta) \;=\;
-\alpha\, \widehat{\Delta L}(\delta\theta)
+\beta\, C(\delta\theta)
+\gamma\, R(\delta\theta)
-\mu\, \Xi(\delta\theta)
-\nu\, \lVert \delta\theta \rVert_{M_t}^2
$$

where $\widehat{\Delta L}(\delta\theta) \approx \langle g_t, \delta\theta\rangle$
(first-order loss estimate; second-order optional).

### 3.3 Admissible set

$$
\mathcal{A}_t \;=\;
\bigl\{ \delta\theta \;:\; \Xi(\delta\theta) \leq \varepsilon_t,\;\;
\lVert \delta\theta \rVert_{M_t}^2 \leq E_t \bigr\}
$$

### 3.4 Selection rule

$$
\delta\theta_t^\star \;=\; \arg\max_{\delta\theta \in \mathcal{K}_t \cap \mathcal{A}_t}\; \mathcal{S}(\delta\theta)
$$

where $\mathcal{K}_t = \{\delta^{(1)}, \dots, \delta^{(m)}\}$ is a finite
candidate set. This keeps the selection discrete and deterministic.

Then $\theta_{t+1} = \theta_t + \delta\theta_t^\star$.

### 3.5 Continuous-flow form (for theoretical paper later)

The unconstrained continuous form is the stationarity of

$$
\mathcal{F}(\delta\theta) \;=\;
\langle g_t, \delta\theta\rangle
+ \lambda_c \Phi_c(\delta\theta)
+ \lambda_r \Phi_r(\delta\theta)
- \lambda_b \Phi_b(\delta\theta)
- \tfrac{1}{2}\delta\theta^\top M_t \delta\theta
$$

giving

$$
\delta\theta_t \;=\; M_t^{-1}\bigl(g_t + \lambda_c \nabla\Phi_c + \lambda_r \nabla\Phi_r - \lambda_b \nabla\Phi_b\bigr).
$$

Setting $\lambda_c = \lambda_r = \lambda_b = 0$ recovers Newton /
preconditioned methods. This is the "standard optimisers as limiting
case" result for the theoretical companion paper.

---

## 4. Candidate Update Families

Minimal $\mathcal{K}_t$ for the first implementation:

1. $d^{(1)} = -g_t$ (raw gradient)
2. $d^{(2)} = -P_t g_t$ (Adam-style diagonal preconditioner)
3. $d^{(3)} = \operatorname{Muon}(g_t)$ (orthogonalised matrix step)
4. $d^{(4)} = \operatorname{NewtonMuon}(g_t)$ (curvature-aware orthogonalised step)
5. $d^{(5)} = \operatorname{repair}(d^{(k)})$ — project chosen candidate to reduce $\Xi$

Each candidate is length-normalised or trust-region clipped before scoring.

---

## 5. Coherence, Resonance, Closure — concrete forms

### 5.1 Cross-layer directional coherence

$$
C_{\text{layer}}(d) \;=\; \frac{1}{L-1}\sum_{\ell=1}^{L-1} \cos\angle\bigl(d_\ell,\; \Pi_{\ell\to\ell+1} d_{\ell+1}\bigr)
$$

where $\Pi_{\ell\to\ell+1}$ is a block-compatible projection (identity
on matched shapes, orthogonal projection otherwise).

### 5.2 Temporal coherence

$$
C_{\text{time}}(d_t) \;=\; \cos\angle\bigl(d_t,\; d_{t-1}\bigr)
$$

bounded-torsion variant preferred over pure alignment to avoid
momentum-collapse.

### 5.3 Resonance (block phase alignment)

For coupled blocks $(i,j) \in \mathcal{E}$ with linear map $\Phi_{ij}$:

$$
R_{ij}(d) \;=\; \frac{\langle d_i,\; \Phi_{ij} d_j\rangle}{\lVert d_i\rVert\,\lVert d_j\rVert}
$$

$R(d) = \operatorname{mean}_{(i,j)\in\mathcal{E}} R_{ij}(d)$.

### 5.4 Closure residual

For invariants $A_{ij}(\theta) = b_{ij}$:

$$
\Xi(d) \;=\; \sum_{(i,j)\in\mathcal{E}} \bigl\lVert A_{ij}(\theta_t + d) - b_{ij} \bigr\rVert^2
$$

In v1, closure invariants are architecture-agnostic stand-ins:
parameter-group norm ratios, layer-norm gain stability, or
attention-head magnitude balance. These are testable proxies for
"structural admissibility" without requiring VFD-specific constraints.

---

## 6. Algorithm (pseudocode)

```
Input: params θ, loss L, candidate generators {G_k}, weights α β γ μ ν,
       budgets E_t ε_t, history buffer (d_{t-1})

for t = 1, 2, …:
    g ← ∇_θ L(θ)
    build M_t (diagonal Fisher / Adam state / identity)

    # candidate generation
    K ← []
    for G_k in generators:
        d ← G_k(g, state)
        d ← trust_region_clip(d, E_t, M_t)
        K.append(d)

    # optional repair step
    d_best_so_far ← argmax_{d ∈ K} base_score(d)
    K.append(repair(d_best_so_far, Ξ, θ))

    # scoring
    scored ← []
    for d in K:
        if Ξ(d) > ε_t: continue
        if ||d||_{M_t}^2 > E_t: continue
        s ← -α·⟨g,d⟩ + β·C(d) + γ·R(d) - μ·Ξ(d) - ν·||d||_{M_t}^2
        scored.append((s, d))

    if scored is empty:
        d_star ← shrink(d_best_so_far)    # fallback: clipped raw candidate
    else:
        d_star ← argmax scored

    θ ← θ + d_star
    d_{t-1} ← d_star
```

Determinism: tiebreaks are lexicographic on (score, candidate-index).
No stochasticity in selection.

---

## 7. PyTorch Implementation Plan

### 7.1 File layout

```
src/vfd_optim/
    __init__.py
    ccro.py              # main optimiser class
    candidates.py        # update generators (SGD/Adam/Muon/NewtonMuon)
    functionals.py       # C, R, Ξ implementations
    repair.py            # closure-repair projection
tests/
    test_ccro_smoke.py   # runs on a 2-layer MLP, checks determinism
    test_candidates.py
    test_functionals.py
benchmarks/vfd_optim/
    mlp_mnist.py         # baseline comparison
    long_run_stability.py
    multi_task.py
```

### 7.2 Class skeleton

```python
class CCRO(torch.optim.Optimizer):
    def __init__(self, params, *, candidates, weights, budgets,
                 coherence_fn, resonance_fn, closure_fn):
        ...
    def step(self, closure=None):
        # 1. compute g per param group
        # 2. build candidates (list of flat update vectors per group)
        # 3. score each candidate
        # 4. select argmax admissible
        # 5. apply update, update history
```

Candidates are produced per-param-group as flat tensors matching the
group's parameter layout. Functionals take flat-tensor dicts keyed by
param group and return scalars.

### 7.3 Dependencies

- torch
- (optional) einops for block reshaping
- no new build dependencies

### 7.4 Determinism guarantees

- candidate generation deterministic given $(g, \text{state})$
- scoring deterministic
- selection deterministic with lexicographic tiebreak
- repair step deterministic (fixed number of projection iterations)

This makes every optimisation trajectory replayable given initial seed
and data order.

---

## 8. Benchmark Plan

### 8.1 Primary metric: long-run stability

**Setup:** train a 2-layer transformer or MLP on a stable task for
$10\times$ the nominal convergence time. Measure:

- loss drift after nominal convergence
- gradient-direction autocorrelation (oscillation proxy)
- parameter-norm blowup rate
- frequency of loss spikes above $k\sigma$

**Hypothesis:** CCRO shows lower drift and fewer spikes than Adam and
Muon at matched wall-clock, because closure-admissibility filters
destabilising steps.

### 8.2 Secondary metric: multi-objective consistency

**Setup:** train a shared backbone on two tasks with gradient conflict.
Measure Pareto frontier coverage under fixed compute.

**Hypothesis:** resonance term rewards updates that align across
task-specific heads, widening the Pareto frontier.

### 8.3 Tertiary metric: replay determinism

**Setup:** run the same training twice with identical seed and data
order. Compare parameter trajectories.

**Hypothesis:** CCRO is bit-identical across runs. Adam/SGD are not
under standard non-deterministic cuDNN settings; CCRO's determinism is
a useful engineering property in its own right.

### 8.4 Baselines

SGD-momentum, Adam, AdamW, Muon. Same learning-rate sweeps per
baseline.

### 8.5 Success criterion

A single benchmark on which CCRO wins by a statistically-meaningful
margin (p < 0.05 across $\geq$ 5 seeds) on any of the three metrics is
sufficient to justify a short workshop paper. The theoretical paper
follows.

---

## 9. WO Pack for Claude — execution instructions

### 9.1 Scope of this WO

**In scope:**
- implement `src/vfd_optim/` as specified
- write the three test files
- write `benchmarks/vfd_optim/long_run_stability.py`
- run it against Adam and SGD-momentum on a small MLP
- produce a markdown results file in this folder

**Out of scope (for v1):**
- Muon / NewtonMuon candidate families (stub them; implement later)
- transformer benchmarks (v2)
- multi-task benchmark (v2)
- the theoretical companion paper (post-empirical)

### 9.2 Deliverables

1. `src/vfd_optim/` package with working `CCRO` class
2. `tests/test_ccro_smoke.py` passing
3. `benchmarks/vfd_optim/long_run_stability.py` runnable
4. `papers/vfd-optimiser/v1-results.md` with:
   - setup description
   - raw numbers (mean ± std over 5 seeds)
   - plots (loss, gradient autocorrelation, parameter norm)
   - verdict: does CCRO beat baselines on at least one metric?

### 9.3 Step-by-step execution plan

1. **Scaffold.** Create `src/vfd_optim/` skeleton with stubs for every
   function. All tests should import-clean before any real logic.
2. **Candidates.** Implement $d^{(1)}$ (SGD) and $d^{(2)}$ (Adam-style).
   Stub $d^{(3)}, d^{(4)}$ to raise `NotImplementedError`.
3. **Functionals.** Implement temporal coherence $C_{\text{time}}$ and
   a trivial closure residual (parameter-group norm balance).
   Resonance can be stubbed to $0$ in v1.
4. **Optimiser.** Wire up `CCRO.step()` as a thin selector over the
   two live candidates. Verify on a toy quadratic that it reduces to
   SGD when $\beta = \gamma = \mu = 0$.
5. **Smoke test.** 2-layer MLP trains on random data without NaNs for
   1000 steps.
6. **Benchmark.** MNIST MLP, 5 seeds, three optimisers (SGD, Adam,
   CCRO), plot long-run metrics.
7. **Results writeup.** Honest. If CCRO does not win, write why and
   what the next variant should try.

### 9.4 Verification checklist

- [ ] `pytest tests/test_ccro_smoke.py` green
- [ ] Determinism test: two identical seeds produce identical trajectories
- [ ] Degenerate case: weights $\beta=\gamma=\mu=0$ reproduces Adam exactly
- [ ] Benchmark runs end-to-end on CPU in < 20 min
- [ ] Results markdown has plots, raw numbers, and honest verdict

---

## 10. Risks and Fallbacks

**Risk 1:** CCRO never beats Adam on anything.
**Fallback:** theoretical paper still viable — position CCRO as a
*governed* optimiser with deterministic replay as the main win.

**Risk 2:** Candidate set too small — selection collapses to "always
pick Adam".
**Fallback:** add repair step and layerwise-normalised candidate as
separate entries; tune weights so non-Adam candidates win sometimes.

**Risk 3:** Closure residual $\Xi$ is too architecture-agnostic to be
informative.
**Fallback:** define task-specific closure invariants (e.g. attention
head magnitude balance in transformers) in v2.

**Risk 4:** Compute overhead per step makes wall-clock comparisons
unfavourable.
**Mitigation:** v1 reports per-step metrics. v2 adds wall-clock.
Governance-over-speed is an honest positioning.

---

## 11. Next steps

1. User sign-off on folder name and scope.
2. Scaffold `src/vfd_optim/` per §7.1.
3. Implement §9.3 steps 1–4 (candidates + functionals + optimiser).
4. Run §9.3 steps 5–7 (tests + benchmark + writeup).
5. Decide on workshop-paper target venue based on v1 results.

---

## Appendix A: Notation

| Symbol | Meaning |
|---|---|
| $\theta_t$ | parameters at step $t$ |
| $g_t$ | $\nabla_\theta L(\theta_t)$ |
| $H_t$ | curvature proxy |
| $M_t$ | metric tensor for trust region |
| $\delta\theta$ | candidate update |
| $\mathcal{K}_t$ | finite candidate set at step $t$ |
| $\mathcal{A}_t$ | admissible update manifold |
| $C, R, \Xi$ | coherence, resonance, closure residual |
| $\alpha,\beta,\gamma,\mu,\nu$ | crystallisation score weights |
| $E_t, \varepsilon_t$ | energy budget, closure tolerance |

## Appendix B: Relationship to existing work

- **Natural gradient / K-FAC:** special case with $M_t = F_t$, $\beta=\gamma=\mu=0$.
- **Muon:** special case of candidate family $d^{(3)}$ alone.
- **Trust-region methods:** recover the $E_t$ constraint with all field terms off.
- **Multi-gradient methods (PCGrad, MGDA):** related but scalarise via conflict resolution, not admissibility selection.
- **Projected gradient / manifold optimisation:** related via $\mathcal{A}_t$, but CCRO's admissibility is soft (scored) in addition to hard (constrained).

The distinguishing claim of CCRO is **deterministic selection among
geometrically distinct candidate steps under a structural admissibility
rule**. No single prior method does this combination.
