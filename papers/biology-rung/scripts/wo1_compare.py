"""WO-BIOLOGY-RUNG-001-CAPSID: Predicted vs. observed T-number comparison.

Implements [N.2] from papers/biology-rung/derivation-capsid.md:
runs statistical comparison of the cascade-predicted T-number
distribution against a VIPERdb-sourced (or literature-sourced)
observed distribution. Tests three nested null hypotheses in order
of increasing cascade content:

    H0: T uniformly distributed over all positive integers
        (expected strongly falsified by Loeschian confinement)

    H1: T uniformly distributed over Loeschian numbers only
        (expected weakly falsified by small-T over-representation)

    H2: T distributed as Z(T) ∝ mu(T) * exp(-beta * c(T))  [C.1]
        with c(T) either a supplied monotone ansatz or an empirical
        fit. This is the cascade-specific conjecture.

Plus a chirality-asymmetry test against H0-chirality = 50/50 on
chiral T-numbers (mu=2 orbits), per [C.3].

Outputs go to `data/wo1_comparison.md`.

Inputs
------
    --prediction FILE   wo1_prediction.csv (default: data/wo1_prediction.csv)
                        columns: T, mu, representative, chirality
    --observed FILE     wo1_viperdb_observed.csv (default: data/wo1_viperdb_observed.csv)
                        columns: id, species_or_genome, T, chirality, source_ref, notes
    --beta FLOAT        beta for H2 if fitting with a fixed c(T) (default: 0.05)
    --c-ansatz STR      functional form for c(T) (default: "linear"; options
                        "linear", "log", "sqrt"; linear uses c(T) = T)
    --out FILE          output report path (default: data/wo1_comparison.md)

Behaviour when inputs are missing
---------------------------------
If `wo1_viperdb_observed.csv` does not exist, the script exits
cleanly with an explicit "WAITING_FOR_DATA" message rather than
fabricating empty results. The paper's [N.2] claim depends on the
observed dataset, not on running this sim against nothing.

Statistical methods
-------------------
* Pearson chi-squared (reporting statistic, df, p-value).
* KL divergence D(observed || predicted), computed with a small
  additive smoothing when the observed histogram has zeros.
* Chirality-asymmetry two-tailed binomial test per chiral T, plus
  a meta-test over pooled chiral T's.

Nothing here claims biological relevance on its own; this is a
statistical bridge that expresses the cascade prediction in a
form comparable to what a viral capsid database provides.
"""

from __future__ import annotations

import argparse
import csv
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Callable

HERE = Path(__file__).resolve().parent
DATA_DIR = HERE.parent / "data"

DEFAULT_PREDICTION = DATA_DIR / "wo1_prediction.csv"
DEFAULT_OBSERVED = DATA_DIR / "wo1_viperdb_observed.csv"
DEFAULT_OUT = DATA_DIR / "wo1_comparison.md"


# ---------------------------------------------------------------
# I/O
# ---------------------------------------------------------------

def load_prediction(path: Path) -> dict[int, dict]:
    """Read per-orbit prediction CSV, collapse to per-T summary.

    Returns {T: {"mu": int, "n_achiral": int, "n_chiral": int}}.
    """
    if not path.exists():
        raise FileNotFoundError(f"Prediction file not found: {path}")
    by_T: dict[int, dict] = defaultdict(lambda: {"mu": 0, "n_achiral": 0, "n_chiral": 0})
    with path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            T = int(row["T"])
            by_T[T]["mu"] = max(by_T[T]["mu"], int(row["mu"]))
            if row["chirality"] == "achiral":
                by_T[T]["n_achiral"] += 1
            elif row["chirality"] == "chiral":
                by_T[T]["n_chiral"] += 1
    return dict(by_T)


def load_observed(path: Path) -> list[dict]:
    """Read observed VIPERdb-style rows. Empty list ⇒ caller handles."""
    if not path.exists():
        return []
    rows = []
    with path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("id", "").startswith("#"):
                continue
            try:
                T = int(row["T"])
            except (KeyError, ValueError):
                continue
            rows.append({
                "id": row.get("id", ""),
                "T": T,
                "chirality": row.get("chirality", "unknown").strip(),
            })
    return rows


# ---------------------------------------------------------------
# Hypothesis distributions
# ---------------------------------------------------------------

def h0_distribution(T_values: list[int]) -> dict[int, float]:
    """Uniform over positive integers covered by the observed range."""
    if not T_values:
        return {}
    T_max = max(T_values)
    support = list(range(1, T_max + 1))
    p = 1.0 / len(support)
    return {T: p for T in support}


def h1_distribution(prediction: dict[int, dict], T_max: int) -> dict[int, float]:
    """Uniform over Loeschians ≤ T_max."""
    loesch = [T for T in prediction if T <= T_max]
    if not loesch:
        return {}
    p = 1.0 / len(loesch)
    return {T: p for T in loesch}


