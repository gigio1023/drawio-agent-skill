---
name: editorial-chart
description: >
  Use when the user wants a data chart, graph, or plot in the clean editorial
  blog-figure look: line, bar, scatter, or dot-plot renderings of measured
  data, produced programmatically with matplotlib and exported to SVG/PNG.
  Trigger on "chart", "graph", "plot", benchmark-score figures, and requests
  for minimal blog-style data graphics. NOT for flowcharts, architecture
  diagrams, or box-and-arrow figures (use drawio-diagram), and NOT for
  interactive dashboards or web-embedded live charts.
---

# Editorial Chart

Render measured data as static charts in the editorial figure language: bold
sans title top-left, chip legend with uppercase mono labels, gridless ink
axes, one accent family per page. SVG is the primary artifact (text preserved
as text); a PNG proof render is mandatory before claiming success.

## Routing: chart or diagram?

Decide by the figure's content, not its name:

- **Measured data** - real numbers, many points, true scales (log axes,
  distributions, time series) - this skill.
- **Structure** - boxes, arrows, layers, pipelines, or a few illustrative
  values inside a larger schematic - the sibling `drawio-diagram` skill, which
  shares the same visual tokens.
- Borderline (3-8 bars): real measurements that may change → this skill (the
  chart regenerates from data); a decorative sketch inside a diagram →
  drawio-diagram.

## Quick start

1. Read [`references/chart-language.md`](references/chart-language.md) for the
   full rule set (anatomy, tokens, marks, dark mode).
2. Write a small script that imports the style module
   [`scripts/editorial_mpl.py`](scripts/editorial_mpl.py):
   `ed.use()` → plot with family colors → `ed.mono_ticks` / `ed.axis_label` /
   `ed.header` → `ed.save(fig, stem)` (writes `stem.svg` + `stem.png`).
   [`scripts/example_chart.py`](scripts/example_chart.py) is a working
   reference for both a line chart and grouped bars; copy its margin setup
   (`subplots_adjust` with `top≈0.80` clears the header row).
3. Run it. No system matplotlib is assumed - use
   `uv run --with matplotlib python <script>.py` (add other deps the same
   way). `findfont` warnings about Inter/IBM Plex Mono are expected on
   machines without those fonts; fallbacks carry the voice and the SVG keeps
   the full stack.
4. **Look at the PNG before finishing.** Check: no clipped direct labels or
   tick text (widen margins, not the font), legend row fits on one line, one
   accent family, no gridlines, title states a claim.

## Non-negotiables

- Data values come from the user or their files - never invent or "smooth"
  numbers. If a value is unknown, ask or leave the series out.
- Emphasis comes from color and direct labels, never thicker strokes or
  bigger fonts.
- Direct value labels on endpoints or one emphasized point only - never every
  point. Axis and tick text stays ink.
- One y-scale per chart. Two measures of different scale become two charts.
- Deterministic scripts: no RNG, no timestamps in output filenames.

## Brand safety

The look is modeled on openai.com editorial figures - geometry, palette, and
typographic structure only. Never add the OpenAI logo, blossom mark, or
wordmark; never label output as OpenAI-branded or imply affiliation. OpenAI
Sans is proprietary - the Inter/IBM Plex Mono stacks in the style module are
the approved substitutes.

## Verification before claiming done

1. The script ran cleanly and wrote both `.svg` and `.png`.
2. You rendered and actually viewed the PNG (step 4 above).
3. The SVG contains `<text` elements (fonts preserved), not outlined paths.
4. Every number in the chart traces to user-provided data.

## Gotchas

- matplotlib's default `svg.fonttype` is `path`: skipping `ed.use()` (or
  saving before it runs) silently outlines all text and kills editability.
  Verification step 3 catches this.
- Endpoint direct labels sit outside the axes and clip at the figure edge;
  reserve margin first (`subplots_adjust(right≈0.88)`). Fix clipping with
  margins, never smaller fonts.
- Coral mid (`#FF9365`) fails 3:1 contrast on white - keep coral series
  dashed or direct-labeled, and set coral value labels in `#804126`.
- `ed.header()` draws the canvas to measure each legend label, so call it
  after the figure size and margins are final; late `subplots_adjust` calls
  shift the plot under a already-placed header.
- `findfont` warnings for Inter/IBM Plex Mono are expected on machines
  without those fonts and are not a failure.
