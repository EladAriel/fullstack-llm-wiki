---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/cleanupOrphaned.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# cleanupOrphaned (database command)

> **Important:** Starting in MongoDB 6.0.3, run an aggregation using the
:pipeline:`$shardedDataDistribution` stage to confirm no orphaned documents
remain. For details, see `shardedDataDistribution-no-orphaned-docs`.

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand( 
  {
    cleanupOrphaned: "<database>.<collection>",
    startingFromKey: <minimumShardKeyValue>, // deprecated
    secondaryThrottle: <boolean>, // deprecated
    writeConcern: <document> // deprecated
  } 
)
```

### Command Fields

`cleanupOrphaned` has the following fields:

## Behavior

### Determine Range

The value of this field is not used to determine the bounds of the cleanup range. The `cleanupOrphaned` command waits until all orphaned documents in all ranges in the namespace are cleaned up from the shard before completing, regardless of the presence of or value of `startingFromKey`.

## Required Access

On systems running with :setting:`~security.authorization`, you must have :authrole:`clusterAdmin` privileges to run `cleanupOrphaned`.

## Output

### Return Document

Each `cleanupOrphaned` command returns a document containing a subset of the following fields:
