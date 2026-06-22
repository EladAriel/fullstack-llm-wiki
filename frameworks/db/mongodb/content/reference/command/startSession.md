---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/startSession.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# startSession (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   { 
     startSession: 1
   }
)
```

.. include:: /includes/fact-dbcommand.rst

```javascript
db.runCommand( 
   { 
     startSession: 1 
   } 
)
```

> **Important:** `featureCompatibilityVersion` must be 3.6 or greater to use the
:dbcommand:`startSession` command.

> **Seealso:** :method:`Mongo.startSession()`

## Behavior

If the deployment enforces authentication/authorization, you must be authenticated to run the :dbcommand:`startSession` command. The user who runs :dbcommand:`startSession` owns the created session, and only that user can use the session.

If the deployment does not enforce authentication/authorization, a created session has no owner and can be used by any user on any connection. If the user authenticates and creates a session for a deployment that does not enforce authentication/authorization, the user owns the session. However, any user on any connection may use the session.

If the deployment transitions to auth without any downtime, any sessions without an owner cannot be used.

.. include:: /includes/client-sessions-reuse.rst

## Output

In addition to the status and operation time of the command, the :dbcommand:`startSession` returns the following session specific information:
