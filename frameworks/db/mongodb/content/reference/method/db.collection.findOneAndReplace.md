---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.findOneAndReplace.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================================

# db.collection.findOneAndReplace() (mongosh method)

.. include:: includes/wayfinding/mongosh-method-findOneAndReplace.rst

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The :method:`~db.collection.findOneAndReplace()` method has the following form:

```javascript
db.collection.findOneAndReplace(
   <filter>,
   <replacement>,
   {
     writeConcern: <document>,
     projection: <document>,
     sort: <document>,
     maxTimeMS: <number>,
     upsert: <boolean>,
     returnDocument: <string>,
     returnNewDocument: <boolean>,
     collation: <document>
   }
)
```

### Fields and Options

The :method:`~db.collection.findOneAndReplace()` method takes the following fields and options:

### Returns

Returns the original document by default. Returns the updated document if `returnDocument <findOneAndReplace-returnDocument>` is set to `after` or `returnNewDocument <findOneAndReplace-returnNewDocument>` is set to `true`.

## Behavior

### Document Match

:method:`db.collection.findOneAndReplace()` replaces the first matching document in the collection that matches the `filter`. The `sort` field can be used to influence which document is modified.

### Projection

.. include:: /includes/extracts/projection-language-consistency-admonition.rst

The `projection` field takes a document in the following form:

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

Shard Key Modification ``````````````````````

.. include:: /includes/limits-sharding-shardkey-document-immutable.rst

.. include:: /includes/shard-key-modification-warning.rst

To modify the **existing** shard key value with :method:`db.collection.findOneAndReplace()`:

- You :red:`must` run on a :binary:`~bin.mongos`. Do :red:`not`
issue the operation directly on the shard.

- You :red:`must` run either in a :doc:`transaction
</core/transactions>` or as a `retryable write </core/retryable-writes>`.

