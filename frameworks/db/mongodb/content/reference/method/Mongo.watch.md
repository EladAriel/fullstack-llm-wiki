---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Mongo.watch.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# Mongo.watch() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Availability

### Deployment

:method:`Mongo.watch()` is available for replica sets and sharded clusters:

- For a replica set, you can issue :method:`Mongo.watch()` on any
data-bearing member.

- For a sharded cluster, you must issue :method:`Mongo.watch()` on a
:binary:`~bin.mongos` instance.

### Storage Engine

You can only use :method:`Mongo.watch()` with the `Wired Tiger storage engine <storage-wiredtiger>`.

### Read Concern `majority` Support

.. include:: /includes/extracts/changestream-rc-majority-4.2.rst

## Behavior

- :method:`Mongo.watch()` only notifies on data changes that have
persisted to a majority of data-bearing members.

- .. include:: /includes/extracts/changestream-cursor-open.rst
### Resumability

.. include:: /includes/extracts/changestream-resume.rst

> **Note:** Hex Encoded Tokens
``````````````````
.. include:: /includes/extracts/changestream-resume-token-hex-change.rst
Decode Resume Tokens
````````````````````
.. include:: /includes/note-decode-resume-tokens.rst

### Full Document Lookup of Update Operations

.. include:: /includes/extracts/changestream-full-document-lookup.rst

### Availability

.. include:: /includes/extracts/changestream-rc-majority-4.2.rst

## Access Control

When running with access control, the user must have the :authaction:`find` and :authaction:`changeStream` privilege actions on `all non-systems collections across all databases<resource-all-but-system-collections>`.. That is, a user must have a `role <roles>` that grants the following `privilege <privileges>`:

```javascript
{ resource: { db: "", collection: "" }, actions: [ "find", "changeStream" ] }
```

The built-in :authrole:`read` role provides the appropriate privileges.

## Cursor Iteration

.. include:: /includes/fact-multiple-cursor-monitors.rst

## Example

The following operation in :binary:`~bin.mongosh` opens a change stream cursor on a replica set. The returned cursor reports on data changes to all the non-`system` collections across all databases except for the `admin`, `local`, and the `config` databases.

```javascript
watchCursor = db.getMongo().watch()
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
