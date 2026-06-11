"""Make `src` importable as a top-level package when pytest runs from the
papers/cosmological-folding-rate/ directory."""
import os
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
