# Community lessons

This file records what is worth borrowing from community draw.io skills and adjacent diagram ecosystems.

## `bahayonghang/drawio-skills`

Useful lessons:

- think in runtime modes: offline-first, desktop-enhanced, optional live review
- split handling by route instead of treating every diagram request the same
- use multiple validator mindsets:
  - structure
  - layout
  - quality
- dense edge routing deserves its own audit pass

What not to copy blindly:

- a heavy YAML-first workflow before the basic authoring loop is stable
- too many routes and profiles for ordinary requests

## C4-style ecosystems

Useful lessons:

- large systems become readable only when split by abstraction level
- context/container/component/deployment separation beats one giant page

## Practical takeaway

The best external skills are strong where they narrow scope:

- one canonical source of truth
- one runtime default
- one validation pass per failure mode

This skill stays focused on:

- native `.drawio`
- compact and editable structure
- readable component-to-component arrows
- explicit visual hierarchy
