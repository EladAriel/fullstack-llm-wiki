---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.bulkWrite.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================================

# db.collection.bulkWrite() (mongosh method)

.. include:: /includes/wayfinding/mongosh-method-bulkWrite.rst

> **Note:** Starting in MongoDB 8.0, you can use the :method:`Mongo.bulkWrite()`
`mongosh` method to perform bulk writes across multiple databases and
collections. To learn more about different bulk write methods and commands,
see `bulk-write-operations`.

## Definition

## Compatibility

|operator-method| is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

> **Note:** You can't perform `bulk write <bulk-write-operations>`
operations in the `Atlas UI <atlas-ui-docs>`.
To insert multiple documents, you must insert an array of documents.
To learn more, see `atlas-ui-docs` in the Atlas documentation.

## Syntax

The :method:`~db.collection.bulkWrite()` method has the following form:

```javascript
db.collection.bulkWrite(
    [ <operation 1>, <operation 2>, ... ],
    {
      writeConcern : <document>,
      ordered : <boolean>
    }
)
```

### Parameters

The `bulkWrite()` method takes the following parameters:

## Behavior

`bulkWrite()` takes an array of write operations and executes each of them. By default operations are executed in order. See `bulkwrite-write-operations-executionofoperations` for controlling the order of write operation execution.

### Write Operations

insertOne +++++++++

Inserts a single document into the collection.

```javascript
db.collection.bulkWrite( [
   { insertOne : { "document" : <document> } }
] )
```

updateOne and updateMany ++++++++++++++++++++++++

replaceOne ++++++++++

`replaceOne` replaces a single document in the collection that matches the filter. If multiple documents match, `replaceOne` will replace the first matching document only.

```javascript
db.collection.bulkWrite([
   { replaceOne :
      {
         "filter" : <document>,
         "replacement" : <document>,
         "upsert" : <boolean>,
         "collation": <document>, 
         "hint": <document|string> 
      }
   }
] )
```

deleteOne and deleteMany ++++++++++++++++++++++++

### `_id` Field

If the document does not specify an `_id` field, then :binary:`~bin.mongod adds the id` field and assign a unique :method:`ObjectId for the document before inserting or upserting it. Most drivers create an ObjectId and insert the id` field, but the :binary:`~bin.mongod will create and populate the id` if the driver or application does not.

If the document contains an `_id field, the id` value must be unique within the collection to avoid duplicate key error.

Update or replace operations cannot specify an `_id` value that differs from the original document.

### Execution of Operations

The `ordered` parameter controls whether operations execute serially or in any order.

With `ordered : true` (default), operations execute serially. If an error occurs, subsequent operations are not executed.

With `ordered : false`, operations may execute in parallel. All operations without errors are completed even if some operations fail.

.. include:: /includes/fact-bulkwrite-operation-batches.rst

.. include:: /includes/fact-bulk-operation-sharded-cluster.rst

### Capped Collections

`bulkWrite()` has restrictions on `capped collections <capped collection>`:

- `updateOne` and `updateMany` throw a `WriteError` if the update increases
the document size.

- `replaceOne` throws a `WriteError` if the replacement document is larger than
the original.

- `deleteOne` and `deleteMany` throw a `WriteError` on capped collections.
### Error Handling

`bulkWrite()` throws a `BulkWriteError` exception on errors. See `bulkwrite-error-handling-txn`.

Excluding `write concern <write-concern>` errors, ordered operations stop after an error, while unordered operations continue to process any remaining write operations in the queue, unless when run inside a transaction. See `bulkwrite-error-handling-txn`.

Write concern errors are displayed in the `writeConcernErrors` field, while all other errors are displayed in the `writeErrors field. If an error is encountered, the number of successful write operations are displayed instead of the inserted id` values. Ordered operations display the single error encountered while unordered operations display each error in an array.

Schema Validation Errors ++++++++++++++++++++++++

If your collection uses `schema validation <schema-validation-overview>` and has `validationAction` set to `error`, inserting an invalid document or updating a document with invalid values throws an error. Operations preceding the invalid operation in the `operations` array are executed and written to the collection. The `ordered` field determines if the remaining operations are executed.

### Transactions

.. include:: /includes/extracts/transactions-supported-operation.rst

.. include:: /includes/extracts/transactions-usage.rst

Inserts and Upserts within Transactions +++++++++++++++++++++++++++++++++++++++

.. include:: /includes/extracts/4.4-changes-transactions-bulkWrite.rst

Write Concerns and Transactions +++++++++++++++++++++++++++++++

.. include:: /includes/extracts/transactions-operations-write-concern.rst

Error Handling inside Transactions ++++++++++++++++++++++++++++++++++

.. include:: /includes/extracts/4.2-changes-bulkWrite-txn-error-handling.rst

## Examples

### Ordered Bulk Write Example

It is important that you understand `bulkWrite()` operation ordering and error handling. By default, `bulkWrite()` runs an ordered list of operations:

- Operations run serially.
- If an operation has an error, that operation and any following
operations are not run.

- Operations listed before the error operation are completed.
The `bulkWrite()` examples use the `pizzas` collection:

.. include:: /includes/pizza-example-collection.rst

.. include:: /includes/pizza-bulk-write-example.rst

If the collection already contained a document with an `_id` of `4` before running the previous `bulkWrite()` example, the following duplicate key exception is returned for the second `insertOne` operation:

