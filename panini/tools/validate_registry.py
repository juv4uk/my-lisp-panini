#!/usr/bin/env python3
"""Read-only validator for the small Panini YAML registries.

It emits diagnostics and returns non-zero on errors. It never writes or
normalizes registry data.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml

SLP1 = set("aAiIuUfFxXeEoOkKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzshMH'")
SUTRA_ID = re.compile(r"^[1-8]\.[1-4]\.[0-9]+$")
IAST_MAP = {
    "A": "ā", "I": "ī", "U": "ū", "f": "ṛ", "F": "ṝ", "x": "ḷ", "X": "ḹ",
    "E": "ai", "O": "au", "K": "kh", "G": "gh", "N": "ṅ", "C": "ch", "J": "jh",
    "Y": "ñ", "w": "ṭ", "W": "ṭh", "q": "ḍ", "Q": "ḍh", "R": "ṇ", "T": "th",
    "D": "dh", "P": "ph", "B": "bh", "S": "ś", "z": "ṣ", "M": "ṃ", "H": "ḥ",
}
ALLOWED = {
    "dhatu": {"canonical", "display", "class", "gana", "pada", "set_anit", "source", "traditional_meaning", "notes", "evidence", "dhatupatha_code", "source_form", "gana_disputed", "homonyms"},
    "karaka": {"canonical", "iast", "display", "class", "definition", "defined_by", "relations", "caveats", "examples", "sources", "extending_sutras"},
    "samjna": {"canonical", "display", "class", "scope", "defined_by", "ontology", "caveats", "sources"},
}


class Reporter:
    def __init__(self) -> None:
        self.errors = 0
        self.warnings = 0

    def emit(self, level: str, path: Path, message: str) -> None:
        print(f"{level} {path.as_posix()}: {message}")
        if level == "ERROR":
            self.errors += 1
        elif level == "WARN":
            self.warnings += 1


def load(path: Path, reporter: Reporter) -> dict[str, Any] | None:
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        reporter.emit("ERROR", path, f"cannot parse YAML: {exc}")
        return None
    if not isinstance(value, dict):
        reporter.emit("ERROR", path, "top level must be a mapping")
        return None
    return value


def to_iast(slp1: str) -> str:
    return "".join(IAST_MAP.get(ch, ch) for ch in slp1)


def validate_record(path: Path, data: dict[str, Any], expected: str, sutras: set[str], seen: dict[str, Path], reporter: Reporter) -> None:
    canonical = data.get("canonical")
    if not isinstance(canonical, str) or not canonical:
        reporter.emit("ERROR", path, "missing non-empty canonical SLP1 identifier")
        return
    bad = sorted(set(canonical) - SLP1)
    if bad:
        reporter.emit("ERROR", path, f"canonical contains unsupported SLP1 glyphs: {''.join(bad)!r}")
    if canonical in seen:
        reporter.emit("ERROR", path, f"duplicate canonical {canonical!r}; first seen in {seen[canonical]}")
    else:
        seen[canonical] = path
    if data.get("class") != expected:
        reporter.emit("ERROR", path, f"class must be {expected!r}")
    unknown = sorted(set(data) - ALLOWED[expected])
    if unknown:
        reporter.emit("ERROR", path, f"unsupported metadata keys: {', '.join(unknown)}")
    display = data.get("display")
    iast = display.get("iast") if isinstance(display, dict) else data.get("iast")
    if not isinstance(iast, str) or not iast:
        reporter.emit("ERROR", path, "missing IAST display")
    elif to_iast(canonical) != iast:
        reporter.emit("ERROR", path, f"SLP1→IAST mismatch: {canonical!r} maps to {to_iast(canonical)!r}, not {iast!r}")
    deva = display.get("devanagari") if isinstance(display, dict) else None
    if expected in {"dhatu", "samjna"} and (not isinstance(deva, str) or not deva):
        reporter.emit("ERROR", path, "missing Devanagari display")
    if expected == "dhatu" and not isinstance(data.get("source"), dict):
        reporter.emit("ERROR", path, "dhatu record requires a source mapping")
    definitions = data.get("defined_by", [])
    if expected in {"karaka", "samjna"} and not isinstance(definitions, list):
        reporter.emit("ERROR", path, f"{expected} record requires a defined_by list")
    if isinstance(definitions, list):
        for entry in definitions:
            sid = entry.get("sutra") if isinstance(entry, dict) else None
            if not isinstance(sid, str) or not SUTRA_ID.fullmatch(sid):
                reporter.emit("ERROR", path, "defined_by entry needs a valid sutra ID")
            elif sid not in sutras:
                reporter.emit("ERROR", path, f"defined_by references absent sutra {sid}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only Panini registry validator")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="panini directory")
    args = parser.parse_args()
    root: Path = args.root
    reporter = Reporter()
    corpus = load(root / "registry" / "sutras" / "index.yaml", reporter)
    sutras = set((corpus or {}).get("sutras", {}))
    if not sutras:
        reporter.emit("ERROR", root / "registry/sutras/index.yaml", "missing sutras mapping")
    seen: dict[str, Path] = {}
    for kind in ("dhatu", "karaka", "samjna"):
        for path in sorted((root / "registry" / kind).glob("*.yaml")):
            data = load(path, reporter)
            if data is not None:
                validate_record(path, data, kind, sutras, seen, reporter)
    print(f"SUMMARY errors={reporter.errors} warnings={reporter.warnings} records={len(seen)} sutras={len(sutras)}")
    return 1 if reporter.errors else 0


if __name__ == "__main__":
    sys.exit(main())
