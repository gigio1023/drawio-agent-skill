# Text and labels

## Contents

- Line breaks and escaping
- Wrapping and fit
- Positioning keys
- Edge labels
- Titles, captions, and bottom strips
- Detail vs compactness
- Fonts

## Line breaks: the #1 text mistake

A literal `\n` inside a `value` attribute is two characters, backslash and n.
draw.io renders it as visible `\n` text, not a line break. XML does not
interpret backslash escapes.

| You want | Write in the `value` attribute | Requires |
| --- | --- | --- |
| Line break | `&lt;br&gt;` | `html=1` in style (this skill always sets it) |
| Line break (either mode) | `&#xa;` (same character as `&#10;`) | works with `html=0` and `html=1` |
| Literal backslash-n | `\n` | nothing - which is why it is usually a bug |

Standard two-line label:

```xml
<mxCell value="&lt;b&gt;Gateway&lt;/b&gt;&lt;br&gt;routes requests"
        style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
```

## Escaping

HTML inside `value` must be XML-escaped: `<` → `&lt;`, `>` → `&gt;`,
`&` → `&amp;`, `"` → `&quot;`. Unescaped `<b>` inside an attribute is malformed
XML and the file will not open. A plain `&` in prose (`R&D`) must be `&amp;`.

Text that should *display* angle brackets inside an HTML label needs double
escaping - once for HTML, once for XML. A rendered `<<abstract>>` stereotype
is written `&amp;lt;&amp;lt;abstract&amp;gt;&amp;gt;` in the attribute.

## Wrapping and fit

- `whiteSpace=wrap` makes long text wrap inside the shape; without it, text
  stays on one line and overflows. Set it on every framed shape with a label.
- Wrapping is a fallback, not a layout tool: if a label wraps into 3+ lines,
  shorten the label or widen the box.
- `overflow=hidden` clips instead of overflowing - avoid; clipped words read
  as missing information.

## Positioning keys (vertices)

- `align` (`left|center|right`) and `verticalAlign` (`top|middle|bottom`)
  place text inside the shape.
- `labelPosition` / `verticalLabelPosition` place the whole label block
  relative to the shape - use for icon-style shapes whose label sits below
  (`verticalLabelPosition=bottom;verticalAlign=top;`).
- `spacing`, `spacingLeft/Right/Top/Bottom` add inner padding; give labeled
  boxes `spacing=8` or more so text never hugs the border.

## Edge labels

Set `value` on the edge cell. Position with the edge geometry:

```xml
<mxCell id="e1" value="ack" style="edgeStyle=orthogonalEdgeStyle;html=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="a" target="b">
  <mxGeometry x="-0.4" y="-10" relative="1" as="geometry">
    <mxPoint as="offset" />
  </mxGeometry>
</mxCell>
```

- `x` in -1..1 slides the label along the edge (-1 source, 0 center, 1 target).
- `y` offsets perpendicular to the edge in pixels; use it to lift a label off
  the line.
- Every edge label needs an opaque `labelBackgroundColor` matching the canvas or
  containing panel (`#FFFFFF` above). Omitted, `none`, and transparent
  backgrounds let the connector show through the glyphs. Offset still helps
  placement, but it does not replace the background.
- Put labels on a straight segment of the route, never on a bend, and keep
  them out of other shapes' space. On short edges prefer no label and let a
  clearer shape label carry the meaning.
- Keep edge labels to 1-3 words (`ack`, `on failure`, `HTTP 429`).

## Titles, captions, and bottom strips

Give every free-standing text block exactly one role before placing it:

- **Title/subtitle:** frames the whole page; no connector.
- **Caption/callout:** explains a nearby region; align it to that region and do
  not connect it as though it were a component.
- **Semantic node/rail:** participates in the model; give it a precise noun or
  claim and connect only the relationship the diagram actually asserts.
- **Decoration:** delete it.

Do not fill the top or bottom with a dot-separated keyword garland merely to
balance whitespace. A list belongs there only when its items form a named set,
sequence, legend, or constraint that the reader needs. Write that relationship
explicitly instead of relying on proximity.

Center a page-level title on the page's actual content frame. Center a shared
bottom strip beneath the components it governs; if it belongs to one component,
size and align it under that component. A semantic center-to-center relation
should use a straight centerline connector. Do not attach a connector at the far
left or right and add a cosmetic dogleg, which makes the composition look
off-center even when the boxes are numerically aligned.

## Detail vs compactness: pick a level deliberately

Choose per element how much the reader needs at first glance, and use the
matching mechanism instead of stuffing prose into boxes:

1. **Name only** - one short noun phrase. Default for secondary components.
2. **Title + one line** - `&lt;b&gt;Title&lt;/b&gt;&lt;br&gt;short qualifier`.
   Default for primary components.
3. **Structured label** - an HTML `&lt;table&gt;` or `&lt;hr&gt;`-separated
   sections inside one shape (UML-class style) when the reader needs fields or
   attributes. Use sparingly; one structured shape per page region.
4. **Side rail / callout card** - explanation that supports the figure but is
   not a component. Keep it out of the flow corridors.
5. **Hover metadata** - wrap the cell in `<object>` and put long detail in
   attributes (shown via Edit Data / tooltips) instead of on the canvas. The
   canvas stays clean; the detail survives in the file.
6. **Another page** - when detail is a different abstraction level (context vs
   component vs deployment), add a named `<diagram>` page rather than
   cramming levels together.

Rule of thumb: the page tells the story with levels 1-2; levels 3-6 hold the
depth. A page where every box uses level 3 has no hierarchy.

## Fonts

- One `fontSize` for peer components (12-14), one for titles (24-28 in a title
  stack), one for captions (10-11). Three sizes per page is the ceiling.
- Whole-label bold via `fontStyle=1`; partial bold via `&lt;b&gt;` - never
  both for the same effect.
- Wide-character scripts (Korean, Japanese, Chinese) run wider than the same
  letter count in Latin; size boxes for the rendered width, and widen early
  instead of accepting mid-word breaks.
