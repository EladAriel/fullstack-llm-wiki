---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/findAndModify.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================

# findAndModify (database command)

modifications) to the method db.collection.findAndModify.txt and vice versa

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

.. versionchanged:: 5.0

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   {
     findAndModify: <collection-name>,
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
     arrayFilters: <array>,
     hint: <document|string>,
     comment: <any>,
     let: <document> // Added in MongoDB 5.0
   } 
)
```

## Command Fields

The command takes the following fields:

## Output

The :dbcommand:`findAndModify` command returns a document with the following fields:

### `lastErrorObject`

The `lastErrorObject` embedded document contains the following fields:

### `value`

For `remove` operations, `value` contains the removed document if the query matches a document. If the query does not match a document to remove, `value` contains `null`.

For `update` operations, the `value` embedded document contains the following:

.. include:: /includes/extracts/fact-findandmodify-command-return.rst

## Behavior

### Upsert with Unique Index

.. include:: /includes/extracts/upsert-unique-index-findAndModify-command.rst

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

To update the **existing** shard key value with :dbcommand:`findAndModify`:

- You :red:`must` run on a :binary:`~bin.mongos`. Do :red:`not`
issue the operation directly on the shard.

- You :red:`must` run either in a :doc:`transaction
</core/transactions>` or as a `retryable write </core/retryable-writes>`.

- You :red:`must` include an equality filter on the full shard key.
Missing Shard Key `````````````````

Documents in a sharded collection can be `missing the shard key fields <shard-key-missing>`. To use :dbcommand:`findAndModify` to set the document's **missing** shard key:

- You :red:`must` run on a :binary:`~bin.mongos`. Do :red:`not`
issue the operation directly on the shard.

- You :red:`must` run either in a :doc:`transaction
</core/transactions>` or as a `retryable write </core/retryable-writes>` if the new shard key value is not `null`.

- You :red:`must` include an equality filter on the full shard key.
> **Tip:** .. include:: /includes/extracts/missing-shard-key-equality-condition-abridged.rst

See also:

- `shard-key-missing`
### Schema Validation

.. include:: /includes/extracts/bypassDocumentValidation-findAndModify.rst

### Comparisons with the `update` Method

document, as well as the status of the operation

.. include:: /includes/fact-findAndModify-update-comparison.rst

.. seealso :

```
:ref:`Considerations for field names <crud-concepts-dot-dollar-considerations>`
```

### Transactions

.. include:: /includes/extracts/transactions-supported-operation.rst

.. include:: /includes/extracts/transactions-usage.rst

Upsert within Transactions ``````````````````````````

.. include:: /includes/extracts/transactions-upsert-availability.rst

Write Concerns and Transactions ````````````````````````````````

.. include:: /includes/extracts/transactions-operations-write-concern.rst

Write Concern Errors ````````````````````

If a `findAndModify` operation fails because the write concern wasn't fulfilled, the operation returns a `writeConcernError` document.

## Examples

### Update and Return

The following command updates an existing document in the `people` collection where the document matches the `query` criteria:

```javascript
db.runCommand(
   {
     findAndModify: "people",
     query: { name: "Tom", state: "active", rating: { $gt: 10 } },
     sort: { rating: 1 },
     update: { $inc: { score: 1 } }
   }
)
```

This command performs the following actions:

#. The `query` finds a document in the `people` collection where the `name` field has the value `Tom`, the `state` field has the value `active` and the `rating` field has a value :expression:`greater than <$gt>` 10.

#. The `sort` orders the results of the query in ascending order. If multiple documents meet the `query` condition, the command will select for modification the first document as ordered by this `sort`.

#. The `update` :update:`increments <$inc>` the value of the `score` field by 1.

#. The command returns a document with the following fields:

- The `lastErrorObject` field that contains the details of the
command, including the field `updatedExisting` which is `true`, and

- The `value` field that contains the original (i.e.
pre-modification) document selected for this update:

```javascript
     {
       "lastErrorObject" : {
          "connectionId" : 1,
          "updatedExisting" : true,
          "n" : 1,
          "syncMillis" : 0,
          "writtenTo" : null,
          "err" : null,
          "ok" : 1
       },
       value" : {
         "_id" : ObjectId("54f62d2885e4be1f982b9c9c"),
         "name" : "Tom",
         "state" : "active",
         "rating" : 100,
         "score" : 5
       },
       "ok" : 1
     }
```

