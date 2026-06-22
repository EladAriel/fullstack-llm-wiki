---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-query-min-max.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The :method:`~cursor.min()` and :method:`~cursor.max()` methods indicate that the system should avoid normal query planning. They construct an index scan where the index bounds are explicitly specified by the values given in :method:`~cursor.min()` and :method:`~cursor.max()`.

> **Warning:** If one of the two boundaries is not specified, the query plan will be
an index scan that is unbounded on one side. This may degrade performance
compared to a query containing neither operator, or one that uses both
operators to more tightly constrain the index scan.
