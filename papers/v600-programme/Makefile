# V_600 programme — single make target builds everything for release.
#
# Usage:
#   make             — run all tests + build all PDFs + assemble arxiv tarballs.
#   make test        — run pytest on the shared library.
#   make pdfs        — build all five paper PDFs (skips ones not yet drafted).
#   make arxiv       — assemble per-paper arxiv tarballs.
#   make clean       — remove build artifacts.
#   make distclean   — also remove release tarballs.

PROGRAMME_DIR := $(realpath $(dir $(lastword $(MAKEFILE_LIST))))
PAPERS_DIR    := $(realpath $(PROGRAMME_DIR)/..)
RELEASE_DIR   := $(PROGRAMME_DIR)/release

PAPER_SLUGS := \
    bekenstein-incidence \
    v600-hawking-quantum \
    tau-sigma-construction \
    v600-cosmic-tensions \
    v600-unified

.PHONY: all test pdfs arxiv clean distclean release $(PAPER_SLUGS)

all: test pdfs arxiv

test:
	@echo ">> running V_600 test suite"
	@cd "$(PROGRAMME_DIR)" && python3 -m pytest tests/ -q

pdfs: $(PAPER_SLUGS)

$(PAPER_SLUGS):
	@pdir="$(PAPERS_DIR)/$@"; \
	tex="$$pdir/$@.tex"; \
	if [ -f "$$tex" ]; then \
	    echo ">> building $@ PDF"; \
	    cd "$$pdir" && pdflatex -interaction=nonstopmode "$@.tex" >/dev/null && \
	        (bibtex "$@" >/dev/null 2>&1 || true) && \
	        pdflatex -interaction=nonstopmode "$@.tex" >/dev/null && \
	        pdflatex -interaction=nonstopmode "$@.tex" >/dev/null; \
	else \
	    echo ">> skipping $@ (tex not yet drafted)"; \
	fi

arxiv: pdfs
	@mkdir -p "$(RELEASE_DIR)"
	@for s in $(PAPER_SLUGS); do \
	    pdir="$(PAPERS_DIR)/$$s"; \
	    if [ -f "$$pdir/$$s.tex" ] && [ -f "$$pdir/$$s.pdf" ]; then \
	        echo ">> assembling arxiv tarball for $$s"; \
	        (cd "$$pdir" && tar czf "$(RELEASE_DIR)/$$s.tar.gz" \
	            "$$s.tex" references.bib "$$s.pdf" 2>/dev/null) || true; \
	    else \
	        echo ">> skipping $$s arxiv tarball (artifacts missing)"; \
	    fi; \
	done

clean:
	@for s in $(PAPER_SLUGS); do \
	    pdir="$(PAPERS_DIR)/$$s"; \
	    rm -f "$$pdir"/*.aux "$$pdir"/*.log "$$pdir"/*.bbl \
	          "$$pdir"/*.blg "$$pdir"/*.out "$$pdir"/*.toc; \
	done

distclean: clean
	rm -rf "$(RELEASE_DIR)"

release: all
	@echo ">> tag and bundle a v600-programme release"
	@echo "   git tag v600-programme-v1.0  (manual)"
	@echo "   release artifacts in: $(RELEASE_DIR)"
