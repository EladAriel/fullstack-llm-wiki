---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/array-filter-and-sort-example-setup.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

When you filter and sort by a field that contains an array, the filter does not affect the value used as the `sort key`. The sort always considers all array values as potential sort keys.

For example, the following query finds shoes with sizes greater than 9 and sorts the results by size in ascending order:
