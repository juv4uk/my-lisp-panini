#!/usr/bin/env python3
"""Read-only structural validator for Derivation IR trace fixtures."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml


PANINI = Path(__file__).resolve().parents[1]
DEFAULT_FIXTURES = PANINI / "tests" / "trace-fixtures"
SUTRA_ID = re.compile(r"^\d+\.\d+\.\d+$")
MACHINE_ID = re.compile(r"^machine:[A-Za-z0-9_.:-]+$")
STATUSES = {"success", "partial", "blocked", "invalid"}


class Reporter:
    def __init__(self) -> None:
        self.errors = 0

    def error(self, path: Path, message: str) -> None:
        self.errors += 1
        print(f"ERROR {path}: {message}")


def mapping(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def nonempty_list(value: Any) -> bool:
    return isinstance(value, list) and bool(value)


def canonical_rule_id(value: Any) -> bool:
    return isinstance(value, str) and bool(SUTRA_ID.fullmatch(value) or MACHINE_ID.fullmatch(value))


def validate_dependencies(path: Path, events: list[dict[str, Any]], reporter: Reporter) -> None:
    ids = [event.get("event_id") for event in events]
    if any(not isinstance(event_id, str) or not event_id for event_id in ids):
        reporter.error(path, "every event requires a non-empty event_id")
        return
    if len(ids) != len(set(ids)):
        reporter.error(path, "event_id values must be unique")
    known = set(ids)
    graph: dict[str, list[str]] = {}
    for event in events:
        event_id = event["event_id"]
        depends_on = event.get("depends_on")
        if not isinstance(depends_on, list):
            reporter.error(path, f"{event_id}: depends_on must be a list")
            continue
        missing = [dependency for dependency in depends_on if dependency not in known]
        if missing:
            reporter.error(path, f"{event_id}: unknown dependencies {missing}")
        graph[event_id] = [dependency for dependency in depends_on if dependency in known]

    active: set[str] = set()
    visited: set[str] = set()

    def visit(event_id: str) -> None:
        if event_id in active:
            reporter.error(path, f"dependency cycle includes {event_id}")
            return
        if event_id in visited:
            return
        active.add(event_id)
        for dependency in graph.get(event_id, []):
            visit(dependency)
        active.remove(event_id)
        visited.add(event_id)

    for event_id in graph:
        visit(event_id)


def validate_trace(path: Path, document: dict[str, Any], reporter: Reporter) -> None:
    events_raw = document.get("events")
    if not isinstance(events_raw, list) or not events_raw:
        return
    events = [mapping(event) for event in events_raw]
    if any(not event for event in events):
        reporter.error(path, "every event must be a mapping")
        return

    validate_dependencies(path, events, reporter)
    state_ids = {state.get("id") for state in document.get("states", []) if isinstance(state, dict)}
    selected_by_event: dict[str, str] = {}
    terminated: list[dict[str, Any]] = []

    for event in events:
        event_id = event.get("event_id", "<missing>")
        if not nonempty_list(event.get("provenance")):
            reporter.error(path, f"{event_id}: provenance must be a non-empty list")
        payload = mapping(event.get("payload"))
        kind = event.get("kind")

        if kind in {"applicability-check", "rule-decision", "state-transition"}:
            if not canonical_rule_id(payload.get("rule")):
                reporter.error(path, f"{event_id}: rule must be a canonical sūtra ID or namespaced machine ID")

        if kind == "state-observed":
            state = payload.get("state")
            if state not in state_ids:
                reporter.error(path, f"{event_id}: observed state {state!r} is not declared")
            if not isinstance(payload.get("serialization"), str):
                reporter.error(path, f"{event_id}: state-observed requires serialization")

        if kind == "rule-decision" and payload.get("decision") == "selected":
            selected_by_event[event_id] = str(payload.get("rule"))

        if kind == "state-transition":
            before, after = payload.get("before"), payload.get("after")
            if before not in state_ids or after not in state_ids:
                reporter.error(path, f"{event_id}: transition states must be declared")
            if before == after:
                reporter.error(path, f"{event_id}: transition before and after must differ")
            if not isinstance(payload.get("operation"), str) or not payload["operation"]:
                reporter.error(path, f"{event_id}: transition requires an explicit operation")
            dependencies = event.get("depends_on", [])
            rule = payload.get("rule")
            if not any(selected_by_event.get(dependency) == rule for dependency in dependencies):
                reporter.error(path, f"{event_id}: transition must directly depend on a selected decision for its rule")

        if kind == "trace-terminated":
            terminated.append(event)
            outcome = payload.get("outcome")
            if outcome not in STATUSES:
                reporter.error(path, f"{event_id}: termination outcome must be one of {sorted(STATUSES)}")

    result = mapping(document.get("result"))
    status = result.get("status")
    if status not in STATUSES:
        reporter.error(path, "result.status must be success, partial, blocked, or invalid")
    if not terminated:
        reporter.error(path, "trace fixtures require a trace-terminated event")
    elif not any(mapping(event.get("payload")).get("outcome") == status for event in terminated):
        reporter.error(path, "at least one trace-terminated outcome must match result.status")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_FIXTURES, help="trace-fixture directory")
    args = parser.parse_args()
    reporter = Reporter()
    paths = sorted(args.root.glob("*.yaml"))
    if not paths:
        print(f"ERROR {args.root}: no YAML fixtures found")
        return 2
    for path in paths:
        try:
            document = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as error:
            reporter.error(path, f"invalid YAML: {error}")
            continue
        if isinstance(document, dict) and "events" in document:
            validate_trace(path, document, reporter)
    if reporter.errors:
        print(f"trace fixture validation: FAIL ({reporter.errors} errors)")
        return 1
    print(f"trace fixture validation: PASS ({len(paths)} YAML files scanned)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
