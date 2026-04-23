#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate draw.io XML structure.")
    parser.add_argument("path", help="Path to a .drawio file")
    return parser.parse_args()


def local_name(tag: str) -> str:
    if "}" in tag:
        return tag.rsplit("}", 1)[1]
    return tag


def main() -> int:
    args = parse_args()
    parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
    tree = ET.parse(args.path, parser=parser)
    root = tree.getroot()

    errors: list[str] = []
    warnings: list[str] = []

    if local_name(root.tag) != "mxfile":
        errors.append("root element must be <mxfile>")

    parent_map = {child: parent for parent in root.iter() for child in parent}

    comments = [elem for elem in root.iter() if elem.tag is ET.Comment]
    if comments:
        errors.append("XML comments are not allowed")

    diagrams = [elem for elem in root if local_name(elem.tag) == "diagram"]
    if not diagrams:
        errors.append("missing <diagram> child under <mxfile>")
    else:
        for diagram in diagrams:
            page_name = diagram.get("name") or diagram.get("id") or "unnamed"
            prefix = f"[{page_name}] "
            graph_model = next(
                (elem for elem in diagram if local_name(elem.tag) == "mxGraphModel"),
                None,
            )
            if graph_model is None:
                errors.append(prefix + "missing <mxGraphModel> child under <diagram>")
                continue
            if graph_model.get("adaptiveColors") != "auto":
                warnings.append(prefix + 'mxGraphModel should set adaptiveColors="auto"')
            root_elem = next(
                (elem for elem in graph_model if local_name(elem.tag) == "root"),
                None,
            )
            if root_elem is None:
                errors.append(prefix + "missing <root> under <mxGraphModel>")
                continue

            page_parent_map = {child: parent for parent in root_elem.iter() for child in parent}
            cells = [elem for elem in root_elem.iter() if local_name(elem.tag) == "mxCell"]
            ids: set[str] = set()
            for cell in cells:
                cell_id = cell.get("id")
                if not cell_id:
                    parent = page_parent_map.get(cell)
                    parent_tag = local_name(parent.tag) if parent is not None else ""
                    if parent_tag not in {"object", "UserObject"}:
                        errors.append(prefix + "mxCell missing id")
                    continue
                if cell_id in ids:
                    errors.append(prefix + f"duplicate mxCell id: {cell_id}")
                ids.add(cell_id)

                style = cell.get("style")
                if style:
                    if "html=1" not in style:
                        warnings.append(prefix + f"mxCell {cell_id} style should include html=1")
                    if not style.endswith(";"):
                        warnings.append(
                            prefix + f"mxCell {cell_id} style should end with a semicolon",
                        )

                if cell.get("edge") == "1":
                    geometry = next(
                        (child for child in cell if local_name(child.tag) == "mxGeometry"),
                        None,
                    )
                    if geometry is None:
                        errors.append(prefix + f"edge {cell_id} is missing child <mxGeometry>")
                    else:
                        if geometry.get("relative") != "1":
                            errors.append(
                                prefix + f'edge {cell_id} mxGeometry must set relative="1"',
                            )
                        if geometry.get("as") != "geometry":
                            errors.append(
                                prefix + f'edge {cell_id} mxGeometry must set as="geometry"',
                            )

            by_id = {cell.get("id"): cell for cell in cells if cell.get("id")}
            cell0 = by_id.get("0")
            cell1 = by_id.get("1")
            if cell0 is None:
                errors.append(prefix + 'missing structural root cell id="0"')
            elif cell0.get("parent") is not None:
                errors.append(prefix + 'structural root cell id="0" must not have a parent')
            if cell1 is None:
                errors.append(prefix + 'missing structural layer cell id="1"')
            elif cell1.get("parent") != "0":
                errors.append(prefix + 'structural layer cell id="1" must have parent="0"')

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
