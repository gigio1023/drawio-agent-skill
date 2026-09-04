---
name: drawio-diagram
description: >
  Use when the user explicitly wants a native .drawio artifact, asks to edit an
  existing draw.io file, needs draw.io metadata or pages, or requests draw.io
  export to SVG, PNG, or PDF. Produces editable mxGraph XML with automatic
  layout first, manual routing only when needed, and structural plus rendered
  quality checks. NOT for generic technical diagrams or measured data charts.
---

# Draw.io Diagram

Produce a valid, readable native `.drawio` file. Native XML is the source of
truth and remains beside any export. This skill exists for draw.io compatibility
and editability; a generic technical diagram belongs to `technical-diagram`.

## Quick path

1. Record the required nodes, edges, groups, and annotations. Read
   `references/local/editorial-principles.md` and
   `references/local/editorial-default-style.md` unless the user supplied a
   different style or an existing file already establishes one.
2. Read `references/local/upstream-drawio-rules.md`. Start with uncompressed
   bare `mxGraphModel` XML unless pages or file metadata require `<mxfile>`.
3. Read `references/local/auto-layout.md` and apply the simplest suitable
   automatic layout. Preserve explicit semantic grouping.
4. Run both validators from the skill root:

   ```bash
   python3 scripts/validate_drawio_xml.py <file>.drawio
   python3 scripts/validate_drawio_layout.py <file>.drawio
   ```

5. Export and inspect SVG or PNG when an export is requested or the layout is
   visually uncertain. If automatic layout leaves a collision or ambiguous
   route, read `references/local/edge-routing.md`, fix only those routes, and
   validate again.

## Content contract

Use the minimum semantic inventory:

```text
required_nodes: [...]
required_edges: [...]
required_groups: [...]
required_annotations: [...]
```

If `required_annotations` is empty, do not add a title, subtitle, legend,
caption, callout, footer, badge, icon, inset, or mini-diagram. Empty canvas is
acceptable. Complexity in the subject must be represented, but visual balance
never justifies invented content.

Only semantic nodes receive connectors. Supporting text and decorative
containers do not. Prefer direct labels and familiar shapes; a different shape
must encode a real distinction.

## Native XML baseline

- Include `mxGraphModel` root cells `0` and `1`; use `adaptiveColors="auto"`.
- Use uncompressed XML and stable unique IDs. Do not emit XML comments.
- Emit vertices before edges. Every edge has source and target IDs plus a child
  `<mxGeometry relative="1" as="geometry" />`.
- Use `html=1;` and XML-escape label HTML. A literal `\n` is not a line break;
  use `&lt;br&gt;` or `&#xa;`.
- Use `swimlane` or `container=1` only for real grouping. Use `<object>` or
  `UserObject` only when metadata improves editability.

Read `references/local/text-and-labels.md` only when labels need multiline HTML,
edge-label positioning, metadata, or another nontrivial treatment.

## Layout decision

Automatic layout is the default for new files:

- a linear process: `horizontalFlow` or `verticalFlow`;
- a hierarchy: `horizontalTree` or `verticalTree`;
- nested or routed architecture: explicit ELK JSON, optionally followed by
  `orthogonalEdge`.

Automatic layout is an explicit authoring step, not a viewer cleanup pass. The
saved file must already contain an acceptable layout. Use fixed ports and
waypoints only for remaining obstacles, parallel lanes, or return corridors.
Never add invisible spacer nodes or supporting bands to manipulate geometry.

## Verification

XML validation is blocking. Treat layout warnings as evidence to inspect and
fix; accept one only when the rendered source is still clear and the tradeoff is
reported. Validators do not detect every clipped label or visual collision.

Before finishing, confirm:

1. the required semantic inventory matches the diagram;
2. no component, label, or unrelated edge overlaps;
3. the dominant path and secondary paths are distinguishable;
4. every visible element earns its place; and
5. the export, when requested, was actually opened or rendered for inspection.

## Exports

Use an existing draw.io CLI; do not install one for a source-only request:

```bash
drawio -x -f svg -e -b 10 -o <name>.drawio.svg <name>.drawio
drawio -x -f png -e -b 10 --width 3840 -o <name>.drawio.png <name>.drawio
```

Prefer SVG for sharp text. If the exporter is unavailable, deliver the valid
`.drawio` source and report that export and visual inspection were unavailable.

## Output

Lead with the artifact created or changed. Report both validator results, the
layout route used, and the exact export inspected. Keep `<name>.drawio` beside
`<name>.drawio.svg`, `<name>.drawio.png`, or `<name>.drawio.pdf`. Name any
accepted warning or unverified rendering.

## Reference router

| Need | Read |
| --- | --- |
| Content and shared appearance invariants | `references/local/editorial-principles.md` |
| draw.io translation of the editorial tokens | `references/local/editorial-default-style.md` |
| Required XML structure and export rules | `references/local/upstream-drawio-rules.md` |
| Automatic layout and current CLI routes | `references/local/auto-layout.md` |
| Manual ports, waypoints, and crossings after auto-layout | `references/local/edge-routing.md` |
| Multiline, HTML, metadata, or edge labels | `references/local/text-and-labels.md` |
| Deep official syntax lookup | `references/local/upstream-docs-map.md` |

Read only the rows needed for the current artifact. Vendored files under
`references/fetched/` are factual lookup material, not workflow instructions.

## Gotchas

- Applying `--layout` is an explicit authoring step; reopening a saved file does
  not perform another obstacle-aware cleanup.
- Passing both validators does not prove the exported diagram is readable.
- A literal `\n` renders as two characters, not a line break.
- Edges between different containers normally belong to the root layer or they
  can clip inside one parent.
- Empty space does not need a title, legend, footer, rail, icon, or inset.
