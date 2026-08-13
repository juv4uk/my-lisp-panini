#!/usr/bin/env python3
"""Run the Panini machine suite against a supplied My Lisp executable.

This is an acceptance harness, not a Pāṇinian source oracle. It fails on REPL
diagnostics as well as a nonzero process exit because the current REPL reports
some evaluation errors while exiting successfully.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


PANINI = Path(__file__).resolve().parents[1]
ENTRYPOINT = "panini/tests/machine-acceptance.my"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runtime", required=True, type=Path, help="path to the My Lisp executable")
    args = parser.parse_args()
    result = subprocess.run(
        [str(args.runtime), ENTRYPOINT],
        cwd=PANINI.parent,
        capture_output=True,
        check=False,
    )
    stdout = result.stdout.decode("utf-8", errors="replace") if isinstance(result.stdout, bytes) else result.stdout
    stderr = result.stderr.decode("utf-8", errors="replace") if isinstance(result.stderr, bytes) else result.stderr
    transcript = stdout + stderr
    print(transcript, end="")
    failures: list[str] = []
    if result.returncode:
        failures.append(f"runtime exited {result.returncode}")
    for marker in ("Error:", "[FAIL]", "unknown symbol"):
        if marker in transcript:
            failures.append(f"runtime emitted {marker!r}")
    if "[PANINI-LISP-ACCEPTANCE] start" not in transcript:
        failures.append("Lisp acceptance entry point did not start")
    if "Tests complete." not in transcript:
        failures.append("run-tests did not reach its completion marker")
    if failures:
        print("PANINI MACHINE ACCEPTANCE: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("PANINI MACHINE ACCEPTANCE: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
