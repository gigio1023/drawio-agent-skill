# Visual patterns

This file summarizes the reusable visual lessons taken from recent official OpenAI, Anthropic, and Vercel materials.

## Shared lessons

- Strong title stack first, figure second
- One dominant message per panel
- Dense information is acceptable only when hierarchy is unmistakable
- Captions and callouts do explanatory work outside the main geometry
- Neutral backgrounds and restrained accent colors outperform decorative styling
- Rounded panels with thin strokes read better than busy card treatments
- In strong examples, each panel answers one question, not many at once
- Small inset legends, metric chips, and annotation strips help compactness without clutter
- The best figures separate `workflow`, `evidence`, and `takeaway` instead of mixing all three in one box
- Strong diagrams do not rely on a bottom footer to explain the figure; the visual hierarchy and labels carry the idea

## OpenAI-leaning patterns

Measured from post-Feb-2025 editorial figures (the SVG sources, not
impressions). This language is codified as this skill's default in
`editorial-default-style.md`; the notes here are for recognizing it.

- White canvas, zero shadows, zero gradients; near-black ink (`#0D0D0D`)
- Header pattern: bold sans title top-left, then a legend chip row, then canvas
- Two text voices: monospace entity labels (UPPERCASE roles, mixed-case product
  names), sans mixed-case support text
- Thin uniform strokes (~1.2px) and small open V arrowheads, never filled triangles
- One accent family per figure (blue, green, or coral) as light fills, family
  strokes, and dotted zone textures; everything else stays white
- Node names are short and operational; one active logic path is emphasized
- Compactness comes from whitespace plus strong alignment, not from squeezing
  more labels into the page
- Even data charts keep the same header, legend chips, and mono axis labels

## Anthropic-leaning patterns

- Editorial research-panel feel
- Multi-panel layouts with direct titles over each insight block
- Compact but readable chart and annotation pairing
- Callouts often carry the takeaway, not just decoration
- Good for report figures, comparisons, and mechanism explanations
- Warm off-white backgrounds plus fine gray strokes support dense content without looking noisy
- The strongest Anthropic figures often stack: process strip at top, insight panels below, chart+caption pairs inside
- Prompt snippets and qualitative examples live in pale inset cards, distinct from the chart itself

## Vercel-leaning patterns

- Architecture clarity and clean boundaries
- Crisp spacing and concise labels
- Minimal clutter around diagrams
- Strong separation between central asset and supporting description
- Good for system maps and infrastructure explainers
- Vercel visuals often use one central hub or one editor surface as the organizing principle
- Hub-and-spoke or builder-canvas compositions work better than many peer boxes with tangled links
- Hero visuals can be dramatic, but explanatory diagrams still stay sparse and operational

## What to borrow

- compactness with explicit hierarchy
- callout discipline
- short labels
- visible narrative flow
- annotation outside the busiest geometry
- small legends and chips that help scanning, not large explanatory footers
- one central organizing frame per figure
- charts with direct labeling instead of forcing the reader to bounce between plot and legend

## What not to borrow

- logos, trademarks, product screenshots, and proprietary brand marks
- proprietary typefaces (OpenAI Sans, Styrene); use the substitute stacks in
  `editorial-default-style.md`
- proprietary illustration systems and mascot/spot-art styles
- decorative complexity that hides the main message

Palette values and geometric conventions are fair to reuse; identity marks and
font files are not.
