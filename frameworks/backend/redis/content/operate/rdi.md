---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rdi.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Redis Data Integration (RDI)
alwaysopen: false
categories:
- docs
- operate
description: Keep Redis in sync with a primary database in near real time.
linkTitle: Redis Data Integration (RDI)
weight: 60
---

Redis Data Integration (RDI) is a [change data capture](https://en.wikipedia.org/wiki/Change_data_capture) (CDC) system that tracks changes to the data in a non-Redis source database and makes corresponding changes to a Redis target database. You can use the target as a cache to improve performance because it will typically handle read queries much faster than the source.

See the main [RDI docs section]({{< relref "/integrate/redis-data-integration" >}})
under [Libraries and tools]({{< relref "/integrate" >}}) to learn how to install and use RDI on your own servers.  See the
[Redis Cloud RDI guide]({{< relref "/operate/rc/rdi" >}}) to learn how to set up RDI for a cloud database.
