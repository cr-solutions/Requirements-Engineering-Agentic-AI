# Requirements-Engineering for Agentic AI (Industry Standard)

This repository utilizes a **Spec-Driven Development** workflow optimized for AI Agents. By providing structured context, we eliminate "vibe coding" and ensure production-ready results that adhere to corporate standards.

## 📁 Document Overview

### 1. `.ai-rules.md` (The House Rules)
* **Purpose:** Contains global project standards (Git workflow, naming conventions, database schemas, and coding paradigms like the Bouncer Pattern).
* **Scope:** Project-wide. This is the "DNA" of your code quality.

### 2. `requirements.md` (The "What")
* **Purpose:** Defines the business logic and user requirements using the **EARS Notation** (Easy Approach to Requirements Syntax).
* **Scope:** Feature-specific. It tells the AI exactly what conditions must be met (WHEN/THEN) without ambiguity.

### 3. `design.md` (The "How")
* **Purpose:** The technical blueprint. It defines the architecture (Service Layer, Repository Pattern), API endpoints, and data flow.
* **Scope:** Feature-specific. It prevents the AI from making poor architectural choices.

### 4. `tasks.md` (The "When")
* **Purpose:** An iterative checklist for the AI.
* **Scope:** Implementation-specific. It allows you to track progress and forces the AI to work in small, testable increments.

---

## 🚀 How to Setup

### **In Kiro**
Save the global rules content under:
` .kiro/steering/global_rules.md`
*Kiro will automatically respect these rules for every action.*

### **In Gemini / Amazon Q and other LLM**
Create the file `.ai-rules.md` or better `.cursorrules` in the root directory of your project. When you open a new chat session, start with this prompt:

> **"Strictly adhere to these specifications for all code suggestions and Git operations."**

Even though it has "Cursor" in the name, .cursorrules has become the absolute de facto universal standard for AI extensions.

---

## 🛠 Workflow Routine
1.  **Draft** your `requirements.md` and `design.md`.
2.  **Initialize** the `tasks.md`.
3.  **Point the AI** to these files: *"Implement Task 1 from tasks.md based on the specs in requirements.md and design.md."*
4.  **Verify** the output against your `.ai-rules.md`/`.cursorrules`.

---


😎 **for more let's have a chat** 😎
