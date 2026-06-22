---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/intra-cluster-authentication.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 5.3, `SCRAM-SHA-1 <authentication-scram-sha-1>` cannot be used for intra-cluster authentication. Only `SCRAM-SHA-256 <authentication-scram-sha-256>` is supported.

In previous MongoDB versions, SCRAM-SHA-1 and SCRAM-SHA-256 can both be used for intra-cluster authentication, even if SCRAM is not explicitly enabled.
