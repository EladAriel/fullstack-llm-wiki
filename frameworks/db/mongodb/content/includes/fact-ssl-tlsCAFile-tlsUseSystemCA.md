---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-ssl-tlsCAFile-tlsUseSystemCA.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

When starting a :binary:`~bin.mongod` instance with `TLS/SSL enabled <configure-mongod-mongos-for-tls-ssl>`, you must specify a value for the :option:`--tlsCAFile <mongod --tlsCAFile>` flag, the :setting:`net.tls.CAFile` configuration option, or the :parameter:`tlsUseSystemCA` parameter.

`--tlsCAFile`, `tls.CAFile`, and `tlsUseSystemCA` are all mutually exclusive.
