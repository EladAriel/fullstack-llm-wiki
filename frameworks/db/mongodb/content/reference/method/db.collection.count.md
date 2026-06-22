---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.count.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# db.collection.count() (mongosh method)

.. include:: /includes/fact-mongosh-shell-method-alt

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The `db.collection.count()` method has the following form:

```javascript
db.collection.count(query, options)
```

### Parameters

This method takes the following parameters:

## Fields

The `options` document contains the following fields:

`count()` is equivalent to the `db.collection.find(query).count()` construct.

> **Seealso:** - :method:`cursor.count()`
- :method:`db.collection.estimatedDocumentCount()`
- :method:`db.collection.countDocuments()`

## Behavior

### Inaccurate Counts Without Query Predicate

Without a query predicate, `count()` returns results based on the collection's metadata, which may result in an incorrect count. In particular,

- On a sharded cluster, the resulting count will not correctly
filter out `orphaned documents <orphaned document>`.

- After an unclean shutdown or :ref:`file copy based initial sync
<replica-set-initial-sync-file-copy-based>`, the count may be incorrect.

For counts based on collection metadata, see also `collStats pipeline stage with the count <collstat-count>` option.

### Count and Transactions

You cannot use :dbcommand:`count` and shell helpers :method:`cursor.count()` and `count()` in `transactions <transactions-ops-count>`.

For details, see `Transactions and Count Operations <transactions-ops-count>`.

### Sharded Clusters

.. include:: /includes/extracts/fact-count-on-sharded-clusters-method-db.collection.count.rst

### Index Use

.. include:: /includes/fact-count-index-use.rst

### Accuracy after Unexpected Shutdown

.. include:: /includes/fact-unexpected-shutdown-accuracy.rst

> **Note:** This loss of accuracy only applies to `count()`
operations that do not include a query predicate.

### Client Disconnection

.. include:: /includes/extracts/4.2-changes-disconnect.rst

## Examples

### Count all Documents in a Collection

To count all documents in the `orders` collection:

```javascript
db.orders.count()
```

The equivalent operation is:

```javascript
db.orders.find().count()
```

### Count all Documents that Match a Query

Count documents in the `orders` collection where `ord_dt` is greater than `new Date('01/01/2012')`:

```javascript
db.orders.count( { ord_dt: { $gt: new Date('01/01/2012') } } )
```

The equivalent operation is:

```javascript
db.orders.find( { ord_dt: { $gt: new Date('01/01/2012') } } ).count()
```
