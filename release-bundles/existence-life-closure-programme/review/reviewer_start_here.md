# Reviewer — start here

Welcome. This is the one-stop entry point for reviewing the
Existence / Life / Closure Programme.

## 1. Read first

- [`../00-review-packet-overview.md`](../00-review-packet-overview.md) — one-page programme overview (5 min).
- [`packet_order.md`](packet_order.md) — recommended reading order with effort estimates.
- [`status_taxonomy.md`](status_taxonomy.md) — what the five status labels mean.

## 2. Read the papers

Primary order:

1. Paper I — Existence as Closure (foundation) — `../papers/I-existence-as-closure/`
2. Paper II — Life as Closure (human bridge) — `../papers/II-life-as-closure/`
3. Note C — Closure-as-Distance (measurement) — `../notes/Note-C-closure-as-distance/`
4. Note B — Cortical Phase Closure (anchor) — `../notes/Note-B-cortical-phase-closure/`
5. Paper III — From Processing to Point of View (consciousness bridge) — `../papers/III-processing-to-point-of-view/`

Optional appendix notes A, D, E, F.

## 3. Check the falsifiers + limitations

- [`../01-falsifiers-and-roadmap.md`](../01-falsifiers-and-roadmap.md) — what would weaken / falsify each claim.
- [`known_limitations.md`](known_limitations.md) — every disclosed gap.
- [`non_claims.md`](non_claims.md) — what the programme does not claim.

## 4. Try to break it

Reviewers are explicitly invited to:

- Find a place where the status taxonomy is broken (theorem stated where conditional should be, or vice versa).
- Find an empirical proxy claim that exceeds what the data supports.
- Find a place where formal-operator language is used for an empirical proxy.
- Find a place where the cosmic-extension material is rhetorically relied on in the primary packet.

## 5. Reproduce the demos

```bash
git clone https://github.com/vfd-org/existence-life-closure-programme.git
cd existence-life-closure-programme
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r repro/shared/requirements.txt
python repro/shared/run_all_smoke_tests.py
```

Real-data analyses require external data download; see
[`../repro/shared/data_access.md`](../repro/shared/data_access.md).

## 6. Submit your review

Open a GitHub issue with the label "review" or email the author. We
welcome:

- Substantive critique on math discipline.
- Substantive critique on empirical scope.
- Suggestions for falsifiers we have not stated.
- Independent replication attempts.
- Negative results.

Personal attacks are not welcome; see `../CONTRIBUTING.md`.
