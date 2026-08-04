# Layout safety

## Main principle

The goal is not maximum density. The goal is that the first human who opens the `.drawio` file can immediately see:

- what the components are
- which arrows matter
- what is primary vs secondary

## Overlap rules

- Primary components need roughly `200px` horizontal and `120px` vertical breathing room
- Keep at least `16px` inner padding inside ordinary boxes
- Keep at least `24px` padding from a panel border to its children
- If labels are long, shorten the labels first before expanding the canvas

## Routing rules

- Use one dominant path through the center of the page
- Reserve dedicated corridors for arrows before tightening component spacing
- Secondary arrows should use a separate corridor from the dominant path
- Long return loops should use a bottom or outer corridor, not cut through component labels
- If 2 edges want the same corridor, add waypoints
- If a node has multiple outgoing edges, vary ports with `exitX/exitY`
- Keep arrows visually outside label-heavy regions whenever possible
- Do not route arrows over component bodies, title bands, boundary labels, or edge labels

## Text rules

- Labels should usually be title + one short line
- Avoid paragraphs inside component boxes
- Avoid vertical labels on the first pass
- Move short notes and sources to a side rail or external caption when needed
- Avoid bottom legends or footer explanations inside the diagram; use semantic labels or split the page instead
- For multilingual or wide-character text, widen early instead of accepting accidental breaks

## Supporting-band rules

- A title/subtitle frames the page, a caption explains a region, and a semantic
  rail participates in the model. Choose one role; do not connect supporting
  prose as though it were a component.
- Delete top/bottom keyword lists whose removal would not change the reader's
  interpretation. If the list is a real legend, sequence, ownership boundary,
  or constraint set, name that role explicitly.
- Align page-level supporting text to the full content frame. Align region-level
  text to its region. Shared bottom rails sit centered beneath the components
  they govern, not shifted toward whichever component happened to connect last.
- Prefer a straight centerline for a whole-strip relationship. A far-edge
  attachment with a shallow two-bend dogleg is both harder to read and visually
  unbalanced.

## Human-editability rule

If the AI cannot make the layout perfect, it must still include the intended components cleanly enough that a human can rearrange them in draw.io without guessing what was omitted.

## Preflight

Before finishing:

1. No component overlaps another
2. No text escapes a component
3. Main arrows are direct and obvious
4. Secondary arrows are quieter than the main path
5. No arrowhead sits on a bend
6. The diagram is still understandable with no chat context
7. No edge crosses a title, caption strip, or dense label cluster without a strong reason
8. Arrow corridors remain clear after any layout tightening
9. Every top/bottom text band has a named information role or has been removed
10. Edge labels have opaque backgrounds matching the surface behind them

Then run:

```bash
python3 scripts/validate_drawio_xml.py path/to/file.drawio
python3 scripts/validate_drawio_layout.py path/to/file.drawio
```
