# Direct SVG fallback

Use direct SVG only for an explicit SVG-source request, an existing SVG edit, an irregular editorial composition D2 cannot express, or a missing D2 renderer when SVG output is still required.

## Contract

- Read `assets/editorial-tokens.json` and apply the same canvas, palette, typography, radius, stroke, and no-shadow/no-gradient rules.
- Use a finite `viewBox` with all visible geometry inside it.
- Give semantic groups stable IDs. Keep markers, gradients, filters, and CSS definitions in `<defs>` only when the visible result needs them.
- Keep text as `<text>` rather than paths. Use explicit `text-anchor` and conservative text widths; SVG does not wrap text automatically.
- Route edges behind labels and between component boundaries. Marker tips must end at the boundary, not inside the box.
- Do not add illustration, texture, decorative dots, a title area, or footer merely because direct SVG offers more freedom than D2.

## Verification

Run:

```bash
python3 scripts/validate_svg.py output.svg
```

Then render or open the SVG and inspect it. Parsing cannot detect clipped text, bad font fallback, edge collisions, or elements that should not exist. Compare the finished IDs and labels against the required semantic inventory and apply the negative-space audit in `references/review.md`.
