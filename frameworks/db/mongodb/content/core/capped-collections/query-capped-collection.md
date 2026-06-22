---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/capped-collections/query-capped-collection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================

# Query a Capped Collection

When you query a capped collection without specifying a sort order, MongoDB returns results in the same order that they were inserted, meaning the oldest documents are returned first.

.. include:: /includes/capped-collections/query-natural-order.rst

## About this Task

.. include:: /includes/capped-collections/use-ttl-index.rst

### Multiple Concurrent Writes

.. include:: /includes/capped-collections/concurrent-writes.rst

## Before you Begin

## Steps

The following examples show you how to:

- `query-capped-collection-insertion-order`
- `query-capped-collection-recent`
### Return Documents in Insertion Order

Query the `log` collection for documents where `type` is `info`, and use the default sort order:

Documents are returned in the order that they were inserted.

### Return Most Recent Documents

To return documents in reverse insertion order (meaning the most recent documents are first), specify the :method:`~cursor.sort()` method with the :operator:`$natural` parameter set to `-1`.

The following query returns the three most recent documents from the `log` collection, starting with the most recent document:

## Learn More

- `index-feature-ttl`
- `read-operations-indexing`
- `create-indexes-to-support-queries`
