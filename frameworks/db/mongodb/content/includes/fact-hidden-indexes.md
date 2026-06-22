---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-hidden-indexes.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

MongoDB offers the ability to hide or unhide indexes from the query planner. By hiding an index from the planner, you can evaluate the potential impact of dropping an index without actually dropping the index.

If after the evaluation, the user decides to drop the index, you can drop the hidden index; i.e. you do not need to unhide it first to drop it.

If, however, the impact is negative, the user can unhide the index instead of having to recreate a dropped index. And because indexes are fully maintained while hidden, the indexes are immediately available for use once unhidden.

For more information on hidden indexes, see `/core/index-hidden`.
