# drawio-agent-skill

Native draw.io authoring guidance for coding agents.

This repo packages the `drawio-diagram` skill. Its job is not just to produce valid XML, but to produce native `.drawio` files that stay readable, editable, and structurally intact under review.

## Install

Install through the Skills CLI. The `--agent` value selects the target
harness; manual paths and restart behavior stay in the corresponding install
guide.

| Target | Install | Manual guide |
| --- | --- | --- |
| Claude Code | `npx skills add gigio1023/drawio-agent-skill@drawio-diagram --agent claude-code` | [Claude Code](.claude/INSTALL.md) |
| Codex | `npx skills add gigio1023/drawio-agent-skill@drawio-diagram --agent codex` | [Codex](.codex/INSTALL.md) |
| Cursor | `npx skills add gigio1023/drawio-agent-skill@drawio-diagram --agent cursor` | [Cursor](.cursor/INSTALL.md) |
| Gemini CLI | `npx skills add gigio1023/drawio-agent-skill@drawio-diagram --agent gemini-cli` | [Gemini CLI](.gemini/INSTALL.md) |

## Usage

Ask naturally for a native draw.io artifact. Claude Code can invoke the skill
explicitly as `/drawio-diagram`; Codex uses `$drawio-diagram`. Explicit syntax
is optional when the request clearly asks for draw.io output.

```text
Make a draw.io architecture diagram for this ingestion pipeline.
Generate a .drawio.svg of the deploy pipeline with clear fan-out edges.
Turn this research section into a compact editorial figure in draw.io.
```

## What changed in this repo

This skill now has four explicit layers:

1. fetched upstream copies (committed digests)
2. optional local clones of official docs and examples (gitignored)
3. local overlay
4. deterministic validators

The fetched upstream layer keeps verbatim `jgraph/drawio-mcp` content inside
this repo at stable local paths for provenance and technical lookup. It is not
loaded wholesale as agent policy: the local overlay controls workflow, layout
judgment, and verification. The validators turn repeated visual bugs into
checks the agent can run before claiming success.

## Fetched upstream copies

Fetched files live under:

```text
references/fetched/
```

Included today:

- `xml-reference.md`
- `style-reference.md`
- `mermaid-reference.md`
- `mxfile.xsd`
- `skill-cli-README.md`
- `skill-cli-drawio-SKILL.md`

Refresh them with:

```bash
python3 scripts/vendor_jgraph_drawio_mcp.py
```

The resolved commit and fetch timestamp are recorded in:

```text
references/fetched/vendor-manifest.json
```

The local repo layout does not mirror the upstream folder tree. The fetch script copies upstream files into stable local filenames, so local references do not churn just because the upstream directory layout changes.

## Local overlay

Local guidance lives under:

```text
references/local/
```

Key files:

- `editorial-default-style.md` - the default visual style (measured from
  post-2025 openai.com editorial figures); applies whenever the user names no
  style, seeded by `assets/editorial-default-template.drawio`
- `upstream-drawio-rules.md` - local digest of the structural rules that always apply
- `edge-routing.md` - connection contract, fixed vs floating terminals, waypoint
  recipes, and why draw.io never routes around other shapes
- `text-and-labels.md` - line breaks (`\n` renders literally), escaping, label
  positioning, and detail-vs-compact representation levels
- `color-palettes.md` - alternative palettes used on request (draw.io standard
  pairs and an indigo report scheme) plus dark-mode rules; the default palette
  lives in `editorial-default-style.md`
- `figure-grammars.md` - one-grammar-per-page layout discipline
- `layout-safety.md` - overlap, padding, and corridor checks
- `quality-gates.md` - hard finishing gates for meaning, layout, text, arrows, and corner consistency
- `real-world-gotchas.md` - repeated failure modes from real sessions
- `review-loop.md` - exported-artifact QA, arrow-corridor audit, and SVG/PNG review guidance
- `visual-patterns.md` - compact visual behaviors from selected official references
- `upstream-docs-map.md` - map of the official docs/example clones and what the
  official diagrams actually do with edges
