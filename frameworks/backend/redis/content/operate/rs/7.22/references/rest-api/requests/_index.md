---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/rest-api/requests/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

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
url: '/operate/rs/7.22/references/rest-api/requests/'
---

A REST API request requires the following components:
- [HTTP method](https://restfulapi.net/http-methods/) (`GET`, `PUT`, `PATCH`, `POST`, `DELETE`)
- Base URL
- Endpoint

Some requests may also require:
- URL parameters
- [Query parameters](https://en.wikipedia.org/wiki/Query_string)
- [JSON](http://www.json.org) request body
- [Permissions]({{< relref "/operate/rs/7.22/references/rest-api/permissions" >}})

{{< table-children columnNames="Request,Description" columnSources="LinkTitle,Description" enableLinks="LinkTitle" >}}
