#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Box:
    cell_id: str
    parent_id: str | None
    x: float
    y: float
    width: float
    height: float
    style: dict[str, str]
    raw_style: str
    value: str
    is_text: bool
    is_framed: bool
    is_overlap_candidate: bool


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate draw.io layout heuristics.",
    )
    parser.add_argument("path", help="Path to a .drawio file")
    parser.add_argument(
        "--min-padding",
        type=float,
        default=16.0,
        help="Minimum padding from a parent border to child boxes",
    )
    return parser.parse_args()


def local_name(tag: str) -> str:
    if "}" in tag:
        return tag.rsplit("}", 1)[1]
    return tag


def parse_style(style: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for token in style.split(";"):
        token = token.strip()
        if not token:
            continue
        if "=" in token:
            key, value = token.split("=", 1)
            result[key] = value
        else:
            result[token] = "1"
    return result


def parse_boxes(root: ET.Element) -> dict[str, Box]:
    boxes: dict[str, Box] = {}
    for cell in root.iter():
        if local_name(cell.tag) != "mxCell":
            continue
        if cell.get("vertex") != "1":
            continue
        geometry = next(
            (child for child in cell if local_name(child.tag) == "mxGeometry"),
            None,
        )
        if geometry is None:
            continue
        x = float(geometry.get("x", "0"))
        y = float(geometry.get("y", "0"))
        width = float(geometry.get("width", "0"))
        height = float(geometry.get("height", "0"))
        style_text = cell.get("style", "")
        style = parse_style(style_text)
        value = cell.get("value", "")
        cell_id = cell.get("id")
        if not cell_id:
            continue
        is_text = "text" in style or style.get("shape") == "text"
        is_group = "group" in style
        is_background_container = (
            style.get("container") == "1" and style.get("pointerEvents") == "0"
        )
        is_framed = not is_text and not is_group and width > 0 and height > 0
        is_overlap_candidate = is_framed and not is_background_container
        boxes[cell_id] = Box(
            cell_id=cell_id,
            parent_id=cell.get("parent"),
            x=x,
            y=y,
            width=width,
            height=height,
            style=style,
            raw_style=style_text,
            value=value,
            is_text=is_text,
            is_framed=is_framed,
            is_overlap_candidate=is_overlap_candidate,
        )
    return boxes


def absolute_box(box: Box, boxes: dict[str, Box]) -> tuple[float, float, float, float]:
    if not box.parent_id or box.parent_id not in boxes:
        return (box.x, box.y, box.width, box.height)
    parent = boxes[box.parent_id]
    parent_x, parent_y, _, _ = absolute_box(parent, boxes)
    return (parent_x + box.x, parent_y + box.y, box.width, box.height)


def strip_label(value: str) -> str:
    text = html.unescape(value or "")
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def overlap(a: tuple[float, float, float, float], b: tuple[float, float, float, float]) -> bool:
    ax1, ay1, aw, ah = a
    bx1, by1, bw, bh = b
    ax2 = ax1 + aw
    ay2 = ay1 + ah
    bx2 = bx1 + bw
    by2 = by1 + bh
    return ax1 < bx2 and ax2 > bx1 and ay1 < by2 and ay2 > by1


def corner_signature(box: Box) -> str | None:
    if not box.is_framed:
        return None
    if box.style.get("rounded") != "1":
        return "square"
    if any(
        token in box.style
        for token in ("ellipse", "rhombus", "hexagon", "cylinder", "cloud")
    ):
        return None
    shape = box.style.get("shape", "")
    if shape and shape not in {"label", "rectangle", ""}:
        return None
    if box.style.get("absoluteArcSize") == "1":
        return f'rounded:absolute:{box.style.get("arcSize", "default")}'
    return f'rounded:default:{box.style.get("arcSize", "default")}'


def main() -> int:
    args = parse_args()
    tree = ET.parse(args.path)
    errors: list[str] = []
    warnings: list[str] = []
    root = tree.getroot()
    diagrams = [elem for elem in root if local_name(elem.tag) == "diagram"]

    for diagram in diagrams:
        page_name = diagram.get("name") or diagram.get("id") or "unnamed"
        prefix = f"[{page_name}] "
        graph_model = next(
            (elem for elem in diagram if local_name(elem.tag) == "mxGraphModel"),
            None,
        )
        if graph_model is None:
            errors.append(prefix + "missing mxGraphModel")
            continue
        page_root = next(
            (elem for elem in graph_model if local_name(elem.tag) == "root"),
            None,
        )
        if page_root is None:
            errors.append(prefix + "missing root")
            continue

        boxes = parse_boxes(page_root)
        siblings: dict[str | None, list[Box]] = {}
        for box in boxes.values():
            siblings.setdefault(box.parent_id, []).append(box)

        for parent_id, child_boxes in siblings.items():
            framed = [box for box in child_boxes if box.is_framed]
            overlap_candidates = [box for box in child_boxes if box.is_overlap_candidate]
            for index, left in enumerate(overlap_candidates):
                left_abs = absolute_box(left, boxes)
                for right in overlap_candidates[index + 1 :]:
                    right_abs = absolute_box(right, boxes)
                    if overlap(left_abs, right_abs):
                        errors.append(
                            prefix + f"framed components overlap: {left.cell_id} vs {right.cell_id}",
                        )

            if parent_id in boxes:
                parent = boxes[parent_id]
                if parent.is_framed:
                    header_size = float(parent.style.get("startSize", "0") or "0")
                    for child in framed + [box for box in child_boxes if box.is_text]:
                        max_x = parent.width - args.min_padding
                        max_y = parent.height - args.min_padding
                        min_x = args.min_padding
                        min_y = args.min_padding + header_size
                        if child.x < min_x:
                            errors.append(
                                prefix
                                + f"{child.cell_id} is too close to parent {parent_id} left border",
                            )
                        if child.y < min_y:
                            errors.append(
                                prefix
                                + f"{child.cell_id} is too close to parent {parent_id} top border",
                            )
                        if child.x + child.width > max_x:
                            errors.append(
                                prefix
                                + f"{child.cell_id} exceeds parent {parent_id} right border",
                            )
                        if child.y + child.height > max_y:
                            errors.append(
                                prefix
                                + f"{child.cell_id} exceeds parent {parent_id} bottom border",
                            )

        signatures = sorted(
            {
                signature
                for signature in (corner_signature(box) for box in boxes.values())
                if signature
            },
        )
        if len(signatures) > 1:
            warnings.append(
                prefix
                + "inconsistent rounded-rectangle corner settings: "
                + ", ".join(signatures),
            )

        for box in boxes.values():
            label = strip_label(box.value)
            if not label:
                continue
            if box.is_framed:
                spacing_values = [
                    float(box.style.get("spacingLeft", box.style.get("spacing", "0")) or "0"),
                    float(box.style.get("spacingRight", box.style.get("spacing", "0")) or "0"),
                    float(box.style.get("spacingTop", box.style.get("spacing", "0")) or "0"),
                    float(box.style.get("spacingBottom", box.style.get("spacing", "0")) or "0"),
                ]
                if any(value < 8 for value in spacing_values) and len(label) >= 16:
                    warnings.append(
                        prefix
                        + f"{box.cell_id} label may hug its border; increase spacing or shorten text",
                    )
            if len(label) > 48 and box.width < 260:
                warnings.append(
                    prefix
                    + f"{box.cell_id} label is long for its width; shorten text before widening the box",
                )
            if "rotation=90" in box.raw_style:
                warnings.append(prefix + f"{box.cell_id} uses vertical text rotation")

    for message in warnings:
        print(f"WARNING: {message}", file=sys.stderr)
    for message in errors:
        print(f"ERROR: {message}", file=sys.stderr)

    if errors:
        return 1

    print(f"OK: {Path(args.path).name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
