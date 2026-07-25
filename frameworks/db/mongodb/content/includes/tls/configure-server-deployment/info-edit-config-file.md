---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/tls/configure-server-deployment/info-edit-config-file.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

On **each node,** locate and open your `mongod` configuration file. If the file does not exist, create it. Add the following `TLS options <net-tls-conf-options>`. Use absolute paths to the certificate files.

For example, the configuration file for your primary node looks like the following:
