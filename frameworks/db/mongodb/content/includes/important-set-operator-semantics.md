---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/important-set-operator-semantics.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

|set-operator-name| performs set operation on arrays, treating arrays as sets. If an array contains duplicate entries, |set-operator-name| ignores the duplicate entries. |set-operator-name| ignores the order of the elements.

|set-operator-name| filters out duplicates in its result to output an array that contains only unique entries. The order of the elements in the output array is unspecified.
