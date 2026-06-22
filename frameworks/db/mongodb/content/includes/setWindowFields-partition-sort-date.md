---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/setWindowFields-partition-sort-date.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

- `partitionBy: "$state"` :ref:`partitions
<setWindowFields-partitionBy>` the documents in the collection by `state`. There are partitions for `CA` and `WA`.

- `sortBy: { orderDate: 1 }` :ref:`sorts
<setWindowFields-sortBy>` the documents in each partition by `orderDate` in ascending order (`1`), so the earliest `orderDate` is first.
