# Editorial default style

This is the default visual style for every figure this skill produces when the
user does not name a different style. It reproduces the figure language used on
openai.com engineering and research posts from the February 2025 rebrand onward,
rebuilt from measured SVG sources (local corpus:
`notes/openai-figure-style/` in the maintainer workspace). Apply its visual
tokens consistently, but let the content determine the composition; do not mix
it with Scheme A or Scheme B from `color-palettes.md` on the same page.

## Contents

- Non-negotiables
- Tokens: color
- Tokens: typography
- Tokens: shape and stroke
- Content-led page composition
- Node recipes (copy-paste styles)
- Edge recipes
- Charts in the same language
- Boundaries (brand safety)

`assets/editorial-default-template.drawio` demonstrates the core node and edge
recipes without a default header or legend. Seed new figures from it when
convenient, then add only content the requested diagram actually needs.

## Non-negotiables

1. White canvas, no shadows, no gradients (`shadow=0`). (A style rule: 2 of
   the 65 corpus sources do contain a gradient; this skill still never adds one.)
2. Ink is `#0D0D0D`, never gray for primary strokes or text. The corpus
   sources actually emit pure `#000000`; the two are visually identical, and
   this skill standardizes on `#0D0D0D` so every figure carries one value.
3. Pick ONE accent family per page (blue is the default; green and coral are
   alternatives). A second family appears only to contrast two systems, and
   coral may additionally mark a single "hot" element on a blue or green page.
4. Two text voices: monospace for entity/system/technical labels (UPPERCASE
   for roles, mixed case for product names), sans-serif for the title and
   human commentary. Nothing else.
5. Thin open arrowheads, never filled triangles.
6. Whitespace is the grouping mechanism. Gap between sibling nodes is at least
   half a node width; when in doubt, add space instead of a container box.
   Whitespace may remain empty and never needs decorative content.

## Tokens: color

Neutrals, always available:

| Token | Value | Use |
| --- | --- | --- |
| ink | `#0D0D0D` | text, neutral node strokes, arrows |
| canvas | `#FFFFFF` | page background, ordinary node fill |
| gray-fill | `#EEEEEE` | muted/inactive surface |
| gray-line | `#CCCCCC` | hairlines, inactive strokes |
| gray-text | `#929591` | secondary/annotation text on white |

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
  variants keep the chip/light colors and swap surfaces to near-black darks -
  `#171717` and `#333333` both occur - so automatic derivation approximates
  this well.)
- Textured zone: the corpus uses a fine dot-grid fill as a first-class surface
  treatment (39 of 58 measured files). `fillStyle=dots;` on the family light
  fill reproduces it and survives desktop-CLI export (verified; `sketch=1` is
  not required - `sketch=1` turns it into hachure). Prefer the plain pale fill;
  use dots only when texture carries a required semantic distinction.
- A family mid value (`#5477C4`, `#71B436`, `#FF9365`) may fill one small
  emphasized node; give it ink or white text, whichever passes contrast.
  Large containers never take saturated fills.

## Tokens: typography

| Voice | Font stack | Case | Use |
| --- | --- | --- | --- |
| mono-label | `IBM Plex Mono, Menlo, monospace` | UPPERCASE | entity names, edge labels, legend labels, axis/series names |
| sans-title | `Inter, Helvetica Neue, Helvetica, sans-serif` | Mixed, bold | optional page title only |
| sans-body | `Inter, Helvetica Neue, Helvetica, sans-serif` | Mixed, regular | node sublines, captions, annotations |

Sizes on a ~1200px-wide page: title 30-32 bold; mono-label 13-14; sans-body
12-13; legend 12. Three sizes per page is still the ceiling.

Precedence: while this style is active, its typography and corner-radius rules
override the generic defaults in `text-and-labels.md` and `quality-gates.md`.
When a title is necessary, use the top-left title recipe below. Those files
still govern mechanics - escaping, wrapping, padding, edge-label backgrounds.

Mechanics:

