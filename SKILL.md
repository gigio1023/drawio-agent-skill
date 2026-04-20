---
name: drawio-diagram
description: >
  Create native draw.io diagrams as editable .drawio files with strong layout,
  readable arrows, and explicit quality checks. Use when the user asks for
  draw.io, .drawio files, architecture diagrams, flowcharts, editorial figures,
  component-to-component arrows, or export to PNG/SVG/PDF. Prefer this over
  ad-hoc XML when editability, routing clarity, and human revision quality
  matter.
---

# Draw.io Diagram

## Quick start

Use this skill when the goal is not just "generate diagram XML", but "author a native `.drawio` file that opens cleanly in draw.io and does not fall apart under review."

Default path:

1. Read `references/local/upstream-drawio-rules.md`
2. Choose one grammar from `references/local/figure-grammars.md`
3. If the request is dense or polish-sensitive, also read:
   - `references/local/quality-gates.md`
   - `references/local/real-world-gotchas.md`
4. Generate native draw.io XML with real draw.io structure
5. Validate the result:
   - `python scripts/validate_drawio_xml.py <file>.drawio`
   - `python scripts/validate_drawio_layout.py <file>.drawio`
6. Export only if the user asked for PNG / SVG / PDF and the draw.io CLI is available

## Runtime defaults

- Native `.drawio` is the source of truth
- XML is the default authoring format, not Mermaid or CSV
- Export is optional
- Upstream `jgraph/drawio-mcp` files are fetched into stable local files in this repo and should be treated as the canonical long-form reference set

## Reference files

### Local overlay

| File | When to read | Purpose |
|---|---|---|
| `references/local/upstream-drawio-rules.md` | Always first | Tight local digest of structural rules and validation expectations |
| `references/local/figure-grammars.md` | Before layout | One-grammar-per-page rule and page-budget guidance |
| `references/local/layout-safety.md` | Before finishing | Overlap, padding, routing, and readability checks |
| `references/local/quality-gates.md` | When quality matters | Hard finishing gates for meaning, layout, text, arrows, and shape consistency |
| `references/local/real-world-gotchas.md` | When diagrams keep breaking in review | Repeated failure modes from real sessions |
| `references/local/visual-patterns.md` | When compact editorial polish matters | Layout behaviors distilled from strong official references |
| `references/local/reference-set.md` | When you need provenance | Which official references informed the local visual guidance |
| `references/local/community-lessons.md` | When evolving the skill | Lessons from adjacent draw.io and diagram ecosystems |

### Fetched upstream copies

| File | When to read | Purpose |
|---|---|---|
| `references/fetched/xml-reference.md` | When XML depth is needed | Canonical upstream XML generation rules |
| `references/fetched/style-reference.md` | When a style or shape needs verification | Canonical upstream style and shape catalog |
| `references/fetched/mxfile.xsd` | When validating schema-level structure | Upstream schema file |
| `references/fetched/mermaid-reference.md` | Only when the user explicitly asks for Mermaid | Upstream Mermaid import reference for draw.io |
| `references/fetched/skill-cli-README.md` | When checking upstream CLI behavior | Current upstream skill-cli README |
| `references/fetched/skill-cli-drawio-SKILL.md` | When checking upstream skill wording | Current upstream skill-cli skill file |

## Workflow

### 1. Understand the diagram

Extract:

- what the diagram must communicate
- which components must appear
- which arrows are required
- whether the output must stay compact on one page
- whether the user wants `.drawio` only or also an export artifact

Do not collapse different levels into one box. Separate:

- external callers
- main container
- internal sections
- implementation choices
- external dependencies

### 2. Choose one grammar only

Read `references/local/figure-grammars.md`.

Default to `flow-canvas` if unsure.

Do not mix grammars on the first pass.

### 3. Lock a page budget

Default limits:

- 3-5 primary framed components
- 1 dominant path
- 0-2 secondary paths
- 1 side rail max
- 1 bottom strip max

If the request exceeds this, split across multiple pages instead of forcing density.

### 4. Generate native draw.io structure

Required structure:

- `mxfile > diagram > mxGraphModel`
- root cells `0` and `1`
- `adaptiveColors="auto"`
- every edge has child `<mxGeometry relative="1" as="geometry" />`
- all cell styles end with `html=1;`
- no XML comments

Use draw.io primitives directly:

