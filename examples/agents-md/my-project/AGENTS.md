<!-- BEGIN:ai-rules - filled by scripts/deploy_rules.py from .ai-rules.md, do not edit between the markers -->
> ⚠️ **TEMPLATE - ACTION REQUIRED:** Replace this block with the full content of the master
> file `.ai-rules.md` (repository root of Requirements-Engineering-Agentic-AI).
> Do not edit the rules here. Change them in `.ai-rules.md` and re-deploy.
<!-- END:ai-rules -->

# Project Context

AGENTS.md has no import syntax. Read these files when relevant to the task:

- Product vision: `docs/product.md`
- Project structure: `docs/structure.md`
- Tech stack, build and test commands: `docs/tech.md`

# Working with feature specs

Features are cut into one folder each: `specs/<feature-name>/` (`requirements.md`, `design.md`, `tasks.md`).

- Work on exactly one feature folder at a time. Do not read or modify other features.
- Read `requirements.md`, then `design.md`, then `tasks.md`.
- Implement one task at a time, in the order of the dependency graph (waves) at the end of `tasks.md`.
- Tick the checkbox of each finished task and keep the `← design.md §x, requirements §y` references intact.
- Log decisions, blockers and progress in the context history file (see `.ai-rules.md`, section "Context History").
