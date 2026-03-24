#!/bin/bash
# Build all LaTeX papers to PDF
# Usage: ./scripts/build_pdfs.sh
# Requirements: pdflatex, bibtex (TeX Live or MiKTeX)

set -e

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PAPERS_DIR="$REPO_ROOT/papers"

build_paper() {
    local dir="$1"
    local tex_file=$(find "$dir" -maxdepth 1 -name '*.tex' | head -1)

    if [ -z "$tex_file" ]; then
        echo "  SKIP: no .tex file in $dir"
        return
    fi

    local basename=$(basename "$tex_file" .tex)
    echo "  Building: $basename"

    cd "$dir"
    pdflatex -interaction=nonstopmode "$basename.tex" > /dev/null 2>&1 || true
    bibtex "$basename" > /dev/null 2>&1 || true
    pdflatex -interaction=nonstopmode "$basename.tex" > /dev/null 2>&1 || true
    pdflatex -interaction=nonstopmode "$basename.tex" > /dev/null 2>&1

    if [ -f "$basename.pdf" ]; then
        echo "    OK: $basename.pdf"
    else
        echo "    FAILED: $basename.pdf not generated"
        exit 1
    fi

    # Clean auxiliary files
    rm -f "$basename.aux" "$basename.bbl" "$basename.blg" \
          "$basename.log" "$basename.out" "$basename.toc" \
          "$basename.nav" "$basename.snm"

    cd "$REPO_ROOT"
}

echo "=== VFD Crystallisation — PDF Build ==="
echo ""

echo "Building main preprint (flagship)..."
build_paper "$PAPERS_DIR/main-preprint"

echo "Building formalism companion (A)..."
build_paper "$PAPERS_DIR/formalism"

echo "Building experimental companion (B)..."
build_paper "$PAPERS_DIR/experimental"

echo "Building inevitability paper..."
build_paper "$PAPERS_DIR/inevitability"

echo "Building mechanism paper..."
build_paper "$PAPERS_DIR/mechanism"

echo "Building supplementary..."
build_paper "$PAPERS_DIR/supplementary"

echo ""
echo "=== All PDFs built successfully ==="
echo ""
echo "Generated PDFs:"
find "$PAPERS_DIR" -name '*.pdf' -exec echo "  {}" \;
