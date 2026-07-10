---
name: drawio-diagram
description: >
  Use when the user asks for a native draw.io or .drawio artifact, an editable
  architecture diagram or flowchart, component-to-component arrow routing, an
  editorial figure in draw.io, or export from .drawio to PNG/SVG/PDF. Produces
  editable mxGraph XML with structural, layout, and rendered quality checks.
  NOT for Mermaid-only output or generic image generation.
---

# Draw.io Diagram

Native `.drawio` XML is the source of truth. Keep it after every export so the
artifact stays editable. Export is optional and should happen only when requested.

## Quick Start

1. Confirm the message, components/arrows, page constraint, and artifacts. Only
   semantic nodes may receive connectors; supporting text may not.
2. Read `references/local/upstream-drawio-rules.md` and
   `references/local/edge-routing.md`. Read
   `references/local/figure-grammars.md` when choosing or changing composition.
3. Generate native `.drawio` XML using the repo's established structure.
4. Read `references/local/layout-safety.md`, then run:
   - `python3 scripts/validate_drawio_xml.py <file>.drawio`
   - `python3 scripts/validate_drawio_layout.py <file>.drawio`
5. If export was requested, use an existing draw.io CLI, inspect the SVG or PNG,
   and revise the `.drawio` source until the rendered artifact is clear.

## Reference Router

| Need | Read |
|---|---|
| XML structure and validation baseline | `references/local/upstream-drawio-rules.md` |
| Edge connections, ports, waypoints, crossings | `references/local/edge-routing.md` |
| Labels, line breaks, escaping, detail-vs-compact | `references/local/text-and-labels.md` |
| Color scheme selection and dark mode | `references/local/color-palettes.md` |
| Page composition and starting budgets | `references/local/figure-grammars.md` |
| Overlap, padding, routing, and preflight | `references/local/layout-safety.md` |
| Publication or review-quality finishing | `references/local/quality-gates.md` |
| A validator/reviewer exposes a repeated failure | `references/local/real-world-gotchas.md` |
| Export or visual-review iteration | `references/local/review-loop.md` |
| Compact editorial styling | `references/local/visual-patterns.md` |
| Official docs/examples for deep lookup | `references/local/upstream-docs-map.md` |
| Provenance or skill maintenance | `references/local/reference-set.md`, `references/local/community-lessons.md` |
| XML/style detail beyond the local digest | Search factual definitions under `references/fetched/`; do not adopt its legacy agent workflow wholesale |

Read only the rows needed for the task. Files under `references/fetched/` are
vendored verbatim for provenance and technical lookup; some contain older model
scaffolding. Use them for exact XML/style facts, while this SKILL and the local
overlay control workflow, layout judgment, and verification. In particular,
ignore the vendored claim that a viewer ELK pass will clean up edge routing -
it does not apply to files this skill writes.

## Workflow

### 1. Define the page

Capture the single message, target reader, required boxes, required relationships,
and whether multiple pages are allowed. Keep different semantic levels distinct:
external callers, main container, internal sections, implementation choices, and
external dependencies should not become one ambiguous box.

### 2. Choose a grammar and budget

Choose one grammar from `references/local/figure-grammars.md` for the first pass;
`flow-canvas` is the safe default for component-to-component flow.

Use this as a starting heuristic, not a content limit:

- 3-5 primary framed components
- 1 dominant path and 0-2 secondary paths
- at most one side rail and one compact bottom strip

Do not omit required content to satisfy the heuristic. If one page cannot remain
readable, split it when allowed. Otherwise shorten labels and simplify hierarchy,
then report any remaining density risk.

### 3. Author native XML

Required baseline:

- `mxfile > diagram > mxGraphModel` with root cells `0` and `1`
- `adaptiveColors="auto"`
- child `<mxGeometry relative="1" as="geometry" />` on every edge
- `html=1;` in cell styles and no XML comments

Use draw.io primitives directly: `swimlane` for titled panels, `group;` for
invisible grouping, `container=1;pointerEvents=0;` for decorative containers, and
`object` / `UserObject` only when metadata or placeholders improve editability.

### 4. Make meaning and routes explicit

- Prefer one or two lines per component and no paragraphs or vertical main labels.
  Line breaks are `&lt;br&gt;` or `&#xa;` in the value attribute - a literal
  `\n` renders as visible backslash-n text.
- Use precise ownership/protocol labels; rename ambiguity instead of decorating it.
- Make one path visually dominant and keep secondary paths quieter. Assign
  colors by semantic role from one palette (`references/local/color-palettes.md`).
- Own every route: draw.io does not route around other shapes. Align connected
  boxes so main edges run straight. Add waypoints only for an obstacle, a
  separate edge lane, or an outer corridor; never dogleg aligned terminals.
  For 2+ edges or an occupied corridor, pin sides and add waypoints
  (`references/local/edge-routing.md` has the recipes).
- Put edge labels on straight segments, give each an opaque
  `labelBackgroundColor` matching its canvas or panel, and keep arrows out of
  text/title regions.
- Include every requested component even if a human may later fine-tune placement.

### 5. Validate and inspect

Run both bundled validators from the skill root:

```bash
python3 scripts/validate_drawio_xml.py <path>.drawio
python3 scripts/validate_drawio_layout.py <path>.drawio
```

XML failure is blocking. The layout validator also audits edges: dangling
terminals fail; probable component crossings, ports facing away from their
target, overlapping floating edge pairs, uncovered edge labels, and unnecessary
aligned-terminal doglegs warn. Treat layout warnings as
evidence to inspect and fix; accept one only when the source remains readable
and the tradeoff is explicit. Validators do not catch every visual collision.
When an export is part of the deliverable, inspect the actual artifact for
clipped text, fuzzy type, route collisions, framing, and arrowheads on bends
or borders.

## Exports

Use a draw.io CLI already present on `PATH` or in the environment's known desktop
app location. Do not install an exporter or run an unrelated postprocessor for a
source-only request. If no exporter is available, deliver the valid `.drawio`
source and report that export was not verified.

```bash
drawio -x -f <format> -e -b 10 -o <output> <input.drawio>
drawio -x -f png -e -b 10 --width 3840 -o <output>.drawio.png <input.drawio>
```

Prefer SVG when text sharpness matters. Use normalized high-resolution PNG when
SVG is impractical, and inspect whichever format you deliver.

## Output Contract

Lead with the artifact created or changed. Report both validator results and,
when exported, the format actually inspected. Name any unverified export or
accepted layout warning. Keep `.drawio` beside exports.

Naming: source `<name>.drawio`; exports `<name>.drawio.png`,
`<name>.drawio.svg`, or `<name>.drawio.pdf`. Use lowercase descriptive names.

## Gotchas

- Passing validators does not prove the exported diagram is readable.
- No routing pass will fix edges later: the built-in router ignores every shape
  except the two terminals, and the vendored "ELK cleanup" note applies only to
  the drawio-mcp viewer, not to files opened in draw.io.
- `\n` in a value attribute renders as literal text; use `&lt;br&gt;` or `&#xa;`.
- Page budgets guide composition but never authorize dropping required content.
- Keep implementation choices and external dependencies semantically separate.
- Do not add tools, formats, pages, or a diagram-wide restyle outside the request.
- This skill intentionally keeps `.drawio` after export even if an upstream CLI
  workflow treats it as intermediate output.
