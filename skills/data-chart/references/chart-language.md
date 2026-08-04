# The editorial chart language

Measured from data charts in post-2025 openai.com editorial figures (line
charts, dot plots, bar charts; the same corpus that grounds the sibling
drawio-diagram skill's `editorial-default-style.md`). The originals are Figma
exports, not library output - the look is a design language, and these are its
rules restated for programmatic rendering.

## Contents

- Page anatomy
- Tokens: color
- Tokens: typography
- Series and marks
- Direct labels
- Dark mode
- What the corpus never does

## Page anatomy

1. **Title** top-left, bold sans, sentence case, states the chart's claim
   (`Success rate scales with agent budget`), never centered.
2. **Legend** directly under the title when 2+ series need naming: small
   filled circles (chips) followed by UPPERCASE mono labels, one horizontal
   row, no boxed panel. A single series gets no legend - the title names it.
3. **Plot area** below with generous whitespace. Left and bottom spines only,
   ink-colored, ~1.2px at a ~1200px page. Small outward ticks. **No
   gridlines.** No top/right spines.
4. Axis titles UPPERCASE mono; tick labels mono. Percent signs attach to the
   number (`38.1%`).

Original artboards are 596pt wide with light/dark and desktop/mobile variants;
a 4:3-ish aspect with ample margins reads closest.

## Tokens: color

Same values as the drawio skill's editorial default:

| Token | Value |
| --- | --- |
| ink (text, axes) | `#0D0D0D` |
| canvas | `#FFFFFF` |
| gray-text (secondary) | `#929591` |
| gray-line (hairlines) | `#CCCCCC` |

Accent families (light fill / chip / mid / deep) - one family per chart, a
second only to contrast two systems:

| Family | light | chip | mid | deep |
| --- | --- | --- | --- | --- |
| blue (default) | `#EAF1FE` | `#A3BEFA` | `#5477C4` | `#2E4780` |
| green | `#D8ECBD` | `#BEEB96` | `#71B436` | `#386411` |
| coral | `#FFEDDE` | `#FFBDA1` | `#FF9365` | `#CC6F47` (text `#804126`) |

Series color assignment: lines and dots take the family **mid**; bars take
**light or chip fill with an ink stroke** (the corpus draws bars as outlined
shapes, not flat fills). The blue-mid + coral-mid pair passes CVD validation
(ΔE 23.2) - keep coral series dashed or direct-labeled since coral sits below
3:1 contrast on white.

## Tokens: typography

| Voice | Stack | Use |
| --- | --- | --- |
| sans (bold) | `Inter, Helvetica Neue, Helvetica, Arial, sans-serif` | title |
| mono | `IBM Plex Mono, Menlo, monospace` | axis labels (UPPERCASE), tick numerals, legend labels (UPPERCASE), direct value labels |

OpenAI Sans is proprietary; these stacks are the approved substitutes. SVG
output must keep text as text (`svg.fonttype: none`) so the stack travels with
the file; hosts without Inter/Plex fall back to Helvetica/Menlo and keep the
voice.

## Series and marks

- Line width ~2.4 at a 1200px page (corpus: 2-3 at 596pt). Round caps.
- Dashed series and reference lines use dash pattern `4 4`.
- Scatter/dot marks ≥ 8px; the corpus dot plot draws dense strokes in family
  mid with the contrasting sub-series in family deep.
- Bars: thin ink outline (1.2), squared ends, value labels in mono ink above
  the bar. Two models on one benchmark = chip fill vs light fill, same family.
- One y-scale. Never a dual-axis chart; split into two charts instead.

## Direct labels

The corpus labels line endpoints (or one emphasized point) with the value in
the series color, mono, e.g. `38.1%` - and never labels every point. Axis text
stays ink; only these short value annotations take series color (deep/text
step for coral, which is illegible at mid on white).

## Dark mode

A separate render, not a filter: canvas `#0D0D0D`, ink/text `#FFFFFF`,
secondary text stays `#929591`. Series colors step brighter - chips, or the
measured dark pair blue `#8386EB` / magenta `#CE55D3` - because family mids
sink into the dark surface. Produce dark variants only when asked; light is
the default.

## What the corpus never does

- Gridlines, boxed legends, centered titles, axis frames on all four sides.
- Filled arrowheads, drop shadows, gradients, background tints behind the plot.
- More than one accent family without a two-system contrast to justify it.
- A number on every data point, or rainbow multi-series palettes.
- The OpenAI logo or wordmark - the originals carry one top-right; charts
  produced with this skill must not (see Brand safety in SKILL.md).
