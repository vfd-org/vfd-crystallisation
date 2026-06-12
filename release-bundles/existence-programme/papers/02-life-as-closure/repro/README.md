# Life as Closure --- numerical demonstrations

This directory contains `life_demo.py`, a self-contained Python script that
demonstrates the load-bearing structural claims of *Life as Closure* on the
same $V_{600}$ + $C_\varphi$ + spectral $\tau$ substrate used by
`closure_demo.py` in the companion paper *Existence as Closure*.

The point: every operator-level definition in the paper has a concrete
numerical demonstration, and each demonstration runs in seconds on a laptop.

## Running

```bash
python life_demo.py                # run all 10 demos, save figures + JSON
python life_demo.py --demo 6       # run only L6 (trauma + healing)
python life_demo.py --no-figures   # skip figure saving, numerics only
```

Outputs land in `output/` (one PNG per demo, plus `life_demo_results.json`
with all numerical results).

## What each demo verifies

| ID  | Demo                                          | Paper grounds                                  |
|-----|-----------------------------------------------|------------------------------------------------|
| L1  | Boundary breach + repair                      | Thm 3.2 (Boundary maintenance), Thm 4.1 (Repair)|
| L2  | Memory persistence (closure-stability)        | Thm 5.2 (Memory persistence)                   |
| L3  | Emotional-eigenmode activation dynamics       | Def 9.1, Thm 9.3 (Emotional state)             |
| L4  | Thought trajectory persistence                | Thm 10.2 (Thought persistence in memory)       |
| L5  | Identity under substrate turnover             | Thm 13.2 (Identity is closure-pattern continuity)|
| L6  | Trauma persistence + healing reweighting      | Thm 13.4, Cond. Prop. 13.5                     |
| L7  | Flow regime (4-condition simultaneity)        | Def 13.6, Thm 13.7 (Flow + time-dilation)      |
| L8  | Creativity: trajectory outside Read(Store)    | Thm 13.9 (Creativity requires expansion slack) |
| L9  | Trust $\kappa_{AB}$ under perturbation        | Thm 13.14 (Trust stability conditions)         |
| L10 | Self-deception via boundary filter            | Thm 13.16 (Self-deception is structurally possible)|

## What is verified, quantitatively

Each demo asserts one or two structural claims with explicit
pass / fail thresholds:

- **L1**: measured off-$\Sigma$ decay rate within 5\% of $(1 - \lambda \mu_\perp)^t$
  prediction; SNR drop $> 25\%$ under above-threshold perturbation.
- **L2**: $\| C_\varphi v - P_{\mathsf{Store}}(C_\varphi v) \| < 10^{-10}$
  for $v \in \mathsf{Store}_\Mcal$ (closure-stability is operator-level); with
  maintenance source, memory norm sustained while off-$\Sigma$ pattern decays
  by 4--6 orders of magnitude.
- **L3**: emotional eigenmode $E_3$ activation $\geq 2\times$ baseline when
  source pumps $E_3$, others decay.
- **L4**: in-Store amplitude persists $\geq 30\%$ of initial with maintenance;
  outside-Store amplitude decays more.
- **L5**: substrate permutation gives trajectory mismatch $< 10^{-6}$;
  edge perturbation gives mismatch at least $100\times$ larger.
- **L6**: untreated trauma steady-state $D \geq 30\%$ of predicted offset;
  healed trajectory steady-state $D < 30\%$ of untreated.
- **L7**: flow $D_I$ at least $2\times$ lower than non-flow $D_I$;
  $\Delta C$ per tick higher in flow.
- **L8**: creative trajectory's rank outside $\mathsf{Read}(\mathsf{Store})$
  at least $3\times$ that of the uncreative trajectory.
- **L9**: $\kappa_{AB}$ for low-variance partner at least $1.5\times$
  high-variance partner.
- **L10**: belief amplitude sustained $\geq 50\%$ of initial under filter;
  $\leq 30\%$ of that when filter removed (belief sign flips).

## Substrate facts confirmed at setup

The script also re-verifies, from scratch, the substrate facts shared with
`closure_demo.py`:

- 120 vertices, uniform degree 12, edge length $1/\varphi$ to 6 digits.
- $\lambda_{\min}(C_\varphi) = \varphi^{-2}$ to 6 digits.
- $\| \tau C_\varphi - C_\varphi \tau \| < 10^{-13}$ (numerical zero).
- $\dim \mathrm{Fix}(\tau) = 116$ for the spectral $\tau$ construction.

## What the demos do NOT do

- They do not claim to be empirical evidence for the phenomenological
  identifications (P-A). They demonstrate that the *structural definitions*
  do what the paper claims they do on the substrate.
- They use the spectral $\tau$ (giving $\dim \Sigma = 116$) rather than the
  full icosian $\tau$ (giving $\dim \Sigma = 94$). Both exhibit the same
  structural shape; the spectral one is faster to construct.
- They do not measure subjective experience or biological correlates.
  Those routes are the experimental falsifiers stated in the paper.

## Dependencies

```
numpy
matplotlib
```

Tested with Python 3.10+.

## Reproducibility

Seed is fixed at 42. All random choices are deterministic given the seed.
Re-running the script reproduces the same numerical results bit-for-bit.

## Files

- `life_demo.py` --- the 10-demo simulation suite
- `requirements.txt` --- pip dependencies
- `output/L*.png` --- one figure per demo (generated)
- `output/life_demo_results.json` --- all numerical results (generated)
