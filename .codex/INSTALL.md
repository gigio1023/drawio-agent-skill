# Install these skills for Codex

## Preferred

```bash
npx skills add gigio1023/drawio-agent-skill@drawio-diagram --agent codex
npx skills add gigio1023/drawio-agent-skill@editorial-chart --agent codex
```

Install only the skills you want; each command is independent.

## Manual install

1. Clone the repo:

```bash
mkdir -p ~/.local/share
git clone https://github.com/gigio1023/drawio-agent-skill.git ~/.local/share/drawio-agent-skill
```

2. Symlink each skill directory into the Codex skill directory:

```bash
mkdir -p ~/.agents/skills
ln -s ~/.local/share/drawio-agent-skill/skills/drawio-diagram ~/.agents/skills/drawio-diagram
ln -s ~/.local/share/drawio-agent-skill/skills/editorial-chart ~/.agents/skills/editorial-chart
```

3. Restart Codex.
