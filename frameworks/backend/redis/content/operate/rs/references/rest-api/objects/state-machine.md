---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/rest-api/objects/state-machine.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.579712Z"
---
# State Machine

---
Title: State machine object
alwaysopen: false
categories:
- docs
- operate
- rs
description: An object that represents a state machine.
linkTitle: state-machine
weight: $weight
---

A state machine object tracks the status of database actions.

A state machine contains the following attributes:

| Name        | Type/Value | Description |
|-------------|------------|-------------|
| action_uid  | string     | A globally unique identifier of the action |
| object_name | string     | Name of the object being manipulated by the state machine |
| status      | pending    | Requested state machine has not started |
|             | active     | State machine is currently running |
|             | completed  | Operation complete |
|             | failed     | Operation or state machine failed |
| name        | string     | Name of the running (or failed) state machine |
| state       | string     | Current state within the state machine, when known |
| error       | string     | A descriptive error string for failed state machine, when known |
