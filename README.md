# drawio-agent-skill

Native draw.io authoring guidance for coding agents.

This repo packages the `drawio-diagram` skill. Its job is not just to produce valid XML, but to produce native `.drawio` files that stay readable, editable, and structurally intact under review.

## Install

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

## What changed in this repo

This skill now has three explicit layers:

1. fetched upstream copies
2. local overlay
3. deterministic validators

The fetched upstream layer keeps canonical `jgraph/drawio-mcp` content inside this repo at stable local paths. The local overlay adds the opinionated rules that emerged from real diagram failures. The validators turn repeated visual bugs into checks the agent can run before claiming success.

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
python scripts/vendor_jgraph_drawio_mcp.py
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

- `upstream-drawio-rules.md` - local digest of the structural rules that always apply
- `figure-grammars.md` - one-grammar-per-page layout discipline
- `layout-safety.md` - overlap, padding, and corridor checks
- `quality-gates.md` - hard finishing gates for meaning, layout, text, arrows, and corner consistency
- `real-world-gotchas.md` - repeated failure modes from real sessions
- `visual-patterns.md` - compact visual behaviors from selected official references
- `reference-set.md` - provenance for those references
- `community-lessons.md` - lessons from adjacent ecosystems

## Validators

Two validators now ship with the skill:

```bash
python scripts/validate_drawio_xml.py path/to/file.drawio
python scripts/validate_drawio_layout.py path/to/file.drawio
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

They are not a replacement for opening the diagram, but they close the gap between "XML is valid" and "diagram is still broken."

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
- `docs/`
- `assets/`
- `data/`
- `references/local/`
- `references/fetched/`
- `scripts/`

## Attribution

This repo vendors upstream files from `jgraph/drawio-mcp` under Apache-2.0 and layers local guidance on top. Exact file mapping and the current vendored commit are recorded in [`NOTICE`](NOTICE).
