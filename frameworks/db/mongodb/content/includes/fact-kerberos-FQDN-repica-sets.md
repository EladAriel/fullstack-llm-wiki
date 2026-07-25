---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-kerberos-FQDN-repica-sets.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

For replica sets and sharded clusters, ensure that your configuration uses fully qualified domain names (FQDN) rather than IP addresses or unqualified hostnames. You must use the FQDN for GSSAPI to correctly resolve the Kerberos realms and allow you to connect.
