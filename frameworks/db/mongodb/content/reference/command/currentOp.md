---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/currentOp.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# currentOp (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand(
   { 
     currentOp: 1 
   }
)
```

> **Note:** .. include:: /includes/5.0-fact-currentop.rst

## Behavior

`currentOp` must run against the `admin` database, and it can accept several optional fields.

`currentOp` and the `database profiler<profiler>` report the same basic diagnostic information for CRUD operations, including the following:

.. include:: /includes/fact-diagnostic-info.rst

### Redaction

When using `Queryable Encryption <qe-manual-feature-qe>`, `currentOp` operations with the `encryptionInformation` option redact certain information:

- The output omits all fields after `"command"`.
- The output redacts `"command"` to include only the first element,
`$comment`, and `$db`.

## Access Control

On systems running with :setting:`~security.authorization`, the user must have access that includes the :authaction:`inprog` privilege action.

Users can use `$ownOps` on :binary:`~bin.mongod` instances to view their own operations without the :authaction:`inprog` privilege action.

```javascript
db.adminCommand( { currentOp: 1, "$ownOps": 1 } )
```

> **Seealso:**  `create-role-to-manage-ops`

## Examples

The following examples use the `currentOp` command with various query documents to filter the output.

### Display All Current Operations

```javascript
db.adminCommand(
   {
     currentOp: true,
     "$all": true
   }
)
```

sure that you also update the examples on db.currentOp (the equiv. method). Single sourcing is weird due to diffs in code block. - ARM

### Write Operations Waiting for a Lock

The following example returns information on all write operations that are waiting for a lock:

```javascript
db.adminCommand(
   {
     currentOp: true,
     "waitingForLock" : true,
     $or: [
        { "op" : { "$in" : [ "insert", "update", "remove" ] } },
        { "command.findandmodify": { $exists: true } }
    ]  
   }
)
```

### Active Operations with no Yields

The following example returns information on all active running operations that have never yielded:

```javascript
db.adminCommand(
   {
     currentOp: true,
     "active" : true,
     "numYields" : 0,
     "waitingForLock" : false
   }
)
```

### Active Operations on a Specific Database

The following example returns information on all active operations for database `db1` that have been running longer than 3 seconds:

```javascript
db.adminCommand(
   {
     currentOp: true,
     "active" : true,
     "secs_running" : { "$gt" : 3 },
     "ns" : /^db1\./
   }
)
```

### Active Indexing Operations

The following example returns information on index creation operations:

```javascript
db.getSiblingDB("admin").aggregate( [
   { $currentOp : { idleConnections: true } },
   { $match: {
         $or: [
            { "op": "command", "command.createIndexes": { $exists: true } },
            { "op": "none", "msg": /^Index Build/ }
         ]
     }
   }
] )
```

MongoDB marks index builds waiting on commit quorum to complete the operation as an idle connection by setting the `active` field to `false`. The `idleConnections: true` setting includes these idle connections in the `$currentOp` output.

## Output Example

.. include:: /includes/currentOp-output-example.rst

## Specific Output Examples

.. include:: /includes/metrics/txt-section-intro.rst

.. include:: /includes/metrics/ex-resharding.rst

## Output Fields
