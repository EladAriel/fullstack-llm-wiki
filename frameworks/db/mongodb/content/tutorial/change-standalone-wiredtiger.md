---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/change-standalone-wiredtiger.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================================

# Change a Self-Managed Standalone to WiredTiger

> **Note:** You must upgrade to WiredTiger. MongoDB removed the deprecated MMAPv1 storage
engine in version 4.2.

Use this tutorial to change the storage engine of a `standalone` MongoDB instance to `WiredTiger <storage-wiredtiger>`.

## Considerations

### `mongodump` and `mongorestore`

This tutorial uses the :binary:`~bin.mongodump` and :binary:`~bin.mongorestore` utilities to export and import data.

- Ensure that these MongoDB package components are installed and
updated on your system.

- Make sure you have sufficient drive space available for the
:binary:`~bin.mongodump` export file and the data files of your new :binary:`~bin.mongod` instance running with WiredTiger.

### Default Bind to Localhost

.. include:: /includes/fact-default-bind-ip-change.rst

The tutorial runs :binary:`~bin.mongodump` and :binary:`~bin.mongorestore` from the same host as the :binary:`~bin.mongod` they are connecting to. If run remotely, :binary:`~bin.mongodump` and :binary:`~bin.mongorestore` must specify the ip address or the associated hostname in order to connect to the :binary:`~bin.mongod`.

### XFS and WiredTiger

With the WiredTiger storage engine, using XFS for data bearing nodes is recommended on Linux. For more information, see `prod-notes-linux-file-system`.

### MMAPv1 Only Restrictions

.. include:: /includes/fact-mmapv1-only-restrictions.rst

## Procedure

.. include:: /includes/steps/change-standalone-wiredtiger.rst
