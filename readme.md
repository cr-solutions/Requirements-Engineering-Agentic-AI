# Requirements-Engineering for Agentic AI (Industry Standard)

This repository utilizes a **Spec-Driven Development** workflow optimized for AI Agents. By providing structured context, we eliminate "vibe coding" and ensure production-ready results that adhere to corporate standards and save costs.

**Goal:** as universal as possible, but cleanly specific per tool. One master rules file, one spec format, and a ready-to-copy example project for every supported AI tool.

---

## 🗺 Repository Layout

```
Requirements-Engineering-Agentic-AI/
├── .ai-rules.md                 ← MASTER rules (single source of truth, tool-neutral)
├── scripts/
│   └── deploy_rules.py          ← fills .ai-rules.md into the tool-specific rules file
├── templates/
│   └── steering/                ← tool-neutral templates: product.md, structure.md, tech.md
└── examples/                    ← one clean example project per tool
    ├── kiro/my-project/         ← .kiro/steering, .kiro/specs, .kiro/hooks, docs/context
    ├── claude/my-project/       ← CLAUDE.md, .claude/rules, specs/
    ├── gemini/my-project/       ← GEMINI.md (+ per-feature GEMINI.md), specs/
    ├── antigravity/my-project/  ← AGENTS.md, .agents/rules, .agents/skills, specs/
    ├── cursor/my-project/       ← .cursor/rules/*.mdc, specs/
    ├── copilot/my-project/      ← .github/copilot-instructions.md, .github/instructions, specs/
    ├── agents-md/my-project/    ← AGENTS.md: the tool-neutral baseline (Codex, Zed, Aider, ...)
    └── paste-based/my-project/  ← prompt template for chat tools without auto-load
```

Every example contains the same three features and the same example context history, so you can diff the tools against each other. The spec content is identical on purpose; only the wiring around it differs.

| Feature | Domain | What it shows |
|---------|--------|---------------|
| `password-reset` | Backend, security | Full-size spec: glossary, EARS, error-flow table, 5 tasks in 4 waves |
| `health-check` | Backend, operations | Small spec: 503 vs 500, no information leak, logging levels |
| `skip-navigation` | Frontend, accessibility | Non-backend spec: HTML/CSS design, edge cases, manual test task |

