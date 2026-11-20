# Tasks: Health Check Implementation

## Planned 📋
- [ ] **Task 1: Health Service & Probe** ← design.md §1, §3, requirements §2.1-§2.2
    - [ ] Implement `DatabaseProbe.run()` with a 1 second timeout.
    - [ ] Implement `HealthService.check()` returning a Health_Report (bouncer pattern: shutdown check first).
    - [ ] Make sure no exception text ends up in the report.
- [ ] **Task 2: Endpoint** ← design.md §2, requirements §2.1
    - [ ] Implement `GET /health` in `HealthController`.
    - [ ] Map the report status to HTTP `200` / `503`.
- [ ] **Task 3: Shutdown State** ← design.md §1, requirements §2.3
    - [ ] Add the `SHUTTING_DOWN` event and set it in the signal handler.
    - [ ] Make `HealthService` return `shutting_down` without running the probe.
- [ ] **Task 4: Testing** ← requirements §2 (all EARS criteria)
    - [ ] Unit tests for each row of the error table in design.md §3.
    - [ ] Test that the response never contains exception text, hostnames or versions.

## Task Dependency Graph

```json
{
  "waves": [
    { "id": 0, "tasks": ["1"] },
    { "id": 1, "tasks": ["2", "3"] },
    { "id": 2, "tasks": ["4"] }
  ]
}
```
