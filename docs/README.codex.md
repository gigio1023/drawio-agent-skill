# drawio-diagram for Codex

Native `.drawio` authoring for Codex CLI. The Codex harness loads the skill via AGENTS.md integration.

## Install

Preferred:

```bash
npx skills add gigio1023/drawio-agent-skill@drawio-diagram --agent codex
```

Or tell Codex:

```text
Fetch and follow instructions from https://raw.githubusercontent.com/gigio1023/drawio-agent-skill/refs/heads/main/.codex/INSTALL.md
```

Manual install is documented in `.codex/INSTALL.md`.

## Prerequisites

- Authoring: none beyond the skill itself.
- Export (PNG / SVG / PDF): draw.io CLI.
  - macOS: `/Applications/draw.io.app/Contents/MacOS/draw.io`
  - Linux: `drawio` on PATH
  - WSL2: `` `/mnt/c/Program Files/draw.io/draw.io.exe` ``
  - Headless / CI: `npx --yes @hediet/drawio-export`

## Usage

Ask Codex naturally. Include a format word (`png`, `svg`, `pdf`) when you want an exported artifact alongside the `.drawio` source.

```text
codex "Make a draw.io architecture diagram for this ingestion pipeline."
codex "Generate a .drawio.svg of the deploy pipeline with clear fan-out edges."
codex "Compact editorial figure in draw.io for the findings section."
```

## Output

- Default: `.drawio` source only.
- With format hint: `.drawio` + `.drawio.{png|svg|pdf}` (source preserved, diverging from upstream skill-cli which deletes it).

## Troubleshooting

| Problem | Fix |
|---------|-----|
| CLI not found | Install draw.io Desktop or use `npx @hediet/drawio-export` |
| Edges don't render | Each edge needs `<mxGeometry relative="1" as="geometry" />` — see `references/drawio-xml-reference.md` |
| Crowded layout | Cap first pass at 3–5 primary components; see `references/figure-grammars.md` and `references/layout-safety.md` |

## Deeper references

- `SKILL.md` — authoring workflow.
- `references/drawio-xml-reference.md` — vendored upstream XML reference (Apache-2.0).
- `references/drawio-style-reference.md` — vendored upstream style/shape catalog.
