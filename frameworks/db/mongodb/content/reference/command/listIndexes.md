---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/listIndexes.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# listIndexes (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand ( 
   {
      listIndexes: "<collection-name>", 
      cursor: { batchSize: <int> },
      comment: <any>
   } 
)
```

## Command Fields

The command takes the following fields:

## Required Access

If access control is enforced, the built-in :authrole:`read` role provides the required privileges to run :dbcommand:`listIndexes` for the collections in a database.

## Behavior

### {+fts+} Indexes

`listIndexes` does not return information on :atlas:`{+fts+} indexes </atlas-search/atlas-search-overview/#fts-indexes>`. Instead, use :pipeline:`$listSearchIndexes`.

### Client Disconnection

.. include:: /includes/extracts/4.2-changes-disconnect.rst

### Replica Set Member State Restriction

.. include:: /includes/extracts/4.4-changes-repl-state-restrictions-operation.rst

### Wildcard Indexes

.. include:: /includes/indexes/fact-wildcard-index-ordering.rst

## Output

## Examples

### List Database Indexes

This example lists indexes for the `contacts` collection without specifying the cursor batch size.

### Specify Result Batch Size

This example lists indexes for the `contacts` collection, and specifies a cursor batch size of 1.

### Retrieve Additional Results

This example uses `getMore` to retrieve additional result batches from the `contacts` collection.
