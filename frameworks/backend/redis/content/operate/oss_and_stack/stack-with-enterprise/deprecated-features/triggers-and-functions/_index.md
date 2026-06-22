---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/triggers-and-functions/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
bannerChildren: true
bannerText: 'The Redis Stack triggers and functions feature preview has ended and it will not be promoted to GA.'
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
description: Trigger and execute JavaScript functions in the Redis process
linktitle: Triggers and functions
stack: true
title: Triggers and functions
weight: 16
aliases:
  - /develop/interact/programmability/triggers-and-functions/
  - /commands/tfcall/
  - /commands/tfcallasync/
  - /commands/tfunction-delete/
  - /commands/tfunction-list/
  - /commands/tfunction-load/
---

[![discord](https://img.shields.io/discord/697882427875393627?style=flat-square)](https://discord.gg/xTbqgTB)
[![Github](https://img.shields.io/static/v1?label=&message=repository&color=5961FF&logo=github)](https://github.com/RedisGears/RedisGears/)

The triggers and functions feature of Redis Stack allows running JavaScript functions inside Redis. These functions can be executed on-demand, by an event-driven trigger, or by a stream processing trigger.

## Quick links
* [Command documentation](https://github.com/RedisGears/RedisGears/tree/master/docs/commands)
* [Source code](https://github.com/RedisGears/RedisGears)
* [Latest release](https://github.com/RedisGears/RedisGears/releases)
* [Docker image](https://hub.docker.com/r/redis/redis-stack-server/)

## Primary features

* JavaScript engine for functions
* On-demand functions
* Keyspace triggers
* Stream triggers
* Async handling of functions
* Read data from across the cluster

## Cluster support

Triggers and functions support deployment and execution of functions across a cluster. Functions are executed on the correct shard based on the key that is changed or read functions can be executed on all to return a correct view of the data.

## References

### Blog posts

- [Expanding the Database Trigger Features in Redis](https://redis.com/blog/database-trigger-features/)

## Overview
