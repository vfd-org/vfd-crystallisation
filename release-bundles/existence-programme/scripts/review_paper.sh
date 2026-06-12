#!/usr/bin/env bash
# Codex review for an existence-programme paper (workspace-aware).
#
# Usage:
#   scripts/review_paper.sh papers/01-existence-as-closure/main.tex --focus "round 1"
#
# Output: writes review to docs/reviews/<paper-stem>-<utc-timestamp>.md
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "usage: $0 <path-to-paper.tex> [--focus \"area\"]" >&2
  exit 2
fi

paper_path="$1"; shift
focus=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --focus) focus="$2"; shift 2 ;;
    *) echo "unknown arg: $1" >&2; exit 2 ;;
  esac
done

if [[ ! -f "$paper_path" ]]; then
  echo "not a file: $paper_path" >&2
  exit 1
fi

BUNDLE_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
stem="$(basename "$(dirname "$paper_path")")"
ts="$(date -u +%Y%m%dT%H%M%SZ)"
out_dir="$BUNDLE_ROOT/docs/reviews"
mkdir -p "$out_dir"
out_file="$out_dir/${stem}-${ts}.md"

focus_block=""
if [[ -n "$focus" ]]; then
  focus_block="

Focus this review on: $focus"
fi

read -r -d '' prompt <<EOF || true
You are reviewing a paper within the Existence Programme: a coordinated
10-paper body of work on existence-as-recursive-geometric-closure. Treat
this like a careful journal-referee pass, not a code review.

THE PROGRAMME (for context):
  01 Existence as Closure --- foundation: distinction, closure operator
     C_phi = L_{V_600} + phi^-2 I on V_600 substrate, sigma-twist tau,
     bounded reference frames, per-frame zero-line Sigma_I, complexity
     hierarchy. 7 sim demos D1-D7, frozen predictions F1-F10.
  02 Life as Closure --- human bridge: living-frame definition
     I_life = (O, C_O, B, M, A, Sigma_I) + 18 derived structural objects
     covering boundary, repair, memory, agency, relevance, dyscoherence,
     emotions, thoughts, qualia, purpose, joint meaning, identity, trauma,
     flow, creativity, hope, trust, self-deception. 13 sim demos L1-L13,
     frozen predictions P1-P15. Real-data anchored via SL-002, SL-005.
  03 From Processing to Point of View --- neuroscience: Levin bioelectric
     bridge + CEMI cortical EM bridge + sleep/anaesthesia thermodynamics.
     3 sim demos B1-B3.
  04 Cosmic Self-Pruning and Frame Recurrence --- cosmology extension:
     frame dynamics + recurrence + pruning + universe-as-frame-at-totality
     (held back from v1.0). 5 sim demos C1-C5.
  05 Bioelectric Closure (Solution Lab 001) --- BETSE planarian methodology
     + R_cl 5-term residual + 5 preregistered wet-lab predictions.
  06 Cortical Phase Closure (Solution Lab 002) --- propofol EEG; 14/14
     positive on ds005620, sLORETA replication, cross-cohort ds004541
     7/7. Empirical anchor for CEMI bridge.
  07 Closure-as-Distance (cross-substrate) --- applicability diagnostic
     CAD-D1-D5-v1; 14/15 substrates correctly classified.
  08 Trauma Cortical Closure (Solution Lab 005) --- ds007609 trait anxiety
     d=+0.79; first real-data extension of SL-002 methodology to chronic-
     clinical-state cohort. Diagnostic predicted PASS a priori.
  09 Flow Cortical Closure (Solution Lab 006) --- FlowIndex-v1 metric;
     synthetic 5/5 PASS; ds005520 MOBA-gaming analysis in progress.
  10 Hyperscanning Joint Meaning (Solution Lab 007) --- ds007471 musical
     joint-action honest negative d_z=+0.23; diagnostic CORRECTLY
     PREDICTED FAIL a priori (D2=0, D3=0.62).

The framework's discipline is bounded: structural propositions are formal;
phenomenological readings are conditional on the Access Principle (P-A);
empirical bridges are scoped by the CAD-D1-D5-v1 applicability diagnostic;
the cosmic recurrence claims (Paper 04) are conditional on H-rec / H-evolve
and held back.

Paper path: $paper_path

Read the file in full, then produce a structured review:

1. **Claim audit**  For every non-trivial claim (theorem, proposition,
   conditional proposition, numerical result), say whether the stated
   proof actually establishes the stated claim. Flag over-claims, hidden
   assumptions, missing hypotheses, or cases where the proof needs more
   work. Quote the specific claim and cite the line number.

2. **Internal consistency**  Identify places where definitions, assumptions,
   or notation conflict across sections.

3. **External consistency with the programme**  For each cross-paper claim,
   verify it matches what the cited companion paper actually says.
   Specifically flag any claim about another programme paper that needs
   tightening, and any place where this paper undersells or overclaims
   its relationship to companion papers.

4. **Narrative coherence with the 9 other papers**  Does this paper's
   framing, scope, and vocabulary cohere with the rest of the programme?
   Where could the narrative be tightened so the 10-paper body reads as
   one coherent work rather than 10 separate documents? Be specific: cite
   sentences that conflict with other-paper framings.

5. **Tightness**  Passages where tone is stronger than the math supports,
   or weaker than the math supports. Suggest one-line edits.

6. **Surface issues**  Typos, undefined macros, broken LaTeX, inconsistent
   capitalisation of technical terms, units/dimensions if relevant.

7. **Top three fixes**  Your ranked list of the most important issues to
   address before this paper is publication-ready in the context of the
   ten-paper programme. Be specific; cite line numbers.

8. **Programme-strengthening recommendations**  At least 3 concrete
   recommendations specific to this paper that would make the entire
   10-paper programme stronger. Examples: cross-references to add,
   conventions to align, framing moves to adopt across the programme.

9. **Publication ready?**  Yes/no on the substantive-math/attribution
   scope. Be direct. Over-claiming is worse than under-claiming.$focus_block
EOF

echo "Reviewing: $paper_path"
echo "Writing review to: $out_file"
echo "---"

(
  cd "$BUNDLE_ROOT"
  codex exec \
    --skip-git-repo-check \
    --sandbox read-only \
    "$prompt"
) | tee "$out_file"

echo "---"
echo "Saved: $out_file"
