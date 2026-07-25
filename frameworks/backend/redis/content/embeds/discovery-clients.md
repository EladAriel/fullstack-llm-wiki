---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/discovery-clients.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

* [Redis-py](https://github.com/andymccurdy/redis-py) (Python redis client)
* [HiRedis](https://github.com/redis/hiredis) (C redis client)
* [Jedis](https://github.com/xetorthio/jedis) (Java redis client)
* [Ioredis](https://github.com/luin/ioredis) (NodeJS redis client)

If you need to use another client, consider using [Sentinel Tunnel](https://github.com/RedisLabs/sentinel_tunnel)
to discover the current Redis master with Sentinel and create a TCP tunnel between a local port on the client and the master.
