---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/introduction-read-preference.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Read preference describes how MongoDB clients route read operations to the members of a `replica set`.

.. include:: /images/replica-set-read-preference.rst

By default, an application directs its read operations to the `primary` member in a `replica set` (that is, read preference mode "primary"). But, clients can specify a read preference to send read operations to secondaries.
