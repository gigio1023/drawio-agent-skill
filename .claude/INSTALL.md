# Install drawio-diagram for Claude Code

## Preferred

```bash
npx skills add gigio1023/drawio-agent-skill@drawio-diagram --agent claude-code
```

## Manual install

```bash
git clone https://github.com/gigio1023/drawio-agent-skill.git ~/.claude/drawio-agent-skill
mkdir -p ~/.claude/skills/drawio-diagram
cp -R ~/.claude/drawio-agent-skill/. ~/.claude/skills/drawio-diagram/
```

Restart Claude Code after copying.