- `swimlane` for titled panels
- `group;` for invisible grouping
- `container=1;pointerEvents=0;` for decorative containers
- `object` / `UserObject` when metadata or placeholders improve editability

### 5. Label with restraint

- Prefer one or two lines per component
- Avoid paragraphs inside boxes
- Do not use vertical text for main labels
- If a label is ambiguous, rename it instead of decorating it
- If a term may be narrower than the real protocol meaning, choose the safer broader term

Examples:

- prefer `response` unless `artifact` is definitely correct
- prefer `Agent logic` or another ownership-specific label over vague labels like `Your logic`
- do not mix implementation choice and external tools under one title

### 6. Route arrows on purpose

- Make the main path visually dominant
- Keep secondary paths quieter
- Put edge labels on straight segments, not bends
- Straighten request/response pairs when alignment makes that possible
- If two edges want the same corridor, add explicit waypoints
- Do not let arrows sit on top of dense text regions

### 7. Keep the file editable

- Include all intended components
- Keep labels explicit
- Prefer conservative boxes over clever geometry
- Keep `.drawio` after export

This skill deliberately diverges from upstream `skill-cli`, which deletes the intermediate `.drawio` after export. Here the `.drawio` source stays visible as the round-trippable authoring file.

## Quality pass

Before finishing, read:

- `references/local/layout-safety.md`
- `references/local/quality-gates.md`
- `references/local/real-world-gotchas.md`

Then run:

```bash
python scripts/validate_drawio_xml.py <path>.drawio
python scripts/validate_drawio_layout.py <path>.drawio
```

Do not claim the diagram is done without passing the XML validator. If the layout validator warns about overlap, border-hugging text, or inconsistent corners, fix the diagram unless there is a clear reason not to.

## Exports

### draw.io CLI locations

Try `which drawio` first. If not found, use the platform-specific fallback.

| Environment | CLI location | Detection hint |
|---|---|---|
| macOS | `/Applications/draw.io.app/Contents/MacOS/draw.io` | draw.io Desktop app bundle |
| Linux | `drawio` on PATH | native package |
| Windows | `C:\Program Files\draw.io\draw.io.exe` | default installer path |
| WSL2 | `` `/mnt/c/Program Files/draw.io/draw.io.exe` `` | use `wslpath -w` for open commands |
| Headless / CI | `npx --yes @hediet/drawio-export` | export-only fallback |

### Post-process routing

If `npx @drawio/postprocess` is available, run it after writing the `.drawio` file:

```bash
npx @drawio/postprocess <path>.drawio
```

Skip silently if unavailable.

### Export commands

Default export:

```bash
drawio -x -f <format> -e -b 10 -o <output> <input.drawio>
```

High-resolution PNG for 4K review:

```bash
drawio -x -f png -e -b 10 --width 3840 -o <output>.drawio.png <input>.drawio
```

WSL2 example:

```bash
`/mnt/c/Program Files/draw.io/draw.io.exe` -x -f png -e -b 10 --width 3840 -o diagram.drawio.png diagram.drawio
```

Use SVG when text sharpness matters more than README convenience.

### Open the result

| Environment | Command |
|---|---|
| macOS | `open <file>` |
| Linux | `xdg-open <file>` |
| WSL2 | `cmd.exe /c start \"\" \"$(wslpath -w <file>)\"` |
| Windows | `start <file>` |

## Troubleshooting

| Problem | Likely cause | Fix |
|---|---|---|
| Diagram renders blank | Structural XML issue | Run `python scripts/validate_drawio_xml.py` |
| Edge missing | Edge lacks child `mxGeometry` | Add `<mxGeometry relative="1" as="geometry" />` |
| Components overlap | Page budget too dense or no corridor planning | Reduce components, change grammar, or reroute |
| Text touches border | Too little spacing or overlong label | Shorten text, then add spacing, then resize |
| Rounded boxes feel inconsistent | Mixed corner settings | Normalize to `rounded=1;absoluteArcSize=1;arcSize=12;` |
| Box title is ambiguous | Mixed hierarchy in one component | Split implementation choices from external tools |
| PNG is fuzzy on large displays | Low export size | Use SVG or PNG with `--width 3840` |

## File naming

- Source: `<name>.drawio`
- Exports: `<name>.drawio.png`, `<name>.drawio.svg`, `<name>.drawio.pdf`
- Use lowercase, hyphen-separated, content-descriptive names
