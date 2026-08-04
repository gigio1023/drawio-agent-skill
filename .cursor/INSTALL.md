# Install these skills for Cursor

## Preferred

```bash
npx skills add gigio1023/drawio-agent-skill@drawio-diagram --agent cursor
npx skills add gigio1023/drawio-agent-skill@editorial-chart --agent cursor
```

Install only the skills you want; each command is independent.

## Manual install

```bash
git clone https://github.com/gigio1023/drawio-agent-skill.git ~/.cursor/drawio-agent-skill
mkdir -p ~/.cursor/skills/drawio-diagram ~/.cursor/skills/editorial-chart
cp -R ~/.cursor/drawio-agent-skill/skills/drawio-diagram/. ~/.cursor/skills/drawio-diagram/
cp -R ~/.cursor/drawio-agent-skill/skills/editorial-chart/. ~/.cursor/skills/editorial-chart/
```

Restart Cursor after copying.
