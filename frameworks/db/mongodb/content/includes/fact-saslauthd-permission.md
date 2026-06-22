---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-saslauthd-permission.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Important:** The parent directory of the `saslauthd` Unix domain socket file
specified to :setting:`security.sasl.saslauthdSocketPath` or
:parameter:`--setParameter saslauthdPath <saslauthdPath>` must grant
read and execute  (`r-x`) permissions for either:
- The user starting the :binary:`mongod <bin.mongod>` or
  :binary:`mongos <bin.mongos>`, or
- A group to which that user belongs.
The :binary:`~bin.mongod` or :binary:`~bin.mongos` cannot successfully authenticate via
`saslauthd` without the specified permission on the `saslauthd`
directory and its contents.
