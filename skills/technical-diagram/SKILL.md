---
name: technical-diagram
description: >
  Use when the user wants a technical diagram, architecture figure, system map,
  process flow, or box-and-arrow schematic without requiring a native editor
  format. Produces a compact D2 source with ELK layout and SVG output, using a
  restrained editorial style and rendered quality checks. NOT for native
  .drawio files, Mermaid-only output, measured data charts, or image generation.
---

# Technical Diagram

Produce the smallest accurate technical figure. D2 is the default authoring
language, ELK owns layout, and SVG is the primary deliverable. Keep the source
beside the render so the diagram remains reproducible without a GUI.

## Quick path

1. Record the required nodes, edges, groups, and annotations from the request.
   Do not turn optional context into visible content.
2. Read `references/editorial-principles.md` and
   `references/d2-authoring.md`.
3. Copy `assets/editorial-theme.d2` beside the new source and import it. Author
   only the semantic structure in the main `.d2` file.
4. Format the source with `d2 fmt <file>.d2`, then render it with:

   ```bash
   bash scripts/render_d2.sh <file>.d2 <file>.svg
   ```

5. Inspect the rendered SVG, using a temporary PNG proof when the available
   viewer cannot display SVG. Apply `references/review.md`, remove any
   unrequired content, and render again after each fix.

## Content contract

Before authoring, use this inventory:

```text
required_nodes: [...]
required_edges: [...]
required_groups: [...]
required_annotations: [...]
```

The inventory need not become a separate file. It is the comparison set for the
finished source. If `required_annotations` is empty, do not add a title,
subtitle, legend, caption, callout, footer, badge, icon, or mini-diagram.

Represent real complexity when the request requires it. Minimality never
authorizes dropping a component or relationship. When one page is too dense,
split by abstraction level if the requested artifact allows multiple figures;
otherwise shorten labels and simplify grouping before enlarging the canvas.

## Backend decision

Use D2 for ordinary topology: flows, trees, service maps, nested containers,
dependencies, and small sequence-like interactions.

Read `references/svg-fallback.md` and author SVG directly only when one of these
holds:

- the user explicitly requires SVG source or asks to edit an existing SVG;
- the composition depends on irregular geometry that D2 cannot express; or
- D2 is unavailable and the user needs an SVG rather than a `.d2` artifact.

Do not silently install D2. If the user explicitly requested D2 and no renderer
is available, leave the valid source and report that the render is unverified.

## Style boundary

The editorial theme preserves the visual language established by this package,
but semantic clarity wins over exact imitation. D2 approximates a 1.2px stroke
with an integer width and uses an unfilled triangle rather than the exact small
V-shaped arrowhead. Do not compensate with SVG decoration or a second visual
system. Use the SVG fallback only when exact geometry is part of the request.

## Verification

The bundled render script checks D2 formatting, validates D2 syntax, renders
with ELK and 16px outer padding, and validates the SVG root, viewBox, and IDs.
It does not prove that the figure is readable.

Before finishing, confirm all three:

1. **Meaning:** every required node, edge, direction, group, and annotation is
   present and no relationship was invented.
2. **Render:** no label is clipped, no edge crosses unrelated content, and the
   dominant reading path is obvious.
3. **Minimality:** every visible element changes the reader's understanding;
   empty top, bottom, or side space remains empty.

## Output

Lead with the artifacts created. Report the D2 validation and SVG validation
results, the layout engine, and whether the render was visually inspected. Keep
`<name>.d2`, `editorial-theme.d2`, and `<name>.svg` together. Name any missing
renderer, unverified visual result, or accepted layout defect.

## Reference router

| Need | Read or run |
| --- | --- |
| Default content and appearance rules | `references/editorial-principles.md` |
| D2 syntax, classes, layout, and known limits | `references/d2-authoring.md` |
| Direct SVG exception path | `references/svg-fallback.md` |
| Semantic, visual, and negative-space audit | `references/review.md` |
| Deterministic D2-to-SVG render | execute `scripts/render_d2.sh` |
| Standalone SVG structure check | execute `scripts/validate_svg.py` |

Read only the route needed for the current artifact.

## Gotchas

- A successful D2 render does not prove that labels, crossings, or semantic
  grouping are readable; inspect the SVG.
- The main source must keep `editorial-theme.d2` beside it. A missing relative
  import loses both portability and the shared style.
- Apply `entity` to technical nodes and `flow` to ordinary connections; the
  default D2 theme is intentionally not the style contract.
- Do not turn an awkward automatic layout into an excuse for a title, legend,
  spacer node, or decorative container. Fix the existing geometry or use the
  narrow SVG fallback.
