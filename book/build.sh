#!/usr/bin/env bash
# Build the publishable book: PDF (6x9, full-bleed cover), EPUB, HTML.
set -euo pipefail
cd "$(dirname "$0")"
TITLE="The-Crystal-and-the-Clock"

CH="01-the-view-from-inside.md 02-what-exists-even-means.md 03-the-most-symmetric-thing.md \
04-what-the-spectrum-knows.md 05-three-directions-for-free.md 06-looking.md \
07-the-mirror-that-makes-time.md 08-the-measured-numbers.md 09-one-world-many-resolutions.md \
10-the-seventh-dimension-upstairs.md 11-which-world-happens.md 12-what-we-dont-know.md \
13-why-it-might-be-true.md"

# --- PDF: cover page + title + copyright + dedication + manual TOC, no pandoc title/toc ---
pandoc \
  00-frontmatter.md 00a-copyright.md 00b-dedication.md 00c-toc.md \
  00-preface.md $CH 90-appendix.md 91-about.md 92-acknowledgements.md \
  --top-level-division=chapter --include-in-header=header.tex --resource-path=.:figures \
  -V documentclass=report -V fontsize=11pt -V lang=en-GB \
  -V geometry:paperwidth=6in -V geometry:paperheight=9in \
  -V geometry:top=0.85in -V geometry:bottom=0.9in \
  -V geometry:left=0.78in -V geometry:right=0.78in \
  -V linkcolor=black -V urlcolor=black \
  --pdf-engine=pdflatex -o "${TITLE}.pdf"
echo "built ${TITLE}.pdf"

# --- EPUB: cover image via metadata, prose matter (latex commands auto-dropped) ---
pandoc metadata.yaml \
  00a-copyright.md 00b-dedication.md 00-preface.md $CH 90-appendix.md 91-about.md 92-acknowledgements.md \
  --toc --toc-depth=1 --epub-cover-image=figures/cover.png \
  --resource-path=.:figures -o "${TITLE}.epub"
echo "built ${TITLE}.epub"

# --- HTML ---
pandoc metadata.yaml \
  00a-copyright.md 00b-dedication.md 00-preface.md $CH 90-appendix.md 91-about.md 92-acknowledgements.md \
  --toc --toc-depth=1 --standalone --css=book.css \
  --resource-path=.:figures --metadata title="The Crystal and the Clock" -o "${TITLE}.html"
echo "built ${TITLE}.html"
