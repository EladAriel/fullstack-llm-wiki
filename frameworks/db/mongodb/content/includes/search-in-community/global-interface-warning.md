---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/search-in-community/global-interface-warning.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
