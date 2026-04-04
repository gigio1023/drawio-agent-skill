# Install drawio-diagram for Gemini CLI

## Preferred

```bash
npx skills add gigio1023/drawio-agent-skill@drawio-diagram --agent gemini-cli
```

## Manual install

```bash
git clone https://github.com/gigio1023/drawio-agent-skill.git ~/.gemini/drawio-agent-skill
mkdir -p ~/.gemini/skills/drawio-diagram
cp -R ~/.gemini/drawio-agent-skill/. ~/.gemini/skills/drawio-diagram/
```

Restart Gemini CLI after copying.
