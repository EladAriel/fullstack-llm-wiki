---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.updateMany.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================================

# db.collection.updateMany() (mongosh method)

.. include:: includes/wayfinding/mongosh-method-updateMany.rst

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The :method:`~db.collection.updateMany()` method has the following form:

```javascript
db.collection.updateMany(
   <filter>,
   <update>,
   {
     upsert: <boolean>,
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

The :method:`~db.collection.updateMany()` method takes the following parameters:

### Returns

The method returns a document that contains:

- A boolean `acknowledged` as `true` if the operation ran with
`write concern` or `false` if write concern was disabled

- `matchedCount` containing the number of matched documents
- `modifiedCount` containing the number of modified documents
- `upsertedId containing the id` for the upserted document
- `upsertedCount` containing the number of upserted documents
## Access Control

On deployments running with :setting:`~security.authorization`, the user must have access that includes the following privileges:

- :authaction:`update` action on the specified collection(s).
- :authaction:`find` action on the specified collection(s).
- :authaction:`insert` action on the specified collection(s) if the
operation results in an upsert.

The built-in role :authrole:`readWrite` provides the required privileges.

## Behavior

`updateMany()` finds all documents in the collection that match the `filter` and applies modifications specified by the `update` parameter.

`updateMany()` modifies each document individually. Each document write is an `atomic operation`, but `updateMany()` as a whole is not atomic. If your use case requires atomicity of writes to multiple documents, use `<transactions>`.

If a single document update fails, all document updates written before the failure are retained, but any remaining matching documents are not updated. For details on this behavior, see `<multi-update-failures>`.

> **Seealso:** `<updateMany-sharded-collection>` for more information about
`updateMany()` behavior in sharded collections.

### Limitations

- `updateMany()` should only be used for `idempotent`
operations.

### Upsert

If `upsert: true` and no documents match the `filter`, :method:`db.collection.updateMany()` creates a new document based on the `filter` and `update` parameters.

If you specify `upsert: true` on a sharded collection, you must include the full shard key in the `filter`. For additional :method:`db.collection.updateMany()` behavior, see `updateMany-sharded-collection`.

See `updateMany-example-update-multiple-documents-with-upsert`.

### Update with an Update Operator Expressions Document

For the modification specification, the :method:`db.collection.updateMany()` method can accept a document that only contains `update operator <update-operators>` expressions to perform.

For example:

```javascript
db.collection.updateMany( 
   <query>,
   { $set: { status: "D" }, $inc: { quantity: 2 } },
   ...
)
```

### Update with an Aggregation Pipeline

The :method:`db.collection.updateMany()` method can accept an `aggregation pipeline <aggregation-pipeline>` `[ <stage1>, <stage2>, ... ]` that specifies the modifications to perform. The pipeline can consist of the following stages:

.. include:: /includes/list-update-agg-stages.rst

Using the aggregation pipeline allows for a more expressive update statement, such as expressing conditional updates based on current field values or updating one field using the value of another field(s).

For example:

```javascript
db.collection.updateMany( 
   <query>,
   [ 
      { $set: { status: "Modified", comments: [ "$misc1", "$misc2" ] } }, 
      { $unset: [ "misc1", "misc2" ] } 
   ]
   ...
)
```

> **Note:** .. include:: /includes/set-aggregation-versus-update.rst

For examples, see `updateMany-example-agg`.

### Capped Collections

.. include:: /includes/extracts/capped-collection-immutable-document-size-update.rst

### Time Series Collections

The :method:`~db.collection.updateMany()` method is available for `time series collections <time series collection>` starting in MongoDB 5.1.

Update commands must meet the following requirements:

.. include:: /includes/time-series/fact-update-limitations.rst

### Sharded Collections

`updateMany()` exhibits the following behaviors when used with sharded collections:

- `updateMany()` operations that include `upsert: true` must
include the full shard key in the `filter`.

- If you attempt to run `updateMany()` during a
`<sharding-chunk-migration>` or a `shard key value update <update-shard-key>`, the operation can miss documents in some scenarios. To ensure all documents are updated, use idempotent updates and rerun the command until no further updates are applied. For more information on idempotent updates with `updateMany()`, see `<updateMany-example-idempotent>`.

.. include:: /includes/method-targets-all-shards-if-no-txn.rst

### Explainability

:method:`~db.collection.updateMany()` is not compatible with :method:`db.collection.explain()`.

### Transactions

.. include:: /includes/extracts/transactions-supported-operation.rst

.. include:: /includes/extracts/transactions-usage.rst

Upsert within Transactions ``````````````````````````

.. include:: /includes/extracts/transactions-upsert-availability.rst

Write Concerns and Transactions ````````````````````````````````

.. include:: /includes/extracts/transactions-operations-write-concern.rst

### Oplog Entries

`updateMany()` adds an entry to the `oplog` (operations log) for each successfully updated document. If no documents are updated, `updateMany()` does not add entries to the oplog.

## Examples

.. include:: /includes/sample-data-usage.rst

### Idempotent Updates

The `sample_mflix.movies` collection contains movies with IMDB ratings. This `idempotent` update does the following operations:

- matches all movies with IMDB ratings less than 3.0
- increments those ratings by 0.5
- sets a `ratingBoosted` field to `true`
`updateMany()` modifies the matching movie documents individually. The individual document updates are atomic operations, but the `updateMany()` operation as a whole is not atomic.

If the operation fails to update all matched documents, you can safely rerun an idempotent command until no additional documents match the specified filter. In this case, each document's `imdb.rating` field is only updated one time regardless of how many times it is retried because the command is idempotent.

### Update Multiple Documents

The `sample_mflix.movies` collection contains movies with a `num_mflix_comments` field.

The following operation finds all movies with more than 100 comments and adds a `popular` flag to those movies:

### Update with Aggregation Pipeline

The :method:`db.collection.updateMany()` can use an aggregation pipeline for the update. The pipeline can consist of the following stages:

.. include:: /includes/list-update-agg-stages.rst

Using the aggregation pipeline allows for a more expressive update statement, such as expressing conditional updates based on current field values or updating one field using the value of another field(s).

Example 1: Update with Aggregation Pipeline Using Existing Fields `````````````````````````````````````````````````````````````````

