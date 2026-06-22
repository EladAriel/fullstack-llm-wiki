---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-projecting-specific-elems.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

:projection:`$elemMatch`, :projection:`$slice`, and :projection:`$` are the only operators that you can use to project specific elements to include in the returned array. For instance, you cannot project specific array elements using the array index; e.g. `{ "instock.0": 1 }` projection does not project the array with the first element.
