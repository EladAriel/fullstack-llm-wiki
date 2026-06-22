---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/update.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================

# update (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

.. versionchanged:: 8.0

The command has the following syntax:

```javascript
db.runCommand(
   {
      update: <collection>,
      updates: [
         {
           q: <query>,
           u: <document or pipeline>,
           c: <document>, // Added in MongoDB 5.0
           upsert: <boolean>,
           multi: <boolean>,
           collation: <document>,
           arrayFilters: <array>,
           hint: <document|string>,
           sort: <document>
         },
         ...
      ],
      ordered: <boolean>,
      maxTimeMS: <integer>,
      writeConcern: { <write concern> },
      bypassDocumentValidation: <boolean>,
      comment: <any>,
      let: <document> // Added in MongoDB 5.0
   }
)
```

## Command Fields

The command takes the following fields:

### Update Statements

Each element of the `updates` array is an update statement document. Each document contains the following fields:

### Returns

The command returns a document that contains the status of the operation. For example:

```javascript
{
   "ok" : 1,
   "nModified" : 0,
   "n" : 1,
   "upserted" : [
      {
         "index" : 0,
         "_id" : ObjectId("52ccb2118908ccd753d65882")
      }
   ]
}
```

For details of the output fields, see `update-command-output`.

## Access Control

On deployments running with :setting:`~security.authorization`, the user must have access that includes the following privileges:

- :authaction:`update` action on the specified collection(s).
- :authaction:`find` action on the specified collection(s).
- :authaction:`insert` action on the specified collection(s).
The built-in role :authrole:`readWrite` provides the required privileges.

## Behavior

### Limitations

If you set `multi: true`, use the `update` command only for `idempotent` operations.

### Update with an Update Operator Expressions Document

The update statement field `u <update-command-u>` can accept a document that only contains `update operator <update-operators>` expressions. For example:

```javascript
updates: [
   {
     q: <query>,
     u: { $set: { status: "D" }, $inc: { quantity: 2 } },
      ...
   },
   ...
]
```

Then, the :dbcommand:`update` command updates only the corresponding fields in the document.

### Update with a Replacement Document

The update statement field `u <update-command-u>` field can accept a replacement document, i.e. the document contains only `field:value` expressions. For example:

```javascript
updates: [
   {
      q: <query>,
      u: { status: "D", quantity: 4 },
      ...
   },
   ...
]
```

Then the :dbcommand:`update` command replaces the matching document with the update document. The :dbcommand:`update` command can only replace a single matching document; i.e. the `multi` field cannot be `true`. The :dbcommand:`update command does not replace the id` value.

### Multi-Update Failures

If a single document fails to update in an update command with the `multi` parameter set to `true`, no further documents update as part of that command.

For example, the `sample_mflix.movies` collection contains movies with `imdb.rating` fields. Create a `document validator <schema-validation-overview>` on the `movies` collection with a rule that the `imdb.rating` value must be less than or equal to `10`:

If any movie already has a rating of `10`, incrementing it would violate the validator rule (rating > 10). When this happens, the update stops and no further documents are updated, even if thousands of documents matched the query.

> **Note:** .. include:: /includes/multi-update-nModified-clarification.rst

### Update with an Aggregation Pipeline

The update statement field `u <update-command-u>` field can accept an `aggregation pipeline <aggregation-pipeline>` `[ <stage1>, <stage2>, ... ]` that specifies the modifications to perform. The pipeline can consist of the following stages:

.. include:: /includes/list-update-agg-stages.rst

Using the aggregation pipeline allows for a more expressive update statement, such as expressing conditional updates based on current field values or updating one field using the value of another field(s).

For example:

```javascript
updates: [
   {
      q: <query>,
      u: [ 
        { $set: { status: "Modified", comments: [ "$misc1", "$misc2" ] } }, 
        { $unset: [ "misc1", "misc2" ] } 
      ],
      ...
   },
   ...
]
```

> **Note:** The `$set` and `$unset` used in the pipeline refers to the
aggregation stages :pipeline:`$set` and :pipeline:`$unset`
respectively, and not the update operators :update:`$set` and :update:`$unset`.

For examples, see `update-command-example-agg`.

### Upsert with Unique Index

.. include:: /includes/extracts/upsert-unique-index-update-command.rst

### Limits

For each update element in the `updates` array, the sum of the query and the update sizes (i.e. `q` and `u` ) must be less than or equal to the :limit:`maximum BSON document size <BSON Document Size>`.

