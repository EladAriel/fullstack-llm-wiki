---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/client-id-audit-log-fields.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 8.1, `mongos` parses the proxy protocol header and stores the origin client computer IP address and port in the `remote` field. Also, if a load balancer is used, the `intermediates` document stores the load balancer IP address and port.

In MongoDB versions earlier than 8.1, the load balancer IP address and port are stored in the `remote` field and the origin client computer IP address and port are omitted.
