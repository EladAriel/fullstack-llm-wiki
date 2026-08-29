---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/command-count.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.044543Z"
---
# Command Count

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
- loading
- stale
complexity: O(1)
description: Returns a count of commands.
group: server
hidden: false
linkTitle: COMMAND COUNT
railroad_diagram: /images/railroad/command-count.svg
since: 2.8.13
summary: Returns a count of commands.
syntax_fmt: COMMAND COUNT
title: COMMAND COUNT
---
Returns [Integer reply]({{< relref "/develop/reference/protocol-spec#integers" >}}) of number of total commands in this Redis server.

## Examples

{{% redis-cli %}}
redis> COMMAND COUNT
(integer) 447
{{% /redis-cli %}}

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="command-count-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

[Integer reply](../../develop/reference/protocol-spec#integers): the number of commands returned by `COMMAND`.

-tab-sep-

[Integer reply](../../develop/reference/protocol-spec#integers): the number of commands returned by `COMMAND`.

{{< /multitabs >}}
