\# Tasks: Password Reset Implementation



\- \[ ] \*\*Task 1: Database Schema Adjustment\*\*

&#x20;   - \[ ] Create migration for `reset\_token` and `reset\_token\_expiry`.

&#x20;   - \[ ] Update Prisma/TypeORM models.

\- \[ ] \*\*Task 2: Email Service Setup\*\*

&#x20;   - \[ ] Create HTML/Text template for the reset email.

&#x20;   - \[ ] Write integration test for `Nodemailer` mock.

\- \[ ] \*\*Task 3: Backend Logic (Core)\*\*

&#x20;   - \[ ] Implement `generateResetToken` in the Service layer.

&#x20;   - \[ ] Implement `/forgot-password` endpoint.

&#x20;   - \[ ] Implement `/reset-password` endpoint (including Bcrypt hashing).

\- \[ ] \*\*Task 4: Validation \& Security\*\*

&#x20;   - \[ ] Add express-validator for email format.

&#x20;   - \[ ] Enable rate-limiting middleware for the forgot-password endpoint.

\- \[ ] \*\*Task 5: Testing\*\*

&#x20;   - \[ ] Write Unit Tests for EARS criteria (Bouncer Pattern cases).

&#x20;   - \[ ] Verify squashed commit history before merging.

