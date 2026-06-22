---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/csfle/reference/supported-operations.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================================

# Supported Operations for Automatic Encryption

This page documents the specific commands, query operators, update operators, aggregation stages, and aggregation expressions supported by drivers configured for automatic {+csfle+}.

## Supported Read and Write Commands

Drivers using automatic {+csfle+} support the following commands:

- :dbcommand:`aggregate`
- :dbcommand:`count`
- :dbcommand:`delete`
- :dbcommand:`distinct`
- :dbcommand:`explain`
- :dbcommand:`find`
- :dbcommand:`findAndModify`
- :dbcommand:`insert`
- :dbcommand:`update`
For any supported command, drivers return an error if the command uses an unsupported operator, aggregation stage, or aggregation expression. For a complete list of the supported operators, stages, and expressions, see the following sections of this page:

- `Supported Query Operators <csfle-supported-query-operators>`
- `Supported Update Operators <csfle-supported-update-operators>`
- `Supported Aggregation Stages <csfle-supported-aggregation-stages>`
- `Supported Aggregation Expressions <csfle-supported-aggregation-expressions>`
The following commands do not require automatic encryption. Drivers configured for automatic {+csfle+} pass these commands directly to the :binary:`~bin.mongod`:

- :dbcommand:`getMore` [#]_
- :dbcommand:`authenticate`
- :dbcommand:`hello`
- :dbcommand:`logout`
- :dbcommand:`abortTransaction`
- :dbcommand:`commitTransaction`
- :dbcommand:`endSessions`
- :dbcommand:`startSession`
- :dbcommand:`create`
- :dbcommand:`createIndexes`
- :dbcommand:`drop`
- :dbcommand:`dropDatabase`
- :dbcommand:`dropIndexes`
- :dbcommand:`killCursors`
- :dbcommand:`listCollections`
- :dbcommand:`listDatabases`
- :dbcommand:`listIndexes`
- :dbcommand:`renameCollection`
- :dbcommand:`ping`
Issuing any other `command <database-commands>` through a driver configured for automatic {+csfle+} returns an error.

While automatic {+csfle+} ({+csfle-abbrev+}) does not encrypt the :dbcommand:`getMore` command, the response to the command may contain encrypted field values.

- Applications configured with the correct {+csfle-abbrev+} options
automatically decrypt those values.

- Applications without the correct {+csfle-abbrev+} options only see
the encrypted values.

## Supported Query Operators

Drivers configured for automatic {+csfle+} allow the following query operators when issued against `deterministically encrypted <csfle-deterministic-encryption>` fields:

- :query:`$eq`
- :query:`$ne`
- :query:`$in`
- :query:`$nin`
- :query:`$and`
- :query:`$or`
- :query:`$not`
- :query:`$nor`
Queries that compare an encrypted field to `null` or a regular expression always return an error even when using a supported query operator. Queries issuing these operators against a `randomly encrypted <csfle-random-encryption>` field return an error.

The :query:`$exists` operator has normal behavior when issued against both deterministically and randomly encrypted fields.

Queries specifying any other query operator against an encrypted field return an error.

The following query operators return an error even if not issued against an encrypted field:

- :query:`$text`
- :query:`$where`
- :query:`$jsonSchema`
> **Warning:** MongoDB stores client-side field level encrypted fields as a
:bsontype:`BinData <data_binary>` blob. Read and write operations
issued against the encrypted `BinData` value may have unexpected or
incorrect behavior as compared to issuing that same operation against
the decrypted value. Certain operations have strict BSON type support
where issuing them against a `BinData` value returns an error.
- Drivers using automatic {+csfle+} parse read and write operations
  for operators or expressions that do not support `BinData` values
  or that have unexpected behavior when issued against `BinData`
  values.
- Applications using explicit (manual) {+csfle+} may use this page
  as guidance for issuing read and write operations against encrypted
  fields.

## Unsupported Insert Operations

Drivers configured for automatic {+csfle+} do not support insert commands with the following behavior:

- Inserting a document with `Timestamp(0,0)` associated to an
encrypted field. The `(0,0)` value indicates that the :binary:`~bin.mongod` should generate the Timestamp. When the :binary:`~bin.mongod` cannot generated encrypted fields, the resulting timestamp is unencrypted.

- Inserting a document without an encrypted `_id` if the configured
automatic schema specifies an encrypted `_id` field. When the :binary:`~bin.mongod` automatically generates an unencrypted `ObjectId <objectid>, omitting id` from documents results in documents that do not conform to the automatic encryption rules.

- Inserting a document with an array associated to a
`deterministically encrypted <csfle-deterministic-encryption>` field. Automatic {+csfle+} does not support deterministically encrypting arrays.

## Supported Update Operators

Drivers configured for automatic {+csfle+} allow the following update operators when issued against `deterministically encrypted <csfle-deterministic-encryption>` fields:

- :update:`$set`
- :update:`$unset`
- :update:`$rename`
When you use the :update:`$rename` operator on encrypted fields, the automatic JSON schema must specify the same encryption metadata for the source and target field names.

Updates specifying any other update operator against an encrypted field return an error.

Update operations with the following behavior return an error even if using a supported operator:

- The update operation produces an array inside of an encrypted path.
- The update operation uses aggregation expression syntax.
For update operations specifying a `query filter <update-command-q>` on deterministically encrypted fields, the query filter must use only `supported operators <csfle-supported-query-operators>` on those fields.

## Supported Aggregation Stages

Drivers configured for automatic {+csfle+} support the following aggregation pipeline stages:

- :pipeline:`$addFields`
- :pipeline:`$bucket`
- :pipeline:`$bucketAuto`
- :pipeline:`$collStats`
- :pipeline:`$count`
- :pipeline:`$geoNear`
- :pipeline:`$graphLookup` (For usage requirements, see
`csfle-lookup-graphLookup-behavior`)

- :pipeline:`$group` (For usage requirements, see
`csfle-group-behavior`)

- :pipeline:`$indexStats`
- :pipeline:`$limit`
- :pipeline:`$lookup` (For usage requirements, see
`csfle-lookup-graphLookup-behavior`)

- :pipeline:`$match`
- :pipeline:`$project`
- :pipeline:`$redact`
- :pipeline:`$replaceRoot`
- :pipeline:`$sample`
- :pipeline:`$skip`
- :pipeline:`$sort`
- :pipeline:`$sortByCount`
- :pipeline:`$unwind`
Pipelines operating on collections configured for automatic encryption that specify any other stage return an error.

For each supported pipeline stage, MongoDB tracks fields that must be encrypted as they pass through the supported pipelines and marks them for encryption.

Each supported stage must specify only supported `query operators <csfle-supported-query-operators>` and `aggregation expressions <csfle-supported-aggregation-expressions>`.

### `$group` Behavior

:pipeline:`$group` has the following behaviors specific to {+csfle+}:

:pipeline:`$group` supports:

- Grouping on deterministically encrypted fields.
- Using :group:`$addToSet` and :group:`$push` accumulators on
encrypted fields.

$group does not support:

- Matching on the array returned by  :group:`$addToSet` and
:group:`$push` accumulators.

- Arithmetic accumulators on encrypted fields.
### `$lookup` and `$graphLookup` Behavior

Starting in MongoDB 8.1, you can reference multiple encrypted collections in a :pipeline:`$lookup` stage. However, `$lookup` does not support:

- Using an encrypted field as the join field in the `localField` or
`foreignField` unless you are performing a self-join operation.

- Using any field in an encrypted array. An array is considered as encrypted if
it contains any encrypted elements.

- For example, you can't use any field within the resulting
`as <lookup-subquery-as>` array of the `$lookup` operation unless you :pipeline:`$unwind` the `as` field.

Automatic {+csfle+} supports the :pipeline:`$graphLookup` stage only if the `from` collection matches the collection on which the aggregation runs against (specifically, self-lookup operations). :pipeline:`$graphLookup` stages that reference a different `from` collection return an error.

### Supported Aggregation Expressions

Drivers configured for automatic {+csfle+} allow aggregation stages using the following expressions against `deterministically encrypted <csfle-deterministic-encryption>` fields:

- :expression:`$cond`
- :expression:`$eq`
- :expression:`$ifNull`
- :expression:`$in`
- :expression:`$let`
- :expression:`$literal`
- :expression:`$ne`
- :expression:`$switch`
All other aggregation expressions return an error if issued against encrypted fields.

Aggregation stages with the following behavior return an error even if using a supported aggregation expression:

## Unsupported Field Types

Drivers configured for automatic {+csfle+} ({+csfle-abbrev+}) do not support any read or write operation that requires encrypting the following value types:

- :bsontype:`MaxKey`
- :bsontype:`MinKey`
- `null`
- `undefined`
Encryption does not adequately hide the type information for these values.

{+csfle-abbrev+} does not support automatic encryption on fields within an array of documents.

Automatic {+csfle-abbrev+} also does not support read or write operations on a deterministically encrypted field where the operation compares the encrypted field to the following value types:

- `array`
- `bool`
- `decimal128`
- `double`
- `object`
