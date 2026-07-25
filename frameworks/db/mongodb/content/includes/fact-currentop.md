---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-currentop.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Because :dbcommand:`currentOp` command and :method:`db.currentOp()` helper returns the results in a single document, the total size of the :dbcommand:`currentOp` result set is subject to the maximum 16MB BSON size limit for documents.

MongoDB provides the :pipeline:`$currentOp` aggregation stage. The :pipeline:`$currentOp` stage returns a cursor over a stream of documents, each of which reports a single operation. Each operation document is subject to the 16MB BSON limit, but unlike the :dbcommand:`currentOp` command, there is no limit on the overall size of the result set.

For this reason, the :pipeline:`$currentOp` aggregation stage is preferred over the :dbcommand:`currentOp` command and its :binary:`~bin.mongosh` helper :method:`db.currentOp()`.
