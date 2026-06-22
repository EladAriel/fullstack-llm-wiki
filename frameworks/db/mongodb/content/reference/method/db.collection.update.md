---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.update.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================================

# db.collection.update() (mongosh method)

.. include:: /includes/fact-mongosh-shell-method-deprecated.rst

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

.. versionchanged:: 5.0

The :method:`db.collection.update()` method has the following form:

```javascript
db.collection.update(
   <query>,
   <update>,
   {
     upsert: <boolean>,
     multi: <boolean>,
     writeConcern: <document>,
     collation: <document>,
     arrayFilters: [ <filterdocument1>, ... ],
     hint:  <document|string>,
     let: <document>,
     maxTimeMS: <int>,
     bypassDocumentValidation: <boolean>
   }
)
```

### Parameters

The :method:`db.collection.update()` method takes the following parameters:

### Returns

The method returns a `writeresults-update` document that contains the status of the operation.

## Access Control

On deployments running with :setting:`~security.authorization`, the user must have access that includes the following privileges:

- :authaction:`update` action on the specified collection(s).
- :authaction:`find` action on the specified collection(s).
- :authaction:`insert` action on the specified collection(s) if the
operation results in an upsert.

The built-in role :authrole:`readWrite` provides the required privileges.

## Behavior

### Limitations

If you set `multi: true`, use the `update()` method only for `idempotent` operations.

### Using `$expr` in an Update with `Upsert`

Attempting to use the :manual:`$expr </reference/operator/query/expr/>` operator with the upsert flag set to `true` will generate an error.

### Sharded Collections

To use :method:`db.collection.update()` with `multi: false on a sharded collection, you must include an exact match on the id` field or target a single shard (such as by including the shard key).

When the :method:`db.collection.update()` performs update operations (and not document replacement operations), :method:`db.collection.update()` can target multiple shards.

> **Seealso:** :method:`~db.collection.findAndModify()`

Replace Document Operations on a Sharded Collection ```````````````````````````````````````````````````

Replace document operations attempt to target a single shard, first by using the query filter. If the operation cannot target a single shard by the query filter, it then attempts to target by the replacement document.

In earlier versions, the operation attempts to target using the replacement document.

`upsert` on a Sharded Collection ``````````````````````````````````

For a :method:`db.collection.update()` operation that includes `upsert: true <update-upsert>` and is on a sharded collection, you must include the full shard key in the `filter`:

- For an update operation.
- For a replace document operation.
.. include:: /includes/extracts/missing-shard-key-equality-condition-update.rst

Shard Key Modification ``````````````````````

.. include:: /includes/limits-sharding-shardkey-document-immutable.rst

To modify the **existing** shard key value with :method:`db.collection.update()`:

- You :red:`must` run on a :binary:`~bin.mongos`. Do :red:`not`
issue the operation directly on the shard.

- You :red:`must` run either in a :ref:`transaction
<transactions>` or as a `retryable write <retryable-writes>`.

- You :red:`must` specify `multi: false`.
- You :red:`must` include an equality :ref:`query filter
<update-query>` on the full shard key.

> **Tip:** .. include:: /includes/extracts/missing-shard-key-equality-condition-abridged.rst

See also `method-update-sharded-upsert`.

Missing Shard Key `````````````````

Documents in a sharded collection can be `missing the shard key fields <shard-key-missing>`. To use :method:`db.collection.update()` to set the document's **missing** shard key, you :red:`must` run on a :binary:`~bin.mongos`. Do :red:`not` issue the operation directly on the shard.

In addition, the following requirements also apply:

> **Tip:** .. include:: /includes/extracts/missing-shard-key-equality-condition-abridged.rst

See also:

- `method-update-sharded-upsert`
- `shard-key-missing`
### Transactions

.. include:: /includes/extracts/transactions-supported-operation.rst

.. include:: /includes/extracts/transactions-usage.rst

Upsert within Transactions ``````````````````````````

.. include:: /includes/extracts/transactions-upsert-availability.rst

Write Concerns and Transactions ````````````````````````````````

