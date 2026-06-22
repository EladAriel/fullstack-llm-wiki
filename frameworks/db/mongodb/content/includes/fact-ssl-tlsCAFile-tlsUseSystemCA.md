---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-ssl-tlsCAFile-tlsUseSystemCA.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

When starting a :binary:`~bin.mongod` instance with `TLS/SSL enabled <configure-mongod-mongos-for-tls-ssl>`, you must specify a value for the :option:`--tlsCAFile <mongod --tlsCAFile>` flag, the :setting:`net.tls.CAFile` configuration option, or the :parameter:`tlsUseSystemCA` parameter.

`--tlsCAFile`, `tls.CAFile`, and `tlsUseSystemCA` are all mutually exclusive.
