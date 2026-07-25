---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/planCacheStats/isActive.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

A boolean that indicates whether the entry is active or inactive.

- If active, the query planner is currently using the entry to generate
query plans.

- If inactive, the query planner is not currently using the entry to
generate query plans.

See `cache-entry-state`.
