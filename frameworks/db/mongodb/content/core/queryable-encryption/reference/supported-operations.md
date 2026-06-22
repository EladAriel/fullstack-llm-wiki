---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/queryable-encryption/reference/supported-operations.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================================

# Supported Operations for {+qe+}

This page documents the specific data types, commands, query operators, update operators, aggregation stages, and aggregation expressions supported for {+qe+} compatible drivers. It outlines the behavior for operations using automatic encryption, and operations using {+manual-enc+}.

> **Note:** Automatic encryption is available in MongoDB Enterprise and MongoDB Atlas

## Operations Using `BinData`

MongoDB stores {+qe+} encrypted fields as a :bsontype:`BinData <data_binary>` blob. Read and write operations issued against the encrypted `BinData` value may have unexpected or incorrect behavior as compared to issuing that same operation against the decrypted value. Certain operations have strict BSON type support where issuing them against a `BinData` value returns an error.

Official drivers compatible with {+qe+} parse read and write operations for operators or expressions that don't support `BinData` values.

## Supported and Unsupported BSON Types

{+qe+} supports `configuring <qe-create-encryption-schema>` the equality query type `queryType: "equality"` for all `BSON types <bson-types>` **except** the following:

- `array`
- `decimal`: Decimal (IEEE 754 Decimal128)
- `double`: Double (IEEE 754 Binary64)
- `object`
{+qe+} supports `configuring <qe-create-encryption-schema>` the range query type `queryType: "range"` for the following `BSON types <bson-types>`:

- `date`: UTC DateTime (Int64)
- `decimal`: Decimal (IEEE 754 Decimal128)
- `double`: Double (IEEE 754 Binary64)
- `int`: 32-bit integer
- `long`: 64-bit integer
> **Note:** The query type is the :ref:`configuration
<qe-create-encryption-schema>` of the encrypted index, not the set
of query operators by itself. In particular, `decimal` and
`double` support the range query type `queryType: "range"`, and
MongoDB evaluates equality queries on these fields using the range
index.

## CRUD

- {+qe+} doesn't support multi-document update or delete operations.
:method:`db.collection.updateMany()` and :method:`db.collection.bulkWrite()` with more than one update or delete operation aren't supported.

- {+qe+} limits :method:`db.collection.findAndModify()` arguments.
- `fields` is not allowed
- `new` must be false
- When performing an upsert operation, any encrypted fields in the
filter are excluded from the insert.

## Supported Read and Write Commands

{+qe+} compatible drivers support automatic encryption with the following commands:

- :dbcommand:`aggregate`
- :dbcommand:`count`
- :dbcommand:`delete`
- :dbcommand:`explain`
- :dbcommand:`find`
- :dbcommand:`findAndModify`
- :dbcommand:`insert`
- :dbcommand:`update`
For any supported command, the drivers return an error if the command uses an unsupported operator, aggregation stage, or aggregation expression. For a complete list of the supported operators, stages, and expressions, see the following sections:

- `Supported Query Operators <qe-supported-query-operators>`
- `Supported Update Operators <qe-supported-update-operators>`
- `Supported Aggregation Stages <qe-supported-aggregation-stages>`
- `Supported Aggregation Expressions <qe-supported-aggregation-expressions>`
The following commands do not require automatic encryption. Official drivers configured for automatic encryption pass these commands directly to the :binary:`~bin.mongod`:

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
Issuing any other command through a compatible driver configured for automatic encryption returns an error.

While automatic encryption does not encrypt the getMore command, the response to the command may contain encrypted field values.

- Applications configured with the correct {+qe+} options automatically decrypt
those values.

- Applications without the correct encryption options see the encrypted values.
## Supported Query Types & Operators

Drivers configured for automatic encryption support a limited set of query operators when issued against an encrypted queryable field.

Querying non-encrypted fields or encrypted fields with a supported query type returns encrypted data that is then decrypted at the client.

{+qe+} currently supports the following query types:

- `none`
- `equality`
- `range`
- `prefix`
- `suffix`
- `substring`
If the query type is unspecified, it defaults to `none`. If the query type is `none`, MongoDB encrypts the field, and clients can't query it.

> **Important:** Comparison of an encrypted field to a plaintext value is supported.
.. code-block:: json
   {$expr: {$eq: ["$encrypted1", "plaintext_value"]}}
Comparison of one encrypted field to another encrypted field will fail.
.. code-block:: json
   {$expr: {$eq: ["$encrypted1", "$encrypted2"]}}

Fields configured for `queryType: "equality"` support the following expressions:

- :query:`$eq`
- :query:`$ne`
- :query:`$in`
- :query:`$nin`
- :query:`$and`
- :query:`$or`
- :query:`$not`
- :query:`$nor`
- :query:`$expr`
- :query:`$exists`
Range queries implicitly convert equality queries to :query:`$lte` and :query:`$gte`. Thus, fields configured for `queryType: "range"` support all expressions above, as well as the following expressions:

- :query:`$lt`
- :query:`$lte`
- :query:`$gt`
- :query:`$gte`
Queries specifying any other query operator against an encrypted field return an error.

### Unsupported Queries

Queries that compare an encrypted field to `null` or a regular expression always throw an error, even if using a supported query operator.

