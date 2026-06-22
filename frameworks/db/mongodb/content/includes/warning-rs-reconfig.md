---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/warning-rs-reconfig.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Warning:** - The :method:`rs.reconfig()` shell method can force the current
  primary to step down, which causes an :ref:`election
  <replica-set-elections>`. When the primary steps down, the
  :binary:`~bin.mongod` closes all client connections. While this
  typically takes 10-20 seconds, try to make these changes during
  scheduled maintenance periods.
- .. include:: /includes/warning-mixed-version-rs-config.rst
