#!/usr/bin/env python3
"""Run the portable-loader negative fixtures against a supplied My Lisp executable.

Each negative fixture must be rejected (nonzero exit or runtime diagnostic).
A fixture that loads cleanly is a loader failure, because the compatibility
contract forbids undocumented helpers and malformed `def` forms.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


PANINI = Path(__file__).resolve().parents[1]
NEGATIVE_DIR = PANINI / "machine" / "negative-fixtures"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runtime", required=True, type=Path, help="path to the My Lisp executable")
    args = parser.parse_args()
    failures: list[str] = []
    seen = 0
    for fixture in sorted(NEGATIVE_DIR.glob("*.my")):
        seen += 1
        result = subprocess.run(
            [str(args.runtime), str(fixture)],
            cwd=PANINI.parent,
            capture_output=True,
            check=False,
        )
        stdout = result.stdout.decode("utf-8", errors="replace") if isinstance(result.stdout, bytes) else result.stdout
        stderr = result.stderr.decode("utf-8", errors="replace") if isinstance(result.stderr, bytes) else result.stderr
        transcript = stdout + stderr
        rejected = result.returncode != 0 or any(marker in transcript for marker in ("Error:", "unknown symbol"))
        print(f"negative fixture {fixture.name}: {'REJECTED (ok)' if rejected else 'ACCEPTED (FAIL)'}")
        if not rejected:
            failures.append(f"{fixture.name} loaded cleanly but must be rejected")
    if seen == 0:
        failures.append("no negative fixtures found")
    if failures:
        print("PORTABLE LOADER NEGATIVE: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"PORTABLE LOADER NEGATIVE: PASS ({seen} fixtures rejected)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