.. include:: /includes/extracts/transactions-operations-write-concern.rst

### Oplog Entries

If a `db.collection.update()` operation successfully updates one or more documents, the operation adds an entry on the `oplog` (operations log). If the operation fails or does not find any documents to update, the operation does not add an entry on the oplog.

### Upsert with Dotted `_id` Query

.. include:: /includes/fact-upsert-id.rst

### Upsert with Duplicate Values

Upserts can create duplicate documents, unless there is a `unique index <index-type-unique>` to prevent duplicates.

If all `db.collection.update()` operations finish the query phase before any client successfully inserts data, **and** there is no unique index on the `name` field, each `db.collection.update()` operation may result in an insert, creating multiple documents with `name: Andy`.

A unique index on the `name` field ensures that only one document is created. With a unique index in place, the multiple `db.collection.update()` operations now exhibit the following behavior:

- Exactly one `db.collection.update()` operation will successfully insert a new
document.

- Other `db.collection.update()` operations either update the newly-inserted
document or fail due to a unique key collision.

In order for other `db.collection.update()` operations to update the newly-inserted document, **all** of the following conditions must be met:

- The target collection has a unique index that would cause a
duplicate key error.

- The update operation is not `updateMany` or `multi` is
`false`.

- The update match condition is either:
- A single equality predicate. For example `{ "fieldA" : "valueA" }`
- A logical AND of equality predicates. For example ``{ "fieldA" :
"valueA", "fieldB" : "valueB" }``

- The fields in the equality predicate match the fields in the
unique index key pattern.

- The update operation does not modify any fields in the
unique index key pattern.

> **Seealso:** :update:`$setOnInsert`

### Array Update Operations

In the update document, use the :update:`$[\<identifier\>]` filtered positional operator to define an identifier, which you then reference in the array filter documents. You cannot have an array filter document for an identifier if the identifier is not included in the update document.

The `<identifier>` must begin with a lowercase letter and contain only alphanumeric characters.

You can include the same identifier multiple times in the update document; however, for each distinct identifier (`$[identifier]`) in the update document, you must specify **exactly one** corresponding array filter document. That is, you cannot specify multiple array filter documents for the same identifier. However, you can specify compound conditions on the same identifier in a single filter document

> **Note:** `arrayFilters` is not available for updates that use an
aggregation pipeline.

## WriteResult

### Successful Results

The :method:`db.collection.update()` method returns a :method:`WriteResult` object that contains the status of the operation. Upon success, the :method:`WriteResult` object contains the number of documents that matched the query condition, the number of documents inserted by the update, and the number of documents modified.

### Write Concern Errors

If the :method:`db.collection.update()` method encounters write concern errors, the results include the `WriteResult.writeConcernError` field.

The following table explains the possible values of `WriteResult.writeConcernError.provenance`:

.. include:: /includes/fact-wc-provenance-table.rst

### Errors Unrelated to Write Concern

If the :method:`db.collection.update()` method encounters a non-write concern error, the results include the `WriteResult.writeError` field.

## Examples

.. include:: /includes/sample-data-usage.rst

### Insert a New Document if No Match Exists (`Upsert`)

When you specify the option `upsert: true <update-upsert>`:

- If document(s) match the query criteria,
:method:`db.collection.update()` performs an update.

- If no document matches the query criteria,
:method:`db.collection.update()` inserts a single document.

> **Note:**   If multiple, identical `upserts <upsert>` are issued at
  roughly the same time, it is possible for
  :method:`~db.collection.update()` used with :ref:`upsert: true
  <update-upsert>` to create duplicate documents. See
  `update-with-unique-indexes` for more information.

If you specify `upsert: true` on a sharded collection, you must include the full shard key in the `filter`. For additional :method:`db.collection.update()` behavior on a sharded collection, see `update-sharded-collection`.

The following tabs showcase a variety of uses of the `upsert` modifier with :method:`~db.collection.update()`.

### Update with Aggregation Pipeline

The :method:`db.collection.update()` method can accept an `aggregation pipeline <aggregation-pipeline>` `[ <stage1>, <stage2>, ... ]` that specifies the modifications to perform. The pipeline can consist of the following stages:

