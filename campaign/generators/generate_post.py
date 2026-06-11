"""Generate a result-first X post draft (lead post + thread) for a claim.

Usage:  python3 campaign/generators/generate_post.py <slug>
        python3 campaign/generators/generate_post.py --all

Campaign rules enforced here (docs/landing-plan-2026-06.md §3b):
  - one claim per artifact; the thread ladders, the lead post does not
  - code link in the FIRST post
  - no consciousness/unified-reality register on the technical feed
"""
import os
import sys

import lib

BANNED_PHRASES = [
    "breaking", "proof of consciousness", "unified geometry of reality",
    "theory of everything", "multiverse", "recursive truth", "paradigm",
]


def check_register(text, slug):
    lowered = text.lower()
    hits = [p for p in BANNED_PHRASES if p in lowered]
    if hits:
        raise ValueError("%s: banned register phrases in draft: %s" % (slug, hits))


def render(claim):
    links = claim["links"]
    repo = links.get("repo", "")
    repo_line = repo if repo not in ("", "PENDING_PUSH") else "[REPO LINK — BLOCKED, see TODOs]"

    lead = "\n".join([
        claim["post_hook"].strip(),
        "",
        "%s vs %s — %s." % (claim["value"], claim["target"], claim["error"]),
        "",
        "No fitted parameters. Verify it yourself:",
        repo_line,
    ])

    inputs_block = "\n".join("%d. %s" % (i + 1, x) for i, x in enumerate(claim["inputs"]))
    thread = [
        "What goes in (everything, numbered — judge for yourself):\n%s" % inputs_block,
        "How to kill it:\n%s" % claim["falsifier"].strip(),
        "Run it (deps: %s):\n  cd %s\n  %s" % (
            claim["script"].get("deps", "none"),
            claim["script"]["cwd"],
            claim["script"]["cmd"],
        ),
    ]
    if links.get("external"):
        thread.append("Background / independent data: %s" % links["external"])
    if links.get("paper") and "preparation" not in str(links["paper"]):
        thread.append("Full write-up: %s" % links["paper"])

    check_register(lead + " ".join(thread), claim["slug"])

    todos = lib.blocking_todos(claim)
    parts = ["# Post draft: %s" % claim["title"],
             "",
             "segment: %s | status: %s" % (claim["segment"], claim["status"]),
             ""]
    if todos:
        parts.append("## BLOCKED — do these before posting")
        parts.extend("- [ ] %s" % t for t in todos)
        parts.append("")
    parts.append("## Lead post (figure attached: %s)" % ("YES" if claim.get("figure") else "TODO"))
    parts.append("")
    parts.append("```\n%s\n```" % lead)
    parts.append("")
    parts.append("## Thread (one reply per block)")
    for i, t in enumerate(thread, 2):
        parts.append("")
        parts.append("**%d/**\n```\n%s\n```" % (i, t))
    parts.append("")
    parts.append("## Figure")
    parts.append(claim.get("figure", "TODO — idea: %s" % claim.get("figure_idea", "").strip()))
    parts.append("")
    return "\n".join(parts)


def main():
    outdir = lib.ensure_outdir("posts")
    for claim in lib.claims_arg(sys.argv):
        out = os.path.join(outdir, "%s.md" % claim["slug"])
        with open(out, "w") as fh:
            fh.write(render(claim))
        print("wrote %s" % os.path.relpath(out, lib.REPO_ROOT))


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    main()
