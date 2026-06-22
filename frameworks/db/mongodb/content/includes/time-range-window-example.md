---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/time-range-window-example.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

In the example:

- `partitionBy: "$state"` :ref:`partitions
<setWindowFields-partitionBy>` the documents in the collection by `state`. There are partitions for `CA` and `WA`.

- `sortBy: { orderDate: 1 }` :ref:`sorts
<setWindowFields-sortBy>` the documents in each partition by `orderDate` in ascending order (`1`), so the earliest `orderDate` is first.

- `output`:
- Sets the `recentOrders` field to an array of `orderDate`
values for the documents in each `state`. The array elements are expanded with additions to the previous elements in the array.

- Uses :group:`$push` to return an array of `orderDate`
values from the documents in a `range <setWindowFields-range>` window.
