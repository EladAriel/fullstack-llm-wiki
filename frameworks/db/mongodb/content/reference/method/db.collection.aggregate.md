---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.aggregate.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================================

# db.collection.aggregate() (mongosh method)

.. include:: /includes/wayfinding/mongosh-method-aggregate.rst

## Definition

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

`db.collection.aggregate()` has the following form:

```javascript
db.collection.aggregate( <pipeline>, <options> )
```

### Parameters

`db.collection.aggregate()` takes the following parameters:

## Behavior

### Error Handling

.. include:: /includes/fact-agg-helper-exception.rst

### Cursor Behavior

In :binary:`~bin.mongosh`, if the `aggregate()` cursor is not assigned to a variable using the `var` keyword, :binary:`~bin.mongosh` automatically iterates the cursor up to 20 times. See `/tutorial/iterate-a-cursor` for handling cursors in :binary:`~bin.mongosh`.

Cursors returned from aggregation only supports cursor methods that operate on evaluated cursors (i.e. cursors whose first batch has been retrieved), such as the following methods:

For more information, see:

- `aggregation-pipeline`
- `/reference/aggregation`
- `/core/aggregation-pipeline-limits`
- :dbcommand:`aggregate`
### Sessions

For cursors created inside a session, you cannot call :dbcommand:`getMore` outside the session.

Similarly, for cursors created outside of a session, you cannot call :dbcommand:`getMore` inside a session.

Session Idle Timeout ````````````````````

.. include:: /includes/extracts/sessions-cursor-timeout.rst

For operations that return a cursor, if the cursor may be idle for longer than 30 minutes, issue the operation within an explicit session using :method:`Mongo.startSession()` and periodically refresh the session using the :dbcommand:`refreshSessions` command. See :limit:`Session Idle Timeout` for more information.

### Transactions

.. include:: /includes/extracts/transactions-supported-operation.rst

However, the following stages are not allowed within transactions:

- :pipeline:`$collStats`
- :pipeline:`$currentOp`
- :pipeline:`$indexStats`
- :pipeline:`$listLocalSessions`
- :pipeline:`$listSessions`
- :pipeline:`$out`
- :pipeline:`$merge`
- :pipeline:`$planCacheStats`
You also cannot specify the `explain` option.

.. include:: /includes/extracts/transactions-operations-getMore.rst

.. include:: /includes/extracts/transactions-usage.rst

### Client Disconnection

For `aggregate()` operations that do not include the :pipeline:`$out` or :pipeline:`$merge` stages:

.. include:: /includes/extracts/4.2-changes-disconnect.rst

### Query Settings

.. include:: /includes/persistent-query-settings-info-for-queries.rst

## Examples

.. include:: /includes/sample-data-usage.rst

.. include:: /includes/sample-data-additional-fields-note.rst

.. include:: /includes/agg-sample-documents.rst

### Group by and Calculate a Sum

The following aggregation operation:

- Selects movies with an IMDB rating greater than 8.5
- Groups the matching movies by the `year` field
- Calculates the `averageRating` for each `year` from the average of the
`imdb.rating` field

- Sorts the results by the `averageRating` field in descending order
The operation returns a cursor with the following documents:

.. include:: /includes/note-mongo-shell-automatically-iterates-cursor.rst

### Return Information on Aggregation Pipeline Operation

The following example uses :method:`db.collection.explain()` to view detailed information regarding the execution plan of the aggregation pipeline.

The operation returns a document that details the processing of the aggregation pipeline. For example, the document may show, among other details, which index, if any, the operation used. [#agg-index-filters]_ If the `movies` collection is a sharded collection, the document also shows the division of labor between the shards and the merge operation, and for targeted queries, the targeted shards.

> **Note:** not machines, and the output format is subject to change between
releases.

You can view more verbose explain output by passing the `executionStats` or `allPlansExecution` explain modes to the :method:`db.collection.explain()` method.

used. See `index-filters` for details.

### Interaction with `allowDiskUseByDefault`

.. include:: /includes/fact-allowDiskUseByDefault.rst

.. include:: /includes/extracts/4.2-changes-usedDisk.rst

For more information, see `agg-pipeline-limits`.

### Specify an Initial Batch Size

To specify an initial batch size for the cursor, use the following syntax for the `cursor` option:

```javascript
cursor: { batchSize: <int> }
```

For example, the following aggregation operation specifies the initial batch size of `0` for the cursor:

.. include:: /includes/batch-size-aggregate.rst

.. include:: /includes/note-mongo-shell-automatically-iterates-cursor.rst

### Specify a Collation

.. include:: /includes/extracts/collation-description.rst

.. include:: /includes/collation-agg-example.rst

> **Note:** .. include:: /includes/extracts/views-collation-agg.rst

For descriptions on the collation fields, see `collation-document-fields`.

### Hint an Index

.. include:: /includes/hint-index-agg-example.rst

### Override `readConcern`

.. include:: /includes/override-readconcern-agg.rst

### Specify a Comment

The `movies` collection in the `sample_mflix` sample dataset contains documents similar to this one:

```javascript
{ 
   title: 'Forrest Gump', 
   year: 1994, 
   genres: [ 'Drama', 'Romance' ], 
   runtime: 142,
   imdb: { rating: 8.8, votes: 1087227, id: 109830 },
   directors: [ 'Robert Zemeckis' ],
   cast: [ 'Tom Hanks', 'Rebecca Williams', 'Sally Field', 'Michael Conner Humphreys' ],
}
```

The following aggregation operation finds movies created in 1994 and includes the `comment` option to provide tracking information in the `logs`, the `db.system.profile` collection, and `db.currentOp`.

On a system with profiling enabled, you can then query the `system.profile` collection to see all recent similar aggregations, as shown below:

```javascript
db.system.profile.find( { "command.aggregate": "movies", "command.comment" : "match_three_movies_from_1994" } ).sort( { ts : -1 } ).pretty()
```

This will return a set of profiler results in the following format:

```javascript
{
  "op" : "command",
  "ns" : "video.movies",
  "command" : {
    "aggregate" : "movies",
    "pipeline" : [
      {
        "$match" : {
          "year" : 1994
        }
      },
      { "$limit": 3 }
    ],
    "comment" : "match_three_movies_from_1994",
    "cursor" : {

    },
    "$db" : "video"
  },
  ...
}
```

An application can encode any arbitrary information in the comment in order to more easily trace or identify specific operations through the system. For instance, an application might attach a string comment incorporating its process ID, thread ID, client hostname, and the user who issued the command.

### Use Variables in `let`

.. include:: /includes/let-variables-match-note.rst

.. include:: /includes/let-variables-example.rst
