---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/client_references/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.368549Z"
---
# _Index

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
url: '/operate/rs/7.22/references/client_references/'
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
