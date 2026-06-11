"""Weekly campaign cycle: rotate to the next claim, regenerate its post draft and
result page, collect KPIs, and write campaign/WEEKLY.md for human review.

Usage:  python3 campaign/run_weekly.py            # advance rotation and build
        python3 campaign/run_weekly.py --dry-run  # rebuild current week, no advance

Nothing here posts anything. The output is a review packet; a human approves
and publishes (landing plan §3b: drafting automated, judgment not).
"""
import datetime
import json
import os
import subprocess
import sys

CAMPAIGN_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(CAMPAIGN_DIR)
STATE = os.path.join(CAMPAIGN_DIR, "state.json")
WEEKLY = os.path.join(CAMPAIGN_DIR, "WEEKLY.md")

sys.path.insert(0, os.path.join(CAMPAIGN_DIR, "generators"))
import lib  # noqa: E402


def load_state():
    if os.path.exists(STATE):
        with open(STATE) as fh:
            return json.load(fh)
    return {"week_index": 0, "history": []}


def run(cmd):
    print("$ %s" % " ".join(cmd))
    subprocess.run(cmd, cwd=REPO_ROOT, check=True)


def main():
    dry = "--dry-run" in sys.argv
    claims = lib.load_registry()
    state = load_state()
    claim = claims[state["week_index"] % len(claims)]
    today = datetime.date.today().isoformat()

    run([sys.executable, "campaign/generators/generate_post.py", claim["slug"]])
    run([sys.executable, "campaign/generators/generate_page.py", claim["slug"]])
    try:
        run([sys.executable, "campaign/kpi/collect_kpis.py"])
        kpi_ok = True
    except subprocess.CalledProcessError:
        kpi_ok = False

    todos = lib.blocking_todos(claim)
    lines = [
        "# Week of %s — claim: %s" % (today, claim["slug"]),
        "",
        "**%s**" % claim["title"],
        "",
        "Segment: %s" % claim["segment"],
        "",
        "## Review packet",
        "- Post draft: `campaign/output/posts/%s.md`" % claim["slug"],
        "- Result page: `campaign/output/pages/%s.html`" % claim["slug"],
        "- Scorecard: `campaign/kpi/SCORECARD.md`%s" % ("" if kpi_ok else " (KPI collection FAILED this run)"),
        "",
        "## Before posting",
    ]
    if todos:
        lines.extend("- [ ] %s" % t for t in todos)
    lines += [
        "- [ ] Read the lead post aloud — register check (no hype words, one claim)",
        "- [ ] Figure attached and legible at timeline size",
        "- [ ] Code link resolves and the command runs clean from a fresh clone",
        "- [ ] Post lead + thread; pin if it is the wave flagship",
        "- [ ] Log any replies from qualified accounts in the scorecard wave gate",
        "",
        "_Rotation: week %d of a %d-claim cycle. Add YAML files to campaign/registry/ to extend._"
        % (state["week_index"] % len(claims) + 1, len(claims)),
        "",
    ]
    with open(WEEKLY, "w") as fh:
        fh.write("\n".join(lines))

    if not dry:
        state["history"].append({"date": today, "slug": claim["slug"]})
        state["week_index"] += 1
        with open(STATE, "w") as fh:
            json.dump(state, fh, indent=2)

    print("\nweekly packet ready: campaign/WEEKLY.md (claim: %s)%s"
          % (claim["slug"], " [dry-run, rotation not advanced]" if dry else ""))
    if todos:
        print("BLOCKED items:")
        for t in todos:
            print("  - %s" % t)


if __name__ == "__main__":
    main()
