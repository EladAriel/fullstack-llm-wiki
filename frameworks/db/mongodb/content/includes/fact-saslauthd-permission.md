---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-saslauthd-permission.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
