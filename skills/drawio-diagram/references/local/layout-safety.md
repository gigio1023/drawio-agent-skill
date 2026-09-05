# Layout safety

## Main principle

The goal is not maximum density. The goal is that the first human who opens the `.drawio` file can immediately see:

- what the components are
- which arrows matter
- what is primary vs secondary
- what question the figure answers, without private project vocabulary

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
- Move notes, sources, versions, and excluded scope to surrounding prose or file metadata unless they are the subject
- Avoid bottom legends or footer explanations inside the diagram; use direct semantic labels or split the page instead
- For multilingual or wide-character text, widen early instead of accepting accidental breaks
- Check text at the intended delivery size and never shrink it to preserve an overfull page

## Supporting-text rules

- A short title may frame a standalone page when surrounding context is absent. A callout may identify one required feature. A semantic node participates in the model. Choose one role; do not connect supporting prose as though it were a component.
- Delete top/bottom keyword lists whose removal would not change the reader's interpretation. If the list is a real legend, sequence, ownership boundary, or constraint set, name that role explicitly.
- Remove subtitles, footer summaries, and separate explanatory regions when the surrounding document or direct labels already carry the same meaning.

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
9. Every free-standing text block has a named, answer-relevant purpose or has been removed
10. Edge labels have opaque backgrounds matching the surface behind them

Then run:

```bash
python3 scripts/validate_drawio_xml.py path/to/file.drawio
python3 scripts/validate_drawio_layout.py path/to/file.drawio
```
