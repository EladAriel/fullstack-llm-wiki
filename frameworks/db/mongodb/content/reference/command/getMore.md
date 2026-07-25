---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/getMore.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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

The command returns a document that contains the cursor information and the next batch.

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

For cursors created outside a session, you cannot call `getMore` inside a session.

Transactions ````````````

For `multi-document transactions <transactions>`:

.. include:: /includes/extracts/transactions-operations-getMore.rst

### Errors

Starting in MongoDB 8.2, the cursor identifier must match the name of the cursor operating on the specified `collection`. If no matching cursor exists, `getMore` returns an error.

### Slow Queries

.. include:: /includes/getMore-slow-queries.rst

## Learn More

- `cursor-batchSize`
- `read-operations-cursors`
