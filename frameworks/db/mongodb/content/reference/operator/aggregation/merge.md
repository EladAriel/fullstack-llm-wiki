---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/merge.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# $merge (aggregation stage)

## Definition

> **Note:** This page describes the `$merge` stage, which outputs the
aggregation pipeline results to a collection. For the
:expression:`$mergeObjects` operator, which merges documents into a
single document, see :expression:`$mergeObjects`.

> **Note:** `$merge` can incorporate the pipeline results into an
existing output collection rather than perform a full replacement of
the collection. This functionality allows users to create on-demand
materialized views, where the content of the output collection is
incrementally updated when the pipeline is run.
For more information on this use case, see
`/core/materialized-views` as well as the examples on this page.
Materialized views are separate from read-only views. For
information on creating read-only views, see :doc:`read-only views
</core/views>`.

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

`$merge` has the following syntax:

```javascript
{ $merge: {
     into: <collection> -or- { db: <db>, coll: <collection> },
     on: <identifier field> -or- [ <identifier field1>, ...],  // Optional
     let: <variables>,                                         // Optional
     whenMatched: <replace|keepExisting|merge|fail|pipeline>,  // Optional
     whenNotMatched: <insert|discard|fail>                     // Optional
} }
```

For example:

```javascript
{ $merge: { into: "myOutput", on: "_id", whenMatched: "replace", whenNotMatched: "insert" } }
```

If using all default options for `$merge`, including writing to a collection in the same database, you can use the simplified form:

```javascript
{ $merge: <collection> } // Output collection is in the same database
```

The `$merge` stage takes a document with the following fields:

## Considerations

### `_id` Field Generation

If the `_id` field is not present in a document from the aggregation pipeline results, the `$merge` stage generates it automatically.

For example, in the following aggregation pipeline, :pipeline:`$project excludes the id` field from the documents passed into `$merge`. When `$merge` writes these documents to the `"newCollection"`, `$merge generates a new id` field and value.

```javascript
db.movies.aggregate( [
   { $project: { _id: 0 } },
   { $merge : { into : "newCollection" } }
] )
```

### Create a New Collection if Output Collection is Non-Existent

The `$merge` operation creates a new collection if the specified output collection does not exist.

- The output collection is created when `$merge` writes
the first document into the collection and is immediately visible.

- If the aggregation fails, any writes completed by the
`$merge` before the error will not be rolled back.

> **Note:** For a `replica set <replica-set>` or a standalone, if the
output database does not exist, `$merge` also creates
the database.
For a `sharded cluster <sharded-cluster>`, the specified
output database must already exist.

If the output collection does not exist, `$merge` requires the `on <merge-on> identifier to be the id` field. To use a different `on` field value for a collection that does not exist, you can create the collection first by creating a unique index on the desired field(s) first. For example, if the output collection `newDailyCommentCount` does not exist and you want to specify the `commentDate` field as the `on <merge-on>` identifier:

```javascript
db.newDailyCommentCount.createIndex(
   { commentDate: 1 }, { unique: true } )

db.comments.aggregate( [
   { $match: { date: { $gte: new Date("2002-01-01"),
     $lt: new Date("2002-02-01") } } },
   { $group: { _id: { $dateToString: { format: "%Y-%m-%d",
     date: "$date" } }, count: { $sum: 1 } } },
   { $project: { _id: 0, commentDate: { $toDate: "$_id" },
     count: 1 } },
   { $merge : { into : "newDailyCommentCount",
     on: "commentDate" } }
] )
```

### Output to a Sharded Collection

The `$merge` stage can output to a sharded collection. When the output collection is sharded, `$merge uses the id` field and all the `shard key <sharding-shard-key-creation>` fields as the default `on <merge-on>` identifier. If you override the default, the `on <merge-on>` identifier must include all the `shard key <sharding-shard-key-creation>` fields:

```javascript
{ $merge: {
   into: "<shardedColl>" or { db:"<sharding enabled db>", coll: "<shardedColl>" },
   on: [ "<shardkeyfield1>", "<shardkeyfield2>",... ], // Shard key fields and any additional fields
   let: <variables>,                                         // Optional
   whenMatched: <replace|keepExisting|merge|fail|pipeline>,  // Optional
   whenNotMatched: <insert|discard|fail>                     // Optional
} }
```

For example, use the :method:`sh.shardCollection()` method to create a new sharded collection `moviesByYearAndRating` with the `rated` field as the shard key.

```javascript
sh.shardCollection(
   "sample_mflix.moviesByYearAndRating",  // Namespace of the collection to shard
   { rated: 1 },                       // Shard key
);
```

