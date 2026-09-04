#!/usr/bin/env python3
"""Validate the structural basics of a generated SVG."""

from __future__ import annotations

import argparse
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def validate_svg(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        root = ET.parse(path).getroot()
    except (OSError, ET.ParseError) as exc:
        return [f"cannot parse SVG: {exc}"]

    if local_name(root.tag) != "svg":
        errors.append("root element is not <svg>")

    raw_view_box = root.get("viewBox")
    if not raw_view_box:
        errors.append("SVG has no viewBox")
    else:
        try:
            values = [float(value) for value in raw_view_box.replace(",", " ").split()]
        except ValueError:
            values = []
        if len(values) != 4 or values[2] <= 0 or values[3] <= 0:
            errors.append("viewBox must contain four numbers with positive width and height")

    seen: set[str] = set()
    duplicates: set[str] = set()
    for element in root.iter():
        element_id = element.get("id")
        if not element_id:
            continue
        if element_id in seen:
            duplicates.add(element_id)
        seen.add(element_id)
    if duplicates:
        errors.append(f"duplicate ids: {', '.join(sorted(duplicates))}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("svg", type=Path)
    args = parser.parse_args()
    errors = validate_svg(args.svg)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"OK: valid SVG structure ({args.svg})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
