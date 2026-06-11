# TASK: Align kernel-spine documents to b-anomaly shipped repo

**Date:** 2026-04-29.
**Pair-programmer pattern:** codex_derive (WO) → Claude implements → review_wo (audit).
**Bar:** "complete + undismissable" per `feedback_credibility_bar.md`. Hostile-review ready. No over-claim, no under-claim. No retreat-to-conditional unless explicitly motivated.
**Mathematical-framing discipline:** per `feedback_mathematical_framing_discipline.md`. Math stays load-bearing; interpretive framing is closing-subsection only.

---

## 1. Background

The b-anomaly repository (`/mnt/c/Users/nexus/OneDrive/Documents/My Projects/BANOMALY-001/vfd-b-anomaly/`) is shipped with `paper/main.pdf` + 10 sections + repro pipeline. Its headline result is a **5-dataset sign-uniform structural pass with no shape retuning**, with an **honest AIC tie** with the `FREE_C9` constant-Wilson-coefficient model. The kernel involved is the φ-regularised closure operator $C_\varphi = L_M + \varphi^{-2} I$ on the 600-cell substrate $V_{600}$.

The same kernel $C_\varphi$ appears across the cascade-derivation programme:
- `papers/adaptive-closure-transport/adaptive-closure-transport.tex` — passive regime ≡ b-anomaly setting; active regime is the missing aria-chess-paper companion.
- `docs/aria-closure-kernel.md` — canonical kernel-spine doc, lists family members across all six Millennium drafts.
- `papers/millennium-{rh,bsd,ns,ym,hodge,pnp}-formal/*.tex` — each cites the family.
- `docs/closure-cosmogenesis.md`, `docs/projection-narrative.md`, `docs/rh-cascade-closure-dynamics.md`, `docs/fractal-cascade-projection.md` — programme-level layered documents.

The b-anomaly result is the **first independent passive-regime empirical landing** for $C_\varphi$. Through the shared cocycle $\kappa(v) = (s(v) - 4)^2$, it bridges to the prime-number-object work (ẑ pentagonal-clock factorisation, soul-prime Π₀, observer-zeta).

Currently the kernel-spine doc cites only the single-dataset Layer-1/2/3 derivation (wo007/wo008 reports, $r=0.983$, ΔAIC = −0.28); the now-shipped b-anomaly paper has a **5-dataset universality claim** that is structurally distinct from a single-dataset r-correlation. Adaptive-closure-transport.tex still flags the witness as "external, unaudited" — stale framing.

---

## 2. What this task closes

Three phases of alignment, each producing edited files. **No new theorems are introduced.** The work is documentation-spine alignment + scope-discipline tightening:

### 2.1 Phase 1 — Kernel-spine doc (`docs/aria-closure-kernel.md`)

