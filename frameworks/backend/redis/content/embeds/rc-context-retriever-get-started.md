---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/rc-context-retriever-get-started.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.101790Z"
---
# Rc Context Retriever Get Started

To set up a Redis Context Retriever on Redis Cloud, you need a database on Redis Cloud that already has relevant data. If you use a relational database, use [Redis Data Integration (RDI)]({{< relref "/operate/rc/rdi" >}}) to ingest data into a Redis Cloud database.

When you have a database, [Create a context retriever service]({{< relref "/operate/iris/context-retriever/create-service" >}}) for your database on Redis Cloud.

After you set up Context Retriever, you can [view your service]({{< relref "/operate/iris/context-retriever/view-service" >}}). See the [Context Surfaces Python Client](https://pypi.org/project/redis-context-retriever/) for more information on how to call your tools.