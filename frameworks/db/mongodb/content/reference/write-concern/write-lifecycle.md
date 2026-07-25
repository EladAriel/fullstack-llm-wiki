---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/write-concern/write-lifecycle.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

========================

# Write Lifecycle Diagrams

These diagrams show the lifecycle of a :dbcommand:`findAndModify` operation on primary and secondary replica set members. The lifecycles of other write commands are similar, but the number of resulting oplog entries may vary.

## Write Lifecycle on a Primary Member

.. figure:: /images/write-lifecycle/write-lifecycle-primary-7-0.png

## Write Lifecycle on a Secondary Member

.. figure:: /images/write-lifecycle/write-lifecycle-secondary-7-0.png
