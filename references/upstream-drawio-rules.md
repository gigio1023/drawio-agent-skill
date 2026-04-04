# Upstream draw.io rules

This skill incorporates the practical parts of `jgraph/drawio-mcp` skill-cli and the official draw.io AI FAQ.

## Required XML structure

- Use native `.drawio` XML
- Include `mxfile > diagram > mxGraphModel`
- Include root cells:
  - `id="0"`
  - `id="1" parent="0"`
- Set `adaptiveColors="auto"` on `mxGraphModel`
- Never emit XML comments
- Use the full `<mxfile>` form when file-level variables or human-editable metadata are useful

## Edge rules

- Every edge must contain `<mxGeometry relative="1" as="geometry" />`
- Use `edgeStyle=orthogonalEdgeStyle` for most readable flows
- Add explicit waypoints when orthogonal routing would create overlap
- Leave enough straight segment for arrowheads near source and target
- If arrows connect to text labels instead of boxes, use explicit points or convert the label into a real component box

## Container rules

- `swimlane` for titled panels
- `group;` for invisible grouping
- `container=1;pointerEvents=0;` for decorative containers
- Child coordinates are relative to the parent container

## Metadata and variables

- `object` / `UserObject` wrappers can store custom metadata on cells
- `placeholders="1"` enables `%name%` substitution
- `<mxfile vars='{\"project\":\"Atlas\"}'>` can hold file-level variables for reusable templates

## Export rules

- Keep `.drawio` as the source of truth
- Export only when the draw.io desktop CLI is available
- If export is unavailable, do not fake success; leave the `.drawio` file
- `.drawio.png` and `.drawio.svg` can embed XML and remain editable in draw.io
