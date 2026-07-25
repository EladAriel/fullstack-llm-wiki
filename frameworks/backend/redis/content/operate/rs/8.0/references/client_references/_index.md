---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/8.0/references/client_references/_index.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Develop with Redis clients
alwaysopen: false
categories:
- docs
- operate
- rs
description: Redis client libraries allow you to connect to Redis instances from within
  your application. This section provides an overview of several recommended Redis
  clients for popular programming and scripting languages.
hideListLinks: true
linkTitle: Redis clients
weight: 80
url: '/operate/rs/8.0/references/client_references/'
---
To connect to Redis instances from within your application, use a Redis client library that matches your application's language.

## Official clients

| Language | Client name |
| :---------- | :------------- |
| .Net | [StackExchange.Redis]({{< relref "/develop/clients/dotnet" >}}) |
| Go | [go-redis]({{< relref "/develop/clients/go" >}}) |
| Java | [Jedis]({{< relref "/develop/clients/jedis" >}}) (Synchronous) and [Lettuce]({{< relref "/develop/clients/lettuce" >}}) (Asynchronous) |
| Node.js | [node-redis]({{< relref "/develop/clients/nodejs" >}}) |
| Python | [redis-py]({{< relref "/develop/clients/redis-py" >}}) |

Select a client name to see its quick start.

## Other clients

For a list of community-driven Redis clients, which are available for more programming languages, see
[Community-supported clients]({{< relref "/develop/clients#community-supported-clients" >}}).
