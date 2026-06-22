---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/rest-api/objects/state-machine.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

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
url: '/operate/rs/7.8/references/rest-api/objects/state-machine/'
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
