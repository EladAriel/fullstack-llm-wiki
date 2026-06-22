---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/resharding-operation-phases.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The resharding operation performs these phases in order:

#. The clone phase duplicates the current collection data. #. The building indexes phase builds indexes on the resharded collection. #. The catch-up phase applies any pending write operations to the resharded collection. #. The commit phase renames the temporary collection and drops the old collection to perform a cut-over.
