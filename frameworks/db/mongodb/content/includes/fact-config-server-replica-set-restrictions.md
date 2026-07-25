---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-config-server-replica-set-restrictions.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The following restrictions apply to a replica set configuration when used for config servers:

- Must have zero `arbiters <replica-set-arbiter-configuration>`.
- Must have no :doc:`delayed members
</core/replica-set-delayed-member>`.

- Must build indexes (i.e. no member should have
:rsconf:`members[n].buildIndexes` setting set to false).
