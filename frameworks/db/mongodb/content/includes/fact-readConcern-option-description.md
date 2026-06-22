---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-readConcern-option-description.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Possible read concern levels are:

- :readconcern:`"local"`. This is the default read concern level for
read operations against the primary and secondaries.

- :readconcern:`"available"`. Available for read operations against
the primary and secondaries. :readconcern:`"available"` behaves the same as :readconcern:`"local"` against the primary and non-sharded secondaries. The query returns the instance's most recent data.

- :readconcern:`"majority"`. Available for replica sets that use
`WiredTiger storage engine <storage-wiredtiger>`.

- :readconcern:`"linearizable"`. Available for read operations on the
:replstate:`primary <PRIMARY>` only.

- :readconcern:`"snapshot"`. Available for :ref:`multi-document
transactions <transactions>` and certain read operations outside of multi-document transactions.

For more formation on the read concern levels, see `read-concern-levels`.
