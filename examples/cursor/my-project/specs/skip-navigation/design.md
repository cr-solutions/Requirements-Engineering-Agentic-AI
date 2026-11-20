# Design: Skip Navigation

## 1. Architectural Decisions

* **Single place:** the change lives in the `Page_Layout` base template only. Pages inherit it, no page-level code.
* **Plain HTML + CSS:** no JavaScript, so the link works without scripts (requirements §2.2).
* **Visually hidden, not removed:** the link is moved off-screen with CSS and revealed on `:focus`. `display: none` would also hide it from assistive technology.
* **Focusable target:** `<main id="main-content" tabindex="-1">` so focus really moves to the target in all browsers. `tabindex="-1"` keeps `main` out of the normal tab order.

## 2. Markup & Style

Template (`base.html`):

```html
<body>
  <a class="skip-link" href="#main-content">Skip to main content</a>
  <nav>...</nav>
  <main id="main-content" tabindex="-1">{% block content %}{% endblock %}</main>
</body>
```

Stylesheet:

```css
.skip-link {
  position: absolute;
  left: -9999px;            /* off-screen, but still focusable and readable by screen readers */
}
.skip-link:focus {
  left: 1rem;
  top: 1rem;
  z-index: 1000;
  padding: 0.5rem 1rem;
  background: #fff;
  color: #000;
  outline: 3px solid #005fcc;   /* >= 3:1 contrast against the background */
}
```

## 3. Data Flow

### Happy Path
1. Page loads, nothing is focused.
2. User presses `Tab` → focus lands on `Skip_Link`, which becomes visible.
3. User presses `Enter` → browser jumps to `#main-content` and focus moves into it.
4. Next `Tab` → first interactive element inside `Main_Content`.

### Edge Cases
| Scenario | Where handled | Behavior |
|---|---|---|
| Page defines no `main` block | `base.html` (conditional) | Skip_Link is not rendered |
| JavaScript disabled | Plain anchor | Works unchanged |
| `<base href>` is set | Link uses `href="#main-content"` | Anchor resolves against the base URL. Verify in a test, use an absolute fragment URL if needed |
| Sticky header covers the target | CSS `scroll-margin-top` on `main` | Target stays visible after the jump |

> **Note:** Automated checks (for example axe) only find part of the accessibility problems. Full validation needs manual testing with a keyboard and screen readers plus expert review.
