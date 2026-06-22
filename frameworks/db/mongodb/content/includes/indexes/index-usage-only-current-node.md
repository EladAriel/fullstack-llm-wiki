---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/indexes/index-usage-only-current-node.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Warning:** :pipeline:`$indexStats` reports index usage metrics in the
`accesses <indexStats-output-accesses>` field only for the node
where the query runs. For more comprehensive index usage statistics,
run :pipeline:`$indexStats` on each node in the cluster.
