---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/qe-csfle-contention.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Concurrent write operations, such as inserting the same field/value pair into multiple documents in close succession, can cause contention: conflicts that delay operations.

With {+qe+}, MongoDB tracks the occurrences of each field/value pair in an encrypted collection using an internal counter. The `contention factor` partitions this counter, similar to an array. This minimizes issues with incrementing the counter when using `insert`, `update`, or `findAndModify` to add or modify an encrypted field with the same field/value pair in close succession. `contention = 0` creates an array with one element at index 0. `contention = 4` creates an array with 5 elements at indexes 0-4. MongoDB increments a random array element during insert.

When unset, `contention` defaults to `8`, which provides high performance for most workloads. Higher contention improves the performance of insert and update operations on low cardinality fields, but decreases find performance.
