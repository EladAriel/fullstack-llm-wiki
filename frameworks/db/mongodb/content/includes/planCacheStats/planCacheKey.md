---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/planCacheStats/planCacheKey.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

A hexadecimal string that represents the hash of the key used to find the plan cache entry associated with this query. The plan cache key is a function of both the `plan cache query shape` and the currently available indexes for that shape. See `explain.queryPlanner.planCacheKey`.
