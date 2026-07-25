---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/reference/fact-connection-check.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

`mongod` verifies the connection to the KMIP server on startup.

The server name specified in :setting:`security.kmip.serverName` must match either the Subject Alternative Name `SAN` or the Common Name `CN` on the certificate presented by the KMIP server. `SAN` can be a system name or an IP address.

If `SAN` is present, `mongod` does not try to match against `CN`.

If the hostname or IP address of the KMIP server does does not match either `SAN` or `CN`, `mongod` does not start.
