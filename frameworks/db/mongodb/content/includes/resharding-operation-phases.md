---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/resharding-operation-phases.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The resharding operation performs these phases in order:

#. The clone phase duplicates the current collection data. #. The building indexes phase builds indexes on the resharded collection. #. The catch-up phase applies any pending write operations to the resharded collection. #. The commit phase renames the temporary collection and drops the old collection to perform a cut-over.
