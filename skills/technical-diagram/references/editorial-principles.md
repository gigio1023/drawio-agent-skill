# Editorial figure principles

Use these rules for the default editorial look across diagram backends.

## Communication before structure

- Treat a diagram as a small document with one communicative job. Before
  choosing shapes, identify the intended reader, the question the figure must
  answer, the one-sentence answer, and the context already supplied by the
  surrounding document.
- Source material is evidence, not a checklist of visible content. Include a
  fact only when it helps the intended reader reach that answer. Put versions,
  provenance, omitted scope, and implementation notes in surrounding prose or
  file metadata unless the figure is specifically about them.
- Do not assume private project vocabulary. Replace an unfamiliar internal name
  with its role, or introduce it once as `role (exact name)` when the identity
  matters. Expand an acronym on first use. Prefer reader language over code
  identifiers, endpoint paths, field names, and product codenames.
- Keep one abstraction level and one dominant reading path per figure. Runtime
  flow, internal implementation, alternatives, and neighboring systems become
  separate figures or prose when they answer different questions.
- Every visible block needs an explicit semantic relationship to the answer.
  Do not arrange disconnected facts or mini-panels side by side merely to make
  the page look substantial; use prose, a table, or a separate figure.
- Preserve complexity that is necessary to answer the question. Complexity in
  the source alone does not make it necessary in the figure.

## Content before composition

- Derive the minimum semantic nodes, relationships, groups, and annotations
  from the communication job above; do not copy the source inventory wholesale.
- Empty space is acceptable. Never add a title, subtitle, legend, caption,
  callout, rail, strip, badge, icon, inset, or mini-diagram to fill or balance
  the page.
- A supporting element is allowed only when it supplies context the intended
  reader needs and a direct node or edge label cannot carry. Remove it when the
  surrounding document already supplies that context.
- Use the simplest familiar shape that expresses each role. Shape variety must
  encode a real distinction.
- Reduce density in this order: remove facts that answer another question;
  replace internals with role-first labels; combine truly equivalent repeated
  elements; move detail to prose or metadata; then split by abstraction level.
  Enlarge the canvas only after those options fail. Never shrink type to make an
  overfull figure fit.

## Visual language

- White canvas, near-black ink, no shadows, and no gradients.
- Use one accent family per figure. A second family is reserved for a real
  two-system comparison; coral may mark at most one exceptional element.
- Use soft rounded rectangles, thin uniform strokes, and unfilled arrowheads.
- Use a monospace voice for entities, protocols, axes, and technical labels;
  use a sans-serif voice for human commentary or an explicitly required title.
- Keep labels short. One or two lines per component is the normal maximum.
- Use whitespace and alignment before adding container borders.
- Judge legibility at the intended delivery size, not while zoomed into the
  source. Every label must remain readable without magnification.

## Identity boundary

This is an independent editorial design language, not OpenAI branding. Never
add the OpenAI logo, blossom, or wordmark; never imply affiliation. OpenAI Sans
is not included. Use the substitute font stacks in `editorial-tokens.json`.
