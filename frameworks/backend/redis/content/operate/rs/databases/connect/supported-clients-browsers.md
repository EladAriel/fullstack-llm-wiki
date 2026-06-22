---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/databases/connect/supported-clients-browsers.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Supported connection clients
categories:
- docs
- operate
- rs
description: Info about Redis client libraries and supported clients when using the
  discovery service.
weight: 10
---
You can connect to Redis Software databases programmatically using client libraries.

## Redis client libraries

To connect an application to a Redis database hosted by Redis Software, use a [client library]({{< relref "/develop/clients" >}}) appropriate for your programming language.

You can also use the `redis-cli` utility to connect to a database from the command line.

For examples of each approach, see the [Redis Software quickstart]({{< relref "/operate/rs/installing-upgrading/quickstarts/redis-enterprise-software-quickstart" >}}).

Note: You cannot use client libraries to configure Redis Software.  Instead, use:

- The Redis Software [Cluster Manager UI]({{< relref "/operate/rs/installing-upgrading/quickstarts/redis-enterprise-software-quickstart" >}})
- The [REST API]({{< relref "/operate/rs/references/rest-api" >}})
- Command-line utilities, such as [`rladmin`]({{< relref "/operate/rs/references/cli-utilities/rladmin" >}})

### Discovery service

All [recommended Redis client libraries]({{< relref "/develop/clients" >}}) support the Redis Sentinel API, so you can use any of them with the [discovery service]({{< relref "/operate/rs/databases/durability-ha/discovery-service.md" >}}).

If you need to use a client that doesn't support Sentinel, you can use [Sentinel Tunnel](https://github.com/RedisLabs/sentinel_tunnel) to discover the current primary Redis endpoint with Sentinel and create a TCP tunnel between a local port on the client and the primary endpoint.

