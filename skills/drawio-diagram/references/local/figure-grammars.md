# Figure grammars

Only use one grammar per page on the first pass.

## Content gate

Choose a grammar to organize required information, never to fill a page. Begin
with the core geometry. A title, subtitle, legend, caption, rail, callout,
process strip, inset, or mini-visual is optional and may be added only when its
removal would make the requested meaning materially less clear. Empty space is
preferable to invented supporting content.

## 1. flow-canvas

Use when:

- the user wants a process, loop, or sequence
- component-to-component arrows matter most
- readability matters more than density

Structure:

- optional one-line title when standalone context requires it
- one main path or swimlane
- required primary components in left-to-right order, commonly 3-5
- no rail, strip, or footer unless it represents a required semantic relationship

## 2. report-split

Use when:

- the page needs both explanation and evidence
- one side is narrative and the other side is table/chart/card content

Structure:

- optional one-line title when standalone context requires it
- left narrative panel and right evidence panel only when both content types are required
- no takeaway or source strip; keep supporting prose outside the diagram unless explicitly required

## 3. system-map

Use when:

- the user wants a small architecture or service map
- there are distinct zones
- the page needs components grouped by role

Structure:

- optional one-line title when standalone context requires it
- required titled zones, commonly 2-3
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

- optional one-line title when standalone context requires it
- process strip only when a required sequence governs every panel
- required adjacent panels, commonly 2-4
- each panel communicates one claim only

## 5. annotated-chart-card

Use when:

- a chart is the main object
- the figure needs callouts, highlights, or inset notes
- the user wants compact explanatory density like strong tech-company research figures

Structure:

- optional one-line title when standalone context requires it
- one dominant chart card
- only callouts needed to interpret a specific feature
- direct labels before a compact legend
- no bottom takeaway or source strip unless the user explicitly requests it
