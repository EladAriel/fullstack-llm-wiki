---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-query-min-max.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The :method:`~cursor.min()` and :method:`~cursor.max()` methods indicate that the system should avoid normal query planning. They construct an index scan where the index bounds are explicitly specified by the values given in :method:`~cursor.min()` and :method:`~cursor.max()`.

> **Warning:** If one of the two boundaries is not specified, the query plan will be
an index scan that is unbounded on one side. This may degrade performance
compared to a query containing neither operator, or one that uses both
operators to more tightly constrain the index scan.
