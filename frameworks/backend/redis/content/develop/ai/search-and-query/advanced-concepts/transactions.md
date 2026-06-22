---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/develop/ai/search-and-query/advanced-concepts/transactions.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
categories:
- docs
- develop
- stack
- oss
- rs
- rc
- oss
- kubernetes
- clients
description: How Redis Search commands behave inside MULTI/EXEC transactions and Lua scripts
linkTitle: Search in transactions
title: Search commands in MULTI/EXEC transactions and Lua scripts
weight: 36
---

Redis Search commands ([`FT.SEARCH`]({{< relref "/commands/ft.search" >}}),
[`FT.AGGREGATE`]({{< relref "/commands/ft.aggregate" >}}),
[`FT.HYBRID`]({{< relref "/commands/ft.hybrid" >}}),
[`FT.PROFILE`]({{< relref "/commands/ft.profile" >}}), and
[`FT.CURSOR READ`]({{< relref "/commands/ft.cursor-read" >}}))
can be used inside [`MULTI`]({{< relref "/commands/multi" >}})/[`EXEC`]({{< relref "/commands/exec" >}})
transactions and [Lua scripts]({{< relref "/develop/programmability/lua-api" >}}),
but the behavior differs depending on your deployment topology.

## Standalone and single-shard deployments

Query commands inside a `MULTI`/`EXEC` block or Lua script (including when issued
through a client pipeline that wraps commands in a transaction) execute synchronously
on the main Redis thread, regardless of the
[`search-workers`]({{< relref "/develop/ai/search-and-query/administration/configuration#search-workers" >}})
setting.

The worker thread pool is bypassed in this context because Redis transactions
require all commands to complete sequentially without yielding to other clients.
As a result, queries inside transactions do not benefit from the parallelism
provided by `search-workers > 0`, but they execute correctly and return results
as expected.

## Multi-shard deployments (OSS Cluster and Redis Software with multiple shards)

Redis Search commands inside a `MULTI`/`EXEC` block or a Lua script are rejected with
the following error:

```
Cannot perform FT.SEARCH: Cannot block
```

This is because the coordinator must fan out the query to multiple shards and
collect results asynchronously, which is incompatible with the sequential
execution model of transactions. This limitation applies regardless of the
`search-workers` setting.

## Related commands

- [`FT.SEARCH`]({{< relref "/commands/ft.search" >}})
- [`FT.AGGREGATE`]({{< relref "/commands/ft.aggregate" >}})
- [`FT.HYBRID`]({{< relref "/commands/ft.hybrid" >}})
- [`FT.PROFILE`]({{< relref "/commands/ft.profile" >}})
- [`FT.CURSOR READ`]({{< relref "/commands/ft.cursor-read" >}})
- [`MULTI`]({{< relref "/commands/multi" >}})
- [`EXEC`]({{< relref "/commands/exec" >}})
