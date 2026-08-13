#!/usr/bin/env python3
"""Executable negative and positive checks for the offline acquisition validator."""

from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path


PANINI = Path(__file__).resolve().parents[1]
VALIDATOR = PANINI / "tools" / "validate_siva_acquisition_record.py"
VALID = """\
id: acquisition:siva-sutras:example:2026-08-14T00:00:00Z
subject: siva-sutras-phoneme-ordering
source:
  title: Example fourteen-row table
  canonical_url: https://example.invalid/siva
  retrieved_at: "2026-08-14T00:00:00Z"
  publisher_revision: none
rights:
  license: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  attribution: Example publisher
  reuse_status: permitted
artifact:
  local_path: sources/siva-sutras/example.txt
  sha256: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
  media_type: text/plain
  byte_count: 42
  fetch_method: reviewed-command
conversion:
  input_representation: IAST
  output_representation: SLP1
  converter: manual-checked
  conversion_record: conversion:siva-sutras:example-v1
verification:
  row_check: pass
  compared_to:
    - registry/siva-sutras/siva-sutras-slp1-provisional-v0.1.yaml
    - tests/pratyahara-exhaustive-v0.1.yaml
  reviewer: panini-test
status: verified
"""


def run(document: str, expected: int) -> None:
    root = Path(tempfile.mkdtemp())
    try:
        record = root / "record.yaml"
        record.write_text(document, encoding="utf-8")
        result = subprocess.run(["python3", str(VALIDATOR), str(record)], text=True, capture_output=True, check=False)
        if result.returncode != expected:
            raise AssertionError(result.stdout + result.stderr)
    finally:
        shutil.rmtree(root)


run(VALID, 0)
run(VALID.replace("reuse_status: permitted", "reuse_status: unresolved"), 1)
run(VALID.replace("sha256: a", "sha256: A", 1), 1)
run(VALID.replace("row_check: pass", "row_check: pending"), 1)
run(VALID.replace("https://example.invalid/siva", "http://example.invalid/siva"), 1)
print("siva acquisition record validator: PASS")
