---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-sparse-index-hint-count.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

If you include a :method:`~cursor.hint()` that specifies a `sparse index <index-type-sparse>` when you perform a :method:`~cursor.count()` of all documents in a collection (i.e. with an empty query predicate), the sparse index is used even if the sparse index results in an incorrect count.

For example, create a sparse index on the `rated` field on the `movies` collection.

If you count the number of documents in the `movies` collection and include a hint that specifies that sparse index, the operation returns only the documents that contain the `rated` field.

To obtain the correct count of the number of documents in the `movies` collection, do not :method:`~cursor.hint()` with a `sparse index <index-type-sparse>` when performing a count of all documents in a collection.
