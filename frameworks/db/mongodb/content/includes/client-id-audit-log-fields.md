---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/client-id-audit-log-fields.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 8.1, `mongos` parses the proxy protocol header and stores the origin client computer IP address and port in the `remote` field. Also, if a load balancer is used, the `intermediates` document stores the load balancer IP address and port.

In MongoDB versions earlier than 8.1, the load balancer IP address and port are stored in the `remote` field and the origin client computer IP address and port are omitted.