To return the updated document in the `value` field, add the `new:true` option to the command.

If no document match the `query` condition, the command returns a document that contains `null` in the `value` field:

```javascript
{ "value" : null, "ok" : 1 }
```

:binary:`~bin.mongosh` and many `drivers <driver>` provide a :method:`~db.collection.findAndModify()` helper method. Using the shell helper, this previous operation can take the following form:

```javascript
db.people.findAndModify( {
   query: { name: "Tom", state: "active", rating: { $gt: 10 } },
   sort: { rating: 1 },
   update: { $inc: { score: 1 } }
} );
```

However, the :method:`~db.collection.findAndModify()` shell helper method returns only the unmodified document, or if `new` is `true`, the updated document.

```javascript
{
  "_id" : ObjectId("54f62d2885e4be1f982b9c9c"),
  "name" : "Tom",
  "state" : "active",
  "rating" : 100,
  "score" : 5
}
```

### `upsert: true`

The following :dbcommand:`findAndModify` command includes the `upsert: true` option for the `update` operation to either update a matching document or, if no matching document exists, create a new document:

```javascript
db.runCommand(
               {
                 findAndModify: "people",
                 query: { name: "Gus", state: "active", rating: 100 },
                 sort: { rating: 1 },
                 update: { $inc: { score: 1 } },
                 upsert: true
               }
             )
```

If the command finds a matching document, the command performs an update.

If the command does **not** find a matching document, the `update` with `upsert: true <upsert>` operation results in an insertion and returns a document with the following fields:

- The `lastErrorObject` field that contains the details of the
command, including the field `upserted that contains the id` value of the newly inserted document, and

- The `value` field containing `null`.
```bash
{
  "value" : null,
  "lastErrorObject" : {
     "updatedExisting" : false,
     "n" : 1,
     "upserted" : ObjectId("54f62c8bc85d4472eadea26f")
  },
  "ok" : 1
}
```

### Return New Document

The following :dbcommand:`findAndModify` command includes both `upsert: true` option and the `new:true` option. The command either updates a matching document and returns the updated document or, if no matching document exists, inserts a document and returns the newly inserted document in the `value` field.

In the following example, no document in the `people` collection matches the `query` condition:

```javascript
db.runCommand(
   {
     findAndModify: "people",
     query: { name: "Pascal", state: "active", rating: 25 },
     sort: { rating: 1 },
     update: { $inc: { score: 1 } },
     upsert: true,
     new: true
   }
)
```

The command returns the newly inserted document in the `value` field:

```bash
{
  "lastErrorObject" : {
     "connectionId" : 1,
     "updatedExisting" : false,
     "upserted" : ObjectId("54f62bbfc85d4472eadea26d"),
     "n" : 1,
     "syncMillis" : 0,
     "writtenTo" : null,
     "err" : null,
     "ok" : 1
  },
  "value" : {
     "_id" : ObjectId("54f62bbfc85d4472eadea26d"),
     "name" : "Pascal",
     "rating" : 25,
     "state" : "active",
     "score" : 1
  },
  "ok" : 1
}
```

### Sort and Remove

By including a `sort` specification on the `rating` field, the following example removes from the `people` collection a single document with the `state` value of `active` and the lowest `rating` among the matching documents:

```javascript
db.runCommand(
   {
     findAndModify: "people",
     query: { state: "active" },
     sort: { rating: 1 },
     remove: true
   }
)
```

The command returns the deleted document:

```bash
{
  "lastErrorObject" : {
     "connectionId" : 1,
     "n" : 1,
     "syncMillis" : 0,
     "writtenTo" : null,
     "err" : null,
     "ok" : 1
  },
  "value" : {
     "_id" : ObjectId("54f62a6785e4be1f982b9c9b"),
     "name" : "XYZ123",
     "score" : 1,
     "state" : "active",
     "rating" : 3
  },
  "ok" : 1
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
db.runCommand(
   {
     findAndModify: "myColl",
     query: { category: "cafe", status: "a" },
     sort: { category: 1 },
     update: { $set: { status: "Updated" } },
     collation: { locale: "fr", strength: 1 }
   }
)
```

The operation returns the following document:

