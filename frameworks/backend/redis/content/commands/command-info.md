---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/command-info.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
acl_categories:
- '@slow'
- '@connection'
arguments:
- display_text: command-name
  multiple: true
  name: command-name
  optional: true
  type: string
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
command_flags:
- loading
- stale
complexity: O(N) where N is the number of commands to look up
description: Returns information about one, multiple or all commands.
group: server
hidden: false
hints:
- nondeterministic_output_order
history:
- - 7.0.0
  - Allowed to be called with no argument to get info on all commands.
linkTitle: COMMAND INFO
railroad_diagram: /images/railroad/command-info.svg
since: 2.8.13
summary: Returns information about one, multiple or all commands.
syntax_fmt: COMMAND INFO [command-name [command-name ...]]
title: COMMAND INFO
---
Returns details about multiple Redis commands using the same format as [`COMMAND`]({{< relref "/commands/command" >}}), except you can specify which commands are inspected.

If you request details about non-existing commands, nil is returned.

## Optional arguments

<details open><summary><code>command-name [command-name ...]</code></summary>

One or more command names to return details for. If omitted, details for all commands are returned.

</details>

## Examples

{{% redis-cli %}}
COMMAND INFO get set eval
COMMAND INFO foo evalsha config bar
{{% /redis-cli %}}

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="command-info-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

[Array reply](../../develop/reference/protocol-spec#arrays): a nested list of command details.

-tab-sep-

[Array reply](../../develop/reference/protocol-spec#arrays): a nested list of command details.

{{< /multitabs >}}
