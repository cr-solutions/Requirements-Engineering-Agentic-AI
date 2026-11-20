# Feature: Password Reset

## 1. User Story

As a registered user, I want to be able to securely reset my forgotten password so that I can regain access to my account.

## 1.1 Glossary

Named entities used in the acceptance criteria below. Using exact names removes ambiguity for the agent.

* **Auth_Controller**: HTTP layer that exposes `/api/auth/forgot-password` and `/api/auth/reset-password`.
* **Reset_Service**: Service-layer class (`PasswordResetService`) that owns all reset logic.
* **Reset_Token**: Signed JWT that authorizes exactly one password change.
* **Mailer**: Component that sends e-mails (`EmailService`).
* **Forgot_Form**: Frontend form in which the user submits an e-mail address.

## 2. Acceptance Criteria (EARS Notation)

### 2.1 Event-Driven

* **WHEN** the user submits an email address in the Forgot_Form, **THE Auth_Controller SHALL** validate the email format.
* **WHEN** a valid, registered email address is submitted, **THE Reset_Service SHALL** generate a Reset_Token valid for 15 minutes.
* **WHEN** the Reset_Token is generated, **THE Mailer SHALL** send an email containing a reset link (Format: `https://domain.com/reset?token=XYZ`) to that address.

### 2.2 Unwanted Behavior

* **IF** the submitted email format is invalid, **THEN THE Auth_Controller SHALL** block the submission and display "Invalid email format".
* **IF** the email address does not exist in the database, **THEN THE Reset_Service SHALL** still return the generic success message ("If an account exists, an email has been sent") to prevent user enumeration.
* **IF** the user clicks an expired or tampered reset link, **THEN THE Reset_Service SHALL** deny access and display "The link is invalid or expired".

### 2.3 State-Driven

* **WHILE** an active, unused Reset_Token has already been generated for an email in the last 5 minutes, **THE Reset_Service SHALL** block further reset requests for this email (Rate Limiting).
