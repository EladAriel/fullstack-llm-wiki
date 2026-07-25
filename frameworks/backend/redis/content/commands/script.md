---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/script.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
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
description: A container for Lua scripts management commands.
group: scripting
hidden: true
linkTitle: SCRIPT
railroad_diagram: /images/railroad/script.svg
since: 2.6.0
summary: A container for Lua scripts management commands.
syntax_fmt: SCRIPT
title: SCRIPT
---
This is a container command for script management commands.

To see the list of available commands you can call [`SCRIPT HELP`]({{< relref "/commands/script-help" >}}).
