---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/list-visibility-of-data.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

- Regardless of a write's `write concern <write-concern>`, other
clients using :readconcern:`"local"` or :readconcern:`"available"` read concern can see the result of a write operation before the write operation is acknowledged to the issuing client.

- Clients using :readconcern:`"local"` or :readconcern:`"available"`
read concern can read data which may be subsequently `rolled back </core/replica-set-rollbacks>` during replica set failovers.

For operations in a `multi-document transaction </core/transactions>`, when a transaction commits, all data changes made in the transaction are saved and visible outside the transaction. That is, a transaction will not commit some of its changes while rolling back others.

.. include:: /includes/extracts/transactions-committed-visibility.rst
