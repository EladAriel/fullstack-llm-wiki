---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/8.0/references/rest-api/requests/_index.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Redis Software REST API requests
alwaysopen: false
categories:
- docs
- operate
- rs
description: Documents the requests supported by the Redis Software REST
  API calls.
hideListLinks: true
linkTitle: Requests
weight: 30
url: '/operate/rs/8.0/references/rest-api/requests/'
---

A REST API request requires the following components:
- [HTTP method](https://restfulapi.net/http-methods/) (`GET`, `PUT`, `PATCH`, `POST`, `DELETE`)
- Base URL
- Endpoint

Some requests may also require:
- URL parameters
- [Query parameters](https://en.wikipedia.org/wiki/Query_string)
- [JSON](http://www.json.org) request body
- [Permissions]({{< relref "/operate/rs/8.0/references/rest-api/permissions" >}})

{{< table-children columnNames="Request,Description" columnSources="LinkTitle,Description" enableLinks="LinkTitle" >}}