The `moviesByYearAndRating` collection will contain documents with movie statistics by year (`year` field) and content rating (shard key); specifically, the `on <merge-on>` identifier is `["year", "rated"]` (the ordering of the fields does not matter). Because `$merge` requires a unique index with keys that correspond to the `on <merge-on>` identifier fields, create the unique index (the ordering of the fields do not matter): [#uniqueoption]_

```javascript
db.moviesByYearAndRating.createIndex(
   { rated: 1, year: 1 }, { unique: true } )
```

With the sharded collection `moviesByYearAndRating` and the unique index created, you can use `$merge` to output the aggregation results to this collection, matching on `[ "year", "rated" ]` as in this example:

```javascript
db.movies.aggregate( [
   { $match: { rated: { $ne: null }, year: { $ne: null } } },
   { $group: {
      _id: { year: "$year", rated: "$rated" },
      movieCount: { $sum: 1 } } },
   { $project: { _id: 0, year: "$_id.year", rated: "$_id.rated",
     movieCount: 1 } },
   { $merge: { into: "moviesByYearAndRating",
     "on": [ "year", "rated" ], whenMatched: "replace",
     whenNotMatched: "insert" } }
] )
```

The :method:`sh.shardCollection()` method can also create a unique index on the shard key when passed the `{ unique: true }` option if: the shard key is `range-based </core/ranged-sharding>`, the collection is empty, and a unique index on the shard key doesn't already exist.

In the previous example, because the `on` identifier is the shard key and another field, a separate operation to create the corresponding index is required.

### Replace Documents (`$merge`) vs Replace Collection (`$out`)

`$merge` can replace an existing document in the output collection if the aggregation results contain a document or documents that match based on the `on <merge-on>` specification. As such, `$merge` can replace all documents in the existing collection if the aggregation results include matching documents for all existing documents in the collection and you specify `"replace" <merge-whenMatched-replace>` for `whenMatched <merge-whenMatched>`.

However, **to replace an existing collection** regardless of the aggregation results, use :pipeline:`$out` instead.

### Existing Documents and `_id` and Shard Key Values

The `$merge` errors if the `$merge results in a change to an existing document's id` value.

> **Tip:** To avoid this error, if the `on <merge-on>` field does not
include the `_id field, remove the id` field in the
aggregation results to avoid the error, such as with a preceding
:pipeline:`$unset` stage, and so on.
Additionally, for a sharded collection, `$merge` also
generates an error if it results in a change to the shard key value
of an existing document.
Any writes completed by the `$merge` before the error will
not be rolled back.

### Unique Index Constraints

If the unique index used by `$merge` for `on <merge-on>` field(s) is dropped mid-aggregation, there is no guarantee that the aggregation will be killed. If the aggregation continues, there is no guarantee that documents do not have duplicate `on` field values.

If the `$merge` attempts to write a document that violates any unique index on the output collection, the operation generates an error. For example:

- :ref:`Insert a non-matching document
<merge-whenNotMatched-insert>` that violates a unique index other than the index on the `on <merge-on>` field(s).

- `Fail <merge-whenMatched-fail>` if there is a matching
document in the collection. Specifically, the operation attempts to insert the matching document which violates the unique index on the `on <merge-on>` field(s).

- :ref:`Replace an existing document
<merge-whenMatched-replace>` with a new document that violates a unique index other than the index on the `on <merge-on>` field(s).

- `Merge the matching documents <merge-whenMatched-merge>` that
results in a document that violates a unique index other than the index on the `on <merge-on>` field(s).

### Schema Validation

If your collection uses `schema validation <schema-validation-overview>` and has `validationAction` set to `error`, inserting an invalid document or updating a document with invalid values with `$merge` throws a `MongoServerError` and the document is not written to the target collection. If there are multiple invalid documents, only the first invalid document encountered throws an error. All valid documents are written to the target collection, and all invalid documents fail to write.

### `whenMatched` Pipeline Behavior

`$merge` inserts the document directly into the output collection when all of the following are true:

- The value of `whenMatched <merge-whenMatched>` is an
aggregation pipeline.

- The value of `whenNotMatched <merge-whenNotMatched>` is
`insert`.

- There is no match for a document in the output collection.
### `$merge` and `$out` Comparison

With the introduction of `$merge`, MongoDB provides two stages, `$merge` and :pipeline:`$out`, for writing the results of the aggregation pipeline to a collection:

### Output to the Same Collection that is Being Aggregated

.. include:: /includes/fact-merge-same-collection-warning.rst

.. include:: /includes/fact-merge-same-collection-behavior.rst

## Restrictions

## Examples
