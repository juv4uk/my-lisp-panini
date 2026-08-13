#!/usr/bin/env python3
"""Run a pinned external SLP1 round-trip fixture without changing registry data."""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate


SCHEMES = {
    "IAST": sanscript.IAST,
    "DEVANAGARI": sanscript.DEVANAGARI,
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", type=Path)
    args = parser.parse_args()
    fixture = yaml.safe_load(args.fixture.read_text(encoding="utf-8"))

    failures: list[str] = []
    for case in fixture["cases"]:
        source = case["slp1"]
        for target, expected_key in (("IAST", "expected_iast"), ("DEVANAGARI", "expected_devanagari")):
            rendered = transliterate(source, sanscript.SLP1, SCHEMES[target])
            round_trip = transliterate(rendered, SCHEMES[target], sanscript.SLP1)
            expected = case[expected_key]
            ok = rendered == expected and round_trip == source
            print(
                f"{'PASS' if ok else 'FAIL'} {case['id']} {target} "
                f"rendered={rendered!r} round_trip={round_trip!r}"
            )
            if not ok:
                failures.append(case["id"] + ":" + target)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
