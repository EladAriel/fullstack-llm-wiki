---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/sharding/targeted-mirror-reads-overview.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 8.2, you can selectively mirror read operations to specific servers that need their caches warmed up by tagging the nodes for read mirroring. Unlike general mirrored reads, targeted read mirroring allows you to target hidden nodes and mirror from both primary and secondary nodes.

You can configure targeted mirrored reads using the `targetedMirroring` field in the :parameter:`mirrorReads` parameter.
