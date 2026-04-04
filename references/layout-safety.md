# Layout safety

## Main principle

The goal is not maximum density. The goal is that the first human who opens the `.drawio` file can immediately see:

- what the components are
- which arrows matter
- what is primary vs secondary

## Overlap rules

- Primary components need roughly `200px` horizontal and `120px` vertical breathing room
- Keep at least `24px` padding from a panel border to its children
- If labels are long, shorten the labels first before expanding the canvas

## Routing rules

- Use one dominant path through the center of the page
- Secondary arrows should use a separate corridor
- Long return loops should use a bottom corridor
- If 2 edges want the same corridor, add waypoints
- If a node has multiple outgoing edges, vary ports with `exitX/exitY`
- Keep arrows visually outside label-heavy regions whenever possible

## Text rules

- Labels should usually be title + one short line
- Avoid paragraphs inside component boxes
- Move notes, sources, and captions to the bottom strip or side rail
- For multilingual or wide-character text, widen early instead of accepting accidental breaks

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
