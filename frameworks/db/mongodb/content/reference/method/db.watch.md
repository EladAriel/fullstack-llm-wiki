---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.watch.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================

# db.watch() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Availability

### Deployment

:method:`db.watch()` is available for replica sets and sharded clusters:

- For a replica set, you can issue :method:`db.watch()` on any
data-bearing member.

- For a sharded cluster, you must issue :method:`db.watch()` on a
:binary:`~bin.mongos` instance.

### Storage Engine

You can only use :method:`db.watch()` with the `Wired Tiger storage engine <storage-wiredtiger>`.

### Read Concern `majority` Support

.. include:: /includes/extracts/changestream-rc-majority-4.2.rst

## Behavior

- You cannot run :method:`db.watch()` on the `admin`, `local`, or
`config` database.

- :method:`db.watch()` only notifies on data changes that have
persisted to a majority of data-bearing members.

- .. include:: /includes/extracts/changestream-cursor-open.rst
- You can run :method:`db.watch()` for a database that does not exist.
However, once the database is created and you drop the database, the change stream cursor closes.

### Resumability

.. include:: /includes/extracts/changestream-resume.rst

.. include:: /includes/change-stream/resume-after

### Full Document Lookup of Update Operations

.. include:: /includes/extracts/changestream-full-document-lookup.rst

## Access Control

When running with access control, the user must have the :authaction:`find` and :authaction:`changeStream` privilege actions on the `database resource <resource-document>`. That is, a user must have a `role <roles>` that grants the following `privilege <privileges>`:

```javascript
{ resource: { db: <dbname>, collection: "" }, actions: [ "find", "changeStream"] }
```

The built-in :authrole:`read` role provides the appropriate privileges.

## Cursor Iteration

.. include:: /includes/fact-multiple-cursor-monitors.rst

## Example

The following operation in :binary:`~bin.mongosh` opens a change stream cursor on the `hr` database. The returned cursor reports on data changes to all the non-`system` collections in that database.

```javascript
watchCursor = db.getSiblingDB("hr").watch()
```

Iterate the cursor to check for new events. Use the :method:`cursor.isClosed()` method with the :method:`cursor.tryNext()` method to ensure the loop only exits if the change stream cursor is closed and there are no objects remaining in the latest batch:

```javascript
while (!watchCursor.isClosed()) {
  let next = watchCursor.tryNext()
  while (next !== null) {
    printjson(next);
    next = watchCursor.tryNext()
  }
}
```

For complete documentation on change stream output, see `change-stream-output`.

.. include:: /includes/isExhausted-no-change-streams.rst
