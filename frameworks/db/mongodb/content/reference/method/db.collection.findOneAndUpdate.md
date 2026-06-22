---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.findOneAndUpdate.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================================

# db.collection.findOneAndUpdate() (mongosh method)

.. include:: includes/wayfinding/mongosh-method-findOneAndUpdate.rst

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

`db.collection.findOneAndUpdate()` has the following form:

```javascript
db.collection.findOneAndUpdate(
    <filter>,
    <update document or aggregation pipeline>,
    {
      writeConcern: <document>,
      projection: <document>,
      sort: <document>,
      maxTimeMS: <number>,
      upsert: <boolean>,
      returnDocument: <string>,
      returnNewDocument: <boolean>,
      collation: <document>,
      arrayFilters: [ <filterdocument1>, ... ]
    }
)
```

### Parameters

`db.collection.findOneAndUpdate()` takes the following parameters:

## Behavior

### Performance

.. include:: /includes/fact-findAndUpdate

### Document Match

`findOneAndUpdate()` updates the first matching document in the collection that matches the `filter`. If no document matches the `filter`, no document is updated.

The `sort` parameter can be used to influence which document is updated.

### Projection

.. include:: /includes/extracts/projection-language-consistency-admonition.rst

The `projection` parameter takes a document in the following form:

```javascript
{ field1 : <value>, field2 : <value> ... }
```

.. include:: /includes/extracts/projection-values-table-without-meta.rst

Embedded Field Specification ````````````````````````````

.. include:: /includes/extracts/projection-embedded-field-format.rst

`_id` Field Projection ````````````````````````

.. include:: /includes/extracts/projection-id-field.rst

Inclusion or Exclusion ``````````````````````

.. include:: /includes/extracts/projection-inclusion-exclusion.rst

### Sharded Collections

.. include:: /includes/extracts/missing-shard-key-equality-condition-findAndModify.rst

Shard Key Modification ``````````````````````

.. include:: /includes/limits-sharding-shardkey-document-immutable.rst

.. include:: /includes/shard-key-modification-warning.rst

To modify the **existing** shard key value with `findOneAndUpdate()`:

- You :red:`must` run on a :binary:`~bin.mongos`. Do :red:`not`
issue the operation directly on the shard.

- You :red:`must` run either in a :doc:`transaction
</core/transactions>` or as a `retryable write </core/retryable-writes>`.

