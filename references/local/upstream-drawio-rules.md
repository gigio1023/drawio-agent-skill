# Upstream draw.io rules (local digest)

This file is a tight, opinionated digest of the rules this skill enforces. For the authoritative long-form references vendored directly from `jgraph/drawio-mcp` (Apache-2.0), read:

- [`../fetched/xml-reference.md`](../fetched/xml-reference.md) - complete XML rules: styles, edge routing, containers, layers, tags, metadata, placeholders, dark mode, well-formedness.
- [`../fetched/style-reference.md`](../fetched/style-reference.md) - comprehensive shape/style catalog.

When this digest and the vendored references disagree, the vendored references win - they're the upstream source of truth.

## Required XML structure

- Use native `.drawio` XML
- Include `mxfile > diagram > mxGraphModel`
- Include root cells:
  - `id="0"`
  - `id="1" parent="0"`
- Set `adaptiveColors="auto"` on `mxGraphModel`
- **NEVER emit XML comments (`<!-- -->`)** - strictly forbidden; they waste tokens and can cause parse errors
- Use the full `<mxfile>` form when file-level variables or human-editable metadata are useful

## Edge rules

- Every edge `mxCell` must contain `<mxGeometry relative="1" as="geometry" />` as a child element - never self-closing
- Use `edgeStyle=orthogonalEdgeStyle` for complex routing with 2+ bends
- Use `edgeStyle=elbowEdgeStyle;elbow=vertical;` for simple 0-1 bend connections
- Use one consistent edge style per diagram type (all orthogonal, all straight, all curved - never mixed)
- Add explicit waypoints when orthogonal routing would create overlap
- Each edge exits and enters as a >=20px straight perpendicular stub
- Bundle fan-out / fan-in edges into a shared trunk before branching

## Container rules

- `swimlane;startSize=30;` for titled panels
- `group;` for invisible grouping (includes `pointerEvents=0` so child connections aren't captured)
- `container=1;pointerEvents=0;` for decorative containers that shouldn't capture connections
- Child cells set `parent="containerId"` and use coordinates relative to the container
- Edges to children inside containers naturally cross the container boundary - this is correct; do not route around it

## Metadata and variables

- `<object>` / `<UserObject>` wrappers can store custom metadata on cells
- `placeholders="1"` on `<object>` enables `%name%` substitution in `label`
- `<mxfile vars='{"project":"Atlas"}'>` can hold file-level variables for reusable templates
- Tags require the `<object>` wrapper; plain `mxCell` cannot have tags

## Export rules

- Keep `.drawio` as the source of truth - **do NOT** delete the source after export (diverges from upstream skill-cli)
- Export only when the draw.io desktop CLI is available
- If export is unavailable, do not fake success; leave the `.drawio` file
- `.drawio.png`, `.drawio.svg`, and `.drawio.pdf` (with `--embed-diagram` / `-e`) carry the diagram XML embedded in the exported file - any of them can be reopened in draw.io to continue editing

## Validation rules

- Run `python scripts/validate_drawio_xml.py <file.drawio>` before claiming the XML is valid
- Run `python scripts/validate_drawio_layout.py <file.drawio>` before claiming the layout is clean
- When the validators and the eye test disagree, trust the failure mode and fix it instead of arguing with it
