# Editorial default style

This is the default visual style for every figure this skill produces when the
user does not name a different style. It reproduces the figure language used on
openai.com engineering and research posts from the February 2025 rebrand onward,
rebuilt from measured SVG sources (local corpus:
`notes/openai-figure-style/` in the maintainer workspace). Apply it fully;
do not mix it with Scheme A or Scheme B from `color-palettes.md` on the same
page.

## Contents

- Non-negotiables
- Tokens: color
- Tokens: typography
- Tokens: shape and stroke
- Page skeleton (title, legend, canvas)
- Node recipes (copy-paste styles)
- Edge recipes
- Charts in the same language
- Boundaries (brand safety)

`assets/editorial-default-template.drawio` implements this style end to end
(header, legend chips, both voices, solid/dashed/coral edges); seed new figures
from it when convenient.

## Non-negotiables

1. White canvas, no shadows, no gradients anywhere (`shadow=0`).
2. Ink is near-black `#0D0D0D`, never pure `#000000` and never gray for
   primary strokes or text.
3. Pick ONE accent family per page (blue is the default; green and coral are
   alternatives). A second family appears only to contrast two systems, and
   coral may additionally mark a single "hot" element on a blue or green page.
4. Two text voices: monospace for entity/system/technical labels (UPPERCASE
   for roles, mixed case for product names), sans-serif for the title and
   human commentary. Nothing else.
5. Thin open arrowheads, never filled triangles.
6. Whitespace is the grouping mechanism. Gap between sibling nodes is at least
   half a node width; when in doubt, add space instead of a container box.

## Tokens: color

Neutrals, always available:

| Token | Value | Use |
| --- | --- | --- |
| ink | `#0D0D0D` | text, neutral node strokes, arrows |
| canvas | `#FFFFFF` | page background, ordinary node fill |
| gray-fill | `#EEEEEE` | muted/inactive surface |
| gray-line | `#CCCCCC` | hairlines, inactive strokes |

Accent families - use one per page (light fill / chip / mid / deep):

| Family | light fill | chip | mid | deep |
| --- | --- | --- | --- | --- |
| blue (default) | `#EAF1FE` (alt `#CEDFFE`) | `#A3BEFA` | `#5477C4` | `#2E4780` |
| green | `#D8ECBD` | `#BEEB96` | `#71B436` | `#386411` |
| coral | `#FFEDDE` | `#FFBDA1` | `#FF9365` | `#CC6F47` (text `#804126`) |

Rules:

- Ordinary nodes are white with ink strokes. Light-fill marks a *layer or
  role* (for example every async component), not a random important box.
- A family-filled node takes either an ink stroke or the same family's deep
  stroke - never another family's color.
- Family mid/deep also colors that family's edges, legend chips, chart series,
  and short emphasized annotations. Family-colored text sits on white only.
- Coral as "hot element" appears 0-1 times. A page with no coral is normal.
- Dark mode: keep `adaptiveColors="auto"` and let draw.io derive it; these
  light-mode tokens are the single source of truth. (OpenAI's own dark
  variants keep the chip/light colors and swap surfaces to `#333333` -
  automatic derivation approximates this well.)
- Textured zone: originals use a fine dot-grid fill for zones and highlighted
  actors. `fillStyle=dots;` on the family light fill reproduces this and
  survives desktop-CLI export (verified; `sketch=1` is not required). Use it
  sparingly - the pale fill alone already carries the role.

## Tokens: typography

| Voice | Font stack | Case | Use |
| --- | --- | --- | --- |
| mono-label | `IBM Plex Mono, Menlo, monospace` | UPPERCASE | entity names, edge labels, legend labels, axis/series names |
| sans-title | `Inter, Helvetica Neue, Helvetica, sans-serif` | Mixed, bold | page title only |
| sans-body | `Inter, Helvetica Neue, Helvetica, sans-serif` | Mixed, regular | node sublines, captions, annotations |

Sizes on a ~1200px-wide page: title 30-32 bold; mono-label 13-14; sans-body
13-14; legend 12. Three sizes per page is still the ceiling.

Mechanics:

- Set the stack via `fontFamily=IBM Plex Mono, Menlo;` - the comma list is
  passed through to CSS, so Menlo covers macOS when Plex Mono is absent.
  A single font name with that font missing falls back to the default sans
  and silently loses the mono voice (verified in desktop-CLI export).
