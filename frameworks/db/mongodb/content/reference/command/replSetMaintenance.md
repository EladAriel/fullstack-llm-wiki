---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/replSetMaintenance.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================================

# replSetMaintenance (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

.. include:: /includes/fact-environments-no-atlas-support.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   { 
     replSetMaintenance: <boolean> 
   }
)
```

## Behavior

Consider the following behavior when running the :dbcommand:`replSetMaintenance` command:

- You cannot run the command on the Primary.
- You must run the command against the `admin` database.
- When enabled `replSetMaintenance: true`, the member enters the
`RECOVERING` state. While the secondary is `RECOVERING`:

- The member is not accessible for read operations.
- The member continues to sync its `oplog` from the Primary.
- When a node receives a `replSetMaintenance: true` request, it
adds a maintenance mode task to a queue of tasks. If the queue of tasks was empty and now is not, the node will transition to `RECOVERING` state and begin to reject read requests. When a node receives a `replSetMaintenance: false` request, it removes a maintenance mode task from the queue (even if that task was initiated by a different client). If the request empties the maintenance mode task queue, the node will return to `SECONDARY` state.

- If you want to prevent a node from servicing reads, consider using
`/core/replica-set-hidden-member` instead.
