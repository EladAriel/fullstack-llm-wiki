---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-projecting-specific-elems.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

:projection:`$elemMatch`, :projection:`$slice`, and :projection:`$` are the only operators that you can use to project specific elements to include in the returned array. For instance, you cannot project specific array elements using the array index; e.g. `{ "instock.0": 1 }` projection does not project the array with the first element.