def c_of_T(ansatz: str) -> Callable[[int], float]:
    if ansatz == "linear":
        return lambda T: float(T)
    if ansatz == "log":
        return lambda T: math.log(T) if T > 0 else 0.0
    if ansatz == "sqrt":
        return lambda T: math.sqrt(T)
    raise ValueError(f"Unknown c(T) ansatz: {ansatz}")


def h2_distribution(
    prediction: dict[int, dict],
    T_max: int,
    beta: float,
    c_func: Callable[[int], float],
) -> dict[int, float]:
    """Z(T) ∝ mu(T) · exp(-beta · c(T))."""
    weights = {T: prediction[T]["mu"] * math.exp(-beta * c_func(T))
               for T in prediction if T <= T_max}
    Z = sum(weights.values())
    if Z <= 0:
        return {}
    return {T: w / Z for T, w in weights.items()}


# ---------------------------------------------------------------
# Statistical tests
# ---------------------------------------------------------------

def chi_squared(observed_counts: dict[int, int],
                predicted_probs: dict[int, float],
                N: int) -> tuple[float, int]:
    """Pearson chi-squared. Returns (statistic, df).

    df = (# bins with nonzero expected) − 1.
    Bins with expected count < 1 are pooled into 'other' to avoid
    unstable behaviour; simple implementation.
    """
    stat = 0.0
    bins = 0
    pooled_obs = 0.0
    pooled_exp = 0.0
    for T in sorted(set(observed_counts) | set(predicted_probs)):
        obs = observed_counts.get(T, 0)
        exp = predicted_probs.get(T, 0.0) * N
        if exp < 1.0:
            pooled_obs += obs
            pooled_exp += exp
        elif exp > 0.0:
            stat += (obs - exp) ** 2 / exp
            bins += 1
    if pooled_exp > 0.0:
        stat += (pooled_obs - pooled_exp) ** 2 / pooled_exp
        bins += 1
    df = max(bins - 1, 0)
    return stat, df


def kl_divergence(observed_probs: dict[int, float],
                  predicted_probs: dict[int, float],
                  eps: float = 1e-9) -> float:
    """D(observed || predicted) with additive smoothing."""
    total = 0.0
    for T, p_obs in observed_probs.items():
        if p_obs <= 0:
            continue
        p_pred = predicted_probs.get(T, eps)
        if p_pred <= 0:
            p_pred = eps
        total += p_obs * math.log(p_obs / p_pred)
    return total


def chirality_asymmetry_test(observed: list[dict],
                             prediction: dict[int, dict]) -> dict:
    """Binomial two-tailed test against 50/50 on chiral T's.

    Only T values where prediction says the orbits are chiral are
    relevant. Returns per-T breakdown + pooled meta-test.
    """
    per_T: dict[int, dict] = {}
    pooled_L = 0
    pooled_D = 0
    for T, rec in prediction.items():
        if rec["n_chiral"] == 0:
            continue
        at_T = [r for r in observed if r["T"] == T]
        L = sum(1 for r in at_T if r["chirality"] == "laevo")
        D = sum(1 for r in at_T if r["chirality"] == "dextro")
        N = L + D
        if N == 0:
            continue
        # Two-sided binomial p-value against p=0.5, no external deps.
        smaller = min(L, D)
        p_value = 2.0 * sum(_binomial_pmf(k, N, 0.5) for k in range(smaller + 1))
        p_value = min(p_value, 1.0)
        per_T[T] = {"L": L, "D": D, "N": N, "p_value": p_value}
        pooled_L += L
        pooled_D += D

    N_tot = pooled_L + pooled_D
    if N_tot > 0:
        smaller_tot = min(pooled_L, pooled_D)
        pooled_p = 2.0 * sum(_binomial_pmf(k, N_tot, 0.5) for k in range(smaller_tot + 1))
        pooled_p = min(pooled_p, 1.0)
    else:
        pooled_p = None

    return {"per_T": per_T, "pooled_L": pooled_L, "pooled_D": pooled_D,
            "pooled_N": N_tot, "pooled_p": pooled_p}


def _binomial_pmf(k: int, n: int, p: float) -> float:
    if k < 0 or k > n:
        return 0.0
    return math.comb(n, k) * (p ** k) * ((1.0 - p) ** (n - k))


# ---------------------------------------------------------------
# Report
# ---------------------------------------------------------------

def emit_report(out_path: Path, sections: list[str]) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w") as f:
        f.write("# WO-1 Capsid Comparison — Predicted vs. Observed\n\n")
        f.write("\n\n".join(sections))
        f.write("\n")


