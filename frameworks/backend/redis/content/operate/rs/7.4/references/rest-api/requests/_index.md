---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/references/rest-api/requests/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.754725Z"
---
# _Index

---
Title: Redis Enterprise REST API requests
alwaysopen: false
categories:
- docs
- operate
- rs
description: Documents the requests supported by the Redis Enterprise Software REST
  API calls.
hideListLinks: true
linkTitle: Requests
weight: 30
url: '/operate/rs/7.4/references/rest-api/requests/'
---

A REST API request requires the following components:
- [HTTP method](https://restfulapi.net/http-methods/) (`GET`, `PUT`, `PATCH`, `POST`, `DELETE`)
- Base URL
- Endpoint

Some requests may also require:
- URL parameters
- [Query parameters](https://en.wikipedia.org/wiki/Query_string)
- [JSON](http://www.json.org) request body
- [Permissions]({{< relref "/operate/rs/7.4/references/rest-api/permissions" >}})

{{< table-children columnNames="Request,Description" columnSources="LinkTitle,Description" enableLinks="LinkTitle" >}}
