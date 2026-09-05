# Color palettes

The default styling for this skill, including its palette, lives in `editorial-default-style.md` and applies whenever the user does not name a style. The schemes below are alternatives to use on request - for example when the user wants the stock draw.io look their team already edits, or an indigo report scheme. Never mix two schemes on one page.

Readability beats decoration. Pick one scheme per page, assign colors by semantic role, and keep most of the page neutral so the one accent color can carry meaning.

## Scheme A: draw.io standard pairs (stock draw.io look, on request)

These are the stock draw.io UI pairs. Always use fill and stroke together as a pair; never mix a fill from one row with a stroke from another.

| Role suggestion | fillColor | strokeColor |
| --- | --- | --- |
| Primary flow / main components | `#DAE8FC` | `#6C8EBF` |
| Data stores / success states | `#D5E8D4` | `#82B366` |
| Decisions / caution | `#FFF2CC` | `#D6B656` |
| Errors / risky paths | `#F8CECC` | `#B85450` |
| Async / queues / background jobs | `#E1D5E7` | `#9673A6` |
| External systems / third parties | `#FFE6CC` | `#D79B00` |
| Neutral / infrastructure | `#F5F5F5` | `#666666` |

Use `fontColor=#333333` on all of these fills. These pairs are what humans expect from a draw.io diagram; a reader can edit the file later and the stock color picker offers the same swatches.

## Scheme B: editorial neutral (for report-grade figures)

A restrained slate-plus-one-accent scheme, matching this repo's sample assets:

| Role | Style values |
| --- | --- |
| Page/panel background | `fillColor=#F8FAFC` or `none`, `strokeColor=#CBD5E1` |
| Panel header band | `swimlaneFillColor=#EEF2FF` |
| Ordinary component | `fillColor=#FFFFFF;strokeColor=#CBD5E1;strokeWidth=1.2` |
| Emphasized component | `fillColor=#EEF2FF;strokeColor=#6366F1;strokeWidth=1.6` |
| Primary edge | `strokeColor=#6366F1;strokeWidth=2` |
| Secondary edge | `strokeColor=#94A3B8;strokeWidth=1.2;dashed=1` |
| Title text | `fontColor=#111827` |
| Supporting text | `fontColor=#4B5563` |
| Callout / note card | `fillColor=#FEF3C7;strokeColor=#F59E0B;fontColor=#78350F` |

Swap the indigo accent (`#6366F1`/`#EEF2FF`) for another hue if the subject calls for it, but keep exactly one accent hue per page.

## Rules that keep any palette readable

- One accent hue per page. Everything else stays neutral (white, near-white, slate). If two things compete for attention, the diagram has two messages - split the page instead of adding a second accent.
- Large containers get pale or no fill (`fillColor=none` or near-white). Saturated fills belong on small shapes only; a saturated 900px swimlane drowns everything inside it.
- Stroke is always darker than fill from the same hue. Light fill + darker same-hue stroke + dark gray text is the contract for every framed shape.
- Text contrast first: `#333333` or darker on light fills. Never place mid-gray text on colored fills.
- Do not encode meaning in color alone. Pair color with position, a label, or a stroke treatment (dashed vs solid) so the figure survives grayscale printing and color-blind readers.
- Edges: the dominant path gets the accent color and heavier stroke; secondary and return paths are gray and/or dashed. Never give each edge its own color.

## Dark mode

- Keep `adaptiveColors="auto"` on `mxGraphModel` (the XML validator enforces it). draw.io then auto-derives dark-mode variants of explicit colors.
- Prefer omitting `fontColor`/`strokeColor` where the theme default works: `default` resolves to black in light mode and white in dark mode.
- Use `light-dark(#lightHex,#darkHex)` in a style only when the automatic inversion of a specific color looks wrong. Do not hand-author a full dark palette.
