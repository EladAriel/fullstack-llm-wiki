---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/setIndexCommitQuorum.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================================

# setIndexCommitQuorum (database command)

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
     setIndexCommitQuorum: <string>,
     indexNames: [ <document> ],
     commitQuorum: <int> | <string>,
     comment: <any>
   }     
)
```

## Command Fields

The command takes the following fields:

## Behavior

.. include:: /includes/extracts/4.4-changes-index-builds-simultaneous-fcv.rst

.. include:: /includes/indexes/commit-quorum.rst

Issuing :dbcommand:`setIndexCommitQuorum` has no effect on index builds started with `commitQuorum <createIndexes-cmd-commitQuorum>` of `0`.

> **Important:** Replica set nodes with `buildIndexes <replica-set-configuration-buildIndexes>`
set to `false` can't be included in a commit quorum.

### Commit Quorum Contrasted with Write Concern

.. include:: /includes/indexes/commit-quorum-vs-write-concern.rst

## Examples

.. include:: /includes/extracts/4.4-changes-index-builds-simultaneous.rst

The following operation starts an index build of two indexes:

```javascript
db.getSiblingDB("examples").invoices.createIndexes(
  [
    { "invoices" : 1 },
    { "fulfillmentStatus" : 1 }
  ]
)
```

By default, index builds use `"votingMembers"` commit quorum, or all data-bearing voting replica set members. The following operation modifies the index build commit quorum to `"majority"`, or a simple majority of data-bearing voting members:.

```javascript
db.getSiblingDB("examples").runCommand(
  {
    "setIndexCommitQuorum" : "invoices", 
    "indexNames" : ["invoices_1", "fullfillmentStatus_1"], 
    "commitQuorum" : "majority"
  }
)
```

- The indexes specified to `indexNames` must be the entire set
of in-progress builds associated to a given index builder, i.e. the :method:`~db.collection.createIndexes()` operation.

- The `indexNames` field specifies the names of the indexes. Since
the indexes were created without an explicit name, MongoDB generated an index name by concatenating the names of the indexed fields and the sort order.
