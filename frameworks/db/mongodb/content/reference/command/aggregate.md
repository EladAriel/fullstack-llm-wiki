---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/aggregate.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# aggregate (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-limited-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

.. versionchanged:: 5.0

The command has the following syntax:

```javascript
db.runCommand(
   {
     aggregate: "<collection>" || 1,
     pipeline: [ <stage>, <...> ],
     explain: <boolean>,
     allowDiskUse: <boolean>,
     cursor: <document>,
     maxTimeMS: <int>,
     bypassDocumentValidation: <boolean>,
     readConcern: <document>,
     collation: <document>,
     hint: <string or document>,
     comment: <any>,
     writeConcern: <document>,
     let: <document> // Added in MongoDB 5.0
   }
)
```

### Command Fields

The :dbcommand:`aggregate` command takes the following fields as arguments:

.. include:: /includes/deprecation-aggregate-wo-cursor.rst

For more information about the aggregation pipeline, see:

- `aggregation-pipeline`
- `/reference/aggregation`
- `/core/aggregation-pipeline-limits`
## Sessions

For cursors created inside a session, you cannot call :dbcommand:`getMore` outside the session.

Similarly, for cursors created outside of a session, you cannot call :dbcommand:`getMore` inside a session.

### Session Idle Timeout

.. include:: /includes/extracts/sessions-cursor-timeout.rst

If the cursor may be idle for longer than 30 minutes, issue the operation within an explicit session using :method:`Mongo.startSession()`. Periodically refresh the session using the :dbcommand:`refreshSessions` command. See :limit:`Session Idle Timeout` for more information.

## Transactions

.. include:: /includes/extracts/transactions-supported-operation.rst

However, the following stages are not allowed within transactions:

- :pipeline:`$collStats`
- :pipeline:`$currentOp`
- :pipeline:`$indexStats`
- :pipeline:`$listLocalSessions`
- :pipeline:`$listSessions`
- :pipeline:`$merge`
- :pipeline:`$out`
- :pipeline:`$planCacheStats`
- :pipeline:`$unionWith`
You also cannot specify the `explain` option.

.. include:: /includes/extracts/transactions-operations-getMore.rst

.. include:: /includes/extracts/transactions-usage.rst

### Client Disconnection

For :dbcommand:`aggregate` operations that do not include the :pipeline:`$out` or :pipeline:`$merge` stages:

.. include:: /includes/extracts/4.2-changes-disconnect.rst

## Query Settings

.. include:: /includes/persistent-query-settings-info-for-queries.rst

## Stable API

When using `Stable API <stable-api>` V1:

- You cannot use the following stages in an :dbcommand:`aggregate`
command:

.. include:: /includes/aggregation/stable-api-unsupported-stages.rst

- Don't include the `explain` field in an :dbcommand:`aggregate`
command. If you do, the server returns an `APIStrictError <api-strict-resp>` error.

- When using the :pipeline:`$collStats` stage, you can only use the
`count` field. No other :pipeline:`$collStats` fields are available.

## Example

.. include:: /includes/deprecation-aggregate-wo-cursor.rst

Instead of running the :dbcommand:`aggregate` command directly, use the :method:`db.collection.aggregate()` helper in :binary:`~bin.mongosh` or the equal helper in your driver.

Except for the first two examples that demonstrate the command syntax, the examples on this page use the :method:`db.collection.aggregate()` helper.

.. include:: /includes/sample-data-usage.rst

### Aggregate Data with Multi-Stage Pipeline

The `movies` collection in the `sample_mflix` database contains documents like these:

.. include:: /includes/sample-data-additional-fields-note.rst

.. include:: /includes/agg-sample-documents.rst

The following example aggregates the `movies` collection to calculate the count of each distinct genre:

In :binary:`~bin.mongosh`, run the same aggregation using the :method:`db.collection.aggregate()` helper:

### Use $currentOp on an Admin Database

The following example runs a two-stage pipeline on the admin database. The first stage executes the :pipeline:`$currentOp` operation, and the second stage filters the results.

> **Note:** The :dbcommand:`aggregate` command does not specify a collection
and instead takes the form `{aggregate: 1}`. The initial
:pipeline:`$currentOp` stage does not draw input from a
collection. The stage produces its own data for the rest of the
pipeline to use.
The :method:`db.aggregate()` helper supports collectionless
aggregations such as this. Run the above aggregation like
`this <admin-pipeline-currentOp>` example.

### Return Information on the Aggregation Operation

The following example sets `explain` to `true` to return information about the aggregation.

> **Note:**

### Interaction with `allowDiskUseByDefault`

.. include:: /includes/fact-allowDiskUseByDefault.rst

.. include:: /includes/extracts/4.2-changes-usedDisk.rst

### Aggregate Data Specifying Batch Size

To set an initial batch size, include the `batchSize` in the `cursor` field:

.. include:: /includes/batch-size-aggregate.rst

### Specify a Collation

.. include:: /includes/extracts/collation-description.rst

.. include:: /includes/collation-agg-example.rst

For descriptions of the collation fields, see `collation-document-fields`.

### Hint an Index

.. include:: /includes/hint-index-agg-example.rst

### Override Default Read Concern

.. include:: /includes/override-readconcern-agg.rst

### Use Variables in `let`

.. include:: /includes/let-variables-match-note.rst

The `movies` collection in the `sample_mflix` database contains documents like this one:

```javascript
{
   title: "The Shawshank Redemption", 
   year: 1994,
   rated: "R",
   imdb: { rating: 9.3, votes: 1513145, id: 111161 },
   runtime: 142
}
```

The following example uses the `let` option to define variables for the pipeline. The example finds movies with high ratings and long runtimes:

## Learn More

- :method:`db.collection.aggregate()`
- `agg-pipeline-limits`
