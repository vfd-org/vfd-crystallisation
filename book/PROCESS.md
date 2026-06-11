# Book Production Process — *The Crystal and the Clock*

How this book gets made. The goal is a finished, publishable manuscript that reads as though one human wrote it over a couple of years — not a generated artifact. Every chapter passes through the same pipeline; the whole book then gets a holistic pass before it is called done.

The two non-negotiables, stated once so they govern everything below:

1. **It must not read as AI-written.** This is a hard gate, enforced by `book/STYLE.md`. Formatting, punctuation (especially em-dashes), sentence rhythm, vocabulary, and structure all get checked against the anti-tell rules. A chapter that trips the AI-tell detector is not done, no matter how good the content.
2. **Honesty contract.** Core (verifiable) and frontier (interpretive/open) stay visibly separated, per `book/OUTLINE.md`. The book earns trust by never letting the precision of the math lend false weight to the speculation.

---

## The per-chapter cycle

Each chapter runs this loop. Codex (the external CLI, read-only) is the reviewer/editor at the marked stages; Claude drafts and revises between them. This mirrors the codex pair-programmer loop already used for the math docs (`feedback_codex_review_workflow`), retargeted to prose.

**Stage 0 — Brief.** Before drafting, write a one-paragraph chapter brief: the single idea this chapter delivers, the concrete anchor it opens from, the one analogy it leans on, what the reader can now do/understand that they couldn't before, and the forward hook. (One idea per chapter — Hawking's discipline.)

**Stage 1 — Draft.** Write the chapter against the brief and `STYLE.md`. Aim for the chapter's natural length, not a target word count.

**Stage 2 — Developmental review (codex).** Codex reads the chapter as a *developmental editor*: does the argument land, is the analogy doing real work, is anything unclear or assumed, does the honesty contract hold, does it earn its emotional beats, does it pull forward? Output: ranked structural notes. Not line edits yet.

**Stage 3 — Revise** to the developmental notes.

**Stage 4 — Line + AI-tell review (codex).** Codex reads as a *line editor and AI-tell auditor*: sentence-level craft, rhythm, and a hard pass against the `STYLE.md` anti-tell list (em-dash count and density, formulaic constructions, intensifier abuse, tricolon overuse, robotic signposting, vocabulary tells, suspiciously even paragraph lengths). Output: specific fixes with line references, plus an AI-tell score.

**Stage 5 — Voice revise.** Apply the line edits and, critically, *de-AI* the prose: vary sentence length hard, cut em-dashes to a human density, break symmetry, let some sentences be plain and a few be rough, kill the tell-vocabulary. This is where the chapter stops sounding generated.

**Stage 6 — Figures.** Identify the 1–3 figures the chapter needs (see Figure tracks below), generate them, write captions in the book's voice.

**Stage 7 — Copy/proof (codex, light).** Final consistency, repetition across chapters, terminology, caption/figure references. Quick.

**Stage 8 — Mark done** in the `OUTLINE.md` tracker (status → REVIEWED), record the AI-tell score and the figure list.

A chapter is "done" only after Stage 8. Drafted ≠ done.

---

## Figure tracks

A physics trade book lives or dies on its figures. Two tracks, used deliberately:

**Track A — Precise figures from real data.** The mathematical figures are generated from the *actual* substrate and verification scripts (matplotlib / the `scripts/` data), never faked. Examples: the Laplacian spectrum with its square-multiplicity blocks; a real projection of the 600-cell; the kernel's exponential decay; the dispersion curve; the cascade ladder. These carry the book's credibility — a reader can regenerate them. Style: clean, single-idea, generous white space, hand-labeled, restrained palette. The "you could check this yourself" figures.

**Track B — Evocative openers / concept art.** One image per part (or per chapter where it helps) that sets mood or makes an abstraction graspable: the crystal, the view-from-inside, the clock-mirror, the ladder. Generated via the image tools. Used sparingly — a trade book is not a coffee-table book. Never used where a precise figure would be more honest.

Rule: if a figure could be precise (Track A), it must be; Track B is only for genuinely non-quantitative imagery.

Figures live in `book/figures/`, named `chNN-slug.{png,pdf}`, with a generating script in `book/figures/scripts/` for every Track-A figure.

---

## The craft references

The writing is calibrated against the best of the genre. The working canon (techniques distilled in `STYLE.md`): Carroll (*The Big Picture*, *Something Deeply Hidden*) for honest speculation and level-headed structure; Hawking (*A Brief History of Time*) for the one-equation rule, everyday analogy, and humor; Greene (*The Elegant Universe*, *The Fabric of the Cosmos*) for the extended controlling analogy and patient layering; Rovelli (*Seven Brief Lessons*, *Reality Is Not What It Seems*) for brevity and lyricism; Feynman (*QED*, *The Character of Physical Law*) for radical clarity and reader empowerment; Sagan (*Cosmos*) for earned awe and the cosmic zoom; Tegmark (*Our Mathematical Universe*) for the maths-is-reality thesis handled honestly, and for first-person nerve. Penrose (*The Road to Reality*) is the cautionary counter-example: brilliant, and too technical to be trade.

---

## Whole-book pass (after all chapters are REVIEWED)

1. **Continuity & arc** (codex, book-level): does the through-line hold, do motifs (the crystal, the clock) pay off, are the what/how/why all delivered, is anything repeated or contradicted across chapters, does Part V honestly own the frontier.
2. **Cold read for voice** (codex + Claude): read the whole thing for AI-tells at book scale — cross-chapter sameness of rhythm is its own tell. Vary.
3. **Front/back matter:** title page, contents, preface (the honesty contract as a short author's note), notes-on-sources, "how to check the claims yourself" appendix pointing at the scripts, acknowledgements.
4. **Typeset to publishable format.** Target: LaTeX book class → PDF (most robust here, with real figures and math where needed), with an EPUB-friendly Markdown master kept in parallel. Decide final format at this stage.
5. **Final hostile read** (codex, as a skeptical science reviewer): is anything overclaimed, is the core/frontier line ever blurred, would a working physicist catch a cheat. Fix, then ship.

---

## Status

- Pipeline + style guide: established (this doc + `STYLE.md`).
- Ch1: drafted (v1, AI-flavored) → undergoing voice rewrite + first codex prose review (demonstrating the cycle).
- Figure pipeline: defined; first figures pending.
- Format decision: LaTeX book → PDF, Markdown master in parallel (provisional).
