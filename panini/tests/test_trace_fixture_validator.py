#!/usr/bin/env python3
"""Negative fixtures for the read-only trace fixture validator."""

from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path


PANINI = Path(__file__).resolve().parents[1]
VALIDATOR = PANINI / "tools" / "validate_trace_fixtures.py"
BASE = """\
fixture_id: trace-fixture:test
result: {status: partial}
states:
  - {id: state:fixture:before}
  - {id: state:fixture:after}
events:
  - event_id: evt:01
    kind: rule-decision
    depends_on: []
    provenance: [prov:test]
    payload: {rule: "1.1.1", decision: selected}
  - event_id: evt:02
    kind: state-transition
    depends_on: [evt:01]
    provenance: [prov:test]
    payload: {rule: "1.1.1", before: state:fixture:before, after: state:fixture:after, operation: test-transition}
  - event_id: evt:03
    kind: trace-terminated
    depends_on: [evt:02]
    provenance: [prov:test]
    payload: {outcome: partial}
"""


def rejects(name: str, document: str) -> None:
    root = Path(tempfile.mkdtemp())
    try:
        (root / "case.yaml").write_text(document, encoding="utf-8")
        result = subprocess.run(["python3", str(VALIDATOR), "--root", str(root)], text=True, capture_output=True, check=False)
        if result.returncode == 0:
            raise AssertionError(f"{name}: validator unexpectedly accepted invalid fixture")
    finally:
        shutil.rmtree(root)


rejects("missing selected dependency", BASE.replace("depends_on: [evt:01]", "depends_on: []", 1))
rejects("unknown state", BASE.replace("state:fixture:after", "state:fixture:missing", 1))
rejects("cyclic dependencies", BASE.replace("depends_on: []", "depends_on: [evt:03]", 1))

bad_digest = BASE.replace(
    "states:\n  - {id: state:fixture:before}\n  - {id: state:fixture:after}\n",
    "states:\n  - {id: state:fixture:before}\n  - {id: state:sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa, serialization: canonical-json-sha256-v0.1}\n",
)
rejects("mismatched canonical digest", bad_digest)
print("trace fixture validator negative fixtures: PASS")
