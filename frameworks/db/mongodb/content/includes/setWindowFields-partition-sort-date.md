---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/setWindowFields-partition-sort-date.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

- `partitionBy: "$state"` :ref:`partitions
<setWindowFields-partitionBy>` the documents in the collection by `state`. There are partitions for `CA` and `WA`.

- `sortBy: { orderDate: 1 }` :ref:`sorts
<setWindowFields-sortBy>` the documents in each partition by `orderDate` in ascending order (`1`), so the earliest `orderDate` is first.
