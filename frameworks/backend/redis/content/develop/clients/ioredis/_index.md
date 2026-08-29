---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/develop/clients/ioredis/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:56.085671Z"
---
# _Index

---
aliases:
- /connect/clients/ioredis/
- /clients/ioredis/
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
description: Connect your Node.js/JavaScript application to a Redis database
linkTitle: ioredis (JavaScript)
title: ioredis guide (JavaScript)
weight: 5
---

[`ioredis`](https://github.com/redis/ioredis) is a Redis client for Node.js/JavaScript.
The sections below explain how to install `ioredis` and connect your application
to a Redis database.

{{< note >}}Redis actively maintains and supports `ioredis` since it is in widespread use, but
for new projects, we recommend using our newer Node.js client
[`node-redis`]({{< relref "/develop/clients/nodejs" >}}). See
[Migrate from ioredis]({{< relref "/develop/clients/nodejs/migration" >}})
if you are interested in converting an existing `ioredis` project to `node-redis`.
{{< /note >}}

`ioredis` requires a running Redis server. See [here]({{< relref "/operate/oss_and_stack/install/" >}}) for Redis Open Source installation instructions.

## Install

To install `ioredis`, run:

```bash
npm install ioredis
```

## Connect and test

Connect to localhost on port 6379. 

{{< clients-example set="landing" step="connect" lang_filter="ioredis" >}}
{{< /clients-example >}}

Store and retrieve a simple string.

{{< clients-example set="landing" step="set_get_string" lang_filter="ioredis" >}}
{{< /clients-example >}}

Store and retrieve a map.

{{< clients-example set="landing" step="set_get_hash" lang_filter="ioredis" >}}
{{< /clients-example >}}

When you have finished using a connection, close it with `client.quit()`.

{{< clients-example set="landing" step="close" lang_filter="ioredis" >}}
{{< /clients-example >}}

## More information

The [Github repository](https://github.com/redis/ioredis) has useful
information, including [API docs](https://redis.github.io/ioredis/index.html)
and a set of [code examples](https://github.com/redis/ioredis/tree/main/examples).
