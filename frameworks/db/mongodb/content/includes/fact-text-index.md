---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-text-index.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

To run `$text` queries, you must have a `text index <index-feature-text>` on your collection. MongoDB provides text indexes to support `$text` queries on string content. Text indexes can include any field whose value is a string or an array of string elements. A collection can only have **one** text index, but that index can cover multiple fields.
