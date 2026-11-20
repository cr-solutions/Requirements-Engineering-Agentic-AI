<!-- BEGIN:ai-rules - filled by scripts/deploy_rules.py from .ai-rules.md, do not edit between the markers -->
> ⚠️ **TEMPLATE - ACTION REQUIRED:** Replace this block with the full content of the master
> file `.ai-rules.md` (repository root of Requirements-Engineering-Agentic-AI).
> Alternative: copy `.ai-rules.md` next to this file and replace this block with the single line `@.ai-rules.md`.
> Do not edit the rules here. Change them in `.ai-rules.md` and re-deploy.
<!-- END:ai-rules -->

# Project Context

Imported on every session (imports are expanded together with this file, keep them short):

@docs/product.md
@docs/structure.md
@docs/tech.md

# Specs

Features are cut into one folder each: `specs/<feature-name>/` (`requirements.md`, `design.md`, `tasks.md`).
Work on exactly one feature folder at a time. The path-scoped rule `.claude/rules/specs.md` loads
automatically as soon as you touch a file below `specs/`, so the workflow is not repeated here.

Example prompt:
> Read `specs/password-reset/` and implement Task 2 from its `tasks.md`, following the rules in `CLAUDE.md`.
