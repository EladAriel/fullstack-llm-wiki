---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/connection-pool/max-connecting-use-case.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Raising the value of `maxConnecting` allows the client to establish connection to the server faster, but increases the chance of `connection storms <connection storm>`. If the value of `maxConnecting` is too low, your connection pool may experience heavy throttling and increased tail latency for clients checking out connections.
