# Real-world gotchas

These come from repeated iteration failures in real diagram sessions.

## Border-hugging text

- Long labels inside small boxes often look fine in XML but render glued to the border.
- Fix order:
  1. shorten the text
  2. add `spacingLeft`, `spacingRight`, `spacingTop`, `spacingBottom`
  3. widen the box only if the label is irreducible

## Inconsistent corner radius

- `rounded=1` by itself is not enough for visual consistency across boxes.
- If a page uses rounded rectangles, explicitly set `absoluteArcSize=1;arcSize=12;` on every peer box.

## False compactness

- A cramped page can look "information dense" in code review but unreadable when opened in draw.io.
- Compact means fewer components, shorter labels, and clearer corridors, not smaller gaps everywhere.

## Parent overflow

- Children often spill outside a container when the parent was treated as decorative only.
- Treat containment as a real constraint. Child boxes and child text must stay inside the parent's content area.

## Ambiguous labels

- `options and tools` mixes two different concepts.
- `artifact` is not always the right return label for A2A-level diagrams.
- `your logic` is vague if the user needs to know what they actually own.
- Prefer precise, stable labels over catchy ones.

## Arrow corridor collisions

- Auto-routing alone is not enough when multiple edges want the same corridor.
- If a dominant path and a secondary path compete, give the secondary path a different corridor or explicit waypoints.

## Straight path opportunities

- If a request/response pair can be made visually straight by moving one box, do that before adding bends.
- Straight arrows are easier to read than elegant-looking elbows.

## Export quality

- PNG is useful for README embedding, but SVG is the better review artifact when fine text matters.
- For high-resolution PNG review on 4K displays, export with `--width 3840` or an equivalent scale.
