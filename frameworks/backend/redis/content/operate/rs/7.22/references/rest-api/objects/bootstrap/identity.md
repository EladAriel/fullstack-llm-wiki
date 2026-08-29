---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/rest-api/objects/bootstrap/identity.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.416036Z"
---
# Identity

---
Title: Identity object
alwaysopen: false
categories:
- docs
- operate
- rs
description: Documents the identity object used with Redis Enterprise Software REST
  API calls.
linkTitle: identity
weight: $weight
url: '/operate/rs/7.22/references/rest-api/objects/bootstrap/identity/'
---

| Name | Type/Value | Description |
|------|------------|-------------|
| uid | integer | Assumed node's UID to join cluster. Used to replace a dead node with a new one. |
| accept_servers | boolean (default:&nbsp;true) | If true, no shards will be created on the node |
| addr | string | Internal IP address of node |
| external_addr | complex object | External IP addresses of node. `GET`&nbsp;`/jsonschema` to retrieve the object's structure. |
| name | string | Node's name |
| override_rack_id | boolean | When replacing an existing node in a rack-aware cluster, allows the new node to be located in a different rack |
| rack_id | string | Rack ID, overrides cloud config |
| second_rack_id | string | Second rack ID where node is installed |
| use_internal_ipv6 | boolean (default:&nbsp;false) | Node uses IPv6 for internal communication |
