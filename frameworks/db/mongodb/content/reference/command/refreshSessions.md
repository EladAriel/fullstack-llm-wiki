---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/refreshSessions.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# refreshSessions (database command)

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
     refreshSessions: [ 
       { id : <UUID> }, ... 
     ] 
   } 
 )
```

.. include:: /includes/fact-dbcommand.rst

```javascript
db.runCommand( 
   { 
     refreshSessions: [ 
       { id : <UUID> }, ... 
     ] 
   } 
)
```

## Behavior

### Session Identification

MongoDB concatenates each of the specified UUIDs with the hash of the authenticated user credentials to identify the user's sessions to refresh. If the user has no session that match, the :dbcommand:`refreshSessions` has no effect.

## Access Control

If the deployment enforces authentication/authorization, you must be authenticated to run the :dbcommand:`refreshSessions` command.

A user can only refresh sessions belonging to the user.

> **Seealso:** - :dbcommand:`startSession`
- :pipeline:`$listLocalSessions`
-  :pipeline:`$listSessions`
