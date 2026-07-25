---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/array-filter-and-sort-example-setup.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

When you filter and sort by a field that contains an array, the filter does not affect the value used as the `sort key`. The sort always considers all array values as potential sort keys.

For example, the following query finds shoes with sizes greater than 9 and sorts the results by size in ascending order:
