---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/spring-framework-cache/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:56.164815Z"
---
# _Index

---
LinkTitle: Spring Data Redis
Title: Spring Data Redis
alwaysopen: false
categories:
- docs
- integrate
- stack
- oss
- rs
- rc
- oss
- client
description: Plug Redis into your Spring application with minimal effort
group: framework
hideListLinks: true
summary: Spring Data Redis integrates Redis with the Spring framework, letting you
  use Redis as a cache and add client-side failover to your connections.
type: integration
weight: 8
---

[Spring Data Redis](https://spring.io/projects/spring-data-redis) integrates Redis with the [Spring framework](https://spring.io/projects/spring-framework), letting you plug Redis into your Spring application with minimal effort. It works with the [Lettuce]({{< relref "/develop/clients/lettuce" >}}) and [Jedis]({{< relref "/develop/clients/jedis" >}}) clients, so Spring applications can take advantage of those clients' connection features as well as Spring's own abstractions.

The pages in this section describe recipes for using Redis from Spring Data Redis:

- [Use Redis with the Spring cache abstraction]({{< relref "/integrate/spring-framework-cache/cache" >}}) shows how to use Redis as the storage for Spring's cache abstraction.
- [Client-side geographic failover]({{< relref "/integrate/spring-framework-cache/geo-failover" >}}) shows how to configure resilient connections that automatically fail over between Redis endpoints.
