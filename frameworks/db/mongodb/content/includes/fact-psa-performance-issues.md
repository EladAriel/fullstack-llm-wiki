---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-psa-performance-issues.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

If you are using a three-member primary-secondary-arbiter (PSA) architecture, consider the following:

- The write concern :writeconcern:`"majority"` can cause
performance issues if a secondary is unavailable or lagging. For advice on how to mitigate these issues, see `performance-issues-psa`.

- If you are using a global default :readconcern:`"majority"`
and the write concern is less than the size of the majority, your queries may return stale (not fully replicated) data.