- You :red:`must` include an equality filter on the full shard key.
Missing Shard Key `````````````````

Documents in a sharded collection can be `missing the shard key fields <shard-key-missing>`. To use `findOneAndUpdate()` to set the document's **missing** shard key,

- You :red:`must` run on a :binary:`~bin.mongos`. Do :red:`not`
issue the operation directly on the shard.

- You :red:`must` run either in a :doc:`transaction
</core/transactions>` or as a `retryable write </core/retryable-writes>` if the new shard key value is not `null`.

- You :red:`must` include an equality filter on the full shard key.
> **Tip:** .. include:: /includes/extracts/missing-shard-key-equality-condition-abridged.rst

### Transactions

.. include:: /includes/extracts/transactions-supported-operation.rst

.. include:: /includes/extracts/transactions-usage.rst

Upsert within Transactions ``````````````````````````

.. include:: /includes/extracts/transactions-upsert-availability.rst

Write Concerns and Transactions ````````````````````````````````

.. include:: /includes/extracts/transactions-operations-write-concern.rst

### Oplog Entries

If a `findOneAndUpdate()` operation successfully updates a document, the operation adds an entry on the `oplog` (operations log). If the operation fails or does not find a document to update, the operation does not add an entry on the oplog.

## Examples

### Update A Document

The `grades` collection contains documents similar to the following:

```javascript
{ _id: 6305, name : "A. MacDyver", "assignment" : 5, "points" : 24 },
{ _id: 6308, name : "B. Batlock", "assignment" : 3, "points" : 22 },
{ _id: 6312, name : "M. Tagnum", "assignment" : 5, "points" : 30 },
{ _id: 6319, name : "R. Stiles", "assignment" : 2, "points" : 12 },
{ _id: 6322, name : "A. MacDyver", "assignment" : 2, "points" : 14 },
{ _id: 6234, name : "R. Stiles", "assignment" : 1, "points" : 10 }
```

The following operation finds the first document where `name : R. Stiles` and increments the score by `5`:

```javascript
db.grades.findOneAndUpdate(
   { "name" : "R. Stiles" },
   { $inc: { "points" : 5 } }
)
```

The operation returns the original document before the update:

```javascript
{ _id: 6319, name: "R. Stiles", "assignment" : 2, "points" : 12 }
```

If `returnNewDocument` was true, the operation would return the updated document instead.

### Sort And Update A Document

The `grades` collection contains documents similar to the following:

```javascript
{ _id: 6305, name : "A. MacDyver", "assignment" : 5, "points" : 24 },
{ _id: 6308, name : "B. Batlock", "assignment" : 3, "points" : 22 },
{ _id: 6312, name : "M. Tagnum", "assignment" : 5, "points" : 30 },
{ _id: 6319, name : "R. Stiles", "assignment" : 2, "points" : 12 },
{ _id: 6322, name : "A. MacDyver", "assignment" : 2, "points" : 14 },
{ _id: 6234, name : "R. Stiles", "assignment" : 1, "points" : 10 }
```

The following operation updates a document where `name : "A. MacDyver"`.  The operation sorts the matching documents by `points` ascending to update the matching document with the least points.

```javascript
db.grades.findOneAndUpdate(
   { "name" : "A. MacDyver" },
   { $inc : { "points" : 5 } },
   { sort : { "points" : 1 } }
)
```

The operation returns the original document before the update:

```javascript
{ _id: 6322, name: "A. MacDyver", "assignment" : 2, "points" : 14 }
```

### Project the Returned Document

The following operation uses projection to only display the `_id`, `points`, and `assignment` fields in the returned document:

```javascript
db.grades.findOneAndUpdate(
   { "name" : "A. MacDyver" },
   { $inc : { "points" : 5 } },
   { sort : { "points" : 1 }, projection: { "assignment" : 1, "points" : 1 } }
)
```

The operation returns the original document with only the fields specified in the `projection document and the id field as it was not explicitly suppressed (id: 0`) in the `projection document <projections>`.

```javascript
{ "_id" : 6322, "assignment" : 2, "points" : 14 }
```

### Update Document with Time Limit

The following operation sets a 5ms time limit to complete the update:

```javascript
try {
   db.grades.findOneAndUpdate(
      { "name" : "A. MacDyver" },
      { $inc : { "points" : 5 } },
      { sort: { "points" : 1 }, maxTimeMS : 5 };
   );
}
catch(e){
   print(e);
}
```

If the operation exceeds the time limit, it returns:

```javascript
Error: findAndModifyFailed failed: { "ok" : 0, "errmsg" : "operation exceeded time limit", "code" : 50 }
```

### Update Document with Upsert

The following operation uses the `upsert` field to insert the update document if nothing matches the `filter`:

```javascript
try {
db.grades.findOneAndUpdate(
   { "name" : "A.B. Abracus" },
   { $set: { "name" : "A.B. Abracus", "assignment" : 5}, $inc : { "points" : 5 } },
   { sort: { "points" : 1 }, upsert:true, returnNewDocument : true }
);
}
catch (e){
   print(e);
}
```

The operation returns the following:

```javascript
{
   "_id" : ObjectId("5789249f1c49e39a8adc479a"),
   "name" : "A.B. Abracus",
   "assignment" : 5,
   "points" : 5
}
```

If `returnNewDocument` was false, the operation would return `null` as there is no original document to return.

### Specify Collation

.. include:: /includes/extracts/collation-description.rst

A collection `myColl` has the following documents:

```javascript
{ _id: 1, category: "café", status: "A" }
{ _id: 2, category: "cafe", status: "a" }
{ _id: 3, category: "cafE", status: "a" }
```

The following operation includes the `collation <collation>` option:

```javascript
db.myColl.findOneAndUpdate(
   { category: "cafe" },
   { $set: { status: "Updated" } },
   { collation: { locale: "fr", strength: 1 } }
);
```

The operation returns the following document:

```javascript
{ "_id" : 1, "category" : "café", "status" : "A" }
```

### Array Update Operations with `arrayFilters`

> **Note:** .. include:: /includes/extracts/arrayFilters-update-aggregation-restriction.rst

.. include:: /includes/extracts/arrayFilters-blurb.rst

Update Elements Match `arrayFilters` Criteria ```````````````````````````````````````````````

> **Note:** .. include:: /includes/extracts/arrayFilters-update-aggregation-restriction.rst

Create a collection `students` with the following documents:

```javascript
db.students.insertMany( [
   { "_id" : 1, "grades" : [ 95, 92, 90 ] },
   { "_id" : 2, "grades" : [ 98, 100, 102 ] },
   { "_id" : 3, "grades" : [ 95, 110, 100 ] }
] )
```

To modify all elements that are greater than or equal to `100` in the `grades` array, use the filtered positional operator :update:`$[\<identifier\>]` with the `arrayFilters` option in the :method:`db.collection.findOneAndUpdate` method:

```javascript
db.students.findOneAndUpdate(
   { grades: { $gte: 100 } },
   { $set: { "grades.$[element]" : 100 } },
   { arrayFilters: [ { "element": { $gte: 100 } } ] }
)
```

The operation updates the `grades` field for a single document, and after the operation, the collection has the following documents:

```javascript
{ "_id" : 1, "grades" : [ 95, 92, 90 ] }
{ "_id" : 2, "grades" : [ 98, 100, 100 ] }
{ "_id" : 3, "grades" : [ 95, 110, 100 ] }
```

Update Specific Elements of an Array of Documents `````````````````````````````````````````````````

> **Note:** .. include:: /includes/extracts/arrayFilters-update-aggregation-restriction.rst

Create a collection `students2` with the following documents:

```javascript
db.students2.insertMany( [
   {
      "_id" : 1,
      "grades" : [
         { "grade" : 80, "mean" : 75, "std" : 6 },
         { "grade" : 85, "mean" : 90, "std" : 4 },
         { "grade" : 85, "mean" : 85, "std" : 6 }
      ]
   },
   {
      "_id" : 2,
      "grades" : [
         { "grade" : 90, "mean" : 75, "std" : 6 },
         { "grade" : 87, "mean" : 90, "std" : 3 },
         { "grade" : 85, "mean" : 85, "std" : 4 }
      ]
   }
] )
```

The following operation finds a document where the `_id` field equals `1` and uses the filtered positional operator :update:`$[\<identifier\>]` with the `arrayFilters` to modify the `mean` for all elements in the `grades` array where the grade is greater than or equal to `85`.

```javascript
db.students2.findOneAndUpdate(
   { _id : 1 },
   { $set: { "grades.$[elem].mean" : 100 } },
   { arrayFilters: [ { "elem.grade": { $gte: 85 } } ] }
)
```

The operation updates the `grades` field for a single document, and after the operation, the collection has the following documents:

```javascript
{
   "_id" : 1,
   "grades" : [
      { "grade" : 80, "mean" : 75, "std" : 6 },
      { "grade" : 85, "mean" : 100, "std" : 4 },
      { "grade" : 85, "mean" : 100, "std" : 6 }
    ]
}
{
   "_id" : 2,
   "grades" : [
      { "grade" : 90, "mean" : 75, "std" : 6 },
      { "grade" : 87, "mean" : 90, "std" : 3 },
      { "grade" : 85, "mean" : 85, "std" : 4 }
   ]
}
```

### Use an Aggregation Pipeline for Updates

:method:`db.collection.findOneAndUpdate()` can accept an aggregation pipeline for the update. The pipeline can consist of the following stages:

.. include:: /includes/list-update-agg-stages.rst

Using the aggregation pipeline allows for a more expressive update statement, such as expressing conditional updates based on current field values or updating one field using the value of another field(s).

For example, create a collection `students2` with the following documents:

```javascript
db.students2.insertMany( [
   {
      "_id" : 1,
      "grades" : [
         { "grade" : 80, "mean" : 75, "std" : 6 },
         { "grade" : 85, "mean" : 90, "std" : 4 },
         { "grade" : 85, "mean" : 85, "std" : 6 }
      ]
   },
   {
      "_id" : 2,
      "grades" : [
         { "grade" : 90, "mean" : 75, "std" : 6 },
         { "grade" : 87, "mean" : 90, "std" : 3 },
         { "grade" : 85, "mean" : 85, "std" : 4 }
      ]
   }
] )
```

The following operation finds a document where the `_id` field equals `1` and uses an aggregation pipeline to calculate a new field `total` from the `grades` field:

```javascript
db.students2.findOneAndUpdate(
   { _id : 1 },
   [ { $set: { "total" : { $sum: "$grades.grade" } } } ],  // The $set stage is an alias for ``$addFields`` stage
   { returnNewDocument: true }
)
```

> **Note:** The `$set` used in the pipeline refers to the aggregation stage
:pipeline:`$set` and not the update operator :update:`$set`.

The operation returns the updated document :

```javascript
{ 
  "_id" : 1, 
  "grades" : [ { "grade" : 80, "mean" : 75, "std" : 6 }, { "grade" : 85, "mean" : 90, "std" : 4 }, { "grade" : 85, "mean" :85, "std" : 6 } ], 
  "total" : 250
}
```
