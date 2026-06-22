---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.currentOp.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# db.currentOp() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

### Syntax

:method:`db.currentOp()` has the following form:

```javascript
db.currentOp(<operations>)
```

:method:`db.currentOp()` can take the following optional argument:

## Behavior

:method:`db.currentOp()` can accept a filter document or a boolean parameter.

If you pass a filter document to :method:`db.currentOp()`, the output returns information only for the current operations that match the filter. The filter document can contain:

Passing in `true` to :method:`db.currentOp()` is equivalent to passing in a document of `{ "$all": true }`. The following operations are equivalent:

```javascript
db.currentOp(true)
db.currentOp( { "$all": true } )
```

:method:`db.currentOp` and the `database profiler <database-profiler>` report the same basic diagnostic information for all CRUD operations, including the following:

.. include:: /includes/fact-diagnostic-info.rst

## Access Control

On systems running with :setting:`~security.authorization`, the user must have access that includes the :authaction:`inprog` privilege action.

Users can run `db.currentOp( { "$ownOps": true } )` on :binary:`~bin.mongod` instances to view their own operations even without the :authaction:`inprog` privilege action.

> **Seealso:** `create-role-to-manage-ops`

## Examples

The following examples use the :method:`db.currentOp()` method with various query documents to filter the output.

sure that you also update the examples on currentOp (the equiv. command). Single sourcing is weird due to diffs in code block. - ARM

### Write Operations Waiting for a Lock

The following example returns information on all write operations that are waiting for a lock:

```javascript
db.currentOp(
   {
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
db.currentOp(
   {
     "active" : true,
     "numYields" : 0,
     "waitingForLock" : false
   }
)
```

### Active Operations on a Specific Database

The following example returns information on all active operations for database `db1` that have been running longer than 3 seconds:

```javascript
db.currentOp(
   {
     "active" : true,
     "secs_running" : { "$gt" : 3 },
     "ns" : /^db1\./
   }
)
```

### Active Indexing Operations

The following example returns information on index creation operations on any number of fields:

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

## Output Example

The following is a prototype of :method:`db.currentOp()` output.

.. include:: /includes/currentOp-output-example.rst

## Specific Output Examples

.. include:: /includes/metrics/txt-section-intro.rst

.. include:: /includes/metrics/ex-resharding.rst

## Output Fields

For a complete list of :method:`db.currentOp()` output fields, see `currentOp <currentOp-stage-output-fields>`.
