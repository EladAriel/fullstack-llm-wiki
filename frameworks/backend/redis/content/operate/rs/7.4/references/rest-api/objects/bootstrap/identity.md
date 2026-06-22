---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/references/rest-api/objects/bootstrap/identity.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

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
url: '/operate/rs/7.4/references/rest-api/objects/bootstrap/identity/'
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
| use_internal_ipv6 | boolean (default:&nbsp;false) | Node uses IPv6 for internal communication |
