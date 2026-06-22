---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.countDocuments.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================================

# db.collection.countDocuments() (mongosh method)

.. include:: /includes/wayfinding/mongosh-method-countDocuments.rst

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The `countDocuments()` method has the following form:

```javascript
db.collection.countDocuments( <query>, <options> )
```

### Parameters

The `countDocuments()` method takes the following parameters:

The `options` document can contain the following:

## Behavior

### Mechanics

Unlike :method:`db.collection.count()`, `countDocuments()` does not use the metadata to return the count. Instead, it performs an aggregation of the document to return an accurate count, even after an unclean shutdown or in the presence of `orphaned documents <orphaned document>` in a sharded cluster.

`countDocuments()` wraps the following aggregation operation and returns just the value of `n`:

```javascript
db.collection.aggregate([
   { $match: <query> },
   { $group: { _id: null, n: { $sum: 1 } } }
])
```

### Empty or Non-Existing Collections and Views

`countDocuments()` returns `0` on an empty or non-existing collection or view.

### Query Restrictions

You cannot use the following query operators as part of the query expression for `countDocuments()`:

### Transactions

.. include:: /includes/extracts/transactions-supported-operation.rst

.. include:: /includes/fact-uncommitted-transactions.rst

.. include:: /includes/extracts/transactions-usage.rst

### Client Disconnection

.. include:: /includes/extracts/4.2-changes-disconnect.rst

## Examples

.. include:: /includes/sample-data-usage.rst

### Count all Documents in a Collection

To count the number of documents in the `movies` collection, use the following operation:

> **Note:** If you use `db.collection.countDocuments()` with an empty query
filter, MongoDB performs a full collection scan which can be
inefficient. To improve performance, this example specifies a
:method:`~cursor.hint() to use the automatically generated id`
index. Alternatively, you can use a query filter that finds all
documents such as `{ "_id": { $gte: MinKey } }` to count all
documents using an index.

### Count all Documents that Match a Query

This example counts the number of documents in the `movies` collection where the `directors` field contains `"David Lynch"`:

## Learn More

- :method:`db.collection.estimatedDocumentCount()`
- :pipeline:`$group` and :group:`$sum`
- :dbcommand:`count`
- `collStats pipeline stage with the count option <collstat-count>`
