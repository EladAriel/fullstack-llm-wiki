---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/hello.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================

# hello (database command)

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
     hello: 1 
   } 
)
```

The :dbcommand:`hello` command accepts optional fields `saslSupportedMechs: <db.user>` to return an additional field `hello.saslSupportedMechs` in its result and `comment <any>` to add a log comment associated with the command.

```javascript
db.runCommand( 
   { 
     hello: 1, 
     saslSupportedMechs: "<db.username>", 
     comment: <any> 
   } 
)
```

The :method:`db.hello()` method in :binary:`~bin.mongosh` provides a wrapper around :dbcommand:`hello`.

## Behavior

### Client Disconnection

.. include:: /includes/extracts/4.2-changes-disconnect.rst

## Output

### All Instances

The following :dbcommand:`hello` fields are common across all roles:

### Sharded Instances

:binary:`~bin.mongos` instances add the following field to the :dbcommand:`hello` response document:

### Replica Sets

:dbcommand:`hello` contains these fields when returned by a member of a replica set:

For details on the `ok` status field, the `operationTime` field, and the `$clusterTime` field, see `Command Response <command-response>`.
