#!/usr/bin/env python3
"""Report the project's English -> Ukrainian ASCII -> German document contract.

The Ukrainian section is the normative, full version. English and German are
parallel translations or summaries, but their *section order* is deliberately
English -> Ukrainian -> German. This tool inventories markers and their order;
it does not translate files, infer factual equivalence, or inspect vendored
material.
"""

from __future__ import annotations

import argparse
from pathlib import Path


LANGUAGE_MARKERS = {
    "English": ("## English", "## English summary"),
    "Ukrainian": ("## Ukrainian (ASCII)",),
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


def marker_positions(text: str) -> dict[str, int]:
    """Return the first position of every recognized language marker."""
    positions: dict[str, int] = {}
    for name, markers in LANGUAGE_MARKERS.items():
        found = [text.find(marker) for marker in markers if text.find(marker) >= 0]
        if found:
            positions[name] = min(found)
    return positions


def has_required_order(path: Path) -> bool:
    """Check section order without judging translation completeness or quality."""
    positions = marker_positions(path.read_text(encoding="utf-8"))
    expected = ("English", "Ukrainian", "German")
    return all(name in positions for name in expected) and [positions[name] for name in expected] == sorted(
        positions[name] for name in expected
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict",
        action="store_true",
        help=(
            "exit nonzero when a repository-owned Markdown file lacks a marker "
            "or violates English -> Ukrainian -> German section order"
        ),
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    incomplete: list[tuple[Path, list[str]]] = []
    out_of_order: list[Path] = []
    for path in project_markdown(root):
        missing = missing_markers(path)
        if missing:
            incomplete.append((path.relative_to(root), missing))
        elif not has_required_order(path):
            out_of_order.append(path.relative_to(root))

    for path, missing in incomplete:
        print(f"MISSING {','.join(missing)} {path.as_posix()}")
    for path in out_of_order:
        print(f"ORDER expected=English>Ukrainian>German {path.as_posix()}")
    print(
        "SUMMARY "
        f"markdown={len(project_markdown(root))} "
        f"complete={len(project_markdown(root)) - len(incomplete)} "
        f"incomplete={len(incomplete)} "
        f"out_of_order={len(out_of_order)}"
    )
    return 1 if args.strict and (incomplete or out_of_order) else 0


if __name__ == "__main__":
    raise SystemExit(main())
