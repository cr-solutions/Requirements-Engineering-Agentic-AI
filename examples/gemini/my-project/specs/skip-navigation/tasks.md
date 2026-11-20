# Tasks: Skip Navigation Implementation

## Planned 📋
- [ ] **Task 1: Target Element** ← design.md §1-§2, requirements §2.1
    - [ ] Add `id="main-content"` and `tabindex="-1"` to `<main>` in `base.html`.
    - [ ] Add `scroll-margin-top` if a sticky header exists.
- [ ] **Task 2: Skip Link Markup & Style** ← design.md §2, requirements §2.1, §2.3
    - [ ] Add the `Skip_Link` as first element of `<body>`.
    - [ ] Add the `.skip-link` CSS (hidden off-screen, visible on `:focus`).
- [ ] **Task 3: Conditional Rendering** ← design.md §3 (Edge Cases), requirements §2.2
    - [ ] Render the `Skip_Link` only if the page defines a `main` block.
- [ ] **Task 4: Verification** ← requirements §2 (all EARS criteria)
    - [ ] Template test: link present as first focusable element, absent without `main`.
    - [ ] Run an automated accessibility check (for example axe) on the base layout.
    - [ ] Manual test: keyboard only, plus one screen reader.

## Task Dependency Graph

```json
{
  "waves": [
    { "id": 0, "tasks": ["1"] },
    { "id": 1, "tasks": ["2", "3"] },
    { "id": 2, "tasks": ["4"] }
  ]
}
```
