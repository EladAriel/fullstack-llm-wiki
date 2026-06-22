---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/killSessions.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# killSessions (database command)

## Definition

## Syntax

The command has the following syntax:

```javascript
db.runCommand( 
   { 
     killSessions: [ { id : <UUID> }, ... ] 
   } 
)
```

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Command Fields

The command takes an array of documents that specify the UUID portion of the session id. Specify an empty array `[ ]` to kill all sessions, or if access control is enabled, all sessions owned by the user. [#exception]_

## View Existing Sessions

To view existing sessions, see :pipeline:`$listSessions` operation or :pipeline:`$listLocalSessions`.

The |command| operation ignores sessions that have `transactions <transactions>` in prepared state. See `killSessions-behavior` for details.

## Behavior

### Session Identification

MongoDB concatenates each of the specified UUIDs with the hash of the authenticated user credentials to identify the user's sessions to kill. If the user has no session that match, the :dbcommand:`killSessions` has no effect.

.. include:: /includes/note-killSessions.rst

## Example

The following operation kills the specified session for the user:

```javascript
db.runCommand( { killSessions: [ { id: UUID("f9b3d8d9-9496-4fff-868f-04a6196fc58a") } ] } )
```

> **Seealso:** `kill-write-ops-sharded-cluster`
