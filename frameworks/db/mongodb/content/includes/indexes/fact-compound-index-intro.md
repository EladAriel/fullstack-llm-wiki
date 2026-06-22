---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/indexes/fact-compound-index-intro.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Compound indexes collect and sort data from multiple field values from each document in a collection. You can use the compound index to query the first field or any prefix fields of the index. The order of fields in a compound index is very important. The B-tree created by a compound index stores the sorted data in the order that the index specifies the fields.

For example, the following image shows a compound index where documents are first sorted by `userid` in ascending order (alphabetically). Then, the `scores` for each `userid` are sorted in descending order:

.. include:: /images/index-compound-key.rst
