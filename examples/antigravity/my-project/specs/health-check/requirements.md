# Feature: Health Check

## 1. User Story

As an operator, I want a lightweight health endpoint so that load balancers and monitoring can tell whether the application is able to serve traffic.

## 1.1 Glossary

* **Health_Endpoint**: Unauthenticated HTTP endpoint `GET /health`.
* **Health_Service**: Service-layer class (`HealthService`) that runs the checks and builds the Health_Report.
* **Database_Probe**: A trivial read (`SELECT 1`) against the primary database, with a timeout of 1 second.
* **Health_Report**: JSON body returned by the Health_Endpoint.
* **Shutdown_State**: Application state after a termination signal was received, while in-flight requests are drained.

## 2. Acceptance Criteria (EARS Notation)

### 2.1 Event-Driven

* **WHEN** a client sends `GET /health`, **THE Health_Endpoint SHALL** respond within 2 seconds.
* **WHEN** the Database_Probe succeeds, **THE Health_Endpoint SHALL** respond with `200` and a Health_Report with `"status": "ok"`.

### 2.2 Unwanted Behavior

* **IF** the Database_Probe fails or exceeds its timeout, **THEN THE Health_Endpoint SHALL** respond with `503` and a Health_Report with `"status": "unavailable"`, and **THE Health_Service SHALL** log the failure with level `ERROR`.
* **IF** the Health_Service raises an unexpected exception, **THEN THE Health_Endpoint SHALL** respond with `503` (not `500`), because the instance must be taken out of rotation.
* **IF** a Health_Report is built, **THEN THE Health_Service SHALL NOT** include exception messages, hostnames, credentials or version numbers in it.

### 2.3 State-Driven

* **WHILE** the application is in the Shutdown_State, **THE Health_Endpoint SHALL** respond with `503` and `"status": "shutting_down"` without running the Database_Probe.
