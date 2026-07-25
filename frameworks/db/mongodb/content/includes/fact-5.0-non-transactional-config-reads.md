---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-5.0-non-transactional-config-reads.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 5.0, non-transaction reads are not allowed on the `config.transactions` collection with the following read concerns and options:

- :readconcern:`"snapshot"`
- :readconcern:`"majority"` and the
`afterClusterTime<afterClusterTime>` option is set

- When using a :driver:`MongoDB Driver </>`
and :readconcern:`"majority"` within a `causally consistent session<sessions>`
