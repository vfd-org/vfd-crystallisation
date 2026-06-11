"""Shared loader for the campaign claims registry."""
import os
import sys

import yaml

CAMPAIGN_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_ROOT = os.path.dirname(CAMPAIGN_DIR)
REGISTRY_DIR = os.path.join(CAMPAIGN_DIR, "registry")
OUTPUT_DIR = os.path.join(CAMPAIGN_DIR, "output")

REQUIRED_FIELDS = [
    "slug", "priority", "status", "segment", "title", "claim",
    "value", "target", "error", "inputs", "falsifier", "script",
    "links", "post_hook",
]


def load_registry():
    """Return all claims sorted by priority. Raises on schema violations."""
    claims = []
    for fname in sorted(os.listdir(REGISTRY_DIR)):
        if not fname.endswith(".yaml"):
            continue
        path = os.path.join(REGISTRY_DIR, fname)
        with open(path) as fh:
            claim = yaml.safe_load(fh)
        missing = [f for f in REQUIRED_FIELDS if f not in claim]
        if missing:
            raise ValueError("%s missing fields: %s" % (fname, ", ".join(missing)))
        if claim["slug"] != fname[:-5]:
            raise ValueError("%s: slug %r does not match filename" % (fname, claim["slug"]))
        claims.append(claim)
    return sorted(claims, key=lambda c: c["priority"])


def get_claim(slug):
    for claim in load_registry():
        if claim["slug"] == slug:
            return claim
    raise KeyError("no claim with slug %r in registry" % slug)


def blocking_todos(claim):
    """Things that must be fixed before this claim's content ships."""
    todos = []
    if claim["links"].get("repo") in (None, "", "PENDING_PUSH"):
        todos.append("Repo not public yet — push a clean verification repo before posting "
                     "(local source: %s)" % claim["links"].get("local", "?"))
    if claim.get("status") != "verified":
        todos.append("Claim status is %r, not 'verified' — run the script and confirm "
                     "before posting" % claim.get("status"))
    if not claim.get("figure"):
        todos.append("No figure attached yet (figure_idea: %s)"
                     % claim.get("figure_idea", "none").strip())
    return todos


def claims_arg(argv):
    """Resolve CLI arg to a list of claims: a slug, or --all."""
    if len(argv) > 1 and argv[1] != "--all":
        return [get_claim(argv[1])]
    return load_registry()


def ensure_outdir(sub):
    path = os.path.join(OUTPUT_DIR, sub)
    os.makedirs(path, exist_ok=True)
    return path


if __name__ == "__main__":
    for c in load_registry():
        print("%d  %-32s %-10s %s" % (c["priority"], c["slug"], c["status"], c["title"]))
    sys.exit(0)