- `reference-set.md` - provenance for those references
- `community-lessons.md` - lessons from adjacent ecosystems

## Official docs and examples (optional local clones)

For deep lookup beyond the vendored digests, clone the official sources into
`references/upstream/` (gitignored, never committed):

```bash
bash scripts/fetch_upstream_docs.sh                    # drawio-mcp + drawio-diagrams (~30MB)
bash scripts/fetch_upstream_docs.sh --with-mxgraph     # + archived mxGraph docs
bash scripts/fetch_upstream_docs.sh --with-app-templates  # + app templates (CC BY 4.0)
```

`references/local/upstream-docs-map.md` maps questions to locations in the
clones and lists the equivalent online URLs when clones are absent.

## Validators

Two validators now ship with the skill:

```bash
python3 scripts/validate_drawio_xml.py path/to/file.drawio
python3 scripts/validate_drawio_layout.py path/to/file.drawio
python3 -m unittest discover -s scripts -p 'test_*.py'
```

What they catch:

- broken root structure
- duplicate ids
- missing edge geometry
- missing `html=1`
- XML comments
- framed component overlap
- child overflow from parent containers
- border-hugging text risk
- inconsistent rounded-rectangle settings
- dangling edges (no source/target and no explicit end point)
- edge routes that likely cross unrelated components
- fixed connection points facing away from the other terminal
- floating edge pairs between the same two shapes (they render overlapped)
- edge labels without an opaque background
- one/two-waypoint doglegs between aligned terminals when the direct corridor is clear

They are not a replacement for opening the diagram, but they close the gap between "XML is valid" and "diagram is still broken."

For review handoffs, the skill now also points agents to inspect the exported SVG
or normalized high-resolution PNG. That catches visual issues validators cannot
see, especially arrows crossing labels or components.

## Export behavior

The skill writes `.drawio` by default.

If the draw.io CLI is available, it can also export:

- `.drawio.png`
- `.drawio.svg`
- `.drawio.pdf`

Unlike upstream `skill-cli`, this repo keeps the `.drawio` source after export. The exported file may contain embedded XML, but the standalone source file remains the easiest thing for a human to edit and diff.

For 4K review PNGs:

```bash
drawio -x -f png -e -b 10 --width 3840 -o diagram.drawio.png diagram.drawio
```

Prefer SVG when text crispness matters more than bitmap convenience.

## Troubleshooting

| Problem | Fix |
| --- | --- |
| draw.io CLI not found | Install draw.io Desktop or use `npx --yes @hediet/drawio-export`; source-only `.drawio` authoring needs no exporter. |
| Export is blank or edges are missing | Every edge needs `<mxGeometry relative="1" as="geometry" />`; see `references/local/upstream-drawio-rules.md`. |
| Layout is crowded or overlapping | Reduce the first-pass component count and reopen corridors; see `references/local/figure-grammars.md` and `references/local/layout-safety.md`. |
| Edges cross unrelated boxes | Pin connection sides and add corridor waypoints; see `references/local/edge-routing.md`. |
| `\n` appears as literal text | Use `&lt;br&gt;` or `&#xa;` in the value attribute; see `references/local/text-and-labels.md`. |

## Why this skill exists

Generic diagram generation usually fails in one of these ways:

1. the XML is technically valid but visually broken
2. the page mixes different hierarchy levels into one component
3. labels are too long, too vague, or too close to borders
4. arrows are routed without ownership of the corridor
5. the first exported image is usable once but painful to edit later

This skill exists to bias the agent toward native draw.io structure, compact page grammar, explicit quality gates, and files that stay editable after the first pass.

## Repo layout

- `SKILL.md`
- `README.md`
- `NOTICE`
- `assets/`
- `data/`
- `references/local/`
- `references/fetched/`
- `references/upstream/` (gitignored; created by `scripts/fetch_upstream_docs.sh`)
- `scripts/`

## Attribution

This repo vendors upstream files from `jgraph/drawio-mcp` under Apache-2.0 and layers local guidance on top. Exact file mapping and the current vendored commit are recorded in [`NOTICE`](NOTICE).
