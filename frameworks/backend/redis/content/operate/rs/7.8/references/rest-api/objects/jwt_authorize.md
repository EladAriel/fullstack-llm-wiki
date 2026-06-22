---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/rest-api/objects/jwt_authorize.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: JWT authorize object
alwaysopen: false
categories:
- docs
- operate
- rs
description: An object for user authentication or a JW token refresh request
linkTitle: jwt_authorize
weight: $weight
url: '/operate/rs/7.8/references/rest-api/objects/jwt_authorize/'
---

An API object for user authentication or a JW token refresh request.

| Name | Type/Value | Description |
|------|------------|-------------|
| password | string | The user’s password (required) |
| ttl | integer (range: 1-86400) (default: 300) | Time to live - The amount of time in seconds the token will be valid |
| username | string | The user’s username (required) |
