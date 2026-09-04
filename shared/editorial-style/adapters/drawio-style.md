# Editorial style for draw.io

Read `references/local/editorial-principles.md` first. The canonical values are
vendored in `assets/editorial-tokens.json`; the recipes below translate them to
draw.io style strings.

## Core rules

- Use `#FFFFFF` canvas and fills with `#0D0D0D` text, strokes, and primary
  edges. Set `shadow=0` and never use gradients.
- Use one accent family per page. Blue is the default: light `#EAF1FE`, chip
  `#A3BEFA`, mid `#5477C4`, deep `#2E4780`.
- Ordinary components use soft ~16px corners and a uniform `1.2` stroke.
- Technical labels use `IBM Plex Mono, Menlo, monospace`; human commentary uses
  `Inter, Helvetica Neue, Helvetica, Arial, sans-serif`.
- Use open, unfilled arrowheads. Emphasis comes from semantic fill or one hot
  element, never a thicker border or larger label.

`assets/editorial-default-template.drawio` is a minimal working sample of these
tokens. It intentionally has no title, legend, footer, or decorative inset.

## Component recipes

Ordinary technical component:

```text
rounded=1;absoluteArcSize=1;arcSize=32;whiteSpace=wrap;html=1;
fillColor=#FFFFFF;strokeColor=#0D0D0D;strokeWidth=1.2;fontColor=#0D0D0D;
fontFamily=IBM Plex Mono, Menlo, monospace;fontSize=13;align=center;spacing=10;shadow=0;
```

Role-based accent: add `fillColor=#EAF1FE;strokeColor=#2E4780;`.

Single hot element: add
`fillColor=#FFEDDE;strokeColor=#CC6F47;fontColor=#804126;`. Zero hot elements is
normal; never add one solely for visual variety.

Inner sub-box: use the ordinary recipe with
`absoluteArcSize=1;arcSize=8;fontSize=12;`.

A semantic zone may use `container=1;pointerEvents=0;` with no fill or the
page's light accent fill. Do not add a container merely to occupy space.

## Edge recipes

Primary flow:

```text
edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;strokeColor=#0D0D0D;
strokeWidth=1.2;endArrow=open;endFill=0;endSize=5;startArrow=none;
```

Secondary or return path: add `dashed=1;dashPattern=2 2;` and keep it outside
the dominant path's corridor. Edge labels use the mono voice, stay to 1-3
words, sit on a straight segment, and take an opaque background matching the
surface behind them.

## Backend limits

- Keep `adaptiveColors="auto"`; do not hand-author a full dark palette.
- A literal `\n` does not create a line break. Use `&lt;br&gt;` with `html=1`
  or `&#xa;`.
- When editing an existing diagram, match its established style unless the user
  explicitly requests a restyle.
