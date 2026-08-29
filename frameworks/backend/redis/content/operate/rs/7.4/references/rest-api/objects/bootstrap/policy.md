---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/references/rest-api/objects/bootstrap/policy.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.786762Z"
---
# Policy

---
Title: Policy object
alwaysopen: false
categories:
- docs
- operate
- rs
description: Documents the policy object used with Redis Enterprise Software REST
  API calls.
linkTitle: policy
weight: $weight
url: '/operate/rs/7.4/references/rest-api/objects/bootstrap/policy/'
---

| Name | Type/Value | Description |
|------|------------|-------------|
| default_fork_evict_ram | boolean (default:&nbsp;false) | If true, the databases should evict data from RAM to ensure successful replication or persistence |
| default_non_sharded_proxy_policy | **'single'** <br />'all-master-shards'<br />'all-nodes' | Default proxy_policy for newly created non-sharded databases' endpoints |
| default_sharded_proxy_policy | 'single'<br /> **'all-master-shards'** <br />'all-nodes' | Default proxy_policy for newly created sharded databases' endpoints |
| default_shards_placement | 'dense'<br /> **'sparse'** | Default shards_placement for newly created databases |
| rack_aware | boolean | Cluster rack awareness |
| shards_overbooking | boolean (default:&nbsp;true) | If true, all databases' memory_size settings are ignored during shards placement |
