---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/cluster.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.002482Z"
---
# Cluster

---
acl_categories:
- '@slow'
arity: -2
categories:
- docs
- develop
- stack
- oss
- rs
- rc
- oss
- kubernetes
- clients
complexity: Depends on subcommand.
description: A container for Redis Cluster commands.
group: cluster
hidden: true
linkTitle: CLUSTER
railroad_diagram: /images/railroad/cluster.svg
since: 3.0.0
summary: A container for Redis Cluster commands.
syntax_fmt: CLUSTER
title: CLUSTER
---
This is a container command for Redis Cluster commands.

To see the list of available commands you can call [`CLUSTER HELP`]({{< relref "/commands/cluster-help" >}}).
