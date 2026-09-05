# D2 authoring

## Contents

- Source shape
- Direction and grouping
- Style classes
- Labels
- Rendering and limits

## Source shape

Keep the semantic source small and import the bundled theme from the same directory:

```d2
...@editorial-theme
direction: right

user: USER { class: entity }
gateway: GATEWAY { class: [entity; accent] }
service: SERVICE { class: entity }

user -> gateway: request { class: flow }
gateway -> service: { class: flow }
```

Copy `assets/editorial-theme.d2` beside the output source before rendering. D2 imports are resolved relative to the importing file. The theme's global globs style nested nodes and connections while unused classes remain invisible.

## Direction and grouping

- Use `direction: right` for a dominant pipeline or request path.
- Use `direction: down` for a hierarchy or staged decomposition.
- Use containers only for real ownership, runtime, trust, or deployment boundaries. Whitespace is enough for visual grouping.
- Let ELK calculate positions. Set explicit width or height only after a render shows that a highly connected node lacks usable routing surface.
- Do not use `near`, manual positions, or invisible spacer nodes to make the canvas look balanced.

## Style classes

Apply `entity` to technical components and combine it with one semantic class when needed:

- `accent`: every member of one actual role or the dominant path
- `muted`: inactive or contextual structure
- `hot`: at most one exceptional or risky element
- `flow`: every ordinary directed connection
- `[flow; secondary-connection]`: return, async, or subordinate connections

Zero accent or hot elements is valid. Do not alternate classes for variety. Avoid built-in special themes, sketch mode, icons, and fill patterns unless the user requests them or they encode a necessary distinction.

## Labels

- Prefer a short noun phrase on each node and a 1-3 word label on an edge.
- Keep implementation choices and external dependencies in distinct nodes.
- Use explicit labels only when direction and nearby node names do not already communicate the relationship.
- Prefer plain text. Markdown labels create `foreignObject` output that is less portable across SVG consumers.
- Quote labels that contain reserved D2 characters. Run the formatter and validator instead of guessing whether the source parses.

## Rendering and limits

The normal command is wrapped by `scripts/render_d2.sh` and resolves to:

```bash
d2 fmt --check input.d2
d2 validate input.d2
d2 --layout elk --pad 16 input.d2 output.svg
```

D2 currently accepts integer stroke widths and supports `mono` as the per-shape font choice. Its unfilled triangle is the closest portable match for the package's open arrowhead. Treat these as known approximations, not reasons to post-process every SVG.

The package was smoke-tested with D2 v0.8.2. Newer versions are acceptable when the documented commands and bundled theme validate successfully.

Official references: https://d2lang.com/tour/style/, https://d2lang.com/tour/classes/, https://d2lang.com/tour/imports-use-cases/, https://d2lang.com/tour/elk/, and https://d2lang.com/tour/exports/.
