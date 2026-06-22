---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/killAllSessions.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# killAllSessions (database command)

## Definition

## Syntax

The command has the following syntax:

```javascript
db.runCommand( 
   { 
     killAllSessions: [ { user: <user>, db: <dbname> }, ... ]  
   } 
)
```

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

.. include:: /includes/fact-environments-no-atlas-support.rst

## Command Fields

The command takes an array of documents where each document specifies the user and the user's authentication database. Specify an empty array to kill all sessions for all users in the system. [#exception]_

## View Existing Sesssions

To view existing sessions, see :pipeline:`$listSessions` operation or :pipeline:`$listLocalSessions`.

> **Seealso:** :dbcommand:`killAllSessionsByPattern`

The |command| operation ignores sessions that have `transactions <transactions>` in prepared state. See `killAllSessions-behavior` for details.

## Access Control

If the deployment enforces authentication/authorization, you must have the :authaction:`killAnySession` to run the :dbcommand:`killAllSessions` command.

> **Note:** Users can kill their own sessions even without
:authaction:`killAnySession` privilege action.

## Behavior

.. include:: /includes/note-killSessions.rst

## Examples

### Kill All Sessions

The following operation kills all sessions for all users in the system:

```javascript
db.runCommand( { killAllSessions: [ ] } )
```

### Kill All Sessions for Specific Users

The following operation kills all sessions for the user `appReader` in the `db1` and the user `reportWriter` in `db2` databases:

```javascript
db.runCommand( { killAllSessions: [ 
   { user: "appReader", db: "db1" },
   { user: "reportWriter", db: "db2" }
] } )
```
