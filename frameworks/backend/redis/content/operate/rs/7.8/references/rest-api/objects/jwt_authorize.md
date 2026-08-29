---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/rest-api/objects/jwt_authorize.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.478785Z"
---
# Jwt_Authorize

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
