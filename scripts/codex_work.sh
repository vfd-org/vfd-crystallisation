#!/usr/bin/env bash
# Forward-invocation script for codex (pair-programmer mode).
#
# Unlike scripts/review_paper.sh and scripts/review_wo.sh (read-only
# critique), this script grants workspace-write so codex can edit files,
# create new artefacts, run sims. Codex model + reasoning effort come
# from ~/.codex/config.toml (currently gpt-5.5 xhigh).
#
# Intended workflow:
#   1. Write a task spec as a short markdown file describing goal,
#      acceptance criteria, context, constraints.
#   2. Run this script. Codex edits files in place and prints a
#      summary to stdout (also captured to docs/codex-work/).
#   3. Claude Code (or the user) reviews git diff + the summary.
#   4. For math/derivation outputs, run scripts/review_wo.sh on the
#      new artefacts as an independent codex-reviews-codex audit.
#
# Usage:
#   scripts/codex_work.sh <task-spec.md> [--context FILE]... [--focus TEXT]
#
# The task spec is REQUIRED. --context may be given multiple times to
# point codex at supporting files. --focus optionally narrows the round.

set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "usage: $0 <task-spec.md> [--context FILE]... [--focus TEXT]" >&2
  exit 2
fi

task_path="$1"
shift

contexts=()
focus=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --context) contexts+=("$2"); shift 2 ;;
    --focus)   focus="$2"; shift 2 ;;
    *) echo "unknown arg: $1" >&2; exit 2 ;;
  esac
done

if [[ ! -f "$task_path" ]]; then
  echo "not a file: $task_path" >&2
  exit 1
fi

repo_root="$(git -C "$(dirname "$task_path")" rev-parse --show-toplevel)"
stem="$(basename "$task_path" .md)"
ts="$(date -u +%Y%m%dT%H%M%SZ)"
out_dir="$repo_root/docs/codex-work"
mkdir -p "$out_dir"
out_file="$out_dir/${stem}-${ts}.md"

context_block="Task spec (READ FULLY): $task_path"
for c in "${contexts[@]}"; do
  context_block+=$'\n'"Context file: $c"
done

focus_block=""
if [[ -n "$focus" ]]; then
  focus_block="

Focus this round on: $focus"
fi

read -r -d '' prompt <<EOF || true
You are leading a pair-programmer loop in a physics / mathematical-biology
research programme. The other agent (Claude Code) will review your output
in a separate session afterwards. You do the work; the reviewer grades.

Repo root: $repo_root

$context_block

Instructions:

1. Read the task spec and all listed context files in full before editing.
2. Edit files directly in the workspace. Create new files where they
   genuinely belong (e.g. a new derivation note, a new sim script).
3. If the task involves a mathematical claim or numerical result, write
   or extend a script that produces it, so the claim can be independently
   re-run. Sim correctness matters.
4. Be conservative. Conditional claims are better than over-claimed ones.
   Cite sources where you have them (file:line is ideal). Flag uncertainty
   where you don't. Downgrade to "working note" / "conjecture" rather
   than "theorem" if the argument doesn't fully close.
5. Do NOT mark anything "publication ready" — that is the reviewer's call.
6. Do NOT commit, push, or touch git state. Just edit working-tree files.
7. When you are done, print a concise summary to stdout:
   - Files you edited, with line counts and one-line per-file purpose.
   - Files you created, same format.
   - Key decisions you made and the reason.
   - Residual uncertainty or caveats for the reviewer.
   - Open sub-questions you hit but did not address.

Direct voice. No padding. No cheerful wrap-up.$focus_block
EOF

echo "Codex work: $task_path"
for c in "${contexts[@]}"; do echo "  + context: $c"; done
echo "Writing summary to: $out_file"
echo "Sandbox: workspace-write (codex can edit files)"
echo "Model / effort: from ~/.codex/config.toml"
echo "---"

(
  cd "$repo_root"
  codex exec \
    --skip-git-repo-check \
    --sandbox workspace-write \
    "$prompt"
) | tee "$out_file"

echo "---"
echo "Saved: $out_file"
echo "Review hints:"
echo "  git diff --stat      # see what changed"
echo "  git diff             # inspect edits"
echo "  scripts/review_wo.sh <new-artefact> --focus '...'  # independent audit"
