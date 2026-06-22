---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/sharding/reshard-build-indexes-consideration.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Index builds that occur during resharding might silently fail.

- Do not create indexes during the resharding process.
- Do not start the resharding process if there are ongoing index builds.
If the collection you're resharding uses :atlas:`{+fts+} </atlas-search>`, the search index becomes unavailable when the resharding operation completes. You need to manually rebuild the search index once the resharding operation completes.
