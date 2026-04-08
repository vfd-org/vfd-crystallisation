# Publication Architecture Decision

## Architecture Comparison

| Criterion | ARCH A (One paper) | ARCH B (Two paired) | ARCH C (Three-paper) |
|-----------|-------------------|--------------------|--------------------|
| Scientific credibility | Weakened by muon/tau failure inside main claims | Strong: Paper I is complete, Paper II is honest | Over-fragmented |
| Reviewer readability | Long, mixed successes and failures | Clean: each paper has one mission | Too many papers to assess |
| Claim discipline | Forced to hedge throughout | Paper I: strong claims. Paper II: open questions | Diluted |
| Risk of dismissal | High if muon/tau failure dominates | Low: Paper I stands alone | Low but diffuse |
| Coherence | One narrative but uneven | Staged narrative, mutually reinforcing | Fragmented |
| Readiness | Paper I ready; Paper II not | Paper I ready now; Paper II defined | Paper I ready; Papers II+III not |

## RECOMMENDED: ARCH B (Two-Paper Paired Release)

**Rationale:** Paper I is already at a high standard for the baryon-lepton hierarchy. Forcing muon/tau content into it weakens the strongest claims. Paper II has a genuine scientific mission (missing operator), not a patch mission. The pair reads as intentional research programme, not fragmented work.

---

## Paper Definitions

### Paper I: "Particles, Geometry, and Mass from Deterministic Field Closure"

- **One-sentence claim:** A three-order zero-parameter mass law for the baryon-lepton hierarchy, derived from closure-class structure on a phi-manifold, achieves 0.02% structural agreement for the proton-to-electron mass ratio.
- **Proved:** Closure classes, assignment rules, Delta C = 15, graph Laplacian correction, degree-variance refinement, phi^(1265/81) ≈ 1835.8.
- **Tested:** Neutron/proton (compatible), muon/tau (fail — identifies missing layer).
- **Open:** Winding-dependent mass contribution, deeper normalization axiom.
- **Excluded:** Full lepton-generation derivation, general mass theory claims.
- **Role:** The foundation paper. Establishes what works and precisely diagnoses what doesn't.

### Paper II: "Lepton Generations and the Missing Mass Operator in Deterministic Field Closure"

- **One-sentence claim:** The baryon-lepton mass law requires a winding-dependent operator for lepton generations; this paper derives the necessity, constrains its form, and identifies 2^(1/phi) as a structural test of the leading candidate.
- **Proved:** No-go for shell-support-based leptons. Necessity of winding contribution.
- **Tested:** f(w) = a·(w-1)^(1/phi) against tau/muon structure.
- **Open:** Derivation of f(w) from closure geometry. Neutron/proton integration.
- **Excluded:** Modification of Paper I's proton/electron law.
- **Role:** The extension paper. Turns Paper I's limitation into a research target.

---

## Content Allocation Matrix

| Content | Paper I | Paper II | Appendix | Remove |
|---------|---------|----------|----------|--------|
| Closure classes | KEEP | — | — | — |
| R1-R5 | KEEP | Reference | — | — |
| Delta C = 15 | KEEP | Reference | — | — |
| phi-manifold | KEEP | Reference | — | — |
| Metric/energy diagnostic | KEEP | — | — | — |
| Bracketing law | KEEP | — | — | — |
| Graph Laplacian correction | KEEP | Reference | — | — |
| Degree-variance 2nd order | KEEP | Reference | — | — |
| Three-order law phi^(1265/81) | KEEP | Reference | — | — |
| Neutron/proton compatibility | KEEP (brief) | Expand | — | — |
| Muon/tau failures | KEEP (as diagnosis) | EXPAND (as core) | — | — |
| Missing-layer discussion | KEEP (brief) | EXPAND (full) | — | — |
| No-go statement | KEEP (statement) | PROVE (full) | — | — |
| Winding hypothesis | KEEP (mention) | DERIVE/TEST | — | — |
| 2^(1/phi) observation | Paper I appendix | Paper II core | — | — |
| Discarded metrics/maps | — | — | Paper I appendix | — |
| Normalization uniqueness | — | — | Paper I appendix | — |

---

## Release Strategy

- **Simultaneous release** as a paired preprint set
- Same repository, same submission date
- Paper I abstract mentions Paper II: "A companion paper addresses the extension to lepton generations"
- Paper II abstract references Paper I: "Building on the baryon-lepton hierarchy law established in [Paper I]"
- Cross-cited in introductions and conclusions
- The pair should read as **one programme, two stages** — not two independent papers

---

## Claim Discipline

### Paper I

| Level | Claims |
|-------|--------|
| Safe | "derived within framework", "structural agreement at 10^-4 level", "zero fitted continuous parameters" |
| Risky | "established mass law" (qualify with "within framework") |
| Forbidden | "general mass derivation", "exact", "first-principles" without qualification |

### Paper II

| Level | Claims |
|-------|--------|
| Safe | "identifies the missing operator", "derives necessity", "constrains the form" |
| Risky | "solves the lepton generation problem" (only if truly derived) |
| Forbidden | "complete mass theory", "unified derivation" unless fully supported |
