"""pytest fixtures for the V_600 programme test suite.

Adds the lib/ directory to sys.path so `import vfd_v600` works.
"""
from __future__ import annotations

import sys
from pathlib import Path

LIB = Path(__file__).resolve().parents[1] / "lib"
if str(LIB) not in sys.path:
    sys.path.insert(0, str(LIB))


import pytest

from vfd_v600.group import build_state


@pytest.fixture(scope="session")
def state():
    return build_state()
