#!/usr/bin/env python3
"""Negative fixtures for the read-only registry validator."""

from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path


PANINI = Path(__file__).resolve().parents[1]
VALIDATOR = PANINI / "tools" / "validate_registry.py"
BASE = "canonical: kartf\niast: kartṛ\nclass: karaka\ndefined_by:\n  - sutra: \"1.4.54\"\n"


def fixture_root() -> Path:
    root = Path(tempfile.mkdtemp()) / "panini"
    for kind in ("sutras", "dhatu", "karaka", "samjna"):
        (root / "registry" / kind).mkdir(parents=True, exist_ok=True)
    (root / "registry" / "sutras" / "index.yaml").write_text("sutras:\n  1.4.54: {}\n", encoding="utf-8")
    return root


def rejects(name: str, record: str, strict: bool = False) -> None:
    root = fixture_root()
    try:
        (root / "registry" / "karaka" / "case.yaml").write_text(record, encoding="utf-8")
        args = ["python3", str(VALIDATOR), "--root", str(root)]
        if strict:
            args.append("--strict-provenance")
        result = subprocess.run(args, text=True, capture_output=True, check=False)
        if result.returncode == 0:
            raise AssertionError(f"{name}: validator unexpectedly accepted invalid fixture")
    finally:
        shutil.rmtree(root.parent)


rejects("missing provenance", BASE, strict=True)
rejects("unsupported certainty", BASE + "evidence:\n  status: certain\n")
rejects("non-SLP1 canonical", BASE.replace("kartf", "kartṛ"))
print("registry provenance negative fixtures: PASS")
