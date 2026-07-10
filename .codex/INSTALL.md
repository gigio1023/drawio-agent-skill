# Install drawio-diagram for Codex

## Preferred

```bash
npx skills add gigio1023/drawio-agent-skill@drawio-diagram --agent codex
```

## Manual install

1. Clone the repo:

```bash
mkdir -p ~/.local/share
git clone https://github.com/gigio1023/drawio-agent-skill.git ~/.local/share/drawio-agent-skill
```

2. Symlink the installable repo root into the Codex skill directory:

```bash
mkdir -p ~/.agents/skills
ln -s ~/.local/share/drawio-agent-skill ~/.agents/skills/drawio-diagram
```

3. Restart Codex.
