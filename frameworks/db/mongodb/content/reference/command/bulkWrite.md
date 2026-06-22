---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/bulkWrite.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# bulkWrite (database command)

## Definition

.. versionadded:: 8.0

.. include:: /includes/bulkWrite-introduction.rst

To specify each collection in the `bulkWrite` command, use a `namespace` (database and collection name).

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has this syntax:

```javascript
db.adminCommand( {
   bulkWrite: 1,

   // Include the insert, update, and delete operations
   // in the ops array
   ops: [
      {
         insert: <integer>,  // Namespace ID index for insert operation.
                             // Must match a namespace ID index in
                             // ns specified later in the nsInfo array.
         document: <document>
      },
      {
         update: <integer>,  // Namespace ID index for update operation
         filter: <document>,
         updateMods: <document>,
         arrayFilters: [ <filterDocument0>, <filterDocument1>, ...  ],
         multi: <bolean>,
         hint: <document>,
         constants: <document>,
         collation: <document>
      },
      {
         delete: <integer>,  // Namespace ID index for delete operation
         filter: <document>,
         multi: <boolean>,
         hint: <document>,
         collation: <document>
      },
      ...
      // Additional insert, update, and delete operations in any order
      ...
   ],

   // Include the namespaces with collections to modify
   // in the nsInfo array. You can add multiple namespaces here.
   nsInfo: [
      {
         ns: <string>,  // Namespace (database and collection name) to modify.
                        // Each operation namespace ID index
                        // specified in the earlier ops array must
                        // match a namespace ID index here.
         collectionUUID: <string>,
         encryptionInformation: <document>
      },
      ...
      // Additional namespaces
      ...
   ],

   // Additional fields
   ordered: <boolean>,
   bypassDocumentValidation: <boolean>,
   comment: <string>,
   let: <document>,
   errorsOnly: <boolean>,
   cursor: { batchSize: <integer> },
   writeConcern: <string>
} )
```

In the command syntax, you can specify multiple:

- Insert, update, and delete operations in any order in the `ops`
array.

- Namespaces for the operations in the `nsInfo` array. To match the
operation to the namespace, use the same namespace ID index. Indexes start at `0`. You can use `sharded <sharding>` collections.

## Command Fields

The command takes the following fields:

## Output

The command returns a document with these fields:

> **Note:** The output fields may vary depending on the operations you run in the
`bulkWrite` command.

## Behavior

This section describes the `bulkWrite` command behavior.

### Multiple Document Field and Retryable Writes

.. include:: /includes/bulkWrite-multi-field.rst

To enable retryable writes, see `retryable writes <retryable-writes>`.

You can use `bulkWrite` insert operations with retryable writes and the `multi` field set to `true`.

You can use `bulkWrite` update and delete operations with the `multi` field set to `true`. But, you cannot use update or delete operations with both `multi` set to `true` and retryable writes.

### Write Concern Errors in Sharded Clusters

.. include:: /includes/fact-update-writeConcernError-mongos.rst

### Operation Performance

If you rewrite existing insert, update, and delete commands as a `bulkWrite` command and set `errorsOnly` to `true`, the `bulkWrite` command has similar performance as the existing commands. If you set `errorsOnly` to `false`, performance is worse.

In addition, if you have a sequence of commands like this:

```javascript
insert
update
delete
```

If you replace those commands with the following example fragment, then the command with the following fragment is faster regardless of other options:

```javascript
{
   bulkWrite: 1, 
   ops: [
      insert,
      update,
      delete
   ]
}
```

Most of the performance improvement is because of network latency, which is variable depending on your implementation, but the example is always faster.

## Examples

This section contains `bulkWrite` command examples.

### Single Namespace Bulk Write Example

The following `bulkWrite` example modifies a single namespace:

### Multiple Namespaces Bulk Write Example

You can specify multiple namespaces in a `bulkWrite` command.

The following `bulkWrite` example contains insert, update, and delete operations for two namespaces:

### Operations with Errors Bulk Write Example

The following `bulkWrite` example contains operations with errors and operations that don't change any documents:

### Bulk Write Example with errorsOnly Enabled

The following `bulkWrite` example sets `errorsOnly` to `true` to only show the error output:

## Learn More

- `server-sessions`
- `query-selectors`
- `aggregation-pipeline`
- `indexes`
- `collation`
- `retryable-writes`
- `transactions`