- Uppercase is authored in the text itself (`MEDIA FRONTEND`), not via CSS.
- Letterspacing for mono-label: wrap the label
  `&lt;span style=&quot;letter-spacing:1px&quot;&gt;...&lt;/span&gt;`. Skip it
  when a label is long enough to risk wrapping; correct case + mono already
  carries the voice.
- A node that needs both voices stacks them:
  `MONO NAME&lt;br&gt;&lt;font face=&quot;Inter&quot; style=&quot;font-size:12px&quot;&gt;sans qualifier&lt;/font&gt;`.

## Tokens: shape and stroke

| Property | Value |
| --- | --- |
| node corner radius | `rounded=1;absoluteArcSize=1;arcSize=8;` |
| chip/legend radius | full pill: `rounded=1;arcSize=50;` on a short box |
| stroke width, all shapes | `strokeWidth=1.2` (do not vary for emphasis) |
| edge stroke | `strokeWidth=1.2` solid ink |
| dashed (async/return) edge | `dashed=1;dashPattern=2 3;` |
| arrowhead | `endArrow=open;endFill=0;endSize=5;` |
| no start decoration | `startArrow=none;` |

Emphasis comes from fill (blue-fill) or the coral role, never from thicker
strokes or bigger fonts.

## Page skeleton

Every figure page carries the same header, left-aligned to the content frame:

1. **Title** (sans-title, bold, ink) at top-left. One line, sentence case,
   states the figure's claim or name: `GPT-Live system architecture`.
2. **Legend row** directly under the title, only when 2+ roles need naming:
   small circles (10-12px, `ellipse;` white fill + ink stroke, or blue-chip
   fill for the accent role) followed by mono-label text. Chips sit in one
   horizontal row, never a boxed legend panel.
3. **Canvas**: nodes on a loose grid below. First node row starts at least
   60px under the legend.

No logo, no footer strip, no caption band. Provenance/source lines belong in
the document that embeds the figure, not inside it.

## Node recipes

Ordinary component:

```text
rounded=1;absoluteArcSize=1;arcSize=8;whiteSpace=wrap;html=1;
fillColor=#FFFFFF;strokeColor=#0D0D0D;strokeWidth=1.2;fontColor=#0D0D0D;
fontFamily=IBM Plex Mono, Menlo;fontSize=13;align=center;spacing=10;shadow=0;
```

Emphasized component (role-based, e.g. every async-path box):
same as ordinary plus `fillColor=#EAF1FE;`.

Highlighted region (at most one per page):
same as ordinary plus `fillColor=#FFEDDE;`.

Inner sub-box (tools list, snapshot inside a server):
same as ordinary with `arcSize=4;fontSize=12;` inside a parent container.

Legend chip: `ellipse;fillColor=#FFFFFF;strokeColor=#0D0D0D;strokeWidth=1.2;`
10-12px, with an adjacent borderless mono-label text cell — or blue-chip
`fillColor=#A3BEFA;strokeColor=none;` for the accent entry.

Icon use stays minimal: at most one small line-art glyph per node, ink-colored,
above the label. Skip icons entirely rather than mixing icon styles.

## Edge recipes

Primary flow:

```text
edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#0D0D0D;
strokeWidth=1.2;endArrow=open;endFill=0;endSize=5;startArrow=none;
```

Async / return / delegation path: primary flow plus `dashed=1;dashPattern=2 3;`.

Coral-highlighted path (0-1 per page): primary flow with
`strokeColor=#FF9365;`.

Edge labels are mono-label UPPERCASE, 1-3 words (`USER AUDIO`,
`DELEGATION REQUEST`), placed above a straight segment with
`labelBackgroundColor=#FFFFFF;fontSize=12;`. The general edge-routing and
label-background rules in `edge-routing.md` and `text-and-labels.md` apply
unchanged.

## Charts in the same language

When the figure is a chart (drawn natively in draw.io), keep the identical
header pattern and voices: title sans bold, legend chips + mono labels, axis
labels mono uppercase, series in coral / coral-ink, gridless or minimal ink
axes with `strokeWidth=1.2`. Do not switch to a different "chart theme".

## Boundaries (brand safety)

This style borrows geometry, spacing, palette, and typographic structure —
which is fine. Do not borrow identity:

- Never place the OpenAI logo, wordmark, or blossom mark (the original figures
  carry one top-right; this skill's figures must not).
- Never label output as OpenAI-branded or imply affiliation.
- OpenAI Sans is proprietary; the Inter/IBM Plex Mono stacks above are the
  approved substitutes.
