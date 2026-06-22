---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/array-filter-and-sort-example-explanation.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The sort is ascending, which means that the sort key is the lowest value in the `sizes` array:

- In document `_id: 'A'`, the lowest `sizes` element is `7`. This
value is used as the sort key even though it does not match the filter `{ sizes: { $gt: 9 }`.

- In document `_id: 'B'`, the lowest `sizes` element is `8`.
Similarly, this value is used as the sort key even though it does not match the filter.

The query returns the document with `_id: 'A'` first.
