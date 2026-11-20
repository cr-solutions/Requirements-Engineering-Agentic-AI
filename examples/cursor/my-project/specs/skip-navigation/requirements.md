# Feature: Skip Navigation

## 1. User Story

As a keyboard or screen reader user, I want a "Skip to main content" link at the start of every page so that I do not have to tab through the whole navigation on each page load.

## 1.1 Glossary

* **Skip_Link**: First focusable element of every page, an anchor with the text "Skip to main content" and `href="#main-content"`.
* **Main_Content**: The `<main id="main-content">` element of a page.
* **Page_Layout**: The shared base template that all pages extend.
* **Focus_Indicator**: The visible outline shown on a focused element.

## 2. Acceptance Criteria (EARS Notation)

### 2.1 Event-Driven

* **WHEN** a keyboard user presses `Tab` for the first time on a freshly loaded page, **THE Page_Layout SHALL** move focus to the Skip_Link.
* **WHEN** the user activates the Skip_Link with `Enter`, **THE Page_Layout SHALL** move focus to the Main_Content, so that the next `Tab` lands on the first interactive element inside it.

### 2.2 Unwanted Behavior

* **IF** a page does not define a Main_Content, **THEN THE Page_Layout SHALL NOT** render the Skip_Link, so there is no link to a missing target.
* **IF** JavaScript is disabled, **THEN THE Skip_Link SHALL** still work, because it uses a plain anchor and no script.

### 2.3 State-Driven

* **WHILE** the Skip_Link has no focus, **THE Skip_Link SHALL** be visually hidden but remain available to assistive technology (it SHALL NOT use `display: none` or `visibility: hidden`).
* **WHILE** the Skip_Link has focus, **THE Skip_Link SHALL** be fully visible with a Focus_Indicator that has a contrast ratio of at least 3:1 against its background.
