#!/usr/bin/env python3
"""Report whether a My Lisp executable satisfies Panini machine requirements.

The probe does not build, modify, or otherwise configure My Lisp. It records
the observable capabilities of the exact executable supplied by the caller.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


SHA256_ABC = "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
PANINI = Path(__file__).resolve().parents[1]
FIXTURE = PANINI / "tests" / "runtime-capability-probe.my"


def revision(source_repo: Path | None) -> str:
    if source_repo is None:
        return "not-requested"
    result = subprocess.run(
        ["git", "-C", str(source_repo), "rev-parse", "HEAD"],
        text=True,
        capture_output=True,
        check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else "unavailable"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runtime", required=True, type=Path)
    parser.add_argument("--source-repo", type=Path, help="optional My Lisp checkout for revision provenance")
    args = parser.parse_args()
    result = subprocess.run(
        [str(args.runtime), str(FIXTURE.relative_to(PANINI.parent))],
        cwd=PANINI.parent,
        text=True,
        capture_output=True,
        check=False,
    )
    transcript = result.stdout + result.stderr
    print(f"runtime={args.runtime}")
    print(f"source_revision={revision(args.source_repo)}")
    print(transcript, end="")
    required = ("[PANINI-RUNTIME-PROBE] start", SHA256_ABC, "machine-fixture", "[PANINI-RUNTIME-PROBE] complete")
    failures = [item for item in required if item not in transcript]
    if result.returncode != 0:
        failures.append(f"runtime-exit-{result.returncode}")
    if "Error:" in transcript or "unknown symbol" in transcript:
        failures.append("runtime-diagnostic")
    if failures:
        print("PANINI MYLISP RUNTIME CAPABILITY: FAIL")
        for failure in failures:
            print(f"- missing-or-invalid: {failure}")
        return 1
    print("PANINI MYLISP RUNTIME CAPABILITY: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
