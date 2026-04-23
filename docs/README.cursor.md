# drawio-diagram for Cursor

Native `.drawio` authoring for Cursor.

## Install

Preferred:

```bash
npx skills add gigio1023/drawio-agent-skill@drawio-diagram --agent cursor
```

Or tell Cursor:

```text
Fetch and follow instructions from https://raw.githubusercontent.com/gigio1023/drawio-agent-skill/refs/heads/main/.cursor/INSTALL.md
```

Manual installation is documented in `.cursor/INSTALL.md`.

## Prerequisites

- Authoring: none beyond the skill.
- Export: draw.io CLI (draw.io Desktop or `npx @hediet/drawio-export`). See per-OS paths in `SKILL.md`.

## Usage

Cursor activates the skill when you ask for a draw.io artifact, a flowchart, an architecture diagram, a class/ER/sequence diagram, or any diagram that should be editable after the first pass. Add a format word to export alongside the `.drawio`.

```text
Make a draw.io system map for the ingestion pipeline.
Generate a .drawio.svg for the deploy pipeline.
Turn this design doc section into a compact editorial figure in draw.io.
```

## Output

- Default: `.drawio` source only.
- With format hint: `.drawio` + `.drawio.{png|svg|pdf}` (source preserved).

## Troubleshooting

| Problem | Fix |
|---------|-----|
| CLI not found | Install draw.io Desktop or use `npx @hediet/drawio-export` |
| Labels overflow shapes | Shorten labels before enlarging the canvas; see `references/local/layout-safety.md` |
| Arrows tangle | Bundle fan-out / fan-in via a shared trunk; see `references/fetched/xml-reference.md` orthogonal routing section |

## Deeper references

- `SKILL.md` - authoring workflow.
- `references/fetched/xml-reference.md` - vendored upstream XML reference (Apache-2.0).
- `references/fetched/style-reference.md` - vendored upstream style/shape catalog.
