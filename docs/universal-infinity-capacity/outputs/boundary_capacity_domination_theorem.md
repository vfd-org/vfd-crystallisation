# Boundary Capacity Domination Theorem (template)

**Template.** Let `X` be a state space with completion boundary `∂X`, `H` a positive
capacity form, `R` a reflection form. If
1. `H` is positive and self-adjoint,
2. `R` is `H`-bounded,
3. `K = H^{−1/2}RH^{−1/2}` exists and is bounded,
4. boundary leakage `L` is controlled (no escape at `∂X`),
5. `‖K‖ ≤ 1`,
then `Q = H − R ≥ 0` and the boundary is stable.

**Domain meanings of condition 5:** RH → Weil positivity (open); BH → no-superradiance
(physics); brain → Lyapunov stability (analogy); VFD → closure stability (analogy).

**Honest status.** Conditions 1–4 are the analytic *setup*; **condition 5 is the content**,
and in each domain it is a *separate* theorem or empirical fact — the template does **not**
supply it. Because the algebra is generic (holds for any PSD `H`+sym `R`), the template is
an organizing schema, not a proof engine. For RH, condition 5 in the infinite limit **is**
RH (Connes/Weil); the template does not advance it.