```javascript
writeErrors: [
   WriteError {
      err: {
         index: 1,
         code: 11000,
         errmsg: 'E11000 duplicate key error collection: test.pizzas index: _id_ dup key: { _id: 4 }',
         op: { _id: 4, type: 'sausage', size: 'large', price: 10 }
      }
   }
],
result: BulkWriteResult {
   result: {
      ok: 1,
      writeErrors: [
         WriteError {
            err: {
               index: 1,
               code: 11000,
               errmsg: 'E11000 duplicate key error collection: test.pizzas index: _id_ dup key: { _id: 4 }',
               op: { _id: 4, type: 'sausage', size: 'large', price: 10 }
            }
         }
      ],
      writeConcernErrors: [],
      insertedIds: [ { index: 0, _id: 3 }, { index: 1, _id: 4 } ],
      nInserted: 1,
      nUpserted: 0,
      nMatched: 0,
      nModified: 0,
      nRemoved: 0,
      upserted: []
   }
}
```

Because the `bulkWrite()` example is ordered, only the first `insertOne` operation is completed.

To complete all operations that do not have errors, run `bulkWrite()` with `ordered` set to `false`. For an example, see the following section.

### Unordered Bulk Write Example

To specify an unordered `bulkWrite()`, set `ordered` to `false`.

In an unordered `bulkWrite()` list of operations:

- Operations can run in parallel (not guaranteed). For details. See
`bulk-write-operations-ordered-vs-unordered`.

- Operations with errors are not completed.
- All operations without errors are completed.
Continuing the `pizzas` collection example, drop and recreate the collection:

.. include:: /includes/pizza-example-collection.rst

In the following example:

- `bulkWrite()` runs unordered operations on
the `pizzas` collection.

- The second `insertOne operation has the same id` as the first
`insertOne`, which causes a duplicate key error.

```javascript
try {
   db.pizzas.bulkWrite( [
      { insertOne: { document: { _id: 3, type: "beef", size: "medium", price: 6 } } },
      { insertOne: { document: { _id: 3, type: "sausage", size: "large", price: 10 } } },
      { updateOne: {
         filter: { type: "cheese" },
         update: { $set: { price: 8 } }
      } },
      { deleteOne: { filter: { type: "pepperoni"} } },
      { replaceOne: {
         filter: { type: "vegan" },
         replacement: { type: "tofu", size: "small", price: 4 }
      } }
   ],
   { ordered: false } )
} catch( error ) {
   print( error )
}
```

Example output, which includes the duplicate key error and a summary of the completed operations:

```javascript
writeErrors: [
   WriteError {
      err: {
         index: 1,
         code: 11000,
         errmsg: 'E11000 duplicate key error collection: test.pizzas index: _id_ dup key: { _id: 3 }',
         op: { _id: 3, type: 'sausage', size: 'large', price: 10 }
      }
   }
],
result: BulkWriteResult {
   result: {
      ok: 1,
      writeErrors: [
         WriteError {
            err: {
               index: 1,
               code: 11000,
               errmsg: 'E11000 duplicate key error collection: test.pizzas index: _id_ dup key: { _id: 3 }',
               op: { _id: 3, type: 'sausage', size: 'large', price: 10 }
            }
         }
      ],
      writeConcernErrors: [],
      insertedIds: [ { index: 0, _id: 3 }, { index: 1, _id: 3 } ],
      nInserted: 1,
      nUpserted: 0,
      nMatched: 2,
      nModified: 2,
      nRemoved: 1,
      upserted: []
   }
}
```

The second `insertOne` operation fails because of the duplicate key error. In an unordered `bulkWrite()`, any operation without an error is completed.

### Write Concern Errors in Sharded Clusters

.. include:: /includes/fact-update-writeConcernError-mongos.rst

### Bulk Write with Write Concern Example

Continuing the `pizzas` collection example, drop and recreate the collection:

.. include:: /includes/pizza-example-collection.rst

The following `bulkWrite()` example runs operations on the `pizzas` collection and sets a `"majority"` `write concern <wc-w>` with a 100 millisecond `timeout <wc-wtimeout>`:

```javascript
try {
   db.pizzas.bulkWrite( [
      { updateMany: {
         filter: { size: "medium" },
         update: { $inc: { price: 0.1 } }
      } },
      { updateMany: {
         filter: { size: "small" },
         update: { $inc: { price: -0.25 } }
      } },
      { deleteMany: { filter: { size: "large" } } },
      { insertOne: {
         document: { _id: 4, type: "sausage", size: "small", price: 12 }
      } } ],
      { writeConcern: { w: "majority", wtimeout: 100 } }
   )
} catch( error ) {
   print( error )
}
```

If the time for the majority of replica set members to acknowledge the operations exceeds `wtimeout`, the example returns a write concern error and a summary of completed operations:

```javascript
result: BulkWriteResult {
   result: {
      ok: 1,
      writeErrors: [],
      writeConcernErrors: [
         WriteConcernError {
            err: {
               code: 64,
               codeName: 'WriteConcernTimeout',
               errmsg: 'waiting for replication timed out',
               errInfo: { wtimeout: true, writeConcern: [Object] }
            }
         }
      ],
      insertedIds: [ { index: 3, _id: 4 } ],
      nInserted: 0,
      nUpserted: 0,
      nMatched: 2,
      nModified: 2,
      nRemoved: 0,
      upserted: [],
      opTime: { ts: Timestamp({ t: 1660329086, i: 2 }), t: Long("1") }
   }
}
```
