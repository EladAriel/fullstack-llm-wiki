---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-5.0-non-transactional-config-reads.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 5.0, non-transaction reads are not allowed on the `config.transactions` collection with the following read concerns and options:

- :readconcern:`"snapshot"`
- :readconcern:`"majority"` and the
`afterClusterTime<afterClusterTime>` option is set

- When using a :driver:`MongoDB Driver </>`
and :readconcern:`"majority"` within a `causally consistent session<sessions>`
