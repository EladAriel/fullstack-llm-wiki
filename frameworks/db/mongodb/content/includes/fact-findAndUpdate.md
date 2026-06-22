---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-findAndUpdate.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Retryable writes require the |findMethod| method to copy the entire document into a special side collection for each node in a replica set before it performs the update. This can make |findMethod| an expensive operation when dealing with large documents or large replica sets.

.. versionadded:: 8.0
