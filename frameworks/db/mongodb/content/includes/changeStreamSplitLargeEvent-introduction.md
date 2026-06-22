---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/changeStreamSplitLargeEvent-introduction.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Splits large `change stream <changeStreams>` events that exceed 16 MB into smaller fragments returned in a change stream cursor.

You can only use `$changeStreamSplitLargeEvent` in a `$changeStream` pipeline and it must be the final stage in the pipeline.
