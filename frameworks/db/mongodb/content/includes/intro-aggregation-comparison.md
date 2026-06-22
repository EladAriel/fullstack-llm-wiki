---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/intro-aggregation-comparison.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Comparison expressions return a boolean except for :expression:`$cmp` which returns a number.

The comparison expressions take two argument expressions and compare both value and type, using the `specified BSON comparison order <bson-types-comparison-order>` for values of different types.
