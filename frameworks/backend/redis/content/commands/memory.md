---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/memory.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

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
description: A container for memory diagnostics commands.
group: server
hidden: true
linkTitle: MEMORY
railroad_diagram: /images/railroad/memory.svg
since: 4.0.0
summary: A container for memory diagnostics commands.
syntax_fmt: MEMORY
title: MEMORY
---
This is a container command for memory introspection and management commands.

To see the list of available commands you can call [`MEMORY HELP`]({{< relref "/commands/memory-help" >}}).
