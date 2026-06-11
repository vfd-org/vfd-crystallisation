"""Collect campaign KPIs: GitHub repo stats (+traffic with token) and X account stats.

Usage:  python3 campaign/kpi/collect_kpis.py

Writes a dated JSON snapshot to campaign/kpi/history/ and regenerates
campaign/kpi/SCORECARD.md with deltas vs the previous snapshot.

KPIs are conversions, not likes (landing plan §3b): clones/visitors need a
GITHUB_TOKEN with push access (export GITHUB_TOKEN=...); stars/forks/issues and
X followers/engagement work unauthenticated.
"""
import datetime
import json
import os
import re
import sys
import urllib.error
import urllib.request

KPI_DIR = os.path.dirname(os.path.abspath(__file__))
HISTORY_DIR = os.path.join(KPI_DIR, "history")
SCORECARD = os.path.join(KPI_DIR, "SCORECARD.md")

GITHUB_USER = "vfd-org"
X_HANDLE = "VFD_org"
# Repos whose traffic (clones/views) we track — the campaign conversion surface.
TRACKED_REPOS = [
    "vfd-crystallisation",
    "icosian-rh-geometric",
    "icosian-closure-object",
    "hypersphere-cosmology",
    "the-24-600-spectral-bridge",
    "existence-life-closure-programme",
]
UA = {"User-Agent": "Mozilla/5.0 (campaign-kpi-collector)"}


def fetch(url, headers=None, timeout=30):
    req = urllib.request.Request(url, headers=dict(UA, **(headers or {})))
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def github_snapshot():
    token = os.environ.get("GITHUB_TOKEN", "")
    auth = {"Authorization": "token %s" % token} if token else {}
    repos, page = [], 1
    while True:
        url = "https://api.github.com/users/%s/repos?per_page=100&page=%d" % (GITHUB_USER, page)
        batch = json.loads(fetch(url, auth))
        if not batch:
            break
        repos.extend(batch)
        page += 1

    snap = {
        "repo_count": len(repos),
        "stars_total": sum(r["stargazers_count"] for r in repos),
        "forks_total": sum(r["forks_count"] for r in repos),
        "open_issues_total": sum(r["open_issues_count"] for r in repos),
        "top_repos": sorted(
            [{"name": r["name"], "stars": r["stargazers_count"], "forks": r["forks_count"]}
             for r in repos], key=lambda x: -x["stars"])[:8],
        "traffic": {},
    }
    if token:
        for name in TRACKED_REPOS:
            try:
                clones = json.loads(fetch(
                    "https://api.github.com/repos/%s/%s/traffic/clones" % (GITHUB_USER, name), auth))
                views = json.loads(fetch(
                    "https://api.github.com/repos/%s/%s/traffic/views" % (GITHUB_USER, name), auth))
                snap["traffic"][name] = {
                    "clones_14d": clones.get("count", 0),
                    "unique_cloners_14d": clones.get("uniques", 0),
                    "views_14d": views.get("count", 0),
                    "unique_visitors_14d": views.get("uniques", 0),
                }
            except urllib.error.HTTPError as err:
                snap["traffic"][name] = {"error": "HTTP %s" % err.code}
    else:
        snap["traffic_note"] = "set GITHUB_TOKEN (push access) to collect clones/visitors"
    return snap


