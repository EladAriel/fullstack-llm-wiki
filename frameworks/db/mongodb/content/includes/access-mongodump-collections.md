---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/access-mongodump-collections.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

To run :binary:`~bin.mongodump` against a MongoDB deployment that has `access control <authorization>` enabled, you must have privileges that grant :authaction:`find` action for each database to back up. The built-in :authrole:`backup` role provides the required privileges to perform backup of any and all databases.

.. include:: /includes/fact-required-access-for-backup-profiling.rst
