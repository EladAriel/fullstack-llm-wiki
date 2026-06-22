---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-config-server-replica-set-restrictions.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The following restrictions apply to a replica set configuration when used for config servers:

- Must have zero `arbiters <replica-set-arbiter-configuration>`.
- Must have no :doc:`delayed members
</core/replica-set-delayed-member>`.

- Must build indexes (i.e. no member should have
:rsconf:`members[n].buildIndexes` setting set to false).
