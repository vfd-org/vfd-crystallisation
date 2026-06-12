-- Wrap any ::: {.codebox} fenced div in a LaTeX `codebox` environment for the
-- PDF build, while leaving the <div class="codebox"> intact for HTML/EPUB.
-- The raw-latex markers are dropped automatically by the HTML/EPUB writers,
-- and the Div renders transparently in LaTeX, so one source serves all three.
function Div(el)
  if el.classes:includes("codebox") then
    table.insert(el.content, 1, pandoc.RawBlock("latex", "\\begin{codebox}"))
    table.insert(el.content, pandoc.RawBlock("latex", "\\end{codebox}"))
    return el
  end
end
