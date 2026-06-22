---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.insertMany.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================================

# db.collection.insertMany() (mongosh method)

.. include:: /includes/wayfinding/mongosh-method-insertMany.rst

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

`db.collection.insertMany()` has the following syntax:

```javascript
db.collection.insertMany(
   [ <document 1> , <document 2>, ... ],
   {
      writeConcern: <document>,
      ordered: <boolean>
   }
)
```

### Parameters

## Behaviors

Given an array of documents, `insertMany()` inserts each document in the array into the collection. There is no limit to the number of documents you can specify in the array.

### Execution of Operations

By default, documents are inserted in the order they are provided.

- If `ordered` is set to `true` and an insert fails, the server does
not continue inserting records.

- If `ordered` is set to `false` and an insert fails, the server
continues inserting records. Documents may be reordered by :binary:`~bin.mongod` to increase performance. Applications should not depend on ordering of inserts if using an unordered `insertMany()`.

.. include:: /includes/fact-bulk-operation-sharded-cluster.rst

### Batching

The driver batches documents specified in the `insertMany()` array according to the :limit:`maxWriteBatchSize <Write Command Batch Limit Size>`, which is 100,000 and cannot be modified. For example, if the `insertMany()` operation contains 250,000 documents, the driver creates three batches: two with 100,000 documents and one with 50,000 documents.

> **Note:** The driver only performs batching when using the high-level API. If
you use :method:`db.runCommand()` directly (for example, when writing
a driver), MongoDB throws an error when attempting to execute a write
batch that exceeds the `maxWriteBatchSize` limit.

If the error report for a single batch grows too large, MongoDB truncates all remaining error messages. If there are at least two error messages with size greater than `1MB`, those messages are truncated.

The sizes and grouping mechanics are internal performance details and are subject to change in future versions.

### Collection and `_id` Field Creation

.. include:: /includes/insert-id-and-collection.rst

### Explainability

`insertMany()` is not compatible with :method:`db.collection.explain()`.

### Error Handling

Inserts throw a `BulkWriteError` exception.

Excluding `write concern <write-concern>` errors, ordered operations stop after an error, while unordered operations continue to process any remaining write operations in the queue.

Write concern errors are displayed in the `writeConcernErrors` field, while all other errors are displayed in the `writeErrors` field. If an error is encountered, the number of successful write operations are displayed instead of a list of inserted _ids. Ordered operations display the single error encountered while unordered operations display each error in an array.

Schema Validation Errors ````````````````````````

If your collection uses `schema validation <schema-validation-overview>` and has `validationAction` set to `error`, inserting an invalid document with `insertMany()` throws a `writeError`. Documents that precede the invalid document in the `documents` array are written to the collection. The value of the `ordered` field determines if the remaining valid documents are inserted.

### Transactions

.. include:: /includes/extracts/transactions-supported-operation.rst

.. include:: /includes/extracts/transactions-usage.rst

Collection Creation in Transactions ````````````````````````````````````

.. include:: /includes/extracts/transactions-insert-implicit-collection-creation.rst

Write Concerns and Transactions ````````````````````````````````

.. include:: /includes/extracts/transactions-operations-write-concern.rst

### Performance Consideration for Random Data

.. include:: /includes/indexes/random-data-performance.rst

### Oplog Entries

MongoDB consolidates operations that insert multiple documents, such as `insertMany()` or multiple `insertOne()` commands within a :method:`db.collection.bulkWrite()` operation, into a single entry in the `oplog`. If the operation fails, the operation does not add an entry on the oplog.

## Examples

.. include:: /includes/sample-data-usage.rst

### Insert Several Documents without Specifying an `_id` Field

The following example inserts three documents without `_id` fields into the `movies` collection:

Because the documents do not include `_id`, :binary:`~bin.mongod creates and adds the id` field for each document and assigns it a unique :method:`ObjectId` value.

.. include:: /includes/fact-object-id-may-differ.rst

### Insert Several Document Specifying an `_id` Field

The following example inserts documents that specify the `_id` field into the `movies collection. The value of id` must be unique within the collection to avoid a duplicate key error:

Inserting a duplicate value for any key that is part of a `unique index, such as id, throws an exception. The following attempts to insert a document with a id` value that already exists:

```javascript
try {
   db.movies.insertMany( [
      { _id: 13, title: "Inception", year: 2010 },
      { _id: 13, title: "The Dark Knight", year: 2008 },
      { _id: 14, title: "Interstellar", year: 2014 }
   ] );
} catch (e) {
   print (e);
}
```

Since `_id: 13` already exists, the following exception is thrown:

```javascript
BulkWriteError({
   "writeErrors" : [
      {
         "index" : 0,
         "code" : 11000,
         "errmsg" : "E11000 duplicate key error collection: sample_mflix.movies index: _id_ dup key: { : 13.0 }",
         "op" : {
            "_id" : 13,
            "title" : "The Dark Knight",
            "year" : 2008
         }
      }
   ],
   "writeConcernErrors" : [ ],
   "nInserted" : 1,
   "nUpserted" : 0,
   "nMatched" : 0,
   "nModified" : 0,
   "nRemoved" : 0,
   "upserted" : [ ]
})
```

Note that one document was inserted: the first document of `_id: 13` inserts successfully, but the second insert fails. The operation does not insert the remaining documents in the queue.

With `ordered` set to `false`, the insert operation continues with any remaining documents.

### Unordered Inserts

The following attempts to insert multiple documents with `_id` field and `ordered: false. The array of documents contains two documents with duplicate id` fields.

Although the documents with `title: "Interstellar"` and `title: "Ex Machina" fail to insert because of duplicate id` values, `insertedCount` shows that the remaining 5 documents insert successfully.

### Using Write Concern

Given a three member replica set, the following operation specifies a `w` of `majority` and `wtimeout` of `100`:

```javascript
try {
   db.movies.insertMany(
      [
         { _id: 15, title: "Forrest Gump", year: 1994 },
         { _id: 16, title: "Schindler's List", year: 1993 },
         { _id: 17, title: "Pulp Fiction", year: 1994 }
      ],
      { w: "majority", wtimeout: 100 }
   );
} catch (e) {
   print (e);
}
```

If the primary and at least one secondary acknowledge each write operation within 100 milliseconds, it returns:

```javascript
{
  "acknowledged" : true,
  "insertedIds" : [
     ObjectId("562a94d381cb9f1cd6eb0e1a"),
     ObjectId("562a94d381cb9f1cd6eb0e1b"),
     ObjectId("562a94d381cb9f1cd6eb0e1c")
  ]
}
```

If the total time required for all required nodes in the replica set to acknowledge the write operation is greater than `wtimeout`, the following `writeConcernError` is displayed when the `wtimeout` period has passed.

This operation returns:

```javascript
WriteConcernError({
   "code" : 64,
   "errmsg" : "waiting for replication timed out",
   "errInfo" : {
     "wtimeout" : true,
     "writeConcern" : { 
       "w" : "majority",
       "wtimeout" : 100,
       "provenance" : "getLastErrorDefaults"
     }
   }
})
```
