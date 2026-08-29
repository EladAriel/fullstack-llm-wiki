---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/client.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.064110Z"
---
# Client

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
description: A container for client connection commands.
group: connection
hidden: true
linkTitle: CLIENT
railroad_diagram: /images/railroad/client.svg
since: 2.4.0
summary: A container for client connection commands.
syntax_fmt: CLIENT
title: CLIENT
---
This is a container command for client connection commands.

To see the list of available commands you can call [`CLIENT HELP`]({{< relref "/commands/client-help" >}}).