# Requirements-Engineering for Agentic AI (Industry Standard)

This repository utilizes a **Spec-Driven Development** workflow optimized for AI Agents. By providing structured context, we eliminate "vibe coding" and ensure production-ready results that adhere to corporate standards and save costs.

---

## 🧠 The Two Layers: Steering vs. Specs

Understanding this distinction is the key insight. Your AI context consists of two fundamentally different layers:

### 🔵 Steering Files (Permanent Project DNA)

These files are **always loaded** into every AI interaction. They teach the AI *who your project is* — its rules, architecture, and tooling. They never change between features.

| File | Purpose | Answers |
|------|---------|---------|
| `global_rules.md` | Coding standards, Git workflow, naming conventions | "How do we write code here?" |
| `product.md` | Product vision, capabilities, design principles | "What does this project do and why?" |
| `structure.md` | File tree, architectural patterns, module layout | "Where do things live?" |
| `tech.md` | Stack, dependencies, build/test/run commands | "How do I build and test this?" |

**Lifespan:** Lives with the project forever. Updated when the project evolves (new dependency, new module, version bump).

### 🟢 Spec Files (Temporary Feature Artifacts)

These files are **created per feature** and guide a specific implementation effort. They are consumed by the AI during development, then become historical documentation.

| File | Purpose | Answers |
|------|---------|---------|
| `requirements.md` | Business logic, user stories, acceptance criteria (EARS) | "What must the system do?" |
| `design.md` | Architecture, API contracts, data flow, error handling | "How should it be built?" |
| `tasks.md` | Implementation checklist with status tracking | "What's next?" |

**Lifespan:** Created at feature start, completed when the feature ships. Kept for historical reference.

### Why This Matters

Without steering files, the AI:
- Invents features that contradict your product vision
- Puts files in wrong directories
- Suggests wrong frameworks and build commands
- Ignores your architectural patterns

Without spec files, the AI:
- Guesses at business requirements
- Makes poor design decisions
- Works in unpredictable order
- Produces untraceable output

**Both layers together** = an AI that knows your project AND knows what to build next.

---

## 📁 Document Overview

### Steering Files

#### 1. `.ai-rules.md` / `global_rules.md` (The House Rules)
* **Purpose:** Contains global project standards (Git workflow, naming conventions, database schemas, and coding paradigms like the Bouncer Pattern).
* **Scope:** **Global — applies to every project and every AI tool you use.** This is the "DNA" of your code quality. You maintain one master copy and reference it from each AI tool (see Setup below).

#### 2. `product.md` (The Product Vision)
* **Purpose:** Describes what the project IS — its core capabilities, design principles, and current version. Prevents the AI from making decisions that contradict your product direction.
* **Scope:** Project-wide. Updated when capabilities change or new versions are released.

#### 3. `structure.md` (The Architecture Map)
* **Purpose:** Documents the file tree, module layout, and architectural patterns. Tells the AI exactly where to put new code and how existing components interact.
* **Scope:** Project-wide. Updated when new modules or patterns are introduced.

#### 4. `tech.md` (The Tech Stack)
* **Purpose:** Lists the language, dependencies, build commands, test framework, and environment variables. Eliminates "let me install X for you" problems.
* **Scope:** Project-wide. Updated when dependencies or tooling change.

### Spec Files

#### 5. `requirements.md` (The "What")
* **Purpose:** Defines the business logic and user requirements using the **EARS Notation** (Easy Approach to Requirements Syntax).
* **Scope:** Feature-specific. It tells the AI exactly what conditions must be met (WHEN/THEN) without ambiguity.

#### 6. `design.md` (The "How")
* **Purpose:** The technical blueprint. It defines the architecture (Service Layer, Repository Pattern), API endpoints, data flow, and **error/edge case handling**.
* **Scope:** Feature-specific. It prevents the AI from making poor architectural choices.

