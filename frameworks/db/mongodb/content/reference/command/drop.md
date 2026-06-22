---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/drop.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================

# drop (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has following syntax:

```javascript
db.runCommand(
   { 
     drop: <collection_name>, 
     writeConcern: <document>, 
     comment: <any> 
   }
)
```

## Command Fields

The command takes the following fields:

:binary:`~bin.mongosh` provides the equivalent helper method :method:`db.collection.drop()`.

## Behavior

- Starting in MongoDB 5.0, the :dbcommand:`drop` command and the
:method:`db.collection.drop()` method will raise an error if passed an unrecognized parameter.

- This command also removes any indexes associated with the dropped
collection.

- .. include:: /includes/extracts/4.4-changes-drop-in-progress-indexes.rst
- The :dbcommand:`drop` command and its helper
:method:`db.collection.drop()` create an `change-event-invalidate` for any `/changeStreams` opened on the dropped collection.

- .. include:: /includes/extracts/zoned-sharding-drop-collection-change.rst
- .. include:: /includes/extracts/5.0-changes-drop-sharding.rst
### Resource Locking

.. include:: /includes/extracts/drop-resource-lock.rst
