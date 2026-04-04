# drawio-agent-skill

Native draw.io authoring guidance for coding agents.

This repo packages the `drawio-diagram` skill: a skill for producing editable `.drawio` files, not just one-off XML blobs or image mockups. It is for cases where the user wants a diagram that already has the right structure, routing, and page grammar, but still remains easy for a human to open and refine in draw.io Desktop or diagrams.net.

## Installation

Installation differs a little by platform, but the recommended path is the same: use the skills ecosystem first, and copy files manually only when you need a direct local install.

### Skills CLI

```bash
npx skills add gigio1023/drawio-agent-skill@drawio-diagram
npx skills add gigio1023/drawio-agent-skill@drawio-diagram -g
```

### Claude Code

```bash
mkdir -p ~/.claude/skills/drawio-diagram && \
  git clone https://github.com/gigio1023/drawio-agent-skill.git /tmp/drawio-agent-skill && \
  cp -R /tmp/drawio-agent-skill/. ~/.claude/skills/drawio-diagram/ && \
  rm -rf /tmp/drawio-agent-skill
```

### Codex CLI

```bash
mkdir -p ~/.codex/skills/drawio-diagram && \
  git clone https://github.com/gigio1023/drawio-agent-skill.git /tmp/drawio-agent-skill && \
  cp -R /tmp/drawio-agent-skill/. ~/.codex/skills/drawio-diagram/ && \
  rm -rf /tmp/drawio-agent-skill
```

### Other skills-compatible agents

```bash
mkdir -p ~/.agents/skills/drawio-diagram && \
  git clone https://github.com/gigio1023/drawio-agent-skill.git /tmp/drawio-agent-skill && \
  cp -R /tmp/drawio-agent-skill/. ~/.agents/skills/drawio-diagram/ && \
  rm -rf /tmp/drawio-agent-skill
```

### Verify installation

Start a fresh session and ask for something that clearly needs a real draw.io deliverable.

For example:

- `Create a draw.io architecture diagram for this ingestion system.`
- `Turn this research figure into an editable .drawio file.`
- `Make a compact system map and export PNG if possible.`

If the install worked, the agent should treat `.drawio` as the source of truth instead of drifting toward Mermaid, generic XML, or image-only output.

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

- `references/upstream-drawio-rules.md` — required draw.io structure and export notes
- `references/figure-grammars.md` — page grammars and composition rules
- `references/layout-safety.md` — overlap, routing, and corridor safety checks
- `references/visual-patterns.md` — compact visual behaviors distilled from strong reference material
- `references/reference-set.md` — provenance for the visual guidance
- `references/community-lessons.md` — practical lessons from community and adjacent diagram systems

### Sample assets

- `assets/safe-layout-flow-canvas.drawio`
- `assets/safe-layout-routed-canvas.drawio`
- `assets/drawio-skill-template-pack.drawio`

These are editable starters, not rigid templates.

### Reference refresh tooling

- `scripts/download_reference_set.py` — refreshes the curated official reference set
- `data/references/manifest.json` — manifest for the local reference archive

## Example prompts

- `Make a draw.io architecture diagram for this ingestion pipeline.`
- `Turn this research section into a compact editorial figure.`
- `Generate a .drawio file with clear arrows between these four components.`
- `Make this system map editable in draw.io, then export PNG if possible.`

## Repo layout

```text
drawio-agent-skill/
├── SKILL.md
├── README.md
├── references/
│   ├── upstream-drawio-rules.md
│   ├── figure-grammars.md
│   ├── layout-safety.md
│   ├── visual-patterns.md
│   ├── reference-set.md
│   └── community-lessons.md
├── assets/
│   ├── safe-layout-flow-canvas.drawio
│   ├── safe-layout-routed-canvas.drawio
│   └── drawio-skill-template-pack.drawio
├── scripts/
│   └── download_reference_set.py
└── data/
    └── references/
        └── manifest.json
```

## Practical notes

- If a connection matters, make it explicit with a visible component-to-component arrow.
- If a page starts requiring too many branches, split it before styling it.
- If the environment cannot export, the `.drawio` file is still a valid finished deliverable.
