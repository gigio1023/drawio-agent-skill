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

1. Form the reader brief in the content contract below. Reduce the source to
   one question and one answer before choosing nodes.
2. Derive the required nodes, edges, groups, and annotations from that brief.
   Source facts that do not support the answer stay outside the figure.
3. Read `references/editorial-principles.md` and
   `references/d2-authoring.md`.
4. Copy `assets/editorial-theme.d2` beside the new source and import it. Author
   only the semantic structure in the main `.d2` file.
5. Format the source with `d2 fmt <file>.d2`, then render it with:

   ```bash
   bash scripts/render_d2.sh <file>.d2 <file>.svg
   ```

6. Inspect the rendered SVG, using a temporary PNG proof when the available
   viewer cannot display SVG. Apply `references/review.md`, remove any
   unrequired content, and render again after each fix.

## Communication and content contract

Before authoring, form this small working brief:

```text
reader: <who must understand it>
question: <the one question this figure answers>
answer: <one sentence the reader should leave with>
surrounding_context: <what the document or conversation already explains>
```

If no audience is supplied, write for a technically literate reader who has no
private project context. Then derive the semantic inventory:

```text
required_nodes: [...]
required_edges: [...]
required_groups: [...]
required_annotations: [{text: ..., purpose: ...}]
deferred_to_prose: [...]
```

The brief and inventory need not become separate files. They are the comparison
set for the finished source. Raw source items are candidates, not requirements.
An annotation needs a named purpose: it was requested, or without it the reader
cannot recover the answer from the figure and its surrounding context. If
`required_annotations` is empty, add no title, subtitle, legend, caption,
callout, footer, badge, icon, or mini-diagram.

Use reader-facing roles instead of unexplained internal terms. If an exact name
matters, introduce it as `role (exact name)` rather than making the reader infer
the role. Show endpoints, field names, versions, and implementation steps only
when the question is specifically about them.

Represent real complexity when the request requires it. Minimality never
authorizes dropping a component or relationship needed for the answer. Remove
details that answer another question, combine repeated peers only when their
differences are irrelevant, and split by abstraction level when one page is too
dense. Shorten role-first labels and simplify grouping before enlarging the
canvas; never reduce type size to preserve an overfull composition.

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

Before finishing, confirm all four:

1. **Communication:** the intended reader can identify the subject and the
   one-sentence answer without private vocabulary or missing chat context.
2. **Meaning:** every required node, edge, direction, group, and annotation is
   present and no relationship was invented.
3. **Render:** at the intended delivery size, every label is readable, no edge
   crosses unrelated content, and the dominant reading path is obvious.
4. **Minimality:** every visible element changes the reader's understanding;
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
- Do not reproduce every term found in source material. A crowded but complete
  inventory is not a clear explanation.
