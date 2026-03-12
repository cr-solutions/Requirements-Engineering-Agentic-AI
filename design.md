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
1. Request -> `AuthController`
2. `AuthController` -> `ValidationMiddleware`
3. `ValidationMiddleware` -> `PasswordResetService`
4. `PasswordResetService` -> `UserRepository` (DB) & `EmailService` (SMTP/Flask-Mail)
