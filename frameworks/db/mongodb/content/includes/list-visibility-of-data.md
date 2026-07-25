---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/list-visibility-of-data.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

- Regardless of a write's `write concern <write-concern>`, other
clients using :readconcern:`"local"` or :readconcern:`"available"` read concern can see the result of a write operation before the write operation is acknowledged to the issuing client.

- Clients using :readconcern:`"local"` or :readconcern:`"available"`
read concern can read data which may be subsequently `rolled back </core/replica-set-rollbacks>` during replica set failovers.

For operations in a `multi-document transaction </core/transactions>`, when a transaction commits, all data changes made in the transaction are saved and visible outside the transaction. That is, a transaction will not commit some of its changes while rolling back others.

.. include:: /includes/extracts/transactions-committed-visibility.rst