The total number of update statements in the `updates` array must be less than or equal to the :limit:`maximum bulk size <Write Command Batch Limit Size>`.

### Schema Validation

.. include:: /includes/extracts/bypassDocumentValidation-update.rst

### Sharded Collections

`upsert` on a Sharded Collection ``````````````````````````````````

To use :dbcommand:`update` with `multi: false` on a sharded collection,

- If you do not specify `upsert: true <update-command-upsert>`,
the filter `q <update-command-q> must either include an equality match on the id` field or target a single shard (such as by including the shard key).

- If you specify `upsert: true <update-command-upsert>`, the
filter `q <update-command-q>` must include an equality match on the shard key.

.. include:: /includes/extracts/missing-shard-key-equality-condition-update.rst

Replace Document ````````````````

When replacing a document, :dbcommand:`update`  attempts to target a shard, first by using the query filter. If the operation cannot target a single shard by the query filter, it then attempts to target by the replacement document.

Shard Key Modification ``````````````````````

.. include:: /includes/limits-sharding-shardkey-document-immutable.rst

To modify the **existing** shard key value with :dbcommand:`update`:

- You :red:`must` run on a :binary:`~bin.mongos`. Do :red:`not`
issue the operation directly on the shard.

- You :red:`must` run either in a :doc:`transaction
</core/transactions>` or as a `retryable write </core/retryable-writes>`.

- You :red:`must` specify `multi: false`.
- You :red:`must` include an equality :ref:`query filter
<update-command-q>` on the full shard key.

> **Tip:** .. include:: /includes/extracts/missing-shard-key-equality-condition-abridged.rst

See also `cmd-update-sharded-upsert`.

Missing Shard Key `````````````````

Documents in a sharded collection can be `missing the shard key fields <shard-key-missing>`. To use :dbcommand:`update` to set the document's **missing** shard key, you :red:`must` run on a :binary:`~bin.mongos`. Do :red:`not` issue the operation directly on the shard.

In addition, the following requirements also apply:

> **Tip:** .. include:: /includes/extracts/missing-shard-key-equality-condition-abridged.rst

Slow Query Logs ```````````````

If an `update` operation on a sharded cluster exceeds the `slow operation threshold <slowms-threshold-option>`, MongoDB adds a `log message <log-messages-ref>` that contains a `routerQueryShapeHash` field. This field contains the query shape of the operation on the :program:`mongos`  before the `mongos` sends the operation to the :program:`mongod`.

> **Note:** The query shape of the operation on the `mongos` may differ from the query
shape on the `mongod`.

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

## Examples

.. include:: /includes/sample-data-usage.rst

### Update Specific Fields of One Document

Use `update operators <update-operators>` to update only the specified fields of a document.

For example, documents in the `movies` collection from the `sample_mflix` database contain fields such as `title`, `year`, and `num_mflix_comments`.

The following command uses the :update:`$set` and :update:`$inc` update operators to update the `year` and the `num_mflix_comments` fields of a document where the `title` equals `"The Godfather"`:

Because `<update>` document does not specify the optional `multi` field, the update only modifies one document, even if more than one document matches the `q` match condition.

See `update-command-output` for details.

### Update Specific Fields of Multiple Documents

Use `update operators <update-operators>` to update only the specified fields of a document, and include the `multi` field set to `true` in the update statement.

For example, documents in the `movies` collection from the `sample_mflix` database contain fields such as `year` and `num_mflix_comments`.

The following command uses the :update:`$inc` update operator to increment the `num_mflix_comments` field for all movies released in 1924:

Because the `multi` field is set to `true`, the update modifies all 6 documents that match the query specified in the `q` field and returns the following output:

See `update-command-output` for details.

### Update with Aggregation Pipeline

The :dbcommand:`update` command can use an aggregation pipeline for the update. The pipeline can consist of the following stages:

.. include:: /includes/list-update-agg-stages.rst

Using the aggregation pipeline allows for a more expressive update statement, such as expressing conditional updates based on current field values or updating one field using the value of another field(s).

Example 1 `````````

The following examples uses the aggregation pipeline to modify a field using the values of the other fields in the document.

Documents in the `users` collection from the `sample_mflix` database contain fields such as `name` and `email`.

The following update operation uses an aggregation pipeline to add new fields to a specific user's document:

> **Note:** The `$set` operation used in the pipeline refers to the aggregation stage
:pipeline:`$set` and not the update operator :update:`$set`.

Example 2 `````````