**How to use an example:** copy `examples/<tool>/my-project/` into your project, run the deploy script (see [Master Rules](#-the-master-rules-ai-rulesmd)), and replace the `[...]` placeholders in the context files.

---

## 🧠 The Two Layers: Steering vs. Specs

Understanding this distinction is the key insight. Your AI context consists of two fundamentally different layers:

### 🔵 Steering (Permanent Project DNA)

These files are **loaded into every AI interaction** (or on demand, depending on the tool). They teach the AI *who your project is* — its rules, architecture, and tooling. They never change between features.

| File | Purpose | Answers |
|------|---------|---------|
| Rules file (from `.ai-rules.md`) | Coding standards, Git workflow, naming conventions | "How do we write code here?" |
| `product.md` | Product vision, capabilities, design principles | "What does this project do and why?" |
| `structure.md` | File tree, architectural patterns, module layout | "Where do things live?" |
| `tech.md` | Stack, dependencies, build/test/run commands | "How do I build and test this?" |

The name and location of the rules file is the only tool-specific part (`global_rules.md`, `CLAUDE.md`, `GEMINI.md`, `AGENTS.md`, ...). See the [compatibility matrix](#-tool-compatibility-matrix).

**Lifespan:** Lives with the project forever. Updated when the project evolves (new dependency, new module, version bump).

### 🟢 Spec Files (Temporary Feature Artifacts)

These files are **created per feature** and guide a specific implementation effort. They are consumed by the AI during development, then become historical documentation.

| File | Purpose | Answers |
|------|---------|---------|
| `requirements.md` | Glossary, user stories, acceptance criteria (EARS) | "What must the system do?" |
| `design.md` | Architecture, API contracts, data flow, error handling | "How should it be built?" |
| `tasks.md` | Implementation checklist with status tracking and dependency graph | "What's next?" |

**Lifespan:** Created at feature start, completed when the feature ships. Kept for historical reference.

### Why This Matters

Without steering, the AI:
- Invents features that contradict your product vision
- Puts files in wrong directories
- Suggests wrong frameworks and build commands
- Ignores your architectural patterns

Without specs, the AI:
- Guesses at business requirements
- Makes poor design decisions
- Works in unpredictable order
- Produces untraceable output

**Both layers together** = an AI that knows your project AND knows what to build next.

---

## ✂️ Feature Cutting: One Folder per Feature

**Don't keep one flat set of spec files at the project root.** Cut each feature into its own self-contained spec folder. This is the difference between the simplified layout you see in tutorials and how mature projects run.

### Flat (the simplified starting point)

```
my-project/
├── requirements.md      ← whatever feature you're working on RIGHT NOW
├── design.md
└── tasks.md
```

One feature at a time. The moment you start a second feature, you either overwrite the first or lose its history. There is no isolation, no parallelism, and no traceable record of what was built. (This repository used to be laid out this way. The new layout in `examples/` replaces it.)

### Feature-Cut (the recommended structure)

Each feature is a **vertical slice** with its own folder, carried end-to-end through the pipeline (EARS requirements → design → tasks):

```
specs/                          (Kiro: .kiro/specs/)
├── password-reset/             ← one feature, fully scoped
│   ├── requirements.md         ← glossary + EARS acceptance criteria
│   ├── design.md               ← architecture, data flow, error handling
│   ├── tasks.md                ← tasks + dependency graph (waves)
│   └── .config.kiro            ← Kiro only: spec metadata
├── health-check/               ← runs in parallel, zero overlap
│   └── ...
└── skip-navigation/            ← another feature, same structure
    └── ...
```

### Why cut features this way

- **Isolation:** each feature has its own requirements, design, and tasks. Nothing bleeds between features.
- **Parallelism:** features coexist. You (or multiple people/agents) can work on several without collision.
- **Traceability:** a shipped feature keeps its full spec as documentation. You can always answer "why was this built this way?"
- **Focused AI context:** you point the AI at exactly one spec folder, so it sees only what the feature needs.
- **Named-entity precision:** a scoped `requirements.md` defines its own **Glossary** (`Reset_Service`, `Reset_Token`, `Mailer`, ...) and writes EARS criteria against those exact entities. See [`requirements.md`](examples/kiro/my-project/.kiro/specs/password-reset/requirements.md).
- **Execution order:** `tasks.md` closes with a dependency graph, so the agent knows what can run in parallel:

```json
{
  "waves": [
    { "id": 0, "tasks": ["1"] },
    { "id": 1, "tasks": ["2"] },
    { "id": 2, "tasks": ["3", "5"] },
    { "id": 3, "tasks": ["4"] }
  ]
}
```

**Rule of thumb:** start flat only for a throwaway one-off. For anything real, cut the feature into its own folder from the first requirement.

---

## 📜 The Master Rules: `.ai-rules.md`

`.ai-rules.md` in the repository root is the **single source of truth** for coding standards, Git workflow, naming, error handling and database conventions. It is tool-neutral and stays where it is.

Every tool wants its rules in a different file. Each example therefore contains a **rules file with a clearly marked placeholder block**:

```markdown
<!-- BEGIN:ai-rules - filled by scripts/deploy_rules.py from .ai-rules.md, do not edit between the markers -->
> ⚠ TEMPLATE - ACTION REQUIRED: Replace this block with the full content of the master file `.ai-rules.md` ...
<!-- END:ai-rules -->
```

There are two ways to fill it:

1. **By hand:** paste the content of `.ai-rules.md` between the markers.
2. **With the script (recommended):** it replaces only the text between the markers and leaves everything else untouched (front matter, imports, project context). Safe to run repeatedly.

```bash
python3 scripts/deploy_rules.py --list                       # supported tools and target files
python3 scripts/deploy_rules.py kiro   ~/work/my-project     # -> .kiro/steering/global_rules.md
python3 scripts/deploy_rules.py claude ~/work/my-project     # -> CLAUDE.md
```

| Tool | Target file in the project | Script name |
|------|----------------------------|-------------|
| Kiro | `.kiro/steering/global_rules.md` | `kiro` |
| Claude Code | `CLAUDE.md` | `claude` |
| Gemini CLI | `GEMINI.md` | `gemini` |
| Antigravity | `AGENTS.md` | `antigravity` |
| Cursor | `.cursor/rules/global-rules.mdc` | `cursor` |
| GitHub Copilot | `.github/copilot-instructions.md` | `copilot` |
| AGENTS.md (generic) | `AGENTS.md` | `agents-md` |

The script exits with code `2` (usage / unknown tool), `3` (file not readable) or `4` (markers missing).

**Enterprise variant:** run the script from CI/CD or Ansible against every project. Rules are versioned in the repo, reviewed via PR, and new developers get them on clone. Projects extend the base rules in additional files (steering files, `.claude/rules/`, `.agents/rules/`, ...) without touching the shared master.

> ⚠ **Do not put secrets into rules files.** They are part of your codebase, and some tools (e.g. Claude Code with `@` imports, Kiro with `#[[file:...]]`) pull referenced files into the context.

---

## 🧩 Tool Compatibility Matrix

One look to see how each tool loads steering and where the tool-specific parts end. Details per tool follow below.

| Tool | Always-on rules file | Scoped / on-demand rules | Imports | Verify it loaded |
|------|----------------------|--------------------------|---------|------------------|
| **Kiro** | `.kiro/steering/*.md` (`inclusion: always`), `AGENTS.md` | front matter: `fileMatch`, `manual`, `auto` | `#[[file:path]]` | Steering view in the Kiro panel |
| **Claude Code** | `CLAUDE.md`, `.claude/CLAUDE.md`, `CLAUDE.local.md` (personal) | `.claude/rules/*.md` with `paths:` | `@path` | `/context all` |
| **Gemini CLI** | `GEMINI.md` (hierarchical, JIT per folder) | nested `GEMINI.md` per directory | `@file.md` | `/memory show` |
| **Antigravity** | `AGENTS.md` or `GEMINI.md` | `.agents/rules/*.md` with `trigger:` (`always_on`, `model_decision`, `glob`, `manual`) | `@[label](path)` inlines | Customizations panel, CLI `/context` |
| **Cursor** | `.cursor/rules/*.mdc` (`alwaysApply: true`), `AGENTS.md` | `.mdc` with `globs` or `description` | `@file` reference (read on demand, not inlined) | Cursor Customize, Rules |
| **GitHub Copilot** | `.github/copilot-instructions.md` | `.github/instructions/*.instructions.md` with `applyTo:` | none | "References" list in chat |
| **AGENTS.md** (Codex, Zed, Aider, ...) | `AGENTS.md` | nested `AGENTS.md` per directory | none | tool dependent |

**`AGENTS.md` is the common denominator.** It is plain markdown without front matter and, according to its documentation or third-party reports, read by Kiro, Cursor, Copilot, Antigravity, Codex and more. Claude Code reads it as a fallback when no `CLAUDE.md` exists, and Gemini CLI can be told to read it via `context.fileName`. If you want exactly one file for every tool, start with `examples/agents-md/`. Add the tool-specific files only where you need scoping, imports or on-demand loading.

> Tool behavior changes quickly. The table reflects the official documentation at the time of writing (see [Sources](#-sources)). Re-check the linked pages before you rely on edge cases.

---

## 🚀 Setup per Tool

Every section points at a ready-to-copy example under `examples/`.

### 🟣 Kiro (recommended) → [`examples/kiro/my-project`](examples/kiro/my-project)

```
.kiro/
├── steering/       global_rules.md, product.md, structure.md, tech.md
├── specs/          <feature-name>/ requirements.md, design.md, tasks.md, .config.kiro
└── hooks/          *.json agent hooks
docs/
└── context/        CONTEXT_HISTORY_<year>-<month>-<day>_<task>.md   (tool-neutral)
```

**Steering.** Markdown files in `.kiro/steering/` (workspace) or `~/.kiro/steering/` (global, personal). On conflict the workspace file wins. `product.md`, `tech.md` and `structure.md` are Kiro's foundation files and are included by default.

Four inclusion modes, set via front matter:

| Mode | Front matter | Loaded when |
|------|--------------|-------------|
| always | `inclusion: always` | every interaction (default) |
| fileMatch | `inclusion: fileMatch` + `fileMatchPattern: "**/*.py"` | a matching file is in context |
| manual | `inclusion: manual` | you type `#file-name` in chat |
| auto | `inclusion: auto` + `name` + `description` | your request matches the description |

`auto` keeps big reference material out of the context until it is relevant. That is the cheapest way to scale steering.

```markdown
---
inclusion: auto
name: api-design
description: REST API design patterns and conventions. Use when creating or modifying API endpoints.
---
```

Other details worth knowing:
- `AGENTS.md` in the workspace root, in subfolders or in `~/.kiro/steering/` is picked up automatically. It has no inclusion modes and is always included.
- Link live files with `#[[file:<relative_path>]]` (IDE and CLI V3 also support line ranges `:12-28` and `#[[folder:<path>]]`).
- **Custom agents do not get steering automatically.** Add `"resources": ["file://.kiro/steering/**/*.md"]` to the agent configuration.
- In Kiro CLI, inclusion modes depend on the CLI version (V3 full, V1/V2 partial). Check the steering docs.
- Amazon Q Developer CLI has become **Kiro CLI**. According to the Kiro upgrade guide, existing Q CLI workflows, subscription and authentication keep working.

**Specs.** `.kiro/specs/<feature-name>/` (three in the example) with `requirements.md`, `design.md`, `tasks.md` and `.config.kiro` (`specId`, `workflowType`, `specType`). Kiro supports requirements-first and design-first workflows. Kiro generates and runs the tasks for you; the example shows the file format.

**Hooks.** JSON files in `.kiro/hooks/`. The example [`context-history-reminder.json`](examples/kiro/my-project/.kiro/hooks/context-history-reminder.json) asks the agent at the end of every run (`Stop`) to update the context history. That automates step 6 of the workflow. Other useful triggers: `PostFileSave` (lint), `PostTaskExec` (run tests), `PreToolUse` (guard against writes to sensitive paths).

**Team distribution.** Global steering can be pushed to developer machines (MDM, group policy, Ansible) or to every repo via `deploy_rules.py` in CI. Treat steering changes like code changes: review them.

```bash
python3 scripts/deploy_rules.py kiro ~/work/my-project
```

---

### 🔵 Claude Code → [`examples/claude/my-project`](examples/claude/my-project)

```
my-project/
├── CLAUDE.md                  ← rules (from .ai-rules.md) + @imports of docs/*.md
├── CLAUDE.local.md            ← personal, in .gitignore
├── .claude/
│   └── rules/specs.md         ← path-scoped rule: loads only when touching specs/**
├── docs/                      ← product.md, structure.md, tech.md, context/
└── specs/                     ← password-reset/, health-check/, skip-navigation/
```

- `CLAUDE.md` is context, not enforcement. Keep it under roughly 200 lines. Move narrow guidance into `.claude/rules/*.md` with `paths:` front matter so it only loads when matching files are touched.
- `@path/to/file` imports expand the file into the context together with `CLAUDE.md`. Imports organize a long file but do not reduce its token cost.
- Subdirectory `CLAUDE.md` files load on demand when Claude touches files there.
- To **block** an action regardless of what the model decides, use a `PreToolUse` hook or `permissions.deny`, not an instruction.
- Claude Code can read `AGENTS.md` as project instructions. If you already have `AGENTS.md`, you can skip `CLAUDE.md` or import it with `@AGENTS.md`. Check the `Project instructions` setting in `/config` for the exact mode.
- Verify with `/context all` (shows the loaded memory files).

Drive one feature at a time:
> *"Read `specs/password-reset/` and implement Task 2 from its `tasks.md`, following the rules in `CLAUDE.md`."*

**Tip:** Claude Code subagents map naturally onto feature cutting. Spin up an isolated subagent scoped to a single spec folder so its context stays clean.

---

### 🟢 Gemini CLI → [`examples/gemini/my-project`](examples/gemini/my-project)

```
my-project/
├── GEMINI.md                          ← root steering (rules + @./docs imports)
├── docs/                              ← product.md, structure.md, tech.md, context/
└── specs/
    ├── password-reset/
    │   ├── GEMINI.md                  ← feature-scoped context
    │   └── requirements.md, design.md, tasks.md
    ├── health-check/                  ← same layout, own GEMINI.md
    └── skip-navigation/               ← same layout, own GEMINI.md
```

Gemini CLI loads context files hierarchically: global `~/.gemini/GEMINI.md`, then workspace and parent directories, then **just-in-time** any `GEMINI.md` in directories a tool touches. That hierarchy **is** the feature cut: when the agent works in `specs/password-reset/`, it sees the global rules plus only that feature's `GEMINI.md`.

- `@file.md` imports (relative or absolute) modularize large files.
- `/memory show` prints the concatenated context, `/memory reload` re-scans.
- The context file name is configurable. To let Gemini read `AGENTS.md` too, set this in your Gemini CLI `settings.json` (for example the project-level `.gemini/settings.json`):

```json
{ "context": { "fileName": ["GEMINI.md", "AGENTS.md"] } }
```

---

### 🟣 Google Antigravity → [`examples/antigravity/my-project`](examples/antigravity/my-project)

```
my-project/
├── AGENTS.md                              ← always-on rules (no front matter)
├── .agents/
│   ├── rules/specs-workflow.md            ← rule with trigger: model_decision
│   └── skills/implement-spec-task/SKILL.md
├── docs/                                  ← product.md, structure.md, tech.md, context/
└── specs/                                 ← password-reset/, health-check/, skip-navigation/
```

- Always-on guidance goes into `AGENTS.md` (or `GEMINI.md`). Both need **no** front matter.
- Files in `.agents/rules/*.md` **must** start with front matter. `trigger` is `always_on`, `model_decision` (needs `description`), `glob` (needs `globs`) or `manual`. A rule without a valid trigger is not loaded, so check the spelling.
- `@[label](path)` inlines another file, `@filename` only resolves the path.
- **Limits:** 24,000 bytes per rule file, 20,000 tokens for all always-on and global rules together. Put long, narrow guidance into `model_decision` or `glob` rules.
- Antigravity loads rules from the workspace folder and its parents up to the repository root. It does **not** load rules from subfolders below the workspace. That is why this example has no per-feature rule file; it uses the skill instead.
- **Skills replace workflows.** Reusable procedures live in `.agents/skills/<name>/SKILL.md`. Legacy workflows in `.agents/workflows/` were announced to stop working on October 19, 2026. Run `/migrate-workflows` if you still have some.
- **Artifacts** (implementation plans, task lists, walkthroughs) are Antigravity's per-objective outputs. They play the role of a feature's `design.md` / `tasks.md`, and Google documents a spec-driven workflow in its [codelab](https://codelabs.developers.google.com/codelabs/getting-started-with-spec-driven-development-in-antigravity).

---

### 🟠 Cursor → [`examples/cursor/my-project`](examples/cursor/my-project)

```
my-project/
├── .cursor/rules/
│   ├── global-rules.mdc        ← alwaysApply: true (rules from .ai-rules.md)
│   ├── project-context.mdc     ← alwaysApply: true, points at docs/*.md
│   └── specs-workflow.mdc      ← globs: specs/**
├── docs/                       ← product.md, structure.md, tech.md, context/
└── specs/                      ← three feature folders
```

- Project rules are `.mdc` files in `.cursor/rules/`. **A plain `.md` file in that folder is ignored.**
- Front matter fields: `description`, `globs`, `alwaysApply`. They give four behaviors: always, auto-attached by glob, agent-decided by description, manual via `@rule-name`.
- Mentioning a file in a rule (`@docs/tech.md`) lets the agent read it when needed. It is **not** inlined. Paste into the rule body if something must always be in context.
- Cursor also reads `AGENTS.md` in the root and in subdirectories, as a simple alternative to rules.
- The legacy `.cursorrules` file is no longer part of the current rules documentation. Use `.cursor/rules/*.mdc` or `AGENTS.md`.

---

### ⚫ GitHub Copilot → [`examples/copilot/my-project`](examples/copilot/my-project)

```
my-project/
├── .github/
│   ├── copilot-instructions.md                 ← repository-wide rules
│   └── instructions/specs.instructions.md      ← applyTo: "specs/**"
├── docs/                       ← product.md, structure.md, tech.md, context/
└── specs/                      ← three feature folders
```

- `.github/copilot-instructions.md` applies to the whole repository.
- Path-specific files must end with `.instructions.md` and start with `applyTo:` glob front matter. On GitHub.com they currently apply to the cloud agent and code review.
- Copilot code review reads instructions from the **head** branch of a pull request, so you can test instruction changes in the same PR.
- Copilot has no import syntax. Point at files by path.

---

### ⚪ AGENTS.md, the tool-neutral baseline → [`examples/agents-md/my-project`](examples/agents-md/my-project)

One plain-markdown file at the repository root (nested ones allowed in monorepos). No front matter, no imports, no lock-in. Start here if you use several tools, or tools not listed above (Codex, Zed, Aider, ...). Add tool-specific files only for scoping and on-demand loading.

---

### 🟡 Paste-based chat tools (ChatGPT and others) → [`examples/paste-based/my-project`](examples/paste-based/my-project)

For tools without a project auto-load mechanism:

1. Keep `.ai-rules.md` and the `docs/` files at hand.
2. Start every chat with [`prompt-template.md`](examples/paste-based/my-project/prompt-template.md).
3. Paste **one** feature folder only. Even without auto-load, feature cutting pays off: the model never sees unrelated specs.

---

## 🛠 Workflow Routine

### One-Time Project Setup (Steering)
1. **Copy** `examples/<tool>/my-project/` into your project.
2. **Deploy the rules:** `python3 scripts/deploy_rules.py <tool> <project-dir>`.
3. **Fill** `product.md`, `structure.md`, `tech.md` (templates in `templates/steering/`).
4. **Verify** the tool actually loaded them (see the matrix column "Verify it loaded").

### Per-Feature Workflow (Specs)
1. **Cut the feature:** create `specs/<feature-name>/` (Kiro: `.kiro/specs/<feature-name>/`).
2. **Draft** `requirements.md` and `design.md`. Define a Glossary of named entities, then write EARS criteria against them. Include error and edge case flows in the design.
3. **Initialize** `tasks.md`. Link each task back to the requirement or design section it implements (`← design.md §2, requirements §2.1`) and add the dependency graph.
4. **Point the AI** at the one folder: *"Implement Task 1 from `specs/password-reset/tasks.md` based on the specs in that folder."*
5. **Verify** the output against `.ai-rules.md`.
6. **Log context** in `docs/context/CONTEXT_HISTORY_<year>-<month>-<day>_<task_name>.md` (location defined in `.ai-rules.md`, section 9; see the [example](examples/kiro/my-project/docs/context/CONTEXT_HISTORY_2026-06-01_password-reset.md)). The path is tool-neutral on purpose, so every tool reads the same history. In Kiro, a `Stop` hook can write it for you.
7. **Keep the folder** after shipping. The completed spec is permanent documentation.

### When to Update Steering

| File | Update when... |
|------|---------------|
| `product.md` | After each version release or capability addition |
| `structure.md` | When adding new modules, directories, or changing patterns |
| `tech.md` | When adding/upgrading dependencies or changing build/test commands |
| Rules file | Rarely, only when team-wide standards evolve. Change `.ai-rules.md`, then re-run `deploy_rules.py` |

> **Tip:** Stale steering is worse than no steering. An outdated `tech.md` that lists old dependencies will actively mislead the AI. Keep it current or remove it.

---

## 💸 Keeping the Context (and the Bill) Small

Every always-on line costs tokens in every interaction. The structure in this repo is built to keep that small:

- **Feature cutting:** the agent reads one spec folder, not every spec.
- **On-demand loading:** use Kiro `auto`/`fileMatch`, Claude `paths:`, Antigravity `model_decision`/`glob`, Cursor `globs`, Copilot `applyTo` for narrow guidance.
- **Short always-on files:** around 200 lines for `CLAUDE.md`, 24 KB per Antigravity rule file. Split beyond that.
- **Skills over rules for procedures:** step-by-step workflows (deploy, implement a spec task) only load when needed.

---

## ⚠️ Common Anti-Patterns (What Goes Wrong Without This)

| Problem | Root Cause | Solved By |
|---------|-----------|-----------|
| "The AI installed Redis even though my project already uses Memcached" | AI doesn't know your stack | `tech.md` |
| "The AI created a new `utils/` folder when I already have `lib/common/`" | AI doesn't know your file structure | `structure.md` |
| "The AI built a REST endpoint but my project uses GraphQL" | AI doesn't know your architecture | `product.md` + `tech.md` |
| "The AI added a feature that contradicts our product philosophy" | AI doesn't know your design principles | `product.md` |
| "The AI used jest for testing but we use pytest" | AI defaults to popular choices, not yours | `tech.md` |
| "The AI forgot what we discussed in the last session" | No persistent session memory | Context History |
| "The AI writes code with deep nesting and no input validation" | No coding standards loaded | Rules file from `.ai-rules.md` |
| "The AI ignored my rule and changed a protected file anyway" | Instructions are context, not enforcement | Hooks / permission deny rules per tool |
| "My rules are loaded in Kiro but not in Claude" | Different file names per tool | `deploy_rules.py` + `AGENTS.md` |
| "The rule file silently has no effect" | Wrong extension or missing front matter (Cursor `.md`, Antigravity trigger, Copilot `.instructions.md`) | The per-tool notes above |

**The pattern:** every time an AI "does something stupid", the real problem is missing context. These files eliminate the guessing.

---

## 📚 Sources

Content was rephrased from the following documentation for this readme. Behavior may have changed since, so check the originals.

- Kiro steering: <https://kiro.dev/docs/steering/>
- Kiro CLI as successor of Q CLI: <https://kiro.dev/docs/upgrade-guides/migrating-from-q/>
- Claude Code memory and rules: <https://code.claude.com/docs/en/memory>
- Gemini CLI context files: <https://geminicli.com/docs/cli/gemini-md/>
- Antigravity rules: <https://antigravity.google/docs/rules>
- Antigravity skills and workflow migration (third-party summary of the docs): <https://iceberglakehouse.com/posts/2026-03-context-google-antigravity/>
- Cursor rules: <https://cursor.com/docs/context/rules>
- GitHub Copilot repository instructions: <https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions>
- Claude Code reading `AGENTS.md` (third-party report): <https://dev.to/valyuai/claude-code-now-supports-agentsmd-natively-heres-how-it-actually-works-5nl>
- Cross-tool loading test of `AGENTS.md` / `CLAUDE.md` / `GEMINI.md` (third-party, small sample): <https://dev.to/silo_crow/agentsmd-vs-claudemd-vs-geminimd-what-6-ai-coding-clis-really-read-1gfh>

---

😎 **for more let's have a chat** 😎
