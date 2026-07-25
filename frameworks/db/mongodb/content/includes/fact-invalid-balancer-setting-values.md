---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-invalid-balancer-setting-values.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 6.2, you must set `value between 1 and 1024 (inclusive) when inserting or updating documents with the id: chunksize` field in the `config.settings` collection. If you specify an invalid `value`, MongoDB returns a schema validation error.

Any `value` fields outside the range of 1 to 1024 MB (inclusive) set prior to MongoDB 6.2 remain unchanged.