```javascript
{
   "lastErrorObject" : {
      "updatedExisting" : true,
      "n" : 1
   },
   "value" : {
      "_id" : 1,
      "category" : "café",
      "status" : "A"
   },
   "ok" : 1
}
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

To update all elements that are greater than or equal to `100` in the `grades` array, use the positional :update:`$[\<identifier\>]` operator with the `arrayFilters` option:

```javascript
db.runCommand(
   {
     findAndModify: "students",
     query: { grades: { $gte: 100 } },
     update:  { $set: { "grades.$[element]" : 100 } },
     arrayFilters: [ { "element": { $gte: 100 } } ]
   }
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

The following operation finds a document where the `_id` field equals `1` and uses the filtered positional operator :update:`$[\<identifier\>]` with the `arrayFilters` to update the `mean` for all elements in the `grades` array where the grade is greater than or equal to `85`.

```javascript
db.runCommand(
   {
     findAndModify: "students2",
     query: { _id : 1 },
     update: { $set: { "grades.$[elem].mean" : 100 } },
     arrayFilters: [ { "elem.grade": { $gte: 85 } } ] 
   }
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

:dbcommand:`findAndModify` can accept an aggregation pipeline for the update. The pipeline can consist of the following stages:

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
db.runCommand(
   {
     findAndModify: "students2",
     query: {  "_id" : 1 },
     update: [ { $set: { "total" : { $sum: "$grades.grade" } } } ],
     new: true
   }
)
```

> **Note:** The `$set` used in the pipeline refers to the aggregation stage
:pipeline:`$set` and not the update operator :update:`$set`.

After the operation, the collection has the following documents:

```javascript
{ 
  "_id" : 1, 
  "grades" : [ { "grade" : 80, "mean" : 75, "std" : 6 }, { "grade" : 85, "mean" : 90, "std" : 4 }, { "grade" : 85, "mean" :85, "std" : 6 } ], 
  "total" : 250
}
{
   "_id" : 2,
   "grades" : [ { "grade" : 90, "mean" : 75, "std" : 6 }, { "grade" : 87, "mean" : 90, "std" : 3 }, { "grade" : 85, "mean" : 85,"std" : 4 } ]
}
```

### Specify `hint` for `findAndModify` Operations

In :binary:`~bin.mongosh`, create a `members` collection with the following documents:

```javascript
db.members.insertMany( [
   { "_id" : 1, "member" : "abc123", "status" : "P", "points" :  0,  "misc1" : null, "misc2" : null },
   { "_id" : 2, "member" : "xyz123", "status" : "A", "points" : 60,  "misc1" : "reminder: ping me at 100pts", "misc2" : "Some random comment" },
   { "_id" : 3, "member" : "lmn123", "status" : "P", "points" :  0,  "misc1" : null, "misc2" : null },
   { "_id" : 4, "member" : "pqr123", "status" : "D", "points" : 20,  "misc1" : "Deactivated", "misc2" : null },
   { "_id" : 5, "member" : "ijk123", "status" : "P", "points" :  0,  "misc1" : null, "misc2" : null },
   { "_id" : 6, "member" : "cde123", "status" : "A", "points" : 86,  "misc1" : "reminder: ping me at 100pts", "misc2" : "Some random comment" }
] )
```

Create the following indexes on the collection:

```javascript
db.members.createIndex( { status: 1 } )
db.members.createIndex( { points: 1 } )
```

The following operation explicitly hints to use the index `{ status: 1 }`:

```javascript
db.runCommand({
   findAndModify: "members",
   query: { "points": { $lte: 20 }, "status": "P" },
   remove: true,
   hint: { status: 1 }
})
```

> **Note:** If you specify an index that does not exist, the operation errors.

To see the index used, run :dbcommand:`explain` on the operation:

```javascript
db.runCommand(
   {
     explain: {
       findAndModify: "members",
       query: { "points": { $lte: 20 }, "status": "P" },
       remove: true,
       hint: { status: 1 }
     },
     verbosity: "queryPlanner"
   }
)
```

### Use Variables in `let`

.. include:: /includes/let-example-introduction.rst

.. include:: /includes/let-example-find-modify-flavors.rst

```javascript
db.cakeFlavors.runCommand( {
   findAndModify: db.cakeFlavors.getName(),
   query: { $expr: { $eq: [ "$flavor", "$$targetFlavor" ] } },
   update: { flavor: "orange" },
   let: { targetFlavor: "cherry" }
} )
```
