---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.drop.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=====================================

# db.collection.drop() (mongosh method)

.. include:: /includes/wayfinding/mongosh-method-drop.rst

## Definition

> **Note:** If the specified collection does not exist, `db.collection.drop()`
still returns `true`.

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The `drop()` method has the following form:

```javascript
db.collection.drop( { writeConcern: <document> } )
```

The `drop()` method takes an optional document with the following field:

## Behavior

- The `drop()` method and :dbcommand:`drop` command create an
`invalidate event <change-event-invalidate>` for any `change streams <changeStreams>` opened on the dropped collection.

- .. include:: /includes/extracts/4.4-changes-drop-in-progress-indexes.rst
- .. include:: /includes/extracts/zoned-sharding-drop-collection-change.rst
- .. include:: /includes/extracts/5.0-changes-drop-sharding.rst
- Starting in MongoDB 6.0, `drop()` drops the specified collection
and any internal collections related to encrypted fields.

> **Important:**   The `mongosh` `drop()` method's behavior differs from the
  driver's `drop` method's behavior. The driver's connection
  must have automatic encryption enabled to drop both the specified
  collection and any internal collections related to encrypted
  fields. `mongosh` always drops the specified collection and
  any internal collections related to encrypted fields.

### Reusing Dropped Collection Names on Sharded Clusters

For a sharded cluster running **MongoDB 5.0 or later**, no special action is required. Use the `drop()` method and then create a new collection with the same name.

### Resource Locking

.. include:: /includes/extracts/drop-method-resource-lock.rst

## Example

### Drop a Collection Using Default Write Concern

The following operation drops the `students` collection in the current database.

```javascript
db.students.drop()
```

### Drop a Collection Using `w: 1` Write Concern

The following operation drops the `students` collection in the current database. The operation uses the :writeconcern:`1 <\<number\>>` write concern:

```javascript
db.students.drop( { writeConcern: { w: 1, j: true } } )
```
