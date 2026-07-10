# drawio-diagram for Claude Code

Native `.drawio` authoring for Claude Code. Claude can load it from a natural
language description match or the explicit `/drawio-diagram` invocation.

## Install

Preferred:

```bash
npx skills add gigio1023/drawio-agent-skill@drawio-diagram --agent claude-code
```

Or tell Claude Code:

```text
Fetch and follow instructions from https://raw.githubusercontent.com/gigio1023/drawio-agent-skill/refs/heads/main/.claude/INSTALL.md
```

Manual installation is documented in `.claude/INSTALL.md`.

## Prerequisites

- Authoring `.drawio` source files needs no extra tools - the skill writes native mxGraphModel XML directly.
- Exporting to PNG / SVG / PDF needs the draw.io CLI:
  - macOS: install [draw.io Desktop](https://github.com/jgraph/drawio-desktop/releases); the bundled binary lives at `/Applications/draw.io.app/Contents/MacOS/draw.io`.
  - Linux: `drawio` on PATH (snap / apt / flatpak).
  - Headless / CI: `npx --yes @hediet/drawio-export`.

## Usage

Talk naturally. The skill activates on phrases like "make a draw.io diagram", "architecture diagram", "flowchart", and explicit format hints.

```text
Make a draw.io architecture diagram for this ingestion pipeline.
Turn this research section into a compact editorial figure in draw.io.
Generate a .drawio.svg file with arrows between these four components.
Make a png class diagram for the models in src/.
```

If you include a format word (`png`, `svg`, `pdf`), the skill exports to the matching `.drawio.*` file after authoring and keeps the `.drawio` source alongside it (intentional divergence from upstream - the source stays as the editable truth).

## Output

- Default: `.drawio` source only.
- With format hint: `.drawio` + `.drawio.{png|svg|pdf}` (both kept).

## Troubleshooting

| Problem | Fix |
|---------|-----|
| "draw.io CLI not found" | Install draw.io Desktop, or use `npx @hediet/drawio-export` |
| Export blank / edges missing | Every edge needs `<mxGeometry relative="1" as="geometry" />`; see `references/local/upstream-drawio-rules.md` |
| Diagram looks overlapped | Reduce primary components to 3-5; see `references/local/layout-safety.md` and `references/local/figure-grammars.md` |

## Where to go deeper

- `SKILL.md` at repo root - the full authoring workflow and validation checklist.
- `references/local/upstream-drawio-rules.md` - runtime XML and validation rules.
- `references/fetched/` - vendored upstream material for factual lookup only.
- `references/local/figure-grammars.md` - one-grammar-per-page rule and the five allowed grammars.
- `references/local/layout-safety.md` - overlap, routing, corridor preflight.
