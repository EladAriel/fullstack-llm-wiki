---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-findAndUpdate.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Retryable writes require the |findMethod| method to copy the entire document into a special side collection for each node in a replica set before it performs the update. This can make |findMethod| an expensive operation when dealing with large documents or large replica sets.

.. versionadded:: 8.0
