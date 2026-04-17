# drawio-agent-skill

Native draw.io authoring guidance for coding agents.

This repo packages the `drawio-diagram` skill: a skill for producing editable `.drawio` files, not just one-off XML blobs or image mockups. It is for cases where the user wants a diagram that already has the right structure, routing, and page grammar, but still remains easy for a human to open and refine in draw.io Desktop or diagrams.net.

## Installation

Preferred:

```bash
npx skills add gigio1023/drawio-agent-skill@drawio-diagram
```

### Codex

Tell Codex:

```text
Fetch and follow instructions from https://raw.githubusercontent.com/gigio1023/drawio-agent-skill/refs/heads/main/.codex/INSTALL.md
```

Detailed docs: `docs/README.codex.md`

### Claude Code

Tell Claude Code:

```text
Fetch and follow instructions from https://raw.githubusercontent.com/gigio1023/drawio-agent-skill/refs/heads/main/.claude/INSTALL.md
```

Detailed docs: `docs/README.claude.md`

### Gemini CLI

Tell Gemini CLI:

```text
Fetch and follow instructions from https://raw.githubusercontent.com/gigio1023/drawio-agent-skill/refs/heads/main/.gemini/INSTALL.md
```

Detailed docs: `docs/README.gemini.md`

### Cursor

Tell Cursor:

```text
Fetch and follow instructions from https://raw.githubusercontent.com/gigio1023/drawio-agent-skill/refs/heads/main/.cursor/INSTALL.md
```

Detailed docs: `docs/README.cursor.md`

## Prerequisites

- **Authoring** `.drawio` source files needs nothing beyond the skill — it writes native mxGraphModel XML directly.
- **Export** (PNG / SVG / PDF) needs the draw.io CLI:

| Environment | CLI location |
|---|---|
| macOS | `/Applications/draw.io.app/Contents/MacOS/draw.io` |
| Linux (native) | `drawio` on PATH (snap / apt / flatpak) |
| Windows (native) | `"C:\Program Files\draw.io\draw.io.exe"` |
| WSL2 | `` `/mnt/c/Program Files/draw.io/draw.io.exe` `` (detect via `grep -qi microsoft /proc/version`) |
| Headless / CI | `npx --yes @hediet/drawio-export` (no prior install) |

The skill tries `drawio` on PATH first, then falls back to the platform-specific path. `SKILL.md` has the full locator logic.

## Export formats

The skill writes `.drawio` by default. If the draw.io CLI is installed, it can also export to PNG / SVG / PDF with the diagram XML embedded in the exported file, so any of them can be reopened in draw.io and edited further.

| Format | Extension | When to use |
|--------|-----------|-------------|
| (default) | `.drawio` | Native source of truth; always works, no CLI required |
| `png` | `.drawio.png` | Embedding in READMEs / chat — viewable anywhere |
| `svg` | `.drawio.svg` | Vector review, scales cleanly |
| `pdf` | `.drawio.pdf` | Printable handoffs |

