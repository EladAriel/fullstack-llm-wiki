---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/sharding/targeted-mirror-reads-overview.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 8.2, you can selectively mirror read operations to specific servers that need their caches warmed up by tagging the nodes for read mirroring. Unlike general mirrored reads, targeted read mirroring allows you to target hidden nodes and mirror from both primary and secondary nodes.

You can configure targeted mirrored reads using the `targetedMirroring` field in the :parameter:`mirrorReads` parameter.
