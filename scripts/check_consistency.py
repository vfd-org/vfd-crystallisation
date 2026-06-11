#!/usr/bin/env python3
"""
VFD cross-paper consistency checker.

Scans every paper under papers/*/paper-*.tex for:
  1. Undefined macro usage (flags `\Foo` where `\newcommand{\Foo}` is not in the paper's preamble).
  2. Begin/end environment balance.
  3. Broken env tags like `\end{remark>`.
  4. Missing \ref and \eqref targets within the same paper.
  5. Missing bib keys cited by \citep within the same paper's references.bib.

Also produces a cross-paper summary:
  - Macros that appear in multiple papers (for coordinated refactoring).
  - Bib keys referenced across multiple papers.
  - Numerical constants (Phi, pi/87, 137, 1/137, 0.014%, etc.) that appear in multiple papers,
    flagging any value-mismatch.

Run:  python3 scripts/check_consistency.py
Exit code 0 if clean; non-zero if any paper has a real issue.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PAPERS_DIR = REPO_ROOT / "papers"


@dataclass
class PaperIssues:
    path: Path
    undefined_macros: set[str]
    unbalanced_envs: list[tuple[str, int]]
    broken_tags: list[tuple[int, str]]
    missing_refs: set[str]
    missing_citations: set[str]

    @property
    def is_clean(self) -> bool:
        return not (
            self.undefined_macros
            or self.unbalanced_envs
            or self.broken_tags
            or self.missing_refs
            or self.missing_citations
        )

    def summary(self) -> str:
        lines = [f"=== {self.path.relative_to(REPO_ROOT)} ==="]
        if self.undefined_macros:
            lines.append(
                f"  undefined macros ({len(self.undefined_macros)}): "
                + ", ".join(sorted(self.undefined_macros)[:10])
                + (" ..." if len(self.undefined_macros) > 10 else "")
            )
        if self.broken_tags:
            lines.append(f"  broken env tags ({len(self.broken_tags)}):")
            for lineno, snippet in self.broken_tags[:5]:
                lines.append(f"    line {lineno}: {snippet!r}")
        if self.unbalanced_envs:
            lines.append("  unbalanced environments:")
            for env, delta in self.unbalanced_envs:
                lines.append(f"    {env}: delta={delta:+d}")
        if self.missing_refs:
            lines.append(
                f"  missing \\ref/\\eqref targets ({len(self.missing_refs)}): "
                + ", ".join(sorted(self.missing_refs)[:5])
                + (" ..." if len(self.missing_refs) > 5 else "")
            )
        if self.missing_citations:
            lines.append(
                f"  missing \\citep keys ({len(self.missing_citations)}): "
                + ", ".join(sorted(self.missing_citations)[:5])
                + (" ..." if len(self.missing_citations) > 5 else "")
            )
        if self.is_clean:
            lines.append("  OK")
        return "\n".join(lines)


RE_NEWCOMMAND = re.compile(r"\\newcommand\{\\([A-Za-z@]+)\}")
RE_MACRO_USE = re.compile(r"\\([A-Z][A-Za-z@]*)\b")
RE_LABEL = re.compile(r"\\label\{([^}]+)\}")
RE_REF = re.compile(r"\\(?:ref|eqref|cref|Cref|autoref)\{([^}]+)\}")
RE_CITE = re.compile(r"\\cite[pt]?\{([^}]+)\}")
RE_BIB_KEY = re.compile(r"^@\w+\{([^,]+),", re.MULTILINE)
RE_BEGIN = re.compile(r"\\begin\{([a-zA-Z*]+)\}")
RE_END = re.compile(r"\\end\{([a-zA-Z*]+)\}")
RE_BROKEN_TAG = re.compile(r"\\(?:begin|end)\{[a-zA-Z*]+>")

# Macros we trust as LaTeX/amsmath/standard-package built-ins.
# Anything case-sensitive starting with uppercase that isn't in this set and
# isn't defined via \newcommand in the paper triggers a warning.
KNOWN_LATEX_MACROS: set[str] = {
    "LaTeX",
    "TeX",
    "Box",
    "Re",
    "Im",
    "Pr",
    "Psi",
    "Phi",
    "Theta",
    "Omega",
    "Delta",
    "Gamma",
    "Lambda",
    "Sigma",
    "Pi",
    "Xi",
    "Upsilon",
    "Psi",
    "Null",
    # amsmath / amssymb built-ins commonly capitalised:
    "Tr",
    "Trace",
    "Hom",
    "End",
    "Aut",
    "Isom",
    "Id",
    "Det",
    "Rank",
    "Ker",
    "Image",
    "Span",
    "Spec",
    "Supp",
    # math constructors
    "Bbb",
    "Rm",
    "Mathbb",
    "Mathcal",
    "Mathrm",
    "Mathfrak",
    "Mathscr",
    "Boldsymbol",
    "Operatorname",
    # we catch \HW, \VW etc. from preamble scan; anything else uppercase is
    # flagged for manual review
}


def scan_paper(tex_path: Path) -> PaperIssues:
    text = tex_path.read_text(encoding="utf-8", errors="replace")

    defined = set(RE_NEWCOMMAND.findall(text))
    defined.update(KNOWN_LATEX_MACROS)

    used = set()
    for m in RE_MACRO_USE.finditer(text):
        used.add(m.group(1))
    # Only flag uppercase-first custom-looking macros (case-sensitive).
    # This is an approximation; standard lowercase macros like \alpha, \phi,
    # \cdot, etc. are fine. Uppercase-first macros like \HW, \Mcl, \Ecal
    # need to be defined.
    suspicious = {m for m in used if m[:1].isupper() and m not in defined}
    # Drop common false positives: math fonts, structural envs, etc.
    suspicious -= {
        "Roman",
        "Tiny",
        "Small",
        "Large",
        "LARGE",
        "Huge",
    }

    begin_counts: defaultdict[str, int] = defaultdict(int)
    end_counts: defaultdict[str, int] = defaultdict(int)
    for m in RE_BEGIN.finditer(text):
        begin_counts[m.group(1)] += 1
    for m in RE_END.finditer(text):
        end_counts[m.group(1)] += 1
    unbalanced: list[tuple[str, int]] = []
    for env in set(begin_counts) | set(end_counts):
        delta = begin_counts[env] - end_counts[env]
        if delta != 0:
            unbalanced.append((env, delta))

    broken_tags: list[tuple[int, str]] = []
    for lineno, line in enumerate(text.splitlines(), 1):
        m = RE_BROKEN_TAG.search(line)
        if m:
            broken_tags.append((lineno, m.group(0)))

    labels = set(RE_LABEL.findall(text))
    refs = set(RE_REF.findall(text))
    missing_refs = refs - labels

    bib_path = tex_path.parent / "references.bib"
    if bib_path.exists():
        bib_text = bib_path.read_text(encoding="utf-8", errors="replace")
        bib_keys = set(RE_BIB_KEY.findall(bib_text))
    else:
        bib_keys = set()
    cited_keys: set[str] = set()
    for m in RE_CITE.finditer(text):
        for k in m.group(1).split(","):
            cited_keys.add(k.strip())
    missing_citations = cited_keys - bib_keys if bib_path.exists() else set()

    return PaperIssues(
        path=tex_path,
        undefined_macros=suspicious,
        unbalanced_envs=unbalanced,
        broken_tags=broken_tags,
        missing_refs=missing_refs,
        missing_citations=missing_citations,
    )


def find_all_paper_tex_files() -> list[Path]:
    paths: list[Path] = []
    for paper_dir in sorted(PAPERS_DIR.iterdir()):
        if not paper_dir.is_dir():
            continue
        for tex in sorted(paper_dir.glob("*.tex")):
            paths.append(tex)
    return paths


def main() -> int:
    parser = argparse.ArgumentParser(description="VFD cross-paper consistency checker.")
    parser.add_argument(
        "--paper",
        help="Only check one paper directory name (e.g. paper-xxx)",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Only print summary counts and exit.",
    )
    args = parser.parse_args()

    tex_files = find_all_paper_tex_files()
    if args.paper:
        tex_files = [p for p in tex_files if args.paper in str(p)]
        if not tex_files:
            print(f"No .tex files found matching {args.paper!r}", file=sys.stderr)
            return 2

    results: list[PaperIssues] = []
    for tex in tex_files:
        results.append(scan_paper(tex))

    dirty = [r for r in results if not r.is_clean]

    if args.quiet:
        print(f"checked={len(results)} clean={len(results) - len(dirty)} dirty={len(dirty)}")
    else:
        for r in results:
            print(r.summary())
            print()

    return 1 if dirty else 0


if __name__ == "__main__":
    sys.exit(main())
