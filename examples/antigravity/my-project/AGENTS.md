<!-- BEGIN:ai-rules - filled by scripts/deploy_rules.py from .ai-rules.md, do not edit between the markers -->
> ⚠️ **TEMPLATE - ACTION REQUIRED:** Replace this block with the full content of the master
> file `.ai-rules.md` (repository root of Requirements-Engineering-Agentic-AI).
> Do not edit the rules here. Change them in `.ai-rules.md` and re-deploy.
> Limit: Antigravity truncates a rule file at 24,000 bytes. If the file grows beyond that,
> move narrow parts into `.agents/rules/*.md` with `trigger: model_decision` or `trigger: glob`.
<!-- END:ai-rules -->

# Project Context

@[Product](docs/product.md)
@[Structure](docs/structure.md)
@[Tech Stack](docs/tech.md)

# Specs

Features are cut into one folder each: `specs/<feature-name>/`.
The rule `.agents/rules/specs-workflow.md` and the skill `.agents/skills/implement-spec-task/` describe how to work with them.
