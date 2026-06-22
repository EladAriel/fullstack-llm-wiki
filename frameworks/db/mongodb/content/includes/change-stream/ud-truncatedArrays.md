---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/change-stream/ud-truncatedArrays.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

An array of documents which record array truncations performed with pipeline-based updates using one or more of the following stages:

- :pipeline:`$addFields`
- :pipeline:`$set`
- :pipeline:`$replaceRoot`
- :pipeline:`$replaceWith`
If the entire array is replaced, the truncations will be reported under `updateDescription.updatedFields <|idref|-ud-updatedFields>`.
