---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-invalid-balancer-setting-values.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 6.2, you must set `value between 1 and 1024 (inclusive) when inserting or updating documents with the id: chunksize` field in the `config.settings` collection. If you specify an invalid `value`, MongoDB returns a schema validation error.

Any `value` fields outside the range of 1 to 1024 MB (inclusive) set prior to MongoDB 6.2 remain unchanged.
