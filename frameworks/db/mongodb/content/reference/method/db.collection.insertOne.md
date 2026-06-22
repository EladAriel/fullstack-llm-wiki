---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.insertOne.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================================

# db.collection.insertOne() (mongosh method)

.. include:: /includes/wayfinding/mongosh-method-insertOne.rst

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

`db.collection.insertOne()` has the following form:

```javascript
db.collection.insertOne(
    <document>,
    {
      writeConcern: <document>
    }
)
```

### Parameters

`insertOne()` takes the following parameters:

## Behaviors

### Collection and `_id` Field Creation

.. include:: /includes/insert-id-and-collection.rst

### Explainability

`insertOne()` is not compatible with :method:`db.collection.explain()`.

### Error Handling

On error, `insertOne()` throws either a `writeError` or `writeConcernError` exception.

Schema Validation Errors ````````````````````````

If your collection uses `schema validation <schema-validation-overview>` and has `validationAction` set to `error`, inserting an invalid document throws a `MongoServerError` and `insertOne()` fails.

### Transactions

.. include:: /includes/extracts/transactions-supported-operation.rst

.. include:: /includes/extracts/transactions-usage.rst

Collection Creation in Transactions ````````````````````````````````````

.. include:: /includes/extracts/transactions-insert-implicit-collection-creation.rst

Write Concerns and Transactions ````````````````````````````````

.. include:: /includes/extracts/transactions-operations-write-concern.rst

### Oplog Entries

If an `insertOne()` operation successfully inserts a document, the operation adds an entry on the `oplog` (operations log). If the operation fails, the operation does not add an entry on the oplog.

## Examples

.. include:: /includes/sample-data-usage.rst

### Insert a Document without Specifying an `_id` Field

The following example inserts a document without an `_id` field into the `movies` collection:

Because the document does not include `_id`, :binary:`~bin.mongod creates and adds the id` field and assigns it a unique :method:`ObjectId` value.

.. include:: /includes/fact-object-id-may-differ.rst

### Insert a Document Specifying an `_id` Field

When you specify `_id when inserting a document, the id` value must be unique within the collection. The following example inserts a document into the `movies collection and specifies id`:

Inserting a duplicate value for any key that is part of a `unique index, such as id, throws an exception. The following attempts to insert a document with a id` value that already exists:

```javascript
try {
   db.movies.insertOne( { _id: 10, title: "Inception", year: 2010 } );
} catch (e) {
   print (e);
}
```

Since `_id: 10` already exists, the following exception is thrown:

```javascript
WriteError({
   "index" : 0,
   "code" : 11000,
   "errmsg" : "E11000 duplicate key error collection: sample_mflix.movies index: _id_ dup key: { : 10.0 }",
   "op" : {
      "_id" : 10,
      "title" : "Inception",
      "year" : 2010
   }
})
```

### Increase Write Concern

Given a three member replica set, the following operation specifies a `w` of `majority`, `wtimeout` of `100`:

```javascript
try {
   db.movies.insertOne(
       { title: "Arrival", year: 2016 },
       { writeConcern: { w : "majority", wtimeout : 100 } }
   );
} catch (e) {
   print (e);
}
```

If the acknowledgment takes longer than the `wtimeout` limit, the following exception is thrown:

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