- **§4 Empirical validation**: Replace the single-dataset framing (wo007/wo008) with the 5-dataset universality framing. Include:
  - Headline: 5-dataset sign-uniform structural pass with one fixed kernel shape.
  - Per-dataset table: LHCb 2015 ($B^0\!\to\!K^{*0}$), LHCb 2021 ($B^+\!\to\!K^{*+}$), CMS 2025 ($B^0\!\to\!K^{*0}$, no $P_4'$), LHCb 2025 ($B^0\!\to\!K^{*0}$), LHCb 2015 ($B_s\!\to\!\phi$, $S$-basis). Columns: $n$, non-linear $\Delta\mathrm{AIC}$, best-fit $A$, $\Delta C_9^{\mathrm{eff}}$. Numbers verbatim from `BANOMALY-001/vfd-b-anomaly/README.md`.
  - Honest AIC caveat: stacked $w_{\mathrm{VFD}} = 0.348$ vs $w_{\mathrm{FREE\_C9}} = 0.652$. Kernel and constant-shift statistically indistinguishable on current data.
  - Geometry-first variant test: unweighted choice wins on pure-geometry criterion *independently* of LHCb data; same variant wins on data $\chi^2$.
  - Linearised-vs-nonlinear caveat: Mode B → $+2.77$ AIC unit drift; the largest single methodological uncertainty.
  - Cross-channel basis: $K^*$ vs $\phi$ amplitudes consistent with Krüger-Matias $P$/$S$ basis amplification ($\sim 2.2\times$, with $\sim 50\%$ residual overshoot).
  - Cocycle convergence: keep the existing observation that $V_m = \varphi^{m^2}$ on shells = κ(v) = $(s(v) - 4)^2$ used in `rh-formal.tex`'s pentagonal clock.

- **§6 Response vs selection**: Update from "selection layer is open" to:
  - Passive-regime empirical landing **shipped** via b-anomaly (with clear scope: structural test, not detection).
  - Active-regime companion (aria-chess paper) **named, not yet written**.
  - The convergence of the gap across RH H_attr / ACT / ARIA frames remains the strongest single-problem evidence.
  - **Do not claim** b-anomaly attacks RH directly. The cocycle convergence is structural; ẑ is a new class, not classical ζ.

- **§7 Canonical references**: Replace the wo007/wo008-specific entries with the b-anomaly paper as primary (`/BANOMALY-001/vfd-b-anomaly/paper/main.pdf`), keeping wo007/wo008 as supporting layer references.

### 2.2 Phase 2 — Cross-paper alignment

- **`adaptive-closure-transport.tex` §sec:aria_home (lines 394-434)**: Replace the "external, unaudited empirical witness ($r \approx 0.98$)" framing with current-state framing:
  - The witness exists, is shipped, and has its own internal stress-test programme (b-anomaly paper §5).
  - 5-dataset universality is the actual claim; $r=0.98$ is one slice of it.
  - The witness is for the **passive-regime** specifically (Fact 3.1 / passive regime, $G \equiv 0$).
  - Active-regime witness for the framework's selection statement is **not** delivered by b-anomaly; aria-chess companion paper is the active-regime target.
  - Honest AIC tie language must propagate.

- **`papers/realisation/realisation.tex`**: Add b-anomaly to the empirical-landing register. Frame as Class-E3 passive-regime witness (per `cascade-empirical-grounding.md`). Distinct from aria-chess preregistered hits (cognitive-substrate witnesses).

- **`papers/cascade-derivation/cascade-empirical-grounding.md`**: Add §0 "Witness extension to flavour physics" or new §1.x for b-anomaly as Class-E3 passive-regime witness for $C_\varphi$. Pair with the aria-chess Class-E3 cognitive-substrate witnesses already documented.

### 2.3 Phase 3 — Prime-object bridge

- **`docs/rh-cascade-closure-dynamics.md`**: Add a subsection noting that $C_\varphi$ now has independent flavour-physics empirical witness via b-anomaly. ẑ inherits via the shared cocycle κ. **Do NOT** claim b-anomaly attacks classical RH. The strengthening is at the kernel-operator level only; the new-analytic-class status of ẑ is preserved.

- **`docs/fractal-cascade-projection.md`**: Strengthen "ẑ as κ-compression trace" by noting κ has independent flavour-physics witness. Preserve all existing scope discipline (A-B σ-fixed vs σ-paired, God Prime κ-fixed-point as conjecture, not theorem).

- **`docs/projection-narrative.md`**: Layer 1 (mainstream coherence) gets explicit empirical landing through 5 LHCb datasets. Strengthens the case that Layer 2 realisation is earned. Preserve the "load-bearing order" discipline.

---

## 3. Acceptance criteria

For each phase:

**AC1.** Every numerical claim (n, ΔAIC, A, ΔC_9^eff, w_VFD, w_FREE_C9) is verbatim from `BANOMALY-001/vfd-b-anomaly/README.md` or `paper/sections/*.tex`. No round-up, no paraphrase.

**AC2.** No claim is stronger than the b-anomaly paper itself claims. In particular:
- Structural test = pass.
- AIC preference = tie (not preference).
- The kernel is **not** the unique q²-shape consistent with the anomaly (free-width Gaussian charm-loop proxy fits comparably with one extra param).
- Linearised "Mode B" preference did not survive non-linear refit; the +2.77 drift is the largest methodological uncertainty.

**AC3.** Cocycle bridge to ẑ is preserved as the structural connection, but does NOT claim that b-anomaly empirically witnesses ẑ or RH. The kernel has new empirical evidence; ẑ inherits only at the operator-level structural sense.

**AC4.** Active-regime / selection layer remains explicitly open. Aria-chess paper is named as the next empirical landing, not delivered.

**AC5.** Hostile-review test: every paragraph pointing at b-anomaly should survive a referee asking "is this what the b-anomaly paper actually claims, or what you wish it claimed?" Cite directly from the b-anomaly paper or its README.

**AC6.** Mathematical-framing discipline: the load-bearing math in each affected paper does not lean on b-anomaly empirical strength. b-anomaly is interpretive context, not a step in any proof.

---

## 4. Open items NOT in scope

- **Aria-chess paper draft (Phase 4 of the original plan).** Active-regime empirical companion. Multi-day work; explicit user go-ahead needed before starting.
- **Edge-space decomposition of $\R^{E_M}$ under $2I$ action** (open item 6 of adaptive-closure-transport.tex). Genuine math, not addressed here.
- **Lyapunov derivation from closure functional $\mathcal{F}$** (open item 1 of adaptive-closure-transport.tex). Genuine math, not addressed here.
- **B-anomaly paper itself.** Already shipped; do not re-edit.

---

## 5. Codex derive prompt

Read this TASK file plus the following context files:
- `BANOMALY-001/vfd-b-anomaly/README.md` (headline + table)
- `BANOMALY-001/vfd-b-anomaly/paper/main.tex` (paper structure)
- `BANOMALY-001/vfd-b-anomaly/paper/sections/04_results.tex` (per-dataset results)
- `BANOMALY-001/vfd-b-anomaly/paper/sections/05_stress_tests.tex` (Akaike + nonlinear refit caveats)
- `BANOMALY-001/vfd-b-anomaly/paper/sections/09_limitations.tex` (honest scope)
- `vfd-crystalisation-paper/docs/aria-closure-kernel.md` (current state of canonical kernel doc)
- `vfd-crystalisation-paper/papers/adaptive-closure-transport/adaptive-closure-transport.tex` (current state of theory paper, esp. §sec:aria_home)
- `vfd-crystalisation-paper/papers/cascade-derivation/cascade-empirical-grounding.md` (existing empirical-grounding doc)
- `vfd-crystalisation-paper/docs/rh-cascade-closure-dynamics.md` (prime-object spine)
- `vfd-crystalisation-paper/docs/fractal-cascade-projection.md` (κ-compression-trace context)
- `vfd-crystalisation-paper/docs/projection-narrative.md` (Layer 1/Layer 2 epistemology)

**For each phase 1/2/3, produce a numbered build list (B1, B2, …)** with:
- target file:line anchor
- exact replacement string (or new section content) — within reasonable size
- rationale tied to specific b-anomaly claim verbatim
- the AC# it discharges

**Flag any drift / hidden over-claim risk** in the proposed edits before they happen. Hostile-review framing.

**Do not propose** to change the b-anomaly repo itself, change adaptive-closure-transport's load-bearing math, or extend to the active-regime aria-chess paper.

**Top-3 risk register** for the alignment as a whole — what are the three most likely places the alignment edits could over-claim or drift, and how to guard against each.
