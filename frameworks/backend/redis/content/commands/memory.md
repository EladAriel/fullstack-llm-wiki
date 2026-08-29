---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/memory.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.075298Z"
---
# Memory

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
