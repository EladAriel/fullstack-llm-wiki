---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/databases/active-active/develop/data-types/json.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: JSON in Active-Active databases
alwaysopen: false
categories:
- docs
- operate
- rs
- rc
description: Information about using JSON with an Active-Active database.
linkTitle: JSON
weight: $weight
tocEmbedHeaders: true
url: '/operate/rs/7.4/databases/active-active/develop/data-types/json/'
---
Active-Active databases support JSON data structures.

The design is based on [A Conflict-Free Replicated JSON Datatype](https://arxiv.org/abs/1608.03960) by Kleppmann and Beresford, but the implementation includes some changes. Several [conflict resolution rule](#conflict-resolution-rules) examples were adapted from this paper as well.

## Prerequisites

To use JSON in an Active-Active database, you must enable JSON during database creation.

Active-Active Redis Cloud databases add JSON by default. See [Create an Active-Active subscription]({{< relref "/operate/rc/databases/active-active/create-active-active-database#select-capabilities" >}}) in the Redis Cloud documentation for details.

In Redis Enterprise Software, JSON is not enabled by default for Active-Active databases. See [Create an Active-Active JSON database]({{< relref "/operate/oss_and_stack/stack-with-enterprise/json/active-active#create-an-active-active-json-database" >}}) in the Redis Stack and Redis Enterprise documentation for instructions.

{{<embed-md "json-active-active-command-differences.md">}}

{{<embed-md "json-active-active-conflict-resolution.md">}}