Installing the skill itself is enough to author `.drawio` files. The draw.io CLI (bundled with [draw.io Desktop](https://github.com/jgraph/drawio-desktop/releases), or available through `npx --yes @hediet/drawio-export` on headless machines) is only needed when export is requested.

## What this skill improves

Generic diagram generation usually fails in one of three ways:

1. it produces non-native output like Mermaid or loose XML
2. it crams too many concepts onto one canvas without page grammar
3. it produces something that looks acceptable once, but is painful to edit later

`drawio-diagram` exists to bias the agent toward native draw.io structure, obvious routing, and diagrams that a human can keep editing after the first pass.

## Example: what generic output looks like

**Weak output**

- vague boxes with no clear page grammar
- arrows that share the same corridor and cross unpredictably
- no distinction between main path and secondary relationships
- output format that is not actually a usable `.drawio` source of truth

**What this skill pushes toward**

- one explicit grammar like `flow-canvas` or `system-map`
- 3-5 primary components on the first pass
- one dominant arrow path with quieter secondary paths
- native draw.io structure that can be reopened and revised cleanly

## What this skill is for

Use it when the task is any of these:

- architecture or system diagrams
- flowcharts with explicit component-to-component arrows
- research or editorial figures
- compact OpenAI / Anthropic / Vercel style explanatory visuals
- deliverables where the `.drawio` file itself matters, not only a PNG export

This skill is opinionated about a few things:

- native draw.io first: `.drawio` is the source of truth
- compact grammar before decoration: pick a page grammar before styling
- important arrows must be obvious: no hidden or accidental routing
- editability matters: do not optimize for clever XML that a human cannot maintain

## When not to use it

This repo is a bad fit when the user actually wants:

- Mermaid / PlantUML / ad-hoc SVG instead of draw.io
- a bitmap illustration rather than an editable diagram
- a huge many-to-many system map on one page with no simplification pass

In those cases, use a different diagram surface or split the figure across pages.

## How the skill works

The skill follows a consistent authoring loop:

1. understand the figure and the required components
2. choose one page grammar
3. lock a page budget before drawing
4. generate native draw.io structure
5. run layout and routing preflight checks
6. export PNG/SVG/PDF only if the environment supports it

The default first-pass grammars are documented in `references/figure-grammars.md`:

- `flow-canvas`
- `report-split`
- `system-map`
- `insight-panels`
- `annotated-chart-card`

The point is to keep the first pass compact and editable instead of cramming everything into a single noisy canvas.

## What's inside

### Skill entrypoint

- `SKILL.md` — the actual `drawio-diagram` skill definition and workflow

### References

Local originals:

- `references/upstream-drawio-rules.md` — tight opinionated digest of the rules this skill enforces (read first)
- `references/figure-grammars.md` — page grammars and composition rules
- `references/layout-safety.md` — overlap, routing, and corridor safety checks
- `references/visual-patterns.md` — compact visual behaviors distilled from strong reference material
- `references/reference-set.md` — provenance for the visual guidance
- `references/community-lessons.md` — practical lessons from community and adjacent diagram systems

Vendored from `jgraph/drawio-mcp` under Apache-2.0 (see [`NOTICE`](NOTICE) for the exact upstream commit and file mapping):

- `references/drawio-xml-reference.md` — authoritative XML rules: edge routing priorities, fan-out bundling, containers, layers, tags, metadata, placeholders, dark mode, well-formedness
- `references/drawio-style-reference.md` — comprehensive shape / style catalog

### Sample assets

- `assets/safe-layout-flow-canvas.drawio`
- `assets/safe-layout-routed-canvas.drawio`
- `assets/drawio-skill-template-pack.drawio`

### Reference refresh tooling

- `scripts/download_reference_set.py` — refreshes the curated official reference set
- `data/references/manifest.json` — manifest for the local reference archive

## Usage patterns

The skill is invoked by description-matching, not a slash command. Ask naturally and the skill activates on phrases like "draw.io", "flowchart", "architecture diagram", "ER diagram", "sequence diagram", "class diagram", or when a file extension is mentioned (`.drawio`, `.drawio.png`, etc.).

**Author `.drawio` only (default):**

```text
Make a draw.io architecture diagram for this ingestion pipeline.
Turn this research section into a compact editorial figure.
Generate a .drawio file with clear arrows between these four components.
```

**Author + export, via natural-language format hints:**

```text
Make a png architecture diagram for the deploy pipeline.      → deploy-pipeline.drawio + .drawio.png
Generate a .drawio.svg of the auth sequence.                   → auth-sequence.drawio + .drawio.svg
Compact pdf handoff for this system map.                       → <name>.drawio + .drawio.pdf
```

If no format is mentioned, the skill writes only the `.drawio` source; you can ask to export later. Export always carries the diagram XML embedded in the output (`-e` / `--embed-diagram`) so reopening the `.drawio.png` / `.drawio.svg` / `.drawio.pdf` in draw.io recovers the editable diagram.

**Deliberate divergence from the upstream skill-cli:** we keep the `.drawio` source alongside the export, rather than deleting it. Source of truth stays visible.

## Example prompts

- `Make a draw.io architecture diagram for this ingestion pipeline.`
- `Turn this research section into a compact editorial figure.`
- `Generate a .drawio file with clear arrows between these four components.`
- `Make this system map editable in draw.io, then export PNG if possible.`

## Inspiration and references

This repo vendors portions of the official [`jgraph/drawio-mcp`](https://github.com/jgraph/drawio-mcp) repository under **Apache-2.0**, and adapts ideas from its [`skill-cli/`](https://github.com/jgraph/drawio-mcp/tree/main/skill-cli) variant's README — the `.drawio.*` double-extension export convention, the explicit draw.io CLI prerequisite table, the "why native XML only?" rationale, the post-processing step via `npx @drawio/postprocess`, the export-flag semantics, the per-OS "open the result" commands, and the strict no-XML-comments rule. Those ideas are reflected in `SKILL.md` (see *Prerequisites*, *Export*, *XML well-formedness*, *Troubleshooting*) and in the vendored reference files.

- Upstream repo: https://github.com/jgraph/drawio-mcp
- Skill-CLI variant README: https://github.com/jgraph/drawio-mcp/blob/main/skill-cli/README.md
- Upstream `shared/xml-reference.md` (vendored locally): https://github.com/jgraph/drawio-mcp/blob/main/shared/xml-reference.md
- Upstream `shared/style-reference.md` (vendored locally): https://github.com/jgraph/drawio-mcp/blob/main/shared/style-reference.md
- Full attribution, upstream commit, and file mapping: [`NOTICE`](NOTICE)
- This repo's own license: [`LICENSE`](LICENSE) (MIT)

Where this repo differs from upstream in intent:

- Multi-harness focus (Claude Code, Codex, Gemini CLI, Cursor) instead of a single Claude Code target
- Page-grammar discipline (`references/figure-grammars.md`) as a required pre-authoring step
- Layout-safety preflight (`references/layout-safety.md`) separate from the XML rules
- `.drawio` source is retained after export (upstream skill-cli deletes it)

## Repo layout

```text
drawio-agent-skill/
├── SKILL.md                        # the drawio-diagram skill definition + authoring workflow
├── README.md                       # this file
├── LICENSE                         # MIT, this repo
├── NOTICE                          # Apache-2.0 attribution for vendored upstream content
├── docs/                           # per-harness install guides (Claude / Codex / Gemini / Cursor)
├── references/                     # authoring references (local + vendored Apache-2.0 upstream)
├── assets/                         # editable .drawio starter templates
├── scripts/                        # download_reference_set.py for refreshing external references
└── data/                           # references archive + manifest
```
