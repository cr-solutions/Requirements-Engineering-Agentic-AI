---
name: implement-spec-task
description: Implements one task from a feature spec folder (specs/<feature>/tasks.md). Use when the user asks to implement, continue or verify a task of a spec.
---
## Prerequisites
- The user named exactly one feature folder, e.g. `specs/password-reset/`. If not, ask which one.
- The folder contains `requirements.md`, `design.md` and `tasks.md`.

## Steps
1. Read `requirements.md` (Glossary and EARS criteria), then `design.md`, then `tasks.md`.
2. Pick the requested task, or the first open task of the earliest unfinished wave in the dependency graph.
3. Implement it in small, testable increments and follow the global rules in `AGENTS.md`.
4. Tick the task's checkbox in `tasks.md`.
5. Append decisions, blockers and next steps to the context history file.

## Verification
- Every EARS criterion referenced by the task (`← requirements §x`) is covered by code or a test.
- Error flows referenced from `design.md` return the documented HTTP status codes.
- Build and tests pass.
