---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/echo.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
acl_categories:
- '@fast'
- '@connection'
arguments:
- display_text: message
  name: message
  type: string
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
- fast
complexity: O(1)
description: Returns the given string.
group: connection
hidden: false
linkTitle: ECHO
railroad_diagram: /images/railroad/echo.svg
since: 1.0.0
summary: Returns the given string.
syntax_fmt: ECHO message
title: ECHO
---
Returns `message`.

## Required arguments

<details open><summary><code>message</code></summary>

The message to echo back.

</details>

## Examples

{{% redis-cli %}}
redis> ECHO "Hello World!"
"Hello World!"
{{% /redis-cli %}}

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="echo-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

[Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the given string.

-tab-sep-

[Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the given string.

{{< /multitabs >}}
