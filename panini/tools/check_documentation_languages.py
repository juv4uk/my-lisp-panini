#!/usr/bin/env python3
"""Report English, Ukrainian, and German section markers in project Markdown.

This is an inventory aid for the documentation migration. It deliberately does
not translate files, infer factual equivalence, or inspect vendored material.
"""

from __future__ import annotations

import argparse
from pathlib import Path


LANGUAGE_MARKERS = {
    "English": ("## English", "## English summary"),
    "Ukrainian": ("## Українська", "## Український повний текст"),
    "German": ("## Deutsch", "## German summary"),
}

EXCLUDED_PARTS = {".git", ".swarm-node", "scratch", "reference-from-engineer-1"}


def project_markdown(root: Path) -> list[Path]:
    """Return repository-owned Markdown files, excluding external material."""
    files = []
    for path in root.rglob("*.md"):
        relative = path.relative_to(root)
        if any(part in EXCLUDED_PARTS for part in relative.parts):
            continue
        files.append(path)
    return sorted(files)


def missing_markers(path: Path) -> list[str]:
    """Return language names whose standard section marker is absent."""
    text = path.read_text(encoding="utf-8")
    return [
        name
        for name, markers in LANGUAGE_MARKERS.items()
        if not any(marker in text for marker in markers)
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="exit nonzero when a repository-owned Markdown file lacks a marker",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    incomplete: list[tuple[Path, list[str]]] = []
    for path in project_markdown(root):
        missing = missing_markers(path)
        if missing:
            incomplete.append((path.relative_to(root), missing))

    for path, missing in incomplete:
        print(f"MISSING {','.join(missing)} {path.as_posix()}")
    print(
        "SUMMARY "
        f"markdown={len(project_markdown(root))} "
        f"complete={len(project_markdown(root)) - len(incomplete)} "
        f"incomplete={len(incomplete)}"
    )
    return 1 if args.strict and incomplete else 0


if __name__ == "__main__":
    raise SystemExit(main())
