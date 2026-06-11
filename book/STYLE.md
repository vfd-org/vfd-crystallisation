# Style Guide — *The Crystal and the Clock*

Two jobs. First, write like the best popular physics, not like a textbook and not like a press release. Second, read like a human did it. The second job is a hard gate: a chapter that sounds generated fails, however clear it is.

---

## Part 1 — Craft, distilled from the genre

These are the moves the best science writers actually make. Use them on purpose.

**One idea per chapter.** Hawking's discipline. Each chapter delivers a single load you can name in a sentence. Everything else serves it. If a chapter has two big ideas, it is two chapters.

**Concrete before abstract, always.** Never open a hard idea cold. Open with something the reader can see, hold, or remember — a room, a clock, a coastline, a coin — and let the abstraction grow out of it. Greene never says "spacetime curvature"; he rolls a marble on a trampoline first.

**One controlling analogy, carried.** Pick the chapter's central image and stay with it; don't switch metaphors every paragraph (a classic generated-text habit). A good analogy is a place the reader can return to. The book's spine images are the crystal and the clock; protect them.

**The minimal-math rule, with rare vivid exceptions.** Hawking's editor told him each equation halves sales. Mostly obey it. But when one number is the whole point — three, here — make it land hard and let the reader feel they could check it. Feynman drew arrows instead of writing amplitudes; do that.

**Empower the reader.** The strongest move in the genre is "you could see this for yourself." Feynman's arrows, Sagan's "try it tonight." When a claim is checkable, say so and show the door, don't just assert.

**Earn the awe.** Sagan and Rovelli reach for wonder, but only after the ground is laid. Wonder asserted is sentimental; wonder arrived at is the best thing the genre does. Put the lyrical beat at the end of a careful build, never at the start.

**Honest about the frontier.** Carroll and Feynman are trusted because they say "we don't know" and "this is my guess" out loud. Make the uncertainty a feature. The reader relaxes when they can tell you'll warn them before you speculate.

**The reader is a smart friend.** Never condescend, never flatter, never "as you surely know." Explain the genuinely hard thing fully and assume they can follow if you lead well.

**Vary the register.** Plain explanatory valleys, occasional lyrical peaks, the odd dry joke for relief (Hawking). A whole chapter at the same emotional pitch is exhausting and, at book scale, a tell.

**End on a pull.** Each chapter closes by opening the next question. Not a summary — a hook. "But to understand that, we first need to ask…"

**Personal, lightly.** First person ("I want to show you") is the chosen voice. Use it for stance and judgment, not autobiography. Tegmark's nerve, not his life story.

---

## Part 2 — The anti-AI-tell rules (the hard gate)

Generated prose has a smell. These are the tells, and the fixes. Codex audits every chapter against this list and returns a score.

### Punctuation

- **Em-dashes: ration them.** The single biggest tell. Target **at most ~2–3 em-dashes per 1000 words**, and never two in one sentence, never the "em-dash sandwich" aside as a default move. Replace with: a full stop (best — just start a new sentence), a comma, a colon, parentheses, or a rewrite. The draft of Ch1 had dozens; that is the disease.
- **No semicolon tic either.** A few are fine and human; a semicolon in every other sentence is its own machine signature. Vary.
- **Real punctuation, human spacing.** Straight quotes or curly, consistently. Hyphens are hyphens; don't use hyphens where a human would just write two words.

### Sentence-level

- **Vary length violently.** Generated text drifts to a uniform 15–25 word sentence. Break it. Put a four-word sentence next to a forty-word one. A fragment, occasionally, for punch. Read it aloud; if the rhythm is metronomic, it fails.
- **Kill negative parallelism.** "It's not X, it's Y." "Not because A, but because B." "This isn't merely P; it's Q." These balanced antitheses are the most recognizable generated cadence. Allow *one* per chapter, maximum, where it genuinely earns its place.
- **Kill the tricolon reflex.** Lists of three ("clear, honest, and precise") feel authoritative and are wildly overused by models. Sometimes use two. Sometimes four. Sometimes just one, well chosen.
- **Don't open every paragraph with a signpost.** "Now," "So," "Here's the thing," "But here's where it gets interesting," "Let me explain." A human starts paragraphs many different ways, including mid-thought.
- **Cut filler intensifiers.** "genuinely," "precisely," "exactly," "simply," "literally," "truly," "remarkably," "embarrassingly," "magnificently," "deeply." They feel like emphasis and add nothing. Earn emphasis with the noun, not the adverb.

### Vocabulary (the dead giveaways)

Avoid, basically always: *delve, tapestry, testament, realm, intricate, multifaceted, nuanced, robust, crucial, pivotal, underscore, navigate (figurative), landscape (figurative), beacon, symphony (as cliché), dance (as in "the dance of"), at its core, it's worth noting, it's important to note, in essence, ultimately, profound, profoundly.* If a word feels like it came from a "make this sound smart" setting, cut it.

### Structure

- **No bullet lists in the prose.** A trade book is paragraphs. Lists are a slide-deck habit. (Lists are fine in *these* process docs; never in a chapter.)
- **No bolded key terms scattered through the text.** Italics, once, on first introduction of a real term, is enough. Bold-peppering is a web-content tell.
- **No section headers every 200 words.** Chapters flow. A couple of section breaks at most, and only at genuine turns.
- **No "In conclusion" / wrap-up paragraph that restates.** End on the forward pull instead.
- **Vary paragraph length.** Some one sentence. Some long. Even, regular paragraph blocks are a tell.

### The aboutness tells

- **Don't hedge robotically.** "It could be argued that," "in many ways," "to a certain extent." State it, then own the uncertainty honestly where it's real.
- **Don't over-transition.** Not every paragraph needs to smoothly hand off to the next. Humans jump, double back, leave a thought slightly unresolved.
- **Have a stance.** Generated prose is suspiciously balanced and opinionless. The narrator should think things, find things beautiful or annoying, prefer one reading over another, and say so.

---

## Part 3 — The codex review rubric (what every prose review checks)

Developmental pass: one nameable idea? concrete anchor? analogy carried, not switched? honesty contract intact (core vs frontier marked)? awe earned, not asserted? forward pull at the end?

Line + AI-tell pass: em-dash count and per-1000-word density (report the number); negative-parallelism instances (list them); tricolon count; signpost-opener count; intensifier and dead-vocabulary hits (list them); sentence-length variance (flag if too uniform); list/bold/header tells; overall **AI-tell score 0–10** (0 = indistinguishable from a careful human author, 10 = obviously generated) with the top offenders cited by line.

Target to pass a chapter: AI-tell score ≤ 2, em-dash density ≤ 3 per 1000 words, zero unfixed dead-vocabulary hits.
