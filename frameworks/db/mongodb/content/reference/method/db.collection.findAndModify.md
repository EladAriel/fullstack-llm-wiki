---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.findAndModify.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================================

# db.collection.findAndModify() (mongosh method)

(possibly w modifications) to the command findAndModify.txt and vice versa

.. include:: /includes/wayfinding/mongosh-method-findAndModify.rst

> **Important:** Use :method:`~db.collection.findOneAndUpdate()`,
:method:`~db.collection.findOneAndDelete()`, or
:method:`~db.collection.findOneAndReplace()`   instead.

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

.. versionchanged:: 5.0

`db.collection.findAndModify()` has the following form:

```javascript
db.collection.findAndModify({
    query: <document>,
    sort: <document>,
    remove: <boolean>,
    update: <document or aggregation pipeline>,
    new: <boolean>,
    fields: <document>,
    upsert: <boolean>,
    bypassDocumentValidation: <boolean>,
    writeConcern: <document>,
    maxTimeMS: <integer>,
    collation: <document>,
    arrayFilters: [ <filterdocument1>, ... ],
    let: <document> // Added in MongoDB 5.0
});
```

### Parameters

`db.collection.findAndModify()` takes a document parameter with the following embedded document fields:

## Return Data

For remove operations, if the query matches a document, `findAndModify()` returns the removed document. If the query does not match a document to remove, `findAndModify()` returns `null`.

For update operations, `findAndModify()` returns one of the following:

.. include:: /includes/extracts/fact-findandmodify-method-return.rst

## Behavior

### Performance

.. include:: /includes/fact-findAndUpdate

### `fields` Projection

.. include:: /includes/extracts/projection-language-consistency-admonition.rst

The `fields` option takes a document in the following form:

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

### Upsert with Unique Index

.. include:: /includes/extracts/upsert-unique-index-findAndModify-method.rst

### Sharded Collections

To use :dbcommand:`findAndModify` on a sharded collection:

- If you only target one shard, you can use a partial shard key in the `query` field or,
- You can provide an equality condition on a full shard key in the `query` field.
- Starting in version 7.1, you do not need to provide the `shard key`
or `_id` field in the query specification.

.. include:: /includes/extracts/missing-shard-key-equality-condition-findAndModify.rst

Shard Key Modification ``````````````````````

.. include:: /includes/limits-sharding-shardkey-document-immutable.rst

.. include:: /includes/shard-key-modification-warning.rst

To update the **existing** shard key value with `findAndModify()`:

- You :red:`must` run on a :binary:`~bin.mongos`. Do :red:`not`
issue the operation directly on the shard.

- You :red:`must` run either in a :doc:`transaction
</core/transactions>` or as a `retryable write </core/retryable-writes>`.

- You :red:`must` include an equality filter on the full shard key.
Missing Shard Key `````````````````

Documents in a sharded collection can be `missing the shard key fields <shard-key-missing>`. To use :method:`db.collection.findAndModify()` to set the document's **missing** shard key:

- You :red:`must` run on a :binary:`~bin.mongos`. Do :red:`not`
issue the operation directly on the shard.

- You :red:`must` run either in a :doc:`transaction
</core/transactions>` or as a `retryable write </core/retryable-writes>` if the new shard key value is not `null`.

- You :red:`must` include an equality filter on the full shard key.
> **Tip:** .. include:: /includes/extracts/missing-shard-key-equality-condition-abridged.rst

### Schema Validation

.. include:: /includes/extracts/bypassDocumentValidation-db.collection.findAndModify.rst

### Comparisons with the `update` Method

.. include:: /includes/fact-findAndModify-update-comparison.rst

### Transactions

.. include:: /includes/extracts/transactions-supported-operation.rst

.. include:: /includes/extracts/transactions-usage.rst

Upsert within Transactions ``````````````````````````

.. include:: /includes/extracts/transactions-upsert-availability.rst

Write Concerns and Transactions ````````````````````````````````

.. include:: /includes/extracts/transactions-operations-write-concern.rst

### Oplog Entries

If a `findAndModify()` operation successfully finds and modifies a document, the operation adds an entry on the `oplog` (operations log). If the operation fails or does not find a document to modify, the operation does not add an entry on the oplog.

### Write Concern Errors

In MongoDB versions earlier than 6.0, if the `findAndModify` command is run on a sharded cluster, :binary:`mongos` discards the `writeConcernError` document if the shard response contains an error. In MongoDB 6.0 and later, :binary:`mongos` returns `writeConcernError`.

## Examples

### Update and Return

The following method updates and returns an existing document in the people collection where the document matches the query criteria:

```javascript
db.people.findAndModify({
    query: { name: "Tom", state: "active", rating: { $gt: 10 } },
    sort: { rating: 1 },
    update: { $inc: { score: 1 } }
})
```

This method performs the following actions:

#. The `query` finds a document in the `people` collection where the `name` field has the value `Tom`, the `state` field has the value `active` and the `rating` field has a value :query:`greater than <$gt>` 10.

#. The `sort` orders the results of the query in ascending order. If multiple documents meet the `query` condition, the method will select for modification the first document as ordered by this `sort`.

#. The update :update:`increments <$inc>` the value of the `score` field by 1.

#. The method returns the original (i.e. pre-modification) document selected for this update:

```javascript
   {
     "_id" : ObjectId("50f1e2c99beb36a0f45c6453"),
     "name" : "Tom",
     "state" : "active",
     "rating" : 100,
     "score" : 5
   }

