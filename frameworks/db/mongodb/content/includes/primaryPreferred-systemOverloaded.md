---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/primaryPreferred-systemOverloaded.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

In sharded clusters that enable the ingress request rate limiter, shard nodes that are shedding load can return errors labeled `SystemOverloadedError`.

For clusters that have :parameter:`overloadAwareServerSelectionEnabled` set to `true`, when a primary responds with a retryable error labeled with `SystemOverloadedError`, the router may temporarily route reads to eligible secondaries instead of the overloaded server. This applies to any read preference that can select multiple servers. By default, `overloadAwareServerSelectionEnabled` is set to `false`.
