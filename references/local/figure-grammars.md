# Figure grammars

Only use one grammar per page on the first pass.

## 1. flow-canvas

Use when:

- the user wants a process, loop, or sequence
- component-to-component arrows matter most
- readability matters more than density

Structure:

- top title stack
- one main swimlane
- optional right rail
- optional bottom strip
- 3-5 primary components in left-to-right order

## 2. report-split

Use when:

- the page needs both explanation and evidence
- one side is narrative and the other side is table/chart/card content

Structure:

- top title stack
- left narrative panel
- right evidence panel
- bottom takeaway/source strip

## 3. system-map

Use when:

- the user wants a small architecture or service map
- there are distinct zones
- the page needs components grouped by role

Structure:

- top title stack
- 2-3 titled zones only
- arrows mostly between zones, not between every box
- minimal cross-links

If the architecture is larger than this, split it progressively:

- context page
- container page
- component page
- deployment or data-flow page only if needed

## Selection rule

If unsure, choose `flow-canvas`.

It is the safest grammar for preserving requested elements without creating unreadable overlap.

## 4. insight-panels

Use when:

- the user wants 2-4 adjacent insight cards
- each panel has its own title and mini-visual
- the figure should feel like a compact research summary

Structure:

- top title stack
- optional top process strip
- 2-4 adjacent panels
- each panel communicates one claim only

## 5. annotated-chart-card

Use when:

- a chart is the main object
- the figure needs callouts, highlights, or inset notes
- the user wants compact explanatory density like strong tech-company research figures

Structure:

- top title stack
- one dominant chart card
- one or more inset callout cards
- optional compact legend or direct labels
- bottom takeaway/source strip