def x_snapshot():
    """Scrape the public syndication timeline; parse defensively with regex."""
    url = ("https://syndication.twitter.com/srv/timeline-profile/screen-name/%s"
           % X_HANDLE)
    try:
        page = fetch(url)
    except Exception as err:  # endpoint is flaky; never fail the whole run
        return {"error": str(err)}

    def first_int(pattern):
        m = re.search(pattern, page)
        return int(m.group(1)) if m else None

    favs = [int(x) for x in re.findall(r'"favorite_count":(\d+)', page)]
    rts = [int(x) for x in re.findall(r'"retweet_count":(\d+)', page)]
    replies = [int(x) for x in re.findall(r'"conversation_count":(\d+)', page)]

    def stats(xs):
        if not xs:
            return None
        xs = sorted(xs)
        return {"n": len(xs), "median": xs[len(xs) // 2],
                "mean": round(sum(xs) / len(xs), 1), "max": xs[-1]}

    return {
        "followers": first_int(r'"followers_count":(\d+)'),
        "posts_total": first_int(r'"statuses_count":(\d+)'),
        "recent_likes": stats(favs),
        "recent_retweets": stats(rts),
        "recent_replies": stats(replies),
    }


def load_previous():
    if not os.path.isdir(HISTORY_DIR):
        return None
    snaps = sorted(f for f in os.listdir(HISTORY_DIR) if f.endswith(".json"))
    if not snaps:
        return None
    with open(os.path.join(HISTORY_DIR, snaps[-1])) as fh:
        return json.load(fh)


def delta(cur, prev):
    if cur is None or prev is None:
        return ""
    d = cur - prev
    return " (%+d)" % d if d else " (=)"


def write_scorecard(snap, prev):
    gh, x = snap["github"], snap["x"]
    pgh = (prev or {}).get("github", {})
    px = (prev or {}).get("x", {})
    lines = [
        "# Campaign scorecard — %s" % snap["date"],
        "",
        "Conversions first (clones / unique visitors), reach second. Likes are not a KPI.",
        "",
        "## GitHub",
        "- Stars total: %s%s" % (gh["stars_total"], delta(gh["stars_total"], pgh.get("stars_total"))),
        "- Forks total: %s%s" % (gh["forks_total"], delta(gh["forks_total"], pgh.get("forks_total"))),
        "- Open issues (engagement!): %s%s" % (
            gh["open_issues_total"], delta(gh["open_issues_total"], pgh.get("open_issues_total"))),
        "",
    ]
    if gh["traffic"]:
        lines.append("| repo | clones 14d | uniq cloners | views 14d | uniq visitors |")
        lines.append("|---|---|---|---|---|")
        for name, t in gh["traffic"].items():
            if "error" in t:
                lines.append("| %s | %s | | | |" % (name, t["error"]))
            else:
                lines.append("| %s | %s | %s | %s | %s |" % (
                    name, t["clones_14d"], t["unique_cloners_14d"],
                    t["views_14d"], t["unique_visitors_14d"]))
    else:
        lines.append("_%s_" % gh.get("traffic_note", "no traffic data"))
    lines += ["", "## X (@%s)" % X_HANDLE]
    if "error" in x:
        lines.append("_syndication endpoint failed: %s_" % x["error"])
    else:
        lines.append("- Followers: %s%s" % (x["followers"], delta(x["followers"], px.get("followers"))))
        for key, label in [("recent_likes", "likes"), ("recent_retweets", "retweets"),
                           ("recent_replies", "replies")]:
            s = x.get(key)
            if s:
                lines.append("- Recent %s (n=%d): median %s / mean %s / max %s"
                             % (label, s["n"], s["median"], s["mean"], s["max"]))
    lines += [
        "",
        "## Wave gate (landing plan §4)",
        "- [ ] Independent verification run reported this period?",
        "- [ ] Substantive technical objection received?",
        "- [ ] Niche-community thread or correspondent?",
        "",
        "_If all three stay unchecked 4 weeks after a wave launch: iterate routing, don't write the next paper._",
        "",
    ]
    with open(SCORECARD, "w") as fh:
        fh.write("\n".join(lines))


def main():
    os.makedirs(HISTORY_DIR, exist_ok=True)
    prev = load_previous()
    today = datetime.date.today().isoformat()
    snap = {"date": today, "github": github_snapshot(), "x": x_snapshot()}
    out = os.path.join(HISTORY_DIR, "%s.json" % today)
    with open(out, "w") as fh:
        json.dump(snap, fh, indent=2)
    write_scorecard(snap, prev)
    print("wrote %s and SCORECARD.md" % os.path.basename(out))
    gh, x = snap["github"], snap["x"]
    print("stars=%s forks=%s issues=%s | followers=%s"
          % (gh["stars_total"], gh["forks_total"], gh["open_issues_total"],
             x.get("followers")))


if __name__ == "__main__":
    sys.exit(main())
