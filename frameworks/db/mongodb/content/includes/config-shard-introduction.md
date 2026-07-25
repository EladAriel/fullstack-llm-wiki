---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/config-shard-introduction.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

.. versionadded:: 8.0

Starting in MongoDB 8.0, you can:

- Configure a config server to store your application data in
addition to the usual `sharded cluster` metadata. A config server that stores application data is called a config shard.

- Transition a config server between being a config
shard and a dedicated config server.

A cluster requires a config server, but it can be a config shard instead of a dedicated config server. Using a config shard reduces the number of nodes required and can simplify your deployment.

If your application has demanding availability and resiliency requirements, consider deploying a dedicated config server. A dedicated config server provides isolation, dedicated resources, and consistent performance for critical cluster operations.
