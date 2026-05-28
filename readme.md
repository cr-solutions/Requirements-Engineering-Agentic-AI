# Requirements-Engineering for Agentic AI (Industry Standard)

This repository utilizes a **Spec-Driven Development** workflow optimized for AI Agents. By providing structured context, we eliminate "vibe coding" and ensure production-ready results that adhere to corporate standards.

## 📁 Document Overview

### 1. `.ai-rules.md` (The House Rules)
* **Purpose:** Contains global project standards (Git workflow, naming conventions, database schemas, and coding paradigms like the Bouncer Pattern).
* **Scope:** **Global — applies to every project and every AI tool you use.** This is the "DNA" of your code quality. You maintain one master copy and reference it from each AI tool (see Setup below).

### 2. `requirements.md` (The "What")
* **Purpose:** Defines the business logic and user requirements using the **EARS Notation** (Easy Approach to Requirements Syntax).
* **Scope:** Feature-specific. It tells the AI exactly what conditions must be met (WHEN/THEN) without ambiguity.

### 3. `design.md` (The "How")
* **Purpose:** The technical blueprint. It defines the architecture (Service Layer, Repository Pattern), API endpoints, data flow, and **error/edge case handling**.
* **Scope:** Feature-specific. It prevents the AI from making poor architectural choices.

### 4. `tasks.md` (The "When")
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
1. **Draft** your `requirements.md` and `design.md` (including error/edge case flows).
2. **Initialize** the `tasks.md`.
3. **Point the AI** to these files: *"Implement Task 1 from tasks.md based on the specs in requirements.md and design.md."*
4. **Verify** the output against your `.ai-rules.md`.
5. **Log context** in `.kiro/context/CONTEXT_HISTORY_<year>-<month>-<day>_<task_name>.md` for traceability.

---

😎 **for more let's have a chat** 😎
