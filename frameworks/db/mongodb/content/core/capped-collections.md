---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/capped-collections.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================

# Capped Collections

Capped collections are fixed-size collections that insert and retrieve documents based on insertion order. Capped collections work similarly to circular buffers: once a collection fills its allocated space, it makes room for new documents by overwriting the oldest documents in the collection.

## Restrictions

- Capped collections cannot be sharded.
- Capped collections are not supported in `Stable API <stable-api>`
V1.

- You cannot write to capped collections in :ref:`transactions
<transactions>`.

- The :pipeline:`$out` aggregation pipeline stage cannot write results
to a capped collection.

## Command Syntax

The following example creates a capped collection called `log` with a maximum size of 100,000 bytes.

```javascript
db.createCollection( "log", { capped: true, size: 100000 } )
```

For more information on creating capped collections, see :method:`~db.createCollection()` or :dbcommand:`create`.

## Use Cases

.. include:: /includes/capped-collections/use-ttl-index.rst

The most common use case for a capped collection is to store log information. When the capped collection reaches its maximum size, old log entries are automatically overwritten with new entries.

## Get Started

To create and query capped collections, see these pages:

- `capped-collections-create`
- `capped-collections-query`
- `capped-collections-check`
- `capped-collections-convert`
- `capped-collections-change-size`
- `capped-collections-change-max-docs`
## Behavior

### Oplog Collection

The `oplog.rs <oplog>` collection that stores a log of the operations in a `replica set` uses a capped collection.

Unlike other capped collections, the oplog can grow past its configured size limit to avoid deleting the `majority commit point <replSetGetStatus.optimes.lastCommittedOpTime>`.

> **Note:** MongoDB rounds the capped size of the oplog up to the nearest
integer multiple of 256, in bytes.

### _id Index

Capped collections have an `_id field and an index on the id` field by default.

### Updates

Avoid updating data in a capped collection. Updates can expand your data beyond the collection's allocated space and cause unexpected behavior.

### Query Efficiency

.. include:: /includes/capped-collections/query-natural-order.rst

### Tailable Cursor

You can use a `tailable cursor` with capped collections. Similar to the Unix `tail -f` command, a tailable cursor continuously retrieves new documents from the end of a capped collection as they are inserted.

For information on creating a tailable cursor, see `tailable-cursors-landing-page`.

### Multiple Concurrent Writes

.. include:: /includes/capped-collections/concurrent-writes.rst

### Read Concern Snapshot

.. include:: /includes/snapshot-capped-collections.rst

## Learn More

- `index-feature-ttl`
- `index-properties`
- `indexing-strategies`
## Contents

- Create </core/capped-collections/create-capped-collection>
- Query </core/capped-collections/query-capped-collection>
- Verify </core/capped-collections/check-if-collection-is-capped>
- Convert </core/capped-collections/convert-collection-to-capped>
- Change Size </core/capped-collections/change-size-capped-collection>
- Change Limits </core/capped-collections/change-max-docs-capped-collection>
