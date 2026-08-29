---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/script.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.006133Z"
---
# Script

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
