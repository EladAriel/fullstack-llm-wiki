---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/references/rest-api/objects/module_metadata.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Module metadata object
alwaysopen: false
categories:
- docs
- operate
- rs
description: An object that represents Redis module metadata
linkTitle: module_metadata
weight: $weight
url: '/operate/rs/7.4/references/rest-api/objects/module_metadata/'
---

Represents a [Redis module]({{< relref "/operate/oss_and_stack/stack-with-enterprise" >}}).

| Name | Type/Value | Description |
|------|------------|-------------|
| uid | string | Cluster unique ID of module |
| architecture | string | Module was compiled under this architecture |
| author | string | Module creator |
| capabilities | array of strings | List of capabilities supported by this module |
| capability_name | string | Short description of module functionality |
| command_line_args | string | Command-line arguments passed to the module |
| config_command | string | Name of command to configure module arguments at runtime |
| crdb | CRDB object | CRDB-related information about the module<br />CRDB object fields:<br />**name**: string<br />**supported_featureset_versions**: array of integers |
| dependencies | dependencies object | Module dependencies |
| description | string | Short description of the module |
| display_name | string | Name of module for display purposes |
| email | string | Author's email address |
| homepage | string | Module's homepage |
| license | string | Module is distributed under this license |
| min_redis_pack_version | string | Minimum Redis Enterprise Software cluster version required by this module |
| min_redis_version | string | Minimum Redis database version required by this module |
| module_file | string | Module filename |
| module_name | string | Module's name |
| semantic_version | string | Module's semantic version |
| sha256 | string | SHA256 of module binary |
| version | integer | Module's version |
