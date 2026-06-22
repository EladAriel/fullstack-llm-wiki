---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.insert.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================================

# db.collection.insert() (mongosh method)

.. include:: /includes/fact-mongosh-shell-method-deprecated.rst

## Definition

## Syntax

`db.collection.insert()` has the following syntax:

```javascript
db.collection.insert(
   <document or array of documents>,
   {
      writeConcern: <document>,
      ordered: <boolean>
   }
)
```

### Parameters

## Behaviors

### Write Concern

The `insert()` method uses the :dbcommand:`insert` command, which uses the default `write concern </reference/write-concern>`. To specify a different write concern, include the write concern in the options parameter.

### Collection and `_id` Field Creation

.. include:: /includes/insert-id-and-collection.rst

### Transactions

.. include:: /includes/extracts/transactions-supported-operation.rst

.. include:: /includes/extracts/transactions-usage.rst

Collection Creation in Transactions ````````````````````````````````````

.. include:: /includes/extracts/transactions-insert-implicit-collection-creation.rst

Write Concerns and Transactions ````````````````````````````````

.. include:: /includes/extracts/transactions-operations-write-concern.rst

### Oplog Entries

If an `insert()` operation successfully inserts a document, the operation adds an entry on the `oplog` (operations log). If the operation fails, the operation does not add an entry on the oplog.

## Examples

.. include:: /includes/sample-data-usage.rst

### Insert a Document without Specifying an `_id` Field

The following example inserts a document without an `_id` field into the `movies` collection:

Because the inserted document does not include `_id`, :binary:`~bin.mongod creates and adds the id` field and assigns it a unique :method:`ObjectId` value.

.. include:: /includes/fact-object-id-may-differ.rst

### Insert a Document Specifying an `_id` Field

The following example specifies the `_id` field in the document inserted into the `movies collection. The value of id` must be unique within the collection to avoid a duplicate key error.

### Insert Multiple Documents

The following example performs a bulk insert by passing an array of documents to `insert()`. By default, MongoDB performs an ordered insert. With ordered inserts, if an error occurs during an insert of one of the documents, MongoDB returns on error without processing the remaining documents in the array.

The first document specifies an `_id field. Because the second and third documents do not contain an id` field, :binary:`~bin.mongod creates and adds the id` field for those documents during the insert:

### Perform an Unordered Insert

The following example performs an unordered insert of three documents. With unordered inserts, if an error occurs during an insert of one of the documents, MongoDB continues to insert the remaining documents in the array.

```javascript
db.movies.insert(
   [
     { _id: 20, title: "2001: A Space Odyssey", year: 1968 },
     { _id: 21, title: "A Clockwork Orange", year: 1971 },
     { _id: 22, title: "The Shining", year: 1980 }
   ],
   { ordered: false }
)
```

### Override Default Write Concern

The following operation to a replica set specifies a `write concern </reference/write-concern>` of `w: 2` with a `wtimeout` of 5000 milliseconds. This operation either returns after the write propagates to both the primary and one secondary, or times out after 5 seconds.

```javascript
db.movies.insert(
    { title: "The Revenant", year: 2015 },
    { writeConcern: { w: 2, j: true, wtimeout: 5000 } }
)
```

## WriteResult

When passed a single document, `insert()` returns a :method:`WriteResult` object.

### Successful Results

Upon success, the returned `WriteResult` object contains information on the number of documents inserted:

```javascript
WriteResult({ "nInserted" : 1 })
```

### Write Concern Errors

If `insert()` encounters write concern errors, the results include the `WriteResult.writeConcernError` field:

```javascript
WriteResult({
  "nInserted" : 1,
  "writeConcernError"({
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

### Errors Unrelated to Write Concern

If `insert()` encounters a non-write concern error, the results include the `WriteResult.writeError` field:

```javascript
WriteResult({
   "nInserted" : 0,
   "writeError" : {
      "code" : 11000,
      "errmsg" : "insertDocument :: caused by :: 11000 E11000 duplicate key error index: test.foo.$_id_  dup key: { : 1.0 }"
   }
})
```

## BulkWriteResult

When passed an array of documents, `insert()` returns a :method:`BulkWriteResult()` object.
