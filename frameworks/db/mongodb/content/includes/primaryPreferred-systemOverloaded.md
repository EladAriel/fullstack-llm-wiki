---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/primaryPreferred-systemOverloaded.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

In sharded clusters that enable the ingress request rate limiter, shard nodes that are shedding load can return errors labeled `SystemOverloadedError`.

For clusters that have :parameter:`overloadAwareServerSelectionEnabled` set to `true`, when a primary responds with a retryable error labeled with `SystemOverloadedError`, the router may temporarily route reads to eligible secondaries instead of the overloaded server. This applies to any read preference that can select multiple servers. By default, `overloadAwareServerSelectionEnabled` is set to `false`.
