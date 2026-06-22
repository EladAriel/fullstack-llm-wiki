---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/ddl-ops-write-concern-sharded-clusters.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

On a sharded cluster, `DDL (Data Definition Language) operations <ddl-operations>` run with write concern :writeconcern:`"majority"`. If you specify a different write concern, the operation overrides the provided write concern with `"majority"`.
