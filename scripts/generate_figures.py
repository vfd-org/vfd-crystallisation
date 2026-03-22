#!/usr/bin/env python3
"""Generate publication figures for the VFD Crystallisation preprint."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import matplotlib
matplotlib.use("Agg")

from vfd.crystallisation.figures import generate_preprint_figures, generate_all_figures

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "preprint"
    output_dir = os.path.join(os.path.dirname(__file__), "..", "figures", "preprint")
    os.makedirs(output_dir, exist_ok=True)

    if mode == "all":
        figs = generate_all_figures(output_dir)
        print(f"Generated {len(figs)} figures (preprint + companion)")
    else:
        figs = generate_preprint_figures(output_dir)
        print(f"Generated {len(figs)} flagship figures")

    for name in figs:
        print(f"  {name}")
