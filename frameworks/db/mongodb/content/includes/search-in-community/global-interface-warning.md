---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/search-in-community/global-interface-warning.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Warning:** Depending on your system topology, it may be necessary
to bind the `mongot` query server to an interface accessible
from your MongoDb Cluster. While binding to the `0.0.0.0`
IP address is permitted, it exposes the server to all public
networks and carries the risk of unauthorized access.
To enhance security, consider restricting `server.grpc.address`
to specific interfaces that are controlled and protected at
the network layer such as `localhost` or other trusted
internal addresses.
