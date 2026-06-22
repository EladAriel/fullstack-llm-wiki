---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-tlsMode-warning.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

If you set :option:`--tlsMode <mongod --tlsMode>`  to any value other than `disabled`, MongoDB uses the certificate specified in :setting:`net.tls.certificateKeyFile` for both server and client authentication in internal replica set connections. This certificate setting applies regardless of whether you set :setting:`security.clusterAuthMode` to `X.509`.
