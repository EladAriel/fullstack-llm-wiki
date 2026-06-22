---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/queryStats.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# $queryStats (aggregation stage)

## Definition

.. include:: /includes/aggregation/queryStats/unsupported-warning.rst

.. include:: /includes/aggregation/queryStats/description.rst

`$queryStats` collects and reports metrics for :method:`~db.collection.aggregate()`, :method:`~db.collection.find()`, and :method:`~db.collection.distinct()` queries. `$queryStats` does not collect information for queries that use `{+qe+} <qe-manual-feature-qe>`.

## Requirements

The `$queryStats` stage is enabled on deployments hosted on :atlas:`MongoDB Atlas </>` with a cluster tier of at least M10.

To run the `$queryStats` stage, your pipeline must meet the following requirements:

- The pipeline must be run on the `admin` database.
- `$queryStats` must be the first stage in the pipeline.
## Syntax

```javascript
db.adminCommand( {
   aggregate: 1,
   pipeline: [
      {
         $queryStats: {
            transformIdentifiers: {
               algorithm: <string>,
               hmacKey: <binData> /* subtype 8 - used for sensitive data */
            }
         }
      }
   ],
   cursor: { }
 } )
```

> **Important:** You cannot run `$queryStats` on a specific collection. For complete
examples, see `queryStats-examples`.

### Command Fields

`$queryStats` takes the following fields:

## Access Control

If your deployment enforces access control, the user running `$queryStats` must have the following permissions:

- To run `$queryStats` without the `transformIdentifiers` option,
the user must have the :authaction:`queryStatsRead` privilege action.

- To run `$queryStats` with the `transformIdentifiers` option, the
user must have the both the :authaction:`queryStatsRead` and :authaction:`queryStatsReadTransformed` privilege actions.

The built-in :authrole:`clusterMonitor` role provides the `queryStatsRead` and `queryStatsReadTransformed` privileges. The following example grants the `clusterMonitor` role on the `admin` database:

```javascript
db.grantRolesToUser(
   "<user>",
   [ { role: "clusterMonitor", db: "admin" } ]
)
```

## Behavior

The following sections describe behavioral details of the `$queryStats` stage.

### How $queryStats Tracks Query Statistics

Statistics for the `$queryStats` stage are tracked in a virtual collection that is stored in-memory. The memory limit for the virtual collection is 1% of the system's total memory.

### How $queryStats Groups Returned Documents

`$queryStats` groups queries with common properties into the same output document. The resulting document is called a **query stats entry**.

`$queryStats` groups similar queries together by normalizing user-provided field values to their data types. For example, a filter specified as `{ item: 'card' }` is normalized to `{ item : '?string'}`. `$queryStats` also normalizes the values of some query options like `hint` and `comment`.

`$queryStats` preserves literal values for options like `readConcern` and `readPreference`.

For the complete list of options included in a query stats entry, see `queryStats-find-query-shape`.

### How $queryStats Transforms Data Using transformIdentifiers

When an HMAC key is specified to the `transformIdentifiers` option, `$queryStats` uses the HMAC key to apply an HMAC-SHA-256 hash function on the following data:

- Document field names
- Collection names
- Database names
`$queryStats` **does not** apply the HMAC transformation to the following data:

- MQL keywords such as operator names (for example, `$gte`).
- Parameter names such as the `partitionBy` parameter in
:pipeline:`$setWindowFields`.

- Field values. `$queryStats` normalizes field values in a query to
their data types (such as number or string) when the query is recorded. `$queryStats` never stores field values that contain user data.

For an example of transformed output, see `queryStats-example-transformed`.

### $queryStats Log Entries

.. include:: /includes/aggregation/queryStats/logging-intro.rst

To learn how to control `$queryStats` logging behavior, see `queryStats-toggle-logging`.

### Change Streams

Query stats for `change streams <changeStreams>` are updated when one of these events occur:

- A cursor is created
- A :dbcommand:`getMore` operation completes
- A cursor closes
Query stats reported for change streams have these behaviors:

- Execution metrics such as `totalExecMicros` contain information for
the most recent operation (cursor creation, `getMore`, or cursor close).

- Internal `getMore` operations increment the `execCount` metric.
- `firstResponseExecMicros` and `totalExecMicros` are always the
same because stats are collected and updated for each `getMore` operation.

- When the cursor closes, `lastExecutionMicros` is 0.
### Sharded Cluster Behavior

.. versionadded:: 8.3

In sharded clusters, MongoDB records query statistics separately on each `mongod` and `mongos` when `$queryStats` is enabled. Shard servers also record statistics for queries that originate from `mongos`. These provide more complete shard-level metrics for queries that users route through `mongos`.

## Output

`$queryStats` returns an array of query stats entries. Some query stats entry properties contain literal values, and some properties are normalized to group common queries.

Query stats entries contain the following top-level documents:

Each document in the output array contains the following fields:

### Collection Type

The `key.collectionType` field indicates the type of collection that the recorded query was issued on. The `collectionType` can be one of the following values:

### Query Shape

The `key.queryShape` document contains query shape fields. To learn about query shapes, see `query-shapes`.

The fields in `key.queryShape` vary based on the command that resulted in the query stats entry. `$queryStats` creates query stats entries for :dbcommand:`aggregate`, :dbcommand:`find`, :dbcommand:`distinct`, and :dbcommand:`count` commands.

Each query shape property corresponds to a query option. For example, `key.queryShape.sort` corresponds to the :method:`~cursor.sort()` specification for the query shape.

find Command Query Shape ````````````````````````

The following table describes the query shape properties for `find` commands.

aggregate Command Query Shape `````````````````````````````

The following table describes the query shape properties for `aggregate` commands.

distinct Command Query Shape ````````````````````````````

The following table describes the query shape properties for `distinct` commands.

count Command Query Shape `````````````````````````

The following table describes the query shape properties for `count` commands.

### Supplemental Metrics

Query stats entries may contain a `metrics.supplementalMetrics` document that provides additional information about your queries.

$vectorSearch Metrics `````````````````````

If your query shape contains :pipeline:`$vectorSearch`, `$queryStats` outputs the following supplemental metrics:

## Examples

## MongoDB Atlas Data Collection

MongoDB Atlas periodically uses `$queryStats` to collect anonymized data about your queries, which helps improve MongoDB products. Your data may also be used to make feature suggestions based on usage. MongoDB retains the data it collects with `$queryStats` for four years.

When Atlas runs `$queryStats` on your deployment, it uses a unique HMAC key per Atlas organization to transform your data and avoid collecting sensitive information.

## Contents

- Toggle Log Output </reference/operator/aggregation/queryStats/toggle-logging>