#### 7. `tasks.md` (The "When")
* **Purpose:** An iterative checklist for the AI.
* **Scope:** Implementation-specific. It allows you to track progress and forces the AI to work in small, testable increments.

---

## 🚀 How to Setup

The `.ai-rules.md` file is your **single source of truth**. You maintain it once and wire it into each AI tool differently. Here is how:

---

### 🟣 Kiro (Recommended)

Kiro uses **Steering Files** — markdown files that are automatically injected into every agent interaction.

---

#### 🏢 Enterprise Pattern (Recommended)

In an enterprise setup, the **project-level** steering file is the right approach:

```
.kiro/steering/global_rules.md
```

**Why project-level wins in enterprise:**
- Rules are **stack/language-specific** — a Python project has different conventions than a TypeScript one
- The file lives **inside the repo** — versioned, reviewed via PR, and fully auditable
- A **central deployment tool** (Ansible, a custom CLI, a GitHub Actions workflow) maintains one master template and pushes it into every project's `.kiro/steering/` automatically
- Teams can **extend** the base rules per project without touching the shared template
- New developers get the rules automatically when they clone the repo — no manual setup

**Example deployment workflow:**
```
central-rules-repo/
  global_rules.md          ← single source of truth, maintained by the team

→ CI/CD or Ansible pushes this to every project:
  project-a/.kiro/steering/global_rules.md
  project-b/.kiro/steering/global_rules.md
  project-c/.kiro/steering/global_rules.md  ← can extend with project-specific additions
```

---

#### 👤 Personal / Solo Pattern

For personal use across all your own projects, the user-level path is a convenient shortcut:

```
~/.kiro/steering/global_rules.md
```

Kiro will apply these rules to every workspace on your machine. Good for personal projects, not suitable for team environments where rules need to be versioned per repo.

---

**How to create a steering file:**
Create `global_rules.md` in the appropriate location and paste in your `.ai-rules.md` content. Optionally add a front-matter header to control when it loads:

```markdown
---
inclusion: always
---
# Global AI Coding & Workflow Rules
...
```

> `inclusion: always` — loaded on every interaction (default).  
> `inclusion: manual` — only when you explicitly reference it with `#global_rules` in chat.  
> `inclusion: fileMatch` + `fileMatchPattern: '**/*.py'` — only when a matching file is in context.

You can also reference other files directly inside a steering file:
```markdown
#[[file:requirements.md]]
```
This injects the full content of `requirements.md` into the steering context automatically.

---

### 🟡 Cursor / VS Code (Copilot / Continue)

`.cursorrules` has become the **de facto universal standard** for AI extensions, even though it originated in Cursor.

Place the file in your project root:
```
.cursorrules
```
This is simply a copy or symlink of your `.ai-rules.md`. Most AI extensions (Cursor, GitHub Copilot Chat, Continue.dev) will pick it up automatically.

When opening a new chat session in tools that don't auto-load it, start with:
> **"Strictly adhere to the rules in `.cursorrules` for all code suggestions and Git operations."**

---

### 🔵 Claude (Anthropic)

Claude uses a `CLAUDE.md` file in your project root:
```
CLAUDE.md
```
This file is automatically loaded by Claude Code and Claude.ai projects. Use it to reference your rules and additional context files:

```markdown
# Project Rules
See full rules: #[[file:.ai-rules.md]]

# Active Feature Context
See requirements: #[[file:requirements.md]]
See design: #[[file:design.md]]
```

> **Tip:** Claude respects file references well. You can chain multiple files to give it the full picture for a feature in one shot.

---

### 🟠 Gemini / Amazon Q / ChatGPT and other LLMs

These tools don't have a native auto-load mechanism. The workflow is:

1. Keep your `.ai-rules.md` in the project root (or a central location).
2. When starting a new chat session, **attach or paste** the file content.
3. Open with this prompt:
   > **"Strictly adhere to these specifications for all code suggestions and Git operations."**
