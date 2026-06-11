#!/usr/bin/env bash
# Derivation / consultation invocation for codex (read-only).
#
# This is the complement to scripts/codex_work.sh: codex does NOT edit
# files, only reports structural gaps / derivation paths / attribution
# corrections that the user (or Claude) will then implement.
#
# Use this for:
#   - Gap analysis: what builds are needed to close an open item.
#   - Priority consultation: which of several candidate targets to attack.
#   - Attribution audits: verify where a claim's support actually lives.
#   - insight.md-aware derivation: pull prior session content into play.
#
# The prompt template is calibrated for structured gap reports
# (Section A-F) rather than paper/WO review.
#
# Usage:
#   scripts/codex_derive.sh <task-or-question.md> [--context FILE]... [--focus TEXT]

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
out_dir="$repo_root/docs/codex-derive"
mkdir -p "$out_dir"
out_file="$out_dir/${stem}-${ts}.md"

# Auto-include insight.md if present in repo root and not already in contexts.
insight_path="$repo_root/insight.md"
auto_insight=""
if [[ -f "$insight_path" ]]; then
  already=0
  for c in "${contexts[@]:-}"; do
    if [[ "$c" == *"insight.md" ]]; then already=1; fi
  done
  if [[ $already -eq 0 ]]; then
    auto_insight="$insight_path"
    contexts+=("$insight_path")
  fi
fi

context_block="Task/question spec: $task_path"
for c in "${contexts[@]:-}"; do
  context_block+=$'\n'"Context: $c"
done
if [[ -n "$auto_insight" ]]; then
  context_block+=$'\n'"(insight.md auto-included — Lee's prior session content)"
fi

focus_block=""
if [[ -n "$focus" ]]; then
  focus_block="

Focus this derivation on: $focus"
fi

read -r -d '' prompt <<EOF || true
DERIVATION / CONSULTATION MODE — DO NOT EDIT FILES.

You are the derivation lead in a pair-programmer loop. Claude Code will
implement your output in a separate session afterwards. Your job is to
REPORT GAPS AND DERIVATION PATHS, not to close or downgrade anything.

Repo root: $repo_root

$context_block

Instructions:

1. Read the task spec and all context files in full, including insight.md
   if auto-included — it often contains prior-session content that is not
   yet in any paper (QMS-3, pentagonal holonomy, god-prime decompositions,
   etc.). Cite line numbers when drawing on it.

2. Report format (structured sections):

   SECTION A. Insight / external content relevance. What prior-session or
   literature content (with specific line numbers / citations) is
   directly relevant to this task. Distinguish "already in cascade papers"
   from "only in insight.md or external literature".

   SECTION B. Priority gaps to close the task. For each gap:
   - Name the object/map/lemma/proof required (domain, codomain, type).
   - State what it bridges.
   - Identify the source route: classical literature / new derivation /
     alternative route (name it).
   - Concrete first step (a lemma statement, a sim, a reference to pin
     down).
   Use "B1, B2, ..." numbering so Claude can anchor edits.

   SECTION C. Reversals or corrections to prior rounds (if any). Exact
   string replacements: "at file:N replace X with Y". This lets Claude
   apply surgical fixes.

   SECTION D+ (task-specific). Use additional sections for alternative
   routes (e.g. Route Q vs Route K), sub-builds, or attribution audits.

   SECTION F. Top 3 next builds, ranked, with file:line anchors and the
   mathematical content that goes there.

3. Constraints:
   - READ ONLY. Do not edit any file. Do not commit.
   - Do not mark anything "publication ready".
   - Do not downgrade existing claims to "open"; instead name the build
     that would make them strong.
   - Be concrete: names, types, domains, codomains, citations.
   - If a bridge is genuinely open and no route exists, say so and name
     what would have to be proved. Do not invent.$focus_block
EOF

echo "Codex derive: $task_path"
for c in "${contexts[@]:-}"; do echo "  + context: $c"; done
echo "Writing report to: $out_file"
echo "Sandbox: read-only (codex cannot edit)"
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
echo "Next: Claude builds from this report (scripts/codex_work.sh or direct edits),"
echo "      then fires scripts/review_wo.sh for independent audit."
