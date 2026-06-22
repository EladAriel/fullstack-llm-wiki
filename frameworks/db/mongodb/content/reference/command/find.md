---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/find.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================

# find (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-limited-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The :dbcommand:`find` command has the following syntax:

.. versionchanged:: 5.0

```javascript
db.runCommand(
   {
      find: <string>,
      filter: <document>,
      sort: <document>,
      projection: <document>,
      hint: <document or string>,
      skip: <int>,
      limit: <int>,
      batchSize: <int>,
      singleBatch: <bool>,
      comment: <any>,
      maxTimeMS: <int>,
      readConcern: <document>,
      max: <document>,
      min: <document>,
      returnKey: <bool>,
      showRecordId: <bool>,
      tailable: <bool>,
      oplogReplay: <bool>,
      noCursorTimeout: <bool>,
      awaitData: <bool>,
      allowPartialResults: <bool>,
      collation: <document>,
      allowDiskUse : <bool>,
      let: <document> // Added in MongoDB 5.0
   }
)
```

> **Note:** Since MongoDB 4.4, the `find` command ignores the
`oplogReplay` flag. If set, the server accepts it for backwards
compatibility but ignores it.

### Command Fields

The command accepts the following fields:

### Output

The command returns a document with cursor information, including the `cursor ID <cursor-id>` and the first batch of documents. The following example shows the output when run against a sharded collection:

```javascript
{
   "cursor" : {
      "firstBatch" : [
         {
            "_id" : ObjectId("5e8e2ca217b5324fa9847435"),
            "zipcode" : "20001",
            "x" : 1
         },
         {
            "_id" : ObjectId("5e8e2ca517b5324fa9847436"),
            "zipcode" : "30001",
            "x" : 1
         }
      ],
      "partialResultsReturned" : true, 
      "id" : Long("668860441858272439"),
      "ns" : "test.contacts"
   },
   "ok" : 1,
   "operationTime" : Timestamp(1586380205, 1),
   "$clusterTime" : {
      "clusterTime" : Timestamp(1586380225, 2),
      "signature" : {
         "hash" : BinData(0,"aI/jWsUVUSkMw8id+A+AVVTQh9Y="),
         "keyId" : Long("6813364731999420435")
      }
   }
}
```

In addition to the preceding :dbcommand:`find`-specific fields, :method:`db.runCommand()` includes the following information for replica sets and sharded clusters:

- `$clusterTime`
- `operationTime`
See `db.runCommand() Results <command-response>` for details.

If you don't require a raw command response, use the :method:`db.collection.find()` or  :method:`db.collection.findOne()` helper methods.

## Behavior

### Order of Operations

A `find()` operation generally uses the following order of operations:

- match
- sort
- skip
- limit
- project
MongoDB may execute components in a different order to optimize query performance while maintaining the above order of operations.

### `$regex` Find Queries No Longer Ignore Invalid Regex

.. include:: /includes/fact-5.1-regex-find-functionality.rst

### Sessions

For cursors created inside a session, you cannot call :dbcommand:`getMore` outside the session.

Similarly, for cursors created outside of a session, you cannot call :dbcommand:`getMore` inside a session.

Session Idle Timeout ````````````````````

.. include:: /includes/extracts/sessions-cursor-timeout.rst

If the cursor may be idle for longer than 30 minutes, issue the operation within an explicit session using :method:`Mongo.startSession()`. Periodically refresh the session using the :dbcommand:`refreshSessions` command. See :limit:`Session Idle Timeout` for more information.

### Transactions

.. include:: /includes/extracts/transactions-supported-operation.rst

.. include:: /includes/extracts/transactions-operations-getMore.rst

.. include:: /includes/extracts/transactions-usage.rst

### Client Disconnection

.. include:: /includes/extracts/4.2-changes-disconnect.rst

### Stable API

When using `Stable API <stable-api>` V1, the following :dbcommand:`find` command fields are not supported:

- `awaitData`
- `max`
- `min`
- `noCursorTimeout`
- `returnKey`
- `showRecordId`
- `tailable`
### Index Filters and Collations

.. include:: /includes/index-filters-and-collations.rst

### Find Cursor Behavior on Views

.. include:: /includes/fact-7.3-singlebatch-cursor.rst

### Query Settings

.. include:: /includes/persistent-query-settings-info-for-queries.rst

## Examples

.. include:: /includes/sample-data-usage.rst

### Specify a Sort and Limit

The following command queries the `movies` collection for movies with an IMDB rating of at least 9 that are in the Drama genre. The command includes a `projection` to return only the `title`, `imdb.rating`, and `year` fields.

The command sorts results by `title` and limits the output to 5 documents.

### Override Default Read Concern

To override the default read concern level of :readconcern:`"local"`, use the `readConcern` option.

The following code example performs these operations on the `movies` collection on a replica set:

- finds movies with an IMDB rating below 5
- limits the results to 5 documents
- specifies a `read concern` of :readconcern:`"majority"` to read the most
recent copy of the data that MongoDB wrote to a majority of the nodes.

.. include:: /includes/fact-readConcern-most-recent-data-in-node.rst

The :dbcommand:`getMore` command uses the `readConcern` level specified in the originating :dbcommand:`find` command.

A `readConcern` can be specified for the :binary:`~bin.mongosh` method :method:`db.collection.find()` using the :method:`cursor.readConcern` method:

For more information on available read concerns, see `read-concern`.

### Specify Collation

.. include:: /includes/extracts/collation-description.rst

This example performs the following operations:

- finds movies with the title `Les Misérables` and date of `2012`
- sorts the matching documents by `title`
- runs  `find` with a French collation (`locale: "fr"`)
and accent-insensitive matching (`strength: 1`):

:binary:`~bin.mongosh` provides the :method:`cursor.collation()` to specify `collation <collation>` for a :method:`db.collection.find()` operation.

### Use Variables in `let`

The following example defines a `targetTitle` variable and uses it to find movies by comparing the `title` field against the variable value. This example finds all movies with the title "The Godfather":
