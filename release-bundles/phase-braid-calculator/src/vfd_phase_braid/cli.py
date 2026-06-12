"""Command-line interface for the VFD Phase-Braid Calculator.

    vfdcalc inspect 27
    vfdcalc add 8 13
    vfdcalc multiply 21 34
    vfdcalc collatz 27 --max-steps 10000
    vfdcalc primes --limit 10000 --modulus 6
    vfdcalc self-adjoint collatz --limit 16
    vfdcalc report collatz 871 --format markdown
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__
from . import boundary_capacity as bc
from . import collatz_closure as cc
from . import lifted_arithmetic as la
from . import prime_trace as pt
from . import report_generator as rg
from . import self_adjoint as sa
from .vfd_number import VFDNumber


def _emit(text: str, output: str | None) -> None:
    if output:
        Path(output).parent.mkdir(parents=True, exist_ok=True)
        Path(output).write_text(text + "\n", encoding="utf-8")
        print(f"written to {output}")
    else:
        print(text)


def _cmd_inspect(args: argparse.Namespace) -> int:
    vn = VFDNumber.lift(args.n)
    _emit(rg.to_json(vn) if args.json else vn.describe(), args.output)
    return 0


_OPS = {"add": la.add, "subtract": la.subtract, "multiply": la.multiply,
        "divide": la.divide, "power": la.power}


def _cmd_op(args: argparse.Namespace) -> int:
    result = _OPS[args.op](args.a, args.b)
    _emit(rg.to_json(result) if args.json else result.describe(), args.output)
    return 0


def _cmd_collatz(args: argparse.Namespace) -> int:
    analysis = cc.analyze(args.n, args.max_steps)
    _emit(rg.to_json(analysis) if args.json else cc.describe(analysis), args.output)
    return 0


def _cmd_primes(args: argparse.Namespace) -> int:
    trace = pt.analyze(args.limit, args.modulus)
    _emit(rg.to_json(trace) if args.json else pt.describe(trace), args.output)
    return 0


def _cmd_self_adjoint(args: argparse.Namespace) -> int:
    result = sa.analyze(args.domain, args.limit)
    _emit(rg.to_json(result) if args.json else sa.describe(result), args.output)
    return 0


def _cmd_capacity(args: argparse.Namespace) -> int:
    verdict = bc.collatz_capacity(args.n, args.max_steps)
    if args.json:
        _emit(rg.to_json(verdict), args.output)
    else:
        _emit(
            f"compression: {verdict.compression:.4f}\n"
            f"expansion:   {verdict.expansion:.4f}\n"
            f"Q:           {verdict.Q:+.4f}\n"
            f"class:       {verdict.classification}",
            args.output,
        )
    return 0


def _cmd_report(args: argparse.Namespace) -> int:
    if args.subject == "collatz":
        analysis = cc.analyze(args.n, args.max_steps)
        if args.format == "markdown":
            text = rg.collatz_to_markdown(analysis)
        elif args.format == "csv":
            text = rg.collatz_to_csv(analysis)
        else:
            text = rg.to_json(analysis)
    elif args.subject == "primes":
        trace = pt.analyze(args.n, args.modulus)
        if args.format == "markdown":
            text = rg.prime_trace_to_markdown(trace)
        elif args.format == "csv":
            text = rg.prime_trace_to_csv(trace)
        else:
            text = rg.to_json(trace)
    else:
        print(f"unknown report subject '{args.subject}'", file=sys.stderr)
        return 2
    _emit(text, args.output)
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="vfdcalc",
        description="VFD Phase-Braid Calculator — lift arithmetic into phase-braid, "
                    "compression and closure-state coordinates.",
    )
    p.add_argument("--version", action="version", version=f"vfdcalc {__version__}")
    sub = p.add_subparsers(dest="command", required=True)

    def _common(sp):
        sp.add_argument("--json", action="store_true", help="emit JSON")
        sp.add_argument("--output", "-o", help="write to file instead of stdout")

    sp = sub.add_parser("inspect", help="inspect a number as a phase-braid object")
    sp.add_argument("n", type=int)
    _common(sp)
    sp.set_defaults(func=_cmd_inspect)

    for name in ("add", "subtract", "multiply", "divide", "power"):
        sp = sub.add_parser(name, help=f"lifted {name}")
        sp.add_argument("a", type=int)
        sp.add_argument("b", type=int)
        _common(sp)
        sp.set_defaults(func=_cmd_op, op=name)

    sp = sub.add_parser("collatz", help="Collatz closure analysis")
    sp.add_argument("n", type=int)
    sp.add_argument("--max-steps", type=int, default=100_000)
    _common(sp)
    sp.set_defaults(func=_cmd_collatz)

    sp = sub.add_parser("capacity", help="Collatz boundary-capacity verdict")
    sp.add_argument("n", type=int)
    sp.add_argument("--max-steps", type=int, default=100_000)
    _common(sp)
    sp.set_defaults(func=_cmd_capacity)

    sp = sub.add_parser("primes", help="prime-trace analysis over 1..limit")
    sp.add_argument("--limit", type=int, default=1000)
    sp.add_argument("--modulus", type=int, default=6)
    _common(sp)
    sp.set_defaults(func=_cmd_primes)

    sp = sub.add_parser("self-adjoint", help="finite-window self-adjoint B-form test")
    sp.add_argument("domain", nargs="?", default="collatz", choices=["collatz"])
    sp.add_argument("--limit", type=int, default=16)
    _common(sp)
    sp.set_defaults(func=_cmd_self_adjoint)

    sp = sub.add_parser("report", help="generate a markdown/csv/json report")
    sp.add_argument("subject", choices=["collatz", "primes"])
    sp.add_argument("n", type=int, help="start value (collatz) or limit (primes)")
    sp.add_argument("--format", choices=["markdown", "csv", "json"], default="markdown")
    sp.add_argument("--max-steps", type=int, default=100_000)
    sp.add_argument("--modulus", type=int, default=6)
    sp.add_argument("--output", "-o", help="write to file instead of stdout")
    sp.set_defaults(func=_cmd_report)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
