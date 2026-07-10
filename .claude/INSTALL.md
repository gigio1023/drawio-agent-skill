# Install drawio-diagram for Claude Code

## Preferred

```bash
npx skills add gigio1023/drawio-agent-skill@drawio-diagram --agent claude-code
```

## Manual install

```bash
git clone https://github.com/gigio1023/drawio-agent-skill.git ~/.claude/drawio-agent-skill
mkdir -p ~/.claude/skills
ln -s ~/.claude/drawio-agent-skill ~/.claude/skills/drawio-diagram
```

Claude Code normally detects `SKILL.md` changes live. Restart only if the new
top-level skills directory was created after the session started or the skill
does not appear.
