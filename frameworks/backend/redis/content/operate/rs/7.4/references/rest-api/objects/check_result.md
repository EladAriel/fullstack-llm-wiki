---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/references/rest-api/objects/check_result.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Check result object
alwaysopen: false
categories:
- docs
- operate
- rs
description: An object that contains the results of a cluster check
linkTitle: check_result
weight: $weight
url: '/operate/rs/7.4/references/rest-api/objects/check_result/'
---

Cluster check result

| Name | Type/Value | Description |
|------|------------|-------------|
| cluster_test_result | boolean | Indication if any of the tests failed |
| nodes | {{<code>}}
[{
  "node_uid": integer,
  "result": boolean,
  "error": string
}, ...]
{{</code>}} | Nodes results |
