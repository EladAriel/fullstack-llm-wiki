---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/killAllSessionsByPattern.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===========================================

# killAllSessionsByPattern (database command)

## Definition

## Syntax

The command has the following syntax:

```javascript
db.runCommand( 
   { 
     killAllSessionsByPattern: [ <pattern>, ... ] 
   } 
)
```

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Command Fields

The command takes an array of documents that specify the patterns to match:

Specify an empty array to kill all sessions. [#exception]_

To view existing sessions, see :pipeline:`$listSessions` operation or :pipeline:`$listLocalSessions`.

> **Seealso:** :dbcommand:`killAllSessions`

The |command| operation ignores sessions that have `transactions <transactions>` in prepared state. See `killAllSessionsByPattern-behavior` for details.

## Behavior

.. include:: /includes/note-killSessions.rst

## Access Control

If the deployment enforces authentication/authorization, you must have the :authaction:`killAnySession` privilege action to run the :dbcommand:`killAllSessionsByPattern` command.

For patterns that include `users` or `roles`, you must also have privileges that grant :authaction:`impersonate` action on the cluster resource.

> **Note:** Users can kill their own sessions even without the
:authaction:`killAnySession` privilege action.

## Examples

### Kill All Sessions

The following operation kills all sessions:

```javascript
db.runCommand( { killAllSessionsByPattern: [ ] } )
```

### Kill All Sessions for Specific Users

The following operation kills all sessions that have the specified `uid` and whose owner has the specified role:

```javascript
db.runCommand( { killAllSessionsByPattern: [ 
   { "uid" : BinData(0,"oBRA45vMY78p1tv6kChjQPTdYsnCHi/kA/fFMZTIV1o=") },
   { roles: [ { role: "readWrite", db: "test" } ] }
] } )
```
