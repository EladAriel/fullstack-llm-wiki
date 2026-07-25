---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/rest-api/objects/jwt_authorize.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
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
---

An API object for user authentication or a JW token refresh request.

| Name | Type/Value | Description |
|------|------------|-------------|
| password | string | The user’s password (required) |
| ttl | integer (range: 1-86400) (default: 300) | Time to live - The amount of time in seconds the token will be valid |
| username | string | The user’s username (required) |
