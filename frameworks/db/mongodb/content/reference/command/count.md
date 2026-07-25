---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/count.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

========================

# count (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-limited-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

> **Note:** .. include:: /includes/extracts/4.2-changes-count-syntax-validation.rst

```javascript
db.runCommand(
   {
     count: <collection or view>,
     query: <document>,
     limit: <integer>,
     skip: <integer>,
     hint: <hint>,
     readConcern: <document>,
     maxTimeMS: <integer>,
     collation: <document>,
     comment: <any>
   }
)
```

### Command Fields

:dbcommand:`count` has the following fields:

## Stable API Support

Starting in MongoDB 6.0, the `count` command is included in `Stable API <stable-api>` V1. To use the `count` command in the Stable API, you must connect your driver to a deployment running MongoDB 6.0 or later.

## Behavior

### Inaccurate Counts Without Query Predicate

When you call :dbcommand:`count` without a query predicate, you may receive inaccurate document counts. Without a query predicate, :dbcommand:`count` commands return results based on the collection's metadata, which may result in an approximate count. In particular,

- On a sharded cluster, the resulting count does not correctly
filter out `orphaned documents <orphaned document>`.

- After an unclean shutdown or :ref:`file copy based initial sync
<replica-set-initial-sync-file-copy-based>`, the count may be incorrect.

For counts based on collection metadata, see also `collStats pipeline stage with the count <collstat-count>` option.

### Count and Transactions

.. include:: /includes/fact-uncommitted-transactions.rst

For details, see `Transactions and Count Operations <transactions-ops-count>`.

### Accuracy and Sharded Clusters

.. include:: /includes/extracts/fact-count-on-sharded-clusters-cmd-count.rst

### Accuracy after Unexpected Shutdown

.. include:: /includes/fact-unexpected-shutdown-accuracy.rst

> **Note:** This loss of accuracy only applies to :dbcommand:`count`
operations that do not include a query document.

### Client Disconnection

.. include:: /includes/extracts/4.2-changes-disconnect.rst

## Examples

### Count All Documents

The following operation counts all documents in the `orders` collection:

```javascript
db.runCommand( { count: 'orders' } )
```

The operation returns the following document:

```javascript
{ "n" : 26, "ok" : 1 }
```

### Count Documents That Match a Query

The following operation counts documents in the `orders` collection where the `ord_dt` field is greater than `Date('01/01/2012')`:

```javascript
db.runCommand( { count:'orders',
                 query: { ord_dt: { $gt: new Date('01/01/2012') } }
               } )
```

The operation returns the following document:

```javascript
{ "n" : 13, "ok" : 1 }
```

### Skip Documents in Count

The following operation counts documents in the `orders` collection where the `ord_dt` field is greater than `Date('01/01/2012')`, skipping the first `10` matches:

```javascript
db.runCommand( { count:'orders',
                 query: { ord_dt: { $gt: new Date('01/01/2012') } },
                 skip: 10 }  )
```

The operation returns the following document:

```javascript
{ "n" : 3, "ok" : 1 }
```

### Specify the Index to Use

The following operation uses the index `{ status: 1 }` to count documents in the `orders` collection where the `ord_dt` field is greater than `Date('01/01/2012')` and the `status` field equals `"D"`:

```javascript
db.runCommand(
   {
     count:'orders',
     query: {
              ord_dt: { $gt: new Date('01/01/2012') },
              status: "D"
            },
     hint: { status: 1 }
   }
)
```

The operation returns the following document:

```javascript
{ "n" : 1, "ok" : 1 }
```

### Override Default Read Concern

To override the default read concern level of :readconcern:`"local"`, use the `readConcern` option.

The following operation on a replica set specifies a `/reference/read-concern` of :readconcern:`"majority"` to read the most recent copy of the data confirmed as having been written to a majority of the nodes.

> **Important:** - To use the `readConcern` level of `"majority"`, you must specify
  a nonempty `query` condition.
- .. include:: /includes/fact-readConcern-most-recent-data-in-node.rst

```javascript
db.runCommand(
   {
     count: "restaurants",
     query: { rating: { $gte: 4 } },
     readConcern: { level: "majority" }
   }
)
```

.. include:: /includes/usage-read-concern-majority.rst
