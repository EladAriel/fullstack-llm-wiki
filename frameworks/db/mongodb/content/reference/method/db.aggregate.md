---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.aggregate.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# db.aggregate() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The :method:`db.aggregate()` method has the following syntax:

```javascript
db.aggregate( [ <pipeline> ], { <options> } )
```

> **Note:** :method:`db.aggregate()` can accept the pipeline stages as separate
arguments instead of as elements in an array. If you do
not specify the `pipeline` as an array, you cannot specify the
`options` parameter.

The `pipeline` parameter is an array of stages to execute. The pipeline must start with a compatible stage that does not require an underlying collection, such as :pipeline:`$currentOp` or :pipeline:`$listLocalSessions`.

The `options` document can contain the following fields:

## Example

### Pipeline with `$currentOp`

The following example runs a pipeline with two stages. The first stage runs the :pipeline:`$currentOp` operation and the second stage filters the results of that operation.

```javascript
use admin
db.aggregate( [ { 
   $currentOp : { allUsers: true, idleConnections: true } }, { 
   $match : { shard: "shard01" } 
   }
] )
```
