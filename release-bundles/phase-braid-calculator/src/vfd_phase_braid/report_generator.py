"""Report generation: JSON / CSV / Markdown for downstream analysis.

Every analysis dataclass in the package is plain data, so JSON export is a
generic dataclass walk.  CSV and Markdown have purpose-built writers for the
trajectory / prime-trace tables that downstream tooling expects.
"""

from __future__ import annotations

import csv
import io
import json
from dataclasses import asdict, is_dataclass
from fractions import Fraction
from typing import Any

from .collatz_closure import CollatzAnalysis
from .prime_trace import PrimeTrace


def _jsonable(obj: Any) -> Any:
    if is_dataclass(obj):
        return _jsonable(asdict(obj))
    if isinstance(obj, dict):
        return {str(k): _jsonable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_jsonable(v) for v in obj]
    if isinstance(obj, Fraction):
        return str(obj) if obj.denominator != 1 else int(obj)
    return obj


def to_json(obj: Any, indent: int = 2) -> str:
    """Serialise any analysis object to JSON."""
    return json.dumps(_jsonable(obj), indent=indent, ensure_ascii=False)


def collatz_to_csv(a: CollatzAnalysis) -> str:
    """Per-step CSV of a Collatz run (full trajectory)."""
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["step", "value", "parity", "triad_phase"])
    for i, v in enumerate(a.trajectory):
        w.writerow([i, v, v % 2, v % 3])
    return buf.getvalue()


def prime_trace_to_csv(t: PrimeTrace) -> str:
    """CSV of primes with index, gap-to-next, and triad phase."""
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["index", "prime", "gap_to_next", "triad_phase"])
    for i, p in enumerate(t.primes):
        gap = t.gaps[i] if i < len(t.gaps) else ""
        w.writerow([i, p, gap, p % 3])
    return buf.getvalue()


def collatz_to_markdown(a: CollatzAnalysis) -> str:
    lines = [
        f"# Collatz closure report — start {a.start}",
        "",
        f"- **Steps to closure:** {a.steps_to_closure}",
        f"- **Max value:** {a.max_value}",
        f"- **Odd (compressed) steps:** {len(a.odd_steps)}",
        f"- **Total capacity Q:** {a.total_capacity:.4f} ({a.regime})",
        f"- **Closure basin:** {a.closure_basin}",
        "",
        "## Compressed odd-to-odd steps",
        "",
        "| i | odd m | a = v2(3m+1) | next odd | q_i | cumulative |",
        "|---|-------|--------------|----------|-----|------------|",
    ]
    for i, ((m, ai, nxt), q, cum) in enumerate(
        zip(a.odd_steps, a.local_capacity, a.cumulative_capacity)
    ):
        lines.append(f"| {i} | {m} | {ai} | {nxt} | {q:+.4f} | {cum:+.4f} |")
    if a.escape_flags:
        lines += ["", "## Flags", ""] + [f"- {f}" for f in a.escape_flags]
    return "\n".join(lines)


def prime_trace_to_markdown(t: PrimeTrace) -> str:
    lines = [
        f"# Prime-trace report — range 1..{t.limit}",
        "",
        f"- **Primes:** {t.count}",
        f"- **Max gap:** {t.max_gap}",
        f"- **Triad distribution (p mod 3):** {t.triad_distribution}",
        f"- **Residue distribution (p mod {t.modulus}):** {t.residue_distribution}",
        f"- **Gap-phase distribution (gap mod 3):** {t.gap_phase_distribution}",
        "",
        "## Chebyshev-bias imbalance (share - 0.5)",
        "",
        f"- phase 1: {t.imbalance.get(1, 0.0):+.5f}",
        f"- phase 2: {t.imbalance.get(2, 0.0):+.5f}",
    ]
    return "\n".join(lines)
