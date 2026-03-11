\# Feature: Password Reset



\## 1. User Story

As a registered user, I want to be able to securely reset my forgotten password so that I can regain access to my account.



\## 2. Acceptance Criteria (EARS Notation)



\### 2.1 Event-Driven

\* \*\*WHEN\*\* the user submits an email address in the "Forgot Password" form, \*\*THE SYSTEM SHALL\*\* validate the email format.

\* \*\*WHEN\*\* a valid, registered email address is submitted, \*\*THE SYSTEM SHALL\*\* generate a secure, unique reset token (JWT) valid for 15 minutes.

\* \*\*WHEN\*\* the token is generated, \*\*THE SYSTEM SHALL\*\* send an email containing a reset link (Format: `https://domain.com/reset?token=XYZ`) to that address.



\### 2.2 Unwanted Behavior

\* \*\*IF\*\* the submitted email format is invalid, \*\*THEN THE SYSTEM SHALL\*\* block the submission and display "Invalid email format".

\* \*\*IF\*\* the email address does not exist in the database, \*\*THEN THE SYSTEM SHALL\*\* still display the generic success message ("If an account exists, an email has been sent") to prevent user enumeration.

\* \*\*IF\*\* the user clicks an expired or tampered reset link, \*\*THEN THE SYSTEM SHALL\*\* deny access and display "The link is invalid or expired".



\### 2.3 State-Driven

\* \*\*WHILE\*\* an active, unused reset token has already been generated for an email in the last 5 minutes, \*\*THE SYSTEM SHALL\*\* block further reset requests for this email (Rate Limiting).

