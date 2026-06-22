---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/atlas-search-commands/behavior/update-behavior.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

|method-name-title| triggers an index build with the new index definition. There may be a delay between when you receive a response from the command and when the updated index is ready.

The old index definition can still support queries while the new index is being built. Once the new index finishes building, the old index is no longer usable. To see the status of your search indexes, use the :pipeline:`$listSearchIndexes` aggregation stage.
