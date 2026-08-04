# Install these skills for Claude Code

## Preferred

```bash
npx skills add gigio1023/gigio-figures@drawio-diagram --agent claude-code
npx skills add gigio1023/gigio-figures@data-chart --agent claude-code
```

Install only the skills you want; each command is independent.

## Manual install

```bash
git clone https://github.com/gigio1023/gigio-figures.git ~/.claude/gigio-figures
mkdir -p ~/.claude/skills
ln -s ~/.claude/gigio-figures/skills/drawio-diagram ~/.claude/skills/drawio-diagram
ln -s ~/.claude/gigio-figures/skills/data-chart ~/.claude/skills/data-chart
```

Claude Code normally detects `SKILL.md` changes live. Restart only if the new
top-level skills directory was created after the session started or a skill
does not appear.
