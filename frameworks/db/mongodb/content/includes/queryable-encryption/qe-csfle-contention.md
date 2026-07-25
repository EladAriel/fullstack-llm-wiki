---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/qe-csfle-contention.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Concurrent write operations, such as inserting the same field/value pair into multiple documents in close succession, can cause contention: conflicts that delay operations.

With {+qe+}, MongoDB tracks the occurrences of each field/value pair in an encrypted collection using an internal counter. The `contention factor` partitions this counter, similar to an array. This minimizes issues with incrementing the counter when using `insert`, `update`, or `findAndModify` to add or modify an encrypted field with the same field/value pair in close succession. `contention = 0` creates an array with one element at index 0. `contention = 4` creates an array with 5 elements at indexes 0-4. MongoDB increments a random array element during insert.

When unset, `contention` defaults to `8`, which provides high performance for most workloads. Higher contention improves the performance of insert and update operations on low cardinality fields, but decreases find performance.
