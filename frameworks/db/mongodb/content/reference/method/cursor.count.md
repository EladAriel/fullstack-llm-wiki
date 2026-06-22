---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.count.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# cursor.count() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

### Inaccurate Counts Without Query Predicate

When you call :method:`~cursor.count()` on a :method:`~db.collection.find()` operation which does not specify a query predicate, the :method:`~cursor.count()` method can return inaccurate document counts. These :method:`~cursor.count()` methods return results based on the collection's metadata, which may result in an approximate count. In particular,

- On a sharded cluster, the resulting count will not correctly
filter out `orphaned documents <orphaned document>`.

- After an unclean shutdown or :ref:`file copy based initial sync
<replica-set-initial-sync-file-copy-based>`, the count may be incorrect.

For counts based on collection metadata, see also `collStats pipeline stage with the count <collstat-count>` option.

### Count and Transactions

You cannot use :dbcommand:`count` and shell helpers :method:`~cursor.count()` and :method:`db.collection.count()` in `transactions <transactions-ops-count>`.

For details, see `Transactions and Count Operations <transactions-ops-count>`.

### Sharded Clusters

.. include:: /includes/extracts/fact-count-on-sharded-clusters-method-cursor.count.rst

### Index Use

.. include:: /includes/fact-count-index-use.rst

## Examples

The following are examples of the :method:`~cursor.count()` method.

### Count All Documents

The following operation counts the number of all documents in the `orders` collection:

```javascript
db.orders.find().count()
```

### Count Documents That Match a Query

The following operation counts the number of the documents in the `orders` collection with the field `ord_dt` greater than `new Date('01/01/2012')`:

```javascript
db.orders.find( { ord_dt: { $gt: new Date('01/01/2012') } } ).count()
```

### Limit Documents in Count

The following operation counts the number of the documents in the `orders` collection with the field `ord_dt` greater than `new Date('01/01/2012')` taking into account the effect of the `limit(5)`:

```javascript
db.orders.find( { ord_dt: { $gt: new Date('01/01/2012') } } ).limit(5).count(true)
```

### Specify the Index to Use

The following operation uses the index named `"status_1"`, which has the index key specification of `{ status: 1 }`, to return a count of the documents in the `orders` collection with the field `ord_dt` greater than `new Date('01/01/2012')` and the `status` field is equal to `"D"`:

```javascript
db.orders.find(
   { ord_dt: { $gt: new Date('01/01/2012') }, status: "D" }
).hint( "status_1" ).count()
```
