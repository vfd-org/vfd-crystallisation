#!/usr/bin/env python3
"""Run the closure-positivity laboratory: build the table, run the gate, and search
for the structural feature that decides B-positivity.

    python3 run_lab.py            # prints the table + discriminator, writes out/lab_table.json
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lab import registry, discriminator_search          # noqa: E402

OUT = os.path.join(HERE, "out")


def main():
    objs = registry()
    rows = [o.verdict() for o in objs]
    os.makedirs(OUT, exist_ok=True)

    # ---- the table
    hdr = f"{'object':<34}{'fix':>4}{'s.adj':>6}{'B>0':>5}{'realσ':>6}{'tot+':>6}{'pos?':>6}  verdict"
    print(hdr); print("-" * len(hdr))
    for r in rows:
        print(f"{r['name']:<34}{_b(r['is_fixed_point']):>4}{_b(r['self_adjoint']):>6}"
              f"{_b(r['form_posdef']):>5}{_b(r['real_spectrum']):>6}"
              f"{_b(r['totally_positive']):>6}{_b(r['B_positive']):>6}  {r['positivity']}")

    # ---- the discriminator search
    disc = discriminator_search(objs)
    print("\nDISCRIMINATOR SEARCH  (over self-adjoint, finite-decidable objects):")
    print(f"  pool = {disc['n_decidable']}  ({disc['n_positive']} positive)")
    for f, d in disc["by_feature"].items():
        mark = "  <-- EXACT" if d["exact_match"] else ""
        print(f"  {f:<18} predicts B_positive on {d['agreement']}/{d['of']}{mark}")

    winners = [f for f, d in disc["by_feature"].items() if d["exact_match"]]
    print("\nCANDIDATE VFD POSITIVITY LAW:")
    if winners:
        print(f"  B-positive  <=>  {' & '.join(winners)}   (self-adjointness = necessary "
              "precondition; this is the missing sufficient ingredient)")
    else:
        print("  no single feature separates the pool yet -- add objects / features")
    print("  RH instance: the icosian object is self-adjoint & finite-positive, but its")
    print("  ALL-PLACES (Weil) total positivity is RH(L) -- left OPEN, gated separately.")

    json.dump({"table": rows, "discriminator": disc}, open(os.path.join(OUT, "lab_table.json"), "w"),
              indent=1)
    print(f"\nwrote {os.path.join('out', 'lab_table.json')}")


def _b(x):
    return "Y" if x else ("." if x is False else "?")


if __name__ == "__main__":
    main()
