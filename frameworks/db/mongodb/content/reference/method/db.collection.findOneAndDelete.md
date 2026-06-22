---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.findOneAndDelete.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================================

# db.collection.findOneAndDelete() (mongosh method)

.. include:: includes/wayfinding/mongosh-method-findOneAndDelete.rst

## Definition

## Syntax

The :method:`~db.collection.findOneAndDelete()` method has the following form:

```none
db.collection.findOneAndDelete(
   <filter>,
   {
      writeConcern: <document>,
      projection: <document>,
      sort: <document>,
      maxTimeMS: <number>,
      collation: <document>
   }
)
```

### Parameters

The :method:`~db.collection.findOneAndDelete()` method takes the following parameters:

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

### Document Match

:method:`~db.collection.findOneAndDelete()` deletes the first matching document in the collection that matches the `filter`. The `sort` parameter can be used to influence which document is deleted.

### Projection

.. include:: /includes/extracts/projection-language-consistency-admonition.rst

The `projection` parameter takes a document in the following form:

```javascript
{ field1: <value>, field2: <value> ... }
```

.. include:: /includes/extracts/projection-values-table-without-meta.rst

Embedded Field Specification ````````````````````````````

.. include:: /includes/extracts/projection-embedded-field-format.rst

`_id` Field Projection ````````````````````````

.. include:: /includes/extracts/projection-id-field.rst

Inclusion or Exclusion ``````````````````````

.. include:: /includes/extracts/projection-inclusion-exclusion.rst

For more information on projection, see also:

- `read-operations-projection`
### Sharded Collections

.. include:: /includes/extracts/missing-shard-key-equality-condition-findAndModify.rst

### Transactions

.. include:: /includes/extracts/transactions-supported-operation.rst

.. include:: /includes/extracts/transactions-operations-write-concern.rst

.. include:: /includes/extracts/transactions-usage.rst

### Oplog Entries

If a `db.collection.findOneAndDelete()` operation successfully deletes a document, the operation adds an entry on the `oplog` (operations log). If the operation fails or does not find a document to delete, the operation does not add an entry on the oplog.

## Examples

### Delete A Document

The `scores` collection contains documents similar to the following:

```javascript
 db.scores.insertMany( [
   { _id: 6305, name : "A. MacDyver", "assignment" : 5, "points" : 24 },
   { _id: 6308, name : "B. Batlock", "assignment" : 3, "points" : 22 },
   { _id: 6312, name : "M. Tagnum", "assignment" : 5, "points" : 30 },
   { _id: 6319, name : "R. Stiles", "assignment" : 2, "points" : 12 },
   { _id: 6322, name : "A. MacDyver", "assignment" : 2, "points" : 14 },
   { _id: 6234, name : "R. Stiles", "assignment" : 1, "points" : 10 }
] )
```

The following operation finds the first document where `name : M. Tagnum` and deletes it:

```javascript
db.scores.findOneAndDelete( 
   { "name" : "M. Tagnum" }
)
```

The operation returns the original document that has been deleted:

```javascript
{ _id: 6312, name: "M. Tagnum", "assignment" : 5, "points" : 30 }
```

### Delete A Document Using WriteConcern

The `scores` collection contains documents similar to the following:

```javascript
db.scores.insertMany( [
   { _id: 6305, name : "A. MacDyver", "assignment" : 5, "points" : 24 },
   { _id: 6308, name : "B. Batlock", "assignment" : 3, "points" : 22 },
   { _id: 6312, name : "M. Tagnum", "assignment" : 5, "points" : 30 },
   { _id: 6319, name : "R. Stiles", "assignment" : 2, "points" : 12 },
   { _id: 6322, name : "A. MacDyver", "assignment" : 2, "points" : 14 },
   { _id: 6234, name : "R. Stiles", "assignment" : 1, "points" : 10 }
] )
```

The following operation uses a write concern document inside of the :method:`db.collection.findOneAndDelete()` method with options:

- `w:1` to requests acknowledgment that the write operation has
propagated to the standalone mongod or the primary in a replica set.

- `j:true` to tell the number of MongoDB instances specified in `w:1`
to have the delete written to on-disk journel.

- `wtimeout : 1000` to specify a time limit, in milliseconds,
for the write concern. `wtimeout` is only applicable for `w` values greater than 1.

```javascript
db.scores.findOneAndDelete(
   { name: "A. MacDyver" },
   { 
      writeConcern: {  
         w : 1,
         j : true,
         wtimeout : 1000
      } 
   }
)
```

The operation returns the following document:

```javascript
{ _id: 6305, name: 'A. MacDyver', assignment: 5, points: 24 }
```

The document is deleted with the writeConcern options specified.

### Sort And Delete A Document

The `scores` collection contains documents similar to the following:

```javascript
db.scores.insertMany( [
   { _id: 6305, name : "A. MacDyver", "assignment" : 5, "points" : 24 },
   { _id: 6308, name : "B. Batlock", "assignment" : 3, "points" : 22 },
   { _id: 6312, name : "M. Tagnum", "assignment" : 5, "points" : 30 },
   { _id: 6319, name : "R. Stiles", "assignment" : 2, "points" : 12 },
   { _id: 6322, name : "A. MacDyver", "assignment" : 2, "points" : 14 },
   { _id: 6234, name : "R. Stiles", "assignment" : 1, "points" : 10 }
] )
```

The following operation first finds all documents where `name : "A. MacDyver"`. It then sorts by `points` ascending before deleting the document with the lowest points value:

```javascript
db.scores.findOneAndDelete(
   { "name" : "A. MacDyver" },
   { sort : { "points" : 1 } }
)
```

The operation returns the original document that has been deleted:

```javascript
{ _id: 6322, name: "A. MacDyver", "assignment" : 2, "points" : 14 }
```

### Projecting the Deleted Document

The following operation uses projection to only return the `_id` and `assignment` fields in the returned document:

```javascript
db.scores.findOneAndDelete(
   { "name" : "A. MacDyver" },
   { sort : { "points" : 1 }, projection: { "assignment" : 1 } }
)
```

The operation returns the original document with the `assignment and id` fields:

```javascript
{ _id: 6322, "assignment" : 2 }
```

### Update Document with Time Limit

The following operation sets a 5ms time limit to complete the deletion:

```javascript
try {
   db.scores.findOneAndDelete(
      { "name" : "A. MacDyver" },
      { sort : { "points" : 1 }, maxTimeMS : 5 }
   )
}
catch(e){
   print(e)
}
```

If the operation exceeds the time limit, it returns:

```javascript
MongoServerError: operation exceeded time limit: { "ok": 0, "code" : 50, "codeName" : "MaxTimeMSExpired" }
```

> **Note:** This error message has been shortened for brevity.

### Specify Collation

.. include:: /includes/extracts/collation-description.rst

A collection `myColl` has the following documents:

```javascript
db.myColl.insertMany( [
   { _id: 1, category: "café", status: "A" },
   { _id: 2, category: "cafe", status: "a" },
   { _id: 3, category: "cafE", status: "a" }
] )
```

The following operation includes the `collation <collation>` option:

```javascript
db.myColl.findOneAndDelete(
   { category: "cafe", status: "a" },
   { collation: { locale: "fr", strength: 1 } }
);
```

The operation returns the following document:

```javascript
{ "_id" : 1, "category" : "café", "status" : "A" }
```
