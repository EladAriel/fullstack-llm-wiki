---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/rc-endpoint-description.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

Static endpoints on Redis Cloud start with `redis-<port>.c<number>` (or `redis-<port>.internal.c<number>` for the private endpoint). For example, a static endpoint might look like this:

```text
redis-12345.c12345.us-east-1-mz.ec2.cloud.rlrcp.com
```

Dynamic endpoints on Redis Cloud always contain three words and a random number, and end in `db.redis.io`. For example, a dynamic endpoint might look like this:

```text
horse-battery-staple-12345.db.redis.io
```

You can see the Dynamic endpoints for databases with both static and dynamic endpoints by expanding the **Dynamic endpoints** section in the **General** section of the **Configuration** tab. 

{{<image filename="images/rc/databases-configuration-general-endpoints-legacy.png" alt="The Static and dynamic endpoints for a database with both kinds of endpoints." >}}