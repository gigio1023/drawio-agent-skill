# Install these skills for Claude Code

## Preferred

```bash
npx skills add gigio1023/drawio-agent-skill@drawio-diagram --agent claude-code
npx skills add gigio1023/drawio-agent-skill@editorial-chart --agent claude-code
```

Install only the skills you want; each command is independent.

## Manual install

```bash
git clone https://github.com/gigio1023/drawio-agent-skill.git ~/.claude/drawio-agent-skill
mkdir -p ~/.claude/skills
ln -s ~/.claude/drawio-agent-skill/skills/drawio-diagram ~/.claude/skills/drawio-diagram
ln -s ~/.claude/drawio-agent-skill/skills/editorial-chart ~/.claude/skills/editorial-chart
```

Claude Code normally detects `SKILL.md` changes live. Restart only if the new
top-level skills directory was created after the session started or a skill
does not appear.