- You :red:`must` include an equality filter on the full shard key.
Missing Shard Key `````````````````

Documents in a sharded collection can be `missing the shard key fields <shard-key-missing>`. To use :method:`db.collection.findOneAndReplace()` to set the document's **missing** shard key,

- You :red:`must` run on a :binary:`~bin.mongos`. Do :red:`not`
issue the operation directly on the shard.

- You :red:`must` run either in a :doc:`transaction
</core/transactions>` or as a `retryable write </core/retryable-writes>` if the new shard key value is not `null`.

- You :red:`must` include an equality filter on the full shard key.
> **Tip:** .. include:: /includes/extracts/missing-shard-key-equality-condition-abridged.rst

See also:

- `shard-key-missing`
### Transactions

.. include:: /includes/extracts/transactions-supported-operation.rst

.. include:: /includes/extracts/transactions-usage.rst

Upsert within Transactions ``````````````````````````

.. include:: /includes/extracts/transactions-upsert-availability.rst

Write Concerns and Transactions ````````````````````````````````

.. include:: /includes/extracts/transactions-operations-write-concern.rst

### Oplog Entries

If a `db.collection.findOneAndReplace()` operation successfully replaces a document, the operation adds an entry on the `oplog` (operations log). If the operation fails or does not find a document to replace, the operation does not add an entry on the oplog.

## Examples

### Replace A Document

Create a sample `scores` collection with the following documents:

```javascript
db.scores.insertMany([
   { "_id" : 1, "team" : "Fearful Mallards", "score" : 25000 },
   { "_id" : 2, "team" : "Tactful Mooses", "score" : 23500 },
   { "_id" : 3, "team" : "Aquatic Ponies", "score" : 19250 },
   { "_id" : 4, "team" : "Cuddly Zebras", "score" : 15235 },
   { "_id" : 5, "team" : "Garrulous Bears", "score" : 18000 }
]);
```

The following operation finds a document with `score` less than `20000` and replaces it:

```javascript
db.scores.findOneAndReplace( 
   { "score" : { $lt : 20000 } },  
   { "team" : "Observant Badgers", "score" : 20000 }
)
```

The operation returns the original document that has been replaced:

```javascript
{ "_id" : 3, "team" : "Aquatic Ponies", "score" : 19250 }
```

If `returnNewDocument <findOneAndReplace-returnNewDocument>` was true, the operation would return the replacement document instead.

Although multiple documents meet the filter criteria, :method:`db.collection.findOneAndReplace` replaces only one document.

### Sort and Replace A Document

Create a sample `scores` collection with the following documents:

```javascript
db.scores.insertMany([
   { "_id" : 1, "team" : "Fearful Mallards", "score" : 25000 },
   { "_id" : 2, "team" : "Tactful Mooses", "score" : 23500 },
   { "_id" : 3, "team" : "Aquatic Ponies", "score" : 19250 },
   { "_id" : 4, "team" : "Cuddly Zebras", "score" : 15235 },
   { "_id" : 5, "team" : "Garrulous Bears", "score" : 18000 }
]);
```

By including an ascending `sort <findOneAndReplace-sort>` on the `score` field, the following example replaces the document with the lowest score among those documents that match the `filter <findOneAndReplace-filter>`:

```javascript
db.scores.findOneAndReplace(
   { "score" : { $lt : 20000 } },
   { "team" : "Observant Badgers", "score" : 20000 },
   { sort: { "score" : 1 } }
)
```

The operation returns the original document that has been replaced:

```javascript
{ "_id" : 4, "team" : "Cuddly Zebras", "score" : 15235 }
```

See `findOneAndReplace-example-replace-document` for the non-sorted result of this command.

### Project Specific Fields in Return Document

Create a sample `scores` collection with the following documents:

```javascript
db.scores.insertMany([
   { "_id" : 1, "team" : "Fearful Mallards", "score" : 25000 },
   { "_id" : 2, "team" : "Tactful Mooses", "score" : 23500 },
   { "_id" : 3, "team" : "Aquatic Ponies", "score" : 19250 },
   { "_id" : 4, "team" : "Cuddly Zebras", "score" : 15235 },
   { "_id" : 5, "team" : "Garrulous Bears", "score" : 18000 }
])
```

The following operation uses `projection <findOneAndReplace-projection>` to only display the `team` field in the returned document:

```javascript
db.scores.findOneAndReplace(
   { "score" : { $lt : 22250 } },
   { "team" : "Therapeutic Hamsters", "score" : 22250 },
   { sort : { "score" : 1 }, projection: { "_id" : 0, "team" : 1 } }
)
```

The operation returns the original document with only the `team` field:

```javascript
{ "team" : "Cuddly Zebras" }
```

### Replace Document with Time Limit

The following operation sets a 5ms time limit to complete:

```javascript
try {
   db.scores.findOneAndReplace(
      { "score" : { $gt : 25000 } },
      { "team" : "Emphatic Rhinos", "score" : 25010 },
      { maxTimeMS: 5 } 
   );
} catch(e){
   print(e);
}
```

If the operation exceeds the time limit, it returns:

```javascript
Error: findAndModifyFailed failed: { "ok" : 0, "errmsg" : "operation exceeded time limit", "code" : 50 }
```

### Replace Document with Upsert

The following operation uses the `upsert <findOneAndReplace-upsert>` field to insert the replacement document if no document matches the `filter <findOneAndReplace-filter>`:

```javascript
try {
   db.scores.findOneAndReplace( 
      { "team" : "Fortified Lobsters" },
      { "_id" : 6019, "team" : "Fortified Lobsters" , "score" : 32000},
      { upsert : true, returnDocument: "after" }
   );
} catch (e){
   print(e);
}
```

The operation returns the following:

```javascript
{
   "_id" : 6019,
   "team" : "Fortified Lobsters",
   "score" : 32000
}
```

If `returnDocument: "before"` was set, the operation would return `null` because there is no original document to return.

### Specify Collation

.. include:: /includes/extracts/collation-description.rst

Create a sample `myColl` collection with the following documents:

```javascript
db.myColl.insertMany([
   { _id: 1, category: "café", status: "A" },
   { _id: 2, category: "cafe", status: "a" },
   { _id: 3, category: "cafE", status: "a" }
]);
```

The following operation includes the `collation <findOneAndReplace-collation>` option:

```javascript
db.myColl.findOneAndReplace(
   { category: "cafe", status: "a" },
   { category: "cafÉ", status: "Replaced" },
   { collation: { locale: "fr", strength: 1 } }
);
```

The operation returns the following document:

```javascript
{ "_id" : 1, "category" : "café", "status" : "A" }
```
