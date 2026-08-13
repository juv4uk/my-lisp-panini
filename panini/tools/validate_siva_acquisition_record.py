#!/usr/bin/env python3
"""Offline validator for Śiva-sūtra source-acquisition records.

The tool validates project metadata only. It never fetches URLs, reads the
acquired artifact, or upgrades a record into machine input.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml


SHA256 = re.compile(r"^[0-9a-f]{64}$")
ACQUISITION_ID = re.compile(r"^acquisition:siva-sutras:[^:]+:\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
CONVERSION_ID = re.compile(r"^conversion:siva-sutras:[^:]+$")
UTC_TIMESTAMP = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
REUSE = {"permitted", "restricted", "unresolved"}
STATUS = {"acquired", "verified", "rejected", "superseded"}
ROW_CHECK = {"pending", "pass", "fail"}
MEDIA_TYPES = {"text/html", "application/pdf", "text/plain"}
FETCH_METHODS = {"manual-browser-download", "reviewed-command"}


def error(message: str) -> None:
    print(f"ERROR: {message}")


def mapping(value: Any, name: str, errors: list[str]) -> dict[str, Any]:
    if isinstance(value, dict):
        return value
    errors.append(f"{name} must be a mapping")
    return {}


def nonempty(value: Any, name: str, errors: list[str]) -> str:
    if isinstance(value, str) and value.strip():
        return value
    errors.append(f"{name} must be a non-empty string")
    return ""


def url(value: Any, name: str, errors: list[str]) -> str:
    text = nonempty(value, name, errors)
    if text and not text.startswith("https://"):
        errors.append(f"{name} must use https")
    return text


def timestamp(value: Any, name: str, errors: list[str]) -> None:
    text = nonempty(value, name, errors)
    if not text:
        return
    if not UTC_TIMESTAMP.fullmatch(text):
        errors.append(f"{name} must be UTC YYYY-MM-DDTHH:MM:SSZ")
        return
    try:
        datetime.strptime(text, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        errors.append(f"{name} is not a real UTC timestamp")


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        document = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        return [f"cannot parse {path}: {exc}"]
    record = mapping(document, "record", errors)

    identifier = nonempty(record.get("id"), "id", errors)
    if identifier and not ACQUISITION_ID.fullmatch(identifier):
        errors.append("id must be acquisition:siva-sutras:<source-key>:<UTC-timestamp>")
    if record.get("subject") != "siva-sutras-phoneme-ordering":
        errors.append("subject must be siva-sutras-phoneme-ordering")

    source = mapping(record.get("source"), "source", errors)
    nonempty(source.get("title"), "source.title", errors)
    url(source.get("canonical_url"), "source.canonical_url", errors)
    timestamp(source.get("retrieved_at"), "source.retrieved_at", errors)
    nonempty(source.get("publisher_revision"), "source.publisher_revision", errors)

    rights = mapping(record.get("rights"), "rights", errors)
    nonempty(rights.get("license"), "rights.license", errors)
    url(rights.get("license_url"), "rights.license_url", errors)
    nonempty(rights.get("attribution"), "rights.attribution", errors)
    if rights.get("reuse_status") not in REUSE:
        errors.append("rights.reuse_status must be permitted, restricted, or unresolved")

    artifact = mapping(record.get("artifact"), "artifact", errors)
    local_path = nonempty(artifact.get("local_path"), "artifact.local_path", errors)
    if local_path and (Path(local_path).is_absolute() or not local_path.startswith("sources/siva-sutras/")):
        errors.append("artifact.local_path must be a relative sources/siva-sutras/ path")
    digest = nonempty(artifact.get("sha256"), "artifact.sha256", errors)
    if digest and not SHA256.fullmatch(digest):
        errors.append("artifact.sha256 must be 64 lowercase hexadecimal characters")
    if artifact.get("media_type") not in MEDIA_TYPES:
        errors.append("artifact.media_type is not permitted by v0.1")
    if not isinstance(artifact.get("byte_count"), int) or artifact.get("byte_count", 0) <= 0:
        errors.append("artifact.byte_count must be a positive integer")
    if artifact.get("fetch_method") not in FETCH_METHODS:
        errors.append("artifact.fetch_method is not permitted by v0.1")

    conversion = mapping(record.get("conversion"), "conversion", errors)
    if conversion.get("input_representation") not in {"devanagari", "IAST", "other"}:
        errors.append("conversion.input_representation must be devanagari, IAST, or other")
    if conversion.get("output_representation") != "SLP1":
        errors.append("conversion.output_representation must be SLP1")
    nonempty(conversion.get("converter"), "conversion.converter", errors)
    conversion_id = nonempty(conversion.get("conversion_record"), "conversion.conversion_record", errors)
    if conversion_id and not CONVERSION_ID.fullmatch(conversion_id):
        errors.append("conversion.conversion_record has invalid identifier")

    verification = mapping(record.get("verification"), "verification", errors)
    if verification.get("row_check") not in ROW_CHECK:
        errors.append("verification.row_check must be pending, pass, or fail")
    compared = verification.get("compared_to")
    if not isinstance(compared, list) or len(compared) < 2:
        errors.append("verification.compared_to must name both local comparison artifacts")
    nonempty(verification.get("reviewer"), "verification.reviewer", errors)
    if record.get("status") not in STATUS:
        errors.append("status must be acquired, verified, rejected, or superseded")
    if record.get("status") == "verified" and verification.get("row_check") != "pass":
        errors.append("verified status requires verification.row_check: pass")
    if rights.get("reuse_status") != "permitted" and record.get("status") == "verified":
        errors.append("verified status requires permitted reuse")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate one Śiva-sūtra acquisition record offline")
    parser.add_argument("record", type=Path, help="YAML acquisition record to validate")
    args = parser.parse_args()
    errors = validate(args.record)
    for item in errors:
        error(item)
    if errors:
        return 1
    print(f"PASS: {args.record.as_posix()} is a valid acquisition record")
    return 0


if __name__ == "__main__":
    sys.exit(main())
