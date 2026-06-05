# Context History: Password Reset — 2026-06-01

> This is an example of a context history file. In a real project, create one per task/feature under `.kiro/context/CONTEXT_HISTORY_<date>_<task-name>.md`.

## Session 1 (2026-06-01)

### Completed
- Task 1: Email Service Setup
  - Created HTML/Text template using Jinja2
  - Integration test passing with Flask-Mail mock

### Decisions
- **Flask-Mail over smtplib** — chose Flask-Mail for built-in template support and async dispatch; smtplib would require manual MIME handling
- **Template location** — placed in `templates/email/` following Flask convention

### Blockers
- None

---

## Session 2 (2026-06-03)

### Completed
- Task 2: Backend Logic (partial)
  - Implemented `generate_reset_token` using PyJWT with dedicated `RESET_SECRET`
  - `/forgot-password` endpoint working

### Decisions
- **Dedicated RESET_SECRET** — not reusing the app `SECRET_KEY`, so rotating one doesn't invalidate the other
- **Token payload** — includes `sub` (user email), `exp` (15 min), `jti` (unique ID for single-use enforcement)

### Blockers
- Rate limiting middleware: undecided between `flask-limiter` (simpler) vs custom middleware (more control). Parking for Session 3.

### Open Questions
- Should rate limit be per-IP or per-email? Design says per-email (§2.3), but per-IP adds brute-force protection.

---

## Session 3 (2026-06-05)

### Completed
- Task 2: Backend Logic (completed)
  - `/reset-password` endpoint with bcrypt hashing
  - Token single-use enforcement via `jti` stored in DB
- Task 3: Validation & Security
  - Email validation with pydantic
  - Rate limiting: `flask-limiter` with per-email key (5-minute window)

### Decisions
- **Rate limit per-email** — sticking with design spec (§2.3). Per-IP protection handled at infrastructure level (WAF/nginx).
- **flask-limiter** — simpler integration, sufficient for our scale. Custom middleware would be over-engineering.

### Blockers
- None

### Next
- Task 4: Testing — write unit tests covering all EARS criteria
