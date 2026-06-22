---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/script.md"
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