.. include:: /includes/list-update-agg-stages.rst

Using the aggregation pipeline allows for a more expressive update statement, such as expressing conditional updates based on current field values or updating one field using the value of another field(s).

Modify a Field Using the Values of the Other Fields in the Document ```````````````````````````````````````````````````````````````````

The following example creates a `displayTitle` field that combines the movie's title and year with an aggregation pipeline that performs these operations:

- creates a `displayTitle` field by concatenating the `title` and `year`
fields

- sets a `lastModified` timestamp
> **Seealso:** `updates-agg-pipeline`

Perform Conditional Updates Based on Current Field Values `````````````````````````````````````````````````````````

The following example updates movies released in 2015 to calculate a combined rating score from IMDB and Tomatoes ratings, and assign a grade based on the score.

> **Note:** The `$set` used in the pipeline refers to the aggregation stage
:pipeline:`$set`, and not the update operators :update:`$set`.

The :pipeline:`$set` stage:

- calculates a new field `combinedScore` by averaging the IMDB rating
(scaled by 10) and Tomatoes viewer rating (scaled by 10), then rounding to one decimal place. See :group:`$avg`, :expression:`$multiply`, and :expression:`$round` for more information.

- sets the field `lastUpdate` to the value of the aggregation
variable :variable:`NOW`.

- assigns a letter grade based on the `combinedScore` using the
:expression:`$switch` operator.

> **Seealso:** `updates-agg-pipeline`

### Specify `arrayFilters` for Array Update Operations

Update Elements Match `arrayFilters` Criteria ```````````````````````````````````````````````

To update all array elements which match a specified criteria, use the `arrayFilters <update-array-filters>` parameter.

The following example updates all movies that have `"English"` in their `languages` array. The operation replaces `"English"` with `"EN"`.

Update Specific Elements of an Array Using Pattern Matching ```````````````````````````````````````````````````````````

You can also use the `arrayFilters <update-array-filters>` parameter with the filtered positional operator to update specific array elements that match a pattern.

The following example uses "The Godfather" movie from the existing collection, which has a `writers` array. The operation updates only the writers whose names contain "screenplay" by appending a suffix.

The operation targets "The Godfather" document and updates only array elements matching the filter criteria. After the operation, the writers who worked on the screenplay have " - UPDATED" appended.

### Specify `hint` for Update Operations

The `hint` option allows you to specify which index MongoDB should use for the update operation. This is useful when updating multiple documents and you want to ensure a specific index is used for performance. This example uses the existing `movies` collection from the sample_mflix database.

First, create an index on the `year` field:

The following update operation explicitly `hints <update-hint>` to use the `{ year: 1 }` index to update all movies from 2010-2015:

> **Note:** If you specify an index that does not exist, the operation errors.

To see the index used, run :dbcommand:`explain` on the operation:

The :method:`db.collection.explain().update() <db.collection.explain>` does not modify the documents.

### Use Variables in `let`

.. include:: /includes/let-example-introduction.rst

The example:

- Defines two variables in the `let` option: `targetTitle` (set to "The Matrix")
and `newTitle` (set to "The Matrix Reloaded")

- Uses `$expr` in the query filter to compare the document's `title` field
against the `$$targetTitle` variable

- Uses an aggregation pipeline with `$set` to update the `title` field to
the value of `$$newTitle`

### Override Default Write Concern

The following operation to a replica set specifies a `write concern <write-concern>` of `w: 2` with a `wtimeout` of 5000 milliseconds. This operation either returns after the write propagates to both the primary and one secondary, or times out after 5 seconds.

The operation successfully completes after the write is acknowledged by the primary and at least one secondary, as specified by `w: 2`.

### Write Concern Errors in Sharded Clusters

.. include:: /includes/fact-update-writeConcernError-mongos.rst

### Specify Collation

.. include:: /includes/extracts/collation-option.rst

This operation updates all movies with titles that start with `night` and uses `strength: 1` for case-insensitive comparison:
