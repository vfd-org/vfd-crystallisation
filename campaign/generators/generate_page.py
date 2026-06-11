"""Generate a self-contained canonical result page (HTML) for a claim.

Usage:  python3 campaign/generators/generate_page.py <slug>
        python3 campaign/generators/generate_page.py --all

One claim, the numbers, the inputs, the falsifier, and a copy-paste
verification block. Nothing else on the page — this is the campaign
landing page, not the programme manifesto.
"""
import html
import os
import sys

import lib

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
  :root {{ --ink:#1a1f2b; --soft:#5b6472; --line:#e3e6eb; --accent:#0b6e4f; --bg:#fbfbf9; }}
  * {{ box-sizing:border-box; }}
  body {{ font:17px/1.65 Georgia,'Times New Roman',serif; color:var(--ink);
         background:var(--bg); margin:0; }}
  main {{ max-width:760px; margin:0 auto; padding:48px 24px 96px; }}
  h1 {{ font-size:1.7em; line-height:1.25; margin:0 0 .4em; }}
  .claim {{ font-size:1.12em; color:var(--soft); margin-bottom:2em; }}
  .numbers {{ display:flex; gap:16px; flex-wrap:wrap; margin:2em 0; }}
  .num {{ flex:1 1 180px; border:1px solid var(--line); border-radius:8px;
          padding:14px 18px; background:#fff; }}
  .num b {{ display:block; font-size:1.35em; font-family:ui-monospace,Menlo,monospace; }}
  .num span {{ color:var(--soft); font-size:.85em; }}
  .err b {{ color:var(--accent); }}
  h2 {{ font-size:1.05em; letter-spacing:.04em; text-transform:uppercase;
        color:var(--soft); border-bottom:1px solid var(--line);
        padding-bottom:.3em; margin-top:2.4em; }}
  ol li {{ margin:.45em 0; }}
  pre {{ background:#11151d; color:#dde3ec; padding:18px 20px; border-radius:8px;
         overflow-x:auto; font:14px/1.6 ui-monospace,Menlo,monospace; }}
  .falsifier {{ border-left:3px solid var(--accent); padding:.2em 0 .2em 1em;
                color:var(--ink); }}
  a {{ color:var(--accent); }}
  footer {{ margin-top:3em; color:var(--soft); font-size:.85em;
            border-top:1px solid var(--line); padding-top:1em; }}
</style>
</head>
<body>
<main>
  <h1>{title}</h1>
  <p class="claim">{claim}</p>

  <div class="numbers">
    <div class="num"><b>{value}</b><span>this computation</span></div>
    <div class="num"><b>{target}</b><span>measured / independent</span></div>
    <div class="num err"><b>{error}</b><span>difference</span></div>
  </div>

  <h2>Everything that goes in</h2>
  <ol>
{inputs}
  </ol>

  <h2>Run it yourself</h2>
  <pre>{runblock}</pre>

  <h2>How to kill this claim</h2>
  <p class="falsifier">{falsifier}</p>

  <h2>Links</h2>
  <ul>
{linkitems}
  </ul>

  <footer>One result, fully stated. Pre-peer-review; every input and the
  falsifier are above. Part of the VFD programme &mdash; but this page stands
  or falls on its own.</footer>
</main>
</body>
</html>
"""


def render(claim):
    e = html.escape
    links = claim["links"]
    repo = links.get("repo", "")
    if repo in ("", "PENDING_PUSH"):
        runblock = "# repo not yet public — verification currently requires the\n" \
                   "# local bundle at: %s\ncd %s\n%s" % (
                       links.get("local", "?"), claim["script"]["cwd"], claim["script"]["cmd"])
    else:
        runblock = "git clone %s\ncd %s\n%s   # deps: %s" % (
            repo, claim["script"]["cwd"], claim["script"]["cmd"],
            claim["script"].get("deps", "none"))

    linkitems = []
    for key in ("repo", "external", "paper"):
        val = links.get(key)
        if not val or val == "PENDING_PUSH":
            continue
        sval = str(val)
        if sval.startswith("http"):
            linkitems.append('    <li><a href="%s">%s</a> (%s)</li>' % (e(sval), e(sval), key))
        else:
            linkitems.append("    <li>%s: %s</li>" % (key, e(sval)))

    return PAGE.format(
        title=e(claim["title"]),
        claim=e(claim["claim"].strip()),
        value=e(str(claim["value"])),
        target=e(str(claim["target"])),
        error=e(str(claim["error"])),
        inputs="\n".join("    <li>%s</li>" % e(x) for x in claim["inputs"]),
        runblock=e(runblock),
        falsifier=e(claim["falsifier"].strip()),
        linkitems="\n".join(linkitems),
    )


def main():
    outdir = lib.ensure_outdir("pages")
    for claim in lib.claims_arg(sys.argv):
        out = os.path.join(outdir, "%s.html" % claim["slug"])
        with open(out, "w") as fh:
            fh.write(render(claim))
        print("wrote %s" % os.path.relpath(out, lib.REPO_ROOT))


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    main()
