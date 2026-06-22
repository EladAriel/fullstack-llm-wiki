---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/stop-unsharding-collection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# Stop Unsharding a Collection

You can stop unsharding a sharded collection with the :dbcommand:`abortUnshardCollection` command.

## About this Task

To stop an in-progress `unshardCollection` operation, run the `abortUnshardCollection` command.

.. include:: /includes/resharding-oplog-note.rst

### Compatibility

You can perform this task on deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

> **Note:** This task is not available on the {+atlas+} Free or Flex Tiers.

.. include:: /includes/fact-environments-onprem-only.rst

### Restrictions

.. include:: /includes/auc-considerations.rst

## Access Control

If your deployment has `access control <authorization>` enabled, the :authrole:`enableSharding` role grants you access to run the `abortUnshardCollection` command.

## Steps

## Learn More

- :dbcommand:`abortUnshardCollection`
- :method:`sh.abortUnshardCollection()`
- `unshard-collection-task`
