---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-update-writeConcernError-mongos.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

.. versionchanged:: 8.1.2

When |cmd| executes on :program:`mongos` in a sharded cluster, a `writeConcernError` is always reported in the response, even when one or more other errors occur. In previous releases, other errors sometimes caused |cmd| to not report write concern errors.

For example, if a document fails validation, triggering a `DocumentValidationFailed` error, and a write concern error also occurs, both the `DocumentValidationFailed` error and the `writeConcernError` are returned in the top-level field of the response.
