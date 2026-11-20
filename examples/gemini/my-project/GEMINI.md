<!-- BEGIN:ai-rules - filled by scripts/deploy_rules.py from .ai-rules.md, do not edit between the markers -->
> ⚠️ **TEMPLATE - ACTION REQUIRED:** Replace this block with the full content of the master
> file `.ai-rules.md` (repository root of Requirements-Engineering-Agentic-AI).
> Alternative: copy `.ai-rules.md` next to this file and replace this block with the single line `@./.ai-rules.md`.
> Do not edit the rules here. Change them in `.ai-rules.md` and re-deploy.
<!-- END:ai-rules -->

# Project Context

@./docs/product.md
@./docs/structure.md
@./docs/tech.md

# Specs

Features are cut into one folder each: `specs/<feature-name>/`. Every feature folder has its own
`GEMINI.md`, which Gemini CLI loads on demand when it works inside that folder.
