---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/warning-rs-reconfig.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Warning:** - The :method:`rs.reconfig()` shell method can force the current
  primary to step down, which causes an :ref:`election
  <replica-set-elections>`. When the primary steps down, the
  :binary:`~bin.mongod` closes all client connections. While this
  typically takes 10-20 seconds, try to make these changes during
  scheduled maintenance periods.
- .. include:: /includes/warning-mixed-version-rs-config.rst
