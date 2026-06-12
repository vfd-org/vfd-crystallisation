# Status Taxonomy

Every non-trivial claim in this programme is classified as exactly one of:

| Status | What it means | Example |
|---|---|---|
| **Theorem / Definition** | Formal structural claim under stated assumptions. Has a proof or a definition. Holds independently of empirical interpretation. | Paper I Theorem fix-tau-94: $\dim \mathrm{Fix}(\tau_{\mathrm{ico}}) = 94$ unconditionally. |
| **Conditional Proposition** | Bridge claim depending on a named hypothesis (H-RP-1/2/3, P-A, P-A-spectral, H-evolve, H-rec, substrate mapping, or empirical interpretation). Holds under the hypothesis, not without. | Paper III Conditional Proposition on CEMI bridge under H-RP-2 and P-A. |
| **Empirical Result** | Completed data analysis with stated effect size and significance. | Note B: ds005620 propofol $n = 14$, $14/14$ positive, $t = 7.11$, $d_z = 1.90$. |
| **Empirical Proxy** | Measurable first-order approximation to a structural object, not the operator itself. Licensed only under its stated applicability diagnostic. | Note C: closure-as-distance is a proxy for distance-to-closure-stable-reference, licensed by CAD-D1–D5-v1. |
| **Pre-registered Proposal** | Future test, frozen script + thresholds, not yet executed. Not evidence. | Note A: 5 preregistered DiBAC4(3) planarian wet-lab predictions. Note D: PTSD pre/post-therapy longitudinal EEG. |

## Reviewer guidance

If a reader feels a claim is "stronger than it should be", check which
status the paper assigns to it. The most common issues to look for:

- A **proxy** result described as if it were a **theorem** (e.g., closure-as-distance is the formal operator).
- An **empirical result** described as if it **proved** a conditional proposition (e.g., SL-002 propofol "proves" CEMI is the carrier of consciousness).
- A **pre-registered proposal** treated as evidence (e.g., PTSD pre/post therapy "supports" the trauma claim).
- A **conditional proposition** stated unconditionally (e.g., "qualia are spectral signatures" — should be "under P-A and P-A-spectral, qualia correspond to spectral signatures").

## Conventions

- Theorems use the `theorem` LaTeX environment.
- Conditional Propositions use the `conditional` environment.
- Empirical Results are reported in the abstract, results sections, and tables; not in theorem environments.
- Empirical Proxies are introduced with explicit "first-order proxy" or "measurable approximation" language.
- Pre-registered Proposals appear in falsifier sections, limitations, and the roadmap document.

## Where this taxonomy is enforced

- Every paper and note has a status-taxonomy block after `\end{abstract}`.
- The programme overview repeats the taxonomy.
- The CHANGELOG records theorem-to-conditional demotions across the
  Round 1–5 codex review iterations.
