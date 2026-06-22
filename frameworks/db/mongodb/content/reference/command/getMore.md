---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/getMore.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# getMore (database command)

## Definition

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
      getMore: <long>,
      collection: <string>,
      batchSize: <int>,
      maxTimeMS: <int>,
      comment: <any>
   }
)
```

## Command Fields

The command accepts the following fields:

## Output

The command returns a document that contains the cursor information as well as the next batch.

For example, running `getMore` on a cursor created by a :dbcommand:`find` operation on a sharded cluster returns a document similar to this output:

```javascript
{
   "cursor" : {
      "id" : Long("678960441858272731"),
      "ns" : "test.contacts",
      "nextBatch" : [
         {
            "_id" : ObjectId("5e8e501e1a32d227f9085857"),
            "zipcode" : "220000"
         }
      ],
      "partialResultsReturned" : true,
      "postBatchResumeToken": "< Resume Token >"
   },
   "ok" : 1,
   "operationTime" : Timestamp(1586385239, 2),
   "$clusterTime" : {
      "clusterTime" : Timestamp(1586385239, 2),
      "signature" : {
         "hash" : BinData(0,"lLjejeW6AQGReR9x1PD8xU+tP+A="),
         "keyId" : Long("6813467763969884181")
      }
   }
}
```

In addition to these fields, the :method:`db.runCommand()` response includes the following information for replica sets and sharded clusters:

- `$clusterTime`
- `operationTime`
See `db.runCommand() Response <command-response>` for details.

## Behavior

### Access Control

If `authentication <authentication>` is enabled, you can only run `getMore` against cursors you created.

### Sessions

For cursors created inside a session, you cannot call `getMore` outside the session.

Similarly, for cursors created outside of a session, you cannot call `getMore` inside a session.

Transactions ````````````

For `multi-document transactions <transactions>`:

.. include:: /includes/extracts/transactions-operations-getMore.rst

### Errors

Starting in MongoDB 8.2, the cursor identifier must match the name of the cursor that operates on the specified `collection`. If the `collection` does not have a cursor with the specified cursor identifier, `getMore` returns an error.

### Slow Queries

.. include:: /includes/getMore-slow-queries.rst

## Learn More

- `cursor-batchSize`
- `read-operations-cursors`
