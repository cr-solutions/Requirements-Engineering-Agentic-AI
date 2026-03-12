# Tasks: Password Reset Implementation


- [ ] **Task 1: Email Service Setup**
    - [ ] Create HTML/Text template for the reset email.
    - [ ] Write integration test for `Flask-Mail` or `smtplib` mock.
- [ ] **Task 2: Backend Logic (Core)**
    - [ ] Implement `generate_reset_token` in the Service layer.
    - [ ] Implement `/forgot-password` endpoint.
    - [ ] Implement `/reset-password` endpoint (including bcrypt hashing).
- [ ] **Task 3: Validation & Security**
    - [ ] Add validation for email format (using pydantic or marshmallow).
    - [ ] Enable rate-limiting middleware for the forgot-password endpoint.
- [ ] **Task 4: Testing**
    - [ ] Write Unit Tests for EARS criteria (Bouncer Pattern cases).
    - [ ] Verify squashed commit history before merging.