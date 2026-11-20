# Design: Health Check

## 1. Architectural Decisions

* **Pattern:** Service-Layer Pattern. Logic resides in `HealthService`, the route only translates the result into HTTP.
* **No authentication:** load balancers must be able to call it. Therefore the response contains no internal details (requirements §2.2).
* **No caching:** the endpoint must reflect the current state. The Database_Probe has its own 1 second timeout so a slow database cannot hold the endpoint open.
* **Shutdown flag:** a process-wide `threading.Event` (`SHUTTING_DOWN`) set by the signal handler. It is read by `HealthService`, never written by it.

## 2. API Endpoint

* **GET `/health`**
    * Input: none
    * Logic: Shutdown check -> Database_Probe -> Health_Report -> HTTP status.
    * Output (`200`): `{ "status": "ok", "checks": { "database": "ok" } }`
    * Output (`503`): `{ "status": "unavailable", "checks": { "database": "fail" } }`

## 3. Data Flow

### Happy Path
1. Request → `HealthController`
2. `HealthController` → `HealthService.check()`
3. `HealthService` → `DatabaseProbe.run()` (timeout 1 s)
4. Response: `200 OK` with Health_Report

### Error & Edge Case Flows
| Scenario | Where caught | HTTP Code | Response |
|---|---|---|---|
| Database unreachable | `HealthService` (EAFP, catches probe error) | `503` | `"status": "unavailable"`, log `ERROR` with trace |
| Probe exceeds 1 s | `DatabaseProbe` (timeout) | `503` | `"status": "unavailable"`, log `ERROR` |
| Unexpected exception in check | `HealthController` | `503` | `"status": "unavailable"`, log `ERROR` with trace |
| Application is shutting down | `HealthService` (bouncer, first check) | `503` | `"status": "shutting_down"`, no probe |

> **Note:** `500` is deliberately not used. A failing health check is a service availability problem (`503`), not a genuine system failure (global rules, error handling).

## 4. Logging

* `DEBUG`: successful probe with duration.
* `ERROR`: failed probe or unexpected exception, including the exception. Never in the response body.
