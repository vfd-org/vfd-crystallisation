#!/usr/bin/env bash
# Non-interactive work-order review via Codex CLI (gpt-5.4).
#
# Unlike scripts/review_paper.sh (which reviews a single LaTeX preprint),
# this reviews a WO spec together with its derivation and any sim /
# catalogue updates. Reviews are written to docs/reviews/ and also
# streamed to stdout.
#
# Usage:
#   scripts/review_wo.sh <wo-spec.md> \
#       [--derivation <derivation.md>] \
#       [--catalogue <math-catalogue.md>] \
#       [--sim <sim.py>] \
#       [--focus "round N: ..."]
#
# The WO spec is REQUIRED. All other file flags are optional — pass
# whichever artefacts this round should be reviewed against.

set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "usage: $0 <wo-spec.md> [--derivation FILE] [--catalogue FILE] [--sim FILE] [--focus TEXT]" >&2
  exit 2
fi

wo_path="$1"
shift

derivation=""
catalogue=""
sim=""
focus=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --derivation) derivation="$2"; shift 2 ;;
    --catalogue)  catalogue="$2";  shift 2 ;;
    --sim)        sim="$2";        shift 2 ;;
    --focus)      focus="$2";      shift 2 ;;
    *) echo "unknown arg: $1" >&2; exit 2 ;;
  esac
done

if [[ ! -f "$wo_path" ]]; then
  echo "not a file: $wo_path" >&2
  exit 1
fi

repo_root="$(git -C "$(dirname "$wo_path")" rev-parse --show-toplevel)"
stem="$(basename "$wo_path" .md)"
ts="$(date -u +%Y%m%dT%H%M%SZ)"
out_dir="$repo_root/docs/reviews"
mkdir -p "$out_dir"
out_file="$out_dir/${stem}-${ts}.md"

# Build the artefact list block for the prompt.
artefacts="WO spec (REQUIRED): $wo_path"
[[ -n "$derivation" ]] && artefacts+=$'\n'"Derivation: $derivation"
[[ -n "$catalogue"  ]] && artefacts+=$'\n'"Math catalogue: $catalogue"
[[ -n "$sim"        ]] && artefacts+=$'\n'"Sim / implementation: $sim"

focus_block=""
if [[ -n "$focus" ]]; then
  focus_block="

Focus this round on: $focus"
fi

read -r -d '' prompt <<EOF || true
You are reviewing a work order (WO) and its current artefacts inside a
physics / mathematical-biology research programme. This is NOT a LaTeX
preprint — it's a WO spec plus an in-progress mathematical derivation,
optionally with a sim and a math-catalogue ledger.

Repo root: $repo_root

Artefacts to review (read each file fully before reporting):
$artefacts

The WO spec declares goals, acceptance criteria, and open items. The
derivation is the mathematical content. The catalogue should list every
new definition, lemma, theorem, conjecture, and computational result
introduced. The sim (if present) should implement a computable claim
from the derivation. Your job is to catch substantive problems before
they ossify.

Produce a structured review with the following sections:

1. **Claim audit** — For every non-trivial mathematical claim in the
   derivation (definition, lemma, theorem, conjecture, numerical
   result), say whether the stated argument actually establishes the
   stated claim. Flag over-claims, hidden assumptions, missing
   hypotheses. Quote the claim and cite file:line.

2. **WO acceptance audit** — For each numbered acceptance criterion
   and each numbered open item in the WO spec, say whether the current
   artefacts resolve it, partially resolve it, or do not touch it.
   Missing items matter as much as wrong items.

3. **Catalogue audit** — Check the math-catalogue (if supplied) against
   the derivation. Every D/L/T/C/N referenced in the derivation should
   appear in the catalogue with correct status. Any catalogue entry
   not backed by the derivation is a defect. Any derivation object
   (definition, lemma, ...) that is not catalogued is a defect.

4. **Attribution / external consistency** — For each claim the
   artefacts attribute to another file in this repo (e.g. "by
   cascade-bio.md §B3", "by paper-xxxii Theorem F"), verify locally
   that the cited source says what the artefact claims it says. If
   you cannot find the claim in the cited source, say so.

5. **Sim correctness** (only if sim is supplied) — Does the sim
   actually implement the claim the derivation says it does? Are
   there bugs? Are the statistical comparisons (χ², KL, ...) set up
   correctly? Is the null hypothesis chosen honestly?

6. **Tightness** — Passages where tone is stronger / weaker than math
   supports. One-line edits welcome.

7. **Top three fixes** — Ranked, specific, with file:line.

8. **Verdict** — "Publication ready: yes" or "Publication ready: no".
   Base this ONLY on substantive math / attribution / sim-correctness
   must-fix items. Surface LaTeX / typo issues do NOT gate the verdict.

Be direct. Over-claiming is worse than under-claiming. Don't pad.
Don't add a cheerful summary. Write as a hostile-but-fair reviewer.$focus_block
EOF

echo "Reviewing WO: $wo_path"
[[ -n "$derivation" ]] && echo "  + derivation: $derivation"
[[ -n "$catalogue"  ]] && echo "  + catalogue:  $catalogue"
[[ -n "$sim"        ]] && echo "  + sim:        $sim"
echo "Writing review to: $out_file"
echo "---"

(
  cd "$repo_root"
  codex exec \
    --skip-git-repo-check \
    --sandbox read-only \
    "$prompt"
) | tee "$out_file"

echo "---"
echo "Saved: $out_file"
