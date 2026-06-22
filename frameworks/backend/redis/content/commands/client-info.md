---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/client-info.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
acl_categories:
- '@slow'
- '@connection'
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
- noscript
- loading
- stale
complexity: O(1)
description: Returns information about the connection.
group: connection
hidden: false
hints:
- nondeterministic_output
linkTitle: CLIENT INFO
railroad_diagram: /images/railroad/client-info.svg
since: 6.2.0
summary: Returns information about the connection.
syntax_fmt: CLIENT INFO
title: CLIENT INFO
---
The command returns information and statistics about the current client connection in a mostly human readable format.

The reply format is identical to that of [`CLIENT LIST`]({{< relref "/commands/client-list" >}}), and the content consists only of information about the current client.

## Examples

{{% redis-cli %}}
CLIENT INFO
{{% /redis-cli %}}

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="client-info-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

[Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): a unique string for the current client, as described at the `CLIENT LIST` page.

-tab-sep-

[Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): a unique string for the current client, as described at the `CLIENT LIST` page.

{{< /multitabs >}}
