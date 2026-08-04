# Review loop

Use this when a diagram is headed for review, when the user asks for exported
artifacts, or after a reviewer complains that the figure is technically valid
but visually hard to read.

## What recent review taught

The most common failure is not invalid XML. It is a diagram that has all the
right parts but still makes the reader work too hard because arrows, labels, and
boundaries compete for the same space.

## Routing audit

Before export:

1. Identify the single dominant path. It should be readable without following every secondary edge.
2. Reserve arrow corridors before tightening the layout.
3. Keep arrows out of component bodies, title bands, label text, and boundary labels.
4. Give return paths and secondary paths their own corridors; do not stack them directly on the main path.
5. Use explicit waypoints when auto-routing would cross a label, run along a box edge, or share a corridor ambiguously.
6. Put edge labels on straight segments with enough empty space around them.

If the layout only works because a reader already knows the explanation from chat, simplify it.

## Layout audit

- Prefer tighter spacing only after every arrow has a clear route.
- Keep boxes close enough to show sequence, but not so close that arrowheads touch borders.
- Avoid bottom legends or explanatory footers inside the diagram. They usually
  become a second narrative competing with the figure.
- If a note is essential, turn it into a semantic label, a side rail, or a separate page.
- Group with semantic boundaries: external caller, runtime/container, internal
  sections, implementation choices, and external dependencies should not
  collapse into one box.
- One page should have one dominant reading path. If two paths feel equally
  important, split the page or make one path secondary.

## Export artifact choice

- Prefer SVG for review when text sharpness and edge clarity matter.
- Use PNG for README/chat compatibility, but normalize it for review with a high
  width such as `--width 3840`.
- Keep the `.drawio` source beside every export.
- If exporting both SVG and PNG, inspect SVG first for geometry and PNG second for rasterization issues.

## Visual QA

After export, inspect the actual artifact, not only the XML:

- no arrows over labels, component text, titles, or boundary names
- no arrowheads on bends, labels, or box borders
- no labels clipped by box edges
- no low-resolution or fuzzy text in the PNG fallback
- no footer text that explains what the diagram failed to communicate visually
- semantic boundaries are obvious without reading a separate legend
- SVG opens sharply; PNG matches the intended framing after normalization

If the exported image fails one of these checks, fix the `.drawio` source and export again.
