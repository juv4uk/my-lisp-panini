#!/usr/bin/env python3
"""Run the canonical Panini Machine gate against one My Lisp executable.

The gate is intentionally evidence-preserving: it always runs capability
probe, negative loader checks, and acceptance in that order. A failed probe
does not suppress later checks, because those checks may reveal an independent
loader or fixture result. This script neither builds nor modifies My Lisp.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


PANINI = Path(__file__).resolve().parents[1]


def run(label: str, command: list[str]) -> bool:
    print(f"\n[PANINI-MACHINE-GATE] {label}: start", flush=True)
    result = subprocess.run(command, cwd=PANINI.parent, check=False)
    outcome = "PASS" if result.returncode == 0 else f"FAIL (exit {result.returncode})"
    print(f"[PANINI-MACHINE-GATE] {label}: {outcome}")
    return result.returncode == 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runtime", required=True, type=Path, help="path to the My Lisp executable")
    parser.add_argument("--source-repo", type=Path, help="optional My Lisp checkout for revision provenance")
    args = parser.parse_args()

    python = sys.executable
    probe = [python, "panini/tests/probe_mylisp_runtime.py", "--runtime", str(args.runtime)]
    if args.source_repo is not None:
        probe.extend(("--source-repo", str(args.source_repo)))

    results = [
        run("runtime-capability", probe),
        run(
            "portable-negative-loader",
            [python, "panini/tests/run_loader_negative.py", "--runtime", str(args.runtime)],
        ),
        run(
            "machine-acceptance",
            [python, "panini/tests/run_machine_acceptance.py", "--runtime", str(args.runtime)],
        ),
    ]
    if all(results):
        print("\nPANINI PORTABLE MACHINE GATE: PASS")
        return 0
    print("\nPANINI PORTABLE MACHINE GATE: BLOCKED OR FAILING")
    print("Inspect each stage above; do not infer a Paninian result from runtime failure.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