4. For feature work, also attach `requirements.md` and `design.md` in the same message.

**Example opening prompt:**
```
Strictly adhere to these specifications for all code suggestions and Git operations.

[paste .ai-rules.md content]

I am now working on the following feature:

[paste requirements.md content]
[paste design.md content]

Implement Task 2 from the task list below:

[paste tasks.md content]
```

---

## 🛠 Workflow Routine

### One-Time Project Setup (Steering)
1. **Create** `product.md` — describe what your project does, its principles, current version.
2. **Create** `structure.md` — document your file tree and architectural patterns.
3. **Create** `tech.md` — list your stack, dependencies, build/test commands.
4. **Create** `global_rules.md` — your coding standards (or use the `.ai-rules.md` template from this repo).

### Per-Feature Workflow (Specs)
1. **Draft** your `requirements.md` and `design.md` (including error/edge case flows).
2. **Initialize** the `tasks.md` — link each task back to the requirement/design section it implements (e.g., `← design.md §2, requirements §2.1`).
3. **Point the AI** to these files: *"Implement Task 1 from tasks.md based on the specs in requirements.md and design.md."*
4. **Verify** the output against your `.ai-rules.md`.
5. **Log context** in `.kiro/context/CONTEXT_HISTORY_<year>-<month>-<day>_<task_name>.md` for traceability.

### When to Update Steering Files

| File | Update when... |
|------|---------------|
| `product.md` | After each version release or capability addition |
| `structure.md` | When adding new modules, directories, or changing patterns |
| `tech.md` | When adding/upgrading dependencies or changing build/test commands |
| `global_rules.md` | Rarely — only when team-wide standards evolve |

> **Tip:** Stale steering files are worse than no steering files. An outdated `tech.md` that lists old dependencies will actively mislead the AI. Keep them current or remove them.

---

## ⚠️ Common Anti-Patterns (What Goes Wrong Without This)

These are real failure modes you'll encounter when AI lacks proper context:

| Problem | Root Cause | Solved By |
|---------|-----------|-----------|
| "The AI installed Redis even though my project already uses Memcached" | AI doesn't know your stack | `tech.md` |
| "The AI created a new `utils/` folder when I already have `lib/common/`" | AI doesn't know your file structure | `structure.md` |
| "The AI built a REST endpoint but my project uses GraphQL" | AI doesn't know your architecture | `product.md` + `tech.md` |
| "The AI added a feature that contradicts our product philosophy" | AI doesn't know your design principles | `product.md` |
| "The AI used jest for testing but we use pytest" | AI defaults to popular choices, not yours | `tech.md` |
| "The AI forgot what we discussed in the last session" | No persistent session memory | Context History |
| "The AI writes code with deep nesting and no input validation" | No coding standards loaded | `global_rules.md` |

**The pattern:** Every time an AI "does something stupid", the real problem is missing context. These files eliminate the guessing.

---

## 📂 Example: File Layout in a Real Project

```
my-project/
├── .kiro/
│   ├── steering/                    ← ALWAYS-ON CONTEXT
│   │   ├── global_rules.md         ← Coding standards
│   │   ├── product.md              ← Product vision
│   │   ├── structure.md            ← Architecture map
│   │   └── tech.md                 ← Stack & tooling
│   └── context/                     ← SESSION LOGS
│       └── CONTEXT_HISTORY_2026-06-01_password-reset.md
├── requirements.md                  ← FEATURE SPEC (temporary)
├── design.md                        ← FEATURE SPEC (temporary)
├── tasks.md                         ← FEATURE SPEC (temporary)
├── src/                             ← Your actual code
└── .ai-rules.md                     ← For non-Kiro tools (Gemini, Q, etc.)
```

> **Note:** In Kiro, spec files can also live under `.kiro/specs/<feature-name>/` for multi-feature tracking.

---

😎 **for more let's have a chat** 😎
