---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/rc-context-retriever-get-started.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

To set up a Redis Context Retriever on Redis Cloud, you need a database on Redis Cloud that already has relevant data. If you use a relational database, use [Redis Data Integration (RDI)]({{< relref "/operate/rc/rdi" >}}) to ingest data into a Redis Cloud database.

When you have a database, [Create a context retriever service]({{< relref "/operate/rc/context-engine/context-retriever/create-service" >}}) for your database on Redis Cloud.

After you set up Context Retriever, you can [view your service]({{< relref "/operate/rc/context-engine/context-retriever/view-service" >}}). See the [Context Surfaces Python Client](https://pypi.org/project/redis-context-retriever/) for more information on how to call your tools.