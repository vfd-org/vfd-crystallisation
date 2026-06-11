# Campaign factory

Automation for the developer-marketing campaign in `docs/landing-plan-2026-06.md` (§3b).
The product is the reproducible result; the ad is the demo; conversion = someone runs
the code. Everything here drafts — **a human approves and posts**.

## Layout

```
campaign/
  registry/           one YAML per claim — the single source of truth
  generators/
    lib.py            registry loader + schema check + blocking-TODO logic
    generate_post.py  X post draft (lead + thread) per claim
    generate_page.py  self-contained canonical result page (HTML) per claim
  kpi/
    collect_kpis.py   GitHub stats (+clones/views with GITHUB_TOKEN) + X stats
    history/          dated JSON snapshots
    SCORECARD.md      latest scorecard with deltas + wave-gate checklist
  output/
    posts/<slug>.md   review-ready post drafts
    pages/<slug>.html result pages (upload to the website)
  run_weekly.py       one command: rotate claim, regenerate, collect, write WEEKLY.md
  WEEKLY.md           this week's review packet
  state.json          rotation state
```

## The weekly cycle (one command)

```bash
python3 campaign/run_weekly.py
```

Then open `campaign/WEEKLY.md`, work the checklist, post manually. `--dry-run`
rebuilds without advancing the rotation.

## Adding a claim

Copy any YAML in `registry/`, fill every field (the loader rejects missing ones).
Non-negotiable fields: `inputs` (numbered modelling inputs — all of them),
`falsifier` (how to kill the claim), `script` (the exact reproduction command).
A claim with `repo: PENDING_PUSH` or `status != verified` generates drafts marked
**BLOCKED** — the post generator will not produce a clean draft until fixed.

## Register guard

`generate_post.py` hard-fails on banned phrases (breaking / proof of consciousness /
unified geometry of reality / theory of everything / multiverse / ...). The technical
feed never uses the old register. Edit `BANNED_PHRASES` only to extend it.

## KPIs

```bash
GITHUB_TOKEN=ghp_... python3 campaign/kpi/collect_kpis.py   # with clones/visitors
python3 campaign/kpi/collect_kpis.py                        # public stats only
```

Conversions (clones, unique visitors, verification reports, substantive objections)
are the KPIs. Likes are not. The scorecard ends with the wave gate from the landing
plan §4: zero external interaction 4 weeks after a wave launch ⇒ iterate routing,
do not write the next paper.
