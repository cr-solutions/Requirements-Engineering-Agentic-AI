\# Design: Password Reset System



\## 1. Architectural Decisions

\* \*\*Pattern:\*\* Service-Layer Pattern. Logic resides in `PasswordResetService.ts`, separated from the Controller.

\* \*\*Data Model:\*\* Extend the `User` table with `reset\_token (string)` and `reset\_token\_expiry (datetime)`.

\* \*\*Security:\*\* Use JSON Web Tokens (JWT) for the reset link, signed with a dedicated `RESET\_SECRET`.



\## 2. API Endpoints

\* \*\*POST `/api/auth/forgot-password`\*\*

&#x20;   \* Input: `{ email: string }`

&#x20;   \* Logic: Validation -> Token Gen -> DB Update -> Email Dispatch.

\* \*\*POST `/api/auth/reset-password`\*\*

&#x20;   \* Input: `{ token: string, newPassword: string }`

&#x20;   \* Logic: Token Verification -> Password Hashing -> DB Update -> Invalidate Token.



\## 3. Data Flow

1\. Request -> `AuthController`

2\. `AuthController` -> `ValidationMiddleware`

3\. `ValidationMiddleware` -> `PasswordResetService`

4\. `PasswordResetService` -> `UserRepository` (DB) \& `EmailService` (Nodemailer)

