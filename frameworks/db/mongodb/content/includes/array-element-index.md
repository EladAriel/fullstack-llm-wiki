---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/array-element-index.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

MongoDB 8.3 improves access to array element indexes in :expression:`$map`, :expression:`$filter`, and :expression:`$reduce` aggregation expressions. You can use the new `arrayIndexAs` field to set a variable to store the index of an array element. You can also use the new :variable:`$$IDX <IDX>` aggregation system variable to access the index of the current array element if you omit `arrayIndexAs`.
