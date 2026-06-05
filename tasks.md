# Tasks: Password Reset Implementation


## Completed ✅

- [X] **Task 1: Email Service Setup** ← design.md §3, requirements §2.1
    - [X] Create HTML/Text template for the reset email.
    - [X] Write integration test for `Flask-Mail` or `smtplib` mock.

## In Progress 🔄

- [ ] **Task 2: Backend Logic (Core)** ← design.md §1-§2, requirements §2.1
    - [ ] Implement `generate_reset_token` in the Service layer.
    - [ ] Implement `/forgot-password` endpoint.
    - [ ] Implement `/reset-password` endpoint (including bcrypt hashing).
- [ ] **Task 3: Validation & Security** ← design.md §3 (Error Flows), requirements §2.2-§2.3
    - [ ] Add validation for email format (using pydantic or marshmallow).
    - [ ] Enable rate-limiting middleware for the forgot-password endpoint.
- [ ] **Task 4: Testing** ← requirements §2 (all EARS criteria)
    - [ ] Write Unit Tests for EARS criteria (Bouncer Pattern cases).
    - [ ] Verify squashed commit history before merging.

## Planned 📋

- [ ] **Task 5: Frontend Integration** ← design.md §3 (Error Flows), requirements §2.2
    - [ ] Build "Forgot Password" form with client-side email validation.
    - [ ] Build "Reset Password" form with password strength indicator.
    - [ ] Handle all API error responses with user-friendly messages (map HTTP codes to UI copy).
    - [ ] Add loading state and disable submit button during request to prevent double-submit.