When using a MongoClient configured for {+qe+}, the following query operators throw an error, even if issued against an unencrypted field:

- :query:`$text`
- :query:`$where`
- :query:`$jsonSchema`
## Supported Update Operators

Drivers configured for automatic encryption support the following update operators when issued against encrypted fields:

- :update:`$set`
- :update:`$unset`
Updates specifying any other update operator against an encrypted field return an error.

Update operations with the following behavior throw an error, even if using a supported operator:

- The update operation produces an array inside of an encrypted path.
- The update operation uses aggregation expression syntax.
For update operations specifying a `query filter <update-command-q>` on encrypted fields, the query filter must use only `supported operators <csfle-supported-query-operators>` on those fields.

## Replacement-style Updates

Replacement-style updates are supported, however, if the replacement document contains a `Timestamp(0,0)` inside a top-level encrypted field, {+qe+} will error. The `(0,0)` value indicates that the :binary:`~bin.mongod` should generate the Timestamp.  :binary:`~bin.mongod` cannot generate encrypted fields.

## Unsupported Insert Operations

Compatible drivers configured for automatic encryption do not support insert commands with the following behavior:

- Inserting a document with `Timestamp(0,0)` associated to an encrypted field.
The `(0,0)` value indicates that the :binary:`~bin.mongod` should generate the Timestamp. Since the :binary:`~bin.mongod` cannot generate encrypted fields, the resulting timestamp would be unencrypted.

## Unsupported Aggregation Stages

Automatic encryption will not support aggregation stages that read from or write to additional collections. These stages are:

- :pipeline:`$out`
- :pipeline:`$merge`
## Supported Aggregation Stages

Compatible drivers configured for automatic encryption support the following aggregation pipeline stages:

- :pipeline:`$addFields`
- :pipeline:`$bucket`
- :pipeline:`$bucketAuto`
- :pipeline:`$collStats`
- :pipeline:`$count`
- :pipeline:`$geoNear`
- :pipeline:`$graphLookup` (For usage requirements, see
`qe-lookup-graphLookup-behavior`)

- :pipeline:`$group` on unencrypted fields
- :pipeline:`$indexStats`
- :pipeline:`$limit`
- :pipeline:`$lookup` (For usage requirements, see
`qe-lookup-graphLookup-behavior`)

- :pipeline:`$match`
- :pipeline:`$project`
- :pipeline:`$redact`
- :pipeline:`$replaceRoot`
- :pipeline:`$sample`
- :pipeline:`$skip`
- :pipeline:`$sort`
- :pipeline:`$sortByCount`
- :pipeline:`$unwind`
Aggregation pipelines operating on collections configured for automatic encryption that specify any other stage return an error.

For each supported pipeline stage, MongoDB tracks fields that must be encrypted as they pass through the supported pipelines and marks them for encryption.

Each supported stage must specify only supported `query operators <qe-supported-query-operators>` and `aggregation expressions <qe-supported-aggregation-expressions>`.

### `$lookup` and `$graphLookup` Behavior

Starting in MongoDB 8.1, you can reference multiple encrypted collections in a :pipeline:`$lookup` stage. However, `$lookup` does not support:

- Using an encrypted field as the join field in the `localField` or
`foreignField`.

- Using any field in an encrypted array. An array is considered as encrypted if
it contains any encrypted elements.

- For example, you can't use any field within the resulting
`as <lookup-subquery-as>` array of the `$lookup` operation.

Automatic encryption supports :pipeline:`$graphLookup` only if the `from` collection matches the collection the aggregation runs against. `$graphLookup` stages that reference a different `from` collection return an error.

Automatic encryption does not support "connectionless" aggregation metadata sources, which read metadata that doesn't pertain to a particular collection, such as:

- :pipeline:`$currentOp`
- `changeStreams` for watching a database or the whole cluster
- :pipeline:`$listSessions`
- :pipeline:`$listLocalSessions`
Automatic encryption does not support the :pipeline:`$planCacheStats` stage as the result may contain sensitive information.

## Supported Aggregation Expressions

Compatible drivers configured for automatic encryption support the following expressions against encrypted fields configured for equality queries:

- :expression:`$cond`
- :expression:`$eq`
- :expression:`$ifNull`
- :expression:`$in`
- :expression:`$let`
- :expression:`$literal`
- :expression:`$ne`
- :expression:`$switch`
Compatible drivers configured for automatic encryption support the following expressions against encrypted fields configured for `prefix`, `suffix`, or `substring` queries:

- :expression:`$encStrStartsWith`
- :expression:`$encStrEndsWith`
- :expression:`$encStrContains`
- :expression:`$encStrNormalizedEq`
All other aggregation expressions return an error if issued against encrypted fields.

Aggregation stages with the following behavior return an error, even if using a supported aggregation expression:

## Unsupported Field Types

Drivers configured for automatic encryption do not support any read or write operation that requires encrypting the following value types:

- :bsontype:`MaxKey`
- :bsontype:`MinKey`
- `null`
- `undefined`
{+qe+} does not adequately hide the type information for these values.

{+qe+} does not support automatic encryption on fields within an array of documents.

{+qe+} does not support read or write operations on an encrypted field where the operation compares the encrypted field to the following value types:

- `array`
- `object`
