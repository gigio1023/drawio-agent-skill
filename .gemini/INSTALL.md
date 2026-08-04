# Install these skills for Gemini CLI

## Preferred

```bash
npx skills add gigio1023/drawio-agent-skill@drawio-diagram --agent gemini-cli
npx skills add gigio1023/drawio-agent-skill@editorial-chart --agent gemini-cli
```

Install only the skills you want; each command is independent.

## Manual install

```bash
git clone https://github.com/gigio1023/drawio-agent-skill.git ~/.gemini/drawio-agent-skill
mkdir -p ~/.gemini/skills/drawio-diagram ~/.gemini/skills/editorial-chart
cp -R ~/.gemini/drawio-agent-skill/skills/drawio-diagram/. ~/.gemini/skills/drawio-diagram/
cp -R ~/.gemini/drawio-agent-skill/skills/editorial-chart/. ~/.gemini/skills/editorial-chart/
```

Restart Gemini CLI after copying.
