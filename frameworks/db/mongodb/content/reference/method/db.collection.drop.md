---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.drop.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================================

# db.collection.drop() (mongosh method)

.. include:: /includes/wayfinding/mongosh-method-drop.rst

## Definition

> **Note:** If the specified collection doesn't exist, `db.collection.drop()`
still returns `true`.

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The :method:`~db.collection.drop()` method has the following form:

```javascript
db.collection.drop( { writeConcern: <document> } )
```

The :method:`~db.collection.drop()` method takes an optional document with the following field:

## Behavior

- The :method:`db.collection.drop()` method and :dbcommand:`drop`
command create an `change-event-invalidate` for any `/changeStreams` opened on dropped collection.

- .. include:: /includes/extracts/4.4-changes-drop-in-progress-indexes.rst
- .. include:: /includes/extracts/zoned-sharding-drop-collection-change.rst
- .. include:: /includes/extracts/5.0-changes-drop-sharding.rst
- Starting in MongoDB 6.0, the :method:`db.collection.drop()` method
drops the specified collection and any internal collections related to encrypted fields.

> **Warning:**   The :method:`db.collection.drop()` method's behavior differs from
  the driver's `drop` method's behavior. The driver's connection
  must have automatic encryption enabled in order to drop both the
  specified collection and any internal collections related to
  encrypted fields. `mongosh` always drops the specified
  collection and any internal collections related to encrypted
  fields.

### Reusing Dropped Collection Names on Sharded Clusters

On a sharded cluster, if you create a collection that has the same name as a previously deleted collection prior to MongoDB 5.0, :binary:`~bin.mongos` may forward operations to the wrong shard. To avoid this situation use the version-specific instructions below:

For a sharded cluster running **MongoDB 5.0 or later**, no special action is required. Use the `drop()` method and then create a new collection with the same name.

For a sharded cluster, if you use the `drop()` method and then create a new collection with the same name, you must either:

- Flush the cached routing table on every :binary:`~bin.mongos`
using :dbcommand:`flushRouterConfig`.

- Use :method:`db.collection.remove()` to remove the existing
documents and reuse the collection.

Flushing the cached routing tables is the preferred procedure because it is faster than removing sharded collections with :method:`db.collection.remove()`. Only use the `remove()` approach if you want to avoid flushing the cache.

### Resource Locking

.. include:: /includes/extracts/drop-method-resource-lock.rst

## Example

### Drop a Collection Using Default Write Concern

The following operation drops the `students` collection in the current database.

```javascript
db.students.drop()
```

### Drop a Collection Using `w: 1` Write Concern

:method:`db.collection.drop()` accepts an options document.

The following operation drops the `students` collection in the current database. The operation uses the :writeconcern:`1 <\<number\>>` write concern:

```javascript
db.students.drop( { writeConcern: { w: 1, j: true } } )
```