- Set the stack via `fontFamily=IBM Plex Mono, Menlo, monospace;` - the comma
  list is passed through to CSS, and the generic keyword guarantees a real
  monospace on hosts without Plex Mono or Menlo (verified in desktop-CLI
  export). Sans text likewise ends in `sans-serif`. A single font name with
  that font missing falls back to a serif default and silently loses the
  voice (measured).
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
| node corner radius | `rounded=1;absoluteArcSize=1;arcSize=32;` (draw.io renders absolute arcSize at half its value, so this is a ~16px radius - the corpus median) |
| inner sub-box radius | `rounded=1;absoluteArcSize=1;arcSize=8;` |
| legend chip | `ellipse;` 10-12px (see Node recipes; do not use a rounded-rect pill for chips - it trips the peer-radius layout check) |
| state/terminal pill | `rounded=1;arcSize=50;` stadium, reserved for start/end/state nodes; the resulting peer-radius layout warning against process rects is a documented, accepted tradeoff |
| stroke width, all shapes | `strokeWidth=1.2` (corpus sources are 1.0 at their 596pt artboard; 1.2 matches that rendered weight at this page scale - do not vary for emphasis) |
| edge stroke | `strokeWidth=1.2` solid ink |
| dashed (async/return) edge | `dashed=1;dashPattern=2 2;` (the corpus's dominant dash) |
| arrowhead | `endArrow=open;endFill=0;endSize=5;` |
| no start decoration | `startArrow=none;` |

Emphasis comes from fill (blue-fill) or the coral role, never from thicker
strokes or bigger fonts.

## Content-led page composition

The canvas and its required semantic shapes are the default. Add page-level
text only when it changes how the figure is understood:

1. **Title, optional**: add a one-line, sentence-case sans-title at top-left
   only when the figure must stand alone and its subject or claim is not already
   clear from the surrounding artifact. Do not add a subtitle by default.
2. **Legend, optional**: prefer direct labels. Add a compact horizontal legend
   only when two or more visual encodings cannot be understood directly; the
   mere presence of multiple roles does not require one.
3. **Canvas**: fit the content frame to the actual nodes and routes. Do not keep
   an empty header, footer, or side region in case optional material is added.

Do not add logos, footer strips, caption bands, takeaways, source lines, chips,
or decorative mini-diagrams to fill whitespace or make the page look finished.
If provenance is explicitly required, keep it terse and place it in the
embedding document when possible.

## Node recipes

Ordinary component:

```text
rounded=1;absoluteArcSize=1;arcSize=32;whiteSpace=wrap;html=1;
fillColor=#FFFFFF;strokeColor=#0D0D0D;strokeWidth=1.2;fontColor=#0D0D0D;
fontFamily=IBM Plex Mono, Menlo, monospace;fontSize=13;align=center;spacing=10;shadow=0;
```

Emphasized component (role-based, e.g. every async-path box):
same as ordinary plus `fillColor=#EAF1FE;`.

Highlighted region (at most one per page):
same as ordinary plus `fillColor=#FFEDDE;`.

Inner sub-box (tools list, snapshot inside a server):
same as ordinary with `arcSize=8;fontSize=12;` inside a parent container.

Legend chip: `ellipse;fillColor=#FFFFFF;strokeColor=#0D0D0D;strokeWidth=1.2;`
10-12px, with an adjacent borderless mono-label text cell — or blue-chip
`fillColor=#A3BEFA;strokeColor=none;` for the accent entry.

Titled zone (system-map grammars): a `container=1;pointerEvents=0;` region
with the ordinary-component style, `fillColor=none` or the family light fill,
and a sans bold zone name at top-left inside
(`verticalAlign=top;align=left;spacingLeft=14;spacingTop=10;fontFamily=Inter,
Helvetica Neue, Helvetica, sans-serif;fontStyle=1;`). Zones never take
saturated fills.

Icons are opt-in: use a small line-art glyph only when it carries meaning the
label does not or the user requests it. Never add icons merely to make nodes
feel less empty, and skip them entirely rather than mixing styles.

## Edge recipes

Primary flow:

```text
edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;strokeColor=#0D0D0D;
strokeWidth=1.2;endArrow=open;endFill=0;endSize=5;startArrow=none;
```

(`rounded=1` gives bends the small curve the corpus uses and matches the
canonical edge form in `edge-routing.md`.)

Async / return / delegation path: primary flow plus `dashed=1;dashPattern=2 2;`.

Coral-highlighted path (0-1 per page): primary flow with
`strokeColor=#FF9365;`.

Edge labels naming systems or protocols are mono-label UPPERCASE, 1-3 words
(`USER AUDIO`, `DELEGATION REQUEST`); labels phrasing a human action or
qualifier may be sans mixed-case (`Pre-processed offline`) - the corpus uses
both by that role split. Place labels above a straight segment with
`labelBackgroundColor=#FFFFFF;fontSize=12;`. The general edge-routing and
label-background rules in `edge-routing.md` and `text-and-labels.md` apply
unchanged.

## Charts in the same language

When the figure is a chart (drawn natively in draw.io), keep the identical
voices and content gate: use a sans bold title or legend chips only when the
chart needs them, axis labels mono uppercase, and gridless or minimal ink axes
with `strokeWidth=1.2`.
Series colors come from the page's accent family ramp; the corpus also uses
purpose-built palettes for special forms (perceptual scales on heatmaps), so
multi-hue series are allowed when the data demands them. What must not
change is the voices and axis treatment - there is no separate "chart theme".

Native draw.io charts are for *schematic* charts only - a few illustrative
bars or a sketched trend inside a larger figure. A chart of measured data
(real values, many points, log or true scales) belongs to the sibling
`data-chart` skill, which renders this same language with matplotlib.

## Boundaries (brand safety)

This style borrows geometry, spacing, palette, and typographic structure —
which is fine. Do not borrow identity:

- Never place the OpenAI logo, wordmark, or blossom mark (the original figures
  carry one top-right; this skill's figures must not).
- Never label output as OpenAI-branded or imply affiliation.
- OpenAI Sans is proprietary; the Inter/IBM Plex Mono stacks above are the
  approved substitutes.
