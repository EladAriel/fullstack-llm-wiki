---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/discovery-clients.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

* [Redis-py](https://github.com/andymccurdy/redis-py) (Python redis client)
* [HiRedis](https://github.com/redis/hiredis) (C redis client)
* [Jedis](https://github.com/xetorthio/jedis) (Java redis client)
* [Ioredis](https://github.com/luin/ioredis) (NodeJS redis client)

If you need to use another client, consider using [Sentinel Tunnel](https://github.com/RedisLabs/sentinel_tunnel)
to discover the current Redis master with Sentinel and create a TCP tunnel between a local port on the client and the master.
