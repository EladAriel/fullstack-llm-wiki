---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/write-concern/write-lifecycle.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================

# Write Lifecycle Diagrams

These diagrams show the lifecycle of a :dbcommand:`findAndModify` operation on primary and secondary replica set members. The lifecycles of other write commands are similar, but the number of resulting oplog entries may vary.

## Write Lifecycle on a Primary Member

.. figure:: /images/write-lifecycle/write-lifecycle-primary-7-0.png

## Write Lifecycle on a Secondary Member

.. figure:: /images/write-lifecycle/write-lifecycle-secondary-7-0.png
