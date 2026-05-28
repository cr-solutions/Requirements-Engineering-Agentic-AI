# Design: Password Reset System

## 1. Architectural Decisions
* **Pattern:** Service-Layer Pattern. Logic resides in `PasswordResetService`, separated from the Controller.
* **Data Model:** Extend the `User` table with `reset_token (str)` and `reset_token_expiry (datetime)`.
* **Security:** Use JSON Web Tokens (JWT) for the reset link, signed with a dedicated `RESET_SECRET`.

## 2. API Endpoints
* **POST `/api/auth/forgot-password`**
    * Input: `{ "email": str }`
    * Logic: Validation -> Token Gen -> DB Update -> Email Dispatch.
* **POST `/api/auth/reset-password`**
    * Input: `{ "token": str, "new_password": str }`
    * Logic: Token Verification -> Password Hashing -> DB Update -> Invalidate Token.

## 3. Data Flow

### Happy Path
1. Request → `AuthController`
2. `AuthController` → `ValidationMiddleware`
3. `ValidationMiddleware` → `PasswordResetService`
4. `PasswordResetService` → `UserRepository` (DB) & `EmailService` (SMTP/Flask-Mail)
5. Response: `200 OK` — generic success message (always, regardless of email existence)

### Error & Edge Case Flows

| Scenario | Where caught | HTTP Code | Response |
|---|---|---|---|
| Invalid email format | `ValidationMiddleware` | `400` | `"Invalid email format"` |
| Email not in DB | `PasswordResetService` | `200` | Generic success (prevents user enumeration) |
| Active token exists (< 5 min) | `PasswordResetService` | `429` | `"Too many requests. Please wait before retrying."` |
| Expired token on reset | `PasswordResetService` | `410` | `"The link is invalid or expired"` |
| Tampered / invalid JWT signature | `PasswordResetService` | `400` | `"The link is invalid or expired"` |
| Token already used | `PasswordResetService` | `410` | `"This reset link has already been used"` |
| DB write failure | `UserRepository` | `500` | `"An internal error occurred"` (log full trace) |
| Email dispatch failure | `EmailService` | `503` | `"Could not send email. Please try again later."` |

> **Note:** The `200` response for unknown emails is intentional — it follows the security principle of not leaking whether an account exists (EARS requirement 2.2).
