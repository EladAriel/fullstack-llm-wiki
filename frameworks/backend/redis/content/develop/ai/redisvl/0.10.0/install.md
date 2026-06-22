---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/develop/ai/redisvl/0.10.0/install.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
linkTitle: Install RedisVL
title: Install RedisVL
weight: 2
aliases:
- /integrate/redisvl/install
url: '/develop/ai/redisvl/0.10.0/install/'
---
## Installation

Install the `redisvl` package into your Python (>=3.8) environment using the `pip` command:

```shell
pip install redisvl
```

Then make sure to have a Redis instance with the Redis Query Engine features enabled on Redis Cloud or locally in docker with Redis Stack:

```shell
docker run -d --name redis -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
```

After running the previous command, the Redis Insight GUI will be available at http://localhost:8001.
