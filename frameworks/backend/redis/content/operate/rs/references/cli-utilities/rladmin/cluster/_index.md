---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/cli-utilities/rladmin/cluster/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: rladmin cluster
alwaysopen: false
categories:
- docs
- operate
- rs
description: Manage cluster.
headerRange: '[1-2]'
hideListLinks: true
linkTitle: cluster
toc: 'true'
weight: $weight
---

Manages cluster configuration and administration. Most `rladmin cluster` commands are only for clusters that are already configured, while a few others are only for new clusters that have not been configured.

## Commands for configured clusters

{{<table-children columnNames="Command,Description" columnSources="linkTitle,Description" enableLinks="linkTitle" limitTags="configured">}}

## Commands for non-configured clusters

{{<table-children columnNames="Command,Description" columnSources="linkTitle,Description" enableLinks="linkTitle" limitTags="non-configured">}}
