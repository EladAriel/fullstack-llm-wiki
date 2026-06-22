---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-kerberos-FQDN-repica-sets.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

For replica sets and sharded clusters, ensure that your configuration uses fully qualified domain names (FQDN) rather than IP addresses or unqualified hostnames. You must use the FQDN for GSSAPI to correctly resolve the Kerberos realms and allow you to connect.