To return the updated document, add the ``new:true`` option to
the method.

If no document matched the ``query`` condition, the method
returns ``null``.
```

### Upsert

The following method includes the `upsert: true` option for the `update` operation to either update a matching document or, if no matching document exists, create a new document:

```javascript
db.people.findAndModify({
    query: { name: "Gus", state: "active", rating: 100 },
    sort: { rating: 1 },
    update: { $inc: { score: 1 } },
    upsert: true
})
```

If the method finds a matching document, the method performs an update.

If the method does **not** find a matching document, the method creates a new document. Because the method included the `sort` option, it returns an empty document `{ }` as the original (pre-modification) document:

```javascript
{ }
```

If the method did **not** include a `sort` option, the method returns `null`.

```javascript
null
```

### Return New Document

The following method includes both the `upsert: true` option and the `new:true` option. The method either updates a matching document and returns the updated document or, if no matching document exists, inserts a document and returns the newly inserted document in the `value` field.

In the following example, no document in the `people` collection matches the `query` condition:

```javascript
db.people.findAndModify({
    query: { name: "Pascal", state: "active", rating: 25 },
    sort: { rating: 1 },
    update: { $inc: { score: 1 } },
    upsert: true,
    new: true
})
```

The method returns the newly inserted document:

```javascript
{
   "_id" : ObjectId("50f49ad6444c11ac2448a5d6"),
   "name" : "Pascal",
   "rating" : 25,
   "score" : 1,
   "state" : "active"
}
```

### Sort and Remove

By including a `sort` specification on the `rating` field, the following example removes from the `people` collection a single document with the `state` value of `active` and the lowest `rating` among the matching documents:

```javascript
db.people.findAndModify(
   {
     query: { state: "active" },
     sort: { rating: 1 },
     remove: true
   }
)
```

The method returns the deleted document:

```javascript
{
   "_id" : ObjectId("52fba867ab5fdca1299674ad"),
   "name" : "XYZ123",
   "score" : 1,
   "state" : "active",
   "rating" : 3
}
```

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
db.myColl.findAndModify({
    query: { category: "cafe", status: "a" },
    sort: { category: 1 },
    update: { $set: { status: "Updated" } },
    collation: { locale: "fr", strength: 1 }
});
```

The operation returns the following document:

```javascript
{ "_id" : 1, "category" : "café", "status" : "A" }
```

### Specify `arrayFilters` for an Array Update Operations

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

To update all elements that are greater than or equal to `100` in the `grades` array, use the filtered positional operator :update:`$[\<identifier\>]` with the `arrayFilters` option in the :method:`db.collection.findAndModify` method:

```javascript
db.students.findAndModify({
   query: { grades: { $gte: 100 } },
   update: { $set: { "grades.$[element]" : 100 } },
   arrayFilters: [ { "element": { $gte: 100 } } ]
})
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

The following operation finds a document where the `_id` field equals `1` and uses the filtered positional operator :update:`$[\<identifier\>]` with the `arrayFilters` to update the `mean` for all elements in the `grades` array where the grade is greater than or equal to `85`.

```javascript
db.students2.findAndModify({
   query: { _id : 1 },
   update: { $set: { "grades.$[elem].mean" : 100 } },
   arrayFilters: [ { "elem.grade": { $gte: 85 } } ] 
})
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

:method:`db.collection.findAndModify()` can accept an aggregation pipeline for the update. The pipeline can consist of the following stages:

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
db.students2.findAndModify( {
   query: {  "_id" : 1 },
   update: [ { $set: { "total" : { $sum: "$grades.grade" } } } ],  // The $set stage is an alias for ``$addFields`` stage
   new: true
} )
```

> **Note:** The `$set` used in the pipeline refers to the aggregation stage
:pipeline:`$set` and not the update operator :update:`$set`.

The operation returns the updated document:

```javascript
{
   "_id" : 1,
   "grades" : [ { "grade" : 80, "mean" : 75, "std" : 6 }, { "grade" : 85, "mean" : 90, "std" : 4 }, { "grade" : 85, "mean" : 85, "std" : 6 } ],
   "total" : 250
}
```

### Use Variables in `let`

.. include:: /includes/let-example-introduction.rst

.. include:: /includes/let-example-find-modify-flavors.rst

```javascript
db.cakeFlavors.findAndModify( {
   query: {
      $expr: { $eq: [ "$flavor", "$$targetFlavor" ] }
   },
   update: { flavor: "orange" },
   let: { targetFlavor: "cherry" }
} )
```

### User Roles and Document Updates

.. include:: /includes/user-roles-system-variable-update-example-introduction.rst

.. include:: /includes/user-roles-system-variable-update-example-middle.rst

.. include:: /includes/user-roles-system-variable-update-example-end.rst
