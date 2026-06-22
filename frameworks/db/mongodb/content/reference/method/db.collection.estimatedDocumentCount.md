---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.estimatedDocumentCount.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================================================

# db.collection.estimatedDocumentCount() (mongosh method)

.. include:: /includes/wayfinding/mongosh-method-estimatedDocumentCount.rst

## Definition

### Parameters

## Fields

The `options` document can contain the following:

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

### Mechanics

:method:`db.collection.estimatedDocumentCount()` does not take a query filter and instead uses metadata to return the count for a collection.

For a `view <views-landing-page>`:

- There is no metadata.
- The document count is calculated by executing the :ref:`aggregation
pipeline <aggregation-pipeline>` in the view definition.

- There is no fast estimated document count.
### Sharded Clusters

On a sharded cluster, the resulting count will not correctly filter out `orphaned documents <orphaned document>`.

### Unclean Shutdown

This section only applies to collections.

After an unclean shutdown, the count may be incorrect.

.. include:: /includes/fact-unexpected-shutdown-accuracy.rst

### Client Disconnection

.. include:: /includes/extracts/4.2-changes-disconnect.rst

### Count and Transactions

.. include:: /includes/fact-uncommitted-transactions.rst

## Example

The following example uses :method:`db.collection.estimatedDocumentCount` to retrieve the count of all documents in the `orders` collection:

```javascript
db.orders.estimatedDocumentCount({})
```

> **Seealso:** - :method:`db.collection.countDocuments()`
- :dbcommand:`count`
- `collStats pipeline stage with the count <collstat-count>`
  option
