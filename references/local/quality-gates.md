# Quality gates

This file turns repeated review pain into hard finishing gates.

## Meaning

- Do not mix implementation choices and external dependencies in one box.
- Preserve semantic boundaries: callers, runtime/container, internal sections, implementation choices, and external dependencies are separate roles unless the user explicitly wants them merged.
- If a label is not unambiguously correct, simplify it. Prefer `response` over a narrower word unless the narrower word is exact.
- Prefer `Agent logic`, `Runtime layer`, `A2A interface` style labels over vague labels like `options and tools`.

## Layout

- No framed component may overlap another framed component.
- Keep at least `16px` inner padding in ordinary boxes.
- Keep at least `24px` padding from a container border to child components.
- Children must stay fully inside their parent.
- If a swimlane has a header, children must stay below the header band.
- Tight layout is acceptable only after arrows have dedicated corridors and labels still breathe.
- If a layout feels crowded, split the page or shorten labels before widening the canvas.
- Avoid bottom legends or explanatory footers that restate the diagram. Prefer semantic labels, a side rail, or a second page.

## Text

- Do not use vertical text for main labels.
- Component labels should usually fit in one or two lines.
- Avoid paragraphs inside boxes.
- If text comes close to the border, add spacing before resizing the box.
- If the same type of component repeats, keep font size, alignment, and padding consistent.

## Arrows

- There must be one visually dominant path.
- Secondary arrows should use a quieter corridor.
- Put edge labels on straight segments, not on bends.
- If the orchestrator and interface can be aligned for a straight request/response pair, do that.
- Do not let arrows or arrowheads sit on top of labels, component bodies, titles, boundary names, or box borders.
- If auto-routing crosses text or components, add waypoints or move boxes before accepting the route.

## Shape consistency

- Use one rounded-rectangle recipe per page.
- For small-radius rounded boxes, prefer `rounded=1;absoluteArcSize=1;arcSize=12;`.
- Do not mix heavily rounded boxes with lightly rounded boxes unless the distinction carries meaning.

## Verification

Before finishing, run:

```bash
python scripts/validate_drawio_xml.py path/to/file.drawio
python scripts/validate_drawio_layout.py path/to/file.drawio
```

If either validator complains, fix the diagram or explicitly accept the tradeoff in the final response.

When an export is part of the deliverable, inspect the exported SVG or high-resolution PNG before finishing. The validators are necessary but not sufficient for visual quality.
