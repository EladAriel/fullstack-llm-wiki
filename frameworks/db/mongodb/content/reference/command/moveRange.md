---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/moveRange.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# moveRange (database command)

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
    moveRange: <namespace>,
    toShard: <ID of the recipient shard>,
    min: <min key of the range to move>, // conditional
    max: <max key of the range to move>, // conditional
    forceJumbo: <bool>, // optional
    writeConcern: <write concern>, // optional
    secondaryThrottle: <bool> // optional
  } 
)
```

.. include:: /includes/retrieve-shard-id-note.rst

## Command Fields

The command takes the following fields:

The `range migration <sharding-chunk-migration>` section describes how ranges move between shards on MongoDB.

## Considerations

Only use the :dbcommand:`moveRange` in scenarios like:

- an initial ingestion of data
- a large bulk import operation
Allow the balancer to create and balance ranges in sharded clusters in most cases.

> **Seealso:** `<create-chunks-in-a-sharded-cluster>`

## Examples

The following examples use a collection with:

- Shard key `x`
- Configured chunk size of 128MB
- A chunk with boundaries: `[x: 0, x: 100)`
### Specify both `min` and `max`

The following table lists the results of setting `min` and `max` to various values:

### Specify `min` but not `max`

The following table lists the results of setting `min` to various values:

### Specify `max` but not `min`

The following table lists the results of setting `max` to various values:
