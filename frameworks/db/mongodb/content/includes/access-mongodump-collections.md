---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/access-mongodump-collections.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

To run :binary:`~bin.mongodump` against a MongoDB deployment that has `access control <authorization>` enabled, you must have privileges that grant :authaction:`find` action for each database to back up. The built-in :authrole:`backup` role provides the required privileges to perform backup of any and all databases.

.. include:: /includes/fact-required-access-for-backup-profiling.rst
