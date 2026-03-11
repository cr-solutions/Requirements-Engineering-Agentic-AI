# Tasks: Password Reset Implementation

- [ ] **Task 1: Database Schema Adjustment**
    - [ ] Create migration for `reset_token` and `reset_token_expiry`.
    - [ ] Update Prisma/TypeORM models.
- [ ] **Task 2: Email Service Setup**
    - [ ] Create HTML/Text template for the reset email.
    - [ ] Write integration test for `Nodemailer` mock.
- [ ] **Task 3: Backend Logic (Core)**
    - [ ] Implement `generateResetToken` in the Service layer.
    - [ ] Implement `/forgot-password` endpoint.
    - [ ] Implement `/reset-password` endpoint (including Bcrypt hashing).
- [ ] **Task 4: Validation & Security**
    - [ ] Add express-validator for email format.
    - [ ] Enable rate-limiting middleware for the forgot-password endpoint.
- [ ] **Task 5: Testing**
    - [ ] Write Unit Tests for EARS criteria (Bouncer Pattern cases).
    - [ ] Verify squashed commit history before merging.