The following example uses the aggregation pipeline to modify a field using the values of the other fields in the document.

This pipeline:

- combines the IMDB and Tomatoes viewer ratings into a new `combinedRatings` array field
- sets the `ratingsUpdated` field
- removes the original `imdb.rating` and `tomatoes.viewer.rating` fields for all
matching documents

> **Note:** .. include:: /includes/set-aggregation-versus-update.rst

First Stage The :pipeline:`$set` stage:

- creates a new array field `combinedRatings` whose elements are the current
content of the `imdb.rating` and `tomatoes.viewer.rating` fields

- sets the field `ratingsUpdated` to the value of the aggregation
variable :variable:`NOW`.

Second Stage The :pipeline:`$unset` stage removes the `imdb.rating` and `tomatoes.viewer.rating` fields.

After the command, matching movies from the 2010s have a `combinedRatings` array with both rating values and a timestamp.

Example 2: Update with Aggregation Pipeline Using Existing Fields Conditionally ```````````````````````````````````````````````````````````````````````````````

Using an aggregation pipeline, you can update movies from the 2010s with a calculated combined rating score (averaging IMDB and Tomatoes viewer ratings) and assign a letter grade based on that score.

> **Note:** .. include:: /includes/set-aggregation-versus-update.rst

First Stage The :pipeline:`$set` stage:

- calculates a new field `combinedScore` based on the average of the
`imdb.rating` and `tomatoes.viewer.rating` fields. See :group:`$avg` for more information on the `$avg` aggregation operator and :expression:`$trunc` for more information on the `$trunc` truncate aggregation operator.

- sets the field `scoreUpdated` to the value of the aggregation
variable :variable:`NOW`.

Second Stage The :pipeline:`$set` stage calculates a new field `ratingGrade` based on the `combinedScore` field calculated in the previous stage. See :expression:`$switch` for more information on the `$switch` aggregation operator.

After the command, matching movies have a combined score and letter grade.

> **Seealso:** `/tutorial/update-documents-with-aggregation-pipeline`

### Update Multiple Documents with Upsert

The following operation updates all movies released after 2020 and directed by Christopher Nolan:

In this example, since no documents match the filter, and `upsert` is `true`, :method:`~db.collection.updateMany inserts a new document with a generated id` as well as the equality conditions from the `filter`, and the `update` modifiers.

### Update with Write Concern

Given a three member replica set, the following operation specifies a `w` of `majority` and `wtimeout` of `100`:

If the acknowledgment takes longer than the `wtimeout` limit, MongoDB throws an exception.

The following table explains the possible values of `errInfo.writeConcern.provenance`:

.. include:: /includes/fact-wc-provenance-table.rst

### Specify Collation

.. include:: /includes/extracts/collation-description.rst

The following operation uses a case-insensitive collation to match movies with the genre "drama" with any combination of lowercase and uppercase.

### Specify `arrayFilters` for an Array Update Operations

.. include:: /includes/extracts/arrayFilters-blurb.rst

Update Elements Match `arrayFilters` Criteria ```````````````````````````````````````````````

Add a `ratings` array to some movies by combining their various rating scores:

To update all ratings that are greater than or equal to `100` in the `ratings` array, use the filtered positional operator :update:`$[\<identifier\>]` with the `arrayFilters` option:

After the operation, all rating values greater than or equal to 100 in the `ratings` arrays are set to 100.

Update Specific Elements of an Array of Documents `````````````````````````````````````````````````

Add a `ratingDetails` array to movies with individual rating sources:

To modify the value of the `weight` field to 10 for all elements in the `ratingDetails` array where the score is greater than or equal to `8`, use the filtered positional operator :update:`$[\<identifier\>]` with `arrayFilters`:

After the operation, all rating sources with scores less than or equal to 8 have their weight set to 10.

### Specify `hint` for Update Operations

Create the following index on the collection:

The following update operation explicitly hints to use the index `{ rated: 1 }`:

> **Note:** If you specify an index that does not exist, the operation errors.

To see if the hinted index is used, run the :pipeline:`$indexStats` pipeline:

### Write Concern Errors in Sharded Clusters

.. include:: /includes/fact-update-writeConcernError-mongos.rst

### User Roles and Document Updates

.. include:: /includes/user-roles-system-variable-update-example-introduction.rst

.. include:: /includes/user-roles-system-variable-update-example-middle.rst

.. include:: /includes/user-roles-system-variable-update-example-end.rst