The aggregation pipeline allows the update to perform conditional updates based on the current field values as well as use current field values to calculate a separate field value.

Documents in the `movies` collection from the `sample_mflix` database have a `year` field.

The following example uses an aggregation pipeline to calculate the age of "The Great Train Robbery" and assign an era classification based on when it was released.

> **Note:** The `$set` used in the pipeline refers to the aggregation stage
:pipeline:`$set`, and not the update operators :update:`$set`.

First Stage The :pipeline:`$set` stage calculates a new field `age` based on the difference between 2026 and the movie's release year. See :expression:`$subtract` for more information.

Second Stage The :pipeline:`$set` stage calculates a new field `era` based on the `year` field using conditional logic. See :expression:`$switch` for more information on the `$switch` aggregation operator.

### Bulk Update

The following example performs multiple update operations in a single command to both update existing documents and insert new documents. The operation:

- marks highly-rated Horror movies from 2015 as `featured`
- categorizes short Drama and Romance movies from 2012 as `melodrama`
- upserts a new Science Fiction movie from 2024 if it doesn't exist
The returned document shows that the command modified existing documents and inserted a new document via upsert. See `update-command-output` for details.

### Specify Collation

.. include:: /includes/extracts/collation-description.rst

Documents in the `movies` collection from the `sample_mflix` database have fields such as `title` and `year`.

The following operation uses collation to perform a case-insensitive search. The query searches for `"the godfather"` in lowercase, but with `strength: 1` collation, the query matches `"The Godfather"` regardless of capitalization:

### Specify `arrayFilters` for Array Update Operations

.. include:: /includes/extracts/arrayFilters-blurb.rst

Update Elements Match `arrayFilters` Criteria ```````````````````````````````````````````````

Documents in the `movies` collection from the `sample_mflix` database have a `languages` array field.

The following example updates all movies that have `"English"` in their `languages` array. The operation replaces `"English"` with `"EN"`.

Update Specific Elements of an Array of Documents `````````````````````````````````````````````````

Documents in the `movies` collection from the `sample_mflix` database have a `cast` array that lists actor names.

The following example finds a movie with the title `"The Godfather"` and replaces `"Al Pacino"` with `"REDACTED"` in its `cast` array. The `arrayFilters` option specifies which array elements to update:

### Specify `hint` for Update Operations

Documents in the `movies` collection from the `sample_mflix` database have fields such as `year` and `num_mflix_comments`.

Create the following indexes on the collection:

The following update operation increments the `num_mflix_comments` field for "The Great Train Robbery" and explicitly hints to use the index `{ year: 1 }`:

> **Note:** If you specify an index that does not exist, the operation errors.

To see the index used, you can run :dbcommand:`explain` on an update operation. For example, the following explains an update that increments `num_mflix_comments` for movies with 5 or fewer comments released in 2000 or later:

The :dbcommand:`explain` does not modify the documents.

### Use Variables in `let` Option or `c` Field

.. versionadded:: 5.0

Variables can be defined in the `let <update-let-syntax>` option or the `c <update-command-c>` field and accessed in the `updates` array.

> **Note:** To filter results using a variable, you must access the variable
within the :query:`$expr` operator.

Documents in the `movies` collection from the `sample_mflix` database have fields such as `title` and `year`.

The following example uses the `let` option to define variables for finding and adding a new field to a movie.

The next example defines `movieTitle` and `franchiseName` variables in `c` and uses the variables to add a `franchise` field.

## Output

The returned document contains a subset of the following fields:

.. include:: /includes/fact-update-writeConcernError-mongos.rst

In addition to the aforementioned update specific return fields, the :method:`db.runCommand()` includes additional information:

- for replica sets: `optime`, `electionId`, `$clusterTime`, and
`operationTime`.

- for sharded clusters: `operationTime` and `$clusterTime`.
See `db.runCommand Response <command-response>` for details on these fields.

### Update Operation with a Sort

Documents in the `movies` collection from the `sample_mflix` database have fields such as `year`, `title`, and `num_mflix_comments`.

The following example finds all movies from 1972 and updates the one with the most comments.

```javascript
db.runCommand( {
   update: "movies",
   updates: [ {
      // Find movies from 1972
      q: { year: 1972 },

      // Add a classic_status field to the found movie
      u: { $set: { classic_status: "Most Discussed 1972 Film" } },

      // Only update one movie
      multi: false,

      // Sort movies by comment count in descending order
      sort: { num_mflix_comments: -1 }
   } ]
} )
```

The operation updates only the 1972 movie with the most comments.
