# drawio-diagram for Gemini CLI

Native `.drawio` authoring for Gemini CLI.

## Install

Preferred:

```bash
npx skills add gigio1023/drawio-agent-skill@drawio-diagram --agent gemini-cli
```

Or tell Gemini CLI:

```text
Fetch and follow instructions from https://raw.githubusercontent.com/gigio1023/drawio-agent-skill/refs/heads/main/.gemini/INSTALL.md
```

Manual installation is documented in `.gemini/INSTALL.md`.

## Prerequisites

- Authoring: none beyond the skill.
- Export: draw.io CLI (draw.io Desktop or `npx @hediet/drawio-export`). See per-OS paths in `SKILL.md`.

## Usage

Gemini CLI picks up the skill via activation. Ask naturally and include a format word to export.

```text
Create a draw.io flowchart for the auth sequence.
Generate a .drawio.png architecture diagram for the payment service.
Turn this analysis into a compact draw.io insight panel.
```

## Output

- Default: `.drawio` source only.
- With format hint: `.drawio` + `.drawio.{png|svg|pdf}` (source preserved).

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Missing CLI | Install draw.io Desktop or use `npx @hediet/drawio-export` |
| XML validates but renders blank | Missing root cells `id="0"` / `id="1"`; see `references/drawio-xml-reference.md` |
| Edges go through unrelated boxes | Add waypoints; see the orthogonal routing rules in `references/drawio-xml-reference.md` |

## Deeper references

- `SKILL.md` — authoring workflow.
- `references/drawio-xml-reference.md` — vendored upstream XML reference (Apache-2.0).
- `references/drawio-style-reference.md` — vendored upstream style/shape catalog.
