"""Collatz closure analysis: the first real proving ground.

Two views of the dynamics are computed:

  * the full trajectory  n -> n/2 (even) | 3n+1 (odd), and
  * the odd-to-odd compressed map  m -> (3m + 1) / 2^a  with a = v2(3m + 1).

For each compressed step we record the local capacity

    q_i = a_i * log 2 - log 3,

whose sign decides whether that step contracts (q_i > 0) or expands.  The
cumulative capacity and the sum-rule
    Q = (sum a_i) * log 2 - k * log 3       (k = number of odd steps)
are the closure diagnostics: Q > 0 over a run means net contraction toward the
4-2-1 basin.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import List, Tuple

LOG2 = math.log(2.0)
LOG3 = math.log(3.0)

# log2(3): mean v2(3n+1) above which trajectories contract on average.
LOG2_3 = LOG3 / LOG2


def collatz_next(n: int) -> int:
    """One step of the standard Collatz map."""
    return n // 2 if n % 2 == 0 else 3 * n + 1


def trajectory(n: int, max_steps: int = 100_000) -> Tuple[List[int], bool]:
    """Full Collatz trajectory from n until it first reaches 1.

    Returns (sequence, reached_one).  The sequence starts at n and includes the
    terminal 1 when reached.
    """
    if n < 1:
        raise ValueError("Collatz is defined for positive integers")
    seq = [n]
    m = n
    steps = 0
    while m != 1 and steps < max_steps:
        m = collatz_next(m)
        seq.append(m)
        steps += 1
    return seq, (m == 1)


@dataclass
class CollatzAnalysis:
    start: int
    trajectory: List[int]
    parity_sequence: List[int]
    triad_sequence: List[int]
    compression_events: List[int]      # v2 at each even (halving) step
    odd_steps: List[Tuple[int, int, int]]  # (odd value m, a_i, next odd)
    local_capacity: List[float]
    cumulative_capacity: List[float]
    steps_to_closure: int              # full-map steps to reach 1 (-1 if none)
    max_value: int
    closure_basin: List[int]
    total_capacity: float
    regime: str                        # closure-dominant / balanced / expansion-dominant
    escape_flags: List[str] = field(default_factory=list)


def analyze(n: int, max_steps: int = 100_000) -> CollatzAnalysis:
    """Run the full closure analysis on starting value n."""
    seq, reached = trajectory(n, max_steps)

    parity_seq = [v % 2 for v in seq]
    triad_seq = [v % 3 for v in seq]

    compression_events: List[int] = []
    for v in seq:
        if v % 2 == 0:
            # v2 of the value being halved
            x, c = v, 0
            while x % 2 == 0:
                x //= 2
                c += 1
            compression_events.append(c)

    # Odd-to-odd compressed map + capacity.
    odd_steps: List[Tuple[int, int, int]] = []
    local_cap: List[float] = []
    cum_cap: List[float] = []
    m = n
    while m % 2 == 0:           # reduce the seed to its odd core first
        m //= 2
    running = 0.0
    guard = 0
    while m != 1 and guard < max_steps:
        t = 3 * m + 1
        a = 0
        x = t
        while x % 2 == 0:
            x //= 2
            a += 1
        nxt = t // (2 ** a)
        q = a * LOG2 - LOG3
        odd_steps.append((m, a, nxt))
        local_cap.append(q)
        running += q
        cum_cap.append(running)
        m = nxt
        guard += 1

    total_a = sum(a for _, a, _ in odd_steps)
    k = len(odd_steps)
    total_capacity = total_a * LOG2 - k * LOG3
    if k == 0:
        regime = "trivial (already at unit)"
    elif total_capacity > 1e-9:
        regime = "closure-dominant"
    elif total_capacity < -1e-9:
        regime = "expansion-dominant"
    else:
        regime = "boundary-balanced"

    escape_flags: List[str] = []
    if not reached:
        escape_flags.append(f"no closure within {max_steps} steps")
    # cycle detection beyond the 4-2-1 basin
    seen = set()
    for v in seq:
        if v in seen and v != 1:
            escape_flags.append(f"state {v} repeats (non-trivial cycle candidate)")
            break
        seen.add(v)

    steps_to_closure = (len(seq) - 1) if reached else -1
    closure_basin = [4, 2, 1] if reached else []

    return CollatzAnalysis(
        start=n,
        trajectory=seq,
        parity_sequence=parity_seq,
        triad_sequence=triad_seq,
        compression_events=compression_events,
        odd_steps=odd_steps,
        local_capacity=local_cap,
        cumulative_capacity=cum_cap,
        steps_to_closure=steps_to_closure,
        max_value=max(seq),
        closure_basin=closure_basin,
        total_capacity=total_capacity,
        regime=regime,
        escape_flags=escape_flags,
    )


def describe(a: CollatzAnalysis, preview: int = 16) -> str:
    """Compact textual report."""
    traj = a.trajectory
    head = " -> ".join(str(x) for x in traj[:preview])
    if len(traj) > preview:
        head += " -> ..."
    tphase = " -> ".join(str(x) for x in a.triad_sequence[:preview])
    if len(a.triad_sequence) > preview:
        tphase += " -> ..."
    lines = [
        f"start: {a.start}",
        f"trajectory ({len(traj)} pts): {head}",
        f"triad phases:  {tphase}",
        f"steps to closure: {a.steps_to_closure}",
        f"max value:        {a.max_value}",
        f"odd (compressed) steps: {len(a.odd_steps)}",
        f"total capacity Q = {a.total_capacity:.4f}  ({a.regime})",
        f"mean v2(3n+1) = {(a.total_capacity / max(len(a.odd_steps),1) + LOG3) / LOG2:.4f} "
        f"(contraction threshold log2(3) = {LOG2_3:.4f})",
        f"closure basin: {a.closure_basin}",
    ]
    if a.escape_flags:
        for f in a.escape_flags:
            lines.append(f"FLAG: {f}")
    return "\n".join(lines)
