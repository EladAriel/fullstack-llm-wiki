---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/checkMetadataConsistency.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================================

# checkMetadataConsistency (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

> **Note:** The `checkMetadataConsistency` command is executable only when connecting to
`mongos`. `mongod` does not support this command.

## Syntax

- To check the entire cluster for sharding metadata inconsistencies, run
the command from the `admin` database.

```javascript
   db.adminCommand( {
      checkMetadataConsistency: 1
   } )
```

- To check the database for sharding metadata inconsistencies, run the command
from the database context:

```javascript
   use cars
   db.runCommand( {
      checkMetadataConsistency: 1
   } )
```

- To check a collection for sharding metadata inconsistencies, run the command
with the collection name:

```javascript
   use library
   db.runCommand( {
      checkMetadataConsistency: "authors",
   } )
```

### Command Fields

### Output

The `checkMetadataConsistency` command returns a cursor with a document for each inconsistency found in sharding metadata. To learn more, see `inconsistency-types`.

The return document has the following fields:

## Behavior

### Batch Results

The `checkMetadataConsistency` command returns results in batches. To customize the batch size, the `batchSize` option:

```javascript
var cur = db.runCommand( {
   checkMetadataConsistency: 1,
   cursor: {
      batchSize: 10
   }
} )
```

If the `cursor.id` field is greater than 0, you can use with the :dbcommand:`getMore` command to retrieve the next batch of results.

### Check Indexes

The `checkMetadataConsistency` command does not check indexes by default. To check metadata consistency and indexes, use the `checkIndexes` option:

```javascript
db.runCommand( {
   checkMetadataConsistency: 1,
   checkIndexes: true
} )
```

## Example

Use :method:`~db.runCommand` to run the `checkMetadataConsistency` command:

```javascript
db.runCommand( { checkMetadataConsistency: 1 } )
```

Example Output:

```json
{
   cursor: {
      id: Long("0"),
      ns: "test.$cmd.aggregate",
      firstBatch: [
         {
            type: "MisplacedCollection",
            description: "Unsharded collection found on shard different from database primary shard",
            details: {
               namespace: "test.authors",
               shard: "shard02",
               localUUID: new UUID("1ad56770-61e2-48e9-83c6-8ecefe73cfc4")
            }
         }
      ],
   },
   ok: 1
}
```
