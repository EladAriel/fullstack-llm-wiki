---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/discovery-clients.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.097366Z"
---
# Discovery Clients

* [Redis-py](https://github.com/andymccurdy/redis-py) (Python redis client)
* [HiRedis](https://github.com/redis/hiredis) (C redis client)
* [Jedis](https://github.com/xetorthio/jedis) (Java redis client)
* [Ioredis](https://github.com/luin/ioredis) (NodeJS redis client)

If you need to use another client, consider using [Sentinel Tunnel](https://github.com/RedisLabs/sentinel_tunnel)
to discover the current Redis master with Sentinel and create a TCP tunnel between a local port on the client and the master.
