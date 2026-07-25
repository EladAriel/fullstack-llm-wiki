---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/important-set-operator-semantics.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

|set-operator-name| performs set operation on arrays, treating arrays as sets. If an array contains duplicate entries, |set-operator-name| ignores the duplicate entries. |set-operator-name| ignores the order of the elements.

|set-operator-name| filters out duplicates in its result to output an array that contains only unique entries. The order of the elements in the output array is unspecified.
