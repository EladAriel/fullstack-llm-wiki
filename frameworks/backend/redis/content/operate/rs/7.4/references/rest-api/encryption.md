---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/references/rest-api/encryption.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Encrypt REST API requests
alwaysopen: false
categories:
- docs
- operate
- rs
description: null
linkTitle: Encrypt requests
weight: 30
url: '/operate/rs/7.4/references/rest-api/encryption/'
---

## Require HTTPS for API endpoints

By default, the Redis Enterprise Software API supports communication over HTTP and HTTPS. However, you can turn off support for HTTP to ensure that API requests are encrypted.

Before you turn off HTTP support, be sure to migrate any scripts or proxy configurations that use HTTP to the encrypted API endpoint to prevent broken connections.

To turn off HTTP support for API endpoints, run:

```sh
rladmin cluster config http_support disabled
```
