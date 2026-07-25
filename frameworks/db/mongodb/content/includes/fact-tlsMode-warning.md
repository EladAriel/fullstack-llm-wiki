---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-tlsMode-warning.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

If you set :option:`--tlsMode <mongod --tlsMode>`  to any value other than `disabled`, MongoDB uses the certificate specified in :setting:`net.tls.certificateKeyFile` for both server and client authentication in internal replica set connections. This certificate setting applies regardless of whether you set :setting:`security.clusterAuthMode` to `X.509`.
