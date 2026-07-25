---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-enable-runtime-audit-configuration.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 5.0, audit configurations for :binary:`~bin.mongod` and :binary:`~bin.mongos` nodes can be configured at runtime. A group of these nodes can take part in a distributed audit configuration.

To include a node in a distributed audit configuration, update the node's configuration file as follows and restart the server.

The server logs an error and fails to start if:

- `runtimeConfiguration` is `true` and
- either :setting:`auditLog.filter` or :parameter:`auditAuthorizationSuccess` is set.
To modify audit filters and the :parameter:`auditAuthorizationSuccess` parameter at runtime, see :parameter:`auditConfig`.