def fmt_hypothesis_block(name: str, description: str,
                         chi2: float, df: int, kl: float,
                         N: int) -> str:
    return (
        f"## Hypothesis {name}\n\n"
        f"**Statement.** {description}\n\n"
        f"- N observed capsids: {N}\n"
        f"- χ² statistic: {chi2:.4f}\n"
        f"- df: {df}\n"
        f"- KL( observed || predicted ): {kl:.4f} nats\n"
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prediction", type=Path, default=DEFAULT_PREDICTION)
    ap.add_argument("--observed", type=Path, default=DEFAULT_OBSERVED)
    ap.add_argument("--beta", type=float, default=0.05)
    ap.add_argument("--c-ansatz", type=str, default="linear")
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = ap.parse_args()

    prediction = load_prediction(args.prediction)
    observed = load_observed(args.observed)

    if not observed:
        # Emit a WAITING_FOR_DATA report rather than fabricating.
        msg = (
            "WAITING_FOR_DATA: no observed-T capsid dataset present.\n"
            f"Expected input file: {args.observed}\n\n"
            "Populate via one of:\n"
            f"  python {HERE / 'wo1_viperdb_fetch.py'} --fetch "
            "(requires updated CANDIDATE_ENDPOINTS for current VIPERdb API)\n"
            f"  python {HERE / 'wo1_viperdb_fetch.py'} "
            "--from-literature <curated CSV>\n"
            "Then re-run wo1_compare.py.\n\n"
            "No empirical claim is being made in [N.2] until this file exists.\n"
        )
        print(msg)
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text("# WO-1 Capsid Comparison — Predicted vs. Observed\n\n"
                            "**Status:** WAITING_FOR_DATA.\n\n" + msg + "\n")
        return 10  # distinct exit code: not an error, but empirical result pending

    # Histogram & basic stats
    counts = Counter(r["T"] for r in observed)
    N = sum(counts.values())
    obs_probs = {T: counts[T] / N for T in counts}
    T_max_obs = max(counts)

    # Build hypothesis distributions over the observed support
    T_values = sorted(counts)
    h0 = h0_distribution(T_values)
    h1 = h1_distribution(prediction, T_max_obs)
    c_func = c_of_T(args.c_ansatz)
    h2 = h2_distribution(prediction, T_max_obs, args.beta, c_func)

    sections = []

    sections.append("## Input summary\n\n"
                    f"- Prediction: {args.prediction}\n"
                    f"- Observed:   {args.observed} (N = {N} capsids)\n"
                    f"- T_max observed: {T_max_obs}\n"
                    f"- beta = {args.beta}, c(T) ansatz: {args.c_ansatz}\n")

    # H0
    chi0, df0 = chi_squared(counts, h0, N)
    kl0 = kl_divergence(obs_probs, h0)
    sections.append(fmt_hypothesis_block(
        "H0", "T uniform over positive integers ≤ T_max_obs.",
        chi0, df0, kl0, N))

    # H1
    chi1, df1 = chi_squared(counts, h1, N)
    kl1 = kl_divergence(obs_probs, h1)
    sections.append(fmt_hypothesis_block(
        "H1", "T uniform over Loeschians ≤ T_max_obs.",
        chi1, df1, kl1, N))

    # H2
    chi2, df2 = chi_squared(counts, h2, N)
    kl2 = kl_divergence(obs_probs, h2)
    sections.append(fmt_hypothesis_block(
        "H2",
        f"T ∝ mu(T) · exp(-{args.beta} · {args.c_ansatz}(T))  "
        "[Conjecture C.1].",
        chi2, df2, kl2, N))

    # Chirality
    chir = chirality_asymmetry_test(observed, prediction)
    lines = ["## Chirality asymmetry (Conjecture C.3)\n"]
    lines.append(f"Pooled laevo vs dextro across chiral T: "
                 f"{chir['pooled_L']}/{chir['pooled_N']}")
    if chir["pooled_p"] is not None:
        lines.append(f"Pooled two-tailed binomial p vs 50/50: {chir['pooled_p']:.4g}")
    else:
        lines.append("No chiral observations — pooled test not computed.")
    if chir["per_T"]:
        lines.append("\n| T | L | D | N | p |")
        lines.append("|---|---|---|---|---|")
        for T in sorted(chir["per_T"]):
            r = chir["per_T"][T]
            lines.append(f"| {T} | {r['L']} | {r['D']} | {r['N']} | {r['p_value']:.4g} |")
    sections.append("\n".join(lines))

    sections.append(
        "## Interpretation (template — fill after first real run)\n\n"
        "* H0 vs. H1: the ratio χ²(H0)/χ²(H1) measures how much of the "
        "observed structure is already captured by bare Loeschian "
        "confinement. A large ratio means the cascade's mathematical "
        "content at the L.1 level does a lot of the work; a small ratio "
        "means small-T over-representation is the dominant signal.\n\n"
        "* H1 vs. H2: χ²(H1)/χ²(H2) measures cascade-specific content "
        "beyond bare Loeschian admissibility (i.e. whether the "
        "μ-weighted structure plus assembly cost c(T) is needed).\n\n"
        "* Chirality: a pooled p « 0.05 with consistent sign across "
        "chiral T supports C.3; a p close to 0.5 falsifies the "
        "direction-predicted asymmetry.\n"
    )

    emit_report(args.out, sections)
    print(f"Wrote: {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
