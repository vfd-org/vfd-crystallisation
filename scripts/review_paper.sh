#!/usr/bin/env bash
# Non-interactive paper review via Codex CLI (gpt-5.4).
#
# Usage:
#   scripts/review_paper.sh papers/paper-xxx/paper-xxx.tex
#   scripts/review_paper.sh papers/paper-xxix/paper-xxix.tex --focus "LMC derivation"
#
# Output: writes the review to docs/reviews/<paper-stem>-<utc-timestamp>.md
# and also streams it to stdout.

set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "usage: $0 <path-to-paper.tex> [--focus \"area to emphasise\"]" >&2
  exit 2
fi

paper_path="$1"
shift

focus=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --focus)
      focus="$2"; shift 2 ;;
    *)
      echo "unknown arg: $1" >&2; exit 2 ;;
  esac
done

if [[ ! -f "$paper_path" ]]; then
  echo "not a file: $paper_path" >&2
  exit 1
fi

repo_root="$(git -C "$(dirname "$paper_path")" rev-parse --show-toplevel)"
stem="$(basename "$paper_path" .tex)"
ts="$(date -u +%Y%m%dT%H%M%SZ)"
out_dir="$repo_root/docs/reviews"
mkdir -p "$out_dir"
out_file="$out_dir/${stem}-${ts}.md"

focus_block=""
if [[ -n "$focus" ]]; then
  focus_block="

Focus this review on: $focus"
fi

# Review prompt: calibrated for a physics preprint, not code.
read -r -d '' prompt <<EOF || true
You are reviewing a physics preprint in LaTeX. Treat this like a careful
journal-referee pass, not a code review.

Paper path: $paper_path (relative to repo root $repo_root).

Read the file in full, then produce a structured review with the following
sections:

1. **Claim audit**  For every non-trivial claim (theorem, proposition,
   corollary, numerical result), say whether the stated proof actually
   establishes the stated claim. Flag over-claims, hidden assumptions,
   missing hypotheses, or cases where the proof needs more work. Quote the
   specific claim and cite the line number.

2. **Internal consistency**  Identify any place where definitions,
   assumptions, or notation conflict across sections. Check that cross-
   references (\\ref, \\eqref) resolve to what the surrounding text
   implies.

3. **External consistency**  For each claim the paper attributes to another
   paper in this repository (e.g. "Paper XVIII establishes X", "by
   Paper XXIX Theorem 12"), flag the citation and note whether you can
   verify it by reading that paper locally. If you can't find the claim in
   the cited source, say so explicitly.

4. **Tightness**  Identify passages where the tone is stronger than the
   math supports, or weaker than the math supports. Suggest one-line
   edits.

5. **Surface issues**  Typos, undefined macros, broken LaTeX, inconsistent
   capitalisation of technical terms, units/dimensions if relevant.

6. **Top three fixes**  Your ranked list of the most important issues to
   address before this paper is publication-ready. Be specific; cite line
   numbers.

Be direct. Over-claiming is worse than under-claiming. Don't pad. Don't add
a cheerful summary. Write in the register of a hostile-but-fair reviewer.$focus_block
EOF

echo "Reviewing: $paper_path"
echo "Model: gpt-5.4 (from ~/.codex/config.toml)"
echo "Writing review to: $out_file"
echo "---"

# --skip-git-repo-check so codex doesn't complain about the OneDrive path
# being on a Windows filesystem. --full-output to avoid any truncation.
(
  cd "$repo_root"
  codex exec \
    --skip-git-repo-check \
    --sandbox read-only \
    "$prompt"
) | tee "$out_file"

echo "---"
echo "Saved: $out_file"
