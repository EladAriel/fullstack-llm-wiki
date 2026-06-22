---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/hotkeys-help.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
acl_categories:
- '@admin'
arity: 2
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
command_flags:
- loading
- stale
complexity: O(1)
container: HOTKEYS
description: Returns helpful text about HOTKEYS commands and parameters.
function: hotkeysCommand
group: server
hidden: true
linkTitle: HOTKEYS HELP
railroad_diagram: /images/railroad/hotkeys-help.svg
reply_schema:
  description: Helpful text about subcommands.
  items:
    type: string
  type: array
since: 8.6.1
summary: Returns helpful text about HOTKEYS commands and parameters.
syntax_fmt: HOTKEYS HELP
title: HOTKEYS HELP
---

Returns helpful text about `HOTKEYS` commands and parameters.

## Return information

{{< multitabs id="return-info"
    tab1="RESP2"
    tab2="RESP3" >}}

Returns an [array reply]({{< relref "/develop/reference/protocol-spec#arrays" >}}) with the list of `HOTKEYS` subcommands and their descriptions.

-tab-sep-

Returns an [array reply]({{< relref "/develop/reference/protocol-spec#arrays" >}}) with the list of `HOTKEYS` subcommands and their descriptions.

{{< /multitabs >}}
