# Install these skills for Cursor

## Preferred

```bash
npx skills add gigio1023/gigio-figures@drawio-diagram --agent cursor
npx skills add gigio1023/gigio-figures@data-chart --agent cursor
```

Install only the skills you want; each command is independent.

## Manual install

```bash
git clone https://github.com/gigio1023/gigio-figures.git ~/.cursor/gigio-figures
mkdir -p ~/.cursor/skills/drawio-diagram ~/.cursor/skills/data-chart
cp -R ~/.cursor/gigio-figures/skills/drawio-diagram/. ~/.cursor/skills/drawio-diagram/
cp -R ~/.cursor/gigio-figures/skills/data-chart/. ~/.cursor/skills/data-chart/
```

Restart Cursor after copying.
