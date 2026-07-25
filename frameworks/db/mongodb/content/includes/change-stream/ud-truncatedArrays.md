---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/change-stream/ud-truncatedArrays.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

An array of documents which record array truncations performed with pipeline-based updates using one or more of the following stages:

- :pipeline:`$addFields`
- :pipeline:`$set`
- :pipeline:`$replaceRoot`
- :pipeline:`$replaceWith`
If the entire array is replaced, the truncations will be reported under `updateDescription.updatedFields <|idref|-ud-updatedFields>`.